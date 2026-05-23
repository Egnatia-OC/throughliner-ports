# Document structure specifications

*Mode: planning, migration.*

Structural specs for the project's documents — required sections, entry shape, rules for additional source-of-truth docs. Not loaded every session.

Method terms (planning batch, build batch, Serves line, source-of-truth doc, etc.) are defined in `VOCABULARY.md` (sibling of this file in `plugin/docs/`). Each subagent body's *First action — load the project's current state* section names what that phase reads.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the three spine docs don't cover. Spine docs remain the spine — additional docs sit alongside. The project decides the doc's purpose, audience, and name.

**Common examples:**

- **`SYSTEM-PROMPT.md`** — for Claude/MCP projects. Describes the system prompt Claude receives at connection time. The audience is Claude-as-runtime, not the end user.
- **`COPY.md`** — for projects where user-facing text is itself the deliverable (marketing sites, onboarding flows, notification copy). Locks the words from mid-build drift.
- **`PATTERNS.md`** or **`CONVENTIONS.md`** — coding conventions, architectural patterns, test-writing style, file-naming rules. Describes how to build, not what to build. Useful when the project has established patterns Claude should follow consistently across builds.
- **`API.md`** — for projects exposing an API. Describes endpoints, payloads, and guarantees at intent level — what the integrating developer experiences, not implementation details.

These are suggestions, not a required set. If the project needs a source-of-truth doc not listed here, create one — same rules apply.

Same structural rules as `UX.md` apply:

- **Read-only in Claude Code.** See `universal-behaviour.md` → *Editing surfaces*.
- **No placeholders, no soft gestures.** Source-of-truth docs describe decided behaviour. Don't write placeholders (`[TO FILL IN]`, `[Open: ...]`) or sentences that gesture at undecidedness ("currently undecided", "pending decision", "to be revisited", "see `BACKLOG.md`"). Open-question status lives in `BACKLOG.md` only. If a default applies while a question is being resolved, state it plainly without flagging it as provisional.
- **Intent level, not implementation.** Describe what the user (or doc consumer, e.g. Claude for a system-prompt doc) experiences and why — not how it's wired.
- **Applying planning answers.** Planning batches whose resolutions describe behaviour for the additional doc go into *it*, not `UX.md`. The planning batch in `BACKLOG.md` should say so at setup so the destination is clear when applying the proposed edit.
- **Build batches in the additional doc's domain** add a `Serves <DOC>: ...` line alongside or instead of `Serves UX.md: ...`, naming the entry the batch implements.

Starter shape: `ADDITIONAL-DOC-TEMPLATE.md` — copy, rename, adapt. Includes a *Proposed edits pending* section at the bottom — see *Proposed edits pending sections* below.

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

**Proposed edits pending section.** A `## Proposed edits pending` section sits at the bottom of `UX.md`, after all Functionalities entries. See *Proposed edits pending sections* below for the shared rules.

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

**Proposed edits pending section.** A `## Proposed edits pending` section sits at the bottom of `MANIFEST.md`, after all entries. See *Proposed edits pending sections* below for the shared rules.

## TEST-LOG.md structure

**Header.** Brief statement of what `TEST-LOG.md` is: a row-per-test record of every shipped batch's outcomes, maintained by Claude during builds (rows added when a batch ships) and planning (rows confirmed per-row via the test-session-close read-back). The test-confirmation gate gates new builds against unconfirmed rows. The five protocol rules live across the plugin: *Never infer completion* and *Do not invoke the batch-executor* in `universal-behaviour.md` → *Required behaviours* / *Prohibited behaviours*; Pass / Fail / Skipped definitions in `VOCABULARY.md`; per-row read-back and retest-after-change drift check in `planning.md` → *Close the previous build's test session* and *Drift checks — always run*.

Starts empty. Entry-format reminder lives in an HTML comment until the first build.

