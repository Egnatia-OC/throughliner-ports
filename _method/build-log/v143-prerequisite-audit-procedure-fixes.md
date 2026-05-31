# v143 — 2026-05-29 — Prerequisite-audit procedure fixes

**What shipped.** Completed batch 0143. Fixed all 5 procedure-doc gaps identified by the v142b skill invocation audit, aligning procedure docs with V90 build-snapshot architecture.

- `tersify.md` phase gate: replaced dead `Status: active` check with `_method/active-build.md` existence check.
- `build.md`: added halt when parser returns a batch with empty `files` array (catches skipped `/sovrecap`).
- `planning.md` and `deliberate.md`: softened "never during builds" to "not in the same session as a build" with a note that V90 permits parallel-session planning.
- `before-build.md`: added active-build check at top — halts if build already in progress.
- `testing.md`: added mid-build invocation note explaining that test rows don't exist yet.

**Decisions taken and why.** Did not change `ideate.md` — the audit cited it as saying "never during building" but the actual file already lacked that restriction. No change needed.

**Pivots and surprises.** None. All five changes were straightforward text edits as scoped.
