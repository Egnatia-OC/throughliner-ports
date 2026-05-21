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
3. Open a Claude Code session in the project folder you want to work in. The plugin's hooks fire at session start. If the folder is empty, or contains existing work without the method's docs, Claude Code surfaces an advisory pointing at the `/adopt` command (see *The safety net* below for what `/adopt` does in each case).

For development or one-off use, `claude --plugin-dir <path-to-clone>/plugin` loads the plugin for a single session without installing.

A first session in Sovereign Implementer is distinct from a normal build sequence session:

- Open Claude Code in the project folder. Run `/adopt`.
- `/adopt` detects which case applies — empty folder, existing code without docs, existing code with non-method docs, already method-managed, or opted out — and runs the matching dialogue.
- For an empty folder, `/adopt` scaffolds the spine docs (CLAUDE.md, UX.md, BACKLOG.md, BUILD-LOG.md, MANIFEST.md, TEST-LOG.md) and creates a `planning/drafts/` folder, then walks four prompts in order: project context, UX principles, core functionalities, and a first build batch sketch.
- The dialogue's outputs land as a `[FOLD-IN PENDING]` block in BACKLOG.md. The no-coder folds the UX content into UX.md by hand (the doc is read-only to Claude), and converts the first-build-batch sketch into a proper build batch with a `Serves UX.md:` line pointing at the entry it implements.
- After the fold-in, the project is ready for its first build. Run `/before-build` to lock the next batch, then `/build` to execute it. The plugin orchestrates the rest.

## Guardrail .md docs

Six markdown files sit in the project root once `/adopt` has scaffolded the project, plus a `planning/drafts/` folder. Each does one job, and the workflow expects a clean separation between them.

- **CLAUDE.md** — entry point. Tells Claude Code where every other doc lives via a JSON path block, and carries any project-specific behavioural notes. Read by Claude at every session start.
- **UX.md** — user-facing description of the app. Every entry corresponds to something the no-coder can experience and test in the current build, plus a mandatory "the user needs this because…" line tying the entry back to a UX principle or other user context. Source of truth — Claude cannot edit this file; the no-coder maintains it by hand during planning sessions.
- **BACKLOG.md** — deferred work, in four fixed-order sections: Red flags (security/privacy/data integrity), Fold-ins pending (source-of-truth content Claude queues for the no-coder to fold in by hand next planning session), Planning batches (open questions blocking a build batch), Build batches (engineering work, top-to-bottom by priority).
- **MANIFEST.md** — a flat alphabetical glossary of named codebase elements the no-coder might want to look up. Maintained by Claude during builds; not read cover-to-cover.
- **TEST-LOG.md** — a row-per-test record of every shipped build batch's outcomes. Eight columns: # / Date / Session / Component / Test Description / Status / Confirmed Explicitly / User Notes. Claude appends blank-Status rows when a batch ships; the no-coder confirms outcomes per-row during the next planning session.
- **BUILD-LOG.md** — a running record of decisions, changes, and reasoning for every build, newest-first. Written by Claude after each build completes. Not read cover-to-cover — search when you need the "why" behind a previous build's choices. Entry shape: What shipped / Decisions taken and why / Pivots and surprises / Carried forward.

`/adopt` also creates a `planning/drafts/` folder — a destination-agnostic holding area for substantive chat content not yet ready for a specific doc (comparison tables, structural sketches, option matrices). Drafts complement BACKLOG.md's *Fold-ins pending* section, which is for source-of-truth doc content specifically. Drafts are written when content is "good enough to walk away from" and deleted when consumed.

A project can also declare additional source-of-truth docs — for example, `SYSTEM-PROMPT.md` for a Claude/MCP integration project, or `COPY.md` for a project where the user-facing text is itself the deliverable. These get the same lock-from-Claude treatment as `UX.md`.

## The session shape

Work in this method moves through two main phases — planning and build — looping back and forth until the project is done. Each Claude Code session sits in one phase or the other; `/clear` or a new session separates them.

