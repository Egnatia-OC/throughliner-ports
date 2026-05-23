# 0066 — Permission prompt surface audit

## Goal

Determine why subagents generate a flood of permission prompts in Accept edits mode and whether the plugin can reduce the volume. The 0060 E2E test found the prompt flood made the experience feel broken — the user couldn't step away during subagent execution.

## Inputs

- E2E finding 6 from `planning/sessions/0060-taskflow-e2e-prep-and-testing.md`
- Claude Code documentation on which tool calls require permission in each mode
- All five subagent bodies (to identify which tool calls they make)

## Outputs

- Audit table: for each subagent, list the tool calls it makes (Read, Edit, Write, Glob, Grep, Bash, Task/Agent) and which ones trigger permission prompts in Accept edits mode
- Classification of each prompt source as: (a) fixable from plugin side (e.g. replace Bash with a direct tool), (b) addressable by user configuration (e.g. allowlisting specific commands), or (c) Claude Code limitation (can't fix)
- For (a) items: changes to subagent bodies or hook scripts
- For (b) items: documentation in Crash course on recommended permission settings
- For (c) items: note in Crash course acknowledging the limitation

## Success criteria

- Root cause of the prompt flood identified
- Actionable fixes implemented for any (a) items
- User-facing guidance written for any (b) items
- Clear determination of what's fixable vs. not

## Open questions for this session

- Does Claude Code's `settings.json` support per-tool-type allowlisting that would let subagent Read/Glob/Grep calls pass silently? Research needed.
- Are subagent tool calls treated differently from main-conversation tool calls by Claude Code's permission system?

## Risks / dependencies

- This is primarily a research session. May produce no code changes if the prompt flood is entirely a Claude Code limitation.
- Depends on 0063 (subagent efficiency pass) landing first — if subagents make fewer tool calls after 0063, the prompt count may already drop.
