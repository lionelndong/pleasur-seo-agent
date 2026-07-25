# Existing-Content Portfolio Improvement System

This is the durable operating contract for existing content. It implements the Ahrefs course as a
portfolio system, not as a daily broken-link crawl.

## The Four Lanes

| Lane | Owner and cadence | Job | Terminal output |
|---|---|---|---|
| New content | Existing publishing routine | Create a genuinely new page only after the Course Formula Gate passes. | Published, no-publish, no-op, or blocked with a real dependency. |
| Portfolio review | Weekly routine | Compare customer, GSC, Ahrefs, integrity, and link-equity evidence; classify candidates; select at most one action. | One selection packet plus at most one focused child issue, or a measured no-op. |
| Focused execution | One child of the review | Work one URL and one action type in `recommend_only` or `preview_only` unless a stronger gate explicitly authorizes execution. | Recommendation/preview, shipped small repair, or blocked disposition. |
| Measurement | Weekly routine; 14-21 day cooldown | Measure due relaunches and repairs against their recorded baselines. | Keep, iterate, revert recommendation, or insufficient-data cooldown. |

New content and existing-content improvement are separate, equally important responsibilities.
Neither lane may quietly consume the other. Planning should reserve roughly half of editorial
effort for existing-content improvement over a rolling four-week window; do not force work when
the evidence says `no_op`.

## Evidence Contract

The EO agent cannot control the operator's signed-in Chrome session. Browser evidence is therefore
a brokered Paperclip packet, never an implied agent capability.

`dataAccessMode` values:

- `brokered_chrome_ahrefs_packet` (default): a trusted board browser broker exports native Ahrefs
  CSV/ZIP files from the operator's signed-in local Chrome session and attaches them to a Paperclip
  packet issue with a manifest. CSV/ZIP are authoritative; screenshots are provenance only.
- `self_service_ahrefs_browser`: alternate only when EO has a working authenticated browser and can
  export current-run files itself. Fail closed on authentication, CAPTCHA, or download failure.
- `live_ahrefs_api`: disabled until an operator records a successful token check and explicitly
  changes the mode. Never fall back to it when the token pool is exhausted.

Every packet artifact must match its manifest on filename, byte size, SHA-256, row/container count,
expected columns, report path, target, country, filters/window, captured time, and Paperclip
attachment URL. The default freshness ceiling is 72 hours. A filename, narrative claim, later export
time, or screenshot alone is not evidence and must not make stale underlying data fresh.

Keep these evidence types distinct:

| Evidence | Answers | Must not be treated as |
|---|---|---|
| Customer/revenue/product analytics | Which pages or paths create customers, orders, activation, or valuable product use? | Traffic volume. |
| GSC, standard window | Which pages/queries changed in clicks, impressions, CTR, and position over complete 28-day vs prior 28-day periods? | Link equity or revenue. |
| Ahrefs Top pages / Organic keywords | Which existing URLs have ranking/traffic potential or loss, and what is the link/ranking context? | First-party conversion proof. |
| Ahrefs Site Audit | Internal technical and link integrity, including links to 4xx/5xx targets. | External backlinks. |
| Ahrefs Broken backlinks / Best by links | External referring pages and link equity pointing at missing/redirected targets. | An internal sitemap crawl. |
| Live HTTP/render checks | Whether a specific page, link, CTA, asset, or metadata element works now. | Portfolio prioritization by itself. |

If page-level GSC or customer data is unavailable, lower confidence; do not invent it. Aggregated or
anonymized GSC totals may describe the site but cannot prove which page should be changed.

## Candidate Register And Priority

Write every reviewed candidate to a register before choosing work. First assign one class:

1. `P0_live_integrity`: current 4xx/5xx, broken customer path, missing critical asset, or harmful
   rendering defect.
2. `P1_customer_revenue_loss`: measured customer, order, activation, or revenue loss tied to a URL.
3. `P2_rank_conversion`: ranking/traffic decline, CTR loss, intent mismatch, weak product proof, or
   conversion-path opportunity on an existing page.
4. `P2_link_equity`: external backlinks or referring domains point to a missing, redirected, or
   wrong target.
5. `P3_maintenance`: low-risk metadata, internal-link, freshness, or visual maintenance without a
   stronger business signal.
6. `no_op`: no candidate has enough evidence or the candidates are already open/in cooldown.

Higher classes outrank lower ones. Within a class, record 1-5 values and calculate:

```text
Priority = Business Value x Impact x Confidence x Urgency / Effort
```

Normalize only for display; keep the raw factors and citations. Before selection, check existing
issues, run manifests, and the measurement registry. Do not reopen the same URL/action while it is
active or inside cooldown.

## Allowed Actions

Classify the chosen target as exactly one of:

- `update`: improve the current page without a new public launch.
- `relaunch`: materially rebuild, re-promote through an approved handoff, and measure after 14-21
  days.