**Planning sessions** decide what gets built. The no-coder pastes test notes from a previous build (and/or raises new feature/s, asks a scope question, etc), and the planning subagent runs its routine: closing the previous build's test session by walking each pending TEST-LOG row one at a time; checking drift between UX.md, MANIFEST.md, and the codebase; sorting any new ideas into Suggestions (already in scope) and Discoveries (not yet in scope, need UX.md updates first); and editing BACKLOG.md directly. The conversation stays in the same chat style as ever — questions, push-back, alternatives, second thoughts all belong in there; the subagent's structure is for what gets recorded and where, not for how the conversation feels. Planning sessions are also when source-of-truth doc edits happen, by hand — the no-coder folds in any pending content from BACKLOG.md's *Fold-ins pending* section, removes resolved planning batches, and reorganises build batches if priorities have shifted.

**Build sessions** ship engineering work, one batch at a time. The no-coder runs `/before-build` and the before-build subagent locks the next batch: validates that the top batch's `Serves UX.md:` line resolves, enumerates the files the batch will modify into a `Files:` sub-section, estimates the verification burden — the list of distinct things that will need testing once the batch ships — and proposes a split if the list is long relative to scope. Once the no-coder okays the locked batch, `/build` runs the batch-executor subagent against the file list. As each file ticks, the PreToolUse hook enforces that no file outside the list gets edited. When the last file ticks, the Stop hook routes to the after-build subagent, which updates MANIFEST.md, generates a plain-English build recap, opens a test session by appending blank-Status rows to TEST-LOG.md — one per user-observable behaviour the recap names — writes a BUILD-LOG.md entry (the persistent per-build narrative), and runs a frame-correction sweep (scanning BACKLOG.md for planning batches or pending fold-ins that reference behaviour the build just changed).

The no-coder then `/clear`s, refreshes their copy of the project, and runs the tests the recap named. The outcomes (Pass / Fail / Skipped, plus notes) come back to the next planning session, which opens by reading them back row by row before any other work starts.

The two-phase loop is the spine. Everything else is detail on what happens inside one phase or the other.

## Walkthrough — Taskflow Day 1

This walkthrough follows a small project — a task manager called **Taskflow**, designed for users with executive dysfunction — through new-project setup, first planning, first build, and the first test note. The point is to make the method's discipline feel concrete.

### Day one — starting from scratch

The no-coder opens a Claude Code session in an empty project folder and runs `/adopt`. Empty folder means no advisory — `/adopt` detects the empty case and walks four prompts:

1. **Project context.** What the app does, and what makes it distinct.
2. **UX principles.** Three to six. For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*. Each gets a one-line claim plus a few sentences of reasoning.
3. **Core functionalities — first pass.** Three to five features that make this app what it is. Each gets a paragraph plus the *user needs this because…* line.
4. **First build batch sketch.** The smallest end-to-end thing that can be built and tested.

These are the decisions the rest of the project is built on. Claude queues the answers as a `[FOLD-IN PENDING]` block in BACKLOG.md. The no-coder folds the UX content into UX.md by hand during the same planning session, and converts the first-build-batch sketch into a proper build batch with a `Serves UX.md:` line.

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
5. **Build batch.** A build batch enters BACKLOG.md ending with `Serves UX.md: Dark mode (and the two reviewed entries).`

If step 3 had answered "no," steps 4 and 5 would not happen. UX.md stays as it was, the planning batch is removed as resolved, no build batch is ever created. That short-circuit case is just as valid an outcome as "yes, build it."

The due-date item runs the same pipeline. It might land at "yes, with relative shortcuts only, no date picker" — folding into a new UX.md entry once decided, then a build batch.

**What if the idea conflicts with an existing UX principle?** If a test note or feature request would violate a principle already in UX.md, that conflict gets surfaced in chat as the first response — not quietly routed into a planning batch and hoped for. The planning batch still happens (step 2), and the conflict becomes one of its questions. Chat surfaces the tension immediately; the planning batch records and resolves it.

### Drift checks at planning sessions

By the third or fourth build, drift checks run at the start of every planning session. Four checks — three pairwise comparisons plus one code-touch judgement:

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

## The safety net — installing on a folder that isn't empty

The method assumes a fresh project. Sooner or later someone installs the plugin into a folder that is not fresh — by mistake, or to bring an existing project under the method's discipline. The safety net is the plugin's response.

When a session opens, **SessionStart** checks whether the folder is *adopted* (carries the method footer in CLAUDE.md) or *unadopted*. Adopted folders, genuinely empty folders, and folders carrying a `.no-code-method-skip` opt-out marker stay silent. An unadopted folder with substantial existing work — code, foreign docs, anything — triggers an advisory pointing at the `/adopt` command.

