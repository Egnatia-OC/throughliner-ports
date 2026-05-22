# Document structure specifications

*Mode: planning, migration.*

Structural specs for the project's documents — required sections, entry shape, rules for additional source-of-truth docs. Not loaded every session.

Method terms (planning batch, build batch, Serves line, source-of-truth doc, etc.) are defined in `VOCABULARY.md` (sibling of this file in `plugin/docs/`). Each subagent body's *First action — load the project's current state* section names what that phase reads.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the three spine docs don't cover — e.g. a Claude/MCP project may need `SYSTEM-PROMPT.md`; a copy-driven project may need `COPY.md`. Spine docs remain the spine — additional docs sit alongside. The project decides the doc's purpose, audience, and name.

Same structural rules as `UX.md` apply:

- **Read-only in Claude Code.** See `universal-behaviour.md` → *Editing surfaces*.
- **No placeholders, no soft gestures.** Source-of-truth docs describe decided behaviour. Don't write placeholders (`[TO FILL IN]`, `[Open: ...]`) or sentences that gesture at undecidedness ("currently undecided", "pending decision", "to be revisited", "see `BACKLOG.md`"). Open-question status lives in `BACKLOG.md` only. If a default applies while a question is being resolved, state it plainly without flagging it as provisional.
- **Intent level, not implementation.** Describe what the user (or doc consumer, e.g. Claude for a system-prompt doc) experiences and why — not how it's wired.
- **Folding planning answers.** Planning batches whose resolutions describe behaviour for the additional doc fold into *it*, not `UX.md`. The planning batch in `BACKLOG.md` should say so at setup so the destination is clear at fold-in time.
- **Build batches in the additional doc's domain** add a `Serves <DOC>: ...` line alongside or instead of `Serves UX.md: ...`, naming the entry the batch implements.

Starter shape: `ADDITIONAL-DOC-TEMPLATE.md` — copy, rename, adapt. Includes a *Fold-ins pending* section at the bottom — see *Fold-ins pending sections* below.

## UX.md structure

Every project's `UX.md` follows this shape. Copy these headers at project start; fill in as the project develops.

**Header.** Brief statement of what `UX.md` does, plus two rules: (1) every entry must correspond to something experienceable in the current build; (2) only decided behaviour belongs — open questions live in `BACKLOG.md` as planning batches, not here as placeholders.

**Project context.** One paragraph: what the app is, what it does, what distinguishes it from existing apps. Sits between header and UX principles. Filled in once project identity is settled.

**UX principles.** Three to six project-specific principles informing every design decision. Each: one-line claim plus a few sentences of reasoning. Act as guardrails — flag conflicts before building. Project-specific, not method-wide.

**Functionalities.** One entry per functionality. Required shape:

> **Feature name**
> One paragraph describing how the user experiences this feature.
> The user needs this because... [rationale tying to a UX principle or user context].

**Optional: Risk accepted.** When a feature has a known downside that's been weighed and chosen, end the entry with a `**Risk accepted:**` line stating the downside in one or two lines — e.g. the cost of a simplification, a deliberate omission, a signed-off trade-off. Use only for consciously-taken downsides, not general caveats.

**Cross-references.** Where features compose, link by entry name in italics: *(see Drag-target icons)*. Encouraged where features genuinely compose; don't duplicate content. If two entries keep cross-referencing for basic context, consider whether they're really one entry.

**Nested entries.** Most entries are flat top-level. If a parent has sub-areas with distinct user-facing rationale, each sub-area can be its own entry, named **Parent → Sub-area** (e.g. `Settings → Day begins at`). Use sparingly: if a sub-control's rationale matches the parent's, fold it in instead.

**Scope: intent-level only.** UX.md describes features and behaviours at user-intent level — what I came to do, plus distinct app behaviours with user-facing rationale. Not every visible UI element. Not implementation details. Not standard platform conventions. The "user needs this because..." line is the test — if you can't write it, it doesn't belong.

If a feature's behaviour isn't decided, it doesn't belong here — it belongs in `BACKLOG.md` as a planning batch. (See *Additional source-of-truth docs* → "No placeholders, no soft gestures" — same rule applies.)

**Non-GUI projects.** UX.md works for any project, not only apps with a visual interface. For CLI tools, backend services, MCP servers, data pipelines, plugins, and scripts: the "user" is whoever the project's audience is — an operator, an integrating developer, a downstream system. The "experience" is whatever that audience observes: a response, an exit code, a log line, a generated file, a hook firing correctly. Write entries the same way — one paragraph describing how the audience experiences the behaviour, plus the "the user needs this because…" line tying it to a principle. The structure doesn't change; only the concrete examples do.

