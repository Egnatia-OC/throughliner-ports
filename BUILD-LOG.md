# Build log

A running record of decisions, changes, and reasoning. Newest first. Written for a friend skimming, not an auditor — half a page per session, less when possible.

For format details, see the project's `CLAUDE.md` → *Build log*.

---

## V18 — 2026-05-12 — Plugin scaffold + SessionStart hook + JSON path block

**What shipped.** The plugin's bones are now on disk at `plugin/`. A minimal `.claude-plugin/plugin.json` manifest, a `hooks/hooks.json` declaring a `SessionStart` hook, a Python script (`session_start.py`) that emits the eight universal behavioural rules — push back, plain English, no stealth fixes, red-flag surfacing, the rest — as `additionalContext` at every session start. The rules text lives in `hooks/universal-behaviour.md` (copied from `NO-CODE-METHOD.md` → Method contract → Required of Claude; becomes canonical when `NO-CODE-METHOD.md` retires in V26). `CLAUDE-TEMPLATE.md`'s path block changed from markdown bullets to a fenced JSON code block so V19+ hooks can parse paths deterministically without grepping prose. Smoke-tested on Windows: `claude --plugin-dir <path>` loaded the plugin, `/hooks` showed `SessionStart` registered, Claude recited all eight rules verbatim when asked.

**Decisions taken and why.**

- **Plugin lives inside the same repo (`sovereign-implementer/plugin/`), not a separate repo.** The method docs and the plugin code will co-evolve through V27 — every change touches both. One history beats threading version tags across two repos. Going from one repo to two later is cheap; the reverse is expensive.
- **Hook script language is Python, not bash or Node.** Bash has the shell-profile contamination risk Opus flagged in V17 and needs Git Bash on Windows. Node isn't bundled with Claude Code on Windows (the native installer doesn't include it). Python is cross-platform, robust at parsing, and most readable for a non-coder debugging a hook.
- **Path block is JSON, not YAML.** Both parse from Python; JSON wins because it needs zero external dependencies (`json` is stdlib; `pyyaml` would be a plugin install dep), fails loudly on syntax errors, and has no quoting gotchas. Path block is edited rarely — reliability beats prettiness.

**Pivots and surprises.**

- **`UserPromptSubmit` hooks in plugins don't execute** — GitHub issue `anthropics/claude-code#10225`. V18 was scoped to install a `UserPromptSubmit` hook; we pivoted to `SessionStart` (works in plugins, functionally equivalent given the method's `/clear`-after-every-build discipline — every new session re-fires the hook). Saved to memory so V19+ doesn't re-discover.
- **`${CLAUDE_PLUGIN_ROOT}` doesn't quote paths with spaces.** The smoke test failed silently the first time because the expanded path (`C:\Users\Alex\Desktop\Taskflow Planning\...`) got truncated at the first space — Python tried to open `C:\Users\Alex\Desktop\Taskflow` and gave up. Fix: wrap the script path in escaped quotes in `hooks.json`. Any future hook command must follow this pattern; saved to memory.
- **Claude Code CLI wasn't installed on this machine.** Smoke testing required installing it from scratch via Anthropic's native PowerShell installer — adds about 30 minutes to a session but is overdue work (Claude Code CLI is Alex's stated Priority 1, not a V18 dependency in itself).
- **Two working-with-me rules added to the project CLAUDE.md mid-session**, both saved as feedback memories: (1) when uncertain about an external fact, ask Alex to web-search rather than guessing; (2) format web-search requests as paste-able prompts for Sonnet, not as questions to Alex.

**Carried forward.**

- V19+ hook commands all need the escaped-quote pattern from the start (carried as a memory + V19.md note).
- Crash course (V25) needs install instructions covering Python prerequisite, Claude Code CLI install, and the `where claude` diagnostic for the native+npm hook bug (saved to memory in V17 work).
- `BUILD-LOG.md` itself was added post-tag as a working-process improvement, not part of the V18 ship — a separate small commit after the V18 tag.

---

## V17 — 2026-05-11 — Plugin-migration architecture decided

**What shipped.** The migration path from "method as markdown docs" to "method as a Claude Code plugin" was scoped end-to-end. Produced `planning/INVENTORY.md` (final plugin component list — hooks, subagents, slash commands, bundled artefacts), `planning/PLAN.md` (session-by-session roadmap V18→V27), and `planning/claude-code-plugin-feasibility-response.md` (an Opus run grounding the design in actual Claude Code capabilities). Created `planning/sessions/V18.md` through `V27.md` as provisional session scopes. Switched versioning convention from numbered folders (`Version 3/` through `Version 16/` in `Archive/`) to git commits and tags (`v17`, `v18`, ...) — folders archived, going forward each session ships as one tagged commit.

**Decisions taken and why.**

- **Plugin layout = two-layer split.** Per-project source-of-truth content (`UX.md`, `BACKLOG.md`, `MANIFEST.md`, `CLAUDE.md`, additional SoT docs) stays per-project. The mechanical method itself (process, schemas, behaviour contract) becomes the plugin. This split is the whole bet of the migration: discipline becomes structural (hooks deny actions) rather than prompt-based (Claude is asked to behave).
- **Stop hook proposes, user gates** (D1). The build sequencer single-steps one batch per user prompt rather than auto-chaining batches. `stop_hook_active` naturally prevents loops; explicit user gating matches the method's existing `/clear`-after-build discipline.
- **Drift checks inlined into the planning subagent** (revision vs walkthrough). Subagents can't spawn other subagents — Opus confirmed. Drift logic moves from a would-be `drift-checker` subagent into the planning subagent's instructions.

**Pivots and surprises.**

- **The "always-loaded core skill" idea collapsed under Opus's check.** Skill bodies are progressive-disclosure by design — never always-loaded. Universal behavioural rules had to move to a hook (V17 chose `UserPromptSubmit`; V18 later pivoted to `SessionStart` after discovering a plugin bug).
- **Slash commands and skills merged in Claude Code v2.1.101.** Slash commands are now defined as skills with `disable-model-invocation: true` + `user-invocable: true` + `agent: <subagent>`. The roadmap depends on v2.1.101+ from V19 onwards.
- **V18 nearly became a research session.** Opus did the research live during V17, so V18 was promoted to the first real build session instead.

**Carried forward.**

- All plugin construction work — distributed across `V18.md` through `V27.md`.
- Risk of method instability during the migration: explicitly accepted at V17 close. The plugin's per-component context isolation is the testability fix, not a freeze of an unstable method.
