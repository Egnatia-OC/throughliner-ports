# BACKLOG.md — [Project Name] Deferred Work

All deferred work in one place. Four sections, in this order; top section first, top item first.

*Full spec for these sections: `DOC-STRUCTURE.md` → BACKLOG.md structure.*

## Red flags

Security, privacy, data integrity, or safety concerns Claude has surfaced and the user has chosen to defer. Items are removed when addressed. Section starts empty for new projects.

For the canonical entry format, see `DOC-STRUCTURE.md` → *BACKLOG.md structure → Red flags*.

## Planning batches

Two kinds of question live here. **(a)** Open questions that must be resolved before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist. Each planning batch is a heading, the questions to answer, and a `Blocks:` line. Resolution: append the answer to the planning batch and add a `[FOLD-IN PENDING]` block to the destination doc's *Fold-ins pending* section (with this batch's name in the block's *origin* field). Leave the planning batch in place — the user removes it by hand during the same planning session in which they fold the answer in.

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

Inputs:
- `[path/to/resource]` — [why this batch needs it]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Serves UX.md: [entry name(s)].

### Batch: [short descriptive name]

- [Suggested] [Change description]
- [Requested] [Change description]

Inputs:
- `[path/to/resource]` — [why this batch needs it]

Files:
- [ ] `[path/to/file]` — [one-sentence summary of the change]
- [ ] `[path/to/file]` — [one-sentence summary of the change]

Serves UX.md: [entry name(s)].
[For batches touching an additional source-of-truth doc, add a `Serves <DOC>: ...` line. Two forms: `Serves <DOC>: [entry/section name].` when the batch implements the doc's content (e.g., `Serves SYSTEM-PROMPT.md: tone and presentation section.`); `Serves <DOC>: [delivery mechanism].` when the batch's purpose is to carry the doc to its runtime destination rather than implement any of its content (e.g., `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt.`).

`Inputs:` is optional — omit it entirely if the batch only needs the standard docs (UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md) that Claude reads every session. Include it when the batch depends on a specific additional resource: a research file, an open-questions entry, a draft, an additional source-of-truth doc, or an external reference.]

## Open questions

Questions worth tracking that aren't blocking a specific build batch yet. Each entry has a question, brief context, and a next-step trigger describing what would promote it to a planning batch or resolve it. The planning subagent scans this section at the start of every planning session and lists all entries with their triggers.

When an open question matures to the point where it blocks a specific build, promote it to a planning batch above.

<!--
Entry format:

### [Short question title]

[One paragraph framing the question.]

**Why it matters.** [Brief context — who raised it, what's at risk.]

**Next step.** [What would resolve or promote this — e.g. "promote to planning batch if X happens", "fold into next batch touching Y", "park until Z".]
-->

---
*No-code method — Version 44.*
