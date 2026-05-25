# 0090 — TEST-LOG folder split + proxy index

Supersedes cancelled 0076. Rewritten for post-0079 procedure-doc architecture and the `_method/proxies/` convention from 0081/0089.

> **Post-0087 note:** Consumer-side proxy directory is now `_method/proxies/` (was `.proxies/`). Template sources remain at `plugin/templates/.proxies/`. Consumer-facing paths below use `_method/proxies/`.

## Goal

Split TEST-LOG.md into a `test-log/` folder with per-session files. `_method/proxies/test-log.md` (created as a companion proxy in 0081) becomes the folder's index — same role as `_method/proxies/backlog.md` and `_method/proxies/build-log.md` after 0089.

## Inputs

- 0081 outputs: `_method/proxies/test-log.md` template (companion proxy).
- 0089 outputs: INDEX relocation pattern for BACKLOG and build-log.
- 0076 scope file — original design reference (scoped against old subagent architecture).
- `plugin/docs/DOC-STRUCTURE.md` — current TEST-LOG structure section.
- `plugin/hooks/pre_tool_use.py` — test-confirmation gate.
- `plugin/hooks/session_start.py` — tripwire, state detection.
- `plugin/scripts/project_state.py` — TEST-LOG parsing.
- `plugin/docs/procedures/after-build.md` — writes TEST-LOG rows.
- `plugin/docs/procedures/planning.md` — per-row read-back, drift check 5.

## Outputs

**Folder structure:**
- `test-log/` — per-session files (naming convention TBD — see open questions).
- `_method/proxies/test-log.md` — upgraded from companion proxy to folder index.

**Template updates:**
- `plugin/templates/.proxies/test-log.md` — rewritten as folder index (from 0081's companion template).
- New: `plugin/templates/test-log/` — per-session file template if needed.
- Delete: `plugin/templates/TEST-LOG-TEMPLATE.md`.

**Procedure doc updates:**
- `plugin/docs/procedures/after-build.md` — write per-session file in `test-log/`, update `.proxies/test-log.md`.
- `plugin/docs/procedures/planning.md` — read-back from `test-log/` files, prune across files.

**Hook updates:**
- `plugin/hooks/pre_tool_use.py` — test-confirmation gate resolves from `test-log/` + `.proxies/test-log.md`. Writable paths update.
- `plugin/hooks/session_start.py` — tripwire detects open test sessions from folder.

**Script updates:**
- `plugin/scripts/project_state.py` — TEST-LOG parsing accepts folder (walk files) or single file.

**Scaffold update:**
- `plugin/skills/setup/scripts/scaffold.py` — scaffold `test-log/` + proxy instead of `TEST-LOG.md`.
- `/setup` case 4: migrate flat `TEST-LOG.md` to folder.

**Docs:**
- `plugin/docs/DOC-STRUCTURE.md` — rewrite TEST-LOG structure section for folder layout.
- `plugin/docs/VOCABULARY.md` — update references.
- `plugin/hooks/universal-behaviour.md` — update references.

**Reference manual + crash course:**
- `Reference manual.md` — update TEST-LOG references.
- `crash-course/` — update HTML pages.

**Tests:**
- `tests/` — update fixtures and assertions. Add folder-mode tests.

## Success criteria

1. `/setup` on fresh folder scaffolds `test-log/` + `.proxies/test-log.md` (not `TEST-LOG.md`).
2. After-build writes per-session file in `test-log/` and updates proxy index.
3. Planning reads rows from `test-log/` files; per-row read-back works across files.
4. Test-confirmation gate resolves unconfirmed rows from folder.
5. Session start tripwire detects open test sessions from folder.
6. `/setup` case 4 migrates flat `TEST-LOG.md` to folder.
7. Pre-folder projects still work (fallback to single file).
8. All tests pass.

## Open questions for this session

1. **Per-session file naming.** `NNN-batch-name.md` matching build-log convention? Or session-tag based? Build-log uses batch name — should test-log mirror that?
2. **Proxy index content.** What does `.proxies/test-log.md` carry as a folder index? Summary row per session with confirmation status? Just a file list with pending count? Both?

## Risks / dependencies

- Depends on 0081 (proxy format) and 0089 (INDEX relocation pattern).
- High blast radius — hooks, procedures, scripts, templates, tests. Mirrors 0076's scope but with fewer files (no subagent bodies).
- Migration: `/setup` case 4 splits an existing file with potentially hundreds of rows across sessions.
