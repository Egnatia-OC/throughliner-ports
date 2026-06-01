# Reference manual

*A standalone primer for Sovereign Implementer as a Claude Code plugin.*

## What this is, and who it's for

A Claude Code plugin for non-coders ("the no-coder"), as distinct from their product's end users. The plugin gives Claude a structured workflow — phase-based (planning, build, close, git), backed by markdown files that act as guardrails and hold design decisions, queued work, and test outcomes.

The plugin doesn't write code; Claude does. The plugin keeps Claude inside a rigid workflow: new features can't enter a build batch directly (planning first), builds don't start until previous tests are confirmed, some docs are locked from Claude, and Claude pushes back when something looks wrong.

Shaped for non-coders who already know what their app should be. Extensive plan-mode use before first build is recommended.

## Install, and a first session

Install via marketplace (persists across sessions):

1. Clone: `git clone https://github.com/FlintCraftTech/sovereign-implementer.git`.
2. In Claude Code: `/plugin marketplace add <path-to-clone>` then `/plugin install sovereign-implementer@sovereign-implementer`.
3. Open a session in the project folder. Hooks fire at session start. Adopted projects get a status summary (batch counts, next batch, pending tests). Empty or undocumented folders get an advisory pointing at `/sovsetup`.

For one-off use: `claude --plugin-dir <path-to-clone>/plugin` loads without installing.

**Desktop app users.** `/plugin` is CLI-only — doesn't work in the desktop app ([#42142](https://github.com/anthropics/claude-code/issues/42142)). Run install commands in a CLI terminal first; the plugin then loads automatically in desktop sessions.

### Desktop app install procedure

**Packaging the plugin:**

```powershell
cd <path-to-clone>\sovereign-implementer
Compress-Archive -Path plugin\* -DestinationPath sovereign-implementer-plugin.zip
```

This puts `.claude-plugin/plugin.json` at the zip root, which the desktop app expects.

**Installing:**

1. Click **Customise** in the top left corner.
2. Click the plugin icon in the left sidebar.
3. Click the **+** icon to the left of "Personal plugins."
4. Click **Create plugin** → **Upload plugin**.
5. Select the `.zip` file (not the folder). Click **Open**.

**Updating:** Re-run the `Compress-Archive` command (delete the old zip first if it exists), then repeat steps 1–5. The desktop app replaces the previous version.

**Verifying version:** Desktop app → **Customise** → **Plugins** → gear icon on plugin entry.

**Troubleshooting stale versions:** If a previous `--plugin-dir` load persists:
1. CLI: uninstall the plugin.
2. Edit `~/.claude/settings.json` (`%USERPROFILE%\.claude\settings.json` on Windows) — remove `enabledPlugins` entries referencing the old path.
3. Close desktop app completely. Reopen. Reinstall or re-upload zip. Verify.

Last resort — only when uninstall/reinstall doesn't clear the stale version.

See *Managing the plugin* below for disable/re-enable/uninstall.

**First session:**
- Open Claude Code in the project folder. Run `/sovsetup`.
- `/sovsetup` detects the case (empty, existing code, foreign docs, already managed) and runs the matching dialogue.
- Empty folders: scaffolds spine docs and walks five prompts (product overview, UX principles, core functionalities, first batch sketch, language).
- Claude writes directly to UX.md during setup (planning phase — docs are open). The no-coder converts the first-batch sketch into a build batch with a `Serves UX.md:` line.
- `/sovrecap` reviews the batch's file list and test plan, `/sovbuild` locks and builds. `/sovclose` handles quality gates and record-keeping, `/sovgit` walks through commit/tag/push.

## Managing the plugin

Once installed, the plugin fires in every folder.

### Disabling in a specific project

**Desktop app:** **Customise** → **Plugins** → gear icon → toggle off. Per-folder.

**CLI:** `/plugin disable sovereign-implementer@sovereign-implementer` or `/plugin` → **Installed** → select → **Disable**. Run `/reload-plugins` afterward.

### Re-enabling

**Desktop app:** **Customise** → **Plugins** → toggle back on.

**CLI:** `/plugin enable sovereign-implementer@sovereign-implementer`. Run `/reload-plugins`.

### Uninstalling

