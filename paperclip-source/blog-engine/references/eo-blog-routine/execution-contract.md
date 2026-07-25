# EO new-content execution contract

Version: 2026-07-17. This is the single authoritative execution contract for the PLE new-content routine. If another workspace or agent instruction conflicts with this file, this file wins for routine-generated work.

## Scope and cadence

- PLE only: company `d11fb003-42e2-4b84-8d88-e1242ad09a70`.
- New blog content only. Do not run existing-content portfolio improvement, relaunch, or measurement work here.
- Schedule: Monday, Tuesday, Thursday, Friday at 09:00 America/New_York.
- A fire is an attempt, not a publish quota. Maximum one public article per fire and four per calendar week.
- `preview_only` forbids all Strapi and public mutations.
- Ahrefs is the only SEO-metrics source. The enabled lane is board-supplied/browser-exported Ahrefs evidence. Do not call Ahrefs, Semrush, DataForSEO, OpenRouter, or paid APIs from this routine.

## Precedence and controller behavior

The routine issue is a controller. It creates exactly one direct child for the current stage and blocks on that child while remaining `in_progress`. A child never creates or wakes its successor. On PASS it writes its receipt, comments a structured handoff, and closes `done`; the controller validates the receipt before creating the next child.

Missing external evidence must not strand the schedule. The current child writes one exact `DATA_REQUIRED` artifact and comment, then closes `done` with `stageDisposition=NO_PUBLISH_DATA_REQUIRED`. The controller closes `done` with the same controlled no-publish disposition. The artifact must name the exact Ahrefs report, country, filters, fields, freshness, and acceptable attachment formats. Never request credentials. A later fire may consume the supplied evidence. Do not leave the routine parent or child in `in_review`, `blocked`, or otherwise active while waiting for a human.

After two failures at the same producing gate, quarantine the run and close it `done` as `NO_PUBLISH_QUARANTINED`. A later fire starts independently. Never interpret a controlled no-publish as a quality PASS or public publish.

## Evidence packet

Candidate selection must precede drafting. A broad packet may be reused for 30 days; the selected candidate's overview and SERP packet must be no older than 14 days.

Required candidate evidence:

- keyword, country, volume, KD, traffic potential or parent topic, intent, trends, SERP features, and observed/updated time;
- Matching terms, Related terms, Search suggestions, and Questions, or an explicit Ahrefs-unavailable marker for an individual report;
- ten distinct typed SERP rows with position, result type, URL, title, DR, UR when available, referring domains, traffic, ranking keywords, and feature membership;
- current Pleasur DR/site ceiling and current-site cannibalization evidence;
- product fit, Business Value, search intent, demand, Course Formula, information-gain asset, named weak URLs, and backlink/content displacement plan.

Conflicting numbers remain conflicts until resolved from provenance. Never average or silently choose one. GO requires all evidence plus a documented kill-rule pass. No candidate passes on KD alone.

## Canonical stages

| Stage | Work | Required skills | Primary outputs |
|---|---|---|---|
| 01 | Candidate + Ahrefs validation | `keyword-prioritization`, `keyword-vet-bid`, `keyword-vet-aio` | validated Ahrefs JSON, `01-candidate.md` |
| 02 | Intent, SERP, research, information gain | `research`, `content-gap-analysis`, `contagious-why-things-catch-on` | research dossier, BEAT SPEC, `02-research.md` |
| 03 | Product truth, author voice/byline, references | `brand-reference`, `product-mentions` | reference packet, Feature Fit Matrix, author packet |
| 04 | Outline, internal links, visual plan | `outline`, `oversubscribed` | outline, annotated outline, Article Promise, visual roles |
| 05 | Draft v1 critique + v2 rewrite | `draft`, `update-draft` | substantive v2 draft |
| 06 | Claims, citations, product proof, links | `verify-claims`, `update-claims`, `update-product-mentions` | cited draft and claim/link ledger |
| 07 | Useful original visuals | `generate-visuals` | cover/OG, in-article assets, visual manifest |
| 08 | Adversarial editorial/policy gate | `quality-check`, `contagious-why-things-catch-on`, `oversubscribed` | scorecard, trace, punch list or PASS |
| 09 | Preview + CMS dry-run | `preview`, `format-for-publish` | preview HTML, CMS payload, dry-run report |
| 10 | Publish/live verification or preview terminal | `format-for-publish`, `preview` | live audit or explicit zero-publish terminal record |

