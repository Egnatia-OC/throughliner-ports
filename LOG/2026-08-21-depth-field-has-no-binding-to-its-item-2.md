# 15e10c9 — Depth lines are slug-bound, and the close reads them by slug rather than position

Build entry; the planning record is `2026-08-21-depth-field-has-no-binding-to-its-item.md`. Two depth lines once landed together and attached to the wrong items; the close reconstructed the intent from context, which a fresh short session cannot do. Built with the binding as the fix: the format is now `Depth: <slug> — short|full`, written at the tick, and done-build.md reads each built item's line by slug — a built slug with no depth line is the discipline-slip flag for free, subsuming the count-check alternative. One discrepancy worth recording: the item named next-build.md as the authoring site, and the build's own grep (which the item required) found the field defined in next.md's per-item completion step — next.md was edited and appended to the run's file list before the write. This run's own working file used the slug-bound form throughout.

**Files touched:** `plugin/throughliner/docs/next.md`, `plugin/throughliner/docs/done-build.md`.
**Routed to Captures:** none from this item.
Tick: done, confirmed — project-wide grep shows no doc still describing a bare positional Depth line.
FAQ: not needed because the working file is internal machinery.
Rule gate: run — an amendment to the per-item completion step (the field's format gains the slug) and done-build.md's read (by slug rather than position). A format the docs define, not hook-enforced — `pre_tool_use.py` does not parse depth lines, checked at the build's grep.
