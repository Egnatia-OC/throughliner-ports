# Hook events research: PreCompact and UserPromptSubmit — 2026-05-22

## Purpose

Verify whether PreCompact and UserPromptSubmit hook events exist in Claude Code and are usable for scope 0055 (new hook events). The platform-capabilities-audit.md (2026-05-21) listed both as available but flagged PreCompact availability as uncertain.

## Findings

### UserPromptSubmit

**Status:** Exists and fully functional.

**When it fires:** Every time the user submits a prompt, before Claude processes it.

**Input payload (stdin JSON):**
```json
{
  "session_id": "string",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "string",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "The user's input text"
}
```

**Output capabilities:**
- `decision`: "block" to reject the prompt, or omit/allow to let it through.
- `reason`: shown to the user when blocking.
- `hookSpecificOutput.additionalContext`: string injected into the conversation as context before Claude processes the prompt.
- `hookSpecificOutput.sessionTitle`: auto-name the session.
- `hookSpecificOutput.suppressOriginalPrompt`: boolean — if true, the original prompt text is suppressed (replaced by additionalContext).
- Plain text stdout is treated as context injection automatically.

**Timeout:** 30 seconds (shorter than the default for other hooks).

**Key for 0055:** Receives the full prompt text. Can classify it and inject routing context via `additionalContext`. Fires on every prompt — the hook must detect first-prompt-of-session and no-op on subsequent prompts (check transcript for prior user messages).

### PreCompact

**Status:** Exists but cannot inject context.

**When it fires:** Before Claude Code compresses/compacts the conversation context (manual or automatic compaction).

**Input payload (stdin JSON):**
```json
{
  "session_id": "string",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "hook_event_name": "PreCompact"
}
```

**Output capabilities:**
- `decision`: "block" to prevent compaction from happening.
- `reason`: shown to the user when blocking.
- Universal fields: `continue`, `systemMessage`, `suppressOutput`.
- **Cannot** return `additionalContext` or any hook-specific output to inject data into the conversation.

**Critical limitation for 0055:** The original scope assumed PreCompact could "inject a structured summary of current build state so it survives compression." This is not possible — the hook can only block or allow compaction. It cannot add context that survives the compression.

**What PreCompact CAN do:** Block compaction during active builds and recommend the user start a fresh session instead. The method's on-disk state (BACKLOG ticked/unticked files, MANIFEST, TEST-LOG) already survives across sessions. SessionStart re-reads all project state. The routing table in universal-behaviour.md already has a "resume" route for partially-ticked batches.

### Comparison

| Capability | PreCompact | UserPromptSubmit |
|---|---|---|
| Block/allow | Yes | Yes |
| Inject `additionalContext` | No | Yes |
| Receives prompt text | No | Yes |
| Session naming | No | Yes |
| Plain stdout as context | No | Yes |
| Timeout | Default | 30 seconds |

## Implications for scope 0055

- **Item 6 (UserPromptSubmit opener routing):** Fully viable as scoped.
- **Item 5 (PreCompact context preservation):** Not viable as originally scoped (context injection). Reframed as: block compaction during active builds, recommend `/clear` + new session. The existing resume path handles the rest automatically.

Filed: 2026-05-22.
