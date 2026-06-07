# REGISTRY

Components that exist in this project. Updated after each build.

- `plugin/si-plugin/.claude-plugin/plugin.json` — plugin manifest (name, version, description)
- `plugin/si-plugin/hooks/hooks.json` — hook declarations (session_start, pre_tool_use)
- `plugin/si-plugin/hooks/session_start.py` — detects project state, loads behaviour rules and FAQ index, checks plugin version against .si-version
- `plugin/si-plugin/hooks/pre_tool_use.py` — SPEC.md read-only, scope-lock, git safety
- `plugin/si-plugin/skills/setup/SKILL.md` — /setup skill definition
- `plugin/si-plugin/skills/plan/SKILL.md` — /plan skill definition
- `plugin/si-plugin/skills/next/SKILL.md` — /next skill definition
- `plugin/si-plugin/skills/done/SKILL.md` — /done skill definition
- `plugin/si-plugin/docs/setup.md` — /setup procedure
- `plugin/si-plugin/docs/plan.md` — /plan procedure
- `plugin/si-plugin/docs/next.md` — /next procedure
- `plugin/si-plugin/docs/done.md` — /done procedure
- `plugin/si-plugin/docs/plugin-behaviour.md` — universal behaviour rules loaded into every adopted session
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` — CLAUDE.md template scaffolded into consumer projects
- `plugin/si-plugin/templates/faq-template.md` — FAQ content template (13 Q&A pairs) scaffolded into consumer projects as FAQ/faq.md
- `plugin/si-plugin/templates/faq-index-template.md` — FAQ index template scaffolded into consumer projects as FAQ/index.md, loaded at session start
- `resources/reader-test-workflow.js` — multi-agent workflow script for testing plugin doc comprehension via simulated project
- `LOG/index.md` — one-line summaries of each session, newest first
- `LOG/log.md` — full session entries for the current release, newest first
- `LOG/log-v*.md` — archived per-release log files (created at push time)
- `README.md` — public-facing project description, install instructions, operating conditions
- `INSTALL.md` — guide for non-coders aimed at Claude reading on the user's behalf in a fresh claude.ai chat; walks through Claude Code install, paid plan setup, and plugin install
