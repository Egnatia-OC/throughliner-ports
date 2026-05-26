# Permission prompt surface audit

**Researched:** 2026-05-24, 0066 session (v66).
**Question:** Why do subagents flood permission prompts in Accept edits mode?
**Answer:** Claude Code platform bug — subagents don't inherit permission mode or approved permissions.

## Root cause

- [#28584](https://github.com/anthropics/claude-code/issues/28584) — Subagents prompt on every tool call regardless of mode.
- [#40241](https://github.com/anthropics/claude-code/issues/40241) — `--dangerously-skip-permissions` doesn't propagate.
- [#18950](https://github.com/anthropics/claude-code/issues/18950) — `settings.json` allowlists not inherited.

Plugin-shipped agents also can't carry `permissionMode` in frontmatter (blocked for security).

## Prompts per subagent

| Subagent | Bash calls | Estimated prompts |
|---|---|---|
| planning | None | 10-20+ |
| before-build | `parse_backlog.py` | 8-12 |
| batch-executor | Build commands | 15-30+ |
| after-build | Test commands | 15-25+ |
| setup | `scaffold.py`, `cp`/`rm` | 10-20+ |

## Mitigations applied

1. Replaced `allocate_number.py` Bash calls with Glob in all subagents.
2. Replaced `git status`/`git diff` in after-build with batch Files list.
3. Documented `/fewer-permission-prompts` in Reference manual.
4. Recommended Auto mode for Build/After-build.
5. Documented the platform bug with issue links.

## Still unfixable

- Every Read/Glob/Grep from subagents still prompts.
- Every Edit/Write from subagents still prompts.
- `parse_backlog.py` and `scaffold.py` still need Bash.
- Test commands in after-build inherently need Bash.

## Sources

- code.claude.com/docs: permissions, permission-modes, sub-agents
- GitHub issues: #28584, #40241, #18950
