# Skill routing map

This map implements `execution-contract.md`. New-content stages and existing-content update skills must not be mixed.

| Stage | Required skills | Proof of use |
|---|---|---|
| 01 | `keyword-prioritization`, `keyword-vet-bid`, `keyword-vet-aio` | candidate decision, kill-rule results, validated Ahrefs artifact |
| 02 | `research`, `content-gap-analysis`, `contagious-why-things-catch-on` | intent, BEAT SPEC, named weak pages, information-gain asset, STEPPS effect |
| 03 | `brand-reference`, `product-mentions` | current proof, Feature Fit Matrix, author/byline/CMS identity |
| 04 | `outline`, `oversubscribed` | Article Promise, annotated outline, link/visual plan, demand constraint |
| 05 | `draft`, `update-draft` | v1 critique and materially improved v2 |
| 06 | `verify-claims`, `update-claims`, `update-product-mentions` | claim ledger, cited draft, link/product corrections |
| 07 | `generate-visuals` | file-backed original assets, alt text, dimensions, manifest hashes |
| 08 | `quality-check`, `contagious-why-things-catch-on`, `oversubscribed` | adversarial comparison, score >=85, explicit accept/reject decisions |
| 09 | `preview`, `format-for-publish` | preview, CMS dry-run payload, validator result |
| 10 | `format-for-publish`, `preview` | zero-mutation preview terminal or verified live audit |

Conditional use is recorded as `NOT_APPLICABLE` only when the receipt gives the exact applicability test and reason. Availability alone is not use.

For every listed skill, the stage receipt records the installed runtime name, SHA-256 of the instruction actually read, input and output paths/hashes, decision before and after, and whether the skill changed the decision. A markdown trace may summarize this evidence but cannot replace the JSON receipt.

Conflict precedence:

1. board instruction, safety/privacy/legal truth, and verified live product behavior;
2. `execution-contract.md`;
3. search intent and reader job;
4. Ahrefs evidence, Business Value, link reality, and kill rules;
5. original product proof, information gain, author/byline, and reader trust;
6. Contagious/Oversubscribed lenses;
7. formatting or scoring suggestions.

Reject any skill suggestion that invents a claim, weakens intent, creates clickbait, substitutes a prohibited data provider, hides a kill verdict, or bypasses a deterministic gate. Skills such as `extract-content`, `update-guidance`, `update-topic-gaps`, and update/relaunch orchestration belong to the separate existing-content lane unless Stage 05/06 explicitly names a bounded rewrite helper above.
