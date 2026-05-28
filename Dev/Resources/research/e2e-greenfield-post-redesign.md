# E2E greenfield post-redesign — 2026-05-25

First E2E test of the procedure-doc architecture (post-0079, post-0080) against a greenfield app ("Polite Fart Announcer" — single-page HTML soundboard).

## Test environment

- Plugin version: 0.67.0 (method V67, session tag v78).
- Architecture: procedure-doc-driven (no subagents). Phase-aware permissions (0080).
- Burner app: empty folder at `C:\Users\Alex\Desktop\Polite Fart Announcer`.
- Install method: local marketplace.

## Finding 1 — uninformed user bypasses /setup

**Severity: high.** The most common real-world case: a user installs the plugin, opens a new folder, and types their app idea with no knowledge of `/setup` or the method.

**What happened:**
- SessionStart hook fired correctly. Injected universal-behaviour rules via additionalContext.
- UserPromptSubmit hook fired correctly. Classified the prompt as a setup/initialisation request. Emitted: "Suggested route: recommend /setup. Wait for the user's okay before proceeding."
- Claude ignored the recommendation entirely. It read the universal-behaviour rules, understood a method existed, but decided to build the HTML app immediately instead of recommending `/setup`.
- PreToolUse hook blocked the file write (planning-phase source lock, V67).
- Claude routed around the enforcement by outputting raw code as a fenced block for the user to save manually.

**Root cause:** The UserPromptSubmit hint is advisory — "This is a hint, not a gate." Claude treated it as ignorable. The deny message from PreToolUse didn't mention `/setup` either (it talks about BACKLOG batches, which don't exist yet in an empty folder).

**Note:** First attempt placed the burner folder inside the no-code-method tree (`No code method\Polite Fart Announcer`). Claude Code's parent-directory CLAUDE.md inheritance poisoned the session — the parent `No code method\CLAUDE.md` made Claude think it was in the method dev project. Moved to Desktop and retried. This is not a plugin bug but a placement constraint worth documenting.

## Finding 2 — /setup works well when invoked directly

When the user explicitly ran `/setup`, the flow was clean:
- Four questions, delivered one at a time, with sensible suggestions.
- Correctly detected case 1 (empty folder).
- Scaffolded all expected files: CLAUDE.md, UX.md, BACKLOG/INDEX.md, BACKLOG/0001-core-soundboard.md, MANIFEST.md, TEST-LOG.md, build-log/INDEX.md, planning/drafts/, research/.
- Path block in CLAUDE.md correct. Footer V67 everywhere.
- Folded user answers into UX.md and seeded the first build batch.

**Scaffold issues (minor):**
- `[Project Name]` placeholder not replaced in CLAUDE.md header, MANIFEST.md header, build-log/INDEX.md header.
- UX.md captured only one of the four design principles the user agreed to ("elegant and posh" — dropped "dead simple," "works on mobile," "funny first and functional second").
- Batch file `0001-core-soundboard.md` missing `Status:` line (0069 feature).
- `marketplace.json` plugin description still mentions "subagents" (removed in 0079).

## Finding 3 — opaque build transition

**Severity: high.** When the user asked to build ("okay let's do the first build session"), the resulting sequence was confusing:

1. Claude tried to Write `index.html`. UI showed "Created index.html" (the attempted write).
2. PreToolUse hook blocked it (planning-phase source lock — no active batch).
3. Claude self-corrected: ran `/before-build` procedure, parsed BACKLOG, validated, set `Status: active`.
4. Before-build recap ended with: "Switch out of plan mode, then run `/build` to start this batch."
5. No `index.html` exists in the folder.

**UX problems for the user:**
- "Created index.html" appeared in the UI but the file doesn't exist. Looks like a silent failure.
- Claude's self-correction was unexplained — no plain-English narration of what happened or why.
- "Switch out of plan mode" is Claude Code jargon a non-coder won't understand.
- The user's mental model is "I asked you to build, you said you would, but nothing happened."

**Hooks fired correctly.** SessionStart, UserPromptSubmit, and PreToolUse all did their jobs. The gap is in how Claude communicates the workflow to the user after the hooks fire.

**Note:** The same result would occur if an uninformed user said "okay when are you going to build the app though" — the confusing sequence isn't caused by developer jargon in the prompt.

## Finding 4 — doc clutter at project root

User observation: UX.md, BACKLOG/, MANIFEST.md, TEST-LOG.md, build-log/ all sitting at the project root clutters the directory alongside the user's actual source files. Suggested: move method docs into a dedicated folder. This also opens the possibility of a folder-level CLAUDE.md for the method docs, separate from the project's root CLAUDE.md.

Impact: structural change to templates, path block defaults, hook path resolution, procedure docs, and the Reference manual. Large surface area but high UX value — the project root should feel like the user's project, not a method filing cabinet.

## Finding 5 — dev project hit by its own plugin

During this E2E session, the plugin's PreToolUse hook blocked research-file writes in the dev project. Root cause: Claude Code session opened at `No code method/` (parent of `sovereign-implementer/`), so the hook resolved `project_root` as `No code method/` instead of `sovereign-implementer/`. The `research/` exemption in `check_planning_phase_source_lock` checks for `project_root/research/`, which doesn't exist at the parent level. The `.no-code-method-skip` marker is inside `sovereign-implementer/`, invisible at the parent level.

Same parent-directory issue as Finding 1's first attempt. Not a consumer-facing bug, but confirms that the plugin assumes cwd = project root, which breaks for nested project layouts.

## Hook verification summary

