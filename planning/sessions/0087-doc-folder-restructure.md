# 0087 — Doc folder restructure

## Goal

Move method spine docs out of the project root into a dedicated subfolder so the user's directory isn't cluttered with method files alongside their source code. The project root should feel like the user's project, not a method filing cabinet.

## Inputs

- E2E research: `research/e2e-greenfield-post-redesign.md` — Finding 4.
- `plugin/templates/` — all template files (path defaults).
- `plugin/hooks/pre_tool_use.py` — path resolution logic.
- `plugin/hooks/session_start.py` — project state detection.
- `plugin/scripts/project_state.py` — path block parsing, BACKLOG resolution.
- `plugin/docs/procedures/` — all procedure docs referencing spine doc paths.
- `plugin/docs/DOC-STRUCTURE.md` — canonical doc layout.
- `Reference manual.md` — user-facing doc layout description.

## Outputs

- New default folder name for spine docs (e.g. `.method/`, `docs/`, or similar — decide during session).
- Updated templates: CLAUDE-TEMPLATE.md path block defaults point to subfolder paths.
- Updated `/setup` scaffold: creates the subfolder and places docs there.
- Updated hooks and scripts: path resolution works with subfolder layout.
- Updated procedure docs: references to spine doc locations.
- Updated DOC-STRUCTURE.md and Reference manual.
- Possibly: a CLAUDE.md inside the subfolder for method-specific context (optional — decide during session).

## Success criteria

1. After `/setup`, the project root contains only CLAUDE.md and the method subfolder (plus the user's source files).
2. All hooks resolve paths correctly through the path block.
3. Existing Taskflow layout continues to work (path block is the indirection layer — old layouts with root-level docs still parse).
4. Pytest suite passes.

## Open questions for this session

1. What should the folder be called? `.method/` (hidden on Unix, visible on Windows), `_method/`, `method/`, `docs/` (generic, might collide with user's docs folder)?
2. Should CLAUDE.md stay at the project root (Claude Code auto-loads it) with only the path block, and a second CLAUDE.md inside the method folder carry method-specific context?
3. Does this change affect the adoption gate? `is_unadopted_with_work` checks for CLAUDE.md at root — that stays. But scaffold path detection changes.

## Risks / dependencies

- Large surface area: templates, hooks, scripts, procedure docs, Reference manual, crash-course guide.
- Depends on 0085 and 0086 landing first (those fix the current layout; this restructures it).
- Existing adopted projects (Taskflow) must continue working — the path block is the compatibility layer, but needs testing.
