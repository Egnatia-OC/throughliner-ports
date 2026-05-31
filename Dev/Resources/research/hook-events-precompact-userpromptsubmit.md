# Hook events research — 2026-05-22 (updated 2026-05-30)

## Purpose

Hook event capabilities relevant to plugin design.

## UserPromptSubmit

**Status:** Exists, fully functional.

Fires on every user prompt submission. Input includes `prompt` text, `transcript_path`, `cwd`, `permission_mode`. Output supports `additionalContext` injection, `decision: "block"`, `sessionTitle`, `suppressOriginalPrompt`. Timeout: 30 seconds.

**Key:** Receives full prompt text; can classify and inject routing context. Must detect first-prompt-of-session and no-op on subsequent prompts.

## PreCompact

**Status:** Exists but **cannot inject context.**

Fires before context compaction. Can return `decision: "block"` with `reason`. **Cannot** return `additionalContext` or any hook-specific output.

**Critical limitation:** Original scope assumed context injection. Not possible — hook can only block or allow. Reframed as: block during active builds, recommend handoff. On-disk state (BACKLOG, MANIFEST, TEST-LOG) already survives across sessions.

## Comparison

| Capability | PreCompact | UserPromptSubmit |
|---|---|---|
| Block/allow | Yes | Yes |
| Inject `additionalContext` | No | Yes |
| Receives prompt text | No | Yes |
| Session naming | No | Yes |

## Implications for 0055

- UserPromptSubmit opener routing: fully viable.
- PreCompact: reframed from context injection to compaction blocking + handoff recommendation.

Filed: 2026-05-22.

## SessionStart re-fire behaviour (added 2026-05-30)

**Finding:** SessionStart hooks re-fire after `/clear` and `/compact` — not just on fresh session start.

The SessionStart event includes a `source` field: `"startup"` (new session), `"resume"` (resumed session), `"clear"` (after /clear), `"compact"` (after compaction). The hook fires on all four events, and its stdout gets injected as fresh context each time.

Only `type: "command"` and `type: "mcp_tool"` handlers are supported for SessionStart events.

**Implication:** The plugin's session-start hook already re-orients Claude after `/clear` or `/compact`. No additional mechanism needed. Resolves OQ "Session-start hook doesn't re-fire after /clear or context loss" — the premise was incorrect.

Sources: [Claude Code hooks reference](https://code.claude.com/docs/en/hooks), [Complete 2026 Production Reference](https://thepromptshelf.dev/blog/claude-code-hooks-complete-reference-2026/).

## Intercepting skill invocations (added 2026-05-30)

**Finding:** Two hook events cover skill invocation — both can block.

**Path 1 — Claude invokes a skill programmatically (agentic loop).**
PreToolUse with `matcher: "Skill"` fires. Input includes `tool_name: "Skill"` and `tool_input` containing the skill name and args. Hook script inspects `tool_input.skill` to identify which skill, checks preconditions, exits 2 to block.

**Path 2 — User types `/skillname` directly.**
UserPromptExpansion fires. Input includes `command_name` (e.g. `"sovbuild"`), `command_args`, `command_source: "plugin"`, `expansion_type: "slash_command"`. Hook can block with `decision: "block"` or inject context.

PreToolUse does NOT fire on path 2. UserPromptExpansion does NOT fire on path 1. Full coverage requires both hooks.

**UserPromptExpansion input format:**
```json
{
  "hook_event_name": "UserPromptExpansion",
  "expansion_type": "slash_command",
  "command_name": "sovbuild",
  "command_args": "",
  "command_source": "plugin",
  "prompt": "/sovbuild"
}
```

**Matcher for PreToolUse:** `"Skill"` (exact match). For UserPromptExpansion: matcher filters on `command_name`.

**Implication for premature /sovbuild idea:** Mechanical gate is viable. PreToolUse on "Skill" guards against Claude launching /sovbuild unprompted. UserPromptExpansion on "sovbuild" guards against user-invoked builds when preconditions aren't met (e.g., active build already exists).

Source: [Claude Code hooks reference](https://code.claude.com/docs/en/hooks).
