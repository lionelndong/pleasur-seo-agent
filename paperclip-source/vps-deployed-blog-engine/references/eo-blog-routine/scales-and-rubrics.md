# Scales And Rubrics

Use these scales every time the blog routine chooses, drafts, updates, or ships an article.
Scores are diagnostic. Publish/no-publish is controlled by the hard gates in the checklists.

## Candidate Selection

For existing content, assign `P0_live_integrity`, `P1_customer_revenue_loss`,
`P2_rank_conversion`, `P2_link_equity`, `P3_maintenance`, or `no_op` before scoring. Higher classes
outrank lower ones. Within a class use:

```text
Business Value x Impact x Confidence x Urgency / Effort
```

Record every 1-5 factor with a citation, then check active work and cooldown. See
`portfolio-improvement-system.md`.

### Business Value, 0-3

| Score | Meaning | Action |
|---|---|---|
| 3 | Pleasur.AI is the natural solution and the page can create a direct signup or paid path. | Prioritize if traffic potential and link reality are workable. |
| 2 | Pleasur.AI helps meaningfully, but the topic can be answered without us. | Use when the article has a clear product proof or internal-link path. |
| 1 | Pleasur.AI is only a light nurture mention or support link. | Publish only when it supports a stronger cluster or linkable asset. |
| 0 | No plausible customer path. | Kill or defer. |

Free-seeker, no-filter, no-signup, and free-tool topics must be discounted unless there is real
conversion evidence or a sharp paid/product-led answer.

### Course-Aligned Opportunity Score

```
Business Value x Traffic Potential / max(1, Estimated Links Needed)
```

Use this to compare candidates, not to override judgment. If a candidate lacks any required field,
it cannot enter draft.

### Estimated Links Needed

Use Ahrefs KD only as a first pass. KD and DR are not linear, so always verify with:

- top-10 referring domains;
- weak-link winners;
- current DR ceiling;
- internal-link support;
- linkable asset or promotion plan.

Use `1` for a genuinely winnable no-link or technical/content-only fix. Never use `0`.

### Intent Fit

| Verdict | Meaning | Action |
|---|---|---|
| PASS | SERP format, reader job, article shape, and product angle align. | Continue. |
| BORDERLINE | Some fit, but the query may want a different page type or weaker product path. | Fix the angle or choose another candidate. |
| FAIL | The SERP rewards a format we cannot or should not create. | Kill or defer. |

## Content Quality

### Quality Gate

Use `.claude/skills/quality-check/SKILL.md`.

Final score:

```
0.6 x mechanical score + 0.4 x judgment score
```

Mechanical dimensions:

| Dimension | Weight |
|---|---:|
| Depth vs benchmark | 25 |
| Consensus coverage | 20 |
| AI tells | 25 |
| Evidence | 15 |
| Structure | 15 |

Judgment overlay asks: if the reader opens our article and the current #1 result side by side,
which one do they keep?

Verdicts:

| Verdict | Rule |
|---|---|
| PASS | Score >= 85, no critical issue, no mechanical dimension below its floor, and adversarial read does not prefer the competitor. |
| BORDERLINE | Score 70-84 or adversarial read is meaningfully negative. |
| FAIL | Score < 70 or any critical issue. |

Do not let a high score override a hard gate. A thin, me-too, unsupported, text-only, or broken
article cannot ship.

### Quality / Uniqueness / Authority

| Factor | Minimum |
|---|---|
| Quality | Useful, well-structured, visually readable, specific, and benchmark-aware. |
| Uniqueness | Real Pleasur.AI proof, first-hand testing, original comparison, proprietary observation, community/VOC synthesis, expert/source synthesis, sharper framework, or defensible contrarian POV. |
| Authority | Live product evidence, reputable sources, named expert/source material, original data, or earned proof. |

All three must be present for publish or relaunch.

### Voice Baseline

Use `.claude/skills/quality-check/references/voice-baseline.md`.

| Metric | Healthy Range |
|---|---|
| Average sentence words | 14-22 |
| Median sentence words | 13-18 |
| Average paragraph words | 35-80 |
| Median paragraph words | 30-60 |
| Second-person mentions per 1k words | 15-35 |
| Em dash per 1k words | 2-8 |

