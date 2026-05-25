# v49 — 2026-05-22 — Non-GUI vocabulary generalisation + planning/plan-mode disambiguation

**What shipped.** V47 scope (bundled). (1) "user-observable behaviours" → "observable behaviours" across all plugin-side docs (12 instances). Non-GUI guidance paragraph added to DOC-STRUCTURE.md (CLI tools, backends, plugins adapt "user" and "experience" concepts). (2) "Planning session (not plan mode)" vocabulary entry. Per-phase permission-mode table in Reference manual. Researched programmatic mode switching — confirmed impossible from hooks. Footer V44→V45; plugin 0.44.0→0.45.0.

**Decisions.** "Observable behaviours" (not "outcomes" or "testable") — keeps existing term, drops GUI assumption. Vocabulary note (not full rename of planning phase) — lower cost, direct fix. Guidance paragraph (not new non-GUI template) — preserves UX.md as universal spine.

**Pivots.** Alex proposed programmatic plan-mode during planning — research disproved. Per-phase table was the outcome. Frozen repo-root docs retain old phrasing (correct per V39 freeze).

**Carried forward.** Two OQ entries resolved.

