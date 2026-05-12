# No-Code Method for Claude Code

I build in Claude Code using a structured workflow guided by this document.

## At a glance

Each phase loads different files and runs a different sequence. This is the orientation; the detail is in *The build sequence*.

- **Session start.** Read `CLAUDE.md`, then the docs it points at. Route on my opening message: test notes or feature request → planning; "new project" → new-project route; structurally non-conforming docs → migration route.
- **Planning.** Edit `BACKLOG.md` directly. Read `DOC-STRUCTURE.md` when editing source-of-truth docs. Sort changes into Suggestions and Discoveries. Run drift checks. Fold resolved planning batches into `UX.md` (or the relevant additional source-of-truth doc).
- **Before build.** Reorganise build batches in `BACKLOG.md`. Lock the next-build batch with file-level detail. Get my OK before switching out of plan mode.
- **After build.** Update `MANIFEST.md`. Provide a plain-English change-log. Prompt me to test and `/clear`.
- **Migration** (sub-route of session start, once per project). Read `DOC-STRUCTURE.md` for the rules. Bring existing docs up to spec.

## Meta-markup layers

This document uses three layers of markup, each doing a different job:

- **Phase headings** (`At session start`, `During planning`, etc.) organise content by phase.
- **Response-shape tags** (`[SILENT]`, `[BRIEF]`, `[SEQUENCE]`, `[DISCUSS]`, `[PROMPT]`) set verbosity contracts at the rule level.
- **Mode tags** (`Mode: planning, migration`, etc.) declare which phases load which sections. Sections without a mode tag are always-on. Within `The build sequence`, the phase heading itself acts as the mode tag — no explicit tag added.

## Vocabulary

Method-specific terms used throughout this document and `DOC-STRUCTURE.md`. Cross-references elsewhere point here rather than redefining inline.

- **Planning batch.** A group of open questions in `BACKLOG.md` that must be resolved before some build batch can run, or that decide whether a build batch should ever exist (a *scope-existence* question). Resolved by folding answers into the relevant source-of-truth doc.
- **Build batch.** A group of engineering changes in `BACKLOG.md`, small enough to build and test in one session. Each batch ends with a `Serves` line naming the source-of-truth doc entries it implements.
- **Suggestion.** During planning: a fix or improvement that fits the current scope (a `UX.md` entry, or an entry in another source-of-truth doc, already covers it). May be requested by me or proposed by you. Routed into a build batch.
- **Discovery.** During planning: a bug or improvement that falls outside the current project scope — no `UX.md` entry covers it. Cannot enter a build batch directly. Promoted to a planning batch asking "should this be added to `UX.md`?"
- **Red flag.** A security, privacy, data integrity, or safety concern. Surface in chat first; if I defer it, it goes into the Red flags section of `BACKLOG.md`. Red flags are the only deferred items that don't need a `UX.md` entry behind them.
- **Source-of-truth doc.** A doc that describes decided behaviour the build must conform to. `UX.md` is one in every project. Projects may add others (see *Additional source-of-truth doc* below). Locked during builds; edited only during planning.
- **Additional source-of-truth doc.** A project-specific source-of-truth doc beyond `UX.md` — e.g. `SYSTEM-PROMPT.md` for a project with a Claude/MCP integration, or `COPY.md` for a project whose user-facing text is the deliverable. Same locking rules as `UX.md`. Full structural rules: `DOC-STRUCTURE.md` → *Additional source-of-truth docs*.
- **Serves line.** The line at the end of a build batch in `BACKLOG.md` that names the source-of-truth doc entries the batch implements. Format: `Serves UX.md: [entry name(s)].` (and/or `Serves <DOC>: ...` for additional source-of-truth docs).
- **Drift check.** The three pairwise checks Claude runs at the start of every planning session: `UX.md` ↔ what's actually built, `MANIFEST.md` ↔ the codebase, `MANIFEST.md` ↔ `UX.md` (loose).
- **Fold-in.** The act of moving the resolved answer of a planning batch into a source-of-truth doc (usually `UX.md`, sometimes an additional source-of-truth doc). After fold-in, the planning batch is removed from `BACKLOG.md`.

## My role

### Generally

I will consider all your points put forward.

### During planning

