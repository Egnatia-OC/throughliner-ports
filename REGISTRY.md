# REGISTRY

Components that exist in this project. Updated after each build.

- `si-plugin/.claude-plugin/plugin.json` — plugin manifest (name, version, description)
- `si-plugin/hooks/hooks.json` — hook declarations (session_start, pre_tool_use)
- `si-plugin/hooks/session_start.py` — detects project state, loads behaviour rules
- `si-plugin/hooks/pre_tool_use.py` — SPEC.md read-only, scope-lock, git safety
- `si-plugin/skills/setup/SKILL.md` — /setup skill definition
- `si-plugin/skills/plan/SKILL.md` — /plan skill definition
- `si-plugin/skills/next/SKILL.md` — /next skill definition
- `si-plugin/skills/done/SKILL.md` — /done skill definition
- `si-plugin/docs/setup.md` — /setup procedure
- `si-plugin/docs/plan.md` — /plan procedure
- `si-plugin/docs/next.md` — /next procedure
- `si-plugin/docs/done.md` — /done procedure
- `si-plugin/docs/behaviour.md` — universal behaviour rules loaded into every adopted session
- `si-plugin/templates/CLAUDE-TEMPLATE.md` — CLAUDE.md template scaffolded into consumer projects
