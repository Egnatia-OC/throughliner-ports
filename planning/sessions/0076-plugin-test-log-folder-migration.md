# 0076 — Plugin-side TEST-LOG folder migration

## Goal

Change the plugin so consumer projects use a `test-log/` folder (INDEX.md + per-batch files) instead of a single `TEST-LOG.md`. Mirrors the BUILD-LOG folder migration shipped in V50. After this, both audit trails (build-log and test-log) use the same folder convention.

## Inputs

- `sovereign-implementer/plugin/templates/build-log/INDEX-TEMPLATE.md` — reference pattern to mirror.
- `sovereign-implementer/plugin/templates/TEST-LOG-TEMPLATE.md` — the file being replaced.
- `sovereign-implementer/plugin/docs/DOC-STRUCTURE.md` — TEST-LOG structure section to rewrite.
- V50 scope context (PLAN.md row + build-log entry at `build-log/v54-build-log-restructured.md`) — how the BUILD-LOG folder migration was done, for pattern consistency.

## Outputs

**Template restructure:**
- `plugin/templates/test-log/INDEX-TEMPLATE.md` — new. Header + empty file list + comment block with per-batch file format.
- Delete `plugin/templates/TEST-LOG-TEMPLATE.md`.

**Docs (2 files):**
- `plugin/docs/DOC-STRUCTURE.md` — rewrite *TEST-LOG.md structure* section to describe folder layout, per-batch file shape, INDEX format.
- `plugin/docs/VOCABULARY.md` — update references from `TEST-LOG.md` to `test-log/` where the path matters.

**Subagent bodies (5 files):**
- `plugin/agents/after-build.md` — write rows to a per-batch file in `test-log/` instead of appending to `TEST-LOG.md`. Add index-line append. Session identifier logic unchanged.
- `plugin/agents/planning.md` — read rows from folder (walk per-batch files). Row pruning walks all files. Test-confirmation read-back identifies previous batch's file. Drift check 5 walks recent files.
- `plugin/agents/before-build.md` — minor reference update.
- `plugin/agents/batch-executor.md` — minor reference update.
- `plugin/agents/setup.md` — add TEST-LOG folder migration case (parallel to existing BUILD-LOG migration case): detect flat `TEST-LOG.md` → create `test-log/`, extract per-batch files, create INDEX.md, update path block, delete old file.

**Hook scripts (4 files):**
- `plugin/hooks/pre_tool_use.py` — add `test-log/` to writable paths (parallel to `build-log/`). Test-confirmation gate: resolve per-batch files instead of single file. Spine-doc writable-name set update.
- `plugin/hooks/session_start.py` — spine detection: `test-log/` folder as alternative to `TEST-LOG.md`. Tripwire: read previous batch's per-batch file instead of parsing single file.
- `plugin/hooks/stop.py` — mtime heuristic: compare BACKLOG mtime against newest file in `test-log/` (parallel to existing build-log folder-mode logic). After-build redirect message: reference `test-log/`.
- `plugin/hooks/user_prompt_submit.py` — minor pattern update if needed.

**Python helpers (2 files):**
- `plugin/scripts/project_state.py` — `resolve_path_block_entry` for `test-log/` folder mode. `parse_test_log_rows` to accept folder (walk files) or single file. `previous_batch_test_rows` folder-aware. `has_unconfirmed_previous_batch_test_rows` folder-aware.
- `plugin/skills/setup/scripts/scaffold.py` — scaffold `test-log/` folder instead of `TEST-LOG.md`.

**Consumer template:**
- `plugin/templates/CLAUDE-TEMPLATE.md` — path block: `"TEST-LOG.md": "test-log/INDEX.md"`.

**Universal behaviour:**
- `plugin/hooks/universal-behaviour.md` — update references.

**Reference manual + crash course:**
- `sovereign-implementer/Reference manual.md` — update TEST-LOG references.
- `sovereign-implementer/crash-course/` — update any TEST-LOG references in HTML pages.

**Tests:**
- `tests/` — update fixtures and assertions for folder mode. Add test cases for: folder detection, per-batch file parsing, migration from flat to folder, INDEX line append, mtime heuristic with folder.

**Dev-side follow-through:**
- After plugin changes land, re-split `sovereign-implementer/test-log/` (from 0075) if the per-batch file format changed during design.

## Success criteria

1. `/setup` on a fresh folder scaffolds `test-log/INDEX.md` (not `TEST-LOG.md`).
2. After-build writes a per-batch file in `test-log/` and appends an index line.
3. Planning subagent reads rows from `test-log/` folder, prunes across files, runs drift check 5.
4. Test-confirmation gate (PreToolUse) resolves unconfirmed rows from folder.
5. SessionStart tripwire detects open test sessions from folder.
6. Stop hook mtime heuristic works with `test-log/` folder.
7. `/setup` case 4 (existing project) migrates flat `TEST-LOG.md` to `test-log/` folder.
8. All existing tests pass; new folder-mode tests added.
9. No remaining `TEST-LOG.md` references in plugin code that assume a single file (audit via grep).

## Open questions for this session

1. **Per-batch file naming.** `NNN-batch-name.md` matching build-log convention? Or session-tag-based (`vNN-slug.md`)? Build-log uses batch name; test-log rows are tagged by session — which key?
2. **Row format inside per-batch files.** Same 10-column table, or can the file carry the session heading + table (closer to dev-side TEST-LOG's current section structure)?
3. **Planning subagent multi-file cost.** Drift check 5 (TEST-LOG↔code-touch) currently parses one file. Walking N files increases token cost. Cap at recent K files? Or accept the cost since test-log files are small?
4. **mtime heuristic in stop.py.** BUILD-LOG folder mode uses `has_ticked_file_in_build_batches`. What's the TEST-LOG equivalent — newest file mtime in `test-log/`?

## Risks / dependencies

- **Depends on 0075** for dev-side folder structure (split runs first, plugin changes land on top).
- **High blast radius** — ~17 plugin files + tests. The BUILD-LOG equivalent (V50) was a full session; this touches more code because TEST-LOG is wired into the test-confirmation gate, tripwire, and mtime heuristic.
- **Not remote-safe.** Design decisions in the open questions above need human judgement. Recommend interactive session.
- **Migration case complexity.** `/setup` case 4 already handles BUILD-LOG migration. Adding TEST-LOG migration is parallel but increases the case-4 code path. Test thoroughly.
