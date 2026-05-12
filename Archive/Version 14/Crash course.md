# Crash course

*A short structural walk-through. 

## What this is

A structured set of markdown documents that tell Claude Code how to work on a project. Designed for non-coders working in Claude Code — someone who can't read or write code well, who is using Claude as the actual implementer, and who needs the structure to do most of the work of keeping the project from drifting.

The method belongs to the family of spec-driven development methodologies. The closest direct neighbour is Cline's Memory Bank: same basic shape (multiple markdown files acting as project memory and behavioural guardrails, read at session start by the AI). Different cut of files; different audience focus.

## The files

**Per-project (one of these per project):**

- **CLAUDE.md** — The project's entry point. Contains a pointer to the method spec, a path block declaring where every other doc in the project lives, and any project-specific behavioural notes.
- **UX.md** — The user-facing description of the app. Every entry corresponds to something the user can actually experience in the current build, plus a mandatory "the user needs this because…" line tying it back to a UX principle or user context.
- **BACKLOG.md** — Deferred work in three sections in fixed order: Red flags (security/privacy/data integrity concerns), Planning batches (open questions blocking a build batch), Build batches (engineering work, top-to-bottom by priority).
- **MANIFEST.md** — A flat alphabetical glossary of named elements in the codebase that the user might want to look up. Maintained by Claude during builds, not intended to be read cover-to-cover.
- **Optional additional source-of-truth docs** — When a project needs an extra doc the spine doesn't cover (e.g. `SYSTEM-PROMPT.md` for an MCP-integrated app, `COPY.md` for a project whose user-facing text is its primary deliverable). Same structural rules apply: read-only in Claude Code, no placeholders, intent-level not implementation.

**Method-side (shared verbatim across every project using the method):**

- **NO-CODE-METHOD.md** — The method spec: behavioural rules, flag taxonomy, the build sequence.
- **DOC-STRUCTURE.md** — Structural specs for the spine docs and additional source-of-truth docs. Reference material — read when writing or migrating a doc, not at every session start.

**Templates** — Starter shapes for `UX.md`, `BACKLOG.md`, `MANIFEST.md`, the project's `CLAUDE.md`, and any additional source-of-truth doc.

## The session shape

Every Claude Code session in a project under this method follows the same shape:

**At session start.** Claude reads `CLAUDE.md`, resolves the path block, reads the spine docs and any additional source-of-truth docs from their declared paths. If a path doesn't resolve, Claude searches the project for the file by name, surfaces what it finds, and asks for confirmation before updating `CLAUDE.md`.

**During planning.** Test notes are sorted into Suggestions (fits current scope) and Discoveries (out of scope until `UX.md` is updated). Drift is checked between `UX.md`, `MANIFEST.md`, and the actual codebase. Backlog edits happen directly. Discoveries are promoted to planning batches before the session ends so nothing slips through `/clear`.

**Before build.** Changes are grouped into batches small enough to build and test in one session. The next-build batch lists every file to be modified.

**During build.** `UX.md` and any additional source-of-truth docs are read-only to Claude Code (full rule in *Editing surfaces — Cowork and Claude Code* below). Any user-facing change Claude notices is flagged at the end of the response, not edited in. This single rule prevents most of the scope creep that plagued the chat-only version.

**After build.** `MANIFEST.md` is updated for anything created/renamed/deleted. A build recap is provided ("I am adding a check to the age field so people can't enter negative numbers"). The user is prompted to test and switch back to planning mode.

## Where each tool fits

This method is designed around two tools used in sequence:

- **Cowork** — where you plan and design. Big-picture decisions and source-of-truth doc work happen here. The walkthrough below assumes you start in Cowork.
- **Claude Code** — where you build. Source-of-truth docs that Cowork has written are read-only here; operational docs (`BACKLOG.md`, `MANIFEST.md`) stay read/write because builds need to update them.

The lock convention — which docs are read-only to Claude Code and why — is in *Editing surfaces — Cowork and Claude Code* below.

## Three disciplines that do most of the work

**The "the user needs this because…" line.** Required for every `UX.md` entry. Forces rationale articulation before implementation. Protects against feature drift. Makes scope decisions easier.

**The flag taxonomy.** Three buckets with three different homes. *Red flags* (security, privacy, data integrity, safety) go into `BACKLOG.md` and stay until addressed. *Suggestions* (improvement that fits current scope) go in chat at the end of the response. *Discoveries* (out-of-scope ideas) become planning batches in `BACKLOG.md` before the session ends. Every concern has exactly one place to live.

**The pipeline for new features.** A new feature can't enter a build batch directly. It must enter as a planning batch in `BACKLOG.md`, get answered in a planning session, become or update a `UX.md` entry, and only then enter as a build batch. Rigid by design. Claude proposing a build batch with no matching `UX.md` entry is a flag that something has been skipped.

