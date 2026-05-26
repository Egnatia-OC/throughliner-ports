# V75 — 2026-05-26 — TEST-LOG folder split + proxy index

**What shipped.** TEST-LOG.md split from a single flat file into a `test-log/` folder with per-session files. `_method/proxies/test-log.md` (formerly a companion summary proxy) becomes the folder's operational index — same proxy-as-index pattern as BACKLOG and build-log (0089). All three audit-trail docs now use identical folder + proxy-as-index architecture. Parser, hooks, procedures, scaffold, and templates updated. Old `TEST-LOG-TEMPLATE.md` deleted; replaced by `test-log/ENTRY-TEMPLATE.md` (per-session) + `.proxies/test-log.md` (index). `/setup` case 4 gains a V75 migration step. 5 new tests added (181 total pass).

**Decisions taken and why.** Per-session file naming mirrors build-log: `NNN-batch-name.md`. Index line format includes row count and unconfirmed count for at-a-glance status. Row IDs remain globally unique across all per-session files (not per-file). The proxy-as-index is directly edited (like BACKLOG and build-log proxies), not regenerated from source — this keeps the proxies/ folder as the single canonical "where to find indexes" location.

**Pivots and surprises.** UX-TEMPLATE.md was at V73 (missed in the V74 bump from session v88) — fixed to V75 in this session's footer bump pass.

**Carried forward.** Scope 0076 (the original pre-0079 version of this work) left in `planning/scopes/` as historical reference — already marked cancelled in BACKLOG.
