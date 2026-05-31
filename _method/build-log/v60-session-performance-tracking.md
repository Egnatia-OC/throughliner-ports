# v60 — 2026-05-23 — Session performance tracking

**What shipped.** Scope 0058. Performance section added to per-build files. Five mechanical measures (completion status, files count, carve-outs, Claude-verified tests, user-verified pending) plus optional user Session notes. After-build, DOC-STRUCTURE, VOCABULARY, INDEX template, Reference manual, BUILD-METHOD, INVENTORY updated. OPEN-QUESTIONS entry removed. 147 tests pass. Footer V54→V55; plugin 0.54.0→0.55.0.

**Decisions.** Collocated in per-build files (already exist, after-build already writes them) over separate folder or conversation-only capture. Mechanical measures only — "without a mechanical success criterion, 'well' becomes vibes-encoded-as-data."

**Pivots.** CLAUDE.md was two sessions stale — fixed at close.

**Carried forward.** V55 Performance section added to deferred smoke tests.

