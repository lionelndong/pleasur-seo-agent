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

Require current `brand_dr` and current evidence-backed `max_targetable_kd`, with `max_targetable_kd > brand_dr`. Calculate:

- `kd <= brand_dr`: `base_winnability = 10`.
- `brand_dr < kd <= max_targetable_kd`: `base_winnability = 5 + 3 × (max_targetable_kd - kd) / (max_targetable_kd - brand_dr)`.
- `max_targetable_kd < kd <= max_targetable_kd + 15`: `base_winnability = 3`.
- `kd > max_targetable_kd + 15`: `base_winnability = 1`.

If `weak_link_count >= 3`, set `winnability = min(10, base_winnability + 2.0)`; otherwise set `winnability = base_winnability`. Keep full precision through ranking.

Return `needs_data` when either authority input is missing or invalid. Do not use qualitative fallback bands. Every value must cite current brand authority and SERP evidence; KD alone cannot determine the score.

Example with `brand_dr=20` and `max_targetable_kd=40`:

- `kd=30` gives `base_winnability=6.5`; three weak links give `winnability=8.5`.
- `kd=45` gives `base_winnability=3`; three weak links give `winnability=5`.
- `kd=60` gives `base_winnability=1`; three weak links give `winnability=3`.

## Formula

With products:

`(0.2 × traffic + 0.2 × brand_fit + 0.4 × product_fit + 0.2 × winnability) × free_seeker_penalty`

Without products:

`(0.3 × traffic + 0.4 × brand_fit + 0.3 × winnability) × free_seeker_penalty`

Set the penalty to `0.4` for free-seeker intent and `1.0` otherwise.

## Routing and ties

Route tool-led opportunities and existing strong coverage before scoring. Sort ties by higher traffic potential, lower KD, then normalized keyword in lexical order. Select at most one eligible blog candidate.
