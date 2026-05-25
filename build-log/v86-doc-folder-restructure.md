# v86 — Doc folder restructure

**Date:** 2026-05-26
**Scope:** 0087 — Doc folder restructure
**Method version:** V73

## What shipped

Moved method spine docs out of the consumer project root into a `_method/` subfolder. CLAUDE.md stays at root (Claude Code auto-loads it). The path block in CLAUDE.md is the indirection layer — old projects keep root-level paths, new projects get `_method/` paths.

### Code changes

- **scaffold.py** — rewritten. Creates `_method/` directory, places UX/MANIFEST/TEST-LOG inside it. Creates `_method/BACKLOG/`, `_method/build-log/`, `_method/planning/drafts/`, `_method/research/`, `_method/research/search-queries/`, `_method/proxies/`. CLAUDE.md stays at root. Split destination maps into root vs method-dir.
- **pre_tool_use.py** — `is_scaffold_path()` rewritten to check root for CLAUDE.md and `_method/` for spine docs, with legacy root-level fallback. `is_research_file()` updated for both `_method/research/` and root-level `research/`.
- **session_start.py** — `find_method_spine_docs()` now scans both `_method/` and root for backward compat.
- **project_state.py** — `identify_previous_session()` adds fallback check for `_method/build-log/INDEX.md`.
- **CLAUDE-TEMPLATE.md** — path block defaults now point to `_method/` paths.

### Doc changes

- DOC-STRUCTURE.md, VOCABULARY.md, universal-behaviour.md, setup.md, planning.md, research SKILL.md, Reference manual.md — all paths updated to `_method/`.
- VOCABULARY.md — added `_method/ folder` term.
- INVENTORY.md — updated project-side doc fates, `/setup` scaffold description, bundled artefacts note.
- Four proxy templates — updated `source:` path in HTML comment headers.
- Three crash-course HTML files — doc card headings, intro text, permission table rows updated.

## Decisions

- **Underscore prefix convention.** `_method/` signals "method infrastructure, not user content." Inside `_method/`, plain names (no double-prefixing): `proxies/` not `_proxies/`.
- **Legacy support via dual-path checks.** All code checks both `_method/` and root locations. No migration command needed — existing projects continue working.
- **Proxy templates stay at `plugin/templates/.proxies/`.** Source template paths didn't change; only the scaffolded destination changed to `_method/proxies/`.

## Performance

- Completion: full scope.
- Files changed: ~25.
- Tests: 172/172 pass.
- Carried forward: nothing.
