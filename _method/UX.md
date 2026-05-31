# UX.md — Sovereign Implementer User Experience

Every entry describes a functionality as the user (non-coder) experiences it, and why the user needs it. Entries must correspond to something in the current build — plans belong in `BACKLOG.md`. Only decided content lives here; open questions and placeholders belong in `BACKLOG.md` as planning batches.

## Project context

A Claude Code plugin that gives non-coders a structured workflow for building apps with Claude. The user knows what their app should be but needs guardrails to keep Claude aligned across sessions. The plugin provides phase-based orchestration (planning, build, close, git), markdown design documents that act as guardrails, and mechanical enforcement via hooks that Claude cannot override.

## UX principles for Sovereign Implementer

These inform every design decision. If a proposed change conflicts with a principle, flag the conflict before building.

1. **Mechanical enforcement over behavioral requests.** Hooks enforce rules that Claude can't override. Behavioral instructions alone degrade over long sessions — the plugin designs around this by making critical constraints deterministic rather than advisory.

2. **Demand-loaded context.** Procedure docs load only when the active phase needs them, preserving context window for actual work. Heavy documentation is necessary but reading it all at once leaves no room to build.

3. **Non-coders own the spec, Claude owns the code.** Source-of-truth docs (UX.md, additional docs) describe what gets built. Claude cannot edit them during builds — changes must wait for planning. This prevents spec drift mid-implementation.

4. **Every feature traces to a rationale.** Nothing gets built without a "user needs this because..." line. This protects against scope creep and ensures every feature can be justified to the project's users.

## Functionalities

### Setup workflow

The user opens Claude Code in a project folder and runs `/sovsetup`. The plugin detects the folder's state (empty, existing code, foreign docs, already managed) and runs the matching dialogue. For empty folders, it scaffolds spine docs and walks five prompts: product overview, UX principles, core functionalities, first batch sketch, and language.

The user needs this because getting the right doc structure in place requires knowledge of the method's conventions that a non-coder shouldn't have to learn upfront.

### Session-open orientation

When a session starts, the plugin automatically presents a status summary: build batch counts, next batch name and goal, pending tests, red flags, and any open questions. The user sees where things stand without having to ask.

The user needs this because sessions are stateless — nothing carries from the previous session's in-memory context. The status summary replaces having to remember or re-read BACKLOG manually.

### Planning sessions

The user runs `/sovplan` to do structural planning (reorder, split, merge, or rescope batches), `/sovdeliberate` to work through accumulated open questions, or `/sovideate` to explore new ideas. Source-of-truth docs are directly editable during planning.

The user needs this because planning and building need different editing permissions — trying to do both at once leads to spec drift mid-implementation.

### Build workflow

The user runs `/sovrecap` to review a batch's file list and test plan, `/sovbuild` to lock the batch and start building, `/sovclose` to run quality gates and record-keeping, and `/sovgit` for commit/tag/push. Each skill is a named entry point that loads the right procedure.

The user needs this because without the workflow, builds lose structure: tests get skipped, MANIFEST falls behind, and the build-log record that future sessions depend on never gets written.

### Test-confirmation gate

After a build ships, the user tests and confirms results — either through guided `/sovtest` walkthroughs or independently. The plugin blocks the next build batch until all previous test rows are explicitly confirmed (Pass, Fail, or Skipped with reason). Bulk confirmations don't count.

The user needs this because without per-row read-back, test rows get bulk-confirmed without being verified, and bugs compound across builds.

### Phase-aware editing

During planning, source-of-truth docs (UX.md, additional docs) are open for editing; source code is locked. During builds, the opposite: source code on the batch file list is open; source-of-truth docs are locked (with a `[PROPOSED EDIT PENDING]` carve-out for queuing changes).

The user needs this because mixing design changes with implementation creates spec drift that's invisible until it compounds. Separate phases enforce deliberation before commitment.

### Safety net

The plugin detects unadopted folders with existing work and blocks destructive edits until the user runs `/sovsetup`. Destructive git commands (`reset --hard`, `push --force`) are blocked by hooks. An unclosed-build commit guard prevents orphaned build snapshots.

The user needs this because a non-coder may not recognize when Claude is about to do something destructive — the guards prevent work loss without requiring git knowledge.

### Rollback

The user runs `/sovrevert` to undo a build that went wrong, restoring the project to the last committed state. No git knowledge required.

The user needs this because recovering from a bad build typically requires git commands that a non-coder wouldn't know how to run safely.

### Doc compression

The user runs `/sovtersify` to compress verbose docs. The skill triages by size, flags wrong-home content and verbose prose, and walks through compression one target at a time.

The user needs this because as docs grow they consume more context window, leaving less room for actual work. Compression recovers context budget.

### Research

The user runs `/sovresearch` to trigger an external information search. The plugin assesses the current work, identifies a gap where research would improve a decision, drafts a query with criteria, and waits for approval before executing. Results are filed to `_method/research/search-queries/` for future reference.

The user needs this because decisions often depend on external facts (API behavior, platform constraints, competing approaches) that Claude shouldn't guess at — structured research prevents building on wrong assumptions.

### Method explanation

The user runs `/sovexplain` to ask about the method. Three question types: "what does my project do" (reads MANIFEST capabilities summary), "how do I do X" (routes to the matching skill or procedure), and "why is X this way" (looks up design rationale).

The user needs this because the method has many moving parts and a non-coder shouldn't have to read the full spec docs to understand what's happening or why.

## Proposed edits pending

Claude-queued entries or updates. Each block describes the change, its origin, and whether it replaces or adds. Apply during planning, then delete. Starts empty.

Format: `DOC-STRUCTURE.md` → *Proposed edits pending sections*.

---
*Sovereign Implementer — Version 108.*
