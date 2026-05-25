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

- Full build cycle (`/build` through after-build).
- After-build recap, MANIFEST update, test-confirmation gate.
- Session-open status summary (0074) on re-entry.
- Token cost baseline for procedure-doc architecture.
- Phase flip from planning to build to after-build permission behaviour.

## Candidate scope files / OQ entries

1. **UserPromptSubmit enforcement for /setup** — the hint is too weak. Options: make the hint a gate (block the prompt until /setup runs), strengthen the prompt language, or have SessionStart inject a more forceful directive.
2. **Build-transition UX** — plain-English narration when hooks block, before-build recap language, "plan mode" jargon removal.
3. **Doc folder restructure** — move spine docs into a subfolder. Touches templates, path block defaults, hooks, procedure docs, Reference manual.
4. **Scaffold quality fixes** — [Project Name] replacement, UX principle capture, Status: line, marketplace.json description.
