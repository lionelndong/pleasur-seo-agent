---
name: keyword-vet-bid
description: Validate Pleasur.ai blog-keyword candidates with the Business potential, Intent, and Difficulty method using current Ahrefs evidence. Use during Stage 01 candidate validation before prioritization.
---

# Keyword Vet — BID

Validate every candidate; do not manufacture a winner. Read [references/bid-policy.md](references/bid-policy.md) before scoring.

## Evidence contract

- Use the configured Ahrefs MCP integration only. Inspect its live schemas before requesting fields.
- Require an approved, versioned brand/product snapshot, target country, and content inventory.
- Record tool/report, exact query, country, selected fields, filters, retrieval time, provider freshness/reference, status, and error.
- Never expose credentials, substitute another provider, turn null into zero, average conflicts, or rely on legacy caches.
- Return `needs_data` when required evidence is missing, stale, contradictory, country-mismatched, rate-limited beyond the bounded retry policy, or unavailable.

## Apply BID

1. Score `brand_fit` and `product_fit` from the approved snapshot. Fail Business when `brand_fit < 4`, `product_fit < 3`, or there is no credible path to users/revenue. Set `business_value` from genuine product usefulness; never reward salesy wording. Flag free-seeker intent without automatically rejecting it.
2. Use Ahrefs intent classification as primary evidence. Pass blog-suitable informational or commercial investigation. Reject dominant transactional or navigational intent. When ambiguous, classify the current top ten by page type and title. Route tool-led SERPs out of the blog queue.
3. Compare the current top-ten SERP with current Pleasur.ai DR. Pass Difficulty only when median top-ten DR is at most `brand_dr + 12` or at least two genuinely weak results are present. KD is supporting evidence, never a standalone gate.
4. Emit a reasoned gate result for every candidate. Complete evidence plus a failed gate is `rejected`; incomplete evidence is `needs_data`.

Preserve evaluated failures for audit. Do not write CSVs, caches, repositories, or production systems. Add the evaluations and exact provenance to the Stage 01 validated-research packet.
