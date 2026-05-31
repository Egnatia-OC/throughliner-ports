# v55 — 2026-05-22 — Automated test suite for dev project

**What shipped.** Scope 0053 (dev-internal, no method bump). Pytest suite at `tests/`: 124 tests, 2.7s, zero failures. 8 test files covering all hooks + shared helpers. 6 fixture directories (empty, tier2 variants, adopted folder/single-file, unadopted-with-work). BUILD-METHOD updated with test-suite section. OQ "Automated testing / CI" resolved.

**Decisions.** Subprocess-based tests (same stdin/stdout protocol as Claude Code). Committed fixtures (deterministic, inspectable). Manual CI only.

**Pivots.** V38/V45 carve-out tests: locked-doc carve-outs pass but batch-boundary denies downstream (UX.md not on Files: list). Correct behaviour — confirmed by asserting deny reason is "not on batch" not "locked doc."

**Carried forward.** Deferred smoke tests unchanged from v54.

