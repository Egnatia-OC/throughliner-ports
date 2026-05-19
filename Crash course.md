# Crash course

*A short structural walk-through.*

## What this is

A structured set of markdown documents that tell Claude Code how to work on a project. Designed for non-coders using Claude as the implementer, who need structure to keep the project from drifting.

The method belongs to the spec-driven development family. Closest neighbour: Cline's Memory Bank — same shape (markdown files as project memory and behavioural guardrails, read at session start), different cut of files, different audience.

## The files

**Per-project (one of each):**

- **CLAUDE.md** — Entry point. Pointer to the method spec, a path block declaring where every other doc lives, and any project-specific behavioural notes.
- **UX.md** — User-facing description of the app. Every entry corresponds to something the user can experience in the current build, plus a mandatory "the user needs this because…" line tying it back to a UX principle or user context.
- **BACKLOG.md** — Deferred work in four fixed-order sections: Red flags (security/privacy/data integrity), Fold-ins pending (source-of-truth content Claude queues for the user to fold in by hand next planning session), Planning batches (open questions blocking a build batch), Build batches (engineering work, top-to-bottom by priority).
- **MANIFEST.md** — Flat alphabetical glossary of named codebase elements the user might want to look up. Maintained by Claude during builds; not read cover-to-cover.
- **TEST-LOG.md** — Row-per-test record of every shipped batch's outcomes. Eight columns: # / Date / Session / Component / Test Description / Status / Confirmed Explicitly / User Notes. Claude adds blank-Status rows when a batch ships; the user confirms per-row in planning via the test-session-close read-back. The test-confirmation gate (see *Four disciplines* below) is what makes the record trustworthy.
- **Optional additional source-of-truth docs** — For projects needing an extra doc the spine doesn't cover (e.g. `SYSTEM-PROMPT.md` for an MCP-integrated app, `COPY.md` where user-facing text is the deliverable). Same rules: read-only to Claude (the agent), no placeholders, intent-level not implementation.

**Method-side (shared verbatim across every project):**

- **NO-CODE-METHOD.md** — The method spec: behavioural rules, flag taxonomy, build sequence.
- **DOC-STRUCTURE.md** — Structural specs for spine docs and additional source-of-truth docs. Reference material — read when writing or migrating a doc, not every session.

**Templates** — Starter shapes for `UX.md`, `BACKLOG.md`, `MANIFEST.md`, the project's `CLAUDE.md`, and any additional source-of-truth doc.

## The session shape

Every session under the method follows the same shape:

**At session start.** Claude reads `CLAUDE.md`, resolves the path block, reads the spine docs and any additional source-of-truth docs. If a path doesn't resolve, Claude searches by name, surfaces what it finds, and asks before updating `CLAUDE.md`.

**During planning.** Main Claude classifies the opener (test notes / feature request / scope question / mixed) and hands off to the **planning subagent** — a focused Claude with its own system prompt for the planning flow. The subagent sorts the opener into Suggestions (in scope) and Discoveries (out of scope until `UX.md` is updated), checks drift between `UX.md`, `MANIFEST.md`, and the codebase (every planning session; the only skip case is "nothing built yet"), and edits `BACKLOG.md` directly. Discoveries become planning batches before session end so nothing slips through `/clear`. The subagent hands a recap to main Claude, who relays it.

**Before build.** The user runs `/before-build` and the **before-build subagent** locks the next batch. Changes are grouped into batches sized by verification burden — small enough that one session's testing covers them (per the *Batch-sizing principle* in `NO-CODE-METHOD.md`). The subagent writes a `Files:` sub-section listing every file the batch will modify; that list becomes the build-time boundary the PreToolUse hook enforces.

**During build.** The user runs `/build` and the **batch-executor subagent** runs one batch in fresh context — reading the `Files:` list, editing each file, ticking as it goes. `UX.md` and any additional source-of-truth docs are read-only to Claude (full rule in *Editing surfaces* below). Any user-facing change Claude notices is flagged at the end of the response, not edited in. If implementation reveals a needed change outside the batch — a prerequisite or a re-batching trigger — the subagent halts and asks before proceeding (the two carve-outs under *Prohibited of Claude* in `NO-CODE-METHOD.md`). When the last file ticks, batch-executor ends with a brief completion note. The Stop hook routes to the **after-build subagent** (or back to batch-executor for the next batch if a fresh planning session ran in between).