**Columns.** Ten, in this order:

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID (`001`, `002`, ...). Never reused. |
| **Date** | YYYY-MM-DD of the row. Row-per-event: a status flip appends a new row; the old stays intact (see *Pruning rule* below). |
| **Session** | The build-batch session. Project-internal tag (`v26`, `v27`) **or** YYYY-MM-DD if the project doesn't tag. The mechanism only needs temporal ordering. |
| **Component** | The named element tested. Matches a `MANIFEST.md` entry where possible; plain English if cross-component (e.g. a user flow spanning components). |
| **Test Description** | What was checked, in one sentence. Specific enough to re-run from this alone. |
| **Type** | One of four test types: `Look and click`, `Run and read`, `Trigger and observe`, `Generate and inspect`. Definitions in `VOCABULARY.md` → *Test type*. |
| **Verifier** | `Claude` or `User`. Records who verified (or will verify) this row. Claude-verified rows are filled in during after-build's automated test pass; user-verified rows are confirmed during the planning read-back. The split is per-row, not per-type. |
| **Status** | `Pass`, `Fail`, `Skipped`, or blank. Blank means the test session is **open** for this row — scoped by *After every build* but not yet confirmed. For Claude-verified rows, Status is filled in by the after-build subagent. For user-verified rows, Status stays blank until the planning read-back. |
| **Confirmed Explicitly** | `Yes (YYYY-MM-DD)` or `No`. Tripwire for Rule 1 ("Never infer completion"). For user-verified rows: reaches `Yes` only when the user names this specific row in the planning read-back; bulk confirmations ("all others good") don't count. For Claude-verified rows: set to `Yes` by the after-build subagent when it fills in Status. |
| **Notes** | Observations, surprises, reason if Skipped (required by Rule 4), regression context if Fail, anything else worth keeping. Tight prose. For Claude-verified rows, the after-build subagent writes its verification evidence here (command output, check result, etc.). |

**Ordering.** Newest-first. New rows append at the top of the table body, directly below the header separator (`|---|...|`), pushing earlier rows downward. Within a single batch's append (one after-build run), rows go in recap order — lowest `#` at the top of that batch's block — so the user reads them top-to-bottom in the order they tested. A reader looking for the most recent batch's outcomes opens the file and reads from the top. *Existing rows in projects whose `TEST-LOG.md` predates this rule stay where they are — newest-first applies to new appends only.*

**Pruning rule (phase-based, not session-based).** A row's validity ends when its component is substantially changed or removed — not after N sessions or M days. Two mechanisms handle the two cases differently.

- **Substantial change → status flips by appending a new row.** Drift check 5 (`planning.md` → *Drift checks — always run*, fifth check) flags rows whose components have changed since the row's Date. The flip appends a new row (at the top, per *Ordering* above): today's date, status `Skipped`, `Confirmed Explicitly: Yes` once the user confirms, Notes naming the change. The original row stays — the component still exists in MANIFEST.md, so the row's history has value until the next retest.
- **Component removed → rows deleted by the planning subagent.** At each planning session, the planning subagent's pruning step (step 2c in `planning.md`) cross-references TEST-LOG rows against MANIFEST.md. Rows whose Component matches no current MANIFEST entry — and are not cross-component descriptive phrases — are deleted. Rows with Status `Superseded` (a legacy status from pre-V53 pruning rules) are also deleted. The subagent surfaces what was pruned in chat. Git history preserves the deleted rows for audit purposes. Cross-component rows (plain-English descriptions of flows spanning multiple components) are exempt from automatic pruning.

**Template.** `templates/TEST-LOG-TEMPLATE.md` (mirrored at `plugin/templates/TEST-LOG-TEMPLATE.md`) is empty by default — header, an HTML comment with the canonical entry format and Status / Confirmed Explicitly / Type / Verifier vocabularies, then the empty table. The comment stays at the top as a permanent format reminder; rows append below it at the top of the table body, per *Ordering* above. No placeholder row — same convention as `MANIFEST.md`.

**Backwards compatibility.** Projects with existing 8-column TEST-LOG rows (pre-V48) get migrated on `/setup` case 4 (refresh): the `Type` column is backfilled to `Look and click` and the `Verifier` column to `User` for all existing rows. The `User Notes` column header is renamed to `Notes`. This is a one-time mechanical migration.

## Build log structure

**Location.** `build-log/` folder at the project root. One file per build, plus a lightweight `INDEX.md` carrying the build order. Created by `/setup` scaffold.

