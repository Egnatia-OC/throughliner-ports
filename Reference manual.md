# Reference manual

*A standalone primer for the no-code method as a Claude Code plugin.*

## What this is, and who it's for

A Claude Code plugin for non-coders ("the no-coder"), as distinct from their product's end users. The plugin gives Claude a structured workflow — phase-based (planning, before-build, build, after-build), backed by markdown files in the project that act as guardrails and hold design decisions, queued work, and test outcomes.

The plugin doesn't write code; Claude does. The plugin keeps Claude inside a rigid workflow: new features can't enter a build batch directly (planning first), builds don't start until previous test outcomes are confirmed, some docs are locked from Claude, and Claude is instructed to push back when something looks wrong.

Shaped for non-coders who already know what their app should be. Extensive plan-mode use before first build is recommended.

## Install, and a first session

Install via marketplace (persists across sessions):

1. Clone: `git clone https://github.com/FlintCraftTech/sovereign-implementer.git`.
2. In Claude Code: `/plugin marketplace add <path-to-clone>` then `/plugin install no-code-method@sovereign-implementer`.
3. Open a session in the project folder. Hooks fire at session start. Empty or undocumented folders get an advisory pointing at `/setup`.

For one-off use: `claude --plugin-dir <path-to-clone>/plugin` loads without installing.

**Desktop app users.** `/plugin` is CLI-only — doesn't work in the desktop app ([#42142](https://github.com/anthropics/claude-code/issues/42142)). Run install commands in a CLI terminal first; the plugin then loads automatically in desktop sessions.

### Desktop app install procedure

**First install:**
1. Open a terminal (PowerShell/Terminal).
2. Run `claude` to start a CLI session.
3. `/plugin marketplace add <path-to-clone>`.
4. `/plugin install no-code-method@sovereign-implementer`.
5. Close CLI. Open desktop app. Verify: **Customise** (gear icon) → **Plugins**.

**Verifying version:** Desktop app → **Customise** → **Plugins** → gear icon on plugin entry.

**Updating:** After pulling new changes, if the desktop app shows the old version:
1. CLI: `claude` → `/plugin uninstall no-code-method@sovereign-implementer`.
2. `/plugin marketplace add <path-to-clone>` → `/plugin install no-code-method@sovereign-implementer`.
3. Close CLI. Close desktop app completely (Windows: Task Manager to end process). Reopen.
4. Verify version.

**Troubleshooting stale versions:** If a previous `--plugin-dir` load persists:
1. CLI: uninstall the plugin.
2. Edit `~/.claude/settings.json` (`%USERPROFILE%\.claude\settings.json` on Windows) — remove `enabledPlugins` entries referencing the old path.
3. Close desktop app completely. Reopen. Reinstall via CLI. Verify.

The `settings.json` edit is a last resort — only when CLI uninstall/reinstall doesn't clear the stale version.

See *Managing the plugin* below for disable/re-enable/uninstall.

**First session:**
- Open Claude Code in the project folder. Run `/setup`.
- `/setup` detects the case (empty, existing code, foreign docs, already managed) and runs the matching dialogue.
- For empty folders: scaffolds spine docs and walks four prompts (project context, UX principles, core functionalities, first batch sketch).
- Outputs land as `[PROPOSED EDIT PENDING]` blocks. The no-coder applies them to UX.md by hand, converts the sketch into a build batch with a `Serves UX.md:` line.
- Run `/before-build` to lock the batch, then `/build` to execute. The plugin orchestrates the rest.

## Managing the plugin

Once installed, the plugin fires in every folder.

### Disabling in a specific project

**Desktop app:** **Customise** → **Plugins** → gear icon → toggle off. Sticks for that folder.

**CLI:** `/plugin disable no-code-method@sovereign-implementer` or interactive `/plugin` → **Installed** → select → **Disable**. Run `/reload-plugins` afterward.

### Re-enabling

**Desktop app:** **Customise** → **Plugins** → toggle back on.

**CLI:** `/plugin enable no-code-method@sovereign-implementer`. Run `/reload-plugins`.

### Uninstalling

