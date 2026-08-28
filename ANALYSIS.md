# Throughliner → Hermes: ANALYSIS

Port target: pristine upstream vendored at `vendor/throughliner/` (pinned `743aa63166ce4875305c7d97041a1b462b0fdc2c`, v1.21.1, 34 files, identity via `vendor/MANIFEST.sha256`; invariant: no vendored file is ever modified). Strategy (per the verified omp reference port at `/home/oc/reports/throughliner`): pristine vendored Python + thin shim translating Hermes events ↔ Claude hook JSON + declarative files; fail-open everywhere.

---

## 1. Harness overview + exact version

- **Hermes Agent CLI** (`hermes`), installed version **0.20.5** — `~/.hermes/hermes-agent/pyproject.toml`: `name = "hermes-agent"`, `version = "0.20.5"`.
- Python-based agent. Config: `~/.hermes/config.yaml` (HERMES_HOME; profile-scoped via `-p NAME`, which sets HERMES_HOME). Surfaces: CLI/TUI, chat one-shot, gateway, desktop.
- Tool names the hooks will see (file/shell tier): `read_file`, `write_file`, `patch`, `search_files`, `terminal` (`tools/file_tools.py:2815-2818`); subagent tool: `delegate_task` (`tools/delegate_tool.py:4767-4768`).
- Logs: `~/.hermes/logs/{agent,errors,gateway,gui,desktop}.log`; `hermes logs [-f] [--level L] [--since 1h]` (`hermes_cli/subcommands/logs.py:20-29`).
- No per-project hook config: shell hooks come only from the profile `config.yaml` (`register_from_config(load_config())`). Project-level injection is via context files (below) and repo-local skills.

## 2. Extension model (paths + formats, quoted from install)

### 2.1 Skills
- Paths: `~/.hermes/skills/<category>/<name>/SKILL.md` (flat `~/.hermes/skills/<name>/SKILL.md` also works); repo-local `./.hermes/skills/` + `./.agents/skills/` at the git root (highest precedence; trust-gated by `skills.trusted_project_dirs` in config — `hermes skills trust <path>`; `agent/skill_utils.py:623-767`); `skills.external_dirs` = read-only extra dirs.
- Frontmatter spec (agentskills.io-compatible, `tools/skills_tool.py:28-45`, verbatim):
  ```
  ---
  name: skill-name              # Required, max 64 chars
  description: Brief description # Required, max 1024 chars
  version: 1.0.0                # Optional
  license: MIT                  # Optional
  platforms: [macos]            # Optional — valid: macos, linux, windows
  prerequisites:
    env_vars: [API_KEY]
    commands: [curl, jq]
  compatibility: Requires X     # Optional
  metadata:
    hermes:
      tags: [fine-tuning, llm]
      related_skills: [peft, lora]
  ---
  ```
- Unknown frontmatter keys are ignored (lenient YAML parse) — the vendored skills' Claude-only keys `disable-model-invocation: true` / `user-invocable: true` parse fine but have NO effect in Hermes (there is no user-only-invocation gate; every installed skill is model-visible).
- Exposure: compact name+description index in the system prompt (`build_skills_system_prompt`, `agent/prompt_builder.py:1828`); full body on demand via `skill_view`/`skills_list` tools; user invocation via `/<skill-name>` slash command; `-s NAME` preloads the body into the first message.
- **No env-var expansion in skill content** (no `expandvars` anywhere in `tools/skills_tool.py`): `${CLAUDE_PLUGIN_ROOT}/docs/setup.md` in the vendored SKILL.md bodies renders literally. The port must install NEW skill files (outside `vendor/`) with references rewritten to real install paths — same approach as the omp port's `<plugin-root>` handling.
- Bundles: YAML files in `~/.hermes/skill-bundles/` (`agent/skill_bundles.py:66-70`), `hermes bundles create <name> --skill a --skill b`, invoked as `/<bundle-slug>` (`hermes_cli/bundles.py:1-169`).
- `hermes skills install <owner/repo/path | https-URL-to-SKILL.md> [--name X] [--category Y] [--force] [--yes]` (`hermes_cli/subcommands/skills.py:109-127`).

### 2.2 Hooks — two mechanisms

