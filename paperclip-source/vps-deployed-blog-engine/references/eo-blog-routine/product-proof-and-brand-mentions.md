# Product Proof And Brand Mentions

This file prevents generic, bolted-on Pleasur.AI mentions. The article should use the product the
way Ryan's Ahrefs examples use Ahrefs: as a concrete demonstration of the thing being taught, not
as an ad block.

## Core Rule

Do not default to the pricing page.

Pricing is allowed only when the section's reader job is cost, limits, coins, plan comparison, or
"is it worth paying?" For normal sections, the default product link should be the relevant product
flow, feature page, existing blog walkthrough, or no link at all.

## Feature Fit Matrix

Before `product-mentions`, build this matrix in `content-pipeline/2-reference/{slug}.md` or the
annotated outline:

| Reader job | Pleasur.AI feature | Proof available | Best link | Visual |
|---|---|---|---|---|
| What the reader is trying to do | Live feature/use case | screenshot, action-shot, existing article, or test note | `/create`, `/generate`, existing blog URL, or `/pricing` only for price sections | typed visual placeholder |

Every material Pleasur.AI mention must map to one row. If no row exists, cut the mention.

## Proof-Led Mention Types

Use these patterns:

- Demonstration: "Here is how this looks in the Companion Creator..."
- Contrast: "This is where an AI companion app differs from a stranger room..."
- Verification: "Check whether the app lets you control X before you commit..."
- Practical next step: "If you want saved context, start with the character setup flow..."

Avoid:

- "Pleasur.AI has X features" without showing where or why they matter.
- Pricing-first paragraphs in articles that are not about pricing.
- Repeating the same CTA in multiple sections.
- Mentioning coming-soon or roadmap features as live.
- Turning safety/privacy/legal sections into sales copy.

## Live Feature Truth

Use `brand-config.md` as the source of truth, then verify live product reality when the claim is
material.

When the site gains or loses features:

- update `brand-config.md` first;
- refresh `brand-reference` inventory when needed;
- use only live features in evergreen articles;
- create a follow-up issue if the feature is visible on the site but missing from the catalog.

Coming-soon features belong only in launch, roadmap, or "where the category is going" sections
where the context explicitly authorizes them.

## Product Mention Budget

Most articles need 1-3 meaningful Pleasur.AI mentions, not constant brand insertion.

For a 6-section article:

- 0-1 mentions: acceptable for low Business Value support articles.
- 2-3 mentions: normal for comparison/decision guides.
- 4-5 mentions: only when the article is product-led and the proof is strong.
- 6+ mentions: usually too salesy; cut or consolidate.

The intro should usually answer the query before mentioning Pleasur.AI. The first product mention
should arrive where it helps the reader make or verify a decision.

## Required Product Proof Packet

For every product-led article or product-led relaunch, save:

- the feature fit matrix;
- the exact feature(s) used;
- the link target(s);
- the product proof visual(s);
- any live verification notes;
- why pricing was or was not used.

The scorecard must state whether product mentions were:

- organic;
- proof-led;
- live-feature accurate;
- free of pricing-page overuse.

If the article links `/pricing` more than once, the scorecard must justify it section by section.