**After build.** The after-build subagent updates `MANIFEST.md` for anything created/renamed/deleted (silently, fully automatic), produces the plain-English build recap ("I am adding a check to the age field so people can't enter negative numbers") with `[Requested]` / `[Suggested]` labels read off the `BACKLOG.md` change list, and opens the test session by appending one blank-`Status` row to `TEST-LOG.md` per user-observable behaviour the recap names. Main Claude relays the recap. The user is prompted to refresh, test, and bring per-row outcomes to the next planning session, where the planning subagent walks the read-back row by row.

## Where each phase fits

This method runs in Claude Code throughout. Within Claude Code, work happens in two phases:

- **Planning** — design and decide. Big-picture decisions, source-of-truth doc edits, drift checks, `BACKLOG.md` maintenance. The user edits `UX.md` and any additional source-of-truth docs by hand here; Claude (the agent) assists in chat but cannot write to those docs directly.
- **Build** — Claude implements one batch at a time. Source-of-truth docs are locked from Claude; operational docs (`BACKLOG.md`, `MANIFEST.md`) stay read/write because builds need to update them. By-hand edits to source-of-truth docs are reserved for planning sessions, keeping build scope clean.

The lock convention is in *Editing surfaces* below.

## Four disciplines that do most of the work

**The "the user needs this because…" line.** Required for every `UX.md` entry. Forces rationale articulation before implementation. Protects against feature drift. Makes scope decisions easier.

**The flag taxonomy.** Three buckets with three different homes. *Red flags* (security, privacy, data integrity, safety) go into `BACKLOG.md` and stay until addressed. *Suggestions* (improvement that fits current scope) go in chat at end of response. *Discoveries* (out-of-scope ideas) become planning batches in `BACKLOG.md` before session end. Every concern has exactly one place to live.

**The pipeline for new features.** A new feature can't enter a build batch directly. It must enter as a planning batch in `BACKLOG.md`, get answered in a planning session, become or update a `UX.md` entry, and only then enter as a build batch. Rigid by design. Claude proposing a build batch with no matching `UX.md` entry is a flag that something's been skipped.

**The test-confirmation gate.** A new build batch cannot start while any row in `TEST-LOG.md` from the previous batch is unconfirmed. Confirmation happens per-row, by name, in the planning session after the test-session was opened by the after-build subagent — bulk confirmations don't count. Five protocol rules (in `NO-CODE-METHOD.md`) make this concrete: never infer completion, resolve "all others good" before recording, no new build until the test session is closed, Skipped ≠ Passed, retest after change. Two hooks make it load-bearing: a PreToolUse hook denies any `Task` invocation of batch-executor while pending rows exist, and the SessionStart hook injects a routing override that steers any session opening with pending rows straight to the planning subagent's read-back, regardless of what the user asks. The subagent walks the user through; the record stays trustworthy because no row gets a positive outcome by accident or drift.

## The safety net — installing on a folder that isn't empty

The method assumes a fresh project. Sooner or later someone installs the plugin into a folder that isn't fresh — by mistake, or because they want to bring an existing project under the method's discipline. The safety net is the plugin's response.

When a session opens, **SessionStart** checks whether the folder is *adopted* (carries the method footer in `CLAUDE.md`) or *unadopted*. Adopted folders, genuinely empty folders, and folders carrying a `.no-code-method-skip` opt-out marker stay silent. An unadopted folder with substantial existing work — code, foreign docs, anything — triggers an advisory pointing at the `/adopt` command.

Until `/adopt` runs, **PreToolUse** denies Edit, Write, MultiEdit, and method-subagent calls from main Claude. Not just a warning — an actual block. `/adopt`'s own scaffolding calls pass through, so adoption can happen while the gate is closed against everything else.

`/adopt` branches on what it finds:

