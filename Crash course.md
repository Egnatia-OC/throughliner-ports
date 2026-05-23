# Crash course

*A standalone primer for the no-code method as a Claude Code plugin.*

## What this is, and who it's for

A Claude Code plugin designed around the needs of non-coders using Claude Code, hereafter referred to as "the no coder," as distinct from "the user" who is the user of the no-coder's product. The plugin gives Claude a structured way to work on a project — phase-based (planning, before-build, build, after-build), backed by a small set of markdown files in the project that act as guardrails (preventing drift) and hold the design decisions, the next batch of work, and the test outcomes of every build that has shipped.

The plugin doesn't write code; Claude does. The plugin keeps Claude inside a deliberately rigid workflow: a new feature cannot enter a build batch directly (it must pass through planning first), build batches do not start until the previous batch's test outcomes are explicitly confirmed, some docs are locked from Claude's edit access entirely, and Claude is instructed to push back rather than quietly agree when something looks wrong.

Shaped for non-coders who already have a clear idea what their app should be. Extensive use of plan mode in Claude prior to first instantiation of the build sequence in Sovereign Implementer is highly recommended.


## Install, and a first session

Install via marketplace (persists across sessions):

1. Clone the repo: `git clone https://github.com/FlintCraftTech/sovereign-implementer.git`.
2. In Claude Code, run: `/plugin marketplace add <path-to-clone>` then `/plugin install no-code-method@sovereign-implementer`.
3. Open a Claude Code session in the project folder you want to work in. The plugin's hooks fire at session start. If the folder is empty, or contains existing work without the method's docs, Claude Code surfaces an advisory pointing at the `/setup` command (see *The safety net* below for what `/setup` does in each case).

For development or one-off use, `claude --plugin-dir <path-to-clone>/plugin` loads the plugin for a single session without installing.

