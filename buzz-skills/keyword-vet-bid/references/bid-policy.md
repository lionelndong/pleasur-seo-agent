# BID policy

Use this policy exactly unless a human-approved, versioned Stage 01 policy supersedes it.

## Business scoring

### Brand fit

- `10`: directly addresses a documented audience pain point.
- `7`: strongly relevant to the audience and its goals.
- `4`: adjacent but plausibly useful.
- `0`: wrong audience.

Use intermediate scores only when the evidence supports the distinction. Pass at `brand_fit >= 4`.

### Product fit

- `10`: a live Pleasur.ai product is essential to a strong answer.
- `7`: a product provides a strong, natural demonstration or solution.
- `4`: a product can be mentioned naturally and usefully.
- `0`: no relevant live product.

Use intermediate scores only when justified. Pass at `product_fit >= 3` when products exist.

### Business value

- `3`: the topic serves a paying-prospect need and a product is a natural answer.
- `2`: a product materially helps and has a credible path to users or revenue.
- `1`: weak or indirect path.
- `0`: no credible business path.

Treat `business_value` as a downstream prioritization signal, not an independent BID gate. A value of `1` may pass when `brand_fit >= 4`, `product_fit >= 3`, and the credible-path check pass; preserve the weak-path signal for prioritization. A value of `0` normally accompanies failed fit or no credible path. If the fields contradict one another, return `needs_data` rather than choosing which value to trust.

Useful informational product-adjacent content may score highly; do not add a commercial-wording boost.

Set `free_seeker=true` when the query centers on free, unlimited, uncensored, unfiltered, no-filter, no-account, no-payment, or without-paying access. Preserve it for prioritization rather than auto-rejecting it.

## Intent policy

Prefer current Ahrefs intent evidence. Accept informational and commercial-investigation blog intent. Reject dominant transactional or navigational-only intent.

When primary intent is ambiguous, ground the decision in the current top ten:

- informational: guides, explanations, tutorials, and knowledge articles;
- commercial investigation: comparisons, reviews, and option-led articles;
- transactional: product, category, checkout, or pricing-led pages;
- hybrid: material mix of blog-suitable and transactional results.

Treat hybrid as PASS only when a blog article can satisfy a clear portion of the observed intent.

Detect tool-led SERPs separately: route when at least three of the top five organic results are tools, calculators, or generators.

## Difficulty policy

Use current Pleasur.ai DR and current organic SERP evidence.

- Calculate the median DR across ten usable organic results.
- Define a weak result as one whose DR is strictly below `brand_dr + 5`; also record its URL and concrete displacement rationale.
- Pass if `median_top10_dr <= brand_dr + 15`.
- Otherwise pass only if at least two named weak results meet the numeric definition and have concrete displacement evidence.
- Treat KD as supporting context, not a standalone pass/fail gate.
- If brand DR or adequate SERP evidence is unavailable, return `needs_data`.

## Failure reason vocabulary

Prefer stable codes: `brand_fit_below_threshold`, `product_fit_below_threshold`, `vanity_rank`, `no_credible_business_path`, `business_evidence_conflict`, `serp_is_transactional`, `serp_is_navigational`, `tool_led_routed`, `difficulty_above_reach`, `brand_dr_unavailable`, `serp_evidence_incomplete`, `country_mismatch`, `stale_evidence`, and `provider_unavailable`.
