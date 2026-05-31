# V18 — 2026-05-12 — Plugin scaffold + SessionStart hook + JSON path block

**What shipped.** Plugin scaffold: `plugin.json`, `hooks.json` with SessionStart hook, `session_start.py` emitting eight universal behavioural rules as `additionalContext`, rules text in `universal-behaviour.md`. CLAUDE-TEMPLATE path block changed from markdown bullets to fenced JSON for deterministic parsing. Smoke-tested on Windows: plugin loaded, hook registered, rules recited verbatim.

**Decisions.** Plugin in same repo (`sovereign-implementer/plugin/`) — method and code co-evolve. Python for hooks, not bash/Node — cross-platform, no profile contamination, readable for non-coders. JSON for path block, not YAML — stdlib, loud failures, no quoting gotchas.

**Pivots.** `UserPromptSubmit` hooks in plugins don't execute (#10225) — pivoted to SessionStart. `${CLAUDE_PLUGIN_ROOT}` doesn't quote paths with spaces — smoke test failed silently; fix: escaped quotes in `hooks.json`. Claude Code CLI wasn't installed — required PowerShell installer.

**Carried forward.** Escaped-quote pattern for all hook commands. Reference manual needs install instructions. BUILD-LOG.md added post-tag.

