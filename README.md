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
   directory).

3. Done. On load the plugin:
   - verifies the vendored hook tree next to `plugin.ts`
     (`<repo>/vendor/throughliner/hooks/pre_tool_use.py` must exist — without
     it the plugin disables itself and logs one line), and
   - materializes the five method skills into
     `~/.config/opencode/skills/<name>/SKILL.md`, rewriting
     `${CLAUDE_PLUGIN_ROOT}` to the real vendor path (idempotent; content
     unchanged → no rewrite).

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
- **Subagent cost gate** — spawning a subagent (`task` tool) triggers a
  permission prompt with the cost reason. In an interactive TUI you approve or
  decline; in headless `opencode run` (no `--auto`) OpenCode auto-rejects
  instantly and the shim treats that as allow-and-log (never blocks a headless
  run); with `--auto` it is auto-approved.
- **Queue lint** — after `QUEUE.md` writes, structural findings (e.g. a
  `####` entry with no trailing `[slug]`) are appended to the tool output as
  advisory context.
- **Stop check** — when a session goes idle, a claim like "I filed
  [some-slug]" that is not actually in `QUEUE.md` re-prompts the session to
  fix it (once per claim; marker-guarded).

## Environment overrides

| Variable             | Meaning                                              |
|----------------------|------------------------------------------------------|
| `THROUGHLINER_ROOT`  | Override the vendored hook tree location             |
| `THROUGHLINER_PYTHON`| Python interpreter for the hooks (default `python3`) |

## Uninstall

Remove the `plugin` line from your config. The materialized skills remain in
`~/.config/opencode/skills/` — delete those five directories if you want them
gone.

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
npx tsc -p .test/tsconfig.check.json
npx esbuild opencode/plugin.ts --bundle --format=esm --platform=node --outfile=.test/plugin.mjs
node --test test/harness.mjs   # 20 tests, ~20s
```

The suite drives the real bundle with a mock OpenCode client and the **real
vendored Python hooks**, asserting the translation contract end-to-end
(denies, allows, ask paths, stop blocks, skill materialization, fail-open).