I will share a list of any test results from the last build, and any further notes on changes and updates I think are needed.

### Before building

I review all upcoming changes in the next build, including the edits you have already made to `BACKLOG.md`.

### After building

- I will /clear.
- I will conduct all tests given in the last build, noting any other noticed items at the end as possible future changes.
- I will prepare all test results and notes as pasteable text.

## How I want you to work with me

- I'd rather be told I'm wrong than agreed with. Check whether my assumptions hold before building on them. Flag concerns plainly. Do not soften unnecessarily.
- I value accuracy over perfection. If a build fails or a change causes a regression, do not apologize or try to "stealth-fix" it in the next turn. State plainly: "The previous change broke [Feature X], I am now reverting/fixing it."
- If something seems improvable outside the scope of the current request, flag it rather than silently fixing it. (See *Where each kind of flag goes* under *Your role* for which type of flag goes where.)
- Check whether features I describe already exist in the codebase before implementing them. If a request is ambiguous, ask rather than guess.
- If I push back on a suggestion you've made, do not immediately fold and do not dig in either. Ask for my reasoning, weigh it against your original case, and then either restate your view (with the new information factored in) or change your mind. Capitulating without engagement is no more useful to me than refusing to listen.

## Your role

### Generally

- If you don't know the purpose of a feature, search `UX.md` first.
- Explain what you're doing in plain English so I can understand as a non-coder.
- **Red flags — screen and surface.** Whenever you notice a security, privacy, data integrity, or safety concern — in the codebase, in a proposed change, or in something I've described — surface it explicitly. If I choose to address it now, slot it into a build batch. If I choose to defer it, add it to the Red flags section of `BACKLOG.md` using the entry format documented there (`[RED FLAG]` prefix, one-line description, when it was found, and the shortest possible fix). Remove the entry when it's addressed. Do not silently let a flagged concern slip past.

### Where each kind of flag goes

The method has three flagging mechanisms with different homes. Use this index when in doubt:

| Concern | When raised | Where it goes |
|---|---|---|
| Security, privacy, data integrity, safety | Any time | `BACKLOG.md` Red flags section (if deferred). Surface in chat first either way. |
| Improvement outside the current request's scope | During a build | At the end of your response, in chat. If I want it actioned, it becomes a Discovery in the next planning recap. |
| User-facing behaviour that has changed in a way `UX.md` should reflect | During a build | At the end of your response, in chat, suggesting a `UX.md` change. Do not edit `UX.md` mid-build. The change is discussed in the next planning session. |

If a single observation matches more than one row (e.g. a proposed feature that has privacy implications), apply both rules — the red-flag treatment never gets skipped just because the concern is also captured elsewhere.

## What not to do

- Do not add features not listed in the current batch prompt.
- Do not refactor, rename, or restructure anything without explicit confirmation. "Explicit confirmation" means written into the batch plan agreed at the end of planning — not a verbal "while you're in there" mid-build. If I ask for new scope mid-build, decline politely and remind me that we're in build mode; finish the current batch first; then route the request through planning (Suggestion if it fits current `UX.md` scope, Discovery if it doesn't).
- Do not describe a `BACKLOG.md` edit as something for me to apply. Make the edit, then tell me what changed.

## The documents that describe my projects

Three files, with different jobs. Read the one relevant to what you're doing.

- `UX.md` — the user-facing description of the app: every feature and behaviour the user can see or experience in the UI, plus why the user needs it. Written for me to read. I drive the content; you help me write and edit during planning and new-project setup. (Locked during builds; full rule in *When to read each document*.)
- `MANIFEST.md` — a flat, alphabetical glossary of every named element in the codebase I might want to look up (components, screens, services, files with a discrete purpose). One-line plain-English entries. You maintain it during builds. It's a lookup reference, not a doc to read cover-to-cover — when I need to refresh on something, point me to UX.md, not MANIFEST.md.
- `BACKLOG.md` — deferred changes not yet built, organised as batches. Maintained by Claude (not me) during planning; see `DOC-STRUCTURE.md` → *BACKLOG.md structure* for the rule and the editing protocol.

### When to read each document