**Fold-ins pending section.** A `## Fold-ins pending` section sits at the bottom of `UX.md`, after all Functionalities entries. See *Fold-ins pending sections* below for the shared rules.

## MANIFEST.md structure

**Header.** Brief statement of what `MANIFEST.md` is: a glossary of named codebase elements, maintained by Claude during builds, not for cover-to-cover reading.

Starts empty. The entry-format reminder lives in an HTML comment so the file stays clean until the first build.

**Entries.** A flat list, alphabetical by name. One line each:

> - **[Name]** (`path/to/file.ext`) — [one-line plain-English description of what this is and does]

Include things the user might plausibly ask about: components, screens, services, modules, files with discrete purpose. Skip trivial helpers, internal utilities, boilerplate.

If the flat list becomes hard to scan, switch to alphabetical sections by area.

**Paths field.** The optional `(path)` in parentheses after the entry name is the runtime anchor for the V39 read-before-edit gate in `pre_tool_use.py`. When an `Edit`/`Write`/`MultiEdit` targets a file whose path matches a MANIFEST entry's paths field, the hook denies the first attempt with the MANIFEST entry and `UX.md`'s Functionalities entry headings inlined in the deny reason — Claude retries with the context in hand. Retries succeed because the hook scans the session transcript for a prior block-once deny on the same file (no state file). Entries that omit the paths field skip the gate silently. Full rule wording: `universal-behaviour.md` → *Required behaviours* → *Check MANIFEST.md and UX.md before working on a feature*.

**Paths-field shape.**

- **Single file.** `` (`app/src/TaskCard.kt`) ``.
- **Multi-file, list shape.** `` (`a.kt`, `b.kt`) ``.
- **Multi-file, directory shape.** `` (`app/src/settings/`) `` — trailing slash signals directory match; any file under that prefix counts.
- **No path.** Omit the parens entirely for entries that don't correspond to a file (a cross-component flow, a named UX state). Such entries skip the gate.

**Migration is incremental.** The after-build subagent populates the paths field on any MANIFEST entry it creates or updates during a build (`after-build.md` → *Work loop* step 1). Legacy entries without paths stay skipped by the gate until something touches them. `/setup` case 4 (refresh) offers a one-time backfill pass — see `setup.md` for the dialogue.

**Fold-ins pending section.** A `## Fold-ins pending` section sits at the bottom of `MANIFEST.md`, after all entries. See *Fold-ins pending sections* below for the shared rules.

## TEST-LOG.md structure

**Header.** Brief statement of what `TEST-LOG.md` is: a row-per-test record of every shipped batch's outcomes, maintained by Claude during builds (rows added when a batch ships) and planning (rows confirmed per-row via the test-session-close read-back). The test-confirmation gate gates new builds against unconfirmed rows. The five protocol rules live across the plugin: *Never infer completion* and *Do not invoke the batch-executor* in `universal-behaviour.md` → *Required behaviours* / *Prohibited behaviours*; Pass / Fail / Skipped definitions in `VOCABULARY.md`; per-row read-back and retest-after-change drift check in `planning.md` → *Close the previous build's test session* and *Drift checks — always run*.

Starts empty. Entry-format reminder lives in an HTML comment until the first build.

**Columns.** Eight, in this order:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID (`001`, `002`, ...). Never reused. |
| **Date** | YYYY-MM-DD of the row. Row-per-event: a status flip appends a new row; the old stays intact (see *Pruning rule* below). |
| **Session** | The build-batch session. Project-internal tag (`v26`, `v27`) **or** YYYY-MM-DD if the project doesn't tag. The mechanism only needs temporal ordering. |
| **Component** | The named element tested. Matches a `MANIFEST.md` entry where possible; plain English if cross-component (e.g. a user flow spanning components). |
| **Test Description** | What was checked, in one sentence. Specific enough to re-run from this alone. |
| **Status** | `Pass`, `Fail`, `Skipped`, or blank. Blank means the test session is **open** for this row — scoped by *After every build* but not yet user-confirmed. |
| **Confirmed Explicitly** | `Yes (YYYY-MM-DD)` or `No`. Tripwire for Rule 1 ("Never infer completion"). Reaches `Yes` only when the user names this specific row in the planning read-back; bulk confirmations ("all others good") don't count. |
| **User Notes** | Observations, surprises, reason if Skipped (required by Rule 4), regression context if Fail, anything else worth keeping. Tight prose. |