- `merge`: recommend consolidation and redirect mapping; destructive execution needs approval.
- `delete`: recommend removal/deindexing with evidence; execution needs approval.
- `leave`: retain the page and record why.
- `technical_repair`: fix one verified small defect.
- `conversion_repair`: improve one verified customer path or product-proof defect.

Broken backlinks are a tactical `P2_link_equity` input. The action may be restore, redirect, reclaim,
merge, or leave; never assume the answer is editing every internal link.

## Action Gates

- `recommend_only`: analysis and recommendation; no public write.
- `preview_only`: artifacts and preview may be created; no publish, redirect, delete, deindex,
  outreach, or public promotion.
- Small technical repair: needs exact before evidence, bounded scope, rollback note, and post-check.
- Relaunch: needs Fix Promise, uniqueness/authority/quality gates, preview approval, a promotion
  handoff, baseline, and a measurement date.
- Conversion repair: needs a first-party customer-path hypothesis and post-change measurement.
- Merge/delete/redirect/deindex: recommendation only until explicitly approved.
- Outreach or public promotion: handoff only until explicitly approved.

The parent review creates at most one focused child issue. The child receives only the selected
target, action, evidence URLs, gate, expected artifact, baseline, and measurement date. It must
also copy the parent's `dataAccessMode`, `evidencePacketIssue`, `evidencePacketManifest`,
`ahrefsCapturedAt`, `freshnessMaxHours`, and `targetCountry` verbatim. In
`brokered_chrome_ahrefs_packet` or `self_service_ahrefs_browser` mode, neither the parent nor the
child may probe Ahrefs REST/MCP/API, even to test remaining units; only validated Ahrefs work
products are allowed. Missing or stale evidence produces a precise no-op.

If `targetUrl` is populated on a portfolio-review fire, treat the run as a bounded validation and
score only that URL. Do not expand back to the full portfolio.

## Cooldown And Measurement Registry

Maintain `content-pipeline/portfolio/measurement-registry.csv` with:

```text
target_url,action,execution_issue_id,shipped_at,baseline_window,measure_on,measurement_window_days,
success_metric,guardrail_metric,status,last_result_issue_id
```

Default `measurementWindowDays` is 21; 14 is the minimum when the metric is sufficiently active.
The measurement routine processes only rows due on or before the run date. An incomplete window is
`insufficient_data`, advances `measure_on`, and closes the current routine issue; it is not left
open across fires.

## Paperclip Lifecycle

- Every routine fire creates a new execution issue.
- Use `coalesce_if_active` and `skip_missed` for the portfolio and measurement schedules.
- Never keep a routine issue open to wait for the next fire.
- A selection+child parent records `blockedByIssueIds` but remains `in_progress` while the child
  runs; Paperclip will wake it when the child reaches a terminal state. Do not set the parent issue
  to `blocked`, because routine execution treats that as a failed fire. The resumed parent closes
  `done` after validating the child's terminal disposition.
- Every run ends `done`, except a genuine external dependency that cannot be represented by the
  focused child lifecycle may end `blocked` with a named owner/action.
- Never use `blocked` to mean "nothing was worth doing." That is `no_op` and `done`.
- Do not create more than one active focused child from a review.

## Routine Variables

Use the smallest relevant set:

- `dataAccessMode`: `brokered_chrome_ahrefs_packet` | `self_service_ahrefs_browser` |
  `live_ahrefs_api` (disabled).
- `scope`: default `existing_content_portfolio`.
- `targetUrl`: required only for a focused manual execution.
- `workType`: `portfolio_review` | `update` | `relaunch` | `merge` | `delete` | `leave` |
  `technical_repair` | `conversion_repair` | `measurement`.
- `runMode`: `recommend_only` | `preview_only` | `quality_gated_live`.
- `targetCountry`: default `us` unless evidence explicitly uses another market.
- `evidencePacketIssue`: explicit packet issue or `AUTO_LATEST_FRESH_PACKET`.
- `evidencePacketManifest`: explicit manifest attachment or `AUTO_FROM_PACKET_ISSUE`.
- `ahrefsCapturedAt`: ISO timestamp for the underlying report capture.
- `freshnessMaxHours`: default `72`.
- `measurementWindowDays`: default `21`.

## Required Review Artifacts

For each run create `content-pipeline/portfolio-runs/{issue-key}/`:

- `evidence-index.md`: each report, window/filter, observation time, and Paperclip artifact URL.
- `candidate-register.csv`: candidate class, action, raw score factors, priority, evidence citations,
  active-work check, cooldown check, and disposition.
- `selection.md`: selected target or no-op, why it outranked alternatives, gate, and child issue ID.
- `measurement-baseline.md` when a child may ship.

The completion comment must link these artifacts and the focused child/measurement row when one
exists.
