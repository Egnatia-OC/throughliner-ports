# Reference manual

*A standalone primer for the no-code method as a Claude Code plugin.*

## What this is, and who it's for

A Claude Code plugin for non-coders ("the no-coder"), as distinct from their product's end users. The plugin gives Claude a structured workflow — phase-based (planning, build, close, git), backed by markdown files in the project that act as guardrails and hold design decisions, queued work, and test outcomes.

The plugin doesn't write code; Claude does. The plugin keeps Claude inside a rigid workflow: new features can't enter a build batch directly (planning first), builds don't start until previous test outcomes are confirmed, some docs are locked from Claude, and Claude is instructed to push back when something looks wrong.

Shaped for non-coders who already know what their app should be. Extensive plan-mode use before first build is recommended.

## Install, and a first session

Install via marketplace (persists across sessions):

1. Clone: `git clone https://github.com/FlintCraftTech/sovereign-implementer.git`.
2. In Claude Code: `/plugin marketplace add <path-to-clone>` then `/plugin install no-code-method@sovereign-implementer`.
3. Open a session in the project folder. Hooks fire at session start. In adopted projects, Claude presents a status summary (batch counts, next batch, pending tests) and asks if you'd like to proceed. Empty or undocumented folders get an advisory pointing at `/sovsetup`.

For one-off use: `claude --plugin-dir <path-to-clone>/plugin` loads without installing.

**Desktop app users.** `/plugin` is CLI-only — doesn't work in the desktop app ([#42142](https://github.com/anthropics/claude-code/issues/42142)). Run install commands in a CLI terminal first; the plugin then loads automatically in desktop sessions.

### Desktop app install procedure

**Packaging the plugin:**

```powershell
cd <path-to-clone>\sovereign-implementer
Compress-Archive -Path plugin\* -DestinationPath sovereign-implementer-plugin.zip
```

This puts `.claude-plugin/plugin.json` at the zip root, which is what the desktop app expects.

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
3. Close desktop app completely. Reopen. Reinstall via CLI or re-upload zip. Verify.

The `settings.json` edit is a last resort — only when CLI uninstall/reinstall doesn't clear the stale version.

See *Managing the plugin* below for disable/re-enable/uninstall.

**First session:**
- Open Claude Code in the project folder. Run `/sovsetup`.
- `/sovsetup` detects the case (empty, existing code, foreign docs, already managed) and runs the matching dialogue.
- For empty folders: scaffolds spine docs and walks four prompts (product overview, UX principles, core functionalities, first batch sketch).
- Claude writes directly to UX.md during setup (planning phase — docs are open). The no-coder converts the first-batch sketch into a build batch with a `Serves UX.md:` line.
- Run `/sovrecap` to review the batch's file list and test plan, then `/sovbuild` to lock and build. When done, `/sovclose` handles quality gates and record-keeping, then `/sovgit` walks you through commit/tag/push.

## Managing the plugin

Once installed, the plugin fires in every folder.

### Disabling in a specific project

**Desktop app:** **Customise** → **Plugins** → gear icon → toggle off. Sticks for that folder.

**CLI:** `/plugin disable no-code-method@sovereign-implementer` or interactive `/plugin` → **Installed** → select → **Disable**. Run `/reload-plugins` afterward.

### Re-enabling

**Desktop app:** **Customise** → **Plugins** → toggle back on.

**CLI:** `/plugin enable no-code-method@sovereign-implementer`. Run `/reload-plugins`.

### Uninstalling

**Desktop app:**
1. Click **Customise**.
2. Click **Browse plugins**.
3. Click **Code**.
4. Click the gear icon on the Sovereign Implementer card.
5. Click **Uninstall**.

**CLI:**
```
/plugin uninstall no-code-method@sovereign-implementer
```

### For `--plugin-dir` sessions

Only loaded for that session. Close and start without the flag.

### Known platform issues

