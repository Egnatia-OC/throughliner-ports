# Claude CLI Headless Feasibility
*Research date: 2026-05-20 — CLI version tested: @anthropic-ai/claude-code@2.1.145*

---

## Summary

Partially possible today, with one significant constraint that affects your specific case. The `claude` CLI has a documented, supported non-interactive mode (`-p` / `--print`) with JSON output and stdin/stdout plumbing. `--plugin-dir` is explicitly listed as usable in scripted invocations. The blocker is `--bare`: the docs recommend it for all scripted/CI calls, but `--bare` explicitly **skips hooks**. If you omit `--bare`, hooks fire — but you pick up whatever happens to be configured in your local user settings, which muddies the test environment. This is a real tension, not a papercut. The loop itself is automatable; clean isolation of the hook surface requires a deliberate workaround (detailed in Open Questions below). The billing situation also changed: starting **June 15, 2026** (in 26 days), `claude -p` usage on subscription plans draws from a new monthly Agent SDK credit separate from your interactive limits — worth knowing before you invest in an automated loop.

---

## `claude --help` Output — Relevant Flags

Verbatim from `npx @anthropic-ai/claude-code@2.1.145 --help`. Only flags relevant to scripting are reproduced; the full output is available by running `claude --help` locally.

```
Usage: claude [options] [command] [prompt]

Claude Code - starts an interactive session by default, use -p/--print for
non-interactive output

Arguments:
  prompt                    Your prompt

Options:
  --add-dir <directories...>
      Additional directories to allow tool access to

  --allowedTools, --allowed-tools <tools...>
      Comma or space-separated list of tool names to allow
      (e.g. "Bash(git *) Edit")

  --append-system-prompt <prompt>
      Append a system prompt to the default system prompt

  --bare
      Minimal mode: skip hooks, LSP, plugin sync, attribution,
      auto-memory, background prefetches, keychain reads, and
      CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1.
      Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper
      via --settings (OAuth and keychain are never read).
      Explicitly provide context via: --system-prompt[-file],
      --append-system-prompt[-file], --add-dir (CLAUDE.md dirs),
      --mcp-config, --settings, --agents, --plugin-dir.

  -d, --debug [filter]
      Enable debug mode with optional category filtering
      (e.g., "api,hooks" or "!1p,!file")

  --debug-file <path>
      Write debug logs to a specific file path (implicitly enables
      debug mode)

  --fallback-model <model>
      Enable automatic fallback to specified model when default
      model is overloaded (only works with --print)

  --include-hook-events
      Include all hook lifecycle events in the output stream
      (only works with --output-format=stream-json)

  --include-partial-messages
      Include partial message chunks as they arrive
      (only works with --print and --output-format=stream-json)

  --input-format <format>
      Input format (only works with --print): "text" (default),
      or "stream-json" (choices: "text", "stream-json")

  --json-schema <schema>
      JSON Schema for structured output validation.

  --max-budget-usd <amount>
      Maximum dollar amount to spend on API calls
      (only works with --print)

  --no-session-persistence
      Disable session persistence (only works with --print)

  --output-format <format>
      Output format (only works with --print): "text" (default),
      "json" (single result), or "stream-json" (realtime streaming)
      (choices: "text", "json", "stream-json")

  --permission-mode <mode>
      Permission mode to use for the session
      (choices: "acceptEdits", "auto", "bypassPermissions",
      "default", "dontAsk", "plan")

  --plugin-dir <path>
      Load a plugin from a directory or .zip for this session only
      (repeatable: --plugin-dir A --plugin-dir B.zip) (default: [])

  --plugin-url <url>
      Fetch a plugin .zip from a URL for this session only
      (repeatable)

  -p, --print
      Print response and exit (useful for pipes). Note: The
      workspace trust dialog is skipped when Claude is run in
      non-interactive mode (via -p, or when stdout is not a TTY,
      e.g. piped or redirected output). Only use this in
      directories you trust. Settings files that fail validation
      are silently ignored in this mode (no error dialog is shown).

  --settings <file-or-json>
      Path to a settings JSON file or a JSON string to load
      additional settings from

  --system-prompt <prompt>
      System prompt to use for the session

  --verbose
      Override verbose mode setting from config
```

---

## Docs Findings

Primary source: Anthropic's own programmatic-usage page at `https://code.claude.com/docs/en/headless` (fetched 2026-05-20).

**Non-interactive mode is first-class and documented.**

> "Add the `-p` (or `--print`) flag to any `claude` command to run it non-interactively. All CLI options work with `-p`."

Source: https://code.claude.com/docs/en/headless

**`--plugin-dir` is explicitly listed as a flag that works in bare/scripted mode.**

The bare-mode reference table on the same page lists plugins under "To load / Use":

> `--plugin-dir <path>`, `--plugin-url <url>`

So the docs explicitly endorse passing `--plugin-dir` in scripted calls.

**`--bare` is the recommended mode for scripted calls — but it skips hooks.**

> "Add `--bare` to reduce startup time by skipping auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md."
> "`--bare` is the recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release."