**(a) Shell hooks** — `hooks:` block in `~/.hermes/config.yaml`. Entry fields (from `agent/shell_hooks.py` `_parse_single_entry`:437-523 + the example below): `matcher` (regex, `fullmatch` on tool_name; honored ONLY for pre/post_tool_call — warned+ignored elsewhere), `command` (executed via `shlex.split`, `shell=False`), `timeout` (default 60s, max 300s), `fail_closed` (bool, pre_tool_call only; `failClosed` accepted). Verbatim config example (`cli-config.yaml.example:1723-1740`):
  ```yaml
  # hooks:
  #   pre_tool_call:
  #     - matcher: "terminal"
  #       command: "~/.hermes/agent-hooks/block-rm-rf.sh"
  #       timeout: 10
  #   post_tool_call:
  #     - matcher: "write_file|patch"
  #       command: "~/.hermes/agent-hooks/auto-format.sh"
  #   pre_llm_call:
  #     - command: "~/.hermes/agent-hooks/inject-cwd-context.sh"
  #   subagent_stop:
  #     - command: "~/.hermes/agent-hooks/log-orchestration.sh"
  #
  # hooks_auto_accept: false
  ```
- Consent: first use of each (event, command) prompts on a TTY, then persists to `~/.hermes/shell-hooks-allowlist.json`; headless needs `--accept-hooks` flag / `HERMES_ACCEPT_HOOKS=1` / `hooks_auto_accept: true` (`agent/shell_hooks.py:_resolve_effective_accept`).
- Fail-open is the default; `fail_closed` makes spawn-error/timeout/malformed-stdout on pre_tool_call BLOCK with `hook <command> failed closed: <reason>` (`_fail_closed_block`, lines 641-646). `HERMES_SAFE_MODE=1` skips shell-hook registration entirely.
- CLI: `hermes hooks {list, test <event> [--for-tool X] [--payload-file F.json], revoke <command>, doctor}` (`hermes_cli/hooks.py:1-300`).
- Shell-supported events (comment at `cli-config.yaml.example:1708-1713`): `pre_tool_call, post_tool_call, pre_llm_call, post_llm_call, pre_api_request, post_api_request, on_session_start, on_session_end, on_session_finalize, on_session_reset, subagent_stop`. Full `VALID_HOOKS` set (Python plugin path, `hermes_cli/plugins.py:161-368`) adds: transform_terminal_output, transform_tool_result, transform_llm_output, on_stream_start/delta/end, on_interim_message, pre_verify, api_request_error, transform_api_error_classification (SHELL_UNSUPPORTED — shell registration refused), on_skill_lifecycle, subagent_start, pre_gateway_dispatch, pre_approval_request, post_approval_response, pre_transcription, kanban_* family, gateway_platform_event, pre_command.

**(b) Native plugin hooks** — `ctx.register_hook(event, callback)` (`hermes_cli/plugins.py:3130`). Callbacks return directive dicts — a SUPERSET of shell-hook stdout:
- `pre_tool_call`: `{"action":"block","message":...}` | `{"action":"approve","message":..., "rule_key":...}` (escalates to the human-approval gate — once/session/always/deny prompt; fail-closed if the gate errors) | `{"action":"modify","args":{...}}` (shallow-merged into tool args). First valid directive wins; anything else is ignored (`_get_pre_tool_call_directive_details`, `hermes_cli/plugins.py:6124-6225`). **`approve` is ONLY available here — it is the sole Hermes channel for Claude's "ask".**
- `pre_verify`: `{"action":"continue","message":...}` or Claude-Stop `{"decision":"block","reason":...}` = keep the agent going (`get_pre_verify_continue_message`, `hermes_cli/plugins.py:6406-6440`; same translation in `agent/shell_hooks.py:826-833`).
- Any event: `{"context": "..."}`; on `pre_llm_call` it is injected into the user message (`agent/turn_context.py:1273-1315`, with oversized-context spill to disk). `on_session_start`/`on_session_end` returns are ignored (observer-only).

### 2.3 Plugins
- **Native**: `~/.hermes/plugins/<name>/` = `plugin.yaml` + `__init__.py` with `register(ctx)`. Real example (`plugins/observability/langfuse/plugin.yaml`, verbatim):
  ```yaml
  name: langfuse
  version: "1.0.0"
  description: "Optional Langfuse observability for Hermes — traces conversations, LLM calls, and tool usage. Opt-in via `hermes plugins enable observability/langfuse` or `hermes tools → Langfuse Observability`."
  author: NousResearch
  requires_env:
    - HERMES_LANGFUSE_PUBLIC_KEY
    - HERMES_LANGFUSE_SECRET_KEY
  hooks:
    - pre_api_request
    - post_api_request
    - api_request_error
    - pre_llm_call
    - post_llm_call
    - pre_tool_call
    - post_tool_call
    - on_session_finalize
    - on_session_end
    - subagent_start
    - subagent_stop
  ```
  `register(ctx)` API (`hermes_cli/plugins.py:1400-3400`): `register_hook`, `register_tool`, `register_skill(name, path, description, frontmatter)` → skill resolvable as `<plugin>:<name>` via `skill_view` but **not** listed in the `<available_skills>` index — "opt-in explicit loads only" (3340-3360), `register_system_prompt_section(id, content)` (3155), `register_command` (slash), `register_cli_command`, `get_config`/`set_config` (namespaced `plugins.entries.<id>.settings`).