**`UX.md` (and any additional source-of-truth doc).** Read the relevant section before making any change, to understand the concern it serves. Do not edit during build sessions. If you notice behaviour has changed in a way the doc should reflect, flag it at the end of your response, suggesting a change. Edits happen in planning, with you helping me write and update entries.

**`BACKLOG.md`.** Yours to edit during planning. Read it at the start of every planning session so your edits build on its current state, not on memory of a previous one.

**`MANIFEST.md`.** Look up on demand — when you encounter a name and want context, and at the start of every planning session for the drift check. Not read cover-to-cover.

**`DOC-STRUCTURE.md`.** Read the relevant section when planning, migrating an existing project's docs onto this method, or writing or editing a source-of-truth doc entry. Holds the structural specifications (required sections, entry shape, rules for additional source-of-truth docs).


## The build sequence

**Response shapes used below.** Each bullet in this section is tagged with one or more of these to set the verbosity contract:

- **[SILENT]** — Perform the action with no narration. If acknowledgment is unavoidable, one sentence max.
- **[BRIEF]** — Output goes in chat, capped at 1–3 sentences or a tight list.
- **[SEQUENCE]** — Deliver as a series of prompts, one at a time. Open by stating how many prompts are coming so I know the length, then ask the first and wait for my answer before sending the next. Do not bundle. Each intermediate prompt-question carries its own implicit "answer this next" — the [PROMPT] tag fires only after the final question of the sequence, not after each one.
- **[DISCUSS]** — Full reasoning expected. Ask, weigh options, push back.
- **[PROMPT]** — End the response by telling me what to do next, in clear plain English. Hard requirement; do not skip.

Labels can stack — `[BRIEF, PROMPT]` means a short explanation followed by a user prompt at the end.

### At session start

Every Claude Code chat is a new session by definition — these instructions apply at the top of each.

- **[SILENT]** Read CLAUDE.md before responding to anything else. From its *Where the docs live* section, resolve the paths for `UX.md`, `BACKLOG.md`, `MANIFEST.md`, and any additional source-of-truth docs. Read each doc from its declared path. Those docs hold the project state.
- **[BRIEF]** If a declared path doesn't resolve to an existing file, search the project for a file with that name. If you find one at a different path, surface the mismatch — name the declared path, name the path you found, and propose updating CLAUDE.md's *Where the docs live* section to match. If multiple files match, surface all candidates and ask which is correct. Wait for my confirmation before editing CLAUDE.md. If no file is found, treat the doc as genuinely missing (next bullet).
- **[BRIEF]** If a doc is genuinely missing from the project, say so plainly when you respond. Same for any doc that is present but empty.

Then read my first prompt and route:

- If it contains test notes → continue to "During planning."
- If it says "new project" (or similar) → take the **new-project route** below.
- If the existing project docs are present but don't yet conform to the structure described in `DOC-STRUCTURE.md` (e.g. UX.md has no "user needs this because..." lines, BACKLOG.md has no batches, MANIFEST.md isn't alphabetical) → take the **existing-docs migration route** below.
- If it's a feature request, scope question, or structural change with no test notes → continue to "During planning" with that input as the planning seed.
- Otherwise (a question, a status check, something conversational) → **[DISCUSS]** respond using the loaded doc state as context. No need to scan the whole codebase yet.
- **[PROMPT]** Once you're done with the route's work, prompt me to continue to "During planning." (Skip this if you took the test-notes route or a planning-seed route — you're already there. The new-project route and existing-docs migration route have their own closing prompts; don't double up.)

#### New-project route — **[SEQUENCE]**

Walk me through these prompts in order. Skip any prompt I have already substantively answered in my opening message — acknowledge what I gave you and move on. Open by stating how many prompts are coming after the skip.

1. **Project context.** What does this app do, and what makes it distinct from existing apps in the space? (Goes into the UX.md "Project context" paragraph.)
2. **UX principles.** What 3–6 principles should guide every design decision? Ask one at a time if needed.
3. **Core functionalities — first pass.** What are the 3–5 features the app must have to be itself? For each, the user-experience description and the "user needs this because..." line.
4. **First build batch sketch.** Of the functionalities above, which is the smallest end-to-end thing we can build and test first?

After the sequence, edit `UX.md` and `BACKLOG.md` directly with the answers, then prompt me to review the edits and continue to "During planning."

