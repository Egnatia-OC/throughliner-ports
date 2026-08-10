# Can a hook force the behaviour rules to be read?

Fetched 2026-08-10 from the Claude Code hooks reference
(`https://code.claude.com/docs/en/hooks`, reached via a 301 from the older
`docs.claude.com/en/docs/claude-code/hooks`). Run because `session_start.py`'s
behaviour-rules directive is an instruction with no enforcement behind it, and
its own docstring names "a skimmed redirect" as the failure mode it accepts.

## Finding 1 — `SessionStart` cannot force anything

`SessionStart` hooks support context only. They **cannot block or deny**. The
fields available under `hookSpecificOutput` are `additionalContext`,
`initialUserMessage`, `watchPaths`, `sessionTitle` and `reloadSkills`.

So there is no way to make the read happen *at session start*. Any forcing
mechanism has to fire later, at the first tool call.

## Finding 2 — the 10,000-character cap is PER HOOK COMMAND, not aggregate

The documented wording: hook output strings, including `additionalContext`,
`systemMessage`, and plain stdout, are capped at 10,000 characters, and output
exceeding the limit is saved to a file and replaced with a preview and file
path.

The reference states this limit applies **per hook command**, not in aggregate.
When one hook's output exceeds the cap, Claude Code writes the full text to a
file and passes a preview plus the path instead.

**This matters because it contradicts the stated premise of the current
design.** `session_start.py:360-384` says the rules are pointed at rather than
pasted because the file "is tens of kilobytes, so appending it whole blew the
cap by a wide margin and the rules reached no session at all". That is true of
*one* hook command. Several `SessionStart` commands, each emitting under 10,000
characters, could carry the rules directly into the session with no read
required.

Unmeasured and not to be assumed: whether the harness concatenates multiple
SessionStart outputs cleanly, in a stable order, and whether the total is
subject to any separate limit further up. The doc says nothing either way.
Verify by experiment before designing on it.

## Finding 3 — `PreToolUse` receives `transcript_path`, and can deny

Input fields to a `PreToolUse` hook include `session_id`, `prompt_id`,
**`transcript_path`**, `cwd`, `permission_mode`, `effort`, `hook_event_name`,
plus `agent_id` / `agent_type` in a subagent, and the tool-specific
`tool_name`, `tool_input`, `tool_use_id`.

Example shape given in the reference:

```json
{
  "session_id": "abc123",
  "prompt_id": "550e8400-e29b-41d4-a716-446655440000",
  "transcript_path": "/home/user/.claude/projects/.../transcript.jsonl",
  "cwd": "/home/user/my-project",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "rm -rf /tmp/build" },
  "tool_use_id": "toolu_01ABC123..."
}
```

Denial is available two ways — structured output:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook"
  }
}
```

with `permissionDecision` accepting `"allow"`, `"deny"`, `"ask"` or `"defer"`;
or exit code 2 with the reason on stderr.

**So a read-gate is constructible:** a `PreToolUse` rule that reads
`transcript_path`, looks for a completed Read of the behaviour doc, and denies
(or asks) until it finds one.

Unmeasured: the transcript's on-disk format and whether a Read's target path is
recoverable from it reliably; how the gate behaves on resume, on compaction, and
in a subagent, all of which change what the transcript holds. The mechanism is
confirmed available; its reliability is not.

## What this does not settle

Whether either mechanism is worth building. Both have real costs — a per-call
transcript scan on every tool use, or several hook commands whose combined
behaviour is undocumented. This file records that the options exist, against a
shipped design that assumed they did not.
