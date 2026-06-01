# REGISTRY

Components that exist in this project. Updated after each build.

- `plugin/si-plugin/.claude-plugin/plugin.json` — plugin manifest (name, version, description)
- `plugin/si-plugin/hooks/hooks.json` — hook declarations (session_start, pre_tool_use)
- `plugin/si-plugin/hooks/session_start.py` — detects project state, loads behaviour rules
- `plugin/si-plugin/hooks/pre_tool_use.py` — SPEC.md read-only, scope-lock, git safety
- `plugin/si-plugin/skills/setup/SKILL.md` — /setup skill definition
- `plugin/si-plugin/skills/plan/SKILL.md` — /plan skill definition
- `plugin/si-plugin/skills/next/SKILL.md` — /next skill definition
- `plugin/si-plugin/skills/done/SKILL.md` — /done skill definition
- `plugin/si-plugin/docs/setup.md` — /setup procedure
- `plugin/si-plugin/docs/plan.md` — /plan procedure
- `plugin/si-plugin/docs/next.md` — /next procedure
- `plugin/si-plugin/docs/done.md` — /done procedure
- `plugin/si-plugin/docs/behaviour.md` — universal behaviour rules loaded into every adopted session
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` — CLAUDE.md template scaffolded into consumer projects
