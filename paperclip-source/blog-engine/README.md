# Pleasur.AI blog engine

This workspace supports the PLE blog publishing system. For work created by the active four-times-per-week new-content routine, the authoritative contract is [`references/eo-blog-routine/execution-contract.md`](references/eo-blog-routine/execution-contract.md).

The routine runs Monday, Tuesday, Thursday, and Friday at 09:00 America/New_York. Each fire is a quality-gated attempt with at most one public article and no more than four per week. The active SEO-data lane uses board-supplied/browser-exported Ahrefs evidence; agents must not call paid SEO or research APIs.

New-content publishing is separate from existing-content portfolio improvement and measurement. Do not combine their queues, manifests, schedules, or success criteria.

Key commands:

```bash
python scripts/pipeline_gate.py <stage-key> <slug>
python scripts/validate_run_contract.py --slug <slug> --run-key <run-key> --mode preview
```

Read `brand-config.md`, the execution contract, and the referenced checklists before acting. A prose claim that a skill or gate ran is not evidence; stage receipts and hash-verified artifacts are required.
