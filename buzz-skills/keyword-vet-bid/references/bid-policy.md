# BID policy

## Business

- `brand_fit`: 10 direct pain point; 7 strongly relevant; 4 adjacent but useful; 0 wrong audience.
- `product_fit`: 10 product is essential to a strong answer; 7 strong demonstration; 4 natural mention; 0 no relevant product.
- Pass only at `brand_fit >= 4`, `product_fit >= 3`, and `business_value >= 2`.
- Flag queries centered on free, unlimited, no-account, or no-payment access as `free_seeker`.

## Intent

Prefer Ahrefs intent evidence. Accept informational and commercial-investigation blog intent. Reject dominant transactional or navigational intent. Route tool-led SERPs when at least three of the top five results are tools, calculators, or generators.

## Difficulty

Calculate median DR from ten usable organic results. Pass when `median_top10_dr <= brand_dr + 12` or `weak_link_count >= 2`. A weak result must have evidence such as low relative authority/link strength, poor intent match, thin coverage, or a clearly displaceable page type. Record named weak URLs and the displacement rationale.
