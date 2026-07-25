# Source Map

Use this map to avoid mixing the sources into mush. Each source has a different job.

## Ryan Law / Ahrefs Content Engineering

Local source: `ahrefs-ryan-law-article.md`

Ryan supplies the workflow architecture:

- Chain narrow editorial skills instead of one giant prompt.
- Save every stage output so failures can be diagnosed.
- Use strong data sources before asking the model to write.
- Front-load human context with angle, product notes, and required ideas.
- Build previews for review and troubleshooting.
- Personalize the workflow to the brand and product.
- Keep skills short enough that the agent can actually follow them.

In our routine, this becomes:

`context -> research -> reference -> outline -> product mentions -> draft -> claims -> visuals -> preview -> publish`

## Ahrefs Course

Local sources:

- `plans/ahrefs-course-full-transcript.txt`
- `plans/2026-06-27_ahrefs-course-gap-analysis.md`
- `plans/2026-06-29_course-to-eo-agent-embedding.md`

The course supplies the strategy formula:

- The KPI is customers/orders/sales, not traffic or publishing volume.
- Estimate full traffic potential from top-ranking pages and parent topics, not single-keyword volume.
- Review ranking difficulty through KD, top-10 referring domains, weak-link winners, and current DR ceiling.
- Score Business Value from 0 to 3.
- Match search intent before writing.
- Prioritize topics that can rank and convert.
- Great content requires Quality, Uniqueness, and Authority.
- Never make a clone of page 1. Add extra value or explain the topic better.
- Promotion/backlinks/internal links are part of the system, not an afterthought.
- Existing content should be updated, merged, deleted, or relaunched based on evidence.
- New content and existing-content improvement are separate, equally important workstreams; reserve
  roughly half of editorial effort for improvement over a rolling period.
- A relaunch is not complete at publish: it requires re-promotion through an approved handoff and
  post-change measurement.
- Linkable assets should use the Contagious/STEPPS lens.
- Promotion and outreach should use the Oversubscribed demand lens.
- Unique content must come from a real source of uniqueness: product proof, first-hand testing,
  original comparison, unique data, operational insight, community/VOC synthesis, or a defensible
  POV. Longer copy, reordered SERP consensus, or generic extra sections do not count.

In our routine, this becomes:

`Course-Aligned Opportunity Score = Business Value x Traffic Potential / max(1, Estimated Links Needed)`

For the existing portfolio, evidence is classed first and candidates are then ranked within class
using `Business Value x Impact x Confidence x Urgency / Effort`. Broken backlinks are one tactical
link-equity input, not the governing daily routine.

The book lenses live in `book-skills.md`; do not stuff full book notes into routine prompts.

## Pleasur.AI Layer

Pleasur.AI supplies the uniqueness layer:

- Real product screenshots and action shots.
- First-hand testing of companion creation, chat, memory, image generation, privacy, and onboarding flows.
- Adult-AI market judgment that generic SERP pages do not have.
- Safer and more precise framing around consent, age, privacy, and legality.
- Internal links toward the most relevant product flows, existing walkthroughs, and money pages.
  Pricing is only the main link when price/cost/coins is the reader job.
- Conversion paths that can be checked through PostHog/GSC where available.

Every article or relaunch must name the Pleasur.AI-specific reason it deserves to exist.

## How To Use The Sources

Do not paste large transcript chunks into routine prompts. Use the source logic:

- Ryan decides the stages.
- The course decides what deserves to be written.
- Pleasur.AI decides what makes the article different and useful.

If those three do not all show up in the artifact, the routine has failed.
