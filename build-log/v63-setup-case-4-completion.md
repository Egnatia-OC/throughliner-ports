# v63 — 2026-05-24 — /setup case 4 completion

**What shipped.** Scope 0064. Two `/setup` case 4 gaps from 0060 E2E: (1) BUILD-LOG folder migration — detects flat file, creates `build-log/` with INDEX.md + per-build files, updates path block. (2) Batch stub quality — broadened pre-V47 detection, extracts original prose as Goal content instead of placeholder. Non-blocking wording (no square brackets). 147 tests pass. Footer V56→V57; plugin 0.56.0→0.57.0.

**Decisions.** Non-blocking placeholder wording over omitting scope sections — before-build benefits from knowing what's missing vs present. Square brackets were the specific problem (pattern-match as template content).

**Pivots.** None.

**Carried forward.** Reference manual case 4 description predates V38 footer-stamp carve-out — flagged for future doc sweep. Deferred smoke tests → 0068.

