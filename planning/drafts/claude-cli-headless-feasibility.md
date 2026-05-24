# Claude CLI Headless Feasibility
*Research date: 2026-05-20 — CLI version: @anthropic-ai/claude-code@2.1.145*

---

## Summary

Partially possible. The CLI has supported non-interactive mode (`-p`/`--print`) with JSON output and `--plugin-dir` for scripted invocations. **Key tension:** `--bare` (recommended for scripted/CI) skips hooks. Without `--bare`, hooks fire but user settings contaminate the test environment. The loop is automatable; clean hook isolation needs a workaround (see Open Questions). **Billing change:** starting June 15, 2026, `claude -p` draws from a separate Agent SDK credit.

---

## Relevant CLI Flags

Key flags from `claude --help` (v2.1.145), scripting-relevant only:

| Flag | Purpose |
|---|---|
| `-p` / `--print` | Non-interactive mode; exit after response |
| `--bare` | Minimal mode — skips hooks, LSP, plugin sync, CLAUDE.md discovery |
| `--plugin-dir <path>` | Load plugin for this session (repeatable) |
| `--output-format <fmt>` | `text` (default), `json`, `stream-json` |
| `--include-hook-events` | Emit hook lifecycle events (requires `stream-json`) |
| `--permission-mode <mode>` | `acceptEdits`, `auto`, `bypassPermissions`, `default`, `dontAsk`, `plan` |
| `--max-budget-usd <n>` | Hard ceiling per run |
| `--settings <file-or-json>` | Additional settings to load |
| `--verbose` | More intermediate state |
| `--debug [filter]` | Debug mode with category filtering |
| `--no-session-persistence` | Disable session persistence |

---

## Docs Findings

Source: https://code.claude.com/docs/en/headless (fetched 2026-05-20).

- **Non-interactive mode is first-class.** `-p` works with all CLI options.
- **`--plugin-dir` works in scripted mode.** Explicitly listed in bare-mode reference table.
- **`--bare` skips hooks.** Recommended for scripted/CI, but central tension for hook testing. Will become `-p` default in a future release.
- **Hooks fire in non-bare `-p` mode.** Third-party guide (techsy.io) confirms; official docs don't contradict.
- **`--include-hook-events`** exposes hook lifecycle events in stream-json output.
- **`system/init` event** reports `plugins` array (loaded) and `plugin_errors` array — assert plugin loaded at run start.
- **`parent_tool_use_id`** tags subagent tool calls in stream-json (from Agent SDK streaming docs).
- **Billing change June 15, 2026.** `claude -p` on subscription plans draws from separate Agent SDK credit.
- **Known bug #27398:** `--setting-sources user` silently skips plugin hooks. Only affects wrapper processes hardcoding that flag.

---

## Tool-Trace Visibility

Using `--output-format stream-json --include-hook-events --verbose`:

| Signal | How to assert |
|---|---|
| Plugin loaded | `system/init` → `plugins` array |
| Plugin failed | `system/init` → `plugin_errors` |
| Hook fired | Hook lifecycle events (via `--include-hook-events`) |
| Main-agent tool call | `content_block_start` with `type: "tool_use"` |
| Subagent tool call | Same + `parent_tool_use_id` set |
| Hook blocked tool | Stream shows tool result with error content (exact format unverified) |
| Session cost | `total_cost_usd` in final `result` event |

**Cannot cleanly assert on:** hook script internals (need side-channel log), whether `parent_tool_use_id` appears in raw CLI stream-json vs SDK wrapper only (see Open Questions), exact hook exit code as parseable field.

---

## Proof-of-Concept Shape

Minimal unattended smoke-test. **Do not use `--bare`** (skips hooks).

### PowerShell script

```powershell
$PLUGIN_DIR  = "C:\Users\Alex\Desktop\Taskflow Planning\No code method\sovereign-implementer"
$FIXTURE_DIR = "C:\tmp\smoke-fixture-001"
$OUTPUT_FILE = "C:\tmp\smoke-output-001.jsonl"

Push-Location $FIXTURE_DIR
claude -p "Exercise SessionStart, PreToolUse, and Stop." `
  --plugin-dir $PLUGIN_DIR `
  --output-format stream-json `
  --include-hook-events --verbose `
  --permission-mode bypassPermissions `
  --max-budget-usd 0.10 `
  > $OUTPUT_FILE 2>&1
$exitCode = $LASTEXITCODE
Pop-Location

# Parse + assert
$lines = Get-Content $OUTPUT_FILE | Where-Object { $_ } | ForEach-Object {
    try { $_ | ConvertFrom-Json } catch { $null }
} | Where-Object { $_ }

$initEvent = $lines | Where-Object { $_.type -eq "system" -and $_.subtype -eq "init" }
$pluginLoaded = $initEvent.plugins | Where-Object { $_.path -like "*sovereign-implementer*" }
if (-not $pluginLoaded) { Write-Error "FAIL: plugin did not load" }

$hookEvents = $lines | Where-Object { $_.type -eq "hook_event" }
$sessionStartFired = $hookEvents | Where-Object { $_.hook_event_name -eq "SessionStart" }
if (-not $sessionStartFired) { Write-Error "FAIL: SessionStart hook did not fire" }

if ($exitCode -ne 0) { Write-Error "FAIL: claude exited $exitCode" }
```

**Key flags:** `-p` (non-interactive), `--plugin-dir` (load plugin), `--output-format stream-json` (required for `--include-hook-events`), `--permission-mode bypassPermissions` (unattended), `--max-budget-usd` (ceiling), **no `--bare`** (would skip hooks).

No PTY needed. `claude -p` detects non-TTY stdout and drops interactive UI.

---

## Open Questions

### 1. Hook event type names in stream-json
`--include-hook-events` is documented but event `type`/`subtype` values are not. **Resolve:** one test run, grep for `hook` in output.

### 2. `parent_tool_use_id` in raw CLI stream-json
Documented in Agent SDK types. Unknown whether raw CLI includes it natively or SDK assembles it. **Resolve:** one run with subagent invocation, check output.

### 3. User-settings contamination
Without `--bare`, user settings load alongside plugin hooks. **Resolve:** test `--settings "{}"` to see if it suppresses user hooks without suppressing plugin hook discovery.

### 4. Agent SDK credit limits (June 15, 2026)
Credit amount for Pro plan and exhaustion behaviour unspecified. **Resolve:** check https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan before building automated loop.
