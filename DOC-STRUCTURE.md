# Document structure specifications

*Mode: planning, migration.*

Structural specs for the project's documents — required sections, entry shape, rules for additional source-of-truth docs. Not loaded every session.

Method terms (planning batch, build batch, Serves line, source-of-truth doc, etc.) are defined in `NO-CODE-METHOD.md` → *Vocabulary*. For each doc's role, see → *The documents that describe my projects*. For when to read each, see → *When to read each document*.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the three spine docs don't cover — e.g. a Claude/MCP project may need `SYSTEM-PROMPT.md`; a copy-driven project may need `COPY.md`. Spine docs remain the spine — additional docs sit alongside. The project decides the doc's purpose, audience, and name.

Same structural rules as `UX.md` apply:

- **Read-only in Claude Code.** See `NO-CODE-METHOD.md` → *Editing surfaces*.
- **No placeholders, no soft gestures.** Source-of-truth docs describe decided behaviour. Don't write placeholders (`[TO FILL IN]`, `[Open: ...]`) or sentences that gesture at undecidedness ("currently undecided", "pending decision", "to be revisited", "see `BACKLOG.md`"). Open-question status lives in `BACKLOG.md` only. If a default applies while a question is being resolved, state it plainly without flagging it as provisional.
- **Intent level, not implementation.** Describe what the user (or doc consumer, e.g. Claude for a system-prompt doc) experiences and why — not how it's wired.
- **Folding planning answers.** Planning batches whose resolutions describe behaviour for the additional doc fold into *it*, not `UX.md`. The planning batch in `BACKLOG.md` should say so at setup so the destination is clear at fold-in time.
- **Build batches in the additional doc's domain** add a `Serves <DOC>: ...` line alongside or instead of `Serves UX.md: ...`, naming the entry the batch implements.

Starter shape: `ADDITIONAL-DOC-TEMPLATE.md` — copy, rename, adapt.

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

## MANIFEST.md structure

**Header.** Brief statement of what `MANIFEST.md` is: a glossary of named codebase elements, maintained by Claude during builds, not for cover-to-cover reading.

Starts empty. The entry-format reminder lives in an HTML comment so the file stays clean until the first build.

**Entries.** A flat list, alphabetical by name. One line each:

> - **[Name]** (`path/to/file.ext`) — [one-line plain-English description of what this is and does]

Include things the user might plausibly ask about: components, screens, services, modules, files with discrete purpose. Skip trivial helpers, internal utilities, boilerplate.

If the flat list becomes hard to scan, switch to alphabetical sections by area.

**Paths field.** The optional `(path)` in parentheses after the entry name is what makes the read-before-edit discipline checkable. When Claude is about to edit a file with a matching MANIFEST entry, the rule (`NO-CODE-METHOD.md` → *Required of Claude* → "Before working on a feature...") requires Claude to have the MANIFEST entry and the relevant `UX.md` entry in mind first. In Claude Code the PreToolUse hook enforces this by denying the first attempt with both inlined in the deny reason; Claude retries with the context in hand and the retry succeeds. Entries without a paths field skip the gate silently.

**Paths-field shape.**

- **Single file.** `` (`app/src/TaskCard.kt`) ``.
- **Multi-file, list shape.** `` (`a.kt`, `b.kt`) ``.
- **Multi-file, directory shape.** `` (`app/src/settings/`) `` — trailing slash signals directory match; any file under that prefix counts.
- **No path.** Omit the parens entirely for entries that don't correspond to a file (a cross-component flow, a named UX state). Such entries skip the gate.

**Migration is incremental.** During *After every build*, Claude populates the paths field on any MANIFEST entry it creates or updates. Legacy entries without paths stay skipped by the gate until something touches them. Project initialization or refresh routes (in Claude Code: `/adopt` case 4) offer a one-time backfill pass.

## TEST-LOG.md structure

**Header.** Brief statement of what `TEST-LOG.md` is: a row-per-test record of every shipped batch's outcomes, maintained by Claude during builds (rows added when a batch ships) and planning (rows confirmed per-row via the test-session-close read-back). The test-confirmation gate gates new builds against unconfirmed rows. For the five protocol rules, see `NO-CODE-METHOD.md` → *Method contract* (Rules 1, 3), *Vocabulary* (Rule 4: Pass / Fail / Skipped definitions), and *During planning* (Rule 2: test-session-close read-back; Rule 5: retest-after-change drift check).

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