**INDEX.md.** Header, an HTML comment with the canonical formats, then a newest-first bullet list of per-build file references. Each entry:

> `- `NNN-batch-name.md` — YYYY-MM-DD — One-line summary`

The after-build subagent appends one line per build at the top of the list (below the header and comment block), pushing earlier entries downward.

**Per-build files.** One file per build, named `NNN-batch-name.md` (three-digit sequential number allocated via `plugin/scripts/allocate_number.py`, plus a kebab-case suffix derived from the batch heading). Each file:

```markdown
# <Session> — YYYY-MM-DD — One-line summary

**What shipped.** Short plain-English paragraph describing concrete deliverables. Reference TEST-LOG row range rather than restating test outcomes. Reference research files by path rather than embedding their content.

**Decisions taken and why.** Two or three bullets on load-bearing decisions — what was chosen, alternatives considered, what tipped the call. Skip housekeeping; focus on choices shaping future sessions.

**Pivots and surprises.** Anything that turned out differently than the plan expected — a bug, a wrong assumption, an external fact discovered mid-build.

**Carried forward.** Items raised but not done, with destination (which planning batch, BACKLOG entry, or "not pursued — reason").

## Performance

- **Batch completion:** Complete / Partial (handoff)
- **Files in batch:** N
- **Carve-outs:** None / N prerequisite, N re-batch
- **Claude-verified tests:** N Pass, N Fail (of N total)
- **User-verified tests:** N pending
- **Session notes:** (optional — added by the user after testing)
```

**Session identifier.** Matches `TEST-LOG.md`'s `Session` column convention — project-internal tag (e.g. `V27`) if the project keeps tags, `YYYY-MM-DD` otherwise. The after-build subagent uses the same *Session identification* logic for both.

**Ordering.** INDEX.md is newest-first. A reader scanning the full history opens INDEX.md; a reader looking for the most recent build's context opens the first referenced file.

