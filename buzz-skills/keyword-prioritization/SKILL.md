---
name: keyword-prioritization
description: Deterministically rank fully vetted Pleasur.ai Stage 01 blog-keyword candidates by product fit, traffic opportunity, brand fit, and DR-relative winnability, selecting at most one.
---

# Keyword Prioritization

Rank only candidates with complete evidence that passed BID and have `aio_verdict` of `PASS` or an explicitly accepted `RISKY`.

Score each dimension from 0–10:

- `traffic`: use current traffic potential and KD; record the declared normalization.
- `brand_fit`: use the BID score.
- `product_fit`: use the BID score and keep it dominant.
- `winnability`: score relative to current Pleasur.ai DR, SERP authority, and named weak links; never use KD alone.

Compute:

`priority_score = (0.2 × traffic + 0.2 × brand_fit + 0.4 × product_fit + 0.2 × winnability) × free_seeker_penalty`

Use `free_seeker_penalty=0.4` when flagged, otherwise `1.0`. Break ties by higher traffic potential, then lower KD, then lexical keyword order. Route tool-led candidates outside the blog set and treat already-strong Pleasur.ai coverage as evaluated but not selected.

Approve only the highest-ranked eligible candidate. Mark other eligible candidates `evaluated_not_selected`, not rejected. Include every score, input, formula version, tie-break, and reason in the immutable Stage 01 packet. If no candidate passes, emit `rejected`; if required evidence is incomplete, emit `needs_data`. Never start Stage 02 or write external systems.
