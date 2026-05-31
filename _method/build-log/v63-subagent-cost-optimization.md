# V63 — 2026-05-25 — Subagent cost optimization

**What shipped.** Scope 0071. Planning subagent optimized for cold-start projects: (1) classify-then-load — restructured "First action" to check MANIFEST + TEST-LOG before loading full doc set; cold-start projects skip BUILD-LOG and TEST-LOG structure docs; (2) cold-start gate — procedure steps 1–3 (test-session close, batch cleanup, aging, pruning, drift checks) skipped when MANIFEST is empty and TEST-LOG has no data rows; (3) reasoning constraint directive — concise-thinking instruction added to behavioural rules; (4) model: sonnet — planning subagent frontmatter routes to Sonnet (~40% cheaper); (5) tool-list audit — all five subagents audited, lists already tight, no changes needed. Research file updated with `model:` frontmatter and `loadProjectInstructions` findings. INVENTORY updated. 0078 scope file updated to make 0071 verification non-optional; 0077 PLAN.md row updated to note cold-start gate testing. All footers bumped V62→V63, plugin 0.62.0→0.63.0. 166 tests pass.

**Decisions.** Sonnet chosen over Haiku — Haiku too error-prone for judgment-heavy planning work (push-back, duplicate detection). Cold-start condition is MANIFEST + TEST-LOG both empty, not build-log — build-log could be empty on a partially-adopted project that has MANIFEST entries. Tool lists not narrowed — audit found all five already tight; planning doesn't have Bash (drift check 1 degrades gracefully), and adding it would increase cost. Smoke test deferred to 0077/0078 E2E sessions rather than this session.

**Pivots.** None. Scope delivered as specified.

**Carried forward.** Smoke test verification: Sonnet quality for push-back/duplicate detection (0078), cold-start gate on greenfield project (0077), token cost measurement vs. 31.6k baseline (0078). Planning subagent missing Bash for drift check 1 (git diff) — noted but not addressed; adding it would increase cost, and the check degrades gracefully.