## A walkthrough — a first project from scratch

This section follows a small project — a task manager called **Taskflow**, designed for users with executive dysfunction — through new-project setup, first planning, first build, and the first test note that comes back. It's meant to make the rules in `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` feel concrete before you read them as rules.

### Day one — starting from scratch

In **Cowork**, you talk through the project — what the app does, who it's for, what makes it distinct. Cowork helps you draft the four pieces that go into `UX.md` and the first sketch of `BACKLOG.md`:

1. **Project context.** What this app does, and what makes it distinct.
2. **UX principles.** Three to six. For Taskflow: *Reduce planning pressure*, *Drag is the primary verb*, *No date pickers, no shame*. Each gets a one-line claim plus a few sentences of why.
3. **Core functionalities — first pass.** Three to five features that make this app what it is. Each gets a paragraph plus the *user needs this because…* line.
4. **First build batch sketch.** The smallest end-to-end thing you can build and test.

You take the time you need on these — they're the decisions the rest of the project is built on. Cowork writes the answers into `UX.md` and `BACKLOG.md` directly.

When the docs feel ready, you switch to Claude Code in the project folder. Claude Code reads `CLAUDE.md`, resolves the path block, reads the docs, and is ready for the first build.

### A first UX entry — Risk accepted in action

One of Taskflow's first functionalities is **One-day-at-a-time view**: the Today screen shows only today's tasks. No week view, no agenda. The entry's *user needs this because…* line ties straight back to the *Reduce planning pressure* principle:

> Looking ahead at a wall of upcoming tasks is the planning-pressure that triggers shutdown for users with executive dysfunction. Seeing only today's load keeps the cognitive surface area small and the bar for getting started low.

The entry ends with a **Risk accepted** line:

> Users cannot plan around upcoming busy periods or anticipate scheduling conflicts. We've judged this an acceptable cost — the people this app is for are already overwhelmed by ahead-planning; protecting the present is more important than enabling the future.

The Risk accepted line is for the future-self who, six months in, wonders why the app deliberately omits a week view. The trade-off is on the page; it doesn't have to be re-derived.

### First build, first test note

The first build batch ships — an empty Today screen, a way to add a task. You `/clear`, refresh the build, test it, and write notes:

> *"Added a task fine. Couldn't find anywhere to set a due date — is that intentional? The screen is hard to read at night — dark mode would help."*

You paste the notes into a new Claude Code session. Claude takes the test-notes route into planning.

### How a test note becomes a feature — the five-step pipeline

Take the dark-mode item. The pipeline is:

1. **Idea raised.** Test note → dark-mode request.
2. **Planning batch.** Claude adds a planning batch in `BACKLOG.md` named *Dark mode* with the questions to answer: *Is this app used at night frequently enough to justify maintaining a parallel theme? Follow OS setting or have its own toggle? Which existing UX entries assume light-background contrast and would need revisiting?* Closes with `Blocks: scope decision — no build batch yet.`
3. **Planning session.** You and Claude answer. Suppose: yes, follow OS setting, two existing UX entries need a contrast pass.
4. **`UX.md` updated.** A new *Dark mode* entry is added with the *user needs this because…* line. The two affected entries get a quick revisit.
5. **Build batch.** A build batch enters `BACKLOG.md` ending with `Serves UX.md: Dark mode (and the two reviewed entries).`

If step 3 had answered "no," steps 4 and 5 would not happen. `UX.md` stays as it was, the planning batch is removed as resolved, no build batch is ever created. That's the short-circuit case — and it's just as valid an outcome as "yes, build it."

The due-date item from the same test note runs the same pipeline. It might land at "yes, with relative shortcuts only, no date picker" — folding into a new `UX.md` entry once the feature is decided, then a build batch.

### Drift checks at planning sessions

By the third or fourth build, Claude is running **drift checks** at the start of every planning session. Three pairwise comparisons:

- **`UX.md` ↔ what's actually built.** `UX.md` describes a "drag to reorder" gesture, but the build only supports tap-and-arrows — flag the entry as describing a non-existent feature. Or the build has a swipe-to-archive behaviour no `UX.md` entry covers — that's a Discovery.
- **`MANIFEST.md` ↔ the codebase.** `MANIFEST.md` still says `TaskCard`, but the last build renamed it `TaskTile` — update the entry. A new service was added with no `MANIFEST.md` entry — add one.
- **`MANIFEST.md` ↔ `UX.md` (loose check).** `MANIFEST.md` lists a `WeeklyDigestEmailer`, but no `UX.md` entry mentions email digests — either there's a hidden feature (Discovery) or it's dead code (delete). Database config and logging middleware are exempt; they don't trace to user-facing intent by design.

The drift check isn't exhaustive. It catches the cases where docs and code have started disagreeing, before that gap turns into a wrong-feature build.

