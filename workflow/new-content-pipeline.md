# New-content pipeline

## Controller contract

The controller owns one run and allows one active stage at a time. A stage worker writes its artifact and receipt, reports a terminal decision, and never starts the successor. The controller verifies the receipt before advancing.

Cadence: Monday, Tuesday, Thursday, Friday at 9:00 AM Eastern. Maximum one public article per run and four per week.

| # | Stage | Artifact | Decision |
|---|---|---|---|
| 01 | Candidate validation | evidence packet and candidate brief | `GO`, `KILL`, `DATA_REQUIRED` |
| 02 | Intent, SERP, research | research dossier and BEAT SPEC | `RESEARCH_ACCEPTED` |
| 03 | Product and author truth | Feature Fit Matrix and author packet | `REFERENCE_ACCEPTED` |
| 04 | Outline and plan | annotated outline and Article Promise | `OUTLINE_ACCEPTED` |
| 05 | Draft and rewrite | substantive v2 draft | `DRAFT_ACCEPTED` |
| 06 | Claims and links | cited draft and claim/link ledger | `CITED_DRAFT_ACCEPTED` |
| 07 | Visual package | assets and manifest | `VISUALS_ACCEPTED` |
| 08 | Quality gate | scorecard and adversarial verdict | `PASS_85_PLUS` |
| 09 | Preview and CMS dry run | preview and validated payload | `DRY_RUN_PASS` |
| 10 | Publish and audit | public audit or zero-publish record | `PUBLISHED_VERIFIED` or `PREVIEW_ONLY_COMPLETE` |

## Failure rules

- Missing or stale evidence produces an exact evidence request and ends the run as `NO_PUBLISH_DATA_REQUIRED`.
- After two failures at the same producing gate, end the run as `NO_PUBLISH_QUARANTINED` with failed criteria and restart stage.
- Never treat a controlled no-publish outcome as a pass.
- Preview mode makes no public mutation.
