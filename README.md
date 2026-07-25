# Pleasur SEO Skills

Portable, evidence-gated SEO content operations extracted from the Paperclip blog-engine routine for Buzz or another workflow runner.

## Layout

- `workflow/` — controller and ten-stage publishing flow.
- `skills/` — ten portable, executable `SKILL.md` modules plus the catalog and stage assignments.
- `gates/` — selection, quality, visual, publish, and live-audit requirements.
- `templates/` — artifacts required for every run.
- `docs/` — architecture and migration guidance.

## Operating rule

Run four scheduled **attempts** each week: Monday, Tuesday, Thursday, and Friday. Each attempt may publish at most one article, but it is never required to publish. Missing evidence ends as `NO_PUBLISH_DATA_REQUIRED`; repeated failure ends as `NO_PUBLISH_QUARANTINED`.

## Use in Buzz

Use `workflow/new-content-pipeline.md` as the controller specification. Load only the skills assigned to the current stage, write the required artifact, enforce every item in `gates/publish-gates.md`, and preserve the manifest and skill trace. Start with `skills/01-candidate-selection/SKILL.md` and advance only after its decision passes.

No credentials, VPS paths, CMS tokens, private data, browser sessions, or legacy provider instructions are included.
