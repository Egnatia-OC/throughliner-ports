# BACKLOG.md — [Project Name] Deferred Work

All deferred work and test tracking in one place. Five sections, in this order; top section first, top item first.

*Full spec for these sections: `DOC-STRUCTURE.md` → BACKLOG structure.*

## Red flags

Security, privacy, data integrity, or safety concerns Claude has surfaced and the user has chosen to defer. Items are removed when addressed. Section starts empty for new projects.

For the canonical entry format, see `DOC-STRUCTURE.md` → *BACKLOG structure → Red flags*.

## Planning batches

Two kinds of question live here. **(a)** Open questions that must be resolved before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist. Each planning batch is a heading, the questions to answer, and a `Blocks:` line. Resolution: append the answer to the planning batch and add a `[PROPOSED EDIT PENDING]` block to the destination doc's *Proposed edits pending* section (with this batch's name in the block's *origin* field). Leave the planning batch in place — the user removes it by hand during the same planning session in which they apply the proposed edit.

<!--
Planning batch format:

### Planning batch: [short descriptive name]

- [Question to answer — one line]
- [Question to answer]

Blocks: [build batch name].

For scope-existence questions, use: Blocks: scope decision — no build batch yet.
-->

## Build batches

Engineering work, ordered top-to-bottom by priority. The top batch is the next build (after any one currently in progress). Each batch must be small enough to build and test in one session. If a batch grows past that, split it.

A change only belongs here if it serves a `UX.md` entry (or an entry in a relevant additional source-of-truth doc). Items that don't trace to such an entry are Discoveries, not build items — they need a planning batch (or a `UX.md` update) before they enter this section.

<!--
Build batch format — two regions: scope context (Goal through Dependencies/Red flags)
and build operations (Changes through Serves). Full spec: DOC-STRUCTURE.md → Build batches.

### Batch: [short descriptive name]

Status: [queued|parked]  ← written by Claude; absent = queued. Legacy active/shipped still recognized

**Goal.** [One paragraph — why this batch exists, what will be different when it ships.]

**Outputs.** [Prose — what changes the user will experience after the batch ships.]

**Success criteria.** [Observable, testable conditions for knowing the batch succeeded.]

**Dependencies.** [What this batch needs from outside itself. Omit if none.]

**Red flags.** [Security/privacy/data-integrity concerns. Only present when detected.]

Changes:
- [Requested] [Change description — one line]
- [Suggested] [Change description]

Inputs:
- `[path/to/resource]` — [why this batch needs it]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Tests:
- [Test description] [Look and click] [User]
- [Test description] [Run and read] [Claude]

Serves UX.md: [entry name(s)].

Notes:
- Goal, Outputs, Success criteria are always present. Dependencies omitted if none.
- Red flags appears only when planning detects security-shaped scope.
- Changes: delimiter is required — separates scope sections from the change list.
- Inputs: is optional — omit if the batch only needs standard docs.
- Tests: is optional — omit if no pre-specification needed.
- For additional source-of-truth docs, add Serves <DOC>: ... line.
-->

## Test sessions

One row per test for every shipped build batch. Per-session files in `test-log/`, newest-first in this index. Maintained by Claude during builds (`/sovclose` writes rows) and planning (per-row read-back confirms). The test-confirmation gate gates new builds against unconfirmed rows.

Full spec: `DOC-STRUCTURE.md` → *TEST-LOG structure*.

<!--
Index format (newest first):
- `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed)
-->

## Open questions

Unscoped captures — from quick one-liner thoughts to fleshed-out questions. Not blocking a specific build batch yet. `/sovdeliberate` works through accumulated entries: promotes to planning batches, resolves, or drops.

Light entries need only a heading, Surfaced tag, and one sentence. Full entries add Why it matters and Next step when the question has enough shape to benefit from them.

<!--
Entry format — full:

### [Short question title]

**Surfaced.** [Session tag or build-cycle identifier when this entry was created, e.g. "Batch: auth overhaul".]

[One paragraph framing the question.]

**Why it matters.** [Brief context — who raised it, what's at risk.]

**Next step.** [What would resolve or promote this — e.g. "promote to planning batch if X happens", "incorporate into next batch touching Y", "park until Z".]

Entry format — light (quick capture):

### [Short title]
*Surfaced: [session tag]*

[One sentence describing the thought or question.]
-->

---
*Sovereign Implementer — Version 111.*