- **Disabled plugins may still run hooks** ([#39307](https://github.com/anthropics/claude-code/issues/39307)). Uninstall instead of disabling.
- **`enabledPlugins: false` in settings.json may be ignored** ([#28554](https://github.com/anthropics/claude-code/issues/28554)). Use `/plugin disable` or the desktop app toggle.

## Guardrail docs

After `/sovsetup`, CLAUDE.md sits at the project root and everything else lives inside `_method/`:

- **CLAUDE.md** (project root) — entry point. Product overview (what the product is, who it's for, what friction it solves, milestones) plus JSON path block telling Claude where docs live. Read every session.
- **_method/UX.md** — user-facing app description. Every entry corresponds to something experienceable + a "the user needs this because…" rationale. Source of truth — Claude cannot edit; no-coder maintains by hand during planning.
- **_method/BACKLOG/** — deferred work. Per-batch files only (e.g. `0001-add-today-screen.md`) with scope-context and build-operations regions. The four index sections (Red flags, Planning batches, Build batches reference list, Open questions) live in `_method/proxies/backlog.md`. Reordering = moving lines in the proxy, not renaming files.
- **_method/MANIFEST.md** — flat alphabetical glossary of named codebase elements. Each entry: name + file path + description + one-line rationale (why it exists). Maintained by Claude during builds. Serves two audiences: the user (lookup reference) and Claude itself (recalls why a component was built so it can explain decisions and update UX accurately without scanning the build log). The path field anchors a read-before-edit gate.
- **_method/test-log/** — per-session test files. Row-per-test record with 10 columns (# / Date / Session / Component / Test Description / Type / Verifier / Status / Confirmed Explicitly / Notes). After a build, Claude writes a per-session file, runs automatable tests, leaves user-verified rows for planning read-back. Index lives at `_method/proxies/test-log.md`. Rows pruned when their component leaves MANIFEST.
- **_method/build-log/** — per-build narrative files. What shipped / Decisions / Pivots / Carried forward / Performance. Index lives at `_method/proxies/build-log.md`. Queryable via grep across builds.

`/sovsetup` also creates inside `_method/`:
- **_method/planning/drafts/** — holding area for content not yet ready for a specific doc.
- **_method/research/** — findings from Claude's research. Zero maintenance. Persists for future sessions.
- **_method/proxies/** — index and summary files. `backlog.md`, `build-log.md`, and `test-log.md` are operational indexes (directly edited). `ux.md`, `manifest.md`, `research.md` are summaries regenerated for context efficiency.

Projects can declare additional source-of-truth docs (e.g. `SYSTEM-PROMPT.md`, `COPY.md`, `PATTERNS.md`) — same locking rules as UX.md.

## The session shape

Two phases loop: **planning** and **build**. `/clear` or new session separates them.

**Planning sessions** decide what gets built. Invoke `/sovplan` to start one. The planning procedure: closes the previous test session (per-row read-back), runs five drift checks, scans Open questions, sorts ideas into Suggestions (in scope) and Discoveries (out of scope), and edits BACKLOG directly. Source-of-truth docs (UX.md, additional docs) are directly editable by Claude during planning — no ceremony needed. The no-coder removes resolved batches and reorganises priorities. When batches are added or reordered, a batch-ordering audit checks dependency flow, stale references, and security prioritization.

**Build sessions** ship engineering work. `/sovrecap` reviews the batch (validates Serves line, populates Inputs/Files/Tests, proposes splits if needed). `/sovbuild` locks the batch and runs the build against the file list. PreToolUse enforces batch boundaries. When done, the user invokes `/sovclose` — which updates MANIFEST, checks spine docs for stale references, opens the test session, runs Claude-automatable tests, generates a recap, writes the build-log entry, sweeps for unrouted ideas, runs any project-specific close steps from CLAUDE.md's `## After-build steps` section, verifies all steps via a pre-commit checkpoint, and nudges `/sovgit`. `/sovgit` walks the user through commit, tag, and push in plain English.

The no-coder `/clear`s, refreshes, and tests. Two options: invoke `/sovtest` for a guided walkthrough of each pending User-verified row (step-by-step instructions, outcome recording, failure debugging), or test independently and bring per-row outcomes to the next planning session.

**Sessions are stateless; the docs are the memory.** BACKLOG, MANIFEST, TEST-LOG, build-log tell each session where things stand. Nothing carries from in-memory state.

## The method absorbs mid-stream ideation

Ideas arrive mid-stream — tests, conversations, feedback. The planning phase catches and routes them. But catching alone isn't enough; scoping matters. A batch that says only "add dark mode" gives no testing anchor, no record of purpose, no surface for pushback.

Every batch gets the same structure: Goal (why), Outputs (what changes), Success criteria (how to know it worked), plus conditional Decisions/Dependencies/Red flags. Written during planning — the no-coder speaks the substance, Claude records it. By build time, the batch carries its own context.

## Anatomy of a batch

Two regions: **scope context** (strategic) and **build operations** (tactical).

**Status tracking.** An optional `Status:` line at the top of the batch body tracks lifecycle state: `queued` (default — absent means queued), `active` (locked by `/sovbuild`), `parked` (paused by planning), `shipped` (completed by `/sovclose`). The parser skips shipped and parked batches. State machine: `queued → active → shipped`, with `active ↔ parked` via planning.

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

Empty folder → `/sovsetup` → four prompts:
1. **Product overview.** What the product does, who it's for, what makes it distinct or what tension it solves, and milestones.
2. **UX principles.** For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*.
3. **Core functionalities.** Three to five features with "user needs this because…" lines.
4. **First batch sketch.** Smallest end-to-end buildable thing.

Claude writes the overview to CLAUDE.md and the project context to UX.md (planning phase — docs are open). No-coder seeds the first build batch.

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

## The `[SECURITY]` marker

Entries that touch sensitive surfaces — authentication, PII, payments, deletion, access control — carry an inline `[SECURITY]` tag on their heading. Applies to UX.md entries, BACKLOG build batches, planning batches, and open questions. Not enforced by hooks — informational only. Two audiences: the user sees it when reviewing their spec; Claude uses it to bias security-shaped work earlier in the queue during batch ordering.

## Four test types and the Claude/user split

- **Look and click** — UI interaction. Structural checks → Claude; judgement → user.
- **Run and read** — command execution. Fully automatable.
- **Trigger and observe** — event-driven. Fully automatable.
- **Generate and inspect** — artefact production. Fully automatable.

Verifier is per-row, not per-type. Both Claude and user rows can exist across any type. All must reach `Confirmed Explicitly: Yes` before the next build.

## The safety net

When a session opens, **SessionStart** checks adopted vs. unadopted. Unadopted folders with substantial work trigger an advisory pointing at `/sovsetup`.

Until `/sovsetup` runs, **PreToolUse** blocks Edit/Write/MultiEdit calls. In unadopted folders, the deny message says "run `/sovsetup` first" — not "describe it in a BACKLOG batch," which would be meaningless before the project is set up.

`/sovsetup` branches: empty folder → scaffold + four prompts; existing code, no docs → scaffold alongside; foreign docs → migrate/overwrite/leave; already managed → refresh footers + migrations.

Nothing destructive without confirmation; every destructive option backs up first.

### Parent-directory placement

Claude Code inherits CLAUDE.md files from parent directories. If a project folder sits inside another project's tree, the parent's instructions will affect the session — potentially poisoning Claude's behaviour with rules meant for a different project.

**SessionStart** detects CLAUDE.md files in parent directories and surfaces a warning. The warning fires in all tiers (empty, partial, complete, unadopted).

**Best practice:** keep project folders at independent locations (e.g. `Desktop/MyApp/`, not `Desktop/OtherProject/MyApp/`). If nesting is unavoidable, the warning tells the user to consider relocating.

## Research search flow

Claude watches for moments where a decision would benefit from external information — API capabilities, library comparisons, platform constraints. When it spots one, it drafts a search query, proposes it to you, and waits for approval before executing.

**`/sovresearch`** triggers the flow explicitly. Claude also suggests searches proactively when it recognises an information gap.

**Three execution mechanisms**, in priority order:
1. **MCP search tool** — if a Gemini search MCP server (e.g. `yukukotani/mcp-gemini-google-search`) is installed. Preferred.
2. **WebSearch** — Claude's built-in search tool, when MCP is unavailable.
3. **Copyable prompt** — a formatted query for the user to paste into Gemini, ChatGPT, Perplexity, or another research environment. When neither tool is available.

**Query files** are saved to `research/search-queries/YYYY-MM-DD-topic-slug.md` — structured records with trigger, decision it informs, query, good-answer criteria, response, and outcome. Distinct from free-form `research/<topic>.md` files.

**MCP server setup** (optional — the fallback paths work without it):
1. Install `yukukotani/mcp-gemini-google-search` (or another MCP server exposing a search tool).
2. Get a Gemini API key from Google AI Studio.
3. Set the environment variable `GEMINI_API_KEY` with your key.
4. Register the MCP server in Claude Code's settings.

The plugin doesn't ship or store API keys — the user brings their own.

## What's inside the plugin

- **Hooks** (Python, deterministic enforcement): SessionStart detects folder state, injects behavioural rules, and mandates a user-facing status summary (batch counts, next batch, top 3 queued batches, pending tests, unclosed builds). PreToolUse enforces edit boundaries (project-boundary, locked docs, batch file list, test gate, adoption gate, read-before-edit, Serves-line check, destructive git guard, Bash/PowerShell write-guard). PostToolUse validates structured doc format after edits (BACKLOG parse, scope-context, TEST-LOG columns, build-log sections, proxy headers). PreCompact blocks compaction mid-build (recommends handoff). UserPromptSubmit classifies first prompt + injects routing hint.
- **Procedure docs** (read into main context on demand): planning, before-build (invoked via `/sovrecap`), build (invoked via `/sovbuild`), close, git, setup. Each specifies what to load and what to do. Claude follows them in the main conversation — no separate agent contexts.
- **Slash commands** (`/sovsetup`, `/sovplan`, `/sovrecap`, `/sovbuild`, `/sovclose`, `/sovgit`, `/sovtest`, `/sovresearch`, `/sovtersify`): user-facing entry points that direct Claude to the matching procedure doc or flow.
- **Templates**: starter shapes for spine docs.
- **Bundled docs** (`DOC-STRUCTURE.md`, `VOCABULARY.md`): read by procedure docs via `${CLAUDE_PLUGIN_ROOT}/docs/`.

Hooks (deterministic) handle correctness; procedure docs (probabilistic) handle judgment.

## Two layers of permission

Claude Code's permission modes (Ask/Accept/Plan/Auto/Bypass) control whether the no-coder gets prompted. The plugin's PreToolUse hooks decide whether Claude is allowed to act at all — firing in every mode, including Bypass.

Every deny is prefixed `[No-code method]` with a `What to do:` line.

### Which mode for which phase

| Phase | Mode | Why |
|---|---|---|
| Planning | Accept edits | Planning procedure edits BACKLOG. |
| Recap (`/sovrecap`) | Accept edits | Writes Files: into BACKLOG. |
| Build (`/sovbuild`) | Auto | Locks batch, source-file edits. Hooks enforce boundaries. |
| Close (`/sovclose`) | Auto | Writes MANIFEST, test-log, build-log. |
| Git (`/sovgit`) | Auto | Commits and pushes. |
| Pre-method ideation | Plan mode | No edits needed yet. |

### Permission prompts

Claude Code may prompt for permission on tool calls depending on your mode setting. Auto mode produces the fewest prompts. `/fewer-permission-prompts` helps reduce main-conversation prompts.

## What's editable

Three layers:

**Method contract — edit at peril.** Rules the machinery depends on. Push-back-rather-than-agree drives drift checks. No-stealth-fix drives the recap. Batch-scope-locking drives clean test coverage. Each annotated with what breaks without it.

**Recommended habits — edit freely.** `/clear` cadence, test-prep workflow, commit timing.

**The build sequence — fixed.** Four-phase cycle is the spine.

### Editing surfaces — phase-aware

Permissions flip based on project phase:

| Doc | Planning phase | Build phase |
|---|---|---|
| `UX.md` | **read/write** | **locked** |
| Additional source-of-truth docs | **read/write** | **locked** |
| `BACKLOG.md` | read/write | read/write |
| `MANIFEST.md` | read/write | read/write |
| `test-log/` | read/write | read/write |
| `CLAUDE.md` | read/write | read/write |
| Source code files | **locked** | batch file list only |
| `research/` files | read/write | read/write |

**Phase detection.** Planning = no `Status: active` batch in BACKLOG. Build = active batch present (written by `/sovbuild`).

**During planning,** Claude edits source-of-truth docs directly — no ceremony needed.

**During build,** the `[PROPOSED EDIT PENDING]` mechanism applies: Claude queues content in the destination doc's `## Proposed edits pending` section. The no-coder applies it next planning session.

**Footer exception.** Footer stamps are metadata — PreToolUse allows footer-only edits on locked docs regardless of phase.

## Why the rules

**Push back rather than agree.** Drift checks and red-flag surfacing assume pushback. Agreement-by-default disables safety nets.

**State regressions plainly.** The recap is the no-coder's record. Stealth-fixes break it.

**Lock batch scope once agreed.** Protects session predictability, clean test coverage, and the planning-gate filter.

**Five drift checks at different levels.** File-temporal, feature-to-feature, name-to-name, purpose-level, per-row code-touch. Bundling produces noise; separate passes catch what each is designed for.

**Lock source-of-truth docs.** Build sessions are the wrong environment for design changes. Planning sessions give decisions proper deliberation.

**No placeholders in source-of-truth docs.** Runtime audiences need the instruction, not its status.

**Project-specific UX principles.** Generic principles are too abstract to guard decisions.

**MANIFEST starts flat.** Most projects never need sections. Pre-sectioning forces premature architecture decisions.

**BACKLOG is a folder, not four files.** `proxies/backlog.md` = one place for what's outstanding. Per-batch files = content volume. Split is content-volume, not category.

**Risk accepted as a labelled line.** Keeps the trade-off on the page for re-litigation.

**Per-row read-back.** Bulk confirmations silently flip rows the user didn't actually verify.

## What this costs

A new feature takes two sessions minimum — one planning, one build. Every shipped feature traces to a written rationale; nothing gets built that no one decided to build.

As docs grow, they consume more of Claude's context window — leaving less room for actual work. `/sovtersify` runs a guided compression pass: triage docs by size, flag wrong-home content and verbose prose, then audit and compress user-selected targets one at a time. Planning phase only.

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
*No-code method — Version 86.*
