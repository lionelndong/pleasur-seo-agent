#!/usr/bin/env python3
"""Validate observable evidence for a PLE new-content run.

This validator is intentionally strict. It verifies receipt hashes, required
artifacts, editorial gates, visuals, and the CMS dry-run package. Exit 0 is
required before a live mutation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CP = ROOT / "content-pipeline"
HEX64 = re.compile(r"^[0-9a-f]{64}$")
RUNTIME_NAME = re.compile(r"^[a-z0-9][a-z0-9-]*--[0-9a-f]{10}$")
PRIVATE_MARKERS = re.compile(
    r":::nutshell|\{/?lead\}|\[(?:VISUAL|SCREENSHOT):|\[CITATION NEEDED\]|\bTODO\b|"
    r"PAPERCLIP_|DOPPLER_|OPENROUTER_|SEM[Rr]USH|DataForSEO",
    re.I,
)
MD_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.passes: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def ok(self, message: str) -> None:
        self.passes.append(message)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_artifact(value: str) -> Path:
    p = Path(value)
    return p if p.is_absolute() else ROOT / p


def load_json(path: Path, audit: Audit) -> dict | None:
    if not path.is_file():
        audit.fail(f"missing JSON: {path.relative_to(ROOT)}")
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        audit.fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return None
    if not isinstance(value, dict):
        audit.fail(f"JSON root must be an object: {path.relative_to(ROOT)}")
        return None
    return value


def validate_receipt(path: Path, expected_stage: str, run_key: str, slug: str, audit: Audit) -> None:
    receipt = load_json(path, audit)
    if receipt is None:
        return
    for key, expected in (("schemaVersion", 1), ("runKey", run_key), ("slug", slug), ("stage", expected_stage)):
        if receipt.get(key) != expected:
            audit.fail(f"{path.relative_to(ROOT)}: {key}={receipt.get(key)!r}, expected {expected!r}")
    if receipt.get("disposition") != "PASS":
        audit.fail(f"{path.relative_to(ROOT)}: disposition must be PASS for advancement")
    skills = receipt.get("skills")
    if not isinstance(skills, list) or not skills:
        audit.fail(f"{path.relative_to(ROOT)}: no skill evidence")
        return
    for i, skill in enumerate(skills):
        label = f"{path.relative_to(ROOT)} skills[{i}]"
        if not isinstance(skill, dict) or not skill.get("key") or not skill.get("runtimeName"):
            audit.fail(f"{label}: missing key/runtimeName")
            continue
        if not RUNTIME_NAME.fullmatch(str(skill["runtimeName"])):
            audit.fail(
                f"{label}: runtimeName must be the installed Paperclip runtime name, "
                "not a local skill path"
            )
        instruction_hash = skill.get("instructionSha256")
        if not isinstance(instruction_hash, str) or not HEX64.fullmatch(instruction_hash):
            audit.fail(f"{label}: invalid instructionSha256")
        decision_after = skill.get("decisionAfter")
        if not skill.get("changedDecision") and decision_after != "NOT_APPLICABLE":
            audit.fail(f"{label}: claimed skill neither changed a decision nor recorded NOT_APPLICABLE")
        for collection in ("inputs", "outputs"):
            entries = skill.get(collection)
            if not isinstance(entries, list) or not entries:
                audit.fail(f"{label}: {collection} must be a non-empty list")
                continue
            for entry in entries:
                validate_hashed_entry(entry, f"{label} {collection}", audit)
    gates = receipt.get("gates")
    if not isinstance(gates, list) or not gates:
        audit.fail(f"{path.relative_to(ROOT)}: no deterministic gate evidence")
    else:
        for gate in gates:
            if not isinstance(gate, dict) or not gate.get("command") or gate.get("exitCode") != 0 or gate.get("result") != "PASS":
                audit.fail(f"{path.relative_to(ROOT)}: gate did not record command/exitCode=0/result=PASS")
    artifacts = receipt.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        audit.fail(f"{path.relative_to(ROOT)}: no hashed artifacts")
    else:
        for entry in artifacts:
            validate_hashed_entry(entry, f"{path.relative_to(ROOT)} artifacts", audit)
    if not any(str(skill.get("decisionAfter", "")).strip() for skill in skills if isinstance(skill, dict)):
        audit.fail(f"{path.relative_to(ROOT)}: decisions are empty")
    if not audit.errors:
        audit.ok(f"receipt {expected_stage} verified")


def validate_hashed_entry(entry: object, label: str, audit: Audit) -> None:
    if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
        audit.fail(f"{label}: entry missing path")
        return
    path = resolve_artifact(entry["path"])
    expected = entry.get("sha256")
    if not path.is_file():
        audit.fail(f"{label}: missing {entry['path']}")
    elif not isinstance(expected, str) or not HEX64.fullmatch(expected):
        audit.fail(f"{label}: invalid SHA-256 for {entry['path']}")
    elif sha256(path) != expected:
        audit.fail(f"{label}: SHA-256 mismatch for {entry['path']}")


def validate_draft(slug: str, audit: Audit) -> str:
    path = CP / "6-drafts-cited" / f"{slug}.md"
    if not path.is_file():
        audit.fail(f"missing cited draft: {path.relative_to(ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8")
    if len(text.split()) < 900:
        audit.fail("cited draft is under 900 words")
    if not text.lstrip().startswith("# "):
        audit.fail("cited draft must start with H1 and contain no frontmatter")
    markers = sorted(set(m.group(0) for m in PRIVATE_MARKERS.finditer(text)))
    if markers:
        audit.fail(f"cited draft contains private/placeholder syntax: {', '.join(markers[:8])}")
    links = MD_LINK.findall(text)
    internal = [url for _, url in links if "pleasur.ai/" in url]
    external = [url for _, url in links if "pleasur.ai/" not in url]
    if len(set(internal)) < 2:
        audit.fail(f"need at least 2 distinct useful internal links; found {len(set(internal))}")
    if len(set(external)) < 2:
        audit.fail(f"need at least 2 distinct external citations; found {len(set(external))}")
    images = MD_IMAGE.findall(text)
    empty_alt = [target for alt, target in images if not alt.strip()]
    if empty_alt:
        audit.fail(f"{len(empty_alt)} markdown image(s) have empty alt text")
    audit.ok(f"draft: {len(text.split())} words, {len(set(internal))} internal links, {len(set(external))} external citations")
    return text


def validate_visuals(slug: str, audit: Audit) -> None:
    path = CP / "images" / slug / "manifest.json"
    manifest = load_json(path, audit)
    if manifest is None:
        return
    visuals = manifest.get("visuals")
    if not isinstance(visuals, list):
        audit.fail("visual manifest has no visuals list")
        return
    active = [v for v in visuals if isinstance(v, dict) and v.get("status") not in {"removed", "skipped"}]
    if len(active) < 4:
        audit.fail(f"visual package has only {len(active)} active assets; minimum is 4")
    types = {str(v.get("type") or v.get("role") or "").lower() for v in active}
    if len(types - {""}) < 2:
        audit.fail("visual package needs at least two useful visual types")
    for i, visual in enumerate(active):
        if visual.get("status") in {"manual", "failed", "pending"}:
            audit.fail(f"visual {i} unresolved: {visual.get('status')}")
        candidate = visual.get("path") or visual.get("file")
        if not candidate and isinstance(visual.get("result"), dict):
            candidate = visual["result"].get("path") or visual["result"].get("file")
        asset: Path | None = None
        if candidate:
            asset = resolve_artifact(str(candidate))
            if not asset.is_file():
                alternate = path.parent / str(candidate)
                if alternate.is_file():
                    asset = alternate
                else:
                    audit.fail(f"visual {i} points to missing asset: {candidate}")
                    asset = None
        else:
            audit.fail(f"visual {i} has no asset path")
        expected_hash = visual.get("sha256")
        if not isinstance(expected_hash, str) or not HEX64.fullmatch(expected_hash):
            audit.fail(f"visual {i} has no valid SHA-256")
        elif asset is not None and sha256(asset) != expected_hash:
            audit.fail(f"visual {i} SHA-256 does not match its asset")
        for dimension in ("width", "height"):
            value = visual.get(dimension)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                audit.fail(f"visual {i} has no positive integer {dimension}")
        alt = visual.get("alt") or visual.get("altText")
        if visual.get("decorative") is not True and not str(alt or "").strip():
            audit.fail(f"visual {i} has no meaningful alt text or decorative=true")
    audit.ok(f"visual manifest: {len(active)} active assets, {len(types - {''})} types")


def validate_quality(slug: str, audit: Audit) -> None:
    path = CP / "quality-checks" / f"{slug}.md"
    if not path.is_file():
        audit.fail(f"missing quality report: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8")
    verdict = re.search(r"Verdict:\s*\*\*(PASS|BORDERLINE|FAIL)\*\*", text, re.I)
    scores = [int(x) for x in re.findall(r"(?<!\d)(\d{2,3})\s*/\s*100", text)]
    if not verdict or verdict.group(1).upper() != "PASS":
        audit.fail("quality verdict is not PASS")
    if not scores or max(scores) < 85:
        audit.fail("quality report has no score >=85/100")
    for required in (CP / "scorecards" / f"{slug}.md", CP / "traces" / f"{slug}-skill-trace.md"):
        if not required.is_file() or required.stat().st_size < 200:
            audit.fail(f"missing/substantive quality evidence: {required.relative_to(ROOT)}")
    audit.ok(f"quality report parsed; top score={max(scores) if scores else 'missing'}")


def extract_payload_text(payload: dict) -> tuple[dict, str]:
    data = payload.get("data") if isinstance(payload.get("data"), dict) else payload
    bodies: list[str] = []
    for block in data.get("blocks", []) if isinstance(data.get("blocks"), list) else []:
        if isinstance(block, dict) and isinstance(block.get("body"), str):
            bodies.append(block["body"])
    for key in ("body", "content", "article"):
        if isinstance(data.get(key), str):
            bodies.append(data[key])
    return data, "\n".join(bodies)


def validate_cms(slug: str, audit: Audit) -> None:
    directory = CP / "8-publish" / slug
    payload_path = directory / "article.json"
    payload = load_json(payload_path, audit)
    if payload is None:
        return
    data, body = extract_payload_text(payload)
    for field in ("title", "slug", "description", "author", "cover", "category"):
        if data.get(field) in (None, "", []):
            audit.fail(f"CMS payload missing {field}")
    if data.get("slug") != slug:
        audit.fail(f"CMS payload slug {data.get('slug')!r} != {slug!r}")
    description = str(data.get("description") or "")
    if PRIVATE_MARKERS.search(description):
        audit.fail("CMS description contains component/private syntax")
    if len(description) < 80 or len(description) > 165:
        audit.fail(f"CMS description length {len(description)} is outside 80-165")
    if not body.strip():
        audit.fail("CMS payload has no article body")
    if body.lstrip().startswith(":::nutshell"):
        audit.fail("CMS body starts with :::nutshell; current live renderer leaks this into meta description")
    if re.search(r"\[(?:VISUAL|SCREENSHOT):|\[CITATION NEEDED\]|\bTODO\b", body, re.I):
        audit.fail("CMS body contains unresolved placeholder syntax")
    article_md = directory / "article.md"
    if not article_md.is_file() or article_md.stat().st_size < 1000:
        audit.fail("publish package missing substantive article.md")
    readme = directory / "README.md"
    if not readme.is_file():
        audit.fail("publish package missing README.md")
    audit.ok("CMS dry-run payload parsed with required identity, taxonomy, cover, and content fields")


def validate_preview(slug: str, audit: Audit) -> None:
    path = CP / "7-preview" / f"{slug}.html"
    if not path.is_file() or path.stat().st_size < 1000:
        audit.fail(f"preview HTML missing or too small: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if PRIVATE_MARKERS.search(text):
        audit.fail("preview exposes placeholder/private syntax")
    if not re.search(r"<h1\b", text, re.I):
        audit.fail("preview has no H1")
    audit.ok(f"preview HTML present ({path.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--run-key", required=True)
    parser.add_argument("--mode", choices=("preview", "live"), required=True)
    parser.add_argument("--required-stages", default="01,02,03,04,05,06,07,08,09")
    args = parser.parse_args()
    stages = [s.strip().zfill(2) for s in args.required_stages.split(",") if s.strip()]
    audit = Audit()
    receipt_dir = CP / "stage-receipts" / args.run_key
    for stage in stages:
        validate_receipt(receipt_dir / f"{stage}.json", stage, args.run_key, args.slug, audit)
    if any(stage in stages for stage in ("05", "06", "07", "08", "09")):
        validate_draft(args.slug, audit)
    if any(stage in stages for stage in ("07", "08", "09")):
        validate_visuals(args.slug, audit)
    if any(stage in stages for stage in ("08", "09")):
        validate_quality(args.slug, audit)
    if "09" in stages:
        validate_preview(args.slug, audit)
        validate_cms(args.slug, audit)

    print(json.dumps({
        "verdict": "PASS" if not audit.errors else "FAIL",
        "mode": args.mode,
        "slug": args.slug,
        "runKey": args.run_key,
        "requiredStages": stages,
        "passes": audit.passes,
        "errors": audit.errors,
    }, indent=2))
    return 0 if not audit.errors else 1


if __name__ == "__main__":
    sys.exit(main())
