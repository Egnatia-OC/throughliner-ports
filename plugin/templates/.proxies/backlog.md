# BACKLOG — [Project Name] Deferred Work

All deferred work and test tracking in one place. Five sections, top-to-bottom priority. Build batches live in individual files — this index carries the order. Test session files live in `test-log/`.

*Full spec: `DOC-STRUCTURE.md` → BACKLOG structure.*

## Red flags

Security, privacy, data integrity, or safety concerns surfaced by Claude and deferred by the user. Removed when addressed. Starts empty.

Format: `DOC-STRUCTURE.md` → *BACKLOG structure → Red flags*.

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

## Test sessions

One row per test for every shipped build batch. Per-session files in `test-log/`, newest-first in this index. Maintained by Claude during builds (`/sovclose` writes rows) and planning (per-row read-back confirms). The test-confirmation gate gates new builds against unconfirmed rows.

Full spec: `DOC-STRUCTURE.md` → *TEST-LOG structure*.

<!--
Index format (newest first):
- `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed)

Entry file format:

# Test session — <Session> — YYYY-MM-DD

| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 001 | ... | ... | ... | ... | ... | ... | ... | ... | ... |
-->

## Open questions

Unscoped captures — from quick thoughts to fleshed-out questions. `/sovdeliberate` works through accumulated entries. Light entries need only a heading, Surfaced tag, and one sentence. Full entries add Why it matters and Next step.

<!--
Full format:

### [Short question title]
*Surfaced: [session tag]*

[One paragraph framing the question.]

**Why it matters.** [Context.]

**Next step.** [What resolves or promotes this.]

Light format:

### [Short title]
*Surfaced: [session tag]*

[One sentence.]
-->

---
*Sovereign Implementer — Version 110.*