Until `/adopt` runs, **PreToolUse** denies Edit, Write, MultiEdit, and method-subagent calls from main Claude. Not just a warning — an actual block. `/adopt`'s own scaffolding calls pass through, so adoption can happen while the gate is closed against everything else.

`/adopt` branches on what it finds:

- *Empty folder* → walks the four new-project prompts and scaffolds the spine docs with the no-coder's answers folded in.
- *Existing code, no docs* → offers to scaffold fresh docs alongside, or to opt out via `.no-code-method-skip`.
- *Existing code, foreign docs* (most commonly: Claude Code's built-in `/init` ran first) → offers to **migrate** the existing CLAUDE.md to method spec (preserving content — Claude proposes edits and iterates with the no-coder until the migration plan is right; anything that does not fit cleanly lands as `[FOLD-IN PENDING]` blocks so nothing is lost), **overwrite** the existing CLAUDE.md after backing it up, or **leave alone** via the opt-out marker.
- *Already method-managed* → detects template state, surfaces any version mismatch, offers a **refresh** (bumps method-version footers across writable docs directly; locked docs get `[FOLD-IN PENDING]` entries for the no-coder to bump by hand; project-specific content in CLAUDE.md stays intact) or **cancel**.
- *Opted out* → folder previously chose `.no-code-method-skip`; offers to clear the marker (returning to unadopted) or to stay opted out.

Nothing destructive happens without explicit confirmation, and every destructive option backs up first.

Why session-start, not install-time? Claude Code's plugin system has no install-time hook the plugin can run code from. The earliest the plugin can act is when a Claude Code session opens in a folder. By the time the no-coder could ask Claude to write a file, the gate has already fired.

## What's inside the plugin

The plugin distributes the method's rules across Claude Code primitives — hooks, subagents, skills, and bundled docs — rather than asking Claude to enforce them from a single long prompt. Non-coders do not normally open these files; the plugin runtime does the work.

- **Hooks** are Python scripts that fire on specific Claude Code events. The SessionStart hook detects what shape of folder the no-coder is working in (adopted, unadopted-with-work, empty, opted-out) and injects an advisory or the universal behavioural rules into Claude's session context. The PreToolUse hook enforces edit boundaries — locking UX.md and additional source-of-truth docs from Claude, blocking edits outside the current batch's `Files:` list, gating new build batches on the previous batch's test outcomes being confirmed, refusing build batches whose `Serves UX.md:` line names entries that do not exist in UX.md, and blocking destructive git commands (`git reset --hard`, `git push --force`) with deny messages pointing at safer alternatives. The Stop hook routes one build batch to the next, or routes to the after-build subagent when a batch finishes.
- **Subagents** handle the phase work in their own Claude Code contexts: planning, before-build, batch-executor, after-build, and adopt. Each runs its own conversation, then returns a recap that main Claude relays to the no-coder. The context isolation keeps each phase's prompts focused.
- **Slash commands** (`/adopt`, `/before-build`, `/build`) are the user-facing entry points. Each invokes the matching subagent.
- **Templates** — the starter shapes for the six spine docs that `/adopt` scaffolds into a new project. These get copied into the project root with method-version footers and start mostly empty.
- **Bundled reference docs** — `DOC-STRUCTURE.md` and `VOCABULARY.md` live inside the plugin at `plugin/docs/`. The subagents read them when needed via `${CLAUDE_PLUGIN_ROOT}/docs/...`. Non-coders do not normally open these directly; the *When you need more* section at the end of this doc says when reaching for them is worthwhile.

The split between hooks (deterministic enforcement) and subagents (probabilistic behaviour) is deliberate: hooks bite when correctness matters and a prompt-based instruction might be ignored; subagents handle the work that needs judgment.

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

**One exception: method-version footer stamps.** The `*No-code method — Version N.*` footer on each doc is metadata, not content. The PreToolUse hook allows footer-only edits on locked docs, so `/adopt`'s version refresh can stamp all footers directly without routing through fold-in blocks.

**The `[FOLD-IN PENDING]` mechanism.** Claude cannot write directly into read-only source-of-truth docs like `UX.md`. Instead, proposed content is queued as a `[FOLD-IN PENDING]` block in BACKLOG.md's *Fold-ins pending* section. The block names the destination doc, the proposed change, and where the content came from — a planning-batch resolution, `/adopt`, or a mid-build edit attempt the PreToolUse hook intercepted.

During planning sessions and `/adopt`, a **preview-then-fold-in convention** applies: before writing the fold-in block, Claude shows the complete proposed section in chat (heading, content, formatting, and all) and waits for the no-coder's approval. On approval, Claude writes the fold-in block and prompts the no-coder to fold it in now — naming the section heading to find and replace in the destination doc. The fold-in happens in the same session rather than being deferred. Mid-build edit attempts intercepted by the hook still produce a standard `[FOLD-IN PENDING]` block deferred to the next planning session.

## Why the rules

The method's rules are not arbitrary; each one defends something. Some of the defences are not obvious from the rule alone, so they live here in prose.

**Why Claude is asked to push back rather than agree.** A planning recap that mirrors whatever the no-coder last said is only useful if Claude has engaged with disagreement before recording the outcome. Capitulating without engagement and refusing to listen are mirror failures: both bypass the conversation that would decide whether a suggestion was right. The drift checks, red-flag surfacing, and planning recaps all assume Claude pushes back when something looks wrong — if Claude defaults to agreement, the safety nets stop functioning.

**Why regressions get stated plainly, not stealth-fixed.** The build recap is the no-coder's primary record of what happened in a build session, used to decide whether to test, push back, or accept. A stealth-fix breaks that record — the regression survives invisibly until it resurfaces later with no breadcrumbs back to its origin. Plain statements keep the recap a reliable trail.

**Why batch scope is locked once agreed.** Mid-build scope additions cost three things the method protects. Predictability of session length — a batch with a fixed file list has a knowable end; one that absorbs "while we're here" additions does not. Clean test coverage — one batch is one set of changes is one set of tests; mid-build mixing makes regressions harder to trace. The planning-gate filter — mid-build, things feel in-scope that would not survive a planning conversation. The rule defers scope decisions back to planning rather than shortcutting them. The two named carve-outs (prerequisite and re-batching) are escape valves the discipline anticipates, not invitations to bend the rule.

**Why drift checks operate at four different abstraction levels.** The four checks — UX.md ↔ build, MANIFEST.md ↔ code, MANIFEST.md ↔ UX.md, TEST-LOG.md ↔ what has been touched — operate at different abstraction levels (feature-to-feature, name-to-name, loose user-facing-purpose, per-row code-touch with reasoning trail). Doing all four at once mixes the levels and produces noise. Running them as four separate passes lets each catch the gap it is designed for.

**Why source-of-truth docs are locked from Claude.** UX.md and additional source-of-truth docs are written slowly, in planning sessions, with the time those decisions deserve. Build sessions are short and build-focused — the wrong environment for stable docs to drift via small "clarifying" tidy-ups. Locking those docs from Claude means design changes can only happen where they get proper deliberation.

**Why source-of-truth docs cannot carry placeholders or soft gestures at undecidedness.** Source-of-truth docs are operational. Runtime audiences (Claude, the no-coder's future self, anyone reading to remember what was decided) need the instruction, not its status. A line that says "currently undecided" forces the reader elsewhere for the actual rule and makes the doc inert until that elsewhere is found. The status of an open question lives in BACKLOG.md, not in the body of a source-of-truth doc.

**Why UX principles are project-specific.** A budgeting app's principles ("never let the user lose data they have entered") look nothing like a task manager's ("reduce planning pressure"). Principles that try to be method-wide become so abstract they stop guarding any actual decision. The job is to write the three-to-six principles that protect *this* project's design from drift, not to compile a general theory of UX.

**Why MANIFEST.md starts flat instead of pre-sectioned.** "Switch to alphabetical sections by area when the flat list grows too long" sounds like permission to start with sections from day one. It is not. Most projects' MANIFEST.md never grows large enough to need sections, and pre-emptive sectioning forces architecture decisions (which "areas" exist?) before there is enough code to know. Wait until scrolling the flat list actually hurts.

**Why BACKLOG.md is one file with four sections instead of four files.** Red flags, fold-ins pending, planning batches, and build batches could live in four separate files. They do not, because the friction of multiple places to check is what causes deferred items to slip through. One file, four sections, top-to-bottom by priority means there is exactly one place to look for what is outstanding.

**Why Risk accepted is its own labelled line.** Without an explicit *Risk accepted* line, the cost of a deliberate simplification fades from view. Six months later, someone (often the same person who chose the simplification) wonders why the app deliberately omits a feature and considers adding it — without remembering why it was omitted. The Risk-accepted line keeps the trade-off on the page so any re-litigation happens with the original reasoning in view.

**Why a test session must be closed by per-row read-back before the next build can start.** Bulk confirmations ("all the others passed") would silently flip dozens of TEST-LOG rows to confirmed when only a few were actually verified. A single per-row read-back — Claude reads the test description, the no-coder names the outcome — is the only way to keep the record honest. Without that, TEST-LOG.md becomes intentions-as-data rather than decided outcomes.

## What this costs

A new feature takes two sessions to land — one planning, one build — at minimum. The pipeline is rigid by design. What the discipline buys: every shipped feature traces to a written user-need rationale; nothing gets built that no one decided to build; and at any moment "why is this here?" has an answer on a page that can be opened.

## Where the method sits in the broader landscape

The method belongs to the spec-driven development family. Closest neighbour: Cline's Memory Bank — same shape (markdown files as project memory and behavioural guardrails, read at session start), different cut of files, different audience. Memory Bank's cut: `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`. This method's cut: UX.md, MANIFEST.md, BACKLOG.md, TEST-LOG.md, plus additional source-of-truth docs as needed. Different cuts of the same idea. Memory Bank is general-purpose; this method is shaped around non-coders.

In the broader spec-driven-development literature (the arXiv paper, the GitHub Spec Kit, the Augment Code guides, the DeepLearning.AI course), this method maps onto the **spec-anchored** rigour level: specs are high-quality context that drive code generation, but code remains the source of truth.

## Caveats

Iteratively developed. Has not yet been used to ship an app. The first real Taskflow build under the current version is the next test — and the most honest one.

A known headwind for any methodology relying on `CLAUDE.md`-style instructions: roughly 30% of the time, Claude will not follow them. The method designs around this by making source-of-truth docs read-only to Claude (so big design changes cannot slip in mid-build) and by making most non-trivial decisions reviewable in chat. But the headwind is real, and any no-coder should expect to recognise drift and recover from it as part of the skill.

Claude will sometimes hand the no-coder a paste-ready prompt and ask them to run a web search (or run one in a separate Claude Sonnet chat) before proceeding. This is a method discipline, not Claude being lazy — it's how the method prevents wrong external facts from getting baked into source-of-truth docs and scope files. If the no-coder can't run the search, Claude marks the uncertain claim with `[UNVERIFIED]` and proceeds conservatively.

Claude Code's built-in **plan panel** (the Shift+Tab plan-mode surface) does not show the method's build sequence. The panel is Claude-Code-internal — populated only by Claude itself via its native plan-mode flow, with no plugin-facing write surface to inject the method's current and queued build batches. Where the real sequence lives is `BACKLOG.md` → Build batches; the top batch is what's next. If the plan panel reads empty mid-build, that is not the plugin losing track of where it is — that is the panel showing what it can show. Open the project's `BACKLOG.md` to see the actual queue.

## When you need more

This document is the primer. The method's full specification lives inside the plugin you installed, at `plugin/docs/NO-CODE-METHOD.md` (the behavioural rules and operational procedures) and `plugin/docs/DOC-STRUCTURE.md` (the structural rules for the project's docs). Both files are also browsable on the source repo at `https://github.com/FlintCraftTech/sovereign-implementer/tree/main/plugin/docs`. From V17 onwards, versions are tracked as git tags (`v17`, `v18`, ...), one tag per working session.

Reach for them when:

- A concept this primer mentions in passing turns out to matter to a decision being made.
- A rule's edge case is the thing actually needed.
- A non-method project is being migrated onto the method and `/adopt`'s case 3 dialogue surfaces a structural rule whose reasoning matters.
- The method itself is being extended — proposing changes, building related tooling, or distinguishing what is core from what is editable habit.

For everything else, this primer is enough.

---
*No-code method — Version 38.*
