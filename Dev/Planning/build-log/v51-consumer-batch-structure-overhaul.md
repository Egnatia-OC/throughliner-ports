# v51 — 2026-05-22 — Consumer-batch structure overhaul

**What shipped.** V49 scope. Five scope-context sections added to BACKLOG build batches (Goal, Outputs, Success criteria, Decisions, Dependencies) plus conditional Red flags sub-section and `Changes:` delimiter separating scope-context from build-operations. Template placeholder cleanup (item 6): example batches → HTML-comment format specs. `/setup` case 4 detects old-format batches and inserts stubs. Parser updated with backwards-compatible `Changes:` support. DOC-STRUCTURE fully rewritten for batch structure. VOCABULARY gains 5 entries. All subagents and Reference manual updated. Footer V46→V47; plugin 0.46.0→0.47.0.

**Decisions.** `Changes:` delimiter (not scope-context fence) — cheaper, robust, backwards-compatible. Red flags auto-detected conditional (planning detects security-shaped scope). HTML-comment format specs in template (no diff noise). Case 4 stubs: Goal/Outputs/Success only (Decisions/Dependencies/Red flags are conditional).

**Pivots.** PowerShell mangled Unicode in inline parser tests — wrote proper `test_parser.py`. Session spanned two context windows.

**Carried forward.** UX friction 6/7 resolved. "Red-flag / threat-class marker" partially resolved (batch-level shipped; UX.md marker remains). Deferred smoke tests (V43–V49).