**Desktop app:**
1. Click **Customise**.
2. Click **Browse plugins**.
3. Click **Code**.
4. Click the gear icon on the Sovereign Implementer card.
5. Click **Uninstall**.

**CLI:**
```
/plugin uninstall sovereign-implementer@sovereign-implementer
```

### For `--plugin-dir` sessions

Only loaded for that session. Close and start without the flag.

### Known platform issues

- **Disabled plugins may still run hooks** ([#39307](https://github.com/anthropics/claude-code/issues/39307)). Uninstall instead of disabling.
- **`enabledPlugins: false` in settings.json may be ignored** ([#28554](https://github.com/anthropics/claude-code/issues/28554)). Use `/plugin disable` or the desktop app toggle.

## Guardrail docs

After `/sovsetup`, CLAUDE.md sits at the project root and everything else lives inside `_method/`:

- **CLAUDE.md** (project root) — entry point. Product overview (what, who, friction, milestones) plus JSON path block telling Claude where docs live. Read every session.
- **_method/UX.md** — user-facing app description. Every entry corresponds to something experienceable + "the user needs this because…" rationale. Source of truth — Claude cannot edit; no-coder maintains during planning.
- **_method/BACKLOG/** — deferred work. Per-batch files (e.g. `0001-add-today-screen.md`) with scope-context and build-operations regions. Index sections (Red flags, Planning batches, Build batches, Open questions) live in `_method/proxies/backlog.md`. Reordering = moving proxy lines, not renaming files.
- **_method/MANIFEST.md** — flat alphabetical glossary of named codebase elements. Each: name + path + description + rationale. Maintained by Claude during builds. Two audiences: user (lookup reference) and Claude (recalls why a component was built). The path field anchors a read-before-edit gate — the first time Claude tries to edit a MANIFEST-covered file in a session, PreToolUse denies the edit and shows the MANIFEST entry inline. This ensures Claude has context about what a feature is and why it exists before changing it. The retry succeeds because the gate sees the entry was already shown.
- **_method/test-log/** — per-session test files. 10-column rows (# / Date / Session / Component / Test Description / Type / Verifier / Status / Confirmed Explicitly / Notes). After build, Claude writes a file, runs automatable tests, leaves user-verified rows for planning read-back. Index in BACKLOG proxy. Rows pruned when their component leaves MANIFEST.
- **_method/build-log/** — per-build narrative files. What shipped / Decisions / Pivots / Performance. Index at `_method/proxies/build-log.md`. Queryable via grep.

`/sovsetup` also creates inside `_method/`:
- **_method/planning/drafts/** — holding area for content not yet ready for a specific doc.
- **_method/research/** — findings from Claude's research. Zero maintenance. Persists for future sessions.
- **_method/proxies/** — index and summary files. Large spine docs burn context window when Claude reads them whole, leaving less room for actual work. Proxies give Claude a lightweight index with line-number references so it can target-read specific sections instead. `backlog.md` and `build-log.md` are operational indexes (directly edited); `backlog.md` also contains the test session index. `ux.md`, `manifest.md`, `research.md` are summaries regenerated for context efficiency.

Projects can declare additional source-of-truth docs (e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`) — same locking rules as UX.md.

## The session shape

Two phases loop: **planning** and **build**. `/clear` or new session separates them. Each skill can be invoked independently — you don't have to follow the cycle in strict order. Skills that need prior state (e.g. `/sovclose` without a build) will tell you what to run first.

**Why the routing matters.** When a session opens, the plugin classifies your first message and loads the matching procedure doc. Without routing, every session would open with generic preamble and you'd have to manually direct Claude to the right workflow. The routing table is priority-ordered — first match wins — so test notes, setup requests, and bug reports each get their own path without you needing to know the internal procedure names.

**Planning sessions** decide what gets built. Two modes, each a separate skill:

- `/sovplan` — **structural planning.** Closes previous test session (per-row read-back), runs five drift checks, sorts ideas into Suggestions and Discoveries, edits BACKLOG directly, runs batch-ordering audit. Reorder, split, merge, or rescope batches.
- `/sovdeliberate` — **OQ deliberation and idea capture.** Works through accumulated open questions one by one: promote to batch, drop with reason, or re-park with updated rationale. Also handles capturing new thoughts — quick one-liners land as light OQs, richer topics get full deliberation.

Source-of-truth docs (UX.md, additional docs) are directly editable by Claude during planning — no ceremony needed.

**Why two phases?** Planning and build need different editing permissions. During planning, you're shaping what gets built — source-of-truth docs like UX.md need to be open. During build, the spec is settled and code is being written — locking source-of-truth docs prevents spec drift mid-implementation, while locking source code during planning prevents premature implementation before the spec is ready. Phase detection is based on whether `_method/active-build.md` exists: present = build phase, absent = planning phase.

**Build sessions** ship engineering work. `/sovrecap` reviews the batch (validates Serves line, populates Inputs/Files/Tests, proposes splits if needed). `/sovbuild` snapshots the batch into `_method/active-build.md` and removes it from BACKLOG. The snapshot serves two purposes: it gives phase detection an unambiguous signal (file exists = build in progress), and it unlocks BACKLOG for parallel planning or deliberation in other sessions. The build runs against the snapshot's file list; PreToolUse enforces batch boundaries. `/sovclose` runs in two turns:

- **Turn 1 (judgment)** — while context is fresh: MANIFEST + capabilities summary update, doc parity, test session + Claude-automatable tests, build recap, build-log entry, decision sweep (routes cross-cutting design decisions to MANIFEST rationale), snapshot deleted (build-log is the shipped record), frame-correction and staleness sweeps, lost-feature check, idea sweep, then `/compact` recommendation.
- **Turn 2 (mechanical)** — after compaction: footer bumps if plugin version changed (`bump_version.py`), proxy regeneration, project-specific after-build steps, pre-commit checkpoint, `/sovgit` nudge.

Short sessions can run both turns without compacting. `/sovgit` walks you through commit, tag, and push in plain English.

**Why close is mandatory.** Skipping `/sovclose` leaves an orphaned `_method/active-build.md` snapshot that blocks all future builds — the plugin sees a build in progress that never finished. Close also writes the build-log entry (the shipped record), MANIFEST updates, test rows, and runs parity checks that catch drift before it compounds. A PreToolUse guard blocks `git commit` when all files are ticked but close hasn't run, so you can't accidentally commit without the close outputs.

**Session-length safeguards.** Long sessions degrade adherence as context fills — Claude has no visibility into its own context-window usage, so it can't self-regulate. Three advisory mechanisms give recovery points: (1) pre-build sizing warns during `/sovrecap` for 8+ files with open design questions (high file count alone is fine — it's the combination with unresolved deliberation that blows out sessions), (2) mid-session compact nudge at 15+ exchanges past `/sovbuild` without `/sovclose`, (3) every skill handoff recommends `/compact`. None block. PreCompact blocks mid-build compaction and surfaces a handoff prompt instead — compaction during a build can silently drop critical context, so a fresh session with full method-doc reads is safer.

The no-coder `/clear`s, refreshes, and tests. Two options: `/sovtest` for a guided walkthrough of each pending User-verified row, or test independently and bring per-row outcomes to the next planning session.

**If a build goes wrong,** `/sovrevert` walks the user through undoing it — restoring the project to the last committed state. No git knowledge required.

**Sessions are stateless; the docs are the memory.** BACKLOG, MANIFEST, TEST-LOG, build-log tell each session where things stand. Nothing carries from in-memory state.

## The method absorbs mid-stream ideation

Ideas arrive mid-stream — tests, conversations, feedback. `/sovdeliberate` handles both: quick thoughts land as light OQs (heading + Surfaced tag + one sentence, writable even during builds), and accumulated entries get worked through — promoted to batches, dropped, or re-parked. But catching alone isn't enough; scoping matters. A batch that says only "add dark mode" gives no testing anchor, no record of purpose, no surface for pushback.

Every batch gets the same structure: Goal (why), Outputs (what changes), Success criteria (how to know it worked), plus conditional Decisions/Dependencies/Red flags. Written during planning — no-coder speaks the substance, Claude records it. By build time, the batch carries its own context.

## Anatomy of a batch

Two regions: **scope context** (strategic) and **build operations** (tactical).

**Status tracking.** Under V99+, active builds use a snapshot (`_method/active-build.md`) rather than a status line. Two active values: `queued` (default — absent = queued) and `parked` (paused by planning). Completed batches are removed from BACKLOG entirely — the build-log entry is the shipped record. Legacy `active` and `shipped` values still recognized by the parser.

**Scope context** (written during planning):
- **Goal.** Why this batch exists.
- **Outputs.** What changes the user experiences.
- **Success criteria.** Observable conditions for success.
- **Decisions.** Unresolved scope questions (omit if resolved).
- **Dependencies.** What's needed from outside (omit if none).
- **Red flags.** Security concerns (only when detected).

**Build operations** (written during `/sovrecap`):
- **Changes:** Labeled `[Requested]`/`[Suggested]`.
- **Inputs:** Non-standard resources needed.
- **Files:** `- [ ]`/`- [x]` task list.
- **Tests:** Type + verifier per test.
- **Serves UX.md:** Which entry the batch implements.

The `Changes:` delimiter separates the two regions.

## Walkthrough — Taskflow Day 1

### Starting from scratch

Empty folder → `/sovsetup` → five prompts:
1. **Product overview.** What the product does, who it's for, what makes it distinct or what tension it solves, and milestones.
2. **UX principles.** For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*.
3. **Core functionalities.** Three to five features with "user needs this because…" lines.
4. **First batch sketch.** Smallest end-to-end buildable thing.
5. **Language.** What language Claude should use for responses and documentation. Defaults to English.

Claude writes the overview to CLAUDE.md and project context to UX.md (planning phase — docs open). No-coder seeds the first build batch.

### Risk accepted in action

Taskflow's **One-day-at-a-time view** ends with a Risk accepted line explaining why there's deliberately no week view — protecting against re-litigation six months later.

### First build, first test note

Build ships. No-coder tests, writes notes:
> "Couldn't find a due date — intentional? Screen hard to read at night — dark mode?"

Notes pasted into new session → planning route.

### How a test note becomes a feature

The dark-mode item:
1. **Idea raised.** Test note.
2. **Planning batch.** Questions: parallel theme justified? OS setting or toggle? Which entries need contrast review?
3. **Questions answered.** Yes, OS setting, two entries need contrast pass.
4. **UX.md updated.** New *Dark mode* entry.
5. **Build batch.** `Serves UX.md: Dark mode`.

If step 3 answers "no," steps 4–5 don't happen. Equally valid.

**UX principle conflicts** surface in chat immediately — not quietly routed into a batch.

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

## The `[SECURITY]` marker

Entries touching sensitive surfaces — authentication, PII, payments, deletion, access control — carry an inline `[SECURITY]` tag on their heading. Applies to UX.md entries, BACKLOG build batches, planning batches, and OQs. Not enforced by hooks — informational only. The user sees it reviewing their spec; Claude uses it to bias security-marked items earlier in batch ordering.

## Four test types and the Claude/user split

- **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
- **Run and read** — command execution. Fully automatable.
- **Trigger and observe** — event-driven. Fully automatable.
- **Generate and inspect** — artefact production. Fully automatable.

Verifier is per-row, not per-type. Both Claude and user rows exist across any type. All must reach `Confirmed Explicitly: Yes` before the next build.

## The safety net

When a session opens, **SessionStart** checks adopted vs. unadopted. Unadopted folders with substantial work trigger an advisory pointing at `/sovsetup`.

Until `/sovsetup` runs, **PreToolUse** blocks Edit/Write/MultiEdit. In unadopted folders, the deny message says "run `/sovsetup` first" — not "describe it in a BACKLOG batch," which is meaningless pre-setup.

`/sovsetup` branches: empty → scaffold + five prompts; existing code, no docs → scaffold alongside; foreign docs → migrate/overwrite/leave; already managed → refresh footers + migrations.

Nothing destructive without confirmation; destructive options back up first.

### Parent-directory placement

Claude Code inherits CLAUDE.md files from parent directories. If a project sits inside another project's tree, the parent's instructions affect the session — potentially poisoning Claude's behaviour with rules meant for a different project.

**SessionStart** detects parent CLAUDE.md files and surfaces a warning. Fires in all tiers (empty, partial, complete, unadopted).

**Best practice:** keep project folders at independent locations (e.g. `Desktop/MyApp/`, not `Desktop/OtherProject/MyApp/`). If nesting is unavoidable, the warning suggests relocating.

### Concurrent-build detection

SessionStart detects an existing `_method/active-build.md` with unticked files — a build is in progress elsewhere. Warning asks whether resuming or starting parallel work. Parallel builds corrupt file state and git history; only ideation is safe in parallel. Distinct from unclosed-build detection (all files ticked = build finished, `/sovclose` never ran).

### Destructive-command guards

Two PreToolUse guards prevent work loss from shell commands:

- **Git safety guard** — blocks `git reset --hard` and `git push --force`. These are the two commands most likely to destroy uncommitted work or overwrite remote history. `--force-with-lease` is explicitly allowed (it's the safe alternative). The guard is mechanical — Claude can't override a hook, even if asked.
- **Bash write guard** — scans shell commands for file-write patterns and applies the same phase-aware rules as the edit hooks. Without it, a `cat > file.txt` or `echo > file.txt` in Bash would bypass all the Edit/Write/MultiEdit protections.

A separate **unclosed-build commit guard** blocks `git commit` when all batch files are ticked but `/sovclose` hasn't run. Committing in that state would create a snapshot that looks finished but lacks the close outputs (build-log entry, MANIFEST updates, test rows) — and the orphaned snapshot would block all future builds.

### Open-question staleness

SessionStart flags OQs sitting 20+ sessions unresolved, surfacing them in the status summary. Nudges toward a deliberation session.

## Language setting

CLAUDE.md carries a `Language:` field (set during `/sovsetup`, defaults to English). Claude responds and writes doc content in this language. Plugin docs stay English — Claude reads internally, paraphrases output.

Control tokens (`Status:`, `Changes:`, `Serves UX.md:`, `[SECURITY]`, `Confirmed Explicitly:`) remain English regardless — hooks regex-match them. Translating them breaks phase enforcement.

`/sovsetup` also sets `git config --local core.quotepath false` to prevent Git from escaping non-ASCII filenames — without it, accented or CJK filenames in batch file lists fail path matching.

## Research search flow

Claude watches for decisions that would benefit from external information — API capabilities, library comparisons, platform constraints. It drafts a search query, proposes it, and waits for approval. The plugin's value here isn't the search itself — it's the discipline wrapper: filing results to `_method/research/`, structuring queries with what decision they inform, and prompting proactive research before wrong assumptions get baked into code or docs.

**`/sovresearch`** triggers explicitly. Claude also suggests searches proactively when it spots an information gap.

**Three mechanisms**, priority order:
1. **MCP search tool** — if a Gemini search MCP server (e.g. `yukukotani/mcp-gemini-google-search`) is installed. Preferred.
2. **WebSearch** — Claude's built-in tool, when MCP unavailable.
3. **Copyable prompt** — formatted query for the user's preferred research environment. When neither tool available.

**Query files** saved to `research/search-queries/YYYY-MM-DD-topic-slug.md` — structured records with trigger, decision it informs, query, criteria, response, outcome. Distinct from free-form `research/<topic>.md` files.

**MCP server setup** (optional — fallbacks work without it):
1. Install `yukukotani/mcp-gemini-google-search` (or another MCP search server).
2. Get a Gemini API key from Google AI Studio.
3. Set `GEMINI_API_KEY` environment variable.
4. Register the MCP server in Claude Code's settings.

The plugin doesn't ship or store API keys — user brings their own.

## Asking questions about the method

`/sovexplain` answers three kinds of questions:

- **"What does my project do?"** — reads the capabilities summary from MANIFEST (a plain-English paragraph auto-generated at each `/sovclose`). Quick orientation without loading full docs.
- **"How do I close a build?"** — routes to the matching skill or procedure doc and summarizes the key steps.
- **"Why is close mandatory?"** — looks up design rationale from the explain-reference index.

No arguments required — Claude classifies the question type and routes to the right source. Also works reactively: invoke `/sovexplain` after a hook denial and Claude infers the question from context.

## What's inside the plugin

- **Hooks** (Python, deterministic): SessionStart detects folder state, injects rules, mandates status summary (batch counts, next batch, pending tests, concurrent-build detection, stale OQs). PreToolUse enforces edit boundaries (locked docs, batch file list, test gate, adoption gate, read-before-edit, Serves-line check, destructive git guard, unclosed-build commit guard, write-guard with project-boundary check). PostToolUse validates doc structure after edits (BACKLOG parse, scope-context, TEST-LOG columns, build-log sections, proxy headers). PreCompact blocks compaction mid-build. UserPromptSubmit classifies first prompt + injects routing hint.
- **Procedure docs** (read on demand): planning, before-build (`/sovrecap`), build (`/sovbuild`), close, git, revert, testing (`/sovtest`), tersify (`/sovtersify`), setup. Each specifies what to load and do. Followed in main context — no agent spawning.
- **Slash commands** (`/sovsetup`, `/sovplan`, `/sovdeliberate`, `/sovrecap`, `/sovbuild`, `/sovclose`, `/sovgit`, `/sovtest`, `/sovresearch`, `/sovtersify`, `/sovrevert`, `/sovexplain`): entry points directing Claude to matching procedure doc or flow.
- **Scripts** (Python): `parse_backlog.py` (BACKLOG parser), `allocate_number.py` (number allocation), `bump_version.py` (footer bumps + proxy updates), `project_state.py` (shared hook helpers), `validate_docs.py` (PostToolUse validation).
- **Templates**: starter shapes for spine docs.
- **Bundled docs** (`DOC-STRUCTURE.md`, `VOCABULARY.md`): read via `${CLAUDE_PLUGIN_ROOT}/docs/`.

Hooks (deterministic) handle correctness; procedure docs (probabilistic) handle judgment.

## Two layers of permission

Claude Code's permission modes (Ask/Accept/Plan/Auto/Bypass) control user prompting. The plugin's PreToolUse hooks decide whether Claude is allowed to act at all — firing in every mode, including Bypass.

Every deny is prefixed `[Sovereign Implementer]` with a `What to do:` line.

### Which mode for which phase

| Phase | Mode | Why |
|---|---|---|
| Planning | Accept edits | Planning procedure edits BACKLOG. |
| Recap (`/sovrecap`) | Accept edits | Writes Files: into BACKLOG. |
| Build (`/sovbuild`) | Auto | Locks batch, source-file edits. Hooks enforce boundaries. |
| Close (`/sovclose`) | Auto | Writes MANIFEST, test-log, build-log. |
| Git (`/sovgit`) | Auto | Commits and pushes. |
| Revert (`/sovrevert`) | Auto | Restores last committed state. |
| Pre-method ideation | Plan mode | No edits needed yet. |

### Permission prompts

Auto mode produces the fewest prompts. `/fewer-permission-prompts` helps reduce remaining ones.

## What's editable

Three layers:

**Method contract — edit at peril.** Rules the machinery depends on. Push-back drives drift checks. No-stealth-fix drives the recap. Batch-scope-locking drives clean test coverage. Each annotated with what breaks without it.

**Recommended habits — edit freely.** `/clear` cadence, test-prep workflow, commit timing.

**The build sequence — fixed.** Four-phase cycle is the spine.

### Editing surfaces — phase-aware

Permissions flip based on project phase:

| Doc | Planning phase | Build phase |
|---|---|---|
| `UX.md` | **read/write** | **locked** |
| Additional source-of-truth docs | **read/write** | **locked** |
| `BACKLOG/` | read/write | read/write |
| `MANIFEST.md` | read/write | read/write |
| `test-log/` | read/write | read/write |
| `CLAUDE.md` | read/write | read/write |
| Source code files | **locked** | batch file list only |
| `research/` files | read/write | read/write |

**Phase detection.** Planning = no `_method/active-build.md` file. Build = file present (created by `/sovbuild`).

**During planning,** Claude edits source-of-truth docs directly — no ceremony.

**During build,** source-of-truth docs are locked, but Claude sometimes spots a needed change while implementing. Rather than blocking entirely, the `[PROPOSED EDIT PENDING]` mechanism lets Claude queue the change in the doc's `## Proposed edits pending` section. You review and apply (or drop) it next planning session. This way, observations aren't lost but design changes still get proper deliberation.

**Footer exception.** Footer stamps are metadata — PreToolUse allows footer-only edits on locked docs regardless of phase.

## Why the rules

**Push back rather than agree.** Drift checks and red-flag surfacing assume pushback. Agreement-by-default disables safety nets.

**State regressions plainly.** The recap is the no-coder's record. Stealth-fixes break it.

**Lock batch scope once agreed.** Protects session predictability, clean test coverage, and the planning-gate filter.

**Five drift checks at different levels.** File-temporal, feature-to-feature, name-to-name, purpose-level, per-row code-touch. Bundling produces noise; separate passes catch different things.

**Lock source-of-truth docs.** Build sessions are the wrong environment for design changes. Planning sessions give decisions proper deliberation.

**No placeholders in source-of-truth docs.** Runtime audiences need the instruction, not its status.

**Project-specific UX principles.** Generic principles are too abstract to guard decisions.

**MANIFEST starts flat.** Most projects never need sections. Pre-sectioning forces premature architecture decisions.

**BACKLOG is a folder, not four files.** `proxies/backlog.md` = one place for what's outstanding. Per-batch files = content volume. Split is content-volume, not category.

**Risk accepted as a labelled line.** Keeps the trade-off on the page for re-litigation.

**Per-row read-back.** Bulk confirmations silently flip rows the user didn't actually verify.

**Open questions are separate from batches.** OQs have a different lifecycle — they're non-blocking parking for things that need deliberation but shouldn't stall the build pipeline. A batch is a commitment to build; an OQ is a question that needs answering before it can become a batch (or get dropped). `/sovdeliberate` walks through them one at a time: promote, drop, or re-park.

**Before-build recap before building.** `/sovrecap` validates the batch — checking the Serves line, populating file lists, proposing splits if the batch is too large. BACKLOG stays editable during the recap so you can discuss and adjust the plan. Without this step, you'd be committing to a batch that might have missing files, no test plan, or scope that should have been split.

**PostToolUse validates doc structure.** After Claude edits a method doc, PostToolUse checks the result for structural correctness — BACKLOG parse errors, wrong TEST-LOG column counts, missing build-log sections, malformed proxy headers. Catching these at write time prevents structural mistakes from propagating into docs that other hooks and procedures depend on. Warnings are advisory (Claude sees and self-corrects), not blocking.

**Response-shape tags control verbosity.** Tags like `[SILENT]`, `[BRIEF]`, `[SEQUENCE]`, `[DISCUSS]`, and `[PROMPT]` appear throughout procedure docs. They solve a specific problem: procedure docs need to specify not just *what* Claude does but *how much it says*. `[SEQUENCE]` means one step at a time (wait for your response before continuing). `[PROMPT]` means end with a clear next-action for you. They compose freely — genuine tension between tags is a doc bug.

## What this costs

A new feature takes two sessions minimum — one planning, one build. Every shipped feature traces to a written rationale; nothing gets built that no one decided to build.

As docs grow, they consume more context — leaving less room for work. `/sovtersify` runs a guided compression pass: triage by size, flag wrong-home content and verbose prose, audit and compress user-selected targets one at a time. Planning phase only — source-of-truth docs are already locked during builds, and the triage analysis itself fills context that isn't needed during the editing pass (so `/sovtersify` recommends `/compact` between triage and audit).

## Where the method sits

Spec-driven development family. Closest neighbour: Cline's Memory Bank (same shape — markdown as project memory, read at session start; different file cut, different audience). Maps onto the **spec-anchored** rigour level in the broader literature.

## Caveats

Iteratively developed. Not yet used to ship a complete app. First real Taskflow build under the current version is the next test.

~30% of the time Claude won't follow CLAUDE.md-style instructions. The method designs around this with read-only docs and reviewable decisions, but the headwind is real.

Claude Code's plan panel doesn't show the method's build sequence — it's internal with no plugin write surface. The actual queue is in BACKLOG → Build batches.

## When you need more

Full spec: `plugin/hooks/universal-behaviour.md` (behavioural rules) and `plugin/docs/DOC-STRUCTURE.md` (structural rules). Also on GitHub at `https://github.com/FlintCraftTech/sovereign-implementer/tree/main/plugin/docs`.

Reach for them when a concept needs detail, a rule's edge case matters, a migration surfaces structural reasoning, or the method itself is being extended.

---
*Sovereign Implementer — Version 112.*
