# BACKLOG.md — [Project Name] Deferred Work

All deferred work in one place. Four sections, in this order; top section first, top item first.

*Full spec for these sections: `DOC-STRUCTURE.md` → BACKLOG.md structure.*

## Red flags

Security, privacy, data integrity, or safety concerns Claude has surfaced and the user has chosen to defer. Items are removed when addressed. Section starts empty for new projects.

For the canonical entry format, see `DOC-STRUCTURE.md` → *BACKLOG.md structure → Red flags*.

## Fold-ins pending

Proposed source-of-truth content that Claude (the agent) has formed but cannot write directly. Each block waits here until the user folds it into the destination doc by hand during their next planning session (or drops it). Created by any route that would otherwise write a read-only doc — new-project, migration, mid-build hook intercept, planning resolution — all land here. Items are removed once folded in or dropped. Section starts empty for new projects.

For the canonical block format, see `DOC-STRUCTURE.md` → *BACKLOG.md structure → Fold-ins pending*.

## Planning batches

Two kinds of question live here. **(a)** Open questions that must be resolved before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist. Each planning batch is a heading, the questions to answer, and a `Blocks:` line. Resolution: append the answer to the planning batch and add a fold-in-pending block to the *Fold-ins pending* section above (with this batch's name in the block's *origin* field). Leave the planning batch in place — the user removes it by hand during the same planning session in which they fold the answer in.

### Planning batch: [short descriptive name]

- [Question to answer — one line]
- [Question to answer]

Blocks: [build batch name].

### Planning batch: [short descriptive name — scope-existence example]

- [Question to answer — e.g. "should this app even have a search box?"]

Blocks: scope decision — no build batch yet.

[Delete the example batches when filling in real ones.]

## Build batches

Engineering work, ordered top-to-bottom by priority. The top batch is the next build (after any one currently in progress). Each batch must be small enough to build and test in one session. If a batch grows past that, split it.

A change only belongs here if it serves a `UX.md` entry (or an entry in a relevant additional source-of-truth doc). Items that don't trace to such an entry are Discoveries, not build items — they need a planning batch (or a `UX.md` update) before they enter this section.

### Batch: [short descriptive name]

- [Requested] [Change description — one line]
- [Suggested] [Change description]
- [Requested] [Change description]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Serves UX.md: [entry name(s)].

### Batch: [short descriptive name]

- [Suggested] [Change description]
- [Requested] [Change description]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Serves UX.md: [entry name(s)].
[For batches touching an additional source-of-truth doc, add a `Serves <DOC>: ...` line. Two forms: `Serves <DOC>: [entry/section name].` when the batch implements the doc's content (e.g., `Serves SYSTEM-PROMPT.md: tone and presentation section.`); `Serves <DOC>: [delivery mechanism].` when the batch's purpose is to carry the doc to its runtime destination rather than implement any of its content (e.g., `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt.`).]

---
*No-code method — Version 27.*
