# Pleasur SEO Agent

The complete Paperclip SEO agent handoff: its live routine, agent instructions, deployed VPS source, skill library, references, templates, scripts, and a portable workflow for another runner such as Buzz.

## Start here

- `paperclip-source/live-routines/` - the active four-attempts-per-week routine and direct VPS verification.
- `paperclip-source/vps-deployed-blog-engine/` - the current deployed agent source snapshot, including the canonical `.claude/skills/` directory.
- `paperclip-source/exact-blog-agent-2/` - the complete historical source mirror, including all references and operational artifacts.
- `paperclip-source/agent/` - the Paperclip agent instructions and identity files.

## Portable adaptation layer

These top-level folders are an implementation guide for a new workflow runner. They do not replace the exact source packages above.

- `workflow/` — controller and ten-stage publishing flow.
- `skills/` — ten portable, executable `SKILL.md` modules plus the catalog and stage assignments.
- `gates/` — selection, quality, visual, publish, and live-audit requirements.
- `templates/` — artifacts required for every run.
- `docs/` — architecture and migration guidance.

`skills/` contains new portable wrappers. `.claude/skills/` inside each preserved source package contains the original skill files and their full references.

## Operating rule

Run four scheduled **attempts** each week: Monday, Tuesday, Thursday, and Friday. Each attempt may publish at most one article, but it is never required to publish. Missing evidence ends as `NO_PUBLISH_DATA_REQUIRED`; repeated failure ends as `NO_PUBLISH_QUARANTINED`.

## Use in Buzz

Use `workflow/new-content-pipeline.md` as the controller specification. Load only the skills assigned to the current stage, write the required artifact, enforce every item in `gates/publish-gates.md`, and preserve the manifest and skill trace. Start with `skills/01-candidate-selection/SKILL.md` and advance only after its decision passes.

No credentials, VPS paths, CMS tokens, private data, browser sessions, or legacy provider instructions are included.
