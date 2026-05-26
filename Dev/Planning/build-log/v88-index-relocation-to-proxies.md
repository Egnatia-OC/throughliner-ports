# V74 — 2026-05-26 — INDEX relocation to proxies

**What shipped.** BACKLOG INDEX.md and build-log INDEX.md content relocated into `_method/proxies/backlog.md` and `_method/proxies/build-log.md`. Proxy-as-index is now the default for new projects (`/setup` scaffolds it). Parser, hooks, and project_state handle all three BACKLOG formats (single-file, folder+INDEX, proxy-as-index) with full fallback. Old INDEX templates deleted. `/setup` case 4 gains a V70 migration step. Test fixture and 5 new tests added (177 total pass).

**Decisions taken and why.** Proxy-as-index means the proxy IS the operational index (directly edited), not a regenerated summary — unlike the UX/MANIFEST/test-log proxies. This keeps the proxies/ folder as the single canonical "where to find indexes" location while BACKLOG/ and build-log/ hold only per-entry files. Bumped to V74 (fixing a pre-existing V73/72 mismatch where v87 bumped footers but missed `PLUGIN_METHOD_VERSION` and `plugin.json`).

**Pivots and surprises.** `project_state.py`'s `identify_previous_session()` needed the same proxy-aware fix as `session_start.py`'s version — the summary from context compaction flagged it but hadn't been applied yet.

**Carried forward.** Scope 0076 (test-log folder migration) references `test-log/INDEX.md` — when it ships it should adopt the proxy-as-index pattern directly rather than creating an INDEX.md that will immediately need relocating.
