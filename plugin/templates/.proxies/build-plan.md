# BUILD-PLAN — [Project Name] Deferred Work

All deferred work in one place. Five sections, top-to-bottom priority. Build batches live in individual files — this index carries the order.

*Full spec: `DOC-STRUCTURE.md` → BUILD-PLAN structure.*

## Red flags

Security, privacy, data integrity, or safety concerns surfaced by Claude and deferred by the user. Removed when addressed. Starts empty.

Format: `DOC-STRUCTURE.md` → *BUILD-PLAN structure → Red flags*.

## Planning batches

Two kinds: **(a)** questions blocking a specific build batch, **(b)** scope-existence questions deciding whether a build batch should exist. Each has a heading, questions, and a `Blocks:` line. Resolution: append the answer and add a `[PROPOSED EDIT PENDING]` block to the destination doc. Leave the batch in place — the user removes it when applying the edit.

<!--
### Planning batch: [short name]

- [Question]
- [Question]

Blocks: [build batch name].
(For scope-existence: Blocks: scope decision — no build batch yet.)
-->

## Build batches

Engineering work, top-to-bottom priority. Each batch lives in its own file — reorder lines here to change priority. A change belongs here only if it serves a `UX.md` entry (or additional source-of-truth doc). Items without such traceability are Discoveries — they need a planning batch first.

<!--
- `NNNN-batch-name.md` — [one-line description]

NNNN is allocated at creation, never changes. Reorder by moving lines.
-->

## Open questions

Questions worth tracking that don't block a specific build yet. Each has a question, context, and a next-step trigger. The planning procedure scans this section at every planning session start. When a question blocks something specific, promote to a planning batch.

<!--
### [Short question title]

[One paragraph framing the question.]

**Why it matters.** [Context.]

**Next step.** [What resolves or promotes this.]
-->

## Ideas

Raw, unprocessed ideas captured during any session type. Date + one-liner. Claude can write here regardless of build phase. `/sovideate` or `/sovdeliberate` promotes ideas to OQs or batches.

<!--
- YYYY-MM-DD — [One-line description of the idea]
-->

---
*No-code method — Version 91.*