**Performance section.** Each per-build file ends with a `## Performance` section carrying structured mechanical measures from the build: batch completion status, file count, carve-out count, Claude-verified test results (Pass/Fail), and user-verified test count. Written by the after-build subagent from data it already has at recap time — no additional input needed. An optional `**Session notes:**` line can be added by the user after testing for subjective observations (what worked, what didn't, hypotheses for next time). The mechanical measures are queryable via grep across all build entries.

**Maintenance.** After-build writes one per-build file and appends one index line per completed batch. The planning subagent reads the index for session identification (test-confirmation gate hook fallback). Entries are permanent — not pruned, not edited after the fact. If a later build invalidates a decision recorded in an earlier entry, the later entry says so in its own *Pivots and surprises*; the earlier entry stays as-is.

**Research cross-references.** Build entries reference research files by path (e.g. `` `research/drag-library-comparison.md` ``) rather than embedding their content. Research lives in `research/`; build entries link to it.

**Template.** `plugin/templates/build-log/INDEX-TEMPLATE.md` is the scaffold source — header, HTML comment with canonical formats, footer. Same convention as `MANIFEST-TEMPLATE.md` and `TEST-LOG-TEMPLATE.md`. The `CLAUDE.md` path block entry `"BUILD-LOG.md"` points to `build-log/INDEX.md`.

## planning/drafts/ folder

**Location.** `planning/drafts/<topic>.md` — project root relative. Created by `/setup` scaffold (empty directory).

**Purpose.** Destination-agnostic carryover for substantive chat content not yet ready for a specific doc. Complements proposed-edits sections on source-of-truth docs (destination-specific content queued as proposed edits — see *Proposed edits pending sections* below). Drafts hold everything else: comparison tables, structural sketches, protocol rules, column shapes, option matrices — content that has value for a future session but doesn't yet have a clear home.

**Lifecycle.** Written during builds or planning when content is "good enough to walk away from" — the bar is preservation, not polish. Deleted when consumed (incorporated into a spec, a source-of-truth doc, or a BACKLOG batch) — in the same session as the consumption, so the file and its destination stay in sync. Dead-end drafts are pruned with a one-line note in the next build-log entry.

**Format.** One file per topic, kebab-case filename (e.g. `settings-panel-layout.md`, `notification-channel-options.md`). No required internal shape — the content is pre-decision, so no template.

**Access.** Read/write to Claude. No locking — drafts are working material, not source-of-truth docs.

## research/ folder

**Location.** `research/<topic>.md` — project root relative. Created by `/setup` scaffold (empty directory).

**Purpose.** Home for findings from any research Claude conducts during a session. When Claude investigates an external fact — a library's behaviour, an API's status, a platform capability, anything it could verify rather than guess — it saves findings to `research/<topic>.md` and mentions briefly in chat what it found and where it saved it.

**Naming convention.** Free-form kebab-case filenames (e.g. `marketplace-options.md`, `drag-library-comparison.md`). No date prefix — the file's own content carries date context where relevant.

**Lifecycle.** Written when Claude conducts research; persists indefinitely as reference material. Not deleted when consumed — research stays available for future sessions. No MANIFEST tracking, no BACKLOG entries, no proposed-edit mechanism. Zero maintenance burden.

**Referencing from build batches.** Research files are valid entries on a build batch's `Inputs:` line when the batch depends on what the research found (e.g. `` `research/drag-library-comparison.md` — informs which library to use ``).

**Access.** Read/write to Claude. Not a source-of-truth doc — no locking, no structural spec beyond the filename convention.

## Proposed edits pending sections

Every read-only source-of-truth doc (`UX.md`, `MANIFEST.md`, and any additional source-of-truth docs) carries a `## Proposed edits pending` section at its bottom. This is where Claude queues proposed content it cannot write directly into the doc's main body (because the doc is locked). The user applies the proposed edit by hand during the next planning session, then deletes the block.

**Placement.** The proposed-edits section is always the last section in the doc, immediately before the `---` separator and method-version footer. Nothing comes after it except the footer.

**Block format.** Each pending block is a blockquote:

> `**`[PROPOSED EDIT PENDING]`**` `<DOC>.md` — [one-line description of the proposed change]. [Proposed text or shape of the change, inline or as an indented sub-quote]. **Action:** [replace | add] — [if replace: "replace the section between **[heading X]** and **[heading Y]**"; if add: "place this new section after **[heading Z]**"]. Surfaced [date]; origin: [planning batch name | new-project route | migration route | mid-build edit attempt].

Each block specifies whether it's a **replace** (swap the section between heading X and heading Y) or an **add** (place this new section after heading Z), so the user knows exactly where to put the content.

**Origins.** Proposed-edit blocks are created by any route that would otherwise write a read-only doc: planning-batch resolution, `/setup` new-project or migration routes, or a mid-build edit attempt intercepted by the PreToolUse hook.

**Lifecycle.** Empty by default. Blocks are removed once the user applies them to the destination doc's main body (or drops them). During planning sessions and `/setup`, the **preview-then-apply convention** applies (see `universal-behaviour.md` → *Editing surfaces*): the subagent previews the complete section in chat, waits for approval, writes the proposed-edit block, then prompts the user to apply it immediately rather than deferring.

**PreToolUse carve-out.** The proposed-edits section is the one part of a locked doc that Claude can edit. The PreToolUse hook allows edits that fall entirely within the proposed-edits section (between the `## Proposed edits pending` heading and the footer separator). This covers appending new blocks and removing blocks after the user confirms. Edits to any other part of the locked doc are still denied. The detection pattern mirrors V38's footer-stamp carve-out (`is_footer_only_edit()`): both use section-boundary markers to verify the edit stays within the allowed region.

**Migration from the centralised BACKLOG proposed-edits section.** Projects upgrading from a version where proposed-edit blocks lived in BACKLOG's centralised *Proposed edits pending* section: the planning subagent redistributes any existing blocks to their destination docs' proposed-edits sections during its normal planning-session work. No explicit `/setup` run needed.

## BACKLOG structure

BACKLOG consolidates everything deferred. Two formats, auto-detected by the plugin:

- **Single-file (legacy):** a single `BACKLOG.md` with everything inline, including full build-batch content in the `## Build batches` section. The `CLAUDE.md` path block entry `"BACKLOG.md"` points to `BACKLOG.md`.
- **Folder (V48+):** a `BACKLOG/` directory containing `INDEX.md` (with the build-order reference list, Red flags, Planning batches, and Open questions) and per-batch `.md` files (one per build batch). The path block entry `"BACKLOG.md"` points to `BACKLOG/INDEX.md`. New projects created by `/setup` use folder mode by default.

**Maintained by Claude during planning, not by the user.** Whenever a planning decision changes BACKLOG — adding, removing, reordering, splitting, or reclassifying an item or batch — Claude edits directly. The user reviews afterwards; doesn't apply.

**Header.** Brief statement of purpose, section order, and the maintenance rule.

**Four sections, in this order** (in INDEX.md for folder mode, in BACKLOG.md for single-file mode):

- **Red flags.** Security, privacy, data integrity, or safety concerns surfaced and explicitly deferred by the user. Empty by default. Each entry is a blockquote: `**`[RED FLAG]`**` [one-line description]. Found during [batch name] ([date]). Fix: [shortest possible fix]. Removed once addressed. Claude populates this section per the *Red flags — screen and surface* rule in `universal-behaviour.md` → *Required behaviours*.

  **Red flags are concerns parked outside any active work stream.** Concerns inside an active build batch live there until the batch ships. Concerns attached to a feature in a planning batch become questions inside that batch — not Red flags. Red flags are specifically concerns the user has explicitly chosen to defer with no active plan to address them. In folder mode, this section lives in INDEX.md.

- **Planning batches.** Two kinds of question live here. **(a)** Open questions that must resolve before some build batch can run. **(b)** Scope-existence questions whose resolution decides whether a build batch should ever exist (e.g. "should this app even have a search box?"). Each batch lists the questions and ends with a `Blocks:` line — either naming the build batch(es) it holds up, or `Blocks: scope decision — no build batch yet` for an existence question. Resolution: append the answer to the batch and add a corresponding `[PROPOSED EDIT PENDING]` block to the destination doc's *Proposed edits pending* section (with this batch's name as *origin*). Leave the planning batch in place — the user removes it during the same planning session in which they apply the proposed edit to the destination doc by hand. If a scope-existence batch resolves to "yes, build it," the planning batch may convert to or spawn a build batch at that point, in addition to the proposed edit.

  **One planning batch per discrete decision.** If a message contains multiple unrelated feature requests or scope questions, create separate planning batches. Bundle only when two items are tightly coupled (deciding one inevitably decides the other). Unrelated items in a single batch create a batch whose `Blocks:` line can't cleanly name what it blocks and whose resolution can't cleanly map to a single entry.