**Ordering.** Newest-first. New rows append at the top of the table body, directly below the header separator (`|---|...|`), pushing earlier rows downward. Within a single batch's append (one after-build run), rows go in recap order — lowest `#` at the top of that batch's block — so the user reads them top-to-bottom in the order they tested. A reader looking for the most recent batch's outcomes opens the file and reads from the top. *Existing rows in projects whose `TEST-LOG.md` predates this rule stay where they are — newest-first applies to new appends only.*

**Pruning rule (phase-based, not session-based).** A row's validity ends when its component is substantially changed or removed — not after N sessions or M days.

- **Substantial change → status flips by appending a new row.** Drift check 5 (`planning.md` → *Drift checks — always run*, fifth check) flags rows whose components have changed since the row's Date. The flip appends a new row (at the top, per *Ordering* above): today's date, status `Skipped`, `Confirmed Explicitly: Yes` once the user confirms, User Notes naming the change. The original row stays where it was — "passed at the time" is worth keeping as history.
- **Component removed → row marked Superseded** in Status, with User Notes pointing to the BUILD-LOG entry that removed it. Rare; only when the test description no longer makes sense post-removal.

**Template.** `templates/TEST-LOG-TEMPLATE.md` (mirrored at `plugin/templates/TEST-LOG-TEMPLATE.md`) is empty by default — header, an HTML comment with the canonical entry format and Status / Confirmed Explicitly vocabularies, then the empty table. The comment stays at the top as a permanent format reminder; rows append below it at the top of the table body, per *Ordering* above. No placeholder row — same convention as `MANIFEST.md`.

## BUILD-LOG.md structure

**Header.** Brief statement of what `BUILD-LOG.md` is: a running record of decisions, changes, and reasoning for every build, newest-first. Maintained by Claude during builds (the after-build subagent writes one entry per completed batch). Not for cover-to-cover reading.

Starts empty. Entry-format reminder lives in an HTML comment until the first build.

**Entries.** One per build, newest first. Each entry:

```markdown
## <Session> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Reference TEST-LOG row range rather than restating test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping; focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the plan expected — a bug, a wrong assumption, an external fact discovered mid-build.

**Carried forward.** Items raised but not done, with destination (which planning batch, BACKLOG entry, or "not pursued — reason").
```

**Session identifier.** Matches `TEST-LOG.md`'s `Session` column convention — project-internal tag (e.g. `V27`) if the project keeps tags, `YYYY-MM-DD` otherwise. The after-build subagent uses the same *Session identification* logic for both.

**Ordering.** Newest-first. A reader looking for recent context opens the file and reads from the top.

**Maintenance.** After-build writes one entry per completed batch. The planning subagent reads for session identification (test-confirmation gate hook fallback). Entries are permanent — not pruned, not edited after the fact. If a later build invalidates a decision recorded in an earlier entry, the later entry says so in its own *Pivots and surprises*; the earlier entry stays as-is.

**Template.** `templates/BUILD-LOG-TEMPLATE.md` (mirrored at `plugin/templates/BUILD-LOG-TEMPLATE.md`) is empty by default — header and an HTML comment with the canonical entry format. Same convention as `MANIFEST-TEMPLATE.md` and `TEST-LOG-TEMPLATE.md`.

## planning/drafts/ folder

**Location.** `planning/drafts/<topic>.md` — project root relative. Created by `/setup` scaffold (empty directory).

**Purpose.** Destination-agnostic carryover for substantive chat content not yet ready for a specific doc. Complements fold-in sections on source-of-truth docs (destination-specific content queued for fold-in — see *Fold-ins pending sections* below). Drafts hold everything else: comparison tables, structural sketches, protocol rules, column shapes, option matrices — content that has value for a future session but doesn't yet have a clear home.

**Lifecycle.** Written during builds or planning when content is "good enough to walk away from" — the bar is preservation, not polish. Deleted when consumed (folded into a spec, a source-of-truth doc, or a BACKLOG batch) — in the same session as the consumption, so the file and its destination stay in sync. Dead-end drafts are pruned with a one-line note in the next `BUILD-LOG.md` entry.

