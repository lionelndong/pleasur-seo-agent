# Visual, Header, And Cover Checklist

This checklist prevents text-only posts, bad covers, broken headers, and leaked prompt markers.
Read `../visual-system.md` before using it.

## Cover Image

Required for publish unless the site route explicitly does not support a cover.

- [ ] Cover asset exists.
- [ ] Canonical size is 1600x900 or the final upload is a clean 16:9 crop.
- [ ] Important content stays inside the central safe zone.
- [ ] Cover is SFW.
- [ ] No nudity, explicit pose, suggestive contact, or real-person likeness.
- [ ] No title text on the image.
- [ ] No stray letters, fake UI text, watermark, wrong logo, or garbled text.
- [ ] No logo on the cover unless the current recipe explicitly requires it.
- [ ] Cover fits the locked house style or the current approved cover recipe.
- [ ] Cover uses the approved recipe in `visual-system.md` or documents a stronger article-specific recipe.
- [ ] Cover clearly relates to the article topic.
- [ ] Cover does not look like generic stock art.
- [ ] Cover passes a visual sanity check after upload.

If any cover item fails, do not publish. Re-render, use the deterministic fallback, or block with a
manual-capture issue.

## Header And First View

- [ ] H1 is correct and human-readable.
- [ ] H1 does not contain `[GAIN]`, `[VISUAL]`, `TODO`, draft labels, or internal markers.
- [ ] Header/hero area does not crop awkwardly.
- [ ] Cover and title do not fight each other visually.
- [ ] The first paragraph answers the query quickly.
- [ ] There is no blank hero, broken image, distorted image, or missing cover alt text.
- [ ] Meta title and description match the final angle.

## In-Article Visuals

Minimums:

- [ ] `content-pipeline/task-packets/{slug}/07-visual-package.md` exists or the manifest explains why
  the `blog-pipeline` visual stage did not need a separate packet.
- [ ] Visual manifest is not empty.
- [ ] Visual set is not table-only.
- [ ] Under 1,200 words: at least 5 useful visuals or a documented exception.
- [ ] 1,200-2,000 words: at least 6 useful visuals.
- [ ] 2,000-3,000 words: at least 8 useful visuals, target 10-13.
- [ ] Over 3,000 words: at least 10 useful visuals, target 12-15.

Role mix:

- [ ] At least three visual roles for 1,500+ word articles.
- [ ] Product proof visual when Pleasur.AI is materially mentioned.
- [ ] At least one screenshot/action-shot when the article demonstrates a Pleasur.AI feature.
- [ ] At least one concept infographic/diagram when the article explains a decision process, workflow, or mental model.
- [ ] Comparison/decision-support visual when the article compares options.
- [ ] Evidence visual when a section leans on data.
- [ ] Concept/diagram visual when the article explains a mental model or workflow.

Quality:

- [ ] Every visual earns its place.
- [ ] The visual sequence works for scanners: cover promise, proof screenshot, explanation,
  decision-support visual, and final product/CTA proof where relevant.
- [ ] The visual package resembles the useful Ahrefs pattern: screenshots for exact steps,
  diagrams/infographics for mental models, charts/tables for decisions, and templates/examples when
  the section teaches a reusable format.
- [ ] No decorative filler is counted toward the minimum.
- [ ] Charts use real data.
- [ ] Screenshots show the claimed state.
- [ ] Action shots show the required interaction.
- [ ] Labels are readable.
- [ ] Alt text/caption is accurate.
- [ ] AI-generated infographic prompts are stored in `images/{slug}/prompts.md`.
- [ ] Nano Banana/GPT-image outputs are inspected for garbled text, malformed arrows, unreadable labels, and generic stock-art feel.
- [ ] No duplicate or near-duplicate visuals.
- [ ] No failed/manual visual is silently treated as done.

## Placeholder And Marker Scrub

Search final preview and live page for:

- [ ] `[VISUAL`
- [ ] `[SCREENSHOT`
- [ ] `[GAIN]`
- [ ] `[link]`
- [ ] `[CITATION NEEDED]`
- [ ] `TODO`
- [ ] `VISUAL-TODO`
- [ ] `<!--`
- [ ] Internal tool names that should not face readers.

Any hit must be fixed or explicitly justified before publish.

## Live Render Verification

- [ ] Live URL returns HTTP 200.
- [ ] H1 matches expected title.
- [ ] Cover image loads.
- [ ] OG/Twitter image points to the expected cover.
- [ ] Article images load.
- [ ] Tables/components render without broken syntax.
- [ ] Mobile first view is not broken.
- [ ] Desktop first view is not broken.
- [ ] No header/cover/layout regression is visible.