- **Build batches.** Engineering work, ordered top-to-bottom by priority. The top batch is the next build (after any one currently in progress). Each batch has two regions: **scope context** (Goal through Dependencies/Red flags — the strategic frame) and **build operations** (Changes through Serves — the tactical execution surface). Each batch must be small enough to build and test in one session — if not, split during *Before build*, not during build. Completed batches are removed during the next planning session (see `planning.md` → *Procedure order* step 2). If a build session ends with the top batch partly done (files still `- [ ]`), the batch stays at the top with its tick state intact; next session resumes the remaining files.

  Build batches must serve an entry in a source-of-truth doc — see `planning.md` → *How a new feature enters the project*. Red flags are the only deferred items that don't need such an entry; they live in BACKLOG regardless of scope. If a build batch's purpose is to carry an additional source-of-truth doc to its runtime destination rather than implement its content, the `Serves <DOC>:` line names the delivery mechanism instead of a section (e.g. `Serves SYSTEM-PROMPT.md: connection-time delivery as Claude's system prompt`).

  **Two batch formats.** In single-file mode, batches are inline under `## Build batches` with `### Batch:` headings. In folder mode (V48+), each batch lives in its own file (`NNNN-batch-name.md`) in the `BACKLOG/` directory, with `INDEX.md`'s `## Build batches` section carrying a reference list for ordering:

  ```
  ## Build batches

  - `0001-first-batch-name.md` — one-line description
  - `0002-second-batch-name.md` — one-line description
  ```

  The `NNNN` number is allocated at creation time (via `plugin/scripts/allocate_number.py`) and never changes. Reordering means moving lines in the reference list, not renaming files.

  **Batch structure — full shape.** Sections appear in this order within each batch. The scope-context sections are written by the planning subagent when the batch is created; the build-operations sections are populated by the before-build subagent during batch lock-in. In folder mode, the heading is `# <name>` (H1); in single-file mode it's `### Batch: <name>`.

  ```
  # [short descriptive name]                        ← folder mode (H1)
  ### Batch: [short descriptive name]               ← single-file mode

  **Goal.** [One paragraph — why this batch exists, what will be different when it ships.]

  **Outputs.** [Prose — what changes the user will experience after the batch ships.]

  **Success criteria.** [Observable, testable conditions for knowing the batch succeeded.]

  **Decisions to make this batch.** [Unresolved scope questions within this batch. Omit if all decisions are made.]

  **Dependencies.** [What this batch needs from outside itself. Omit if none.]

  **Red flags.** [Security/privacy/data-integrity concerns for this batch. Only present when detected.]

  Changes:
  - [Requested] [Change description — one line]
  - [Suggested] [Change description]

  Inputs:
  - `[path/to/resource]` — [why this batch needs it]

  Files:
  - [ ] `[path/to/file]` — [one-sentence summary of the change]

  Tests:
  - [Test description] [Look and click] [User]

  Serves UX.md: [entry name(s)].
  ```

  **`Handoff notes:` block.** An optional free-text block added at the bottom of the batch (before the `Serves` line) when a session ends mid-build and the user accepts the PreCompact hook's recommendation to prepare a handoff rather than allow context compaction. Contains decisions made, approach chosen, alternatives rejected, and edge cases discovered — build-time context the next session needs to resume cleanly. Written by Claude during the handoff step; stripped by the after-build subagent when the batch completes (the build-log entry captures the narrative). Not present in new batches; appears only during partially-delivered builds. Full protocol: `universal-behaviour.md` → *Session handoff*.

  **Scope-context sections.** Five sections frame the batch's purpose. The first three (Goal, Outputs, Success criteria) are always present; the last two (Decisions to make this batch, Dependencies) are omitted when empty. A sixth conditional section (Red flags) appears only when the planning subagent detects security-shaped scope (see *Red flags sub-section* below).

  - **Goal.** One paragraph: why does this batch exist? Written in plain English, naming the user-facing change.
  - **Outputs.** Prose describing what changes the user will experience after the batch ships. The pre-build pin between a planning conversation and the eventual UX.md entry — prose matches that pipeline stage.
  - **Success criteria.** Observable, testable conditions. How the no-coder (or Claude, for automatable tests) will know the batch succeeded. Prose or a short list; avoid `- ` bullet format to keep the parser's change-list extraction clean.
  - **Decisions to make this batch.** Unresolved scope questions within this batch — things that must be decided during the build, not parked as open questions. Distinct from the section-level Open questions (parking lot for non-blocking items) and from planning batches (blocking questions with a `Blocks:` line). Omit entirely if all decisions are made at planning time.
  - **Dependencies.** What this batch needs from outside itself: another batch shipped first, a planning batch resolved, an external resource provisioned. Peer to `Blocks:` on planning batches — `Blocks:` points forward ("resolving me unblocks X"), Dependencies points backward ("before starting me, Y must have happened"). Omit if none.

  **Red flags sub-section.** Appears only when the planning subagent detects security-shaped scope — the batch touches auth, secrets, PII, deletion of user data, payment, third-party API keys, or similar surfaces. Written by the planning subagent at batch-creation time; not a static always-present section. Contains specific concerns and mitigations for this batch's scope. Distinct from the top-level Red flags section in BACKLOG (which holds concerns deferred with no active plan); this sub-section holds concerns attached to an active batch.

  **`Changes:` delimiter.** The `Changes:` line separates scope-context sections from the change list. Required for new batches; the parser falls back to legacy behaviour (extract all `- ` bullets before `Files:`) for batches without it. The delimiter keeps the parser's change-list extraction clean when scope sections contain bullet-formatted content.

  **Change list — `[Requested]`/`[Suggested]` labels.** Each bullet in a build batch's change list carries `[Requested]` (user asked) or `[Suggested]` (Claude proposed) immediately after the leading `- `, e.g. `- [Requested] Fix drag-to-postpone overshoot on tablet`. Labels are written by the planning subagent when the change enters BACKLOG, preserved by the before-build subagent when the batch is locked, and read by the after-build subagent for the build recap. The `Files:` sub-section does **not** carry labels — a single `[Requested]` change can touch many files, and a single file can absorb edits from both, so labels attach to changes, not files. `[Prerequisite, not in plan]` and `[Re-batch, not in plan]` carve-out labels are added by the batch-executor at recap time and don't appear in BACKLOG change-list bullets ahead of the build.

