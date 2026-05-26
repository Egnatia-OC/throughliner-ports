# v56 — 2026-05-22 — Validation + warnings bundle

**What shipped.** Scope 0054. Four "six prose directives" items plus `[FOLD-IN PENDING]` → `[PROPOSED EDIT PENDING]` rename. (1) `Serves <DOC>:` validation extended to all path-block docs (matches against `##` headings, excludes structural sections). (2) Red flags non-empty warning at SessionStart. (3) Deferred build-material aging in planning subagent (folder-mode batch-number comparison). (4) Rename across all live plugin files. Footer V50→V51; plugin 0.50.0→0.51.0. 8 new tests. Scope 0060 created.

**Decisions.** Additional-doc entries match `##` headings (additional docs use `##`, unlike UX.md's `###`). Structural sections excluded via frozen set. Rename bundled because all four items touched the same files.

**Carried forward.** Deferred smoke tests unchanged. "Six prose directives" items 2–4 resolved; 5–6 remain (→0055).

