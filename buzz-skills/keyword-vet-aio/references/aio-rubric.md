# AIO completeness rubric

Score the observed Google AI Overview body against the full search need. Use the current keyword, intent, country, and body evidence; do not score presence alone.

## Score bands

- `8–10` — substantially complete. It directly answers the query, covers the important sub-needs, gives enough specificity to act, and leaves little value in clicking.
- `5–7` — partial. It answers the core question but a reader still benefits from examples, proof, comparison criteria, nuance, firsthand evidence, depth, or action steps.
- `0–4` — shallow, generic, incorrect, off-intent, or materially incomplete. Regular results retain meaningful click value.

Use the full range. Do not force each run to contain every band.

## Click-intent labels

- `yes-deep` — the reader still needs substantial detail or evidence.
- `yes-shallow` — the reader may click for one narrow missing element.
- `no` — clicking would be largely redundant.

The score and click label must agree. Resolve any mismatch in the second review pass.

## Intent application

For informational intent:

- `8–10` and `no` → `FAIL_CANNIBALIZED`;
- `5–7` → `RISKY`;
- `0–4` → `PASS`.

For comparison or commercial-investigation intent, test whether readers still need multiple options, explicit selection criteria, verifiable evidence, product-specific tradeoffs, or firsthand comparison. High completeness does not receive an automatic exemption.

For tool-led intent, route outside the blog queue rather than using AIO scoring to justify a blog post.

## Required rationale

Write one evidence-specific sentence that names:

1. what the AIO answers well;
2. the most important satisfied or missing need; and
3. why that leaves deep, shallow, or no click intent.

Reject generic rationales such as “good overview,” “needs more depth,” or “users may still click” without naming the actual content gap.

## Calibration

Human editors should periodically spot-check representative queries across score bands. If scores drift high or low, revise the rubric through reviewed source control; do not insert runtime-specific model routing or force a target distribution.
