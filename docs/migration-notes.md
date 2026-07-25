# Migration notes

## Architecture

Paperclip supplied the schedule, controller/child lifecycle, stage handoffs, and recordkeeping. The skills were local instruction packages in the blog-engine workspace. Ahrefs, analytics, product truth, and the CMS were external inputs/services.

## Buzz mapping

- Paperclip routine issue → Buzz workflow run.
- Paperclip child issue → current-stage workflow node.
- Paperclip receipt/comment → stage log plus attached artifact.
- Paperclip schedule → Buzz scheduler.
- Paperclip task packet → run workspace or channel attachment.

## Do not migrate

Do not copy credentials, private keys, VPS paths, CMS tokens, logs, customer data, browser sessions, or Paperclip identifiers. Ignore legacy skill text that refers to Semrush, DataForSEO, OpenRouter, five posts per week, or unconditional auto-publishing. The portable contract uses Ahrefs evidence, four weekly attempts, and quality-gated publication.