**`Inputs:` line.** An optional bullet list of non-standard resources the batch needs before starting work. Each entry: `` `<path or reference>` — <why this batch needs it> ``. Sits between the change list and the `Files:` sub-section. Standard docs (UX.md, BACKLOG, MANIFEST.md, CLAUDE.md) are omitted — they're read every session. Only list what's beyond the standard set: a research file, an open-questions entry, a draft, an additional source-of-truth doc, or an external reference. Written by the before-build subagent during batch lock-in; consumed by the batch-executor, which reads every named input before starting work.

**`Files:` sub-section.** A GitHub-style task list — one `- [ ]` per file, `- [x]` when done — of every file the batch will modify, each shaped `` - [ ] `<path>` — <one-sentence summary of the change in that file> ``. It is the build-time enforcement surface: the PreToolUse hook blocks `Edit`/`Write`/`MultiEdit` on any file not in the current batch's `Files:` list. Prerequisite carve-outs (a file added mid-build per `universal-behaviour.md` → *Prohibited behaviours* → *Two exceptions* → *Prerequisite carve-out*) are appended with a trailing `[Prerequisite, not in plan]` label, recording both presence and provenance.

**`Tests:` sub-section.** An optional list of tests the batch should verify once built, each with a test type and verifier assignment. Sits after the `Files:` sub-section, before the `Serves` line. Written by the before-build subagent during batch lock-in. Each entry:

