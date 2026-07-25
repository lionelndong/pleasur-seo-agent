# PLE blog pipeline

The canonical new-content pipeline is `references/eo-blog-routine/execution-contract.md`.

## New-content lane

- Cadence: Mon/Tue/Thu/Fri, 09:00 America/New_York.
- Ceiling: one public article per fire, four per week.
- Data: board-supplied/browser-exported Ahrefs evidence only; no agent API purchase or direct paid-provider calls.
- Orchestration: one routine controller and one direct current-stage child.
- Failure behavior: close the fire with `NO_PUBLISH_DATA_REQUIRED` or `NO_PUBLISH_QUARANTINED`; do not wait in an active state.
- Publishing: quality-gated live only after PASS >=85 and a successful CMS dry-run; preview mode is zero-public-mutation.

## Stage order

1. Candidate + Ahrefs validation
2. Intent/SERP research + information gain
3. Product truth + author/byline reference
4. Outline + internal links + visual plan
5. Draft critique and rewrite
6. Claims/citations/product proof/link verification
7. Original useful visual package
8. Adversarial quality/policy gate
9. Preview + CMS dry-run
10. Publish/live verification or preview-only terminal record

Each stage must write `content-pipeline/stage-receipts/{run-key}/{stage}.json` using the schema in the execution contract. The controller validates file existence and SHA-256 values before advancing.

## Legacy material

Older files and scripts may mention Semrush, OpenRouter, autonomous one-issue publishing, five posts per week, or deterministic-only visuals. Those statements are historical and are not valid instructions for the active routine. Useful existing scripts may still be used when they do not contact prohibited providers and their output passes the current contract.
