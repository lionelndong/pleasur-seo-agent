---
name: keyword-vet-aio
description: Evaluate AI Overview presence and click-cannibalization risk for BID-passing Pleasur.ai keyword candidates using Ahrefs-only evidence. Use during Stage 01 before final keyword prioritization.
---

# Keyword Vet — AI Overview

Evaluate only BID-passing candidates.

1. Detect AIO presence from Ahrefs Keywords Explorer `serp_features`; the literal feature is `ai_overview`. Do not request `serp_features` from SERP Overview.
2. If absent, set `aio_verdict=PASS`. If present and the query is tool-led or comparison-driven, record the exemption and remaining click rationale.
3. Default to presence-only evaluation: non-exempt AIO presence is `RISKY`, requiring a clear information-gain/click reason.
4. Perform deep completeness scoring only when current Ahrefs Brand Radar supplies a fresh Google AIO response body. Never use web fetch or another provider as fallback. If deep evidence is required but unavailable, return `needs_data`.
5. Apply [references/aio-rubric.md](references/aio-rubric.md) directly. Do not select or name a model. An independent review pass may be used only when Buzz exposes it; otherwise apply the same rubric in a documented self-review.

Persist `has_aio`, evidence freshness, completeness score or null, click intent, verdict, reasoning, body source or null, and uncertainties in the Stage 01 packet. Do not write caches or trigger later work.