Stage 10 may publish only in `quality_gated_live` after Stages 01-09 validate. In `preview_only`, Stage 10 records `PREVIEW_ONLY_COMPLETE`, public-publish count 0, and makes no external request.

## Observable skill receipt

Every stage writes `content-pipeline/stage-receipts/{run-key}/{stage}.json`. A receipt is evidence, not prose. It must contain:

```json
{
  "schemaVersion": 1,
  "runKey": "PLE-0000-slug",
  "slug": "slug",
  "parentIssueId": "uuid",
  "stage": "01",
  "skills": [{
    "key": "keyword-prioritization",
    "runtimeName": "installed runtime name",
    "instructionSha256": "64 lowercase hex",
    "inputs": [{"path": "relative/path", "sha256": "64 lowercase hex"}],
    "outputs": [{"path": "relative/path", "sha256": "64 lowercase hex"}],
    "decisionBefore": "candidate",
    "decisionAfter": "GO|KILL|DATA_REQUIRED",
    "changedDecision": true
  }],
  "gates": [{"command": "exact command", "exitCode": 0, "result": "PASS"}],
  "artifacts": [{"path": "relative/path", "sha256": "64 lowercase hex"}],
  "disposition": "PASS",
  "nextStage": "02"
}
```

The skill list must contain every required skill for that stage. `instructionSha256` is the hash of the instruction actually read. Every input/output/artifact path must exist and its hash must match. A claimed skill with no receipt, unchanged decision, or unverifiable artifact fails closed. Conditional skills may record `changedDecision=false` only with `decisionAfter=NOT_APPLICABLE` and a concrete applicability reason.

## Editorial and product gates

All of these are blocking:

- dominant search intent is explicit and the opening answers it immediately;
- information gain is a concrete original asset, test, framework, dataset, screenshot, chart, or analysis--not a claim of uniqueness;
- Business Value is at least 2 and the conversion path matches a real reader job;
- product statements map to current proof; pricing, privacy, safety, platform, media, memory, and moderation claims are source-verified or removed;
- named author, voice packet, byline, author ID/profile, and CMS author field agree;
- at least one useful original cover/OG asset and enough in-article visuals for the article's length; every image exists, loads, has meaningful alt text unless intentionally decorative, and supports a reader decision;
- material factual claims have proximate authoritative citations; links resolve and support their sentence;
- at least two useful internal links, with anchor and destination relevant to the reader job;
- no placeholders, YAML frontmatter, hidden editor syntax, internal stack names, secrets, or PII;
- adversarial comparison against the best result and the strongest plausible alternative;
- deterministic score is PASS and at least 85. BORDERLINE never publishes.

## CMS and rendered-page gate

Before any public mutation run:

`python scripts/validate_run_contract.py --slug {slug} --run-key {run-key} --mode live`

The CMS payload must have the expected slug, title, clean description, body, cover, category, and author. It must not contain raw `:::nutshell`, `{lead}`, `[VISUAL:...]`, `TODO`, or other private pipeline syntax in metadata or unsupported fields. The article body may use only component syntax known to be supported by the current renderer.

After publish, verify the public URL directly:

- HTTP 200 and canonical URL;
- expected H1, title, and clean meta description (no component markup, truncation artifact, or wrong source field);
- expected named byline and author profile;
- cover/OG and all in-article images load with non-zero dimensions and correct alt handling;
- citations, internal links, and CTA resolve;
- desktop and mobile first view are usable;
- no placeholders, unsupported components, or internal implementation terms are visible.

Any live mismatch is a failed Stage 10. Do not call it PASS. If a safe rollback is part of the approved existing publish mechanism, use it; otherwise report one precise actionable blocker and stop.

## Required terminal record

The controller's final comment and run manifest must include: disposition; variable snapshot; all child issue IDs; receipt and artifact paths; candidate and intent verdicts; Article Promise and information-gain asset; author/byline; product proof; visual counts/types; claim and link results; score; CMS dry-run/live audit result; public-publish count 0 or 1; exact restart stage or data request; and confirmation that no separate existing-content routine was modified.