- **Substantial change → status flips by appending a new row.** Drift check 4 (`NO-CODE-METHOD.md` → *During planning*) flags rows whose components have changed since the row's Date. The flip appends a new row (at the top, per *Ordering* above): today's date, status `Skipped`, `Confirmed Explicitly: Yes` once the user confirms, User Notes naming the change. The original row stays where it was — "passed at the time" is worth keeping as history.
- **Component removed → row marked Superseded** in Status, with User Notes pointing to the BUILD-LOG entry that removed it. Rare; only when the test description no longer makes sense post-removal.

**Template.** `templates/TEST-LOG-TEMPLATE.md` (mirrored at `plugin/templates/TEST-LOG-TEMPLATE.md`) is empty by default — header, an HTML comment with the canonical entry format and Status / Confirmed Explicitly vocabularies, then the empty table. The comment stays at the top as a permanent format reminder; rows append below it at the top of the table body, per *Ordering* above. No placeholder row — same convention as `MANIFEST.md`.

## BUILD-LOG.md structure

**Header.** Brief statement of what `BUILD-LOG.md` is: a running record of decisions, changes, and reasoning for every build, newest-first. Maintained by Claude during builds (after-build writes one entry per completed batch). Not for cover-to-cover reading.

Starts empty. Entry-format reminder lives in an HTML comment until the first build.

**Entries.** One per build, newest first. Each entry:

```markdown
## <Session> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Reference TEST-LOG row range rather than restating test outcomes.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping; focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the plan expected — a bug, a wrong assumption, an external fact discovered mid-build.

**Carried forward.** Items raised but not done, with destination (which planning batch, BACKLOG entry, or "not pursued — reason").
```

**Session identifier.** Matches `TEST-LOG.md`'s `Session` column convention — project-internal tag (e.g. `V27`) if the project keeps tags, `YYYY-MM-DD` otherwise. The after-build phase uses the same session-identification logic for both.

**Ordering.** Newest-first. A reader looking for recent context opens the file and reads from the top.

**Maintenance.** After-build writes one entry per completed batch. Planning reads for session identification (test-confirmation gate fallback). Entries are permanent — not pruned, not edited after the fact. If a later build invalidates a decision recorded in an earlier entry, the later entry says so in its own *Pivots and surprises*; the earlier entry stays as-is.

**Template.** `templates/BUILD-LOG-TEMPLATE.md` is empty by default — header and an HTML comment with the canonical entry format. Same convention as `MANIFEST-TEMPLATE.md` and `TEST-LOG-TEMPLATE.md`.

## planning/drafts/ folder

**Location.** `planning/drafts/<topic>.md` — project root relative. Created by `/adopt` scaffold (empty directory).

**Purpose.** Destination-agnostic carryover for substantive chat content not yet ready for a specific doc. Complements `BACKLOG.md`'s *Fold-ins pending* section, which is destination-specific (source-of-truth doc content queued for fold-in). Drafts hold everything else: comparison tables, structural sketches, protocol rules, column shapes, option matrices — content that has value for a future session but doesn't yet have a clear home.

**Lifecycle.** Written during builds or planning when content is "good enough to walk away from" — the bar is preservation, not polish. Deleted when consumed (folded into a spec, a source-of-truth doc, or a BACKLOG batch) — in the same session as the consumption, so the file and its destination stay in sync. Dead-end drafts are pruned with a one-line note in the next `BUILD-LOG.md` entry.

**Format.** One file per topic, kebab-case filename (e.g. `settings-panel-layout.md`, `notification-channel-options.md`). No required internal shape — the content is pre-decision, so no template.

**Access.** Read/write to Claude. No locking — drafts are working material, not source-of-truth docs.

## BACKLOG.md structure

`BACKLOG.md` consolidates everything deferred, in four sections in fixed order.

**Maintained by Claude during planning, not by the user.** Whenever a planning decision changes `BACKLOG.md` — adding, removing, reordering, splitting, or reclassifying an item or batch — Claude edits directly. The user reviews afterwards; doesn't apply.

**Header.** Brief statement of purpose, section order, and the maintenance rule (so a runtime reader of `BACKLOG.md` itself sees the rule too).

**Four sections, in this order:**

