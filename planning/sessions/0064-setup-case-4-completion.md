# 0064 — /setup case 4 completion

## Goal

Close the two gaps in `/setup` case 4 (already-adopted refresh) found during the 0060 E2E test: the missing BUILD-LOG folder migration and the placeholder-content quality in migrated BACKLOG batch files.

## Inputs

- E2E findings 2 and 5 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- `plugin/agents/setup.md` (the setup subagent body)
- `plugin/templates/build-log/INDEX-TEMPLATE.md` (the build-log folder template)

## Outputs

- Setup subagent's case 4 path gains BUILD-LOG.md → `build-log/` folder migration (create folder, move content to INDEX.md, delete old file, update CLAUDE.md path block)
- Batch stub quality improved: when case 4 splits BACKLOG.md into per-batch files, scope-context sections should carry content extracted from the original BACKLOG.md entries rather than placeholder text. If the original entry had no scope content (just a title and change list), the stub should say so explicitly rather than using `[To be filled in during the next planning session.]` — which before-build interprets as blocking.

## Success criteria

- Case 4 refresh on a project with a flat BUILD-LOG.md produces a `build-log/` folder with INDEX.md
- CLAUDE.md path block updated from `BUILD-LOG.md` path to `build-log/INDEX.md`
- Migrated batch files carry whatever scope content the original BACKLOG.md entry had, or a clear "no scope content in original — fill during planning" note that before-build can distinguish from a blocking placeholder

## Risks / dependencies

- Depends on understanding how `parse_backlog.py` extracts batch content from single-file BACKLOG.md — the migration needs to preserve whatever the parser can extract.
