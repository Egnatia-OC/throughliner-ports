# REGISTRY

Components that exist in this project. Updated after each build.

- `plugin/si-plugin/.claude-plugin/plugin.json` — plugin manifest (name, version, description)
- `plugin/si-plugin/hooks/hooks.json` — hook declarations (session_start, pre_tool_use, post_tool_use)
- `plugin/si-plugin/hooks/session_start.py` — detects project state, loads behaviour rules and FAQ index, checks plugin version against .si-version, backfills unfilled LOG hash placeholders (hash-position-only, oldest-introducing-commit)
- `plugin/si-plugin/hooks/pre_tool_use.py` — SPEC.md read-only, scope-lock (tri-state on _build.md's Files: section), git safety (denies reset --hard, push --force, blanket adds, commit -a/-am; every denial teaches the fix and the patterns-as-data workaround)
- `plugin/si-plugin/hooks/post_tool_use.py` — advisory lint of QUEUE.md structure after Edit/Write lands (six deny-list checks; warnings fed back via additionalContext, silent when clean)
- `plugin/si-plugin/skills/setup/SKILL.md` — /setup skill definition
- `plugin/si-plugin/skills/plan/SKILL.md` — /plan skill definition
- `plugin/si-plugin/skills/next/SKILL.md` — /next skill definition
- `plugin/si-plugin/skills/done/SKILL.md` — /done skill definition
- `plugin/si-plugin/docs/setup.md` — /setup procedure
- `plugin/si-plugin/docs/plan.md` — /plan procedure
- `plugin/si-plugin/docs/next.md` — /next procedure front page (pre-flight, lock scope, route to per-type doc, ending before scope-lock)
- `plugin/si-plugin/docs/next-build.md` — build execution procedure (build entries, scope management, course-correction, completion)
- `plugin/si-plugin/docs/next-test.md` — test execution procedure (test entries, scope management, course-correction, completion)
- `plugin/si-plugin/docs/next-audit.md` — audit execution procedure (read target, compile findings, present, route captures, close)
- `plugin/si-plugin/docs/done.md` — /done procedure front page (route by session shape; LOG entry file naming, deferred tests, and commit core each stated once)
- `plugin/si-plugin/docs/done-build.md` — build close-out (judgment, LOG entry, staleness sweep, _build.md cleanup, recommend next)
- `plugin/si-plugin/docs/done-test.md` — test close-out (verify ticks, route fixes, LOG entry, cleanup, recommend next)
- `plugin/si-plugin/docs/done-audit.md` — audit close-out (verify findings handled, LOG entry, cleanup, recommend next)
- `plugin/si-plugin/docs/done-plan.md` — plan close-out (LOG entry, commit via core, recommend next)
- `plugin/si-plugin/docs/plugin-behaviour.md` — universal behaviour rules loaded into every adopted session
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md` — CLAUDE.md template scaffolded into consumer projects
- `plugin/si-plugin/templates/faq-template.md` — FAQ content template (14 Q&A pairs) scaffolded into consumer projects as FAQ/faq.md
- `plugin/si-plugin/templates/faq-index-template.md` — FAQ index template scaffolded into consumer projects as FAQ/index.md, loaded at session start
- `resources/reader-test-workflow.js` — multi-agent workflow script for testing plugin doc comprehension via simulated project
- `LOG/index.md` — one-line summaries of each session, newest first; post-split lines end with the session's entry filename
- `LOG/<slug or type-date>.md` — per-entry session files written by /done (one per session, named per done.md LOG entry files)
- `LOG/log.md` — pre-split session entries (frozen — new entries are per-entry files; contents findable by hash)
- `LOG/log-v*.md` — archived per-release log files from before the per-entry split (frozen, findable by hash)
- `README.md` — public-facing project description, install instructions, operating conditions
- `INSTALL.md` — guide for non-coders aimed at Claude reading on the user's behalf in a fresh claude.ai chat; walks through Claude Code install, paid plan setup, and plugin install
