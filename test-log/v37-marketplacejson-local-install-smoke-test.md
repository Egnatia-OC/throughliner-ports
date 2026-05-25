# V37 — Marketplace.json + local install + smoke test (2026-05-21)

First globally-installed test (`/plugin marketplace add` + `/plugin install`). Empty `~\v37-scratch`. All 7 Pass.

| # | Date | Session | Test | Component | Status | Notes |
|---|---|---|---|---|---|---|
| 109 | 2026-05-21 | V37 | `claude plugin validate .` passes clean on `.claude-plugin/marketplace.json` | `.claude-plugin/marketplace.json` | Pass | Initial run surfaced "no marketplace description" warning; description field added; second run clean. |
| 110 | 2026-05-21 | V37 | `claude plugin marketplace add ./` adds marketplace to user settings | `.claude-plugin/marketplace.json` | Pass | Output: "Successfully added marketplace: sovereign-implementer (declared in user settings)". |
| 111 | 2026-05-21 | V37 | `claude plugin install no-code-method@sovereign-implementer` installs plugin globally (scope: user) | `plugin/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` | Pass | Output: "Successfully installed plugin: no-code-method@sovereign-implementer (scope: user)". No `--plugin-dir` needed going forward. |
| 112 | 2026-05-21 | V37 | Empty-folder session (no `--plugin-dir`) opens silently — SessionStart tier 1 | `plugin/hooks/session_start.py` (tier detection) | Pass | `~\v37-scratch` is empty; tier 1 = plugin invisible. Standard Claude Code greeting only. First globally-installed SessionStart validation. |
| 113 | 2026-05-21 | V37 | `/hooks` shows 2 `[Plugin]` PreToolUse hooks: `Bash` (git guard) and `Edit\|Write\|MultiEdit\|Task` (locked-doc + boundary enforcement) | `plugin/hooks/hooks.json` + `pre_tool_use.py` + `pre_tool_use_git_guard.py` | Pass | 4 total hooks (2 plugin + 2 user settings). SessionStart/Stop don't appear in `/hooks` UI — differs from `--plugin-dir` (#035, #091). |
| 114 | 2026-05-21 | V37 | `/adopt` fires case 1 on empty folder — scaffold detection + first prompt delivered | `plugin/agents/adopt.md` (case 1) + `plugin/skills/adopt/scripts/scaffold.py` | Pass | Subagent ran `detect-case`, correctly identified empty folder, opened with "I'll ask you four quick questions" and presented Q1 (project context). First globally-installed subagent invocation. |
| 115 | 2026-05-21 | V37 | `/reload-plugins` loads full plugin surface without restart | plugin (all components) | Pass | Output: "Reloaded: 1 plugin · 2 skills · 11 agents · 4 hooks · 0 plugin MCP servers · 0 plugin LSP servers". Confirms filesystem-based reload mechanism works for globally-installed plugin. |