> `- <Test description> [<Type>] [<Verifier>]`

Where `<Type>` is one of `Look and click`, `Run and read`, `Trigger and observe`, `Generate and inspect`; and `<Verifier>` is `Claude` or `User`. Example:

> `- Run the CLI with --help flag and verify the output lists all commands [Run and read] [Claude]`
> `- Open the settings screen and verify the toggle appears [Look and click] [User]`

The after-build subagent uses the `Tests:` sub-section as the basis for opening the test session — each entry becomes one TEST-LOG row with the specified type and verifier. If the `Tests:` sub-section is absent (legacy batches, or batches where the before-build subagent determined no pre-specification was needed), the after-build subagent derives tests from the build recap as before, defaulting to `Look and click` type and `User` verifier.

**`Serves <DOC>:` name matching.** Names on `Serves UX.md:` lines match `UX.md`'s Functionalities entries (### headings) case-insensitively after whitespace-trim — `Serves UX.md: Dark Mode` matches `Dark mode`, but `Dark mode toggle` would not. Names on `Serves <ADDITIONAL>.md:` lines match the additional doc's ## headings (excluding structural sections like Proposed edits pending) using the same case-insensitive whitespace-trimmed match. The PreToolUse hook blocks build-batch edits whose `Serves` line names entries that don't exist in the named doc. Writable docs (BACKLOG.md, MANIFEST.md, TEST-LOG.md, BUILD-LOG.md) are skipped — only locked source-of-truth docs are validated.

- **Open questions.** Questions worth tracking that aren't blocking a specific build batch. Each entry has a question title (as a heading), a paragraph framing the question, a *Why it matters* line with brief context, and a *Next step* line describing what would promote it to a planning batch or resolve it. The planning subagent scans this section at the start of every planning session and lists all entries with one-line summaries.

  Open questions are distinct from planning batches: a planning batch names what it blocks (`Blocks:` line) and its resolution directly unlocks a build; an open question is non-blocking parking for ideas that aren't yet tied to a specific build. When an open question matures to the point where it blocks something specific, promote it to a planning batch.

---
*No-code method — Version 55.*