**Desktop app users.** The `/plugin` command is only available in the Claude Code CLI — it does not work in the Claude Code desktop app (Windows or Mac). This is a Claude Code platform limitation ([#42142](https://github.com/anthropics/claude-code/issues/42142)), not specific to this plugin. Desktop app users must run the install commands in a CLI terminal first: open a terminal, run `claude`, and execute the `/plugin marketplace add` and `/plugin install` commands there. Once installed, the plugin loads automatically in desktop app sessions. See *Managing the plugin* below for disable, re-enable, and uninstall instructions.

A first session in Sovereign Implementer is distinct from a normal build sequence session:

- Open Claude Code in the project folder. Run `/setup`.
- `/setup` detects which case applies — empty folder, existing code without docs, existing code with non-method docs, already method-managed, or opted out — and runs the matching dialogue.
- For an empty folder, `/setup` scaffolds the spine docs (CLAUDE.md, UX.md, BACKLOG/ folder, build-log/ folder, MANIFEST.md, TEST-LOG.md) and creates `planning/drafts/` and `research/` folders, then walks four prompts in order: project context, UX principles, core functionalities, and a first build batch sketch.
- The dialogue's outputs land as `[PROPOSED EDIT PENDING]` blocks in the destination docs' own *Proposed edits pending* sections (e.g. UX.md's `## Proposed edits pending`). The no-coder applies the proposed edits to UX.md's main body by hand (the doc is read-only to Claude), and converts the first-build-batch sketch into a proper build batch with a `Serves UX.md:` line pointing at the entry it implements.
- After applying the proposed edits, the project is ready for its first build. Run `/before-build` to lock the next batch, then `/build` to execute it. The plugin orchestrates the rest.

## Managing the plugin

All plugin management commands use the Claude Code CLI. The `/plugin` command does not work in the desktop app ([#42142](https://github.com/anthropics/claude-code/issues/42142)). Desktop app users must open a terminal, run `claude`, and use the commands below. Changes made via CLI take effect in the desktop app on the next session.

### Disabling in a specific project

Once installed via marketplace, the plugin fires in every folder. To turn it off in a particular project without uninstalling:

Open a CLI session in that folder and run:

```
/plugin disable no-code-method@sovereign-implementer
```

Or use the interactive UI: type `/plugin`, go to the **Installed** tab, select the plugin, press Enter, and choose **Disable**.

Run `/reload-plugins` afterward for the change to take effect in the current session. The disable sticks for that project folder — the plugin stays active everywhere else.

### Re-enabling

Open a CLI session in the project folder and run:

```
/plugin enable no-code-method@sovereign-implementer
```

Or use the interactive UI: type `/plugin`, go to the **Installed** tab, expand the **Disabled plugins** section at the bottom, select the plugin, press Enter, and choose **Enable**. Run `/reload-plugins` afterward.

### Uninstalling

To remove the plugin entirely:

```
/plugin uninstall no-code-method@sovereign-implementer
```

Use the CLI command, not the `/plugin` UI's uninstall option — the UI uninstall has been reported as unreliable ([#52456](https://github.com/anthropics/claude-code/issues/52456)).

### For `--plugin-dir` sessions

The plugin is only loaded for that one session. Close the session and start a new one without the `--plugin-dir` flag. There is nothing to disable or uninstall.

### Known platform issues affecting plugin management

Two Claude Code bugs may affect plugin management as of May 2026:

- **Disabled plugins may still run hooks** ([#39307](https://github.com/anthropics/claude-code/issues/39307)). If you disable the plugin but its hooks still fire, uninstall it instead of disabling.
- **`enabledPlugins: false` in settings.json may be ignored** ([#28554](https://github.com/anthropics/claude-code/issues/28554)). Editing settings.json directly may not take effect. Use the `/plugin disable` command instead.

These are Claude Code platform issues, not specific to this plugin.


## Guardrail .md docs

Five markdown files and one folder sit in the project root once `/setup` has scaffolded the project, plus a `planning/drafts/` folder. Each does one job, and the workflow expects a clean separation between them.

- **CLAUDE.md** — entry point. Tells Claude Code where every other doc lives via a JSON path block, and carries any project-specific behavioural notes. Read by Claude at every session start.
- **UX.md** — user-facing description of the app. Every entry corresponds to something the no-coder can experience and test in the current build, plus a mandatory "the user needs this because…" line tying the entry back to a UX principle or other user context. Source of truth — Claude cannot edit this file; the no-coder maintains it by hand during planning sessions.
- **BACKLOG/** — deferred work, structured as a folder. `INDEX.md` inside the folder carries four fixed-order sections: Red flags (security/privacy/data integrity), Planning batches (open questions blocking a build batch), Build batches (a reference list ordering per-batch files), and Open questions (non-blocking parking-lot items worth tracking but not blocking any specific batch). Each build batch lives in its own file in the folder (e.g. `0001-add-today-screen.md`), carrying scope-context sections (Goal, Outputs, Success criteria, and conditionally Decisions/Dependencies/Red flags) written during planning, plus build-operations sections (Changes, Inputs, Files, Tests, Serves) populated during before-build. Reordering batches means moving lines in INDEX.md, not renaming files.
- **MANIFEST.md** — a flat alphabetical glossary of named codebase elements the no-coder might want to look up. Each entry pairs a name with the file path it lives at (in parentheses) and a one-line description. Maintained by Claude during builds; not read cover-to-cover. The path field anchors a read-before-edit gate in the PreToolUse hook — Claude must have the MANIFEST entry and the matching `UX.md` entry in view before editing a file that has a MANIFEST entry; see *What's inside the plugin* below.
- **TEST-LOG.md** — a row-per-test record of every shipped build batch's outcomes. Ten columns: # / Date / Session / Component / Test Description / Type / Verifier / Status / Confirmed Explicitly / Notes. When a batch ships, Claude appends rows, runs Claude-automatable tests (filling in results for Claude-verified rows), and leaves user-verified rows for the no-coder to confirm per-row during the next planning session. Rows are automatically pruned when their tested component is removed from MANIFEST.md — the planning subagent handles this at the start of each planning session, keeping the file bounded and drift checks fast.
- **build-log/** — a running record of decisions, changes, and reasoning for every build. One file per build (`NNN-batch-name.md`), plus an `INDEX.md` carrying a newest-first reference list. Written by Claude after each build completes. Not read cover-to-cover — search when you need the "why" behind a previous build's choices. Entry shape: What shipped / Decisions taken and why / Pivots and surprises / Carried forward / Performance. The Performance section carries structured mechanical measures (batch completion status, file count, carve-outs, test results) that are queryable across builds — grep for regressions, carve-out frequency, or test coverage patterns over time.

`/setup` also creates a `planning/drafts/` folder — a destination-agnostic holding area for substantive chat content not yet ready for a specific doc (comparison tables, structural sketches, option matrices). Drafts complement proposed-edits sections on source-of-truth docs (see *Editing surfaces* below), which are for source-of-truth doc content specifically. Drafts are written when content is "good enough to walk away from" and deleted when consumed.

`/setup` also creates a `research/` folder at the project root — a home for findings from any research Claude conducts during a session. When Claude investigates an external fact (a library's behaviour, an API's status, a platform capability), it saves findings to `research/<topic>.md` automatically and mentions briefly in chat what it found. Research files are reference material with zero maintenance burden: no MANIFEST tracking, no BACKLOG entries, no proposed-edit mechanism. They persist for future sessions and can be listed in a build batch's `Inputs:` line when a specific batch depends on what the research found.

A project can also declare additional source-of-truth docs. These get the same lock-from-Claude treatment as `UX.md`. Common examples: `SYSTEM-PROMPT.md` for a Claude/MCP integration project (describes what Claude receives at connection time); `COPY.md` for a project where user-facing text is the deliverable; `PATTERNS.md` or `CONVENTIONS.md` for coding conventions and architectural patterns Claude should follow consistently across builds; `API.md` for projects exposing an API. The project decides what it needs — these are suggestions, not a required set.

## The session shape

Work in this method moves through two main phases — planning and build — looping back and forth until the project is done. Each Claude Code session sits in one phase or the other; `/clear` or a new session separates them.

**Planning sessions** decide what gets built. The no-coder pastes test notes from a previous build (and/or raises new feature/s, asks a scope question, etc), and the planning subagent runs its routine: closing the previous build's test session by walking each pending TEST-LOG row one at a time; checking drift between UX.md, MANIFEST.md, and the codebase; scanning BACKLOG.md's Open questions section (listing every entry with a one-line summary so the user can promote, drop, or leave items as-is); sorting any new ideas into Suggestions (already in scope) and Discoveries (not yet in scope, need UX.md updates first); and editing BACKLOG.md directly. The conversation stays in the same chat style as ever — questions, push-back, alternatives, second thoughts all belong in there; the subagent's structure is for what gets recorded and where, not for how the conversation feels. Planning sessions are also when source-of-truth doc edits happen, by hand — the no-coder applies any pending proposed edits from each source-of-truth doc's own *Proposed edits pending* section, removes resolved planning batches, and reorganises build batches if priorities have shifted.

**Build sessions** ship engineering work, one batch at a time. By this point the batch already carries its scope-context sections (Goal, Outputs, Success criteria, and any Decisions/Dependencies/Red flags) from planning. The no-coder runs `/before-build` and the before-build subagent locks the batch's build-operations region: validates that the top batch's `Serves UX.md:` line resolves, populates the `Inputs:` line if the batch needs non-standard resources, enumerates the files the batch will modify into a `Files:` sub-section, writes a `Tests:` sub-section listing what to verify with each test's type and verifier (Claude or user), and proposes a split if the test list is long relative to scope. Once the no-coder okays the locked batch, `/build` runs the batch-executor subagent against the file list. The batch-executor reads any resources named in the `Inputs:` line before starting work. As each file ticks, the PreToolUse hook enforces that no file outside the list gets edited. When the last file ticks, the Stop hook routes to the after-build subagent, which updates MANIFEST.md, opens the test session by appending rows to TEST-LOG.md, runs Claude-automatable tests (filling in results for tests Claude can verify — command output, file contents, structural checks), generates a two-section build recap distinguishing "Claude has verified" from "please manually check", writes a build-log entry (the persistent per-build file in `build-log/`), runs a frame-correction sweep, and prompts the no-coder to commit/tag and then test.

The no-coder then `/clear`s, refreshes their copy of the project, and runs the user-verified tests the recap named. The outcomes (Pass / Fail / Skipped, plus notes) come back to the next planning session, which opens by reading the user-verified rows back row by row before any other work starts.

**Sessions are stateless; the docs are the memory.** When a new session opens, the plugin reads the project's docs — BACKLOG, MANIFEST, TEST-LOG, build-log — to figure out where things stand. Which batches are ticked, which test rows are unconfirmed, what the last build shipped. Nothing is carried from the previous session's in-memory state. This means a no-coder can close a session, open a fresh one, and pick up where they left off — the docs are the continuity, not the session.

The two-phase loop is the spine. Everything else is detail on what happens inside one phase or the other.

## The method absorbs mid-stream ideation

Non-coders absorb ideas mid-stream. A test reveals a missing feature; a conversation surfaces a risk; a friend's comment reshapes a priority. The method expects this — the planning phase exists precisely to catch mid-stream ideas and route them somewhere durable before they're forgotten or quietly acted on.

But catching an idea is only half the job. The other half is scoping it with enough structure that the no-coder knows what they're committing to before the build starts. A build batch that says only "add dark mode" gives no anchor for testing ("how do I know it worked?"), no record of what the batch is for ("why are we doing this?"), and no surface for Claude to push back against ("is this the right scope?"). The result is a build that drifts, a test session that tests the wrong things, and a no-coder who can't tell whether what shipped matches what they asked for.

The method's response is to give every build batch the same scoping structure that a careful planning conversation would produce — a Goal stating why the batch exists, Outputs describing what changes the user will experience, Success criteria naming the observable conditions for "done," and (where relevant) the unresolved decisions, dependencies, and security concerns the batch carries. These sections are written during planning, not during the build — the no-coder speaks the substance aloud in conversation, and the planning subagent records it into the batch. By the time the build starts, the batch carries its own context. The no-coder doesn't have to remember why they asked for this three sessions ago; the batch says so.

## Anatomy of a batch

A build batch lives in its own file inside the BACKLOG/ folder (e.g. `BACKLOG/0001-add-today-screen.md`). Each file has two regions: **scope context** at the top (the strategic frame) and **build operations** below (the tactical execution surface).

**Scope context** — written by the planning subagent when the batch is created:

- **Goal.** One paragraph: why does this batch exist, and what will be different when it ships.
- **Outputs.** Prose describing what changes the user will experience.
- **Success criteria.** Observable, testable conditions for knowing the batch succeeded.
- **Decisions to make this batch.** Unresolved scope questions within the batch — things to decide during the build. Omitted if all decisions are already made.
- **Dependencies.** What the batch needs from outside itself — another batch shipped first, a planning batch resolved, an external resource available. Omitted if none.
- **Red flags.** Security, privacy, or data-integrity concerns specific to this batch's scope. Not always present — the planning subagent writes this section only when it detects the batch touches a security-shaped surface (auth, secrets, PII, deletion, payment). When absent, the batch has no flagged security concerns.

**Build operations** — populated by the before-build subagent during batch lock-in:

- **Changes:** The list of concrete changes, each labeled `[Requested]` (the no-coder asked) or `[Suggested]` (Claude proposed).
- **Inputs:** (optional) Non-standard resources the batch needs beyond the default docs.
- **Files:** The file-by-file task list — `- [ ]` per file, ticked as each is completed.
- **Tests:** (optional) What to verify once built, with each test's type and verifier (Claude or user).
- **Serves UX.md:** Which UX.md entry the batch implements.

The `Changes:` line is a structural delimiter — it separates the scope-context sections (which may contain their own lists and paragraphs) from the change list (which the parser needs to extract cleanly for the build recap). Everything above it is "why and what"; everything below it is "how."

## Walkthrough — Taskflow Day 1

This walkthrough follows a small project — a task manager called **Taskflow**, designed for users with executive dysfunction — through new-project setup, first planning, first build, and the first test note. The point is to make the method's discipline feel concrete.

### Day one — starting from scratch

The no-coder opens a Claude Code session in an empty project folder and runs `/setup`. Empty folder means no advisory — `/setup` detects the empty case and walks four prompts:

1. **Project context.** What the app does, and what makes it distinct.
2. **UX principles.** Three to six. For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*. Each gets a one-line claim plus a few sentences of reasoning.
3. **Core functionalities — first pass.** Three to five features that make this app what it is. Each gets a paragraph plus the *user needs this because…* line.
4. **First build batch sketch.** The smallest end-to-end thing that can be built and tested.

These are the decisions the rest of the project is built on. Claude queues the answers as `[PROPOSED EDIT PENDING]` blocks in the destination docs' own *Proposed edits pending* sections (e.g. UX.md's `## Proposed edits pending`). The no-coder applies the proposed edits to UX.md's main body by hand during the same planning session, and converts the first-build-batch sketch into a proper build batch with a `Serves UX.md:` line.

Once the docs are seeded, Claude Code is ready for the first build.

### A first UX entry — Risk accepted in action

One of Taskflow's first functionalities is **One-day-at-a-time view**: the Today screen shows only today's tasks. No week view, no agenda. The entry's *user needs this because…* line ties straight back to *Reduce planning pressure*:

> Looking ahead at a wall of upcoming tasks is the planning-pressure that triggers shutdown for users with executive dysfunction. Seeing only today's load keeps the cognitive surface area small and the bar for getting started low.

The entry ends with a **Risk accepted** line:

> Future days' task load isn't visible in Taskflow until each day arrives — time-bound commitments still surface through calendar integration. We've judged this an acceptable cost: looking at a wall of upcoming tasks is itself the pressure that triggers shutdown for the users this app is for; protecting the present matters more than enabling forward task-planning.

The *Risk accepted* line is for the future-self who, six months in, wonders why the app deliberately omits a week view. The trade-off is on the page; it does not have to be re-derived.

### First build, first test note

The first build batch ships — an empty Today screen, a way to add a task. The no-coder `/clear`s, refreshes, tests, and writes notes:

> *"Added a task fine. Couldn't find anywhere to set a due date — is that intentional? The screen is hard to read at night — dark mode would help."*

The notes get pasted into a new Claude Code session. Claude takes the test-notes route into planning.

### How a test note becomes a feature — the five-step pipeline

Take the dark-mode item:

1. **Idea raised.** Test note → dark-mode request.
2. **Planning batch.** Claude adds a planning batch in BACKLOG.md named *Dark mode* with the questions to answer: *Is this app used at night frequently enough to justify maintaining a parallel theme? Follow OS setting or have its own toggle? Which existing UX entries assume light-background contrast and would need revisiting?* The batch closes with `Blocks: scope decision — no build batch yet.`
3. **Planning session.** The no-coder and Claude answer the questions. Suppose: yes, follow OS setting, two existing UX entries need a contrast pass.
4. **UX.md updated.** A new *Dark mode* entry is added with the *user needs this because…* line. The two affected entries get a quick revisit.
5. **Build batch.** A build batch enters BACKLOG.md with scope-context sections (Goal: "add OS-following dark mode"; Outputs: "the app follows the OS light/dark setting"; Success criteria: "switching OS theme switches app theme") and a `Serves UX.md: Dark mode` line.

If step 3 had answered "no," steps 4 and 5 would not happen. UX.md stays as it was, the planning batch is removed as resolved, no build batch is ever created. That short-circuit case is just as valid an outcome as "yes, build it."

The due-date item runs the same pipeline. It might land at "yes, with relative shortcuts only, no date picker" — folding into a new UX.md entry once decided, then a build batch.

**What if the idea conflicts with an existing UX principle?** If a test note or feature request would violate a principle already in UX.md, that conflict gets surfaced in chat as the first response — not quietly routed into a planning batch and hoped for. The planning batch still happens (step 2), and the conflict becomes one of its questions. Chat surfaces the tension immediately; the planning batch records and resolves it.

### Drift checks at planning sessions

By the third or fourth build, drift checks run at the start of every planning session. Five checks — one file-level temporal check, three pairwise comparisons, and one per-row code-touch judgement:

- **Direct-edit detection (git-diff against last build).** Catches manual edits to files outside the build cycle — a function modified by hand inside a tracked file, a new file added without going through a build batch. Claude diffs the working tree against the most recent tag (or against `HEAD` if the project doesn't tag) and walks each flagged file with the no-coder: *"Was this you?"* per file. Confirmed user edits get accepted, checked against upcoming build batches for conflicts, and queued as `[PROPOSED EDIT PENDING]` blocks in UX.md's own *Proposed edits pending* section if they imply a UX.md update. Unconfirmed changes pause the planning session for investigation. Files in the last batch's `Files:` list and the method's writable docs (MANIFEST/BACKLOG/TEST-LOG/build-log/CLAUDE) pass through silently — only unexpected edits surface.
- **UX.md ↔ what's actually built.** UX.md describes a "drag to reorder" gesture, but the build only supports tap-and-arrows — flag the entry as describing a non-existent feature. Or the build has a swipe-to-archive behaviour no UX.md entry covers — that is a Discovery.
- **MANIFEST.md ↔ the codebase.** MANIFEST.md still says `TaskCard`, but the last build renamed it `TaskTile` — update the entry. A new service was added with no MANIFEST.md entry — add one.
- **MANIFEST.md ↔ UX.md (loose check).** MANIFEST.md lists a `WeeklyDigestEmailer`, but no UX.md entry mentions email digests — either there is a hidden feature (Discovery) or it is dead code (delete). Database config and logging middleware are exempt; they do not trace to user-facing intent by design.
- **TEST-LOG.md ↔ what has been touched (Rule 5 — retest after change).** For each TEST-LOG row with `Status: Pass` and `Confirmed Explicitly: Yes`, judge whether the component it tested has been substantially changed since the row's Date. A row from v23 testing a touch handler whose code was edited in v26 — flag for retest. Trivial changes (comments, formatting, unrelated refactors in the same file) do not count. Produce a brief reasoning trail per flagged row so the call is auditable.

The drift check is not exhaustive. It catches cases where docs and code have started disagreeing, before that gap turns into a wrong-feature build.

## The four disciplines that do most of the work

**The "the user needs this because…" line.** Required for every UX.md entry. Forces rationale articulation before implementation. Protects against feature drift. Makes scope decisions easier.

**The flag taxonomy.** Three buckets with three different homes. *Red flags* (security, privacy, data integrity, safety) go into BACKLOG.md and stay until addressed. *Suggestions* (improvements that fit current scope) go in chat at end of response. *Discoveries* (out-of-scope ideas) become planning batches in BACKLOG.md before session end. Every concern has exactly one place to live.

**The pipeline for new features.** A new feature cannot enter a build batch directly. It must enter as a planning batch in BACKLOG.md, get answered in a planning session, become or update a UX.md entry, and only then enter as a build batch. Rigid by design. Claude proposing a build batch with no matching UX.md entry is itself a flag that something has been skipped.

**The test-confirmation gate.** A new build batch cannot start while any row in TEST-LOG.md from the previous batch is unconfirmed. Confirmation happens per-row, by name, in the planning session after the test session was opened by the after-build subagent — bulk confirmations do not count. Five protocol rules make this concrete: never infer completion, resolve "all others good" before recording, no new build until the test session is closed, Skipped is not Passed, retest after change. Two hooks make it load-bearing: a PreToolUse hook denies any `Task` invocation of batch-executor while pending rows exist, and the SessionStart hook injects a routing override that steers any session opening with pending rows straight to the planning subagent's read-back, regardless of what the no-coder asks. The subagent walks the no-coder through; the record stays trustworthy because no row gets a positive outcome by accident or drift.

## Four test types and the Claude/user split

The method recognises four test types, covering both UI and non-UI projects:

- **Look and click** — open an app or interface, interact, observe behaviour. The classic UI test. Structural checks within this type (element exists, text matches, navigation works) can be verified by Claude; judgement and visual-nuance checks (does this feel right, is this the layout I want) stay with the user.
- **Run and read** — execute a command, read the output. CLI tools, scripts, data pipelines. Fully automatable by Claude.
- **Trigger and observe** — set up conditions, trigger an event, verify the system responded. Plugins, hooks, webhooks, scheduled tasks. Fully automatable by Claude.
- **Generate and inspect** — run a process that produces a file, verify its contents. Reports, exports, generated documents. Fully automatable by Claude.

The verifier for each test row is decided during before-build (in the `Tests:` sub-section) and recorded in TEST-LOG.md's `Verifier` column. The split is by *what's being checked*, not by type: structural/factual checks go to Claude, judgement/taste checks go to the user. A single batch can have both Claude-verified and user-verified rows across any test type.

After the build, the after-build subagent runs every Claude-verified test, fills in the result, and reports it in the recap under "Claude has verified." User-verified tests appear under "please manually check." The test-confirmation gate requires ALL rows — both Claude-verified and user-verified — to reach `Confirmed Explicitly: Yes` before the next build can start. Claude-verified rows reach Yes during after-build; user-verified rows reach Yes during the planning read-back.

## The safety net — installing on a folder that isn't empty

The method assumes a fresh project. Sooner or later someone installs the plugin into a folder that is not fresh — by mistake, or to bring an existing project under the method's discipline. The safety net is the plugin's response.

When a session opens, **SessionStart** checks whether the folder is *adopted* (carries the method footer in CLAUDE.md) or *unadopted*. Adopted folders and genuinely empty folders stay silent. An unadopted folder with substantial existing work — code, foreign docs, anything — triggers an advisory pointing at the `/setup` command and explaining how to disable the plugin if the user doesn't want it here.

Until `/setup` runs, **PreToolUse** denies Edit, Write, MultiEdit, and method-subagent calls from main Claude. Not just a warning — an actual block. `/setup`'s own scaffolding calls pass through, so adoption can happen while the gate is closed against everything else.

`/setup` branches on what it finds:

- *Empty folder* → walks the four new-project prompts and scaffolds the spine docs with the no-coder's answers applied.
- *Existing code, no docs* → offers to scaffold fresh docs alongside, or cancel.
- *Existing code, foreign docs* (most commonly: Claude Code's built-in `/init` ran first) → offers to **migrate** the existing CLAUDE.md to method spec (preserving content — Claude proposes edits and iterates with the no-coder until the migration plan is right; anything that does not fit cleanly lands as `[PROPOSED EDIT PENDING]` blocks so nothing is lost), **overwrite** the existing CLAUDE.md after backing it up, or **leave alone**.
- *Already method-managed* → detects template state, surfaces any version mismatch, offers a **refresh** (bumps method-version footers across writable docs directly; locked docs get `[PROPOSED EDIT PENDING]` entries for the no-coder to bump by hand; project-specific content in CLAUDE.md stays intact) or **cancel**.

Users who don't want the method in a particular folder don't need to go through `/setup` at all — they can disable the plugin for that project (see *Managing the plugin* above).

Nothing destructive happens without explicit confirmation, and every destructive option backs up first.

Why session-start, not install-time? Claude Code's plugin system has no install-time hook the plugin can run code from. The earliest the plugin can act is when a Claude Code session opens in a folder. By the time the no-coder could ask Claude to write a file, the gate has already fired.

## What's inside the plugin

The plugin distributes the method's rules across Claude Code primitives — hooks, subagents, skills, and bundled docs — rather than asking Claude to enforce them from a single long prompt. Non-coders do not normally open these files; the plugin runtime does the work.

- **Hooks** are Python scripts that fire on specific Claude Code events. The SessionStart hook detects what shape of folder the no-coder is working in (adopted, unadopted-with-work, empty, opted-out) and injects an advisory or the universal behavioural rules into Claude's session context. The PreToolUse hook enforces edit boundaries — blocking edits to files outside the project root (so a session in one project can't modify another project's files), locking UX.md and additional source-of-truth docs from Claude, blocking edits outside the current batch's `Files:` list, gating new build batches on the previous batch's test outcomes being confirmed, refusing build batches whose `Serves <DOC>:` line names entries that do not exist in the referenced doc (UX.md entries matched against `### Functionalities` headings; additional source-of-truth docs matched against `##` headings, excluding structural sections; writable docs like MANIFEST.md are not validated), denying the first edit on a MANIFEST-covered file with the matching MANIFEST entry and UX.md's Functionalities headings inlined in the deny reason (Claude retries with the context in hand — the hook scans the transcript for the prior deny and allows the retry), and blocking destructive git commands (`git reset --hard`, `git push --force`) with deny messages pointing at safer alternatives. The PostToolUse hook validates BACKLOG.md's format after every edit — if the edit broke the parser's expected structure, Claude sees an immediate warning naming common causes so it can fix the formatting before continuing (without this, a format error stays invisible until the Stop hook or `/build` tries to parse BACKLOG.md several turns later). The Stop hook routes one build batch to the next, or routes to the after-build subagent when a batch finishes. The PreCompact hook blocks context compaction when a build batch is in progress — long sessions cost more tokens and Claude's adherence to the method degrades as context grows, so the hook recommends the user ask Claude to prepare a handoff before starting a fresh session rather than allowing lossy compression mid-build. The UserPromptSubmit hook classifies the user's first prompt of each session (test notes, setup request, or resume) and injects a routing hint so Claude starts with a structural classification rather than deriving it from the routing table alone — it's a hint, not a gate, and no-ops on subsequent prompts.
- **Subagents** handle the phase work in their own Claude Code contexts: planning, before-build, batch-executor, after-build, and setup. Each runs its own conversation, then returns a recap that main Claude relays to the no-coder. The context isolation keeps each phase's prompts focused. The after-build subagent runs Claude-automatable tests during its pass — command-output checks, file-content verification, structural DOM checks — and fills in their results before prompting the user for the remaining taste/judgement tests.
- **Slash commands** (`/setup`, `/before-build`, `/build`) are the user-facing entry points. Each invokes the matching subagent.
- **Templates** — the starter shapes for the six spine docs that `/setup` scaffolds into a new project. These get copied into the project root with method-version footers and start mostly empty.
- **Bundled reference docs** — `DOC-STRUCTURE.md` and `VOCABULARY.md` live inside the plugin at `plugin/docs/`. The subagents read them when needed via `${CLAUDE_PLUGIN_ROOT}/docs/...`. Non-coders do not normally open these directly; the *When you need more* section at the end of this doc says when reaching for them is worthwhile.

The split between hooks (deterministic enforcement) and subagents (probabilistic behaviour) is deliberate: hooks bite when correctness matters and a prompt-based instruction might be ignored; subagents handle the work that needs judgment.

## Two layers of permission

Claude Code has its own permission modes — Ask permissions, Accept edits, Plan mode, Auto, and the `--dangerously-skip-permissions` bypass. These control whether Claude Code prompts the no-coder before a tool call goes through. They are Claude Code's own mechanism, independent of any plugin.

The no-code method plugin adds a second layer on top. Its PreToolUse hooks evaluate every Edit, Write, MultiEdit, Task, and Bash tool call against method rules — project-boundary enforcement, locked-doc enforcement, batch file-list boundaries, the test-confirmation gate, the adoption gate, the read-before-edit gate, the Serves-line check, and the destructive-git guard. When a hook denies, the tool call is blocked regardless of Claude Code's permission mode. Setting Claude Code to Auto or Bypass does not override a method deny.

The two layers are complementary, not overlapping:

- **Claude Code's permission modes** decide whether the no-coder gets prompted before Claude acts. They affect the user-prompting step, not the plugin's hook evaluation.
- **The plugin's hooks** decide whether Claude is allowed to act at all. They fire in every permission mode, including Bypass.

Every deny message from the plugin's hooks is prefixed `[No-code method]` and ends with a `What to do:` line naming the specific action to take instead. In permissive modes (Accept edits, Auto, Bypass), an additional line clarifies that changing the permission mode won't help — so the no-coder doesn't waste time escalating through modes looking for one that works.

### Which mode for which phase

The method's "planning session" is not the same as Claude Code's "plan mode." Plan mode blocks all file edits; the planning phase needs to edit BACKLOG.md. Here's which mode to use when:

| Phase | Recommended mode | Why |
|---|---|---|
| Planning | Accept edits | The planning subagent edits BACKLOG.md and writes proposed-edit blocks. Plan mode would block those. |
| Before-build | Accept edits | Writes the Files: sub-section into BACKLOG.md. |
| Build | Accept edits (or Auto) | Source-file edits. The plugin's hooks enforce batch boundaries regardless of mode. |
| After-build | Accept edits (or Auto) | Writes to MANIFEST.md, TEST-LOG.md, build-log/. |
| Pre-method ideation | Plan mode | Exploring the app idea before running `/setup` — no file edits needed yet. |
| Reviewing a locked batch | Plan mode (optional) | Reading the batch before `/build` — useful for a read-only review pass. |

Auto is viable during builds because the plugin's PreToolUse hooks enforce the same boundaries that Accept edits prompts the no-coder about — locked docs, batch file lists, the test-confirmation gate. The hooks fire in every mode, including Auto.

## What's editable

The method ships with a default set of preferences and commitments. A new no-coder needs to distinguish three layers.

**Method contract — load-bearing, edit at peril.** Some lines read like personal preferences but the method's machinery depends on them. "Push back rather than simply agreeing" — the drift checks, red-flag surfacing, and planning recaps all assume Claude will push back. "Do not stealth-fix regressions" — the build recap assumes Claude states regressions plainly. "Walkthroughs one step at a time; alternatives all at once" — multi-step procedures lose usability when bundled; alternative-presentation loses comparison context when sequenced. These are structured as *Required of Claude* (positive lines) and *Prohibited of Claude* (negative lines — "do not add features not listed in the current batch prompt," "do not refactor without explicit confirmation"), each annotated with the mechanism that breaks without it.

**Recommended habits — edit freely.** Some lines are habits surrounding the build sequence: `/clear` after each build, prepare test results as pasteable text, review all upcoming changes before each build, tag and push after every shipped build batch. A different no-coder with a different rhythm might rewrite these.

**The build sequence — fixed.** The four-phase cycle (session start → planning → before build → after build) is the method's spine. Not part of the editable surface.

Each layer has its own section in `NO-CODE-METHOD.md` inside the plugin.

### Editing surfaces — what Claude can write

Some docs are stable artefacts written slowly and deliberately. UX.md and any additional source-of-truth docs are written during planning sessions by hand; Claude (the agent) cannot edit them, enforced by the PreToolUse hook. Build sessions are short, `/clear`-bounded, build-focused — the wrong environment for stable docs to drift via small "clarifying" tidy-ups. So those docs are locked from Claude. When Claude thinks one should be reworded, it surfaces the suggestion in chat rather than editing.

| Doc | Claude (the agent) edit access |
|---|---|
| `UX.md` | **read-only** (no-coder edits by hand during planning) |
| Additional source-of-truth docs (`SYSTEM-PROMPT.md`, `COPY.md`, etc.) | **read-only** (no-coder edits by hand during planning) |
| `BACKLOG.md` | read/write |
| `MANIFEST.md` | read/write |
| `TEST-LOG.md` | read/write |
| `CLAUDE.md` | read/write |
| `NO-CODE-METHOD.md` | read (method spec inside plugin) |
| `DOC-STRUCTURE.md` | read (method spec inside plugin) |

`BACKLOG.md` is read/write because builds need it. The protective rule is built into the build sequence: Claude must discuss every `BACKLOG.md` change with the no-coder at the appropriate stage — never silently.

**One exception: method-version footer stamps.** The `*No-code method — Version N.*` footer on each doc is metadata, not content. The PreToolUse hook allows footer-only edits on locked docs, so `/setup`'s version refresh can stamp all footers directly without routing through proposed-edit blocks.

**The `[PROPOSED EDIT PENDING]` mechanism.** Claude cannot write directly into read-only source-of-truth docs like `UX.md`. Instead, proposed content is queued as a `[PROPOSED EDIT PENDING]` block in the destination doc's own `## Proposed edits pending` section (the last section before the method-version footer). The PreToolUse hook allows edits within this section while keeping the rest of the doc locked. The block names the proposed change, its origin, and whether it replaces an existing section or adds a new one.

During planning sessions and `/setup`, a **preview-then-apply convention** applies: before writing the proposed-edit block, Claude shows the complete proposed section in chat (heading, content, formatting, and all) and waits for the no-coder's approval. On approval, Claude writes the proposed-edit block to the destination doc's proposed-edits section and prompts the no-coder to apply it now — naming the section heading to find and replace. The edit is applied in the same session rather than being deferred. Mid-build edit attempts intercepted by the hook still produce a standard `[PROPOSED EDIT PENDING]` block deferred to the next planning session.

## Why the rules

The method's rules are not arbitrary; each one defends something. Some of the defences are not obvious from the rule alone, so they live here in prose.

**Why Claude is asked to push back rather than agree.** A planning recap that mirrors whatever the no-coder last said is only useful if Claude has engaged with disagreement before recording the outcome. Capitulating without engagement and refusing to listen are mirror failures: both bypass the conversation that would decide whether a suggestion was right. The drift checks, red-flag surfacing, and planning recaps all assume Claude pushes back when something looks wrong — if Claude defaults to agreement, the safety nets stop functioning.

**Why regressions get stated plainly, not stealth-fixed.** The build recap is the no-coder's primary record of what happened in a build session, used to decide whether to test, push back, or accept. A stealth-fix breaks that record — the regression survives invisibly until it resurfaces later with no breadcrumbs back to its origin. Plain statements keep the recap a reliable trail.

**Why batch scope is locked once agreed.** Mid-build scope additions cost three things the method protects. Predictability of session length — a batch with a fixed file list has a knowable end; one that absorbs "while we're here" additions does not. Clean test coverage — one batch is one set of changes is one set of tests; mid-build mixing makes regressions harder to trace. The planning-gate filter — mid-build, things feel in-scope that would not survive a planning conversation. The rule defers scope decisions back to planning rather than shortcutting them. The two named carve-outs (prerequisite and re-batching) are escape valves the discipline anticipates, not invitations to bend the rule.

**Why drift checks operate at five different abstraction levels.** The five checks — direct-edit detection, UX.md ↔ build, MANIFEST.md ↔ code, MANIFEST.md ↔ UX.md, TEST-LOG.md ↔ what has been touched — operate at different abstraction levels (file-level temporal, feature-to-feature, name-to-name, loose user-facing-purpose, per-row code-touch with reasoning trail). Doing them at once mixes the levels and produces noise. Running them as five separate passes lets each catch the gap it is designed for; in particular, direct-edit detection runs first because its output (a list of files touched since the last build) feeds the MANIFEST ↔ codebase and TEST-LOG ↔ touched-since-recorded checks downstream.

**Why source-of-truth docs are locked from Claude.** UX.md and additional source-of-truth docs are written slowly, in planning sessions, with the time those decisions deserve. Build sessions are short and build-focused — the wrong environment for stable docs to drift via small "clarifying" tidy-ups. Locking those docs from Claude means design changes can only happen where they get proper deliberation.

**Why source-of-truth docs cannot carry placeholders or soft gestures at undecidedness.** Source-of-truth docs are operational. Runtime audiences (Claude, the no-coder's future self, anyone reading to remember what was decided) need the instruction, not its status. A line that says "currently undecided" forces the reader elsewhere for the actual rule and makes the doc inert until that elsewhere is found. The status of an open question lives in BACKLOG.md, not in the body of a source-of-truth doc.

**Why UX principles are project-specific.** A budgeting app's principles ("never let the user lose data they have entered") look nothing like a task manager's ("reduce planning pressure"). Principles that try to be method-wide become so abstract they stop guarding any actual decision. The job is to write the three-to-six principles that protect *this* project's design from drift, not to compile a general theory of UX.

**Why MANIFEST.md starts flat instead of pre-sectioned.** "Switch to alphabetical sections by area when the flat list grows too long" sounds like permission to start with sections from day one. It is not. Most projects' MANIFEST.md never grows large enough to need sections, and pre-emptive sectioning forces architecture decisions (which "areas" exist?) before there is enough code to know. Wait until scrolling the flat list actually hurts.

**Why BACKLOG is a folder, not four separate files by section type.** Red flags, planning batches, build batches, and open questions could live in four separate files by type. They do not — INDEX.md carries all four sections in one file so there is exactly one place to look for what is outstanding. Build batches get their own per-batch files because batches accumulate content (scope context, file lists, test plans) that would bloat the index. The index carries the build order as a reference list; each per-batch file carries its own content. The split is content-volume, not category — the four-section structure and top-to-bottom ordering are preserved in INDEX.md.

**Why Risk accepted is its own labelled line.** Without an explicit *Risk accepted* line, the cost of a deliberate simplification fades from view. Six months later, someone (often the same person who chose the simplification) wonders why the app deliberately omits a feature and considers adding it — without remembering why it was omitted. The Risk-accepted line keeps the trade-off on the page so any re-litigation happens with the original reasoning in view.

**Why a test session must be closed by per-row read-back before the next build can start.** Bulk confirmations ("all the others passed") would silently flip dozens of TEST-LOG rows to confirmed when only a few were actually verified. A single per-row read-back — Claude reads the test description, the no-coder names the outcome — is the only way to keep the record honest. Without that, TEST-LOG.md becomes intentions-as-data rather than decided outcomes. Claude-verified rows skip the read-back because Claude filled in the result during after-build with concrete evidence (command output, structural check result); user-verified rows go through the read-back because only the user can judge taste and visual nuance.

## What this costs

A new feature takes two sessions to land — one planning, one build — at minimum. The pipeline is rigid by design. What the discipline buys: every shipped feature traces to a written user-need rationale; nothing gets built that no one decided to build; and at any moment "why is this here?" has an answer on a page that can be opened.

## Where the method sits in the broader landscape

The method belongs to the spec-driven development family. Closest neighbour: Cline's Memory Bank — same shape (markdown files as project memory and behavioural guardrails, read at session start), different cut of files, different audience. Memory Bank's cut: `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`. This method's cut: UX.md, MANIFEST.md, BACKLOG.md, TEST-LOG.md, plus additional source-of-truth docs as needed. Different cuts of the same idea. Memory Bank is general-purpose; this method is shaped around non-coders.

In the broader spec-driven-development literature (the arXiv paper, the GitHub Spec Kit, the Augment Code guides, the DeepLearning.AI course), this method maps onto the **spec-anchored** rigour level: specs are high-quality context that drive code generation, but code remains the source of truth.

## Caveats

Iteratively developed. Has not yet been used to ship an app. The first real Taskflow build under the current version is the next test — and the most honest one.

A known headwind for any methodology relying on `CLAUDE.md`-style instructions: roughly 30% of the time, Claude will not follow them. The method designs around this by making source-of-truth docs read-only to Claude (so big design changes cannot slip in mid-build) and by making most non-trivial decisions reviewable in chat. But the headwind is real, and any no-coder should expect to recognise drift and recover from it as part of the skill.

Claude will sometimes pause mid-session to research an external fact — checking a library's status, verifying an API's behaviour, confirming how a platform feature works. When it does, it saves findings to `research/<topic>.md` in the project's `research/` folder and mentions briefly what it found. This is a method discipline: it's how the method prevents wrong external facts from getting baked into source-of-truth docs and scope files. If research tools aren't available in the session, Claude marks the uncertain claim with `[UNVERIFIED]` and proceeds conservatively.

Claude Code's built-in **plan panel** (the Shift+Tab plan-mode surface) does not show the method's build sequence. The panel is Claude-Code-internal — populated only by Claude itself via its native plan-mode flow, with no plugin-facing write surface to inject the method's current and queued build batches. Where the real sequence lives is `BACKLOG.md` → Build batches; the top batch is what's next. If the plan panel reads empty mid-build, that is not the plugin losing track of where it is — that is the panel showing what it can show. Open the project's `BACKLOG.md` to see the actual queue.

## When you need more

This document is the primer. The method's full specification lives inside the plugin you installed, at `plugin/hooks/universal-behaviour.md` (the behavioural rules and operational procedures) and `plugin/docs/DOC-STRUCTURE.md` (the structural rules for the project's docs). Both files are also browsable on the source repo at `https://github.com/FlintCraftTech/sovereign-implementer/tree/main/plugin/docs`. From V17 onwards, versions are tracked as git tags (`v17`, `v18`, ...), one tag per working session.

Reach for them when:

- A concept this primer mentions in passing turns out to matter to a decision being made.
- A rule's edge case is the thing actually needed.
- A non-method project is being migrated onto the method and `/setup`'s case 3 dialogue surfaces a structural rule whose reasoning matters.
- The method itself is being extended — proposing changes, building related tooling, or distinguishing what is core from what is editable habit.

For everything else, this primer is enough.

---
*No-code method — Version 58.*
