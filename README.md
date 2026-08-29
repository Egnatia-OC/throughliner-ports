# Throughliner for OpenCode

[Throughliner](https://github.com/FlintcraftTech/throughliner) is a spec-driven
workflow for agentic coding: a `QUEUE.md` of work items, a `SPEC.md` contract,
session-scoped build files, and five method commands that move work through
plan → build → queue. This port runs the **unmodified** upstream hooks
(vendored pristine at `vendor/throughliner/`, pinned to upstream
`v1.21.1` / commit `743aa63`) under [OpenCode](https://opencode.ai) via a thin
plugin shim.

## Requirements

- OpenCode (the shim was verified against 1.18.x plugin/SDK contracts)
- Python 3 (`python3` on `PATH`) — the vendored hooks are Python
- git

The model is whatever OpenCode is configured with; Throughliner is
model-agnostic and makes no model choice.

## Install

1. Put this repository anywhere on disk, e.g. `git clone <url> ~/dev/throughliner-opencode`.
2. Add the plugin to your OpenCode config — per project (recommended, so the
   plugin only fires where you want it):

   ```json
   // <project>/.opencode/opencode.json
   { "plugin": ["/home/you/dev/throughliner-opencode/opencode/plugin.ts"] }
   ```

   or globally in `~/.config/opencode/opencode.json` for every project.
   Absolute paths, paths relative to the config file, and `file://` URLs all
   work (OpenCode resolves path plugin specs against the config file's
   directory). A minimal config template is checked in at
   `example.opencode.json`.

3. Done. On load the plugin:
   - verifies the vendored hook tree next to `plugin.ts`
     (`<repo>/vendor/throughliner/hooks/pre_tool_use.py` must exist — without
     it the plugin disables itself and logs one line), and
   - materializes the five method skills into the OpenCode global skills dir
     `~/.config/opencode/skills/<name>/SKILL.md` (a global side effect — the
     skills are then available in every project; override the location with
     `THROUGHLINER_SKILLS_DIR`), rewriting `${CLAUDE_PLUGIN_ROOT}` to the real
     vendor path (idempotent; content unchanged → no rewrite), and
   - writes a per-session trace to `<project>/.throughliner/.shim-<sid>.jsonl`
     (add `.throughliner/` to the project's `.gitignore`; disable with
     `THROUGHLINER_TRACE=0`).

## The five commands

Type these yourself in the OpenCode prompt — the plugin **denies model
self-invocation** of all five, exactly as upstream intends:

| Command   | Purpose                                                        |
|-----------|----------------------------------------------------------------|
| `/setup`  | Create `SPEC.md` + `QUEUE.md` for a new or adopted project     |
| `/plan`   | Turn the next queued item into a build plan                    |
| `/next`   | Execute the current build (scope-locked to the build's `Files:`) |
| `/rescan` | Re-read project state into the session context                 |
| `/done`   | Close out the build: file results, commit, queue updates       |

**Headless automation note:** `opencode run` treats a non-TTY *open* stdin as
piped input and waits on it. When scripting runs, redirect stdin:
`opencode run … < /dev/null` (verified 1.18.x).

## What the shim enforces

All decisions come from the vendored Python hooks; the shim only translates
OpenCode events to the Claude hook protocol and back:

- **Session orientation** — `session_start.py` output is appended to the
  system prompt (fresh per LLM call, never cumulative), plus the `brevity.md`
  output style.
- **Scope lock** — while a build file `_build-<session>.md` exists, writes
  outside its `Files:` list are denied; the session's own build file is always
  editable.
- **Git guard** — `git push --force` etc. denied.
- **Subagent cost gate** — a `task` (subagent) spawn carries the vendored
  cost reason. OpenCode 1.18.x gives plugins no way to raise a permission
  prompt (the SDK has no permission-create method, and the `permission.ask`
  hook is declared but never triggered — source-verified in `ANALYSIS.md`),
  so the shim records the reason in the trace and lets OpenCode's own
  permission system gate the call: default config prompts in the TUI,
  headless `opencode run` auto-rejects (approve with `--auto`), and
  `permission: { "task": "allow" }` in `opencode.json` disables the gate.
- **Queue lint** — after `QUEUE.md` writes, structural findings (e.g. a
  `####` entry with no trailing `[slug]`) are appended to the tool output as
  advisory context.
- **Stop check** — when a session goes idle, a claim like "I filed
  [some-slug]" that is not actually in `QUEUE.md` re-prompts the session to
  fix it (once per claim; marker-guarded).

Treat this as a workflow guardrail, not a security boundary: every shim
failure mode is fail-open, and enforcement covers only the mapped host tools
(write/edit/bash/task/skill). The orientation injection also rides on the
`experimental.chat.system.transform` hook (verified in 1.18.21, re-verified in 1.18.25); if a future
OpenCode renames it, orientation silently stops appearing — the trace file
shows whether the hook fired.

## Environment overrides

| Variable             | Meaning                                              |
|----------------------|------------------------------------------------------|
| `THROUGHLINER_ROOT`  | Override the vendored hook tree location             |
| `THROUGHLINER_PYTHON`| Python interpreter for the hooks (default `python3`) |
| `THROUGHLINER_SKILLS_DIR` | Override the skills dir the plugin materializes into |
| `OPENCODE_CONFIG_DIR`     | If set, skills materialize under `<dir>/skills` (OpenCode auto-loads it) |
| `THROUGHLINER_TRACE`    | Set `0` to disable the `.throughliner/` trace files |

## Uninstall

Remove the `plugin` line from your config. The materialized skills remain in
`~/.config/opencode/skills/` — delete those five directories if you want them
gone. Per-project `.throughliner/` trace directories remain in your projects.

## Provenance

`vendor/throughliner/` is byte-identical to upstream
`FlintcraftTech/throughliner` at `743aa63166ce4875305c7d97041a1b462b0fdc2c`
(`v1.21.1`), pinned and verified by `vendor/MANIFEST.sha256`
(`tools/vendor.sh` re-checks it). Every port change lives outside `vendor/`
and is a reviewable diff. See `PROVENANCE.md` and `ANALYSIS.md` (full
platform mapping, source-verified).

## Tests

```sh
npm install
npm run typecheck   # tsc -p tsconfig.json (strict, no emit)
npm test            # esbuild bundle + node --test test/harness.mjs — 19 tests
```

The same flow runs in CI on every push (`.github/workflows/test.yml`), plus a
`sha256sum -c` of the vendored tree.

The suite drives the real bundle with a mock OpenCode client and the **real
vendored Python hooks**, asserting the translation contract end-to-end
(denies, allows, ask degradation, stop blocks, skill materialization,
fail-open). The mock client implements the real 1.18.x SDK call shapes
(`{ path: { id } }` envelopes) and rejects anything else — a hand-imagined
API fails the suite.

## License

CC BY-NC-SA 4.0 — non-commercial. See `LICENSE`.
