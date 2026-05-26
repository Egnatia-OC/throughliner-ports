# v52 — 2026-05-22 — ADR-style numbering + per-batch BACKLOG file-split

**What shipped.** Scope 0050. Two structural overhauls: (1) dev-side scope files renamed `V*.md` → `NNNN-kebab-title.md` (0051–0059 created); (2) consumer-side BACKLOG split into `BACKLOG/` folder with `INDEX.md` + per-batch `NNNN-batch-name.md` files. Shared `allocate_number.py`. All hooks updated for folder-aware BACKLOG (`is_backlog_file()`, `resolve_backlog_dir()` in `project_state.py`). Parser auto-detects folder vs single-file. `/setup` case 4 migrates. All subagents updated. BUILD-METHOD updated with triple-distinction (session tag / scope-file number / method version). Footer V47→V48; plugin 0.47.0→0.48.0.

**Decisions.** Combined dev+consumer in one session (shared `allocate_number.py` concept). 4-digit zero-padded (ADR convention). INDEX.md not README.md (no GitHub collision). Numbers frozen at allocation. Legacy single-file kept working via parser fallback.

**Pivots.** Spanned two context windows. `stop.py` docstring edit failed string match — skipped.

**Carried forward.** Deferred smoke tests (all previous + V48 folder-split). OQ "Red-flag / threat-class marker" UX.md half unscheduled.

