# EO routine prompt map

The authoritative rules and schemas are in `execution-contract.md`. This file maps the canonical stage number to the instruction packet a controller must place on the child issue.

Every child description includes: Objective; Inputs; Output path; Acceptance criteria; Owner; Blocker dependency; Controller handoff; run key; slug; parent issue UUID; run mode; accepted input hashes; exact stage; and public-publish ceiling.

| Stage | Prompt objective | Required receipt decision |
|---|---|---|
| 01 | Validate board-supplied Ahrefs evidence and select or kill one candidate. No downstream work when evidence is incomplete or conflicting. | `GO`, `KILL`, or `DATA_REQUIRED` |
| 02 | Derive intent and BEAT SPEC from the accepted SERP; name weak pages and create a concrete information-gain asset plan. | `RESEARCH_ACCEPTED` or exact `restartStage` |
| 03 | Bind current product proof, Feature Fit Matrix, author voice, byline, profile, and CMS author identity. | `REFERENCE_ACCEPTED` or exact `restartStage` |
| 04 | Produce answer-first outline, Article Promise, internal-link plan, visual roles, and conditional Contagious/Oversubscribed decisions. | `OUTLINE_ACCEPTED` or exact `restartStage` |
| 05 | Critique v1 and write substantive v2 in the named author voice. | `DRAFT_ACCEPTED` or exact `restartStage` |
| 06 | Verify/remove material claims; validate citations, internal links, CTA, and product proof; scrub placeholders. | `CITED_DRAFT_ACCEPTED` or exact `restartStage` |
| 07 | Produce and verify useful original visuals, cover/OG, alt text, dimensions, and manifest/file consistency. | `VISUALS_ACCEPTED` or exact `restartStage` |
| 08 | Run deterministic and adversarial editorial/policy gates. Compare the strongest ranking result and alternative. | `PASS_85_PLUS` or exact `restartStage` |
| 09 | Render preview and build CMS payload without public mutation; run the contract validator. | `DRY_RUN_PASS` or exact `restartStage` |
| 10 | In preview mode, record zero-publish terminal result. In live mode only, validate, publish once, and audit the public page. | `PREVIEW_ONLY_COMPLETE`, `PUBLISHED_VERIFIED`, or `PUBLISH_FAILED` |

The child always writes `content-pipeline/stage-receipts/{run-key}/{stage}.json`, posts a structured handoff, and closes itself. It never creates or wakes its successor.

When evidence is missing, write `content-pipeline/data-requests/{run-key}.md` with the exact Ahrefs report/fields/freshness and close as `NO_PUBLISH_DATA_REQUIRED`. Do not leave a routine fire waiting in an active status.