### What this all costs

A new feature takes two sessions to land — one planning, one build — minimum. The pipeline is rigid by design. What the discipline buys you: every shipped feature traces to a written user-need rationale; nothing gets built that no one decided to build; and at any moment you can ask *why is this here?* and the answer is on a page you can open.

## What's editable, what's not

The method ships with a default set of preferences and commitments embedded in `NO-CODE-METHOD.md`. A new user adopting the method needs to distinguish three layers:

**Method contract — load-bearing, edit at your peril.** Some lines read like personal preferences but the method's machinery depends on them. "I'd rather be told I'm wrong than agreed with" — the drift checks, red-flag surfacing, and planning recaps all assume Claude will push back on the user. "Don't stealth-fix regressions" — the build recap assumes Claude states regressions plainly. "Don't immediately fold under push-back" — planning recaps assume Claude engages with disagreement rather than collapsing into either position.

**Recommended habits — edit freely.** Some lines are habits surrounding the build sequence: `/clear` after each build, prepare test results as pasteable text, review all upcoming changes before each build. A different user with a different rhythm might rewrite these to match how they actually work.

**The build sequence — fixed, not advisable to personalise.** The four-phase build cycle (At session start → During planning → Before build → After every build) is the method's spine. It is not part of the editable surface.

These three layers each have their own section in `NO-CODE-METHOD.md`: *Method contract* (with the Required-of-Claude / Prohibited-of-Claude split), *Recommended habits*, and *The build sequence*.

## Editing surfaces — Cowork and Claude Code

Some docs are stable artefacts — written slowly, in their proper environment, and meant to stay stable. `UX.md` and any additional source-of-truth docs are written deliberately in Cowork during planning, where their design decisions get the time and headspace they deserve. `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` are the method spec — updated in the method's own development project, then shared verbatim across every project using the method.

Claude Code sessions are different: short, `/clear`-bounded, and build-focused. The wrong environment for stable docs to drift via small "clarifying" tidy-ups. So these docs are locked to Claude Code — read-only. If Claude Code thinks one of them should be reworded or reorganised, it tells you in chat instead of editing.

The full split:

| Doc | Cowork | Claude Code |
|---|---|---|
| `UX.md` | read/write | **read-only** |
| Additional source-of-truth docs (`SYSTEM-PROMPT.md`, `COPY.md`, etc.) | read/write | **read-only** |
| `BACKLOG.md` | read/write | read/write |
| `MANIFEST.md` | read | read/write |
| `CLAUDE.md` | read/write | read/write |
| `NO-CODE-METHOD.md` | read | read |
| `DOC-STRUCTURE.md` | read | read |

**`BACKLOG.md` stays read/write to both** because builds need it (red flags get added, completed batches removed, batches split or reordered). The protective rule is built into the build sequence: Claude Code must discuss every `BACKLOG.md` change with you at the appropriate stage — never silently. The recap rules (after planning, before build, after build) make this explicit.

**`NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` are also read-only to Cowork** in your project — they're shared verbatim across every project using the method, so editing them in your project would diverge from the verbatim copy. They get updated in the method's own development project.

**Planning batch fold-in.** When a planning batch is resolved during a Claude Code session, Claude Code can't write the answer into `UX.md` directly — `UX.md` is locked. Instead, Claude Code writes the resolved answer into the planning batch in `BACKLOG.md` as a *fold-in pending in Cowork* marker. Next time you open Cowork, you do the actual fold-in. Operational detail: `NO-CODE-METHOD.md` → *During planning*.

## Why the rules

The rationale behind specific rules in `NO-CODE-METHOD.md` and `DOC-STRUCTURE.md` — the *why* that doesn't fit in a tight operational rule. Organised in the order the rules appear in those documents.

### From NO-CODE-METHOD.md

**Push-back without folding.** The rule "if I push back on a suggestion, don't immediately fold and don't immediately dig in" is load-bearing for planning recaps. A recap that just mirrors whatever the user last said is only useful if Claude has actually engaged with any disagreement before recording the outcome. Capitulating without engagement and refusing to listen are mirror failures: both bypass a conversation that would decide whether a suggestion was right. (See *What's editable, what's not* for why this is method contract, not personal preference.)

**No stealth-fixing.** The rule "if a build fails or causes a regression, state it plainly rather than silently fixing it" is load-bearing for the build recap. The recap is the user's primary record of what happened in a build session, and is used to decide whether to test, push back, or accept. A stealth-fix breaks that record — the regression survives invisibly until it resurfaces later with no breadcrumbs back to its origin. Plain statements keep the recap a reliable trail.

**Why batch scope is locked.** Mid-build scope additions cost three things the method is built to protect:

