# 0089 — INDEX relocation to proxies

## Goal

Move BACKLOG INDEX.md and build-log INDEX.md content into `_method/proxies/`, making it the universal index layer for folder-based docs. BACKLOG/ and build-log/ folders keep only per-entry files. Establishes the pattern: for folder-based docs, the proxy IS the index.

> **Post-0087 note:** Consumer-side proxy directory is now `_method/proxies/` (was `.proxies/`). Template sources remain at `plugin/templates/.proxies/`. All consumer-facing paths in this scope file use `_method/proxies/`; legacy `.proxies/` fallback applies per 0087's backward-compat pattern.

## Inputs

- 0081 outputs: proxy format spec, `.proxies/` folder convention, templates.
- `plugin/scripts/parse_backlog.py` — BACKLOG parser (currently reads INDEX.md).
- `plugin/docs/procedures/after-build.md` — currently prepends to build-log INDEX.md.
- `plugin/docs/procedures/planning.md` — currently reads BACKLOG INDEX.md.
- `plugin/hooks/session_start.py` — BACKLOG and build-log state detection.
- `plugin/templates/BACKLOG/INDEX-TEMPLATE.md` — current BACKLOG INDEX template.
- `plugin/templates/build-log/INDEX-TEMPLATE.md` — current build-log INDEX template.

## Outputs

**Proxy files (2, replacing INDEX.md):**
- `_method/proxies/backlog.md` — carries Red flags, Planning batches, Build batch references, Open questions (all four BACKLOG INDEX sections).
- `_method/proxies/build-log.md` — carries the one-liner build-log index list.

**Template updates:**
- `plugin/templates/.proxies/backlog.md` — replaces `plugin/templates/BACKLOG/INDEX-TEMPLATE.md`.
- `plugin/templates/.proxies/build-log.md` — replaces `plugin/templates/build-log/INDEX-TEMPLATE.md`.
- Delete `plugin/templates/BACKLOG/INDEX-TEMPLATE.md` and `plugin/templates/build-log/INDEX-TEMPLATE.md`.

**Parser update:**
- `plugin/scripts/parse_backlog.py` — resolve BACKLOG index at `.proxies/backlog.md` (fallback to `BACKLOG/INDEX.md` for pre-proxy projects).

**Procedure doc updates:**
- `plugin/docs/procedures/after-build.md` — prepend build-log lines to `_method/proxies/build-log.md`. Add a proxy regeneration step: after MANIFEST update and build-log/test-log writes, regenerate all stale `_method/proxies/` files (UX, MANIFEST, build-log, test-log, research). Discovered 2026-05-25 ideation session — v81 shipped proxy generation for planning and setup but never added it to after-build.
- `plugin/docs/procedures/planning.md` — read BACKLOG state from `_method/proxies/backlog.md`.

**Hook updates:**
- `plugin/hooks/session_start.py` — find BACKLOG and build-log indexes in `_method/proxies/`.
- `plugin/hooks/pre_tool_use.py` — `_method/proxies/` writable paths.

**Scaffold update:**
- `plugin/skills/setup/scripts/scaffold.py` — scaffold `_method/proxies/backlog.md` and `_method/proxies/build-log.md` instead of INDEX.md files.

**Docs:**
- `plugin/docs/DOC-STRUCTURE.md` — update BACKLOG structure and build-log structure sections for new index location.
- `plugin/hooks/universal-behaviour.md` — update references.
- `plugin/docs/VOCABULARY.md` — update references.

**Consumer template:**
- `plugin/templates/CLAUDE-TEMPLATE.md` — path block updates for new index locations.

**Reference manual + crash course:**
- `Reference manual.md` — update references.
- `crash-course/` — update INDEX.md references in HTML pages.

**Tests:**
- `tests/` — update fixtures and assertions for new paths. Add fallback tests.

**Setup migration:**
- `/setup` case 4: detect old INDEX.md locations → migrate content to `_method/proxies/`.

## Success criteria

1. BACKLOG/ contains only per-batch files; `.proxies/backlog.md` carries the four sections.
2. build-log/ contains only per-build files; `.proxies/build-log.md` carries the index list.
3. Parser resolves BACKLOG from `.proxies/backlog.md` with fallback to old location.
4. After-build prepends to `.proxies/build-log.md` and regenerates all stale proxies.
5. Session start detects state from `.proxies/` locations.
6. `/setup` case 4 migrates old INDEX.md files to `.proxies/`.
7. Pre-proxy projects still work (fallback paths).
8. All tests pass.

## Open questions for this session

1. **Path block shape.** Currently `"BACKLOG.md": "BACKLOG/INDEX.md"` and `"BUILD-LOG.md": "build-log/INDEX.md"`. New target: `.proxies/backlog.md` and `.proxies/build-log.md`? Or a new key convention?
2. **BACKLOG folder naming.** With INDEX.md gone from inside the folder, does the folder name or convention need adjusting? (Likely not — it's established.)

## Risks / dependencies

- Depends on 0081 (proxy format and `.proxies/` established).
- Medium blast radius — parser, procedures, hooks, templates, tests.
- Migration complexity: `/setup` case 4 needs to move INDEX.md content without losing user data.
- Pre-proxy fallback needed for backwards compatibility.
