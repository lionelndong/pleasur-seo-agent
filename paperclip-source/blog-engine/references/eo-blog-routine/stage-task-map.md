# EO stage task map

This map is subordinate to `execution-contract.md` and uses the same stage numbering.

| Stage | Packet | Producing artifact | Deterministic gate |
|---|---|---|---|
| 01 | `01-candidate.md` | validated Ahrefs JSON + selection verdict | schema, provenance, freshness, conflict, intent, fit, Course Formula, vulnerability, cannibalization |
| 02 | `02-research.md` | `1-research/{slug}.md` | research + adversarial research gate |
| 03 | `03-reference.md` | `2-reference/{slug}.md` + author packet | product proof, Feature Fit Matrix, byline/CMS identity |
| 04 | `04-outline.md` | `3-outlines/{slug}.md` + `4-outlines-annotated/{slug}.md` | outline + adversarial outline gate |
| 05 | `05-draft.md` | `5-drafts/{slug}.md` | draft structure, v1 critique/v2 rewrite, author voice |
| 06 | `06-claims-links.md` | `6-drafts-cited/{slug}.md` + ledger | claim source, link resolution/support, placeholder scrub |
| 07 | `07-visuals.md` | `images/{slug}/manifest.json` + assets | manifest/file hashes, dimensions, alt, role mix, visual adversarial gate |
| 08 | `08-quality.md` | quality report, scorecard, trace | PASS >=85; all blocking gates |
| 09 | `09-preview-cms.md` | preview HTML + `8-publish/{slug}/article.json` | `validate_run_contract.py` with stages 01-09 |
| 10 | `10-terminal.md` | live audit or preview-only record | zero mutation in preview; full rendered-page audit in live |

The controller has exactly one current child. The parent's `blockedByIssueIds` contains that child while the parent remains `in_progress`. A terminal data/quarantine disposition closes both child and parent `done`, preserving the next schedule fire.

Accepted predecessor artifacts are immutable inputs. When a downstream gate identifies an upstream defect, record the exact `restartStage`; do not silently rewrite the lineage or claim earlier receipt hashes still apply.
