# Hook events research: PreCompact and UserPromptSubmit — 2026-05-22

## Purpose

Verify availability for scope 0055 (new hook events).

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