- Enable: `plugins: {enabled: [name]}` in config or `hermes plugins enable <name>`. Install: `hermes plugins install <git-url | owner/repo | index-name> [--enable | --no-enable] [--ref <40-hex-SHA>] [--force]` (`hermes_cli/subcommands/plugins.py`). Also: `update`, `remove`, `list`, `doctor [--ci]`, `capabilities`, `pack` (hermes-pack.yaml sets), `show`, `search`.
- **Portable Agent Plugins v1** (root `plugin.json`): translated to skills + MCP only; "Portable packages install disabled"; no hooks, no Python. NOT usable for Throughliner (hooks are the core).
- Debug: `HERMES_PLUGINS_DEBUG=1` → verbose plugin-discovery logs to stderr + agent.log (`hermes_cli/plugins.py:112-116`).

### 2.4 Identity / output style / context files
- `SOUL.md` in HERMES_HOME = identity slot #1 of the system prompt (`agent/prompt_builder.py`).
- Personalities: `agent.personalities: {name: "text"}` map + `display.personality: <name>` selector (this machine's config carries the full personalities map; `display.personality: ''`). `agent.system_prompt` = manual overlay.
- Project context files, **first match wins**, cwd only (`build_context_files_prompt`, `agent/prompt_builder.py:2537-2600`): `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules` / `.cursor/rules/*.mdc`; plus SOUL.md.

### 2.5 One-shot CLI (`hermes_cli/_parser.py`, verbatim help)
- `-z/--oneshot PROMPT`: "One-shot mode: send a single prompt and print ONLY the final response text to stdout. No banner, no spinner, no tool previews, no session_id line. Tools, memory, rules, and AGENTS.md in the CWD are loaded as normal; approvals are auto-bypassed. Intended for scripts / pipes."
- `-s/--skills NAME`: "Preload one or more skills for the session (repeat flag or comma-separate)"
- `--in DIR`: "Change into DIR before starting or resuming. Combined with '--resume latest' or -c, the most recent session for DIR's workspace is picked, and the session stays in DIR (skips the recorded-cwd restore)."
- `-m/--model` / `--provider`: per-invocation overrides ("Applies to -z/--oneshot and --tui. Also settable via HERMES_INFERENCE_MODEL env var."); `--provider` has no `choices=`, so user-defined custom-provider names pass.
- Also: `--accept-hooks`, `--yolo` ("Bypass all dangerous command approval prompts"), `--pass-session-id` ("Include the session ID in the agent's system prompt"), `--usage-file PATH` (JSON usage report after a -z run, written even on failure), `--ignore-user-config`, `--safe-mode`, `-V/--version`; `chat` subcommand: `-q/--query`, `-Q/--quiet`, `--max-turns N`, `--run-budget SECONDS`, `--source TAG` ('tool' hides from session lists), `-r/--resume`, `-c/--continue`, `-w/--worktree`.

## 3. Mapping table (Claude Code mechanism → Hermes)

| # | Claude Code mechanism | Hermes equivalent | Path / format | Fidelity |
|---|---|---|---|---|
| 1 | Five SKILL.md skills (setup/plan/next/rescan/done) | File skills `~/.hermes/skills/throughliner/<name>/SKILL.md` (or trusted repo-local `./.hermes/skills/`) | NEW SKILL.md files outside `vendor/` (frontmatter reduced to name+description; body = vendored text with `${CLAUDE_PLUGIN_ROOT}` refs rewritten to the real install path) | **exact** (frontmatter is a compatible subset) — two caveats: (a) vendored `plan` name collides with bundled `~/.hermes/skills/software-development/plan/SKILL.md` (profile tier shadows bundled) → rename installed skill (e.g. `tl-plan`) or accept shadowing; (b) `disable-model-invocation`/`user-invocable` have no Hermes equivalent — the model can invoke the skills too |
| 2 | PreToolUse hook (scope-lock + git guard + subagent ask-gate) | `pre_tool_call` hook — native plugin callback (recommended) or shell hook | Shim builds the Claude payload `{cwd, tool_name, tool_input}` from Hermes kwargs. Tool-name map: `write_file`→`Write` (`path`→`file_path`), `patch`→`Edit` (`path`→`file_path`), `terminal`→`Bash` (`command`), `delegate_task`→`Task`; parse vendored stdout `hookSpecificOutput.permissionDecision` = `deny`→`{"action":"block"}` / exit 2, `ask`→`{"action":"approve"}`, `allow`→None | **exact** for deny (JSON or exit 2); **exact** for ask via the plugin path (approve escalation, `hermes_cli/plugins.py:6131-6140`); **missing** for ask via shell hooks (stdout supports block/modify only — `agent/shell_hooks.py:775-830`); upstream's 3 matcher groups collapse into one hook with in-shim `tool_name` gating (or 3 config entries with regex matchers) |
| 3 | PostToolUse hook (advisory QUEUE.md lint) | `post_tool_call` hook (shell or plugin) | Fires with `result`, `status` ("ok"\|"error"\|"blocked"), `error_type`, `error_message`, `duration_ms`, `tool_call_id`, … | **adapted**: fires at the right moment, but there is NO context-injection channel on post_tool_call → lint findings can't ride next to the tool result. Workaround: shim writes findings under `.throughliner/`; `pre_llm_call` surfaces them on the next LLM call |
| 4 | SessionStart context injection | `pre_llm_call` hook filtered on `is_first_turn` | `{"context": "..."}` injected into the first user message (`agent/turn_context.py:1273-1315`); `on_session_start` fires too but its return value is ignored at the fire site (`conversation_loop.py:1044-1056`) | **adapted**: fires per LLM call (shim must no-op when `is_first_turn` is false); context rides the user message, not the system prompt |
| 5 | Stop hook (false-report block-once) | `on_session_end` (reliable per-turn observer, every turn incl. interrupted) + `pre_verify` (the only stop-equivalent with a decision channel) | on_session_end kwargs: session_id, task_id, turn_id, completed, failed, interrupted, turn_exit_reason, model, platform (`agent/turn_finalizer.py:822-832`). pre_verify kwargs: session_id, platform, model, coding, attempt, final_response, changed_paths (`hermes_cli/plugins.py:6424-6432`; fire site `conversation_loop.py:8292-8307`) | **adapted (partial)**: pre_verify accepts Claude-Stop `{"decision":"block","reason"}` = keep going (`final_response` ↔ `last_assistant_message`), but fires ONLY when the agent mutated files that turn and is capped by `agent.max_verify_nudges` — the primary failure mode (report with no write ⇒ no mutation) never fires pre_verify. Fallback: run stop.py on on_session_end, write the pending correction to `.throughliner/`, surface via pre_llm_call next turn. Block-once semantics are preserved by stop.py's own `.throughliner/stop-claim-<sid>-<slug>.marker` files (`stop.py:200-224`) |
| 6 | Output style (brevity.md) | `register_system_prompt_section(id, content)` (native plugin) — or `agent.personalities` + `display.personality`, or SOUL.md append | `plugin.yaml` + `__init__.py` | **adapted**: no first-class "output style"; system-prompt section is the closest |
| 7 | Plugin/marketplace packaging | No marketplace. Native plugin: `hermes plugins install <git-url> --enable`; or manual (skills copy + `hooks:` block) | `plugin.yaml` + `__init__.py` at the port repo root | **missing/adapted**: single-unit install exists (native plugin) but there is no registry/marketplace; portable plugin.json cannot carry hooks |

## 4. Event/payload schemas (verbatim from source — the shim author must not guess a field)

### 4.1 Shell-hook stdin payload
`agent/shell_hooks.py` module docstring (lines 27-39):
```
{
    "hook_event_name": "pre_tool_call",
    "tool_name":       "terminal",
    "tool_input":      {"command": "rm -rf /"},
    "session_id":      "sess_abc123",
    "cwd":             "/home/user/project",
    "extra":           {...}   # event-specific kwargs
}
```
Built by `_serialize_payload` (~line 750): top-level keys = `hook_event_name`, `tool_name`, `tool_input` (= `kwargs["args"]` if dict else None), `session_id` (= session_id or parent_session_id), `cwd` (= `Path.cwd()`), `extra` (= all other kwargs).

Per-event `extra` keys (docstring 89-122):
- pre_tool_call: `task_id, tool_call_id, turn_id, api_request_id, middleware_trace`
- post_tool_call: `result, status ("ok"|"error"|"blocked"), error_type, error_message, duration_ms, task_id, tool_call_id, turn_id, api_request_id, middleware_trace`
- pre_llm_call: `user_message, conversation_history, is_first_turn, model, platform, task_id, turn_id, parent_session_id, sender_id`
- on_session_end: `task_id, turn_id, completed, interrupted, model, platform` (+ `failed`, `turn_exit_reason` at the fire site)
- pre_verify: `platform, model, coding, attempt, final_response, changed_paths`
- on_session_start: `model, platform`
- subagent_stop: `parent_session_id, child_role, child_summary, child_status, tool_call_history, duration_ms`

### 4.2 Shell-hook stdout contract (`agent/shell_hooks.py:775-860`)
- pre_tool_call: `{"action":"block","message":...}` or Claude-style `{"decision":"block","reason":...}`; modify: `{"action":"modify","args":{...}}` / `{"decision":"modify","tool_input":{...}}`. **No approve/ask channel.**
- pre_verify: `{"action":"continue","message":...}` or Claude-Stop `{"decision":"block","reason":...}` → keep going; a continue with no message is a no-op.
- Any event: `{"context": "..."}` passes through.
- Empty/non-JSON stdout = silent no-op (warning logged). Exit code 2 = block on pre_tool_call ONLY (`_BLOCKING_EVENTS = frozenset({"pre_tool_call"})`, `BLOCK_EXIT_CODE = 2`); other non-zero exits warn, stdout still parsed.
- Fail-open default; `fail_closed`/`failClosed` (pre_tool_call only) → block with `hook <command> failed closed: <reason>` on spawn error/timeout/unparseable stdout. Timeout default 60s, max 300s; `shlex.split`, `shell=False`; `HERMES_SAFE_MODE=1` skips registration.
- Registration log line: `shell hook registered: %s -> %s (matcher=%s, timeout=%ds, fail_closed=%s)` (`agent/shell_hooks.py:324-328`).

### 4.3 Native plugin callback return shapes (`hermes_cli/plugins.py`)
- pre_tool_call (6124-6225): `{"action": "block", "message": "Reason the tool was blocked"}` | `{"action": "approve", "message": "Why this needs human confirmation", "rule_key": "write_file:ssh"}` | `{"action": "modify", "args": {...}}`. "The first valid directive wins. Invalid or irrelevant hook return values are silently ignored."
- pre_verify (6406-6440): `{"action": "continue", "message": "<follow-up for the model>"}` — "The Claude-Code Stop shape `{"decision": "block", "reason": "..."}` (block the stop == keep going) is accepted too. The first directive carrying a non-empty message wins; any other return lets the turn finish."
- pre_llm_call: `{"context": str}` (`agent/turn_context.py:1295-1315`).
- on_session_start / on_session_end: observer-only, return ignored.

### 4.4 Fire-site kwargs (exact)
- pre_tool_call: `invoke_hook("pre_tool_call", tool_name=..., args=..., task_id=..., session_id=..., tool_call_id=..., turn_id=..., api_request_id=..., middleware_trace=...)` (`hermes_cli/plugins.py:6144-6158`).
- pre_llm_call: `session_id, task_id, turn_id, user_message, conversation_history, is_first_turn=(not bool(conversation_history)), model, platform, parent_session_id, sender_id` (`agent/turn_context.py:1280-1293`).
- on_session_end: `session_id, task_id, turn_id, completed, failed, interrupted, turn_exit_reason, model, platform` — "Fired at the very end of every run_conversation call" (`agent/turn_finalizer.py:822-832`).
- pre_verify: `session_id, platform, model, coding, attempt, final_response, changed_paths` (`hermes_cli/plugins.py:6424-6432`); fire site `agent/conversation_loop.py:8292-8307`, gated by `_edited and has_hook("pre_verify") and _attempt < max_verify_nudges()` where `_edited = sorted(getattr(agent, "_turn_file_mutation_paths", set()))` (8285). `max_verify_nudges` = config `agent.max_verify_nudges` (`agent/verify_hooks.py:35-39`).

### 4.5 `hermes hooks test` synthetic payloads (`hermes_cli/hooks.py`, `_DEFAULT_PAYLOADS`, verbatim)
```python
"pre_tool_call": {"tool_name": "terminal", "args": {"command": "echo hello"}, "session_id": "test-session", "task_id": "test-task", "tool_call_id": "test-call"},
"post_tool_call": {"tool_name": "terminal", "args": {"command": "echo hello"}, "session_id": "test-session", "task_id": "test-task", "tool_call_id": "test-call", "result": '{"output": "hello"}', "duration_ms": 42},
"pre_llm_call": {"session_id": "test-session", "user_message": "What is the weather?", "conversation_history": [], "is_first_turn": True, "model": "gpt-4", "platform": "cli"},
"post_llm_call": {"session_id": "test-session", "model": "gpt-4", "platform": "cli"},
"pre_verify": {"session_id": "test-session", "platform": "cli", "model": "gpt-4", "coding": True, "attempt": 0, "final_response": "All done — the change is applied.", "changed_paths": ["src/app.tsx"]},
"on_session_start": {"session_id": "test-session"},
"on_session_end": {"session_id": "test-session", "task_id": "test-task", "turn_id": "test-turn", "completed": True, "failed": False, "interrupted": False, "turn_exit_reason": "text_response(stop)", "model": "gpt-4", "platform": "cli"},
"on_session_finalize": {"session_id": "test-session"},
"on_session_reset": {"session_id": "test-session"},
```
`hermes hooks test <event> [--for-tool X] [--payload-file F.json]`: the dict is merged over the synthetic payload, then the CONFIGURED shell hooks for that event are really executed through the production-identical wire (`run_once` → `_serialize_payload`/`_spawn`/`_evaluate_result`) and the `parsed:` canonical directive is printed. Caveats: (1) only shell-configured hooks run — plugin-registered hooks are invisible to `hooks test`; (2) `--for-tool` filters pre/post_tool_call by matcher.

### 4.6 Consent allowlist (`~/.hermes/shell-hooks-allowlist.json`)
```json
{"approvals": [{"event": "pre_tool_call", "command": "<cmd>", "approved_at": "<iso8601Z>", "script_mtime_at_approval": "<iso8601Z>"}]}
```
Drift (script mtime newer than approval) is flagged by `hermes hooks list` ("⚠ script modified since approval") and checked by `hermes hooks doctor` (also validates exec bit: bare invocation needs X_OK, interpreter-prefixed needs R_OK — `script_is_executable`, `agent/shell_hooks.py:1050-1070`).

### 4.7 Upstream (vendored) hook contracts the shim must serve
- `hooks/pre_tool_use.py` stdin: `{"cwd", "tool_name", "tool_input"}` (reads `data.get("cwd")`, `data.get("tool_name")`, `data.get("tool_input")` at 1072-1074). Claude tool names inside: `Task`/`Agent` (ask-gate, 1090), `Skill` (1111), `Bash`/`PowerShell` (git safety, 1147; reads `tool_input["command"]`), `Edit`/`Write`/`MultiEdit` (scope-lock, 1280; reads `tool_input["file_path"]`). Stdout: `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny"|"ask", "permissionDecisionReason": ...}}` (191-216); fail-open on any parse error.
- `hooks/stop.py` stdin: `{"last_assistant_message", "cwd", "session_id"}` (218-228). Stdout: `{"decision": "block", "reason": ...}` = block the stop (keep the turn going); exit 0; loop-protected by `.throughliner/stop-claim-<sid[:40]>-<slug>.marker` files.
- `hooks/session_start.py` stdin: Claude SessionStart payload (uses `cwd`); reads env `CLAUDE_PLUGIN_ROOT` to locate `docs/skill-nonspecific-rules.md` (1234, 1099) — **the shim must set `CLAUDE_PLUGIN_ROOT` in the spawn env, pointing at the vendored tree root**. Stdout: `{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "..."}}` (1925-1930, nested envelope — a top-level additionalContext is discarded upstream).
- `hooks/post_tool_use.py`: advisory QUEUE.md lint, findings "fed back to Claude as context next to the tool result" (i.e. via Claude PostToolUse additionalContext — no Hermes channel, see §5.2).

## 5. Gaps & risks

1. **No "ask" channel in shell hooks.** The vendored subagent cost-ask (`permissionDecision: "ask"`) is inexpressible from shell-hook stdout (block/modify only). → **Recommended: native plugin callback** (returns `{"action":"approve"}`) — the only faithful path. Shell-hook fallback: shim maps ask→block with an explanatory reason (posture change: "prompt with full choice" becomes "deny with explanation").
2. **No context-injection channel on post_tool_call / on_session_end / Stop** (and on_session_start's return is ignored). Claude PostToolUse additionalContext and Stop-feedback have no direct equivalent. → `pre_llm_call` context on the next LLM call, with file-mediated handoff under `.throughliner/` (shim-owned, gitignored in the project).
3. **pre_verify is conditional and capped**: fires only when the agent mutated files that turn (`_turn_file_mutation_paths`) and is bounded by `agent.max_verify_nudges`. stop.py's primary failure mode (report with no write ⇒ no mutation) is never seen by pre_verify. → Run stop.py on BOTH on_session_end (reliable, advisory-via-next-turn) and pre_verify (best-effort block-when-observable). Do NOT use on_session_finalize/on_session_reset for Stop logic — those are session-identity boundaries (/new, /reset, gateway expiry), not turn ends.
4. **Skill name collision**: vendored `plan` (frontmatter `name: plan`) vs bundled `~/.hermes/skills/software-development/plan/SKILL.md`; profile tier shadows bundled. Installing `plan` would shadow Hermes's own plan skill for the whole profile. → rename installed skill (e.g. `tl-plan`) + rewrite `/plan` cross-references in the ported skill/doc bodies, or namespace all five (`tl-*`). Decision for the build phase; smoke must assert which `plan` resolves.
5. **`disable-model-invocation: true` has no equivalent**: every installed skill is model-visible in Hermes; the model can load /setup etc. without the user typing. Acceptable (the skills are safe to load) but a semantic drift — document in the port README.
6. **`${CLAUDE_PLUGIN_ROOT}` in skill/doc bodies**: no env expansion in Hermes skill rendering; vendored files are pristine → port installs NEW skill files outside `vendor/` with references rewritten to real install paths; the shim sets `CLAUDE_PLUGIN_ROOT` for the spawned hook scripts.
7. **cwd in plugin callbacks**: not passed in pre_tool_call kwargs — shim uses `os.getcwd()` (CLI chdirs into `--in DIR` before the agent starts; `terminal.cwd` config also applies). Shell payloads carry `cwd` explicitly.
8. **Consent friction (shell hooks only)**: per-(event,command) TTY prompt or headless opt-in. Native plugin hooks need no consent (enabling the plugin is consent). Another point for the native-plugin recommendation.
9. **Fail-open posture preserved**: Hermes default is fail-open (spawn error/timeout/malformed stdout → warn, contribute nothing) — matches the vendored hooks' own fail-open design (stop.py exits 0 on any parse error; pre_tool_use.py never raises). `fail_closed` exists for pre_tool_call but the port must NOT enable it by default (a crashed hook would start blocking writes) — document as opt-in.
10. **`-z` auto-bypasses approvals** ("approvals are auto-bypassed", `_parser.py:158-161`): under `-z`, the `approve` directive's human gate likely auto-resolves — the ask-gate cannot be interactively smoke-tested in one-shot; assert the directive is PRODUCED (shim log / `hooks test` for the shell path) rather than the prompt.
11. **Portable plugin.json can't carry hooks** → the stranger install must be the native plugin layout (`hermes plugins install <git-url> --enable`).
12. **`hermes hooks test` only sees shell-configured hooks** — for the plugin path, smoke = live one-shot runs + `HERMES_PLUGINS_DEBUG=1` + `hermes logs --level DEBUG`; optionally register the shim as a shell hook in the local test config to reuse `hooks test`.
13. **on_session_end fires per user message (turn), including interrupted/incomplete turns** — matches Claude Stop timing (fires when the agent finishes responding). It is the reliable per-turn record point.

## 6. Smoke-test plan

Prereqs: port installed (plugin enabled + skills in place), model configured (§7). Budget: CPU llama.cpp, 3–15 min per agent run — run the five skill one-shots plus hook-triggering runs sequentially; expect ~1–2 h wall time.

### 6.1 One-shot per skill
Template (scratch git project per skill; `--in` sets the cwd the hooks see; `-s` preloads the skill body — slash-command parsing is unreliable under `-z`):
```
cd /tmp/smoke/tl-<skill> && git init -q
git config user.email smoke@example.com && git config user.name Smoke
hermes -z "You are running the <skill> skill of the Throughliner method. <one-line task for that skill>." \
  -s <installed-skill-name> --in /tmp/smoke/tl-<skill> \
  -m /models/Qwen3.8-27B-UD-Q4_K_M.gguf --provider <provider-from-§7> \
  --accept-hooks --pass-session-id --usage-file /tmp/smoke/tl-<skill>.usage.json
```
- **setup**: "set up this folder with the Throughliner method; answer interview questions minimally (one-word answers)." Assert: `SPEC.md`, `QUEUE.md` (both `## Processed` / `## Unprocessed` sections), `LOG/` exist and are non-empty.
- **plan**: "plan: add a new idea '<x>' to the queue." Assert: new `#### ... [slug]` work item under `## Unprocessed` in `QUEUE.md`.
- **next**: (in the same project, after plan) "run the next skill: do the next build." Assert: build working file `_build-<session-id>.md` with a `Files:` section + a `LOG/` entry.
- **rescan**: "rescan this project for drift and report." Assert: report references concrete QUEUE.md state.
- **done**: "close out: run the done skill." Assert: queue processed / git commit made.

### 6.2 Observing the four hook paths
(a) **pre_tool_call (scope-lock + git guard)** — live: in the `next` run, instruct "also write /tmp/smoke/outside.txt" → expect the final response to report the BLOCK (the block message returns to the model as the tool result); then instruct `git add -A && git commit -m x` → expect the blanket-add denial text. Debug: `hermes logs --since 1h --level DEBUG | grep -iE 'hook|block'`; registration line `shell hook registered: pre_tool_call -> ...` (shell path) or the plugin's own debug lines under `HERMES_PLUGINS_DEBUG=1`.
(b) **post_tool_call (lint)** — after a `plan` run that writes `QUEUE.md`: check `.throughliner/` for the shim's lint side-file (§5.2 workaround) and `hermes logs --level DEBUG` for the post_tool_call fire.
(c) **SessionStart context (pre_llm_call, is_first_turn)** — each one-shot's first turn must begin with the orientation context ("not adopted → /setup" / active-build resume). Observable in the resumed session transcript (`hermes --resume <id>`) and via the shim's own log line ("session_start context injected (N chars)"). Synthetic (shell path only): `hermes hooks test pre_llm_call` prints the `parsed:` context (synthetic payload has `is_first_turn: True`).
(d) **Stop (on_session_end + pre_verify)** — every run ends with on_session_end: assert stop.py ran (its claim check; if the final response names a slug absent from QUEUE.md, the correction lands in `.throughliner/` for the next turn). pre_verify: in the `next` run (files mutated) the shim log shows the fire with `final_response`; synthetic: `hermes hooks test pre_verify` (shell path) prints the parsed continue.
- `hermes hooks list` — configured hooks + consent status; `hermes hooks doctor` — exec bit + script drift.
- `HERMES_PLUGINS_DEBUG=1` on every run for plugin discovery/registration trace.

## 7. Smoke-test model config — THIS MACHINE ONLY (never ship these values)

Machine: CPU llama.cpp box. Local OpenAI-compatible endpoint `http://192.168.1.117:8083/v1`, model id `/models/Qwen3.8-27B-UD-Q4_K_M.gguf`. `~/.hermes/config.yaml` already has providers on these hosts (verbatim, relevant entries):
```yaml
model:
  base_url: https://api.minimaxi.com/v1
  default: glm-5.3
  provider: zai
providers:
  mirai-router:
    base_url: http://192.168.1.117:8083/v1
custom_providers:
  - name: mirai-qwen38
    base_url: http://192.168.1.117:8085/v1
    context_length: 262144
    model: Qwen3.8-27B-UD-Q5_K_XL.gguf
    api_key: not-needed
    extra_body: {chat_template_kwargs: {enable_thinking: false}}
  - name: mirai-router
    base_url: http://192.168.1.117:8083/v1
    api_key: ''
    model: /models/Qwen3.8-27B-Q4_K_M.gguf
    context_length: 160000
  - name: mirai-mercury
    base_url: http://192.168.1.117:8082/v1
    api_key: not-needed
    model: /models/Qwen3.8-27B-Q4_K_M.gguf
    context_length: 160000
    models: {/models/Qwen3.8-27B-UD-Q4_K_M.gguf: {}}
    models_discovered: true
```
Smoke recipe (pick one):
1. Per-invocation override (no config edit): append `-m /models/Qwen3.8-27B-UD-Q4_K_M.gguf --provider mirai-router` to every one-shot (`--provider` has no `choices=`, so user-defined names pass; keyed `providers:` entries normalize into `custom_providers`).
2. Or add one `custom_providers` entry: `- name: mirai-qwen38-ud / base_url: http://192.168.1.117:8083/v1 / api_key: not-needed / model: /models/Qwen3.8-27B-UD-Q4_K_M.gguf / context_length: 160000` (+ optionally `extra_body: {chat_template_kwargs: {enable_thinking: false}}` like the 8082/8085 entries) and use `--provider mirai-qwen38-ud`.
`-z --usage-file` gives per-run token/cost accounting. Cloud glm-5.3 (zai) is the configured default if the local box is down.

## 8. Universal install contract (end-user, model-agnostic)

Prereqs for ANY user on ANY machine:
- Hermes **>= 0.20.5** (port developed and verified against 0.20.5; relies on shell hooks, native plugins, `register_hook` directives incl. `approve`, and one-shot `-z`, all present at 0.20.5).
- Python 3 on PATH (the vendored hooks are stdlib-only).
- git.
- Any model/provider already configured in Hermes (`hermes setup`). **The port is model-agnostic — Throughliner is a workflow layer, never a model choice.** No machine-specific paths, endpoints, or credentials appear in any shipped file.

Install (stranger path, single command):
```
hermes plugins install <port-git-url> --enable
```
The port repo root carries `plugin.yaml` + `__init__.py` + the vendored tree; `register()` self-copies the five adapted skill files into `~/.hermes/skills/throughliner/` idempotently on first load (so skills land in the model-visible index + `/<name>` slash commands) and registers the hooks (pre_tool_call, post_tool_call, pre_llm_call, on_session_end, pre_verify) as callbacks that translate Hermes kwargs ↔ Claude hook JSON and spawn the pristine vendored scripts with `CLAUDE_PLUGIN_ROOT` set.

Usage: `cd <project> && hermes`, then type `/setup` (or the installed skill name) in a new or existing project folder.

Alternative manual install (no plugin): copy the five adapted SKILL.md into `~/.hermes/skills/throughliner/<name>/` and add the `hooks:` block to `~/.hermes/config.yaml` (shell-hook path — accepts the ask→block downgrade, §5.1), then answer the one-time first-use consent prompt (or run with `--accept-hooks` headless).