- *Empty folder* → walks the four new-project prompts and scaffolds the spine docs with your answers folded in.
- *Existing code, no docs* → offers to scaffold fresh docs alongside, or to opt out via `.no-code-method-skip`.
- *Existing code, foreign docs* (most commonly: Claude Code's built-in `/init` ran first) → offers to migrate the existing `CLAUDE.md` to method spec, overwrite with backup, or leave alone via the opt-out marker.
- *Already method-managed* → detects template state, surfaces any version mismatch, offers a footer refresh or cancel.
- *Opted out* → folder previously chose `.no-code-method-skip`; offers to clear the marker (returning to unadopted) or to stay opted out.

Nothing destructive happens without explicit confirmation, and every destructive option backs up first.

Why session-start, not install-time? Claude Code's plugin system has no install-time hook the plugin can run code from. The earliest the plugin can act is when a Claude Code session opens in a folder. By the time you could ask Claude to write a file, the gate has already fired.

## A walkthrough — a first project from scratch

This section follows a small project — a task manager called **Taskflow**, designed for users with executive dysfunction — through new-project setup, first planning, first build, and the first test note. Meant to make the rules in `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` feel concrete before reading them as rules.

### Day one — starting from scratch

You open a Claude Code session in an empty project folder and run `/adopt`. Empty folder means no advisory — `/adopt` detects the empty case and walks you through four prompts:

1. **Project context.** What the app does, and what makes it distinct.
2. **UX principles.** Three to six. For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*. Each gets a one-line claim plus a few sentences of why.
3. **Core functionalities — first pass.** Three to five features that make this app what it is. Each gets a paragraph plus the *user needs this because…* line.
4. **First build batch sketch.** The smallest end-to-end thing you can build and test.

Take the time you need — these are the decisions the rest of the project is built on. Claude queues your answers as a `[FOLD-IN PENDING]` block in `BACKLOG.md`. You fold the UX content into `UX.md` by hand during the same planning session and convert the first-build sketch into a proper build batch.

Once the docs are seeded, Claude Code is ready for the first build.

### A first UX entry — Risk accepted in action

One of Taskflow's first functionalities is **One-day-at-a-time view**: the Today screen shows only today's tasks. No week view, no agenda. The entry's *user needs this because…* line ties straight back to *Reduce planning pressure*:

> Looking ahead at a wall of upcoming tasks is the planning-pressure that triggers shutdown for users with executive dysfunction. Seeing only today's load keeps the cognitive surface area small and the bar for getting started low.

The entry ends with a **Risk accepted** line:

> Users cannot plan around upcoming busy periods or anticipate scheduling conflicts. We've judged this an acceptable cost — the people this app is for are already overwhelmed by ahead-planning; protecting the present is more important than enabling the future.

The Risk accepted line is for the future-self who, six months in, wonders why the app deliberately omits a week view. The trade-off is on the page; it doesn't have to be re-derived.

### First build, first test note

The first build batch ships — an empty Today screen, a way to add a task. You `/clear`, refresh, test, and write notes:

> *"Added a task fine. Couldn't find anywhere to set a due date — is that intentional? The screen is hard to read at night — dark mode would help."*

You paste the notes into a new Claude Code session. Claude takes the test-notes route into planning.

### How a test note becomes a feature — the five-step pipeline

Take the dark-mode item:

1. **Idea raised.** Test note → dark-mode request.
2. **Planning batch.** Claude adds a planning batch in `BACKLOG.md` named *Dark mode* with the questions to answer: *Is this app used at night frequently enough to justify maintaining a parallel theme? Follow OS setting or have its own toggle? Which existing UX entries assume light-background contrast and would need revisiting?* Closes with `Blocks: scope decision — no build batch yet.`
3. **Planning session.** You and Claude answer. Suppose: yes, follow OS setting, two existing UX entries need a contrast pass.
4. **`UX.md` updated.** A new *Dark mode* entry is added with the *user needs this because…* line. The two affected entries get a quick revisit.
5. **Build batch.** A build batch enters `BACKLOG.md` ending with `Serves UX.md: Dark mode (and the two reviewed entries).`

If step 3 had answered "no," steps 4 and 5 wouldn't happen. `UX.md` stays as it was, the planning batch is removed as resolved, no build batch is ever created. That's the short-circuit case — and it's just as valid an outcome as "yes, build it."

The due-date item runs the same pipeline. It might land at "yes, with relative shortcuts only, no date picker" — folding into a new `UX.md` entry once decided, then a build batch.

**What if the idea conflicts with an existing UX principle?** If a test note or feature request would violate a principle already in `UX.md`, that conflict gets surfaced in chat as the first response — not quietly routed into a planning batch and hoped for. The planning batch still happens (step 2), and the conflict becomes one of its questions. Chat surfaces the tension immediately so you can react; the planning batch records and resolves it.

### Drift checks at planning sessions

By the third or fourth build, Claude is running **drift checks** at the start of every planning session. Four checks — three pairwise comparisons plus one code-touch judgement:

- **`UX.md` ↔ what's actually built.** `UX.md` describes a "drag to reorder" gesture, but the build only supports tap-and-arrows — flag the entry as describing a non-existent feature. Or the build has a swipe-to-archive behaviour no `UX.md` entry covers — that's a Discovery.
- **`MANIFEST.md` ↔ the codebase.** `MANIFEST.md` still says `TaskCard`, but the last build renamed it `TaskTile` — update the entry. A new service was added with no `MANIFEST.md` entry — add one.
- **`MANIFEST.md` ↔ `UX.md` (loose check).** `MANIFEST.md` lists a `WeeklyDigestEmailer`, but no `UX.md` entry mentions email digests — either there's a hidden feature (Discovery) or it's dead code (delete). Database config and logging middleware are exempt; they don't trace to user-facing intent by design.
- **`TEST-LOG.md` ↔ what's been touched (Rule 5 — retest after change).** For each `TEST-LOG.md` row with `Status: Pass` and `Confirmed Explicitly: Yes`, judge whether the component it tested has been substantially changed since the row's `Date`. A row from v23 testing a touch handler whose code was edited in v26 — flag for retest. Trivial changes (comments, formatting, unrelated refactors in the same file) don't count. Produce a brief reasoning trail per flagged row so the call is auditable.

The drift check isn't exhaustive. It catches cases where docs and code have started disagreeing, before that gap turns into a wrong-feature build.

### What this all costs

A new feature takes two sessions to land — one planning, one build — minimum. The pipeline is rigid by design. What the discipline buys: every shipped feature traces to a written user-need rationale; nothing gets built that no one decided to build; and at any moment you can ask *why is this here?* and the answer is on a page you can open.

## What's editable, what's not

The method ships with a default set of preferences and commitments embedded in `NO-CODE-METHOD.md`. A new user needs to distinguish three layers:

**Method contract — load-bearing, edit at your peril.** Some lines read like personal preferences but the method's machinery depends on them. "I'd rather be told I'm wrong than agreed with" — the drift checks, red-flag surfacing, and planning recaps all assume Claude will push back. "Don't stealth-fix regressions" — the build recap assumes Claude states regressions plainly. "Don't immediately fold under push-back" — planning recaps assume Claude engages with disagreement rather than collapsing into either position. "Walkthroughs one step at a time; alternatives all at once" — multi-step procedures lose usability when bundled, alternative-presentation loses comparison context when sequenced. In `NO-CODE-METHOD.md` the contract is structured as *Required of Claude* (positive lines like the four above) and *Prohibited of Claude* (negative lines — "do not add features not listed in the current batch prompt," "do not refactor without explicit confirmation"), each annotated with the mechanism that breaks without it.

**Recommended habits — edit freely.** Some lines are habits surrounding the build sequence: `/clear` after each build, prepare test results as pasteable text, review all upcoming changes before each build. A different user with a different rhythm might rewrite these.

**The build sequence — fixed, not advisable to personalise.** The four-phase cycle (session start → planning → before build → after build) is the method's spine. Not part of the editable surface.

Each layer has its own section in `NO-CODE-METHOD.md`: *Method contract* (with the Required-of-Claude / Prohibited-of-Claude split), *Recommended habits*, and *The build sequence*.

## Editing surfaces

The point of locking is to keep `UX.md` as a stable source of truth that doesn't get edited in flight; structural changes only happen in planning sessions, where they're discussed and decided properly.

Some docs are stable artefacts — written slowly, deliberately, meant to stay stable. `UX.md` and any additional source-of-truth docs are written in planning sessions, where their design decisions get the time they deserve. The user edits these by hand; Claude (the agent) cannot. `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` are the method spec — updated in the method's own development project, then shared verbatim across every project using it.

Build sessions are different: short, `/clear`-bounded, build-focused. The wrong environment for stable docs to drift via small "clarifying" tidy-ups. So those docs are locked from Claude — read-only, enforced by the PreToolUse hook. If Claude thinks one should be reworded or reorganised, it tells you in chat instead of editing.

The full split:

| Doc | Claude (the agent) edit access |
|---|---|
| `UX.md` | **read-only** (user edits by hand during planning) |
| Additional source-of-truth docs (`SYSTEM-PROMPT.md`, `COPY.md`, etc.) | **read-only** (user edits by hand during planning) |
| `BACKLOG.md` | read/write |
| `MANIFEST.md` | read/write |
| `CLAUDE.md` | read/write |
| `NO-CODE-METHOD.md` | read (method spec, edited in the method's own dev project) |
| `DOC-STRUCTURE.md` | read (method spec, edited in the method's own dev project) |

**`BACKLOG.md` is read/write to Claude** because builds need it (red flags added, completed batches removed, batches split or reordered). The protective rule is built into the build sequence: Claude must discuss every `BACKLOG.md` change with you at the appropriate stage — never silently. The recap rules (after planning, before build, after build) make this explicit.

**`NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` are read-only across the board** in your project — shared verbatim across every project using the method, so editing them in your project would diverge from the verbatim copy. They get updated in the method's own development project.

**The `[FOLD-IN PENDING]` mechanism.** Claude can't write directly into read-only source-of-truth docs like `UX.md`. Instead, proposed content is queued as a `[FOLD-IN PENDING]` block in a dedicated *Fold-ins pending* section of `BACKLOG.md`. The block names the destination doc, the proposed change, and where the content came from — a planning-batch resolution, `/adopt` (during empty-folder scaffold or foreign-doc migration), or a mid-build edit attempt the PreToolUse hook intercepted. During the next planning session, you review pending blocks and fold them into the destination doc by hand (or drop them). Canonical block format and section ordering: `DOC-STRUCTURE.md` → *BACKLOG.md structure*.

## Why the rules

The rationale behind specific rules in `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` — the *why* that doesn't fit in a tight operational rule. Organised in the order the rules appear.

### From NO-CODE-METHOD.md

**Push-back without folding.** The rule "if I push back on a suggestion, don't immediately fold and don't immediately dig in" is load-bearing for planning recaps. A recap that mirrors whatever the user last said is only useful if Claude has actually engaged with any disagreement before recording the outcome. Capitulating without engagement and refusing to listen are mirror failures: both bypass a conversation that would decide whether a suggestion was right. (See *What's editable, what's not* for why this is method contract, not personal preference.)

**No stealth-fixing.** The rule "if a build fails or causes a regression, state it plainly rather than silently fixing it" is load-bearing for the build recap. The recap is the user's primary record of what happened in a build session, used to decide whether to test, push back, or accept. A stealth-fix breaks that record — the regression survives invisibly until it resurfaces later with no breadcrumbs back to its origin. Plain statements keep the recap a reliable trail.

**Why batch scope is locked.** Mid-build scope additions cost three things the method protects:

- **Predictability of session length.** A batch with a fixed file list has a knowable end; one that absorbs "while we're here" additions doesn't.
- **Clean test coverage.** One batch = one set of changes = one set of tests; mid-build mixing makes regressions harder to trace.
- **The planning-gate filter.** Mid-build, things *feel* in-scope that wouldn't survive a planning conversation. The rule defers scope decisions back to that conversation rather than shortcutting it.

The rule isn't absolute. If implementation reveals a prerequisite the batch genuinely cannot complete without — something invisible at planning time — the carve-out is: halt, surface in chat with a one-line justification, wait for the user's okay, label `[Prerequisite, not in plan]` in the build recap. The bar is high ("cannot complete," not "would be nicer") and the protocol is no-silent-prerequisites; both keep the carve-out from becoming a back door for the scope creep the rest of the rule blocks.

**The drift checks at different abstraction levels.** The four drift checks (`UX.md`↔build, `MANIFEST.md`↔code, `MANIFEST.md`↔`UX.md`, `TEST-LOG.md`↔what's-been-touched) operate at different abstraction levels — feature-to-feature, name-to-name, loose user-facing-purpose, and per-row code-touch with reasoning trail. Doing all four at once mixes the levels and produces noise. Run them as four separate passes.

**Editing surfaces — why some docs are locked to Claude.** Full reasoning in *Editing surfaces* above.

### From DOC-STRUCTURE.md

**No placeholders, no soft gestures.** Source-of-truth docs are operational — runtime audiences (Claude, your future self, anyone reading to remember what was decided) need the instruction, not its implementation status. A line that says "currently undecided" forces the reader elsewhere for the actual rule and makes the doc inert until that elsewhere is found. The status of an open question lives in `BACKLOG.md`, not in the doc body.

**Additional source-of-truth doc shape — loose by design.** Different projects need different additional docs (a system-prompt doc, a copy doc, something else) and the shape that works for one won't work for another. The structural rules — locked to Claude, no placeholders, intent-level, fold-in target — are what's invariant. The shape inside is the project's call.

**UX principles are project-specific.** A budgeting app's principles ("never let the user lose data they've entered") look nothing like a task manager's ("reduce planning pressure"). Principles that try to be method-wide become so abstract they stop guarding any actual decision. The job is to write the three-to-six that protect *this* project's design from drift, not to compile a general theory of UX.

**The "user needs this because…" line.** See *Four disciplines* above.

**Risk accepted — keeping the trade-off visible.** Without an explicit *Risk accepted* line, the cost of a deliberate simplification fades from view. Six months later, someone (often the same person who chose the simplification) wonders why the app deliberately omits a feature and considers adding it — without remembering why it was omitted. The *Risk accepted* line keeps the trade-off on the page so any re-litigation happens with the original reasoning in view.

**`MANIFEST.md` flat list — don't pre-empt the section split.** The rule "switch to alphabetical sections by area when the flat list grows too long" sounds like permission to start with sections from day one. It's not. Most projects' `MANIFEST.md` never grows large enough to need sections, and pre-emptive sectioning forces architecture decisions (which "areas" exist?) before there's enough code to know. Wait until scrolling the flat list actually hurts.

**`BACKLOG.md` as one file with four sections.** Red flags, fold-ins pending, planning batches, and build batches could live in four separate files. They don't, because the friction of multiple places to check is what causes deferred items to slip through. One file, four sections, top-to-bottom by priority means there's exactly one place to look for what's outstanding.

## Where the method sits in the broader landscape

If you've used Cline's Memory Bank, this will feel familiar — multiple structured markdown files governing AI behaviour, read at session start, with a workflow that loops planning and building. Memory Bank's cut: `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`. This method's cut: `UX`, `MANIFEST`, `BACKLOG`, plus additional source-of-truth docs as needed. Different cuts of the same idea. Memory Bank is general-purpose; this method is shaped around non-coders.

In the broader spec-driven-development literature (the arXiv paper, the GitHub Spec Kit, the Augment Code guides, the DeepLearning.AI course), this method maps onto the **spec-anchored** rigour level: specs are high-quality context that drive code generation, but code remains the source of truth.

## Caveats

Iteratively developed. Has not yet been used to ship an app. The first real Taskflow build under the current version is the next test — and the most honest one.

A known headwind for any methodology relying on `CLAUDE.md`-style instructions: roughly 30% of the time, Claude won't follow them. The method designs around this by making source-of-truth docs read-only to Claude (so big design changes can't slip in mid-build) and by making most non-trivial decisions reviewable in chat. But the headwind is real, and any user should expect to recognise drift and recover from it as part of the skill.

## Where the actual files live

The current versioned method files (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, all templates) live in the `sovereign-implementer` repo on GitHub — *(replace with the real link when the repo goes public)*. From V17 onwards, versions are tracked as git tags (`v17`, `v18`, ...) — one tag per working session, full commit history walkable from any tag.

---
*No-code method — Version 29.*
