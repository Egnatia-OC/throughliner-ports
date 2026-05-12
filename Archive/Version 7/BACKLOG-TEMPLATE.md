# BACKLOG.md — [Project Name] Deferred Work

All deferred work in one place. Three sections, in this order; top section first, top item first.

## Red flags

Security concerns Claude has surfaced and the user has chosen to defer. Each item is a blockquote starting with **`[RED FLAG]`** in bold, then a one-line description, then the context (which batch, when found). Items are removed when addressed.

> **`[RED FLAG]`** [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix description].

[Delete the example above when filling in real items. Section starts empty for new projects.]

## Planning batches

Open questions that must be resolved before some build batch can run. Each planning batch is a heading plus the questions to answer, plus a one-line note saying which build batch it blocks. Once resolved, fold answers into the relevant `UX.md` entries and remove the planning batch.

### Planning batch: [short descriptive name]

- [Question to answer — one line]
- [Question to answer]

Blocks: [build batch name].

### Planning batch: [short descriptive name]

- [Question to answer]

Blocks: [build batch name].

[Delete the example batches when filling in real ones.]

## Build batches

Engineering work, ordered top-to-bottom by priority. The top batch is the next build (after any one currently in progress). Each batch must be small enough to build and test in one sitting. If a batch grows past that, split it.

A change only belongs here if it serves a `UX.md` entry. Items that don't trace to `UX.md` are Discoveries, not build items — they need a planning batch (or a `UX.md` update) before they enter this section.

### Batch: [short descriptive name]

- [Change description — one line]
- [Change description]
- [Change description]

### Batch: [short descriptive name]

- [Change description]
- [Change description]

[Delete the example batches when filling in real ones.]
