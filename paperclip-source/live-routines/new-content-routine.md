# EO Blog Content Engine — 4 quality-gated attempts/week

This is the live Paperclip new-content routine definition recovered from the active routine. It is separate from existing-content portfolio improvement and post-change measurement.

## Scope

Create genuinely new blog articles only. Do not scan, relaunch, or measure existing posts in this lane.

## Cadence and concurrency

- Monday, Tuesday, Thursday, Friday at 9:00 AM Eastern.
- Each fire is a quality-gated attempt, not a publish quota.
- Maximum one public article per fire and four per calendar week.
- Coalesce when active; skip missed fires.

## Required references

Before acting, read `references/eo-blog-routine/execution-contract.md` completely. It supersedes older cadence, provider, one-issue, autonomous-publish, stage-numbering, and failure instructions. Use the prompt map, stage-task map, skill-routing map, scorecards/traces, and checklists only under that contract.

## Runtime variables

- `candidateKeyword`
- `targetCountry`
- `manualDataArtifact`
- `scope` (`new_content`)
- `runMode` (`quality_gated_live` or `preview_only`)
- `ahrefsObservedAt`
- `ahrefsRenewalDate`

## Data policy

Ahrefs is the only SEO-metrics source. Consume board-supplied or browser-exported Ahrefs evidence only. Do not call Ahrefs, Semrush, DataForSEO, OpenRouter, or paid APIs. Do not ask for credentials or approximate missing metrics.

A broad packet may be reused for 30 days. The selected candidate overview and SERP packet must be no older than 14 days and pass schema, conflict, intent, product-fit, Course Formula, vulnerability, and cannibalization gates.

## Controller contract

The routine issue is the controller. It creates exactly one direct child for the current stage and stays in progress while that child runs. The child performs one canonical stage, writes `content-pipeline/stage-receipts/{run-key}/{stage}.json`, posts a structured handoff, and closes. A child never creates or wakes its successor. The controller verifies artifact paths and SHA-256 values before starting the next stage.

## Missing evidence

Required external evidence must not strand the cadence. When evidence is missing or conflicting, the stage writes `content-pipeline/data-requests/{run-key}.md` naming the exact Ahrefs report, country, filters, fields, freshness, and accepted formats. It closes as `NO_PUBLISH_DATA_REQUIRED`; the controller closes with the same disposition. Do not leave either workflow state waiting for a human.

## Canonical stages

1. Candidate and Ahrefs validation
2. Intent, SERP research, and information gain
3. Product truth, author, and byline
4. Outline, internal links, and visual plan
5. Draft critique and version-two rewrite
6. Claims, citations, product proof, and links
7. Useful original visuals
8. Adversarial quality and policy gate
9. Preview and CMS dry run
10. Live verification or preview-only terminal record

The authoritative contract defines required skills and receipt schema.

## Publication rule

`preview_only` forbids every CMS and public mutation. `quality_gated_live` can publish once only after stages 01–09 have valid receipts, the deterministic quality verdict is `PASS` at 85 or above, and the run-contract validator passes.

After publication, verify public HTTP 200, canonical URL, H1/title/clean metadata, named byline/profile, cover/OG/article images with non-zero dimensions and correct alt handling, citations, internal links, CTA, desktop/mobile first view, and a placeholder/component scrub. Any mismatch is a stage-10 failure, not a pass.

## Terminal record

Record disposition, variables, child-stage IDs, receipts/artifacts, candidate/intent/information-gain/product/author/visual/claim/link/score/CMS/live results, public publish count (zero or one), restart stage or exact data request, and confirmation that separate existing-content routines were untouched.
