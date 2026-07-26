# Keyword prioritization scoring policy

Use this policy unless a human-approved, versioned Stage 01 policy supersedes it.

## Traffic

Calculate:

`traffic = clamp(2 × log10(traffic_potential + 1) - kd / 20, 0, 10)`

Traffic potential and KD must share the target country and satisfy the run's freshness policy. Treat null as missing, not zero.

## Fit

Reuse BID scores:

- brand fit: `10` direct pain point, `7` strongly relevant, `4` adjacent but useful, `0` wrong audience;
- product fit: `10` essential, `7` strong demonstration, `4` natural useful mention, `0` irrelevant.

Do not re-evaluate or inflate fit at the ranking stage.

## Winnability

Prefer the explicit moving-ceiling calculation in the skill when current evidence includes `max_targetable_kd`.

If it does not, map the current BID evidence to these conservative bands:

- `9–10`: median top-ten DR is at or below brand DR and at least two results are clearly displaceable;
- `7–8`: median top-ten DR is within 12 points of brand DR, or three named weak links create a credible opening;
- `5–6`: BID passed on two named weak links but the median authority remains above the normal reach band;
- `3–4`: plausible reach requiring material authority/link growth;
- `1–2`: substantially above current reach;
- `0`: evidence shows the SERP is not realistically contestable under the current strategy.

Every value must cite current brand authority and SERP evidence. KD alone cannot determine the score.

## Formula

With products:

`(0.2 × traffic + 0.2 × brand_fit + 0.4 × product_fit + 0.2 × winnability) × free_seeker_penalty`

Without products:

`(0.3 × traffic + 0.4 × brand_fit + 0.3 × winnability) × free_seeker_penalty`

Set the penalty to `0.4` for free-seeker intent and `1.0` otherwise.

## Routing and ties

Route tool-led opportunities and existing strong coverage before scoring. Sort ties by higher traffic potential, lower KD, then normalized keyword in lexical order. Select at most one eligible blog candidate.