CLI only — the reliable path:
```
/plugin uninstall no-code-method@sovereign-implementer
```
The UI uninstall has been reported as unreliable ([#52456](https://github.com/anthropics/claude-code/issues/52456)).

### For `--plugin-dir` sessions

Only loaded for that session. Close and start without the flag.

### Known platform issues

- **Disabled plugins may still run hooks** ([#39307](https://github.com/anthropics/claude-code/issues/39307)). Uninstall instead of disabling.
- **`enabledPlugins: false` in settings.json may be ignored** ([#28554](https://github.com/anthropics/claude-code/issues/28554)). Use `/plugin disable` or the desktop app toggle.

## Guardrail docs

Six items sit in the project root after `/setup`, plus two folders:

- **CLAUDE.md** — entry point. JSON path block tells Claude where docs live. Read every session.
- **UX.md** — user-facing app description. Every entry corresponds to something experienceable + a "the user needs this because…" rationale. Source of truth — Claude cannot edit; no-coder maintains by hand during planning.
- **BACKLOG/** — deferred work. `INDEX.md` carries four sections: Red flags, Planning batches, Build batches (reference list), Open questions. Each build batch lives in its own file (e.g. `0001-add-today-screen.md`) with scope-context and build-operations regions. Reordering = moving lines in INDEX.md, not renaming files.
- **MANIFEST.md** — flat alphabetical glossary of named codebase elements. Each entry: name + file path + description. Maintained by Claude during builds. The path field anchors a read-before-edit gate.
- **TEST-LOG.md** — row-per-test record with 10 columns (# / Date / Session / Component / Test Description / Type / Verifier / Status / Confirmed Explicitly / Notes). After a build, Claude appends rows, runs automatable tests, leaves user-verified rows for planning read-back. Rows pruned when their component leaves MANIFEST.
- **build-log/** — per-build narrative files + INDEX.md. What shipped / Decisions / Pivots / Carried forward / Performance. Queryable via grep across builds.

`/setup` also creates:
- **planning/drafts/** — holding area for content not yet ready for a specific doc.
- **research/** — findings from Claude's research. Zero maintenance. Persists for future sessions.

Projects can declare additional source-of-truth docs (e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`) — same locking rules as UX.md.

## The session shape

Two phases loop: **planning** and **build**. `/clear` or new session separates them.

**Planning sessions** decide what gets built. The planning subagent: closes the previous test session (per-row read-back), runs five drift checks, scans Open questions, sorts ideas into Suggestions (in scope) and Discoveries (out of scope), and edits BACKLOG directly. Source-of-truth doc edits happen by hand — the no-coder applies proposed edits, removes resolved batches, reorganises priorities.

**Build sessions** ship engineering work. `/before-build` locks the batch (validates Serves line, populates Inputs/Files/Tests, proposes splits if needed). `/build` runs the batch-executor against the file list. PreToolUse enforces batch boundaries. When done, the after-build subagent updates MANIFEST, opens the test session, runs Claude-automatable tests, generates a two-section recap ("Claude has verified" / "please manually check"), writes the build-log entry, and prompts commit/tag/test.

The no-coder `/clear`s, refreshes, runs user-verified tests, and brings outcomes to the next planning session.

**Sessions are stateless; the docs are the memory.** BACKLOG, MANIFEST, TEST-LOG, build-log tell each session where things stand. Nothing carries from in-memory state.

## The method absorbs mid-stream ideation

Ideas arrive mid-stream — tests, conversations, feedback. The planning phase catches and routes them. But catching alone isn't enough; scoping matters. A batch that says only "add dark mode" gives no testing anchor, no record of purpose, no surface for pushback.

Every batch gets the same structure: Goal (why), Outputs (what changes), Success criteria (how to know it worked), plus conditional Decisions/Dependencies/Red flags. Written during planning — the no-coder speaks the substance, the subagent records it. By build time, the batch carries its own context.

## Anatomy of a batch

Two regions: **scope context** (strategic) and **build operations** (tactical).

**Status tracking.** An optional `Status:` line at the top of the batch body tracks lifecycle state: `queued` (default — absent means queued), `active` (locked by before-build), `parked` (paused by planning), `shipped` (completed by after-build). The parser skips shipped and parked batches. State machine: `queued → active → shipped`, with `active ↔ parked` via planning.

**Scope context** (planning subagent):
- **Goal.** Why this batch exists.
- **Outputs.** What changes the user experiences.
- **Success criteria.** Observable conditions for success.
- **Decisions.** Unresolved scope questions (omit if resolved).
- **Dependencies.** What's needed from outside (omit if none).
- **Red flags.** Security concerns (only when detected).

**Build operations** (before-build subagent):
- **Changes:** Labeled `[Requested]`/`[Suggested]`.
- **Inputs:** Non-standard resources needed.
- **Files:** `- [ ]`/`- [x]` task list.
- **Tests:** Type + verifier per test.
- **Serves UX.md:** Which entry the batch implements.

The `Changes:` delimiter separates the two regions.

## Walkthrough — Taskflow Day 1

### Starting from scratch

Empty folder → `/setup` → four prompts:
1. **Project context.** What the app does and what makes it distinct.
2. **UX principles.** For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*.
3. **Core functionalities.** Three to five features with "user needs this because…" lines.
4. **First batch sketch.** Smallest end-to-end buildable thing.

Answers land as `[PROPOSED EDIT PENDING]` blocks. No-coder applies them, seeds the first build batch.

### Risk accepted in action

Taskflow's **One-day-at-a-time view** ends with a Risk accepted line explaining why there's deliberately no week view — protecting against re-litigation six months later.

### First build, first test note

Build ships. No-coder tests, writes notes:
> "Couldn't find a due date — intentional? Screen hard to read at night — dark mode?"

Notes pasted into new session → planning route.

### How a test note becomes a feature

The dark-mode item:
1. **Idea raised.** Test note.
2. **Planning batch.** Questions: justify a parallel theme? OS setting or toggle? Which entries need contrast review?
3. **Questions answered.** Yes, OS setting, two entries need contrast pass.
4. **UX.md updated.** New *Dark mode* entry.
5. **Build batch.** With `Serves UX.md: Dark mode`.

If step 3 answers "no," steps 4–5 don't happen. That's equally valid.

**UX principle conflicts** get surfaced in chat immediately — not quietly routed into a batch.

### Drift checks

Five checks at every planning session start:
- **Direct-edit detection.** Git-diff against last build. Per-file: "Was this you?"
- **UX.md ↔ what's built.** Feature-to-feature comparison.
- **MANIFEST.md ↔ codebase.** Name-to-name comparison.
- **MANIFEST.md ↔ UX.md (loose).** User-facing purpose check. Plumbing exempt.
- **TEST-LOG ↔ code-touch.** Per-row: has the tested component changed since?

## The four disciplines

**The "user needs this because…" line.** Forces rationale before implementation. Protects against drift.

**The flag taxonomy.** Red flags → BACKLOG Red flags section. Suggestions → chat. Discoveries → planning batches before session end. Every concern has exactly one home.

**The feature pipeline.** Planning batch → answered → UX.md entry → build batch. Rigid by design.

**The test-confirmation gate.** New batch blocked while previous-batch TEST-LOG rows are unconfirmed. Per-row read-back; bulk confirmations don't count. PreToolUse hook enforces structurally.

## Four test types and the Claude/user split

- **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
- **Run and read** — command execution. Fully automatable.
- **Trigger and observe** — event-driven. Fully automatable.
- **Generate and inspect** — artefact production. Fully automatable.

Verifier is per-row, not per-type. Both Claude and user rows can exist across any type. All must reach `Confirmed Explicitly: Yes` before the next build.

## The safety net

When a session opens, **SessionStart** checks adopted vs. unadopted. Unadopted folders with substantial work trigger an advisory pointing at `/setup`.

Until `/setup` runs, **PreToolUse** blocks Edit/Write/MultiEdit and method-subagent calls.

`/setup` branches: empty folder → scaffold + four prompts; existing code, no docs → scaffold alongside; foreign docs → migrate/overwrite/leave; already managed → refresh footers + migrations.

Nothing destructive without confirmation; every destructive option backs up first.

## What's inside the plugin

- **Hooks** (Python, deterministic enforcement): SessionStart detects folder state + injects behavioural rules. PreToolUse enforces edit boundaries (project-boundary, locked docs, batch file list, test gate, adoption gate, read-before-edit, Serves-line check, destructive git guard). PostToolUse validates BACKLOG format after edits. Stop hook routes between batches / to after-build. PreCompact blocks compaction mid-build (recommends handoff). UserPromptSubmit classifies first prompt + injects routing hint.
- **Subagents** (own contexts): planning, before-build, batch-executor, after-build, setup. Each returns a recap main Claude relays.
- **Slash commands** (`/setup`, `/before-build`, `/build`): user-facing entry points invoking matching subagents.
- **Templates**: starter shapes for spine docs.
- **Bundled docs** (`DOC-STRUCTURE.md`, `VOCABULARY.md`): read by subagents via `${CLAUDE_PLUGIN_ROOT}/docs/`.

Hooks (deterministic) handle correctness; subagents (probabilistic) handle judgment.

## Two layers of permission

Claude Code's permission modes (Ask/Accept/Plan/Auto/Bypass) control whether the no-coder gets prompted. The plugin's PreToolUse hooks decide whether Claude is allowed to act at all — firing in every mode, including Bypass.

Every deny is prefixed `[No-code method]` with a `What to do:` line.

### Which mode for which phase

| Phase | Mode | Why |
|---|---|---|
| Planning | Accept edits | Planning subagent edits BACKLOG. |
| Before-build | Accept edits | Writes Files: into BACKLOG. |
| Build | Auto | Source-file edits. Hooks enforce boundaries. |
| After-build | Auto | Writes MANIFEST, TEST-LOG, build-log. |
| Pre-method ideation | Plan mode | No edits needed yet. |

### Known limitation: subagent permission prompts

Subagents prompt on every tool call regardless of mode — a Claude Code bug ([#28584](https://github.com/anthropics/claude-code/issues/28584), [#40241](https://github.com/anthropics/claude-code/issues/40241)). Auto mode produces the fewest prompts. `/fewer-permission-prompts` helps with main-conversation prompts.

## What's editable

Three layers:

**Method contract — edit at peril.** Rules the machinery depends on. Push-back-rather-than-agree drives drift checks. No-stealth-fix drives the recap. Batch-scope-locking drives clean test coverage. Each annotated with what breaks without it.

**Recommended habits — edit freely.** `/clear` cadence, test-prep workflow, commit timing.

**The build sequence — fixed.** Four-phase cycle is the spine.

### Editing surfaces

| Doc | Claude edit access |
|---|---|
| `UX.md` | **read-only** |
| Additional source-of-truth docs | **read-only** |
| `BACKLOG.md` | read/write |
| `MANIFEST.md` | read/write |
| `TEST-LOG.md` | read/write |
| `CLAUDE.md` | read/write |

**Footer exception.** Footer stamps are metadata — PreToolUse allows footer-only edits on locked docs.

**`[PROPOSED EDIT PENDING]` mechanism.** Claude queues content in the destination doc's `## Proposed edits pending` section. Preview-then-apply convention during planning: show in chat → approval → write block → prompt to apply now.

## Why the rules

**Push back rather than agree.** Drift checks and red-flag surfacing assume pushback. Agreement-by-default disables safety nets.

**State regressions plainly.** The recap is the no-coder's record. Stealth-fixes break it.

**Lock batch scope once agreed.** Protects session predictability, clean test coverage, and the planning-gate filter.

**Five drift checks at different levels.** File-temporal, feature-to-feature, name-to-name, purpose-level, per-row code-touch. Bundling produces noise; separate passes catch what each is designed for.

**Lock source-of-truth docs.** Build sessions are the wrong environment for design changes. Planning sessions give decisions proper deliberation.

**No placeholders in source-of-truth docs.** Runtime audiences need the instruction, not its status.

**Project-specific UX principles.** Generic principles are too abstract to guard decisions.

**MANIFEST starts flat.** Most projects never need sections. Pre-sectioning forces premature architecture decisions.

**BACKLOG is a folder, not four files.** INDEX.md = one place for what's outstanding. Per-batch files = content volume. Split is content-volume, not category.

**Risk accepted as a labelled line.** Keeps the trade-off on the page for re-litigation.

**Per-row read-back.** Bulk confirmations silently flip rows the user didn't actually verify.

## What this costs

A new feature takes two sessions minimum — one planning, one build. Every shipped feature traces to a written rationale; nothing gets built that no one decided to build.

## Where the method sits

Spec-driven development family. Closest neighbour: Cline's Memory Bank (same shape — markdown as project memory, read at session start; different file cut, different audience). In the broader spec-driven literature, this maps onto the **spec-anchored** rigour level.

## Caveats

Iteratively developed. Not yet used to ship a complete app. First real Taskflow build under the current version is the next test.

~30% of the time, Claude won't follow CLAUDE.md-style instructions. The method designs around this with read-only docs and reviewable decisions, but the headwind is real.

Claude Code's plan panel doesn't show the method's build sequence — it's Claude-Code-internal with no plugin write surface. The actual queue is in BACKLOG → Build batches.

## When you need more

Full spec: `plugin/hooks/universal-behaviour.md` (behavioural rules) and `plugin/docs/DOC-STRUCTURE.md` (structural rules). Also on GitHub at `https://github.com/FlintCraftTech/sovereign-implementer/tree/main/plugin/docs`.

Reach for them when a concept needs detail, a rule's edge case matters, a migration surfaces structural reasoning, or the method itself is being extended.

---
*No-code method — Version 60.*
