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

## Rule gate — the mechanical half

The vendored method ships the *judgment* side of the rule gate: at close, a
session whose work touched the project's rules records a disposition
(`Rule gate: <slug> — run, …` / `— not needed, <why>`; see
`vendor/throughliner/docs/next.md`). Upstream pairs that judgment with a
small script that re-checks the mechanical half against the project's own
records; their script is hardwired to their repo's paths, so this port ships
a layout-agnostic re-implementation of the same four checks:

```sh
python3 opencode/scripts/rule_corpus_check.py <project-dir> \
    [--rules PATH ...] [--log-dir DIR] [--dup-threshold 0.85] \
    [--retired NAME ...] [--capture-queue QUEUE.md]
```

Checks: `gate-line` (every rule-authoring session's record carries a
`Rule gate:` line), `not-needed-growth` (a "not needed" disposition is not
contradicted by rule text growing in the entry's own commit), `near-dup`
(no two rule segments say nearly the same thing), `retired-name` (no live
rule names a retired mechanism — names from any `## Retired` section in the
rules files plus `--retired` flags). Exit codes: 0 clean, 1 findings, 2
usage/setup error. `--capture-queue` files the findings as work items in
the queue's Unprocessed section (stable slugs; re-runs never duplicate).
Rule-authoring sessions are detected conservatively: the entry's
`**Files touched:**` line or its title must name a rules file.

The session-start orientation points the model at the script, so a session
that must run a rule-gate pass can find it. A clean run proves the checks
ran, never that the rules are good — the checks verify record-keeping
consistency, not rule quality; that stays with the judgment gate.


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
python3 test/rule_corpus_check.py  # 6 tests, throwaway git projects
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