- **Predictability of session length.** A batch with a fixed file list has a knowable end; one that absorbs "while we're here" additions doesn't.
- **Clean test coverage.** One batch = one set of changes = one set of tests; mid-build mixing makes regressions harder to trace.
- **The planning-gate filter.** Mid-build, things *feel* in-scope that wouldn't survive a planning conversation. The rule defers scope decisions back to that conversation rather than shortcutting it.

The prerequisite carve-out — "if the batch genuinely cannot complete or be tested cleanly without an unplanned change" — exists because implementation occasionally reveals dependencies that weren't visible at planning time. The bar is high (cannot complete, not "would be nicer"), the protocol is halt-and-confirm (no silent prerequisites), and the build-recap labeling keeps it visible after the fact. The carve-out keeps the rule from forbidding the impossible without opening the door to creep.

**The drift checks at different abstraction levels.** The three drift checks (`UX.md`↔build, `MANIFEST.md`↔code, `MANIFEST.md`↔`UX.md`) operate at different abstraction levels — feature-to-feature, name-to-name, and a loose user-facing-purpose check. Trying to do all three at once mixes the levels and produces noise. Run them as three separate passes.

**Editing surfaces — why some docs are locked to Claude Code.** Full reasoning is in *Editing surfaces — Cowork and Claude Code* above.

### From DOC-STRUCTURE.md

**No placeholders, no soft gestures.** Source-of-truth docs are operational — runtime audiences (Claude Code, your future self in Cowork, anyone reading the doc to remember what was decided) need the instruction, not its implementation status. A line that says "currently undecided" forces the reader to look elsewhere for the actual rule and makes the doc inert until that elsewhere is found. The status of an open question lives in `BACKLOG.md`, not in the doc body.

**Additional source-of-truth doc shape — loose by design.** Different projects need different additional docs (a system-prompt doc, a copy doc, something else entirely) and the shape that works for one won't work for another. The structural rules — locked to Claude Code, no placeholders, intent-level, fold-in target — are what's invariant. The shape inside is the project's call.

**UX principles are project-specific.** A budgeting app's principles ("never let the user lose data they've entered") look nothing like a task manager's ("reduce planning pressure"). Principles that try to be method-wide become so abstract they stop guarding any actual decision. The job is to write the three-to-six that protect *this* project's design from drift, not to compile a general theory of UX.

**The "user needs this because…" line.** See *Three disciplines that do most of the work* above.

**Risk accepted — keeping the trade-off visible.** Without an explicit *Risk accepted* line, the cost of a deliberate simplification fades from view. Six months later, someone (often the same person who chose the simplification) wonders why the app deliberately omits a feature and considers adding it — without remembering the reason it was omitted. The *Risk accepted* line keeps the trade-off on the page so any re-litigation happens with the original reasoning in view.

**`MANIFEST.md` flat list — don't pre-empt the section split.** The rule "switch to alphabetical sections by area when the flat list grows too long" sounds like permission to start with sections from day one. It's not. Most projects' `MANIFEST.md` never grows large enough to need sections, and pre-emptive sectioning forces architecture decisions (which "areas" exist?) before there's enough code to know. Wait until scrolling the flat list actually hurts.

**`BACKLOG.md` as one file with three sections.** Red flags, planning batches, and build batches could live in three separate files. They don't, because the friction of three places to check is what causes deferred items to slip through. One file, three sections, top-to-bottom by priority means there's exactly one place to look for what's outstanding.

## Where the method sits in the broader landscape

If you've used Cline's Memory Bank, this will feel familiar — multiple structured markdown files governing AI behaviour, read at session start, with a workflow that loops planning and building. Memory Bank's cut: `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`. This method's cut: `UX`, `MANIFEST`, `BACKLOG`, plus additional source-of-truth docs as needed. Different cuts of the same idea. Memory Bank is general-purpose; this method is shaped specifically around non-coders.

In the broader spec-driven-development literature (the arXiv paper, the GitHub Spec Kit, the Augment Code guides, the DeepLearning.AI course), this method maps roughly onto the **spec-anchored** rigour level: specs are high-quality context that drive code generation, but code remains the source of truth.

## Caveats

The method is iteratively developed. It has not yet been used to ship an app. The first real Taskflow build under the current version is the next test — and the most honest one.

There is also a known headwind for any methodology that relies on `CLAUDE.md`-style instructions: roughly 30% of the time, Claude will not follow them. The method tries to design around this by making source-of-truth docs read-only to Claude Code (so big design changes can't slip in mid-build), and by making most non-trivial decisions reviewable in chat. But the headwind is real, and any user of the method should expect to recognise drift and recover from it as part of the skill.

## Where the actual files live

The current versioned method files (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `Crash course.md`, all templates) are in [the Taskflow repo on GitHub](https://github.com/your-username/Taskflowapp) — *(replace with the real link)*. Versions are numbered; each new working session produces one new version folder so the history stays intact and walkable.

---
*No-code method — Version 14.*