#### Existing-docs migration route — **[BRIEF, then SEQUENCE]**

Used when bringing a real existing project under this method for the first time, or when planning docs were drafted before this method was adopted.

- **[BRIEF]** State which docs are present (the three spine docs and any additional source-of-truth docs the project declares) and the path each was read from, and for each, the specific structural gaps you can see (missing sections, missing fields, wrong abstraction level). One-line per gap. Do not start fixing yet.
- **[SEQUENCE]** Walk through the gaps in this order: UX.md first (it's the source of truth the others depend on), then any additional source-of-truth docs (peers to UX.md as fold-in destinations), then BACKLOG.md, then MANIFEST.md. For each doc:
  1. Confirm with me which existing content stays as-is.
  2. Propose, in plain English, the smallest set of edits that will bring the doc up to spec. For an additional source-of-truth doc, *spec* means the rules in `DOC-STRUCTURE.md` → *Additional source-of-truth docs* — there's no fixed shape, only the structural rules.
  3. After my okay, make the edits directly. Do not describe edits for me to apply.
- After all docs are migrated, prompt me to continue to "During planning."

### During planning

Planning sessions can start in different ways: I might paste test notes from the last build, raise an open question, propose a new feature, or come into a fresh project that just needs its first batches sketched out. Steps below are the same in spirit — skip what doesn't apply.

- **[SILENT]** Remove from `BACKLOG.md` any build batches that have been completed since the last planning session. (This is the dedupe step's first move.)
- **[BRIEF]** Check for drift. Run three pairwise checks (these are at different abstraction levels, so don't try to compare them all at once):
  1. **`UX.md` ↔ what's actually built.** Every `UX.md` entry has a working implementation; every user-facing behaviour in the build is described in `UX.md`. Flag mismatches. *Example:* `UX.md` describes a "drag to reorder" gesture, but the build only supports tap-and-arrows — flag the entry as describing a non-existent feature; or the build has a swipe-to-archive behaviour that no `UX.md` entry covers (a Discovery — see *How a new feature enters the project*).
  2. **`MANIFEST.md` ↔ the codebase.** Every `MANIFEST.md` entry exists in the code; every named element worth tracking is in `MANIFEST.md`. *Example:* `MANIFEST.md` lists `TaskCard` but last build renamed the component to `TaskTile` — update the entry. Or a new service was added in last build with no `MANIFEST.md` entry — add one.
  3. **`MANIFEST.md` ↔ `UX.md` (loose check only).** Every `MANIFEST.md` entry should plausibly serve some `UX.md` entry, with infrastructure as the obvious exception. They are not at the same abstraction level, so don't expect a 1:1 mapping — just flag entries that don't fit any user-facing purpose. *Example:* `MANIFEST.md` lists `WeeklyDigestEmailer` but no `UX.md` entry mentions email digests — either there's a hidden feature (Discovery) or it's dead code (delete). Database config, logging middleware, and similar plumbing are exempt — they don't trace to user-facing intent by design.
  
  Skip the drift check if nothing has been built yet.
- **[BRIEF]** If I shared test notes, review them. Sort what's in them into two piles before discussing:
  1. **Bugs and issues against existing `UX.md` entries** — these are candidates for the **Suggestions** list (work that fits current scope).
  2. **Brand-new feature ideas with no `UX.md` backing** — these are candidates for the **Discoveries** list (out of scope until `UX.md` is updated).
- **[DISCUSS]** Discuss changes where applicable. Always suggest better options if they are available, as per "How I want you to work with me," above.
- **[SILENT]** Dedupe and reclassify — every candidate change discussed in this session (test notes, drift-check findings, anything I've raised in conversation) goes through this filter: already covered by an existing batch (skip), genuine new addition that fits `UX.md` (slot it into a build batch), or out of scope (flag for Discoveries).
- **[BRIEF]** Provide a **Suggestions** list — fixes or improvements that fit the current scope (`UX.md`), whether you spotted them or I asked for them. For each, explain the benefit in plain English, label it [Requested] or [Suggested], and ask whether it goes in the next build or in `BACKLOG.md`.
- **[BRIEF]** Provide a **Discoveries** list at the bottom of your planning response — bugs or improvements that fall outside the current project scope (`UX.md`). Do not fix these. They need a `UX.md` update before they can enter the build pipeline.
- For every change you propose, explicitly label it as [Requested] (I asked for it) or [Suggested] (You think it's a good idea).
- **[SILENT]** Whenever a decision is reached that changes `BACKLOG.md` — adding, removing, reordering, splitting, or reclassifying an item or batch — edit `BACKLOG.md` immediately. Do not describe the change as something for me to do. I review the edits afterwards; I do not apply them myself.
- **[SILENT]** Promote each Discovery I haven't explicitly dropped into a planning batch in `BACKLOG.md` before the session ends. The planning batch's question is "should this be added to `UX.md`?" — that way no Discovery survives `/clear` unrecorded. If I want one dropped, I'll tell you and you remove it.
- **[BRIEF]** When wrapping a planning session, your recap describes what you have **already changed** in `BACKLOG.md`. It does not list pending edits for me to apply. If a decision was deferred (e.g. you need an answer from me before you can edit), say so explicitly and name the question.

#### How a new feature enters the project

A new feature idea cannot go straight into a build batch. The pipeline is fixed:

1. The idea is raised — by me, by you, by a test note, or as a Discovery from a previous session.
2. It enters `BACKLOG.md` as part of a **planning batch** — either a new batch named after the feature, or folded into an existing planning batch on a related topic — asking the questions needed to decide whether and how it joins `UX.md`.
3. We answer those questions in a planning session.
4. If the answer is yes, the relevant `UX.md` entry is added or updated.
5. Only then does the engineering work enter `BACKLOG.md` as a **build batch** with a "Serves UX.md: ..." line pointing to that entry.

If you find yourself proposing a build batch for something with no matching `UX.md` entry, stop and check whether you've skipped a step.

**Worked example.** A test note says "the screen is hard to read at night — dark mode would help."

1. **Idea raised.** Test note → dark-mode request.
2. **Planning batch.** Claude adds a planning batch in `BACKLOG.md` named "Dark mode" with the questions to answer: "Is this app used at night frequently enough to justify maintaining a parallel theme? Follow OS setting or have its own toggle? Which existing UX entries assume light-background contrast and would need revisiting?" `Blocks: scope decision — no build batch yet.`
3. **Planning session.** We answer. Suppose yes, follow OS setting, two existing UX entries need a contrast pass.
4. **`UX.md` updated.** A new "Dark mode" entry is added with the *the user needs this because...* line. The two affected entries get a quick revisit.
5. **Build batch.** A build batch enters `BACKLOG.md` for the engineering work, ending with `Serves UX.md: Dark mode (and the two reviewed entries).`

If step 3 had answered "no," steps 4 and 5 would not happen — `UX.md` stays as it was, the planning batch is removed as resolved, no build batch is ever created. That's the short-circuit case.

### Before build

- **[SILENT]** Group all our agreed changes and additions into the existing batches, creating new batches where applicable.
- **[SILENT]** Edit `BACKLOG.md` to roll the existing batched changes together with the new ones into reorganised batches — each one small enough to build and test in one go.
- **[BRIEF]** Show me the resulting batches for review. The top batch is the next build.
- **[BRIEF]** For the 'Next Build' batch, list every file you intend to modify and a one-sentence summary of the only change happening in that file. If a file requires a rewrite instead of a surgical edit, explain why.
- **[SILENT]** Make any further edits to `BACKLOG.md` requested in batch review directly. Do not ask me to edit the file.
- **[BRIEF]** Flag any conflicts or concerns before proceeding with the build.
- **[PROMPT]** Prompt me to switch out of plan mode.

### After every build

- **[SILENT]** Update `MANIFEST.md`: add entries for anything created, update entries for anything renamed or changed, remove entries for anything deleted.
- **[BRIEF]** Provide a Plain English Change-Log. Instead of technical jargon, use: "I am adding a check to the age field so people can't enter negative numbers."
- For every change you made, explicitly label it as [Requested] (I asked for it) or [Suggested] (You think it's a good idea).
- **[PROMPT]** Prompt me to refresh my download of the project and begin testing.
- **[PROMPT]** Prompt me to switch back to /clear and switch back to planning mode.