**Format.** One file per topic, kebab-case filename (e.g. `settings-panel-layout.md`, `notification-channel-options.md`). No required internal shape — the content is pre-decision, so no template.

**Access.** Read/write to Claude. No locking — drafts are working material, not source-of-truth docs.

## Fold-ins pending sections

Every read-only source-of-truth doc (`UX.md`, `MANIFEST.md`, and any additional source-of-truth docs) carries a `## Fold-ins pending` section at its bottom. This is where Claude queues proposed content it cannot write directly into the doc's main body (because the doc is locked). The user folds the content in by hand during the next planning session, then deletes the block.

**Placement.** The fold-in section is always the last section in the doc, immediately before the `---` separator and method-version footer. Nothing comes after it except the footer.

**Block format.** Each pending block is a blockquote:

> `**`[FOLD-IN PENDING]`**` `<DOC>.md` — [one-line description of the proposed change]. [Proposed text or shape of the change, inline or as an indented sub-quote]. **Action:** [replace | add] — [if replace: "replace the section between **[heading X]** and **[heading Y]**"; if add: "place this new section after **[heading Z]**"]. Surfaced [date]; origin: [planning batch name | new-project route | migration route | mid-build edit attempt].

Each block specifies whether it's a **replace** (swap the section between heading X and heading Y) or an **add** (place this new section after heading Z), so the user knows exactly where to put the content.

**Origins.** Fold-in blocks are created by any route that would otherwise write a read-only doc: planning-batch resolution, `/setup` new-project or migration routes, or a mid-build edit attempt intercepted by the PreToolUse hook.

**Lifecycle.** Empty by default. Blocks are removed once the user folds them into the destination doc's main body (or drops them). During planning sessions and `/setup`, the **preview-then-fold-in convention** applies (see `universal-behaviour.md` → *Editing surfaces*): the subagent previews the complete section in chat, waits for approval, writes the fold-in block, then prompts the user to fold in immediately rather than deferring.

**PreToolUse carve-out.** The fold-in section is the one part of a locked doc that Claude can edit. The PreToolUse hook allows edits that fall entirely within the fold-in section (between the `## Fold-ins pending` heading and the footer separator). This covers appending new blocks and removing blocks after the user confirms fold-in. Edits to any other part of the locked doc are still denied. The detection pattern mirrors V38's footer-stamp carve-out (`is_footer_only_edit()`): both use section-boundary markers to verify the edit stays within the allowed region.

**Migration from the centralised BACKLOG.md fold-in section.** Projects upgrading from a version where fold-in blocks lived in BACKLOG.md's centralised *Fold-ins pending* section: the planning subagent redistributes any existing blocks to their destination docs' fold-in sections during its normal planning-session work. No explicit `/setup` run needed.

## BACKLOG.md structure

`BACKLOG.md` consolidates everything deferred, in four sections in fixed order.

**Maintained by Claude during planning, not by the user.** Whenever a planning decision changes `BACKLOG.md` — adding, removing, reordering, splitting, or reclassifying an item or batch — Claude edits directly. The user reviews afterwards; doesn't apply.

**Header.** Brief statement of purpose, section order, and the maintenance rule (so a runtime reader of `BACKLOG.md` itself sees the rule too).

**Four sections, in this order:**

