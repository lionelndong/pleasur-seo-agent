#!/usr/bin/env python3
"""Validate and normalize a manually supplied Ahrefs JSON artifact.

The manual bridge intentionally accepts only a strict JSON shape here. CSV/XLSX/Markdown
exports must first be converted to this shape by the stage agent, preserving the original
artifact path in the stage packet.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

OVERVIEW_FIELDS = {
    "keyword",
    "country",
    "volume",
    "kd",
    "trafficPotential",
    "parentTopic",
    "cpc",
    "updatedAt",
    "intents",
    "serpFeatures",
}
SERP_FIELDS = {
    "position",
    "resultType",
    "url",
    "title",
    "dr",
    "ur",
    "referringDomains",
    "backlinks",
    "estimatedTraffic",
    "rankingKeywords",
    "serpFeatures",
    "updatedAt",
}
RELATED_FIELDS = {"keyword", "volume", "kd", "parentTopic"}
PROVENANCE_FIELDS = {
    "packetLocator",
    "boardLocator",
    "packetSha256",
    "sourceDate",
    "snapshotDate",
    "collectedDate",
}
NUMERIC_FIELDS = {
    "volume",
    "kd",
    "trafficPotential",
    "cpc",
    "position",
    "dr",
    "ur",
    "referringDomains",
    "backlinks",
    "estimatedTraffic",
    "rankingKeywords",
}


class ValidationError(ValueError):
    pass


def require_fields(record: dict[str, Any], fields: set[str], location: str) -> None:
    missing = sorted(fields - record.keys())
    if missing:
        raise ValidationError(f"{location}: missing fields: {', '.join(missing)}")


def require_number(value: Any, location: str, *, nullable: bool = False) -> None:
    if value is None and nullable:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValidationError(f"{location}: expected number{' or null' if nullable else ''}")
    if value < 0:
        raise ValidationError(f"{location}: expected non-negative number")


def require_text(value: Any, location: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{location}: expected non-empty text")


def parse_date(value: Any, location: str) -> dt.date:
    require_text(value, location)
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{location}: expected YYYY-MM-DD") from exc


def parse_date_or_timestamp(value: Any, location: str) -> dt.date:
    require_text(value, location)
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError as exc:
        raise ValidationError(f"{location}: expected ISO date or timestamp") from exc


def require_string_array(value: Any, location: str) -> None:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValidationError(f"{location}: expected string array")


def reject_sensitive_text(data: dict[str, Any]) -> None:
    text = json.dumps(data, ensure_ascii=False)
    patterns = {
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "bearer token": r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}",
        "credential assignment": r"(?i)\b(?:api[_ -]?key|secret|password|token)\s*[:=]\s*[A-Za-z0-9._~+/=-]{16,}",
        "email address": r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "US phone number": r"(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)",
        "full customer identifier": r"\b(?:cus|person|distinct_id)_[A-Za-z0-9]{8,}\b",
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            raise ValidationError(f"sensitive-data scan: possible {label}")


def validate(
    data: dict[str, Any],
    *,
    expected_keyword: str,
    expected_country: str,
    observed_date: dt.date,
    max_age_days: int,
    allow_fixture: bool,
    expected_packet_sha256: str | None = None,
    expected_locator: str | None = None,
) -> dict[str, Any]:
    if data.get("fixture") is True and not allow_fixture:
        raise ValidationError("fixture artifact is smoke-test-only; pass --allow-fixture only in preview_only tests")

    source = data.get("source")
    require_text(source, "source")
    if "ahrefs" not in source.lower():
        raise ValidationError("source: must identify Ahrefs")

    provenance = data.get("provenance")
    if not isinstance(provenance, dict):
        raise ValidationError("provenance: expected object")
    require_fields(provenance, PROVENANCE_FIELDS, "provenance")
    for field in ("packetLocator", "boardLocator"):
        require_text(provenance[field], f"provenance.{field}")
    packet_sha256 = provenance["packetSha256"]
    if not isinstance(packet_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", packet_sha256):
        raise ValidationError("provenance.packetSha256: expected lowercase SHA-256")
    if expected_packet_sha256 and packet_sha256 != expected_packet_sha256.lower():
        raise ValidationError("provenance.packetSha256: does not match expected packet hash")
    if expected_locator and provenance["boardLocator"] != expected_locator:
        raise ValidationError("provenance.boardLocator: does not match expected board locator")
    for field in ("sourceDate", "snapshotDate", "collectedDate"):
        parse_date(provenance[field], f"provenance.{field}")

    overview = data.get("keywordOverview")
    if not isinstance(overview, dict):
        raise ValidationError("keywordOverview: expected object")
    require_fields(overview, OVERVIEW_FIELDS, "keywordOverview")
    require_text(overview["keyword"], "keywordOverview.keyword")
    require_text(overview["country"], "keywordOverview.country")
    if overview["keyword"].strip().casefold() != expected_keyword.strip().casefold():
        raise ValidationError("keywordOverview.keyword: does not match selected keyword")
    if overview["country"].strip().lower() != expected_country.strip().lower():
        raise ValidationError("keywordOverview.country: does not match target country")
    for field in ("volume", "kd", "trafficPotential"):
        require_number(overview[field], f"keywordOverview.{field}")
    require_number(overview["cpc"], "keywordOverview.cpc", nullable=True)
    require_text(overview["parentTopic"], "keywordOverview.parentTopic")
    require_string_array(overview["intents"], "keywordOverview.intents")
    require_string_array(overview["serpFeatures"], "keywordOverview.serpFeatures")
    updated_at = parse_date(overview["updatedAt"], "keywordOverview.updatedAt")
    age_days = (observed_date - updated_at).days
    if age_days < 0:
        raise ValidationError("keywordOverview.updatedAt: cannot be in the future")
    if age_days > max_age_days:
        raise ValidationError(
            f"keywordOverview.updatedAt: stale ({age_days} days; maximum {max_age_days})"
        )

    serp = data.get("serpTop10")
    if not isinstance(serp, list) or len(serp) != 10:
        raise ValidationError("serpTop10: expected exactly 10 rows")
    positions: list[int] = []
    dedupe_keys: set[tuple[str, int, str]] = set()
    for index, row in enumerate(serp, start=1):
        location = f"serpTop10[{index}]"
        if not isinstance(row, dict):
            raise ValidationError(f"{location}: expected object")
        require_fields(row, SERP_FIELDS, location)
        require_number(row["position"], f"{location}.position")
        for field in (SERP_FIELDS & NUMERIC_FIELDS) - {"position"}:
            require_number(row[field], f"{location}.{field}", nullable=True)
        positions.append(row["position"])
        require_text(row["resultType"], f"{location}.resultType")
        require_text(row["url"], f"{location}.url")
        parsed = urlparse(row["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValidationError(f"{location}.url: expected absolute http(s) URL")
        require_text(row["title"], f"{location}.title")
        require_string_array(row["serpFeatures"], f"{location}.serpFeatures")
        parse_date_or_timestamp(row["updatedAt"], f"{location}.updatedAt")
        dedupe_key = (row["url"], row["position"], row["resultType"].casefold())
        if dedupe_key in dedupe_keys:
            raise ValidationError(f"{location}: duplicate URL+position+type")
        dedupe_keys.add(dedupe_key)
    if positions != list(range(1, 11)):
        raise ValidationError("serpTop10.position: expected ordered positions 1 through 10")

    term_sections = data.get("termSections")
    if not isinstance(term_sections, dict):
        raise ValidationError("termSections: expected object")
    section_counts: dict[str, int] = {}
    for section in ("matching", "relatedAll", "relatedAlsoRankFor"):
        related = term_sections.get(section)
        if not isinstance(related, list) or not related:
            raise ValidationError(f"termSections.{section}: expected at least one row")
        section_counts[section] = len(related)
        for index, row in enumerate(related, start=1):
            location = f"termSections.{section}[{index}]"
            if not isinstance(row, dict):
                raise ValidationError(f"{location}: expected object")
            require_fields(row, RELATED_FIELDS, location)
            require_text(row["keyword"], f"{location}.keyword")
            if row["parentTopic"] is not None:
                require_text(row["parentTopic"], f"{location}.parentTopic")
            require_number(row["volume"], f"{location}.volume", nullable=True)
            require_number(row["kd"], f"{location}.kd", nullable=True)

    reject_sensitive_text(data)

    normalized = dict(data)
    normalized["validation"] = {
        "status": "PASS",
        "validatedAt": observed_date.isoformat(),
        "expectedKeyword": expected_keyword,
        "expectedCountry": expected_country.lower(),
        "freshnessDays": age_days,
        "maxAgeDays": max_age_days,
        "stage02MaximumAgeDays": 30,
        "packetSha256Verified": bool(expected_packet_sha256),
        "boardLocatorVerified": bool(expected_locator),
        "termSectionCounts": section_counts,
        "serpDedupeKey": "url+position+resultType",
        "secretPiiScan": "PASS",
        "restartStageOnFailure": "02",
    }
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--keyword", required=True)
    parser.add_argument("--country", default="us")
    parser.add_argument("--observed-date", type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument("--max-age-days", type=int, default=30)
    parser.add_argument("--allow-fixture", action="store_true")
    parser.add_argument("--expected-packet-sha256")
    parser.add_argument("--expected-locator")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.artifact.suffix.lower() != ".json":
        print(
            "FAIL restartStage=02: validator accepts normalized JSON only; convert the supplied export first",
            file=sys.stderr,
        )
        return 2
    try:
        data = json.loads(args.artifact.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValidationError("root: expected object")
        normalized = validate(
            data,
            expected_keyword=args.keyword,
            expected_country=args.country,
            observed_date=args.observed_date,
            max_age_days=args.max_age_days,
            allow_fixture=args.allow_fixture,
            expected_packet_sha256=args.expected_packet_sha256,
            expected_locator=args.expected_locator,
        )
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"FAIL restartStage=02: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(normalized, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS restartStage=03 "
        f"keyword={args.keyword!r} country={args.country.lower()} "
        f"serpRows={len(normalized['serpTop10'])} "
        f"matchingRows={len(normalized['termSections']['matching'])} "
        f"relatedAllRows={len(normalized['termSections']['relatedAll'])} "
        f"relatedAlsoRankForRows={len(normalized['termSections']['relatedAlsoRankFor'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
