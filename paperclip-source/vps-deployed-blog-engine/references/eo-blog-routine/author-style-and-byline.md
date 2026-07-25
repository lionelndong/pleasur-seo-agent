# Author Style And Byline Gate

This gate prevents the "published with no author" failure and keeps authored posts from drifting
into generic SEO prose.

## Required Artifact

Before drafting or relaunching, save:

- New article: `content-pipeline/2-reference/{slug}-author.md`
- Relaunch: `content-pipeline/2-reference/{slug}-author-relaunch.md`

## Author Packet

The packet must include:

- selected author name;
- CMS/Strapi author id or slug;
- expected public profile URL;
- whether this author is allowed for the topic;
- 3-5 example posts by the same author, or a documented house-style fallback;
- short style profile;
- intro patterns;
- section/BLUF patterns;
- sentence and paragraph rhythm;
- preferred examples and analogies;
- how the author handles product mentions;
- banned moves that would break the author's voice;
- final byline verification plan.

Do not copy paragraphs from example posts. Extract patterns and write fresh.

## Hard Gates

Do not publish or relaunch if any of these fail:

- no author selected;
- author id/slug is missing from the publish payload;
- public byline or author profile link is missing;
- author examples were not reviewed or a house-style fallback was not justified;
- the article voice clearly conflicts with the selected author;
- the live page shows the wrong author, no author, or an unlinked author when the site supports
  author links.

If the site currently lacks author/profile support for a route, block with a precise follow-up
issue instead of silently shipping a no-author page.

## Style Use

The selected author style should influence:

- intro pace and hook;
- H2/H3 rhythm;
- how direct the BLUFs are;
- examples and analogies;
- how much first-person or product proof appears;
- CTA and product mention restraint;
- how much personality is allowed.

The author style cannot override:

- verified facts;
- adult/safety/legal/privacy accuracy;
- search intent;
- product truth;
- the Contagious integrity rule against clickbait.

## Verification

Before publish/live completion, record:

- publish payload author id/slug;
- rendered author name;
- rendered author link/profile URL;
- HTTP status for author profile when available;
- screenshot or preview note showing byline in the first screen or expected byline location;
- final author fit score from `scorecards-and-traces.md`.

The done comment must include the author name, author profile/link result, author packet path, and
author fit score.
