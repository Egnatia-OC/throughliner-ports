# BACKLOG.md — [Project Name] Deferred Work

All deferred work in one place. Three sections, in this order; top section first, top item first.

Maintained by Claude during planning sessions. The user does not maintain this file directly — when a planning decision changes the backlog, Claude edits this file.

A change only belongs here if it serves a `UX.md` entry. Items that don't trace to `UX.md` are Discoveries, not backlog items — they need a `UX.md` update before they enter this file. (Red flags are the exception — see below.)

## Red flags

Security, privacy, data integrity, or safety concerns that Claude has surfaced and the user has chosen to defer rather than address now. Each entry is a blockquote in the format below — description + when found + shortest possible fix. Items are removed from this section once addressed.

> **`[RED FLAG]`** [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix description].

[Delete the example above when filling in real items. Section starts empty for new projects. Claude populates this section per the "Red flags — screen and surface" rule in `CLAUDE.md`.]

## Planning batches

Open questions that must be resolved before some build batch can run. Each planning batch lists the questions to answer and which build batch (or batches) it blocks. Once resolved, fold answers into the relevant `UX.md` entries and remove the planning batch.

### Planning batch: [short descriptive name]

- [Question to resolve.]
- [Question to resolve.]

Blocks: Build batch — [name of the build batch this blocks, or "Nothing currently" if not blocking specific work].

[Delete the example planning batch above and add real ones during planning.]

## Build batches

Engineering work. The top batch is the next build (after any one currently in progress). Each batch must be small enough to build and test in one sitting. If a batch grows past that, split it.

### Batch: [short descriptive name]

[Optional: one-line framing for the batch — what's the smallest thing this batch proves or delivers?]

- [Change description — one line.]
- [Change description.]
- [Change description.]
- Serves UX.md: *[entry name]*, *[entry name]*.

### Batch: [short descriptive name]

- [Change description.]
- [Change description.]
- Serves UX.md: *[entry name]*.

[Delete the example build batches above and add real ones during planning.]