These are guardrails, not the voice. The editor/adversarial read decides whether the article
actually sounds human and useful.

## Linkability And Shareability

### Contagious STEPPS

Use `.claude/skills/contagious-why-things-catch-on/SKILL.md` for linkable assets, headlines,
shareable frameworks, and promotional angles.

Score each article or linkable asset on six 0/1 ingredients:

| Ingredient | Question |
|---|---|
| Social Currency | Does sharing this make the reader look smart, tasteful, prepared, or in-the-know? |
| Triggers | Is there a frequent cue that will remind people of this article? |
| Emotion | Does it create high-arousal emotion such as awe, surprise, excitement, anxiety, humor, anger, or disgust? |
| Public | Is the idea observable or easy to show? |
| Practical Value | Is it immediately useful to a narrow audience? |
| Stories | Is there a Trojan-horse story that carries the point? |

Guidance:

- 0-1: not linkable/shareable; treat as ordinary SEO support.
- 2-3: usable if Business Value and intent are strong.
- 4-6: strong linkable/promotion candidate.

### Contagion Score

For any linkable/promotable article, record the 0-10 Contagion Score from
`scorecards-and-traces.md`:

```
STEPPS count (0-6)
+ Share/link asset strength (0-2)
+ Story integration (0-1)
+ Headline trigger strength (0-1)
```

If the Contagious pass creates false, unsafe, clickbait, or off-intent framing, force the score to
0 and reject that change. Search intent, truth, product proof, and author integrity outrank
Contagious.

### Headline Ideation

Before drafting the final H1, brainstorm at least five distinct headline angles. Pick the one
that best combines keyword fit, honesty, click reason, and one strong STEPPS ingredient.

## Promotion And Demand Creation

### Oversubscribed Demand Thresholds

Use `.claude/skills/oversubscribed/SKILL.md` for promotion, outreach, guest-post demand, and
distribution planning.

For campaigns and link-building pushes, record the demand state:

| State | Signal |
|---|---|
| Soft interest | People lightly opt in, click, save, reply positively, or ask to see more. |
| Educated interest | People understand the angle and why it is relevant to them. |
| Strong interest | People are ready to place, link, collaborate, cite, or share. |

Priestley threshold to watch before a serious release:

- 5x strong interest;
- 10x educated interest;
- 100x soft interest.

For link building, use this as a quality lens, not an excuse to spam. Build a qualified prospect
pipeline and keep the operator gate on external outreach.

### 7-Hour Rule

For guest-post or partner-link demand, warm the market with value before asking. Aim for roughly
eleven useful touches or seven hours of education/entertainment across the campaign when feasible.

## Visual And Cover Gates

Use `visual-system.md` and `checklists/visual-header-cover-checklist.md`.

The visual count scale is:

| Article Length | Minimum Useful Visuals |
|---|---:|
| Under 1,200 words | 5 |
| 1,200-2,000 words | 6 |
| 2,000-3,000 words | 8, target 10-13 |
| Over 3,000 words | 10, target 12-15 |

For 1,500+ word articles, use at least three visual roles: product proof, explanation, comparison,
decision support, evidence, or conversion.

Visual Proof is zero when the manifest is empty, the visual set is table-only, the cover is broken
or generic, or Pleasur.AI is materially mentioned without a screenshot/action-shot product proof
visual or an approved exception.

## Live Verification

Use a binary result, not a score:

- HTTP 200.
- Expected H1/title/meta.
- Cover and OG image load.
- Article images load.
- Links and CTA path work.
- Mobile and desktop first view are not broken.
- No placeholder, hidden prompt marker, `[GAIN]`, `[VISUAL]`, `[SCREENSHOT]`, `[link]`,
  `[CITATION NEEDED]`, `TODO`, or internal tooling leak.

Any failed live verification item blocks publish until fixed or explicitly no-publish/no-op.

## Author And Trace Gates

Use `author-style-and-byline.md` and `scorecards-and-traces.md`.

- Author Fit score must be at least 3 for publish or rewritten relaunch.
- Missing author, wrong author, unlinked author profile, missing author examples, or missing author
  style packet blocks publish when the route supports authors.
- Every run must save a run manifest, scorecard, and skill trace.
- Any claimed skill use must be traceable to a stage, input, output, and decision.
