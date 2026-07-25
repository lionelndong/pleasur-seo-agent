# Live VPS verification

This package was checked read-only against the deployed EO blog-engine workspace on the Paperclip VPS on 2026-07-25. The deployed workspace, rather than a local reconstruction, is the source for this verification.

## Routine-critical file fingerprints

| Deployed file | SHA-256 |
| --- | --- |
| `PIPELINE.md` | `9b9d7315e072f0b0781c3b1ddfaf4f43034d02a727453376f1d7baac15fb5df7` |
| `references/eo-blog-routine/execution-contract.md` | `e1a0b6e6b3c8814185fa6abe313ad086e0b27ec8ab47381e0ce184b897446cd8` |

## Deployed skill inventory

The following 38 deployed skill folders each contain a `SKILL.md` in the live workspace. Their complete source, references, templates, and scripts are preserved in `../exact-blog-agent-2/.claude/skills/`.

`apexcharts`, `auto-blog-loop`, `blog-pipeline`, `brand-reference`, `capture-visuals`, `cluster-planner`, `contagious-why-things-catch-on`, `content-gap-analysis`, `draft`, `extract-content`, `format-for-publish`, `generate-visuals`, `geo-citation-audit`, `keyword-prioritization`, `keyword-research-pipeline`, `keyword-vet-aio`, `keyword-vet-bid`, `linkable-asset`, `linkbuild-competitor-mining`, `outline`, `outreach`, `oversubscribed`, `preview`, `product-mentions`, `quality-check`, `relaunch`, `research`, `seed-modifier-prompt`, `skill-eval`, `squeeze-max-traffic`, `update-claims`, `update-draft`, `update-guidance`, `update-pipeline`, `update-preview`, `update-product-mentions`, `update-topic-gaps`, and `verify-claims`.

The live routine definition is documented in [new-content-routine.md](new-content-routine.md). It uses the deployed execution contract and these skills as its operating source.
