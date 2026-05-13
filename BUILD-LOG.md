# Build log

A running record of decisions, changes, and reasoning. Newest first. Written for a friend skimming, not an auditor — half a page per session, less when possible.

For format details, see the project's `CLAUDE.md` → *Build log*.

---

## V19 — 2026-05-13 — PreToolUse hook + bundled templates + /init-project + Fold-ins pending section

**What shipped.** The plugin now blocks edits to locked source-of-truth docs and gives Claude an unambiguous place to record the proposed change instead. Concretely: a `PreToolUse` hook (`plugin/hooks/pre_tool_use.py`) intercepts `Edit`, `Write`, and `MultiEdit` against `UX.md` and any additional SoT doc declared in the project's `CLAUDE.md` path block; the hook returns a deny decision whose reason tells Claude to add a `[FOLD-IN PENDING]` block to the new *Fold-ins pending* section of `BACKLOG.md`. The hook is registered in `plugin/hooks/hooks.json` with a tool-name matcher (`Edit|Write|MultiEdit`). The 5 templates are now bundled inside the plugin at `plugin/templates/` (a copy of the repo-root `templates/`, both versions kept in sync via the session-close footer-bump rule). A new `/init-project` skill at `plugin/skills/init-project/` (frontmatter `disable-model-invocation: true`, `user-invocable: true`) coordinates a Python scaffold script that recursively scans `cwd` for any of the four destination filenames before writing, echoes the target path back to the user for confirmation, and refuses (pointing at `/migrate`) if any conflicts exist. The structural rewrites for fold-ins pending (`BACKLOG-TEMPLATE.md` ×2, `DOC-STRUCTURE.md` BACKLOG.md section, `NO-CODE-METHOD.md` Editing surfaces + Fold-in vocabulary entry + per-route mentions) brought the method docs into alignment with what the hook tells Claude to do. Smoke-tested on Windows in a scratch directory: plugin loaded, both hooks registered, `/init-project` scaffolded cleanly into an empty dir and refused on a non-empty one, the `PreToolUse` hook blocked an `Edit(UX.md)` attempt with the deny message visible, Claude pivoted to add the `[FOLD-IN PENDING]` block to `BACKLOG.md` as designed, and the `BACKLOG.md` edit proceeded unblocked.

**Decisions taken and why.**

- **Templates live at `plugin/templates/`, not nested inside `skills/init-project/`.** Originally drafted as `skills/init-project/templates/` (one consumer), revised mid-session after recognising the templates also serve `/migrate` (V24) as the reference structure to diff user-authored docs against. With multiple consumers, plugin-root placement is the right semantic home; `/migrate` would have read awkwardly out of an init-only path.
- **`/init-project` refuses on a non-empty target, doesn't merge.** The recursive scan checks for any of the four destination filenames anywhere under `cwd`. Cowork-first authoring is the expected path, so "user arrives with pre-drafted docs" is the *normal* case, not the exception — and that case belongs to `/migrate`, not `/init-project`. Half-scaffolding into an in-progress project would silently mix template-source and user-source content. Refusal is louder and safer.
- **Hook denies with a redirect message rather than silently rewriting the edit.** PreToolUse can technically rewrite an Edit's target via `updatedInput`, but doing so would silently transform `UX.md` writes into `BACKLOG.md` writes without Claude knowing — magical, brittle (the hook would have to synthesize a well-formed `[FOLD-IN PENDING]` block from the raw edit), and against the method's own "be told what's wrong, don't be silently rerouted" principle. The hard-block + reason-text path keeps Claude in the loop.
- **`[FOLD-IN PENDING]` gets its own top-level section in `BACKLOG.md`**, between Red flags and Planning batches. The pre-V19 model nested fold-ins inside the planning batch they originated from, but only the planning-batch-resolution route actually has a preceding batch — new-project, migration, and now the PreToolUse intercept all produced orphan blocks. Giving fold-ins their own section means the user has one clear "things waiting for me to fold in next Cowork session" location regardless of origin. The structural rewrite to `DOC-STRUCTURE.md` and `NO-CODE-METHOD.md` was bigger than the V19 scope said, but the alternative (shipping a hook whose deny message refers to a section that doesn't exist in the template) was a worse inconsistency.

**Pivots and surprises.**

- **`${CLAUDE_PLUGIN_ROOT}` does expand inside skill bodies.** Flagged as a real uncertainty in the V19 plan ("may differ from hooks"); smoke test resolved it on the first try — the `python "${CLAUDE_PLUGIN_ROOT}/skills/init-project/scripts/scaffold.py" check` command in the SKILL.md expanded to the full Windows path correctly.
- **The skill frontmatter shape works.** `disable-model-invocation: true` + `user-invocable: true` produced a working slash command at `/init-project` (visible in Claude Code's UI prefix as `/no-code-method:init-project`). No agent: key needed for skills that just run a script with no subagent.
- **V18's universal-behaviour rules visibly self-policed on the first hook test.** When asked to add a placeholder entry to `UX.md`, Claude refused before the PreToolUse hook even fired — citing the UX.md "no placeholder entries" rule and offering three alternatives. The hook is a backstop, not the only line of defence. We forced the hook test with an explicit "I'm stress-testing the hook, please attempt the edit anyway" instruction, which confirmed both layers work and that the universal rules are doing more soft work than the bare deny-and-redirect mechanism alone.
- **A Discovery surfaced mid-smoke-test.** Claude's first attempt at writing the fold-in block flagged that `BACKLOG-TEMPLATE.md` didn't have a designated section for `[FOLD-IN PENDING]` — Claude placed the block at the top of Planning batches and explicitly noted "this is my guess at the canonical location." That note is what made the structural rewrite (originally pushed to OPEN-QUESTIONS) part of V19's actual shipped work. Taking the user's "let's do it in v19 anyway" call on extending scope was the right move; closing the inconsistency now is cheaper than carrying it into V20+.
- **Hook permission gates appeared at every Python invocation.** First-run UX inside Claude Code's "approve commands" workflow: each `python ...` command (the `check` call, then the `write` call) triggered its own approval dialog. Bothersome on a 4-step skill but correct — broad blanket approval (`don't ask again for python *`) would have been over-permissive. Worth noting for the Crash course in V25.
- **Test scratch dir lived outside the mounted workspace.** Alex created `~/v19-scratch` on Windows; the smoke-test work happened in a Claude Code session pointing at that dir, but I couldn't delete it myself (path outside mounted workspace). Handed back a PowerShell `Remove-Item -Recurse -Force` one-liner. Trivia, but a confirmation that smoke-test directories don't need to live in mounted workspace folders to be usable — they only need to be visible to the user's own Claude Code session.

**Carried forward.**

- **Cross-version template reconciliation** raised as an `OPEN-QUESTIONS.md` entry — fold into V20 (tripwire in SessionStart) + V24 (worker in `/migrate`); entry removed when both folds are confirmed.
- **Step 8 (subfolder-conflict test on Windows) not pursued, reason:** the recursive scan was verified in the sandbox during V19 (`/tmp/scaffold_test2/docs/UX.md` was caught as `docs/UX.md` and the write refused with exit code 2). `pathlib`'s `rglob` and `name` matching are platform-agnostic, so Windows path separators aren't a different code path. Skipping the live Windows test saved usage with negligible information loss.
- **Note for V25 Crash course:** document the per-command Claude Code approval gate so first-time users know to expect dialogs at each Python invocation, not one approval for the whole `/init-project` flow.

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