- **Red flags.** Security, privacy, data integrity, or safety concerns surfaced and explicitly deferred by the user. Empty by default. Each entry is a blockquote: `**`[RED FLAG]`**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Removed once addressed. Claude populates this section per the *Red flags — screen and surface* rule in `universal-behaviour.md` → *Required behaviours*.

  **Red flags are concerns parked outside any active work stream.** Concerns inside an active build batch live there until the batch ships. Concerns attached to a feature in a planning batch become questions inside that batch — not Red flags. Red flags are specifically concerns the user has explicitly chosen to defer with no active plan to address them.

- **Planning batches.** Two kinds of question live here. **(a)** Open questions that must resolve before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist (e.g. "should this app even have a search box?"). Each batch lists the questions and ends with a `Blocks:` line — either naming the build batch(es) it holds up, or `Blocks: scope decision — no build batch yet` for an existence question. Resolution: append the answer to the batch and add a corresponding `[FOLD-IN PENDING]` block to the destination doc's *Fold-ins pending* section (with this batch's name as *origin*). Leave the planning batch in place — the user removes it during the same planning session in which they fold the answer into the destination doc by hand. If a scope-existence batch resolves to "yes, build it," the planning batch may convert to or spawn a build batch at that point, in addition to the fold-in.

  **One planning batch per discrete decision.** If a message contains multiple unrelated feature requests or scope questions, create separate planning batches. Bundle only when two items are tightly coupled (deciding one inevitably decides the other). Unrelated items in a single batch create a batch whose `Blocks:` line can't cleanly name what it blocks and whose resolution can't fold into a single entry.

- **Build batches.** Engineering work, ordered top-to-bottom by priority. The top batch is the next build. Each batch: heading, list of changes, optional `Inputs:` line, `Files:` sub-section, then a `Serves UX.md: ...` line listing implemented entries (and/or `Serves <DOC>: ...` for additional source-of-truth docs). If a build batch's purpose is to carry an additional source-of-truth doc to its runtime destination rather than implement its content, the `Serves <DOC>:` line names the delivery mechanism instead of a section (e.g. `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt`). Each batch must be small enough to build and test in one session — if not, split during *Before build*, not during build. Completed batches are removed during the next planning session (see `planning.md` → *Procedure order* step 2). If a build session ends with the top batch partly done (files still `- [ ]`), the batch stays at the top with its tick state intact; next session resumes the remaining files.

Build batches must serve an entry in a source-of-truth doc — see `planning.md` → *How a new feature enters the project*. Red flags are the only deferred items that don't need such an entry; they live in `BACKLOG.md` regardless of scope.

**Change list — `[Requested]`/`[Suggested]` labels.** Each bullet in a build batch's change list may carry `[Requested]` (user asked) or `[Suggested]` (Claude proposed) immediately after the leading `- `, e.g. `- [Requested] Fix drag-to-postpone overshoot on tablet`. Labels are written by the planning subagent when the change enters BACKLOG.md, preserved by the before-build subagent when the batch is locked, and read by the after-build subagent for the build recap. The `Files:` sub-section does **not** carry labels — a single `[Requested]` change can touch many files, and a single file can absorb edits from both, so labels attach to changes, not files. `[Prerequisite, not in plan]` and `[Re-batch, not in plan]` carve-out labels are added by the batch-executor at recap time and don't appear in BACKLOG.md change-list bullets ahead of the build.

**`Inputs:` line.** An optional bullet list of non-standard resources the batch needs before starting work. Each entry: `` `<path or reference>` — <why this batch needs it> ``. Sits between the change list and the `Files:` sub-section. Standard docs (UX.md, BACKLOG.md, MANIFEST.md, CLAUDE.md) are omitted — they're read every session. Only list what's beyond the standard set: a research file, an open-questions entry, a draft, an additional source-of-truth doc, or an external reference. Written by the before-build subagent during batch lock-in; consumed by the batch-executor, which reads every named input before starting work.

**`Files:` sub-section.** A GitHub-style task list — one `- [ ]` per file, `- [x]` when done — of every file the batch will modify, each shaped `` - [ ] `<path>` — <one-sentence summary of the change in that file> ``. It is the build-time enforcement surface: the PreToolUse hook blocks `Edit`/`Write`/`MultiEdit` on any file not in the current batch's `Files:` list. Prerequisite carve-outs (a file added mid-build per `universal-behaviour.md` → *Prohibited behaviours* → *Two exceptions* → *Prerequisite carve-out*) are appended with a trailing `[Prerequisite, not in plan]` label, recording both presence and provenance.

**`Serves UX.md:` name matching.** Names on `Serves UX.md:` lines match `UX.md`'s Functionalities entries case-insensitively after whitespace-trim — `Serves UX.md: Dark Mode` matches `Dark mode`, but `Dark mode toggle` would not. The PreToolUse hook (in Claude Code) blocks build-batch edits whose `Serves UX.md:` line names entries that don't exist in `UX.md`. `Serves <ADDITIONAL>.md:` lines aren't yet hook-checked.

- **Open questions.** Questions worth tracking that aren't blocking a specific build batch. Each entry has a question title (as a heading), a paragraph framing the question, a *Why it matters* line with brief context, and a *Next step* line describing what would promote it to a planning batch or resolve it. The planning subagent scans this section at the start of every planning session and lists all entries with one-line summaries.

  Open questions are distinct from planning batches: a planning batch names what it blocks (`Blocks:` line) and its resolution directly unlocks a build; an open question is non-blocking parking for ideas that aren't yet tied to a specific build. When an open question matures to the point where it blocks something specific, promote it to a planning batch.

---
*No-code method — Version 45.*
