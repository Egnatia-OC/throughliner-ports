# ee238d1 — Guard audit batches against direct doc-writes: plan.md authoring guard + next-audit.md execution guard + FAQ

Built in a six-batch goal session (plugin off).

An audit's findings are supposed to route to Captures only, so /plan and the user can vet them before anything durable is written — next-audit.md states this as the audit's defining contract. But a consumer audit batch (message-audit-4, in an E2E project, 2026-06-22) was authored as an Audit while naming a findings doc in its Files and setting an Output of "append candidates to" that doc. When /next ran it, the session followed the batch's Output and prepared to write straight into the durable doc, silently overriding the route-to-Captures contract — no capture appeared until the user asked for one. Her actual intent was a vetted, lawyer-facing doc eventually, not a write at the audit stage, so the doc-write was a misread of her need.

Two guards installed so the misread can't recur:

- **Authoring-time guard (plan.md).** The findings-vs-decisions ground rule now states the audit's output contract mechanically: an audit names no write-target doc in its Files and sets no file-writing Output. A fuller guard sits in Step 3's batch-structure guidance — when the deliverable is a written document, that document is a *build* authored later from vetted findings, and the flow is audit → Captures → /plan → a build batch that writes the doc. It names the worked slip to avoid (an Audit batch that lists a findings doc and sets an "append candidates to" Output is a feature build wearing an audit's label; split it).
- **Execution-time guard (next-audit.md).** A new pre-read step: if the running batch's Output directs a write into a named doc, that contradicts the route-to-Captures contract — surface the conflict in plain language and ask which the user wants (file findings as captures, or run it as a build that writes the doc now), rather than silently following the batch's Output. Carries a plain-English exemplar.

FAQ entry added (why an audit files findings as captures instead of writing them into a named doc, and how to get a durable findings doc the right way) plus its index line.

Test is host-side and self-verifying from the build entries (a review, not a pass/fail) — deferred line written for the first audit session after push + reinstall.
