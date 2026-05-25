# v47 — 2026-05-22 — Distributed fold-ins + BACKLOG open-questions + batch Inputs line

**What shipped.** V45 scope. Three structural changes: (1) Fold-in blocks moved from centralized BACKLOG section to `## Fold-ins pending` at bottom of each destination doc (UX.md, MANIFEST.md, etc.). PreToolUse gained `is_fold_in_section_edit()` carve-out (same pattern as V38 footer carve-out). Templates updated. (2) Open questions section in BACKLOG — fourth section, non-blocking parking. Planning scans every session. (3) Batch `Inputs:` line — optional list of non-standard resources. Before-build populates; batch-executor reads. Footer V42→V43; plugin 0.42.0→0.43.0.

**Decisions.** Fold-in sections at end-of-doc (simple position detection). Open questions coexist with planning batches (different lifecycles — non-blocking vs blocking). No BACKLOG fold-ins section (BACKLOG is writable). Planning handles migration from old centralized location. Inputs between change list and Files (natural reading order).

**Pivots.** Context compaction mid-session (no work lost). Two extra subagents needed fold-in updates beyond scope.

**Carried forward.** Fold-in carve-out smoke test deferred. Reference manual stale `NO-CODE-METHOD.md` reference noted (pre-existing).

