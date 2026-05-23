# Permission prompt surface audit

**Researched:** 2026-05-24, 0066 session (v66).
**Question:** Why do subagents generate a flood of permission prompts in Accept edits mode, and can the plugin reduce the volume?
**Answer:** The root cause is a Claude Code platform bug — subagents do not inherit the parent session's permission mode or approved permissions. Every tool call from every subagent prompts regardless of mode.

## Root cause

Three open GitHub issues document the problem:

- [#28584](https://github.com/anthropics/claude-code/issues/28584) — Subagents prompt for permission on every tool call (Read, Glob, Grep, Edit — everything), regardless of session permission mode. Regression since v2.1.56.
- [#40241](https://github.com/anthropics/claude-code/issues/40241) — `--dangerously-skip-permissions` does not propagate to subagents.
- [#18950](https://github.com/anthropics/claude-code/issues/18950) — Subagents don't inherit `settings.json` permission allowlists.

Additionally, plugin-shipped agents cannot carry `permissionMode` in their YAML frontmatter — Claude Code blocks it for security reasons (confirmed in `research/marketplace-install-permission-surface.md`).

## Impact

Every Read, Edit, Write, Glob, Grep, and Bash call from every subagent generates a permission prompt. A full build cycle (planning → before-build → build → after-build) can produce 50-100+ prompts. The E2E finding (#6 from 0060) correctly identified this as making the experience feel broken.

## Audit table — tool calls per subagent

| Subagent | tools: line | Bash calls | Estimated prompts per invocation |
|---|---|---|---|
| planning | Read, Edit, Write, Glob, Grep | None (no Bash access) | 10-20+ (all doc reads and BACKLOG edits) |
| before-build | Read, Edit, Glob, Grep, Bash | `parse_backlog.py` | 8-12 (doc reads, BACKLOG edit, parser call) |
| batch-executor | Read, Edit, Write, MultiEdit, Glob, Grep, Bash | Build commands | 15-30+ (file reads, edits, BACKLOG tick edits) |
| after-build | Read, Edit, Write, Glob, Grep, Bash | ~~`git status`, `git diff`~~, ~~`allocate_number.py`~~, test commands | 15-25+ (doc reads, MANIFEST/TEST-LOG/build-log writes, tests) |
| setup | Read, Edit, Write, Bash, Glob, Grep | `scaffold.py` (3 calls), `cp`/`rm`, ~~`allocate_number.py`~~ | 10-20+ (detection, scaffolding, doc seeding) |

Strikethrough items were eliminated by this session's fixes.

## Classification and mitigations

| # | Category | Mitigation | Status |
|---|---|---|---|
| 1 | (a) plugin fix | Replace `allocate_number.py` Bash calls with Glob + arithmetic in all subagents | Done |
| 2 | (a) plugin fix | Replace `git status`/`git diff` in after-build with batch Files list | Done |
| 3 | (b) user config | Document `/fewer-permission-prompts` skill in Crash course | Done |
| 4 | (b) user config | Recommend Auto mode for Build/After-build phases | Done |
| 5 | (c) limitation | Document the platform bug in Crash course with issue links | Done |

## What remains unfixable from the plugin side

- Every Read/Glob/Grep call from subagents still prompts — these are read-only operations that should never prompt, but the inheritance bug causes them to.
- Every Edit/Write call from subagents still prompts — Accept edits should auto-allow these, but doesn't for subagents.
- `parse_backlog.py` in before-build still requires Bash — the parser handles too many edge cases (folder vs single-file mode, change-list extraction, placeholder detection) to replicate reliably in subagent prompt instructions.
- `scaffold.py` in setup still requires Bash — the scaffold script handles file creation, template copying, and case detection.
- Claude-automatable test commands in after-build inherently need Bash.

## Remaining Bash calls after fixes

| Subagent | Remaining Bash calls | Why Bash is needed |
|---|---|---|
| planning | None | No Bash in tools list |
| before-build | `parse_backlog.py` (1 call) | Complex parser with edge-case handling |
| batch-executor | Build commands (N calls) | Writing/running code is the job |
| after-build | Test commands (N calls) | Running automatable tests |
| setup | `scaffold.py` (3 calls), `cp`/`rm` (1-2 calls) | File scaffolding and backups |

## Sources

- [Configure permissions](https://code.claude.com/docs/en/permissions) — permission modes, rule precedence
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes) — Accept edits / Auto behavior
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents) — subagent tool and permission configuration
- [#28584](https://github.com/anthropics/claude-code/issues/28584) — subagent permission regression
- [#40241](https://github.com/anthropics/claude-code/issues/40241) — bypass flag not propagating
- [#18950](https://github.com/anthropics/claude-code/issues/18950) — settings.json not inherited
