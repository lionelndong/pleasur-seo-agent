# Visual System

This file defines the visual bar for EO blog publishing and relaunches. It exists because a post can
technically "have visuals" and still feel weak. Ahrefs-style content uses visuals as evidence,
explanation, and review aids, not decoration.

## Visual Package

Every publish or material relaunch must produce a visual package before preview:

- `content-pipeline/images/{slug}/manifest.json`
- `content-pipeline/images/{slug}/prompts.md` when AI-generated images are used
- real image files for all captured/generated visuals
- `content-pipeline/images/{slug}/manual-capture.md` only when a visual cannot be automated
- a cover candidate and OG candidate named in the scorecard

An empty manifest is a failed visual stage. A table-card image by itself is also a failed visual
stage for a normal article.

## Required Mix

Use the article length scale in `scales-and-rubrics.md`, then apply this role mix:

| Role | Required when | Good examples |
|---|---|---|
| Product proof | Pleasur.AI is materially mentioned | screenshot of the exact UI, action-shot of a completed flow |
| Concept explanation | The article explains a model, workflow, or decision | Nano Banana / image model infographic, flow diagram, decision tree |
| Comparison support | The article compares choices | table, decision matrix, chart, competitor UI capture when allowed |
| Evidence | A claim depends on a source or data | chart from real data, clipped external quote/chart, sourced screenshot |
| Cover/OG | Every publish unless the route cannot support it | topic-specific SFW editorial image, no text/title/logo by default |

For 1,500+ word posts, use at least three visual roles. A strong default is:

1. one cover image;
2. one product proof screenshot or action-shot;
3. one concept infographic or diagram;
4. one table/chart/decision-support visual;
5. additional screenshots, charts, or diagrams where sections need them.

## Cover Recipe

The cover is not a decorative afterthought. It is the first trust signal.

Hard rules:

- 1600x900 or clean 16:9 crop.
- SFW. No nudity, explicit pose, real-person likeness, or suggestive contact.
- No title text, fake UI text, watermark, or garbled letters.
- No logo unless the current approved recipe says to use one.
- The image must feel specific to the topic, not generic "AI companion" stock art.
- The focal point must survive mobile crop and social-card crop.

Preferred cover styles:

- clean editorial still life with a visible but unreadable chat/product motif;
- abstract but concrete metaphor for the article promise;
- branded-but-subtle product surface crop when the product is the proof;
- SFW generated image with a specific prompt, or a real product screenshot if it is beautiful enough.

Reject covers that are dark, generic, blurry, text-heavy, over-sexualized, or visibly AI-garbled.

## Ahrefs-Style Blocks

The target feel is closer to Ahrefs blog blocks:

- cropped screenshots with padding and a clear subject;
- diagrams that explain the idea at a glance;
- charts and tables that carry real decision value;
- callout/table blocks that break long prose;
- visuals roughly every 200-350 words in long sections when the topic supports it.

Do not count decorative lifestyle images, repeated table-card screenshots, or generic AI art toward
the useful visual minimum.

Observed Ahrefs patterns to emulate:

- Tool walkthrough posts place screenshots beside the exact instruction, such as Keywords Explorer
  filters, Rank Tracker history, GSC reports, or AWT health reports.
- Format/education posts use simple infographics and flowcharts to make the structure scannable
  before the reader commits to the prose.
- Template posts show the actual template or excerpt, not a generic illustration.
- Data or optimization posts use charts/tables where the number changes the decision.

A reader should be able to scroll the article quickly and understand the argument from the visual
sequence alone: cover promise, proof screenshot, explanatory diagram, decision table/chart, final
CTA or product proof.

## Visual Planning Timing

Do not leave visuals for a last-minute CMO rescue. The outline stage must name the visual role mix
and the draft must preserve typed visual slots. The visual package stage then produces the assets.

If the visual package fails, create a focused stage packet or child task titled:

`Visual package for {slug}: cover, screenshots, infographic, manifest`

The task must include only the visual brief, input paths, expected assets, and pass/fail checklist.

## Screenshots

Use `screenshot` for static product states and `action-shot` for multi-step product states. The
visual must show the exact feature or workflow being discussed.

Examples:

- Companion Creator personality/backstory controls for customization sections.
- AI Image Generation panel for image-related sections.
- Chat thread with speaker icon/call affordance only when that feature is live or explicitly
  allowed as coming-soon in the article context.

If a product screenshot cannot be captured, block or create one precise capture issue. Do not
replace product proof with a pricing-page link.

## Infographics And Nano Banana

Use generated images for concept visuals, not for fake product UI.

Use Nano Banana (`google/nano-banana` through Replicate) when:

- the board explicitly asked for a Nano Banana-style infographic;
- GPT Image output is weak, generic, or refused;
- the visual is a concept diagram, decision tree, comparison map, or workflow illustration.

Prompts must be structured, label-explicit, and stored in `images/{slug}/prompts.md`. One-line
prompts are a gate failure. Use the patterns in `templates/visual-types.md` and
`templates/editorial-principles-visuals.md`.

## Visual Score

Visual Proof score is:

- 0: no manifest, broken images, or empty/table-only visual set.
- 1: mostly decorative or weakly related visuals.
- 2: minimum count present but poor role mix or no product proof where needed.
- 3: useful minimum passes, with relevant cover and at least two roles.
- 4: strong role mix, real product proof, and good first-view/OG behavior.
- 5: visuals materially improve trust, comprehension, and shareability.

Publish requires at least 3. Product-led posts require product proof. Linkable/promotable posts
should aim for 4 or 5.
