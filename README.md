# Throughliner for Hermes Agent

[Throughliner](https://github.com/FlintcraftTech/throughliner) is a spec-driven
workflow for agentic coding: a `QUEUE.md` of work items, a `SPEC.md` contract,
session-scoped build files, and five method commands that move work through
plan → build → queue. This port runs the **unmodified** upstream hooks
(vendored pristine at `vendor/throughliner/`, pinned to upstream
`v1.21.1` / commit `743aa63`) under [Hermes Agent](https://github.com/NousResearch/Hermes-Agent)
as a native Python plugin.

## Requirements

- Hermes Agent **>= 0.20.5** (port developed and verified against 0.20.5)
- Python 3 (the vendored hooks are stdlib-only; the plugin uses the
  interpreter it runs under, so no separate `python3` on PATH is needed)
- git

The model is whatever Hermes is configured with (`hermes setup`);
Throughliner is model-agnostic and makes no model choice.

## Install

Hermes's installer runs a security scan before installing any external
plugin. This repo will report a **dangerous** verdict — and every finding in
it is a false positive: the vendored upstream docs legitimately reference
agent-config files (the upstream method maintains a managed block in the
project's Claude Code config file), and this port's own docs reference the
Hermes config file. The scanner treats any such reference *in documentation*
as a persistence signal, and a single critical finding blocks
`hermes plugins install` outright — `--force` does not override a dangerous
verdict. The hooks themselves are stdlib-only, spawn only the vendored hook
scripts, and fail open on every error path.

Two install paths (both permanent; the loaded plugin is identical):

**Path A — installer, with the install-time scan disabled:**

```
hermes config set plugins.scan_on_install false
hermes plugins install <port-git-url> --ref <40-hex-sha> --enable
```

`--ref` takes the full 40-hex SHA of the pinned commit you verified
(see Provenance). You can re-enable the scan afterwards — it only governs
future installs, not this plugin.

**Path B — manual clone (no scan involved):**

```
git clone --depth 1 --branch <port-branch> <port-git-url> ~/.hermes/plugins/throughliner
hermes plugins enable throughliner
```

This is exactly what the installer does (clone into `~/.hermes/plugins/<name>/`);
the runtime loader performs no security scan. Recommended if you prefer to
keep the install-time scan on.

Either way, on first load the plugin:

- verifies the vendored hook tree (`vendor/throughliner/hooks/pre_tool_use.py`
  must exist — without it the plugin disables itself and logs one line),
- materializes the five method skills into
  `~/.hermes/skills/throughliner/tl-<name>/SKILL.md` (idempotent), and
- registers the lifecycle hooks.

Manage it with `hermes plugins list`, `hermes plugins disable throughliner`,
`hermes plugins remove throughliner`.

## The five commands

Type these yourself in the Hermes prompt (TUI, one-shot, or gateway):

| Command      | Purpose                                                        |
|--------------|----------------------------------------------------------------|
| `/tl-setup`  | Create `SPEC.md` + `QUEUE.md` for a new or adopted project     |
| `/tl-plan`   | Turn the next queued item into a build plan                    |
| `/tl-next`   | Execute the current build (scope-locked to the build's `Files:`) |
| `/tl-rescan` | Re-read project state into the session context                 |
| `/tl-done`   | Close out the build: file results, commit, queue updates       |

Why the `tl-` prefix: Hermes ships its own `plan` skill
(`software-development/plan`), and skill name resolution is
first-come-first-served — a bare `plan` would silently shadow or be shadowed
depending on scan order. The `tl-*` set is deterministic and never collides.
The vendored docs' prose still refers to the bare names; the mapping is 1:1.

Model self-invocation is denied: if the model tries to `skill_view` any of the
five (bare or `tl-` name), the vendored Skill hook blocks it with "the /x
command is yours to type" — same as upstream. (Hermes has no
`disable-model-invocation` equivalent, so the installed skills are
model-visible in the skills index; the hook is what keeps them user-only.)

## What the plugin enforces

All decisions come from the vendored Python hooks; the plugin only translates
Hermes hook kwargs to the Claude hook protocol and back:

- **Session orientation** — `session_start.py` output is injected into the
  first user message of each turn (`{"context": ...}`), plus the `brevity.md`
  output style as a system-prompt section.
- **Scope lock** — while a build file `_build-<session>.md` exists, writes
  outside its `Files:` list are blocked; the session's own build file is
  always editable.
- **Git guard** — `git push --force` etc. blocked.
- **Subagent cost gate** — `delegate_task` escalates to Hermes's native
  human-approval gate (`{"action": "approve"}` — the platform's only "ask"
  channel): the user gets once/session/always/deny.
- **Queue lint** — after `QUEUE.md` writes, structural findings are parked in
  `.throughliner/pending-context.md` (Hermes has no context channel on
  post-tool events) and surfaced as context on the next LLM call.
- **Stop check** — when the agent ends a turn claiming a slug that is not
  actually in `QUEUE.md`, the vendored `stop.py` blocks the stop
  (`pre_verify`, when files were mutated) with the correction; when it cannot
  observe (a report with no writes), the correction is parked for the next
  LLM call via `on_session_end`. Loop-protected by the vendored claim markers.
- **Plugin trace** — every hook fire appends a JSON line to
  `.throughliner/.shim-<sessionID>.jsonl` in the project. The fastest way to
  see what the port did; also `HERMES_PLUGINS_DEBUG=1` and
  `hermes logs --level DEBUG`.

Add `.throughliner/` to your project's `.gitignore` (it holds the shim trace,
parked notes, and the vendored loop-protection markers).

## One-shot usage

```
hermes -z "run tl-next: do the next build" -s tl-next --in <project-dir> \
  --accept-hooks --pass-session-id --usage-file usage.json
```

`-s tl-next` preloads the skill body (slash-command parsing is unreliable
under `-z`); `--in` sets the project cwd the hooks see. Note: `-z`
auto-bypasses approvals, so the subagent cost gate auto-resolves under
one-shot — it prompts interactively in the TUI/gateway.

## Manual install (no plugin)

Copy the five adapted skills into `~/.hermes/skills/throughliner/` (the
plugin's materializer does this; the adapted files live there after any plugin
load) and add a `hooks:` block to `~/.hermes/config.yaml` — see
[`example/hooks-config.yaml`](example/hooks-config.yaml). The shell-hook path
downgrades the subagent cost gate from "ask" to "deny with explanation"
(shell hooks have no approve channel), so the plugin install is preferred.

## Environment overrides

| Variable             | Meaning                                              |
|----------------------|------------------------------------------------------|
| `THROUGHLINER_ROOT`  | Override the vendored hook tree location             |
| `THROUGHLINER_PYTHON`| Python interpreter for the hooks (default: the interpreter Hermes runs under) |

## Uninstall

`hermes plugins remove throughliner`. The materialized skills remain in
`~/.hermes/skills/throughliner/` — delete that directory if you want them gone.

## Provenance

`vendor/throughliner/` is byte-identical to upstream
`FlintcraftTech/throughliner` at `743aa63166ce4875305c7d97041a1b462b0fdc2c`
(`v1.21.1`), pinned and verified by `vendor/MANIFEST.sha256`
(`tools/vendor.sh` re-checks it). Every port change lives outside `vendor/`
and is a reviewable diff. See `PROVENANCE.md` and `ANALYSIS.md` (full
platform mapping, source-verified).

## Tests

```
python3 -m unittest test.test_hermes -v    # 17 tests, ~2s
```

The suite drives the real plugin module with synthetic Hermes hook kwargs
(shaped by the host's fire sites) and the **real vendored Python hooks**,
asserting the translation contract end-to-end (denies, ask escalation, stop
blocks + loop protection, lint parking/draining, skill materialization,
fail-open).