| Hook | Fired | Correct behaviour | Notes |
|---|---|---|---|
| SessionStart | Yes | Yes | Injected universal-behaviour rules. |
| UserPromptSubmit | Yes | Yes | Classified setup request, recommended `/setup`. |
| PreToolUse (adoption gate) | Not tested | N/A | Folder was empty, so `is_unadopted_with_work()` returned False. |
| PreToolUse (planning-phase source lock) | Yes | Yes | Blocked `index.html` write during planning. |
| PreToolUse (batch file-list boundary) | Not tested | N/A | Never reached build phase with file writes. |
| PreToolUse (locked source-of-truth) | Not tested | N/A | Never reached build phase. |

## What wasn't tested

- Full build cycle (`/build` through `/sovclose`).
- Close recap, MANIFEST update, test-confirmation gate.
- Session-open status summary (0074) on re-entry.
- Token cost baseline for procedure-doc architecture.
- Phase flip from planning to build to close permission behaviour.

## Candidate scope files / OQ entries

1. **UserPromptSubmit enforcement for /setup** — the hint is too weak. Options: make the hint a gate (block the prompt until /setup runs), strengthen the prompt language, or have SessionStart inject a more forceful directive.
2. **Build-transition UX** — plain-English narration when hooks block, before-build recap language, "plan mode" jargon removal.
3. **Doc folder restructure** — move spine docs into a subfolder. Touches templates, path block defaults, hooks, procedure docs, Reference manual.
4. **Scaffold quality fixes** — [Project Name] replacement, UX principle capture, Status: line, marketplace.json description.

## V91 build-phase E2E — 2026-05-28

Second E2E test, completing the build lifecycle coverage from "What wasn't tested" above. Plugin version 0.91.0 (method V91, session tag v114). Same burner app, fresh `/sovsetup` scaffold.

### Test flow

`/sovsetup` (case 1) → `/sovplan` → `/sovrecap` → `/sovbuild` → `/sovclose` → `/sovgit`. Full transcript at `Dev/Planning/test-log/session-transcript.md`.

### Bug 1 — active-build.md creation blocked

`_METHOD_INFRA_DIRS` in `pre_tool_use.py` covers subdirectory names (`BUILD-PLAN`, `proxies`, `planning`) but not root-level files in `_method/`. `is_method_infra_file()` checks `parts[0]` against the set — for `active-build.md`, `parts[0]` is the filename itself, not a directory, so it fails. `check_batch_file_list()` does exempt the snapshot path but only runs during build phase — which can't be entered without the snapshot. Chicken-and-egg.

Workaround: fell back to pre-V90 `Status: active` directly in the per-batch BUILD-PLAN file. Fix: add root-file handling to `is_method_infra_file()`.

### Bug 2 — test-log/ and build-log/ writes blocked during close

Same root cause: `test-log` and `build-log` not in `_METHOD_INFRA_DIRS`. Compounded by Bug 3 — phase detection drops to "planning" after batch completion, so even if directories were exempt, the phase context is wrong.

Workaround: stored files in `_method/planning/drafts/` (which IS exempt via "planning"). Fix: add `"test-log"` and `"build-log"` to `_METHOD_INFRA_DIRS`.

### Bug 3 — Phase detection falls through after batch completion

When all files in the batch are ticked complete, the parser returns `{}` (no unticked batch). Phase detection drops to "planning" even with `Status: active` in the batch file. Affects close steps that need to write to method infrastructure directories.

Fix: `Status: active` should keep phase as "build" regardless of tick state. The close procedure manages its own transition.

### Observation — /sovrecap is Claude-facing

The recap content (batch scope summary, file list, test plan) is presented to the user but written for Claude's benefit — preparing Claude's context before building. Users see a wall of technical detail they didn't ask for. Options: (a) rewrite recap output to be user-facing ("here's what I'm about to build, does this look right?"), (b) fold recap silently into `/sovbuild` so the user never sees it, (c) keep it separate but add a brief user-facing summary.

### Observation — /compact nudge at invocation prompts

The most significant UX finding. A fresh session that invokes `/sovplan` starts cold — no project context, Claude asks "what brings you to planning?" even though the project is fully documented. A compacted session carries the full context forward seamlessly.

Every skill handoff message ("next, run `/sovrecap`") should include a `/compact` nudge. The invocation prompt is a natural pause point — the user is between skills, context is loaded, and compacting here preserves it for the next skill. Cost of the nudge is zero if skipped; benefit when followed is substantial.

### Observation — /sovsetup skill unavailability

Plugin was enabled and showed v0.91.0 with all skills listed on the plugin summary page, but `/sovsetup` wasn't available in an existing session. Required closing and opening a new session. Likely a Claude Code platform behavior — skills loaded at session start, not dynamically when plugins toggle.

### Observation — git commit message false positive

Bash write-guard parsed `"` characters in a non-heredoc commit message as file path boundaries. Workaround: use heredoc format (`cat <<'EOF'`). The 0115 heredoc-stripping fix covers heredoc content but not non-heredoc `-m` arguments. Minor — Claude should use heredoc format for commit messages anyway.

### Coverage update

Items from "What wasn't tested" (v78):

| Item | Status |
|---|---|
| Full build cycle (`/build` through `/sovclose`) | Tested. Three bugs found. |
| Close recap, MANIFEST update, test-confirmation gate | Tested. MANIFEST updated. Test-log written (workaround location). |
| Session-open status summary | Not tested (single-session lifecycle). |
| Token cost baseline for procedure-doc architecture | Not formally measured. |
| Phase flip from planning to build to close permission behaviour | Tested. Planning-to-build flip broken (Bug 1). Build-to-close flip broken (Bug 3). |
