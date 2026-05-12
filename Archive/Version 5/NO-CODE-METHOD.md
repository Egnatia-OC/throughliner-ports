# No-Code Method for Claude Code

I build in Claude Code using a structured workflow guided by this document.

## Your role

### Generally

- If you don't know the purpose of a feature, search `UX.md` first.
- Explain what you're doing in plain English so I can understand as a non-coder.
- **Red flags — screen and surface.** Whenever you notice a security, privacy, data integrity, or safety concern — in the codebase, in a proposed change, or in something I've described — surface it explicitly. If I choose to address it now, slot it into a build batch. If I choose to defer it, add it to the Red flags section of `BACKLOG.md` using the entry format documented there (`[RED FLAG]` prefix, one-line description, when it was found, and the shortest possible fix). Remove the entry when it's addressed. Do not silently let a flagged concern slip past.

### During planning

- Before reviewing my test notes, check for drift: compare `UX.md`, `MANIFEST.md`, and the actual codebase against each other. Flag anything user-facing in the build that isn't described in `UX.md`, and anything in `UX.md` that no longer matches what's actually built.
- Review my **Test notes** (my test results plus anything else I noticed).
- Discuss changes where applicable. Always suggest better options if they are available, as per "how to work with me," below.
- Dedupe and reclassify — for each item in my test notes, check whether it is already covered by an existing batch (skip it), is a genuine new addition (slot it into an appropriate batch), or is out of scope (flag it).
- After deduping, provide a **Suggestions** list — fixes or improvements you spot that fit the current scope (`UX.md`). For each, explain the benefit in plain English and ask whether it goes in the next build or in `BACKLOG.md`.
- Provide a **Discoveries** list at the bottom of your planning response — bugs or improvements that fall outside the current project scope (`UX.md`). Do not fix these. They need a `UX.md` update before they can enter the build pipeline.
- For every change you propose, explicitly label it as [Requested] (I asked for it) or [Suggested] (You think it's a good idea).
- **Whenever a decision is reached that changes `BACKLOG.md` — adding, removing, reordering, splitting, or reclassifying an item or batch — edit `BACKLOG.md` immediately. Do not describe the change as something for me to do.** I review the edits afterwards; I do not apply them myself.
- When wrapping a planning session, your recap describes what you have **already changed** in `BACKLOG.md`. It does not list pending edits for me to apply. If a decision was deferred (e.g. you need an answer from me before you can edit), say so explicitly and name the question.

### Before build

- Group all our agreed changes and additions into the existing batches, creating new batches where applicable.
- Edit `BACKLOG.md` to roll the existing batched changes together with the new ones into reorganised batches — each one small enough to build and test in one go.
- Show me the resulting batches for review. The top batch is the next build.
- For the 'Next Build' batch, list every file you intend to modify and a one-sentence summary of the only change happening in that file. If a file requires a rewrite instead of a surgical edit, explain why.
- Make any further edits to `BACKLOG.md` requested in batch review directly. Do not ask me to edit the file.
- Flag any conflicts or concerns before proceeding with the build.
- Prompt me to switch out of plan mode.

### After every build

- Update `MANIFEST.md`: add entries for anything created, update entries for anything renamed or changed, remove entries for anything deleted.
- Provide a Plain English Change-Log. Instead of technical jargon, use: "I am adding a check to the age field so people can't enter negative numbers."
- For every change you made, explicitly label it as [Requested] (I asked for it) or [Suggested] (You think it's a good idea).
- Prompt me to refresh my download of the project and begin testing.
- Prompt me to switch back to /clear and switch back to planning mode.

## My role

### Generally

I will always use /opusplan. I will consider all your points put forward.

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
- If something seems improvable outside the scope of the current request, flag it at the end of your response rather than silently fixing it.
- Check whether features I describe already exist in the codebase before implementing them. If a request is ambiguous, ask rather than guess.

## The documents that describe my projects

Three files, with different jobs. Read the one relevant to what you're doing.

- `UX.md` — the user-facing description of the app: every functionality and UI element the user experiences, and why the user needs it. I maintain this manually or in a planning chat; you do not edit it during builds.
- `MANIFEST.md` — a flat, alphabetical glossary of every named element in the codebase that the user might want context on (components, screens, services, files with a discrete purpose). One-line plain-English entries. Maintained by Claude during builds; the user does not maintain it. The user is not expected to read it cover-to-cover — it's a reference for lookups and a check against drift.
- `BACKLOG.md` — deferred changes not yet built, organised as batches. **Maintained by Claude during planning; the user does not maintain it.** When a planning decision changes the backlog, Claude edits this file directly.

### UX.md structure

Every project's `UX.md` follows this shape. Start a new project by copying these headers; fill them in as the project develops.

**Header.** A brief statement of what `UX.md` does, plus two rules: (1) every entry must correspond to something the user can actually experience in the current build, and (2) `UX.md` only describes what has been decided — open questions live in `BACKLOG.md` as planning batches, not here as placeholders.

**Project context.** One paragraph stating what the app is, what it does, and what makes it distinct from existing apps in the space. Sits between the header and the UX principles. Filled in once the project's basic identity is settled.

**UX principles.** Three to six project-specific principles that inform every design decision. Each principle is a one-line claim plus a few sentences of reasoning. Principles act as guardrails: if a proposed change conflicts with a principle, flag it before building. Principles are project-specific, not method-wide — a budgeting app's principles will look nothing like a task manager's.

**Functionalities.** Each functionality is one entry. Required shape:

> **Feature name**
> One paragraph describing how the user experiences this feature.
> The user needs this because... [rationale tying back to a UX principle or user context].

The "the user needs this because..." line is **required, not optional**. It forces articulation of the why before the how, which protects against feature drift and makes scope decisions easier later.

If a feature's behaviour is not yet decided, it does not belong here at all — it belongs in `BACKLOG.md` as a planning batch. Do not write `[TO FILL IN]` placeholders into `UX.md`; that's the job of planning batches.

### MANIFEST.md structure

**Header.** A brief statement of what `MANIFEST.md` is: a glossary of named elements in the codebase, maintained by Claude during builds, not intended to be read cover-to-cover.

The file starts empty at project start. The entry-format reminder lives inside an HTML comment so the file stays cleanly empty until the first build adds entries.

**Entries.** A single flat list, alphabetical by name. Each entry is one line:

> - **[Name]** — [one-line plain-English description of what this is and what it does]

Include things the user might plausibly ask about: components, screens, services, modules, files with a discrete purpose. Do not include trivial helpers, internal utility functions, or boilerplate.

If a project ever grows large enough that the flat list becomes hard to scan, switch to alphabetical sections by area. Don't pre-empt this — wait until the flat list actually hurts.

### BACKLOG.md structure

`BACKLOG.md` consolidates everything that is deferred, in three sections in this fixed order. The same file holds them all so I have one place to look instead of several.

**Header.** A brief statement of purpose, the section order, and the maintenance rule (maintained by Claude during planning, not by the user).

**Three sections, in this order:**

- **Red flags.** Security, privacy, data integrity, or safety concerns surfaced and explicitly deferred by the user. Empty by default. Each entry is a blockquote — `[RED FLAG]` prefix, one-line description, when it was found (which batch and date), and the shortest possible fix. Items are removed once addressed. Claude populates this section per the "Red flags — screen and surface" rule under *Your role → Generally*.
- **Planning batches.** Open questions that must be resolved before some build batch can run. Each planning batch lists the questions and which build batch (or batches) it blocks. Once resolved, fold answers into `UX.md` and remove the planning batch.
- **Build batches.** Engineering work, ordered top-to-bottom by priority. The top batch is the next build (after any one currently in progress). Each batch is a heading plus a list of changes; each batch ends with a "Serves UX.md: ..." line listing the entries it implements. Each batch should be small enough to build and test in one sitting.

If a change does not serve any `UX.md` entry, it is a Discovery, not a backlog item — it does not belong in `BACKLOG.md` until `UX.md` is updated to cover it. Red flags are the only exception: they live in `BACKLOG.md` even without a `UX.md` entry, because they're concerns to track regardless of scope.

### When to read each document

Before making any change: read the relevant section of `UX.md` to understand the user concern it serves.

Do not edit `UX.md` during build sessions. If user-facing behaviour has changed in a way `UX.md` should reflect, flag it at the end of your response, suggesting a change. I will update `UX.md` manually or in a planning chat.

`BACKLOG.md` is yours to edit during planning, as described above. Read it at the start of every planning session so your edits build on its current state, not on memory of a previous one.

## What not to do

- Do not add features not listed in the current batch prompt.
- Do not refactor, rename, or restructure anything without explicit confirmation.
- Do not describe a `BACKLOG.md` edit as something for me to apply. Make the edit, then tell me what changed.

---

This is a high-level orchestration strategy. You are essentially building a Control Plane (your .md files) to manage an Execution Engine (Claude Code).
