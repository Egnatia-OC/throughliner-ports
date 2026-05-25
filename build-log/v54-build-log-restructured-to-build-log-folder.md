# v54 — 2026-05-22 — BUILD-LOG restructured to build-log/ folder

**What shipped.** Scope 0052. Replaced monolithic `BUILD-LOG.md` with `build-log/` folder (one file per build + `INDEX.md`). Same folder pattern as BACKLOG/ (V48). `/setup` scaffolds it. Path block key stays `"BUILD-LOG.md"` (changing would break parsing), value points to `build-log/INDEX.md`. Session identification updated across all hooks/subagents for folder mode with single-file fallback. Footer V49→V50; plugin 0.49.0→0.50.0.

**Decisions.** 3-digit numbers (fewer builds than BACKLOG batches). No case 4 migration (no consumer project has used the method yet). Bullet list for INDEX.md (matches BACKLOG/INDEX.md). Research cross-references by path, not embedded content.

**Carried forward.** Deferred smoke tests accumulating (V43–V50) — all testable in one desktop-app burner session.