Source: https://code.claude.com/docs/en/headless

The `--help` flag list confirms: `--bare` skips "hooks" explicitly. This is the central tension for your use case — you cannot use the recommended scripted mode and also test hooks.

**Hooks do fire in non-bare `-p` mode.**

A third-party guide (https://techsy.io/en/blog/claude-code-hooks-guide) states:

> "Claude Code hooks work in headless mode (`claude -p`) with some differences: Notification hooks still fire but you should redirect to logging instead of desktop alerts. PreToolUse hooks with exit code 2 can pause headless sessions for human review."

There is no contradicting statement in the official docs; the docs only say `--bare` skips hooks, which implies non-bare `-p` does not.

**`--include-hook-events` exposes hook lifecycle in the stream.**

The `--help` output confirms: `--include-hook-events` includes all hook lifecycle events in the output stream, but only works with `--output-format=stream-json`.

**The `system/init` event in stream-json reports loaded plugins.**

> "The `system/init` event reports session metadata including the model, tools, MCP servers, and loaded plugins. [...] Use the plugin fields to fail CI when a plugin did not load."
>
> | Field | Type | Description |
> |---|---|---|
> | `plugins` | array | plugins that loaded successfully, each with `name` and `path` |
> | `plugin_errors` | array | plugin load-time errors, each with `plugin`, `type`, and `message` |

Source: https://code.claude.com/docs/en/headless — this means you can assert "did my plugin load?" at the start of every run.

**Subagent tool calls carry `parent_tool_use_id` in stream-json.**

From the Agent SDK streaming docs (https://code.claude.com/docs/en/agent-sdk/streaming-output):

> `parent_tool_use_id: str | None  # Parent tool ID if from a subagent`

This is in the Python SDK's `StreamEvent` dataclass, but the underlying stream-json format is the same from the CLI. Subagent events are tagged with the tool use ID of the `Task`/`Agent` call that spawned them.

**Billing change incoming: June 15, 2026.**

> "Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit, separate from your interactive usage limits."

Source: https://code.claude.com/docs/en/headless — check https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan for the credit amounts.

**Known bug: plugin hooks do not fire when `--setting-sources user` is in effect (Cowork-specific).**

GitHub issue #27398 documents that when a process hardcodes `--setting-sources user`, plugin `hooks/hooks.json` is silently skipped while skills still work. This bug is Cowork-specific (Cowork hardcodes that flag) and should not affect direct CLI invocations. Filed 2026-02-21, status unknown at time of writing. Relevant as a flag if you ever run your smoke tests via Cowork rather than direct CLI.

---

## Tool-Trace Visibility in Non-Interactive Mode

### What you can assert on

Using `--output-format stream-json --include-hook-events --verbose`:

| Signal | How to assert | Format |
|---|---|---|
| Plugin loaded | `system/init` event, `plugins` array contains your plugin's `name` and `path` | JSON |
| Plugin failed to load | `system/init` event, `plugin_errors` array non-empty | JSON |
| Hook fired | Hook lifecycle events in stream (via `--include-hook-events`) | JSON |
| Tool called by main agent | `content_block_start` event with `type: "tool_use"`, `name` field | JSON |
| Tool called by subagent | Same as above but event has `parent_tool_use_id` set to the parent `Task`/`Agent` tool_use_id | JSON |
| Hook blocked a tool | `PreToolUse` hook returning exit code 2 / `permissionDecision: "deny"` — surfaces in stream as a tool result with error content | JSON (inferred from hook docs; exact format unverified) |
| Session cost | `total_cost_usd` in the final `result` event (`--output-format json`) or `message_delta` usage fields | JSON |

### What you cannot (or cannot cleanly) assert on

- **Hook script internals**: You can see that a hook fired and whether it blocked/allowed; you cannot easily assert on what your hook script *wrote to its own log file* from the stream alone. You'd need to check a side-channel log or have the hook write a fixture file.
- **Exact subagent tool trace without SDK**: The `parent_tool_use_id` linkage is documented in the Python/TypeScript Agent SDK. Whether it's present in the raw CLI `stream-json` output (as opposed to the SDK wrapper) is asserted in third-party tooling but not explicitly confirmed in official CLI docs. See Open Questions.
- **Hook exit code in stream**: Whether the exact exit code (0 vs 2) of a hook is surfaced as a parseable field, or only as downstream tool-block feedback, is not confirmed in official docs.

---

## Proof-of-Concept Shape

This is the minimal viable shape for an unattended smoke-test run. **Do not use `--bare`** — it would skip hooks, which are what you're testing.

### PowerShell (Windows 11, Git Bash path or native PS)

```powershell
# ---- CONFIG ----
$PLUGIN_DIR   = "C:\Users\Alex\Desktop\Taskflow Planning\No code method\sovereign-implementer"
$FIXTURE_DIR  = "C:\tmp\smoke-fixture-001"       # pre-created fixture folder
$OUTPUT_FILE  = "C:\tmp\smoke-output-001.jsonl"
$PROMPT       = "Do the thing that exercises SessionStart, then PreToolUse, then Stop."

# ---- SETUP ----
# (fixture folder already staged before this script runs)

# ---- INVOKE ----
Push-Location $FIXTURE_DIR
claude -p $PROMPT `
  --plugin-dir $PLUGIN_DIR `
  --output-format stream-json `
  --include-hook-events `
  --verbose `
  --permission-mode bypassPermissions `
  --max-budget-usd 0.10 `
  > $OUTPUT_FILE 2>&1
$exitCode = $LASTEXITCODE
Pop-Location

# ---- ASSERT ----
$lines = Get-Content $OUTPUT_FILE | Where-Object { $_ } | ForEach-Object {
    try { $_ | ConvertFrom-Json } catch { $null }
} | Where-Object { $_ }

# 1. Plugin loaded?
$initEvent = $lines | Where-Object { $_.type -eq "system" -and $_.subtype -eq "init" }
$pluginLoaded = $initEvent.plugins | Where-Object { $_.path -like "*sovereign-implementer*" }
if (-not $pluginLoaded) { Write-Error "FAIL: plugin did not load" }

# 2. SessionStart hook fired?
$hookEvents = $lines | Where-Object { $_.type -eq "hook_event" }   # exact type TBD — see Open Questions
$sessionStartFired = $hookEvents | Where-Object { $_.hook_event_name -eq "SessionStart" }
if (-not $sessionStartFired) { Write-Error "FAIL: SessionStart hook did not fire" }

# 3. Tool calls visible?
$toolCalls = $lines | Where-Object {
    $_.type -eq "stream_event" -and $_.event.type -eq "content_block_start" `
    -and $_.event.content_block.type -eq "tool_use"
}
Write-Host "Tools called: $($toolCalls | ForEach-Object { $_.event.content_block.name } | Sort-Object -Unique)"

# 4. Exit clean?
if ($exitCode -ne 0) { Write-Error "FAIL: claude exited $exitCode" }
```

### Key flags

| Flag | Why |
|---|---|
| `-p` | Non-interactive mode; required |
| `--plugin-dir` | Load your plugin for this session |
| `--output-format stream-json` | Parseable JSONL; required for `--include-hook-events` |
| `--include-hook-events` | Emit hook lifecycle events into the stream |
| `--verbose` | Surfaces more intermediate state |
| `--permission-mode bypassPermissions` | Prevents permission prompts from blocking an unattended run; use only in your test fixture directory |
| `--max-budget-usd` | Hard ceiling per run — sanity-check for loops |
| **No `--bare`** | Bare mode skips hooks; omitting it is required for hook testing |

### Shape constraint

The loop does not need a PTY. Direct pipe (`> file`) or `Start-Process` with stdout/stderr redirect works. `claude -p` detects non-TTY stdout and drops the interactive UI automatically (per the `--print` help text).

---

## Open Questions

### 1. Exact event type name for hook lifecycle events in stream-json

**What's unknown**: `--include-hook-events` is documented at the flag level but the official docs do not specify what `type` / `subtype` values the emitted JSON objects carry. The `system/init` event format is documented; hook lifecycle event fields are not.

**How to resolve**: Run `claude -p "list files in this directory" --plugin-dir <path> --output-format stream-json --include-hook-events --verbose` against a minimal fixture and `cat` the output. Grep for any line where `hook` appears in the JSON. One run, 5 minutes.

---

### 2. Does `parent_tool_use_id` appear in raw CLI stream-json (not just SDK wrappers)?

**What's unknown**: The `parent_tool_use_id` field is explicitly documented in the Agent SDK Python/TypeScript `StreamEvent` type. It is less clear whether the raw CLI `--output-format stream-json` output includes this field natively, or whether the SDK assembles it by correlating events.

**How to resolve**: Run a prompt that deliberately invokes a subagent (e.g., a `Task` tool call), capture stream-json, and check whether any line includes `parent_tool_use_id`. One targeted run.

---

### 3. Hook environment when no `--setting-sources` flag is passed

**What's unknown**: Without `--bare` and without `--setting-sources`, `claude -p` loads user settings from `~/.claude/settings.json`. If hooks are defined there, they fire alongside plugin hooks. This is environment contamination for a smoke test.

**How to resolve**: Pass `--settings "{}"` (an empty inline JSON object) to suppress user-settings loading while keeping plugin settings active. Needs a quick experiment to confirm this suppresses `~/.claude/settings.json` without also suppressing plugin hook discovery. The `--settings` flag is documented as "additional settings to load" which suggests it doesn't replace the settings stack, but the interaction with `--setting-sources` is unclear.

---

### 4. June 15, 2026 Agent SDK credit — monthly limit and Pro plan behaviour

**What's unknown**: The docs note that `claude -p` usage on subscription plans will draw from a new Agent SDK credit starting June 15. The credit amount for the Pro plan and what happens at exhaustion (hard stop vs. pay-per-use vs. degraded access) is not specified in the docs page.

**How to resolve**: Check https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan before building a looped test harness — the credit situation directly affects how many automated runs are practical per month.