- **Red flags.** Security, privacy, data integrity, or safety concerns surfaced and explicitly deferred by the user. Empty by default. Each entry is a blockquote: `**`[RED FLAG]`**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Removed once addressed. Claude populates this section per the "Red flags — screen and surface" rule under *Method contract → Required of Claude* in `NO-CODE-METHOD.md`.

  **Red flags are concerns parked outside any active work stream.** Concerns inside an active build batch live there until the batch ships. Concerns attached to a feature in a planning batch become questions inside that batch — not Red flags. Red flags are specifically concerns the user has explicitly chosen to defer with no active plan to address them.

- **Fold-ins pending.** Proposed source-of-truth content Claude Code has formed but cannot write directly to read-only docs (`UX.md` and additional source-of-truth docs). All fold-in blocks live here regardless of origin — new-project route, migration route, planning-batch resolution, or a mid-build edit attempt intercepted by the PreToolUse hook. Each block is a blockquote:

  > `**`[FOLD-IN PENDING]`**` `<DOC>.md` — [one-line description of the proposed change]. [Proposed text or shape of the change, inline or as an indented sub-quote]. Surfaced [date]; origin: [planning batch name | new-project route | migration route | mid-build edit attempt].

  Empty by default. Removed once the user folds them into the destination doc by hand during a planning session (or drops them). Full mechanism — when blocks get created and how they reconcile back — in `NO-CODE-METHOD.md` → *Editing surfaces*.

- **Planning batches.** Two kinds of question live here. **(a)** Open questions that must resolve before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist (e.g. "should this app even have a search box?"). Each batch lists the questions and ends with a `Blocks:` line — either naming the build batch(es) it holds up, or `Blocks: scope decision — no build batch yet` for an existence question. Resolution: append the answer to the batch and add a corresponding `[FOLD-IN PENDING]` block (with this batch's name as *origin*). Leave the planning batch in place — the user removes it during the same planning session in which they fold the answer into `UX.md` (or the relevant additional source-of-truth doc) by hand. If a scope-existence batch resolves to "yes, build it," the planning batch may convert to or spawn a build batch at that point, in addition to the fold-in.

  **One planning batch per discrete decision.** If a message contains multiple unrelated feature requests or scope questions, create separate planning batches. Bundle only when two items are tightly coupled (deciding one inevitably decides the other). Unrelated items in a single batch create a batch whose `Blocks:` line can't cleanly name what it blocks and whose resolution can't fold into a single entry.

- **Build batches.** Engineering work, ordered top-to-bottom by priority. The top batch is the next build. Each batch: heading, list of changes, `Files:` sub-section, then a `Serves UX.md: ...` line listing implemented entries (and/or `Serves <DOC>: ...` for additional source-of-truth docs). If a build batch's purpose is to carry an additional source-of-truth doc to its runtime destination rather than implement its content, the `Serves <DOC>:` line names the delivery mechanism instead of a section (e.g. `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt`). Each batch must be small enough to build and test in one session — if not, split during *Before build*, not during build. Completed batches are removed during the next planning session (see `NO-CODE-METHOD.md` → *During planning*). If a build session ends with the top batch partly done (files still `- [ ]`), the batch stays at the top with its tick state intact; next session resumes the remaining files.

Build batches must serve an entry in a source-of-truth doc — see `NO-CODE-METHOD.md` → *How a new feature enters the project*. Red flags are the only deferred items that don't need such an entry; they live in `BACKLOG.md` regardless of scope.

**Change list — `[Requested]`/`[Suggested]` labels.** Each bullet in a build batch's change list may carry `[Requested]` (user asked) or `[Suggested]` (Claude proposed) immediately after the leading `- `, e.g. `- [Requested] Fix drag-to-postpone overshoot on tablet`. Labels are written by the planning subagent when the change enters BACKLOG.md, preserved by the before-build subagent when the batch is locked, and read by the after-build subagent for the build recap. The `Files:` sub-section does **not** carry labels — a single `[Requested]` change can touch many files, and a single file can absorb edits from both, so labels attach to changes, not files. `[Prerequisite, not in plan]` and `[Re-batch, not in plan]` carve-out labels are added by the batch-executor at recap time and don't appear in BACKLOG.md change-list bullets ahead of the build.

**`Files:` sub-section.** A GitHub-style task list — one `- [ ]` per file, `- [x]` when done — of every file the batch will modify, each shaped `` - [ ] `<path>` — <one-sentence summary of the change in that file> ``. It is the build-time enforcement surface: the PreToolUse hook blocks `Edit`/`Write`/`MultiEdit` on any file not in the current batch's `Files:` list. Prerequisite carve-outs (a file added mid-build per `NO-CODE-METHOD.md` → *Prohibited of Claude* → prerequisite exception) are appended with a trailing `[Prerequisite, not in plan]` label, recording both presence and provenance.

**`Serves UX.md:` name matching.** Names on `Serves UX.md:` lines match `UX.md`'s Functionalities entries case-insensitively after whitespace-trim — `Serves UX.md: Dark Mode` matches `Dark mode`, but `Dark mode toggle` would not. The PreToolUse hook (in Claude Code) blocks build-batch edits whose `Serves UX.md:` line names entries that don't exist in `UX.md`. `Serves <ADDITIONAL>.md:` lines aren't yet hook-checked.

---
*No-code method — Version 39.*
