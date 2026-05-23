# BACKLOG — [Project Name] Deferred Work

All deferred work in one place. Four sections, in this order; top section first, top item first. Build batches live in individual files in this folder — this index carries the build order.

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

Engineering work, ordered top-to-bottom by priority. The top entry is the next build (after any one currently in progress). Each batch lives in its own file in this folder — reorder entries here to change priority without renaming files.

A change only belongs here if it serves a `UX.md` entry (or an entry in a relevant additional source-of-truth doc). Items that don't trace to such an entry are Discoveries, not build items — they need a planning batch (or a `UX.md` update) before they enter this section.

<!--
Build-order list format — one entry per batch file:

- `NNNN-batch-name.md` — [one-line description]

The NNNN number is allocated at creation time and never changes. Reordering
means moving lines in this list, not renaming files.
-->

## Open questions

Questions worth tracking that aren't blocking a specific build batch yet. Each entry has a question, brief context, and a next-step trigger describing what would promote it to a planning batch or resolve it. The planning subagent scans this section at the start of every planning session and lists all entries with their triggers.

When an open question matures to the point where it blocks a specific build, promote it to a planning batch above.

<!--
Entry format:

### [Short question title]

[One paragraph framing the question.]

**Why it matters.** [Brief context — who raised it, what's at risk.]

**Next step.** [What would resolve or promote this — e.g. "promote to planning batch if X happens", "incorporate into next batch touching Y", "park until Z".]
-->

---
*No-code method — Version 57.*
