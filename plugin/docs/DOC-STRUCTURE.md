# Document structure specifications

*Mode: planning, migration.*

Structural specs for project documents — required sections, entry shapes, additional doc rules. Not loaded every session.

Method terms defined in `VOCABULARY.md` (sibling). Each subagent body's *First action* section names what that phase reads.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the spine docs don't cover. Common examples: `SYSTEM-PROMPT.md` (Claude/MCP projects), `COPY.md` (user-facing text is the deliverable), `PATTERNS.md` (coding conventions), `API.md` (endpoint/payload specs). Not a required set — create as needed.

Same structural rules as `UX.md`:
- **Read-only in Claude Code.** See `universal-behaviour.md` → *Editing surfaces*.
- **No placeholders.** Source-of-truth docs describe decided behaviour. Open-question status lives in BACKLOG only.
- **Intent level, not implementation.**
- **Planning answers** for the additional doc go into *it*, not `UX.md`.
- **Build batches** add `Serves <DOC>:` alongside/instead of `Serves UX.md:`.

Starter shape: `ADDITIONAL-DOC-TEMPLATE.md`. Includes a *Proposed edits pending* section.

## UX.md structure

**Header.** What UX.md does, plus two rules: every entry corresponds to something experienceable; only decided behaviour belongs.

**Project context.** One paragraph: what the app is, what distinguishes it.

**UX principles.** 3–6 project-specific principles. Each: one-line claim + reasoning. Act as guardrails.

**Functionalities.** One entry per functionality:

> **Feature name**
> One paragraph: how the user experiences this.
> The user needs this because... [rationale].

**Optional: Risk accepted.** Known downside weighed and chosen — one or two lines at entry end. Only for conscious trade-offs.

**Cross-references.** Link by entry name in italics: *(see Drag-target icons)*. Don't duplicate content.

**Nested entries.** If a parent has sub-areas with distinct rationale: **Parent → Sub-area**. Use sparingly.

**Scope: intent-level only.** Features at user-intent level. Not every UI element, not implementation details. The "user needs this because..." line is the test.

Undecided behaviour → BACKLOG as a planning batch, not here.

**Non-GUI projects.** Works for CLI tools, backends, MCP servers, plugins. The "user" is whoever the audience is; the "experience" is what they observe.

**Proposed edits pending section.** `## Proposed edits pending` at the bottom. See *Proposed edits pending sections* below.

## MANIFEST.md structure

**Header.** Glossary of named codebase elements, maintained by Claude during builds.

Starts empty. Entry-format reminder in HTML comment.

**Entries.** Flat, alphabetical. One line each:

> - **[Name]** (`path/to/file.ext`) — [plain-English description]

Include things the user might ask about. Skip trivial helpers and boilerplate.

**Paths field.** The `(path)` is the anchor for the V39 read-before-edit gate. When an edit targets a MANIFEST-pathed file, the hook denies the first attempt with the entry inlined; retry succeeds (hook scans for prior block-once deny). Entries without paths skip the gate.

**Paths-field shape:**
- Single file: `(app/src/TaskCard.kt)`
- Multi-file list: `(a.kt, b.kt)`
- Directory: `(app/src/settings/)` — trailing slash = prefix match
- No path: omit parens for non-file entries

**Migration is incremental.** After-build populates paths on create/update. Legacy entries stay skipped until touched. `/setup` case 4 offers backfill.

**Proposed edits pending section.** At bottom. See below.

## TEST-LOG.md structure

**Header.** Row-per-test record of build outcomes. Maintained by Claude during builds (rows added) and planning (rows confirmed per-row). The test-confirmation gate gates new builds against unconfirmed rows.

Starts empty. Format reminder in HTML comment.

**Columns (10):**

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID. Never reused. |
| **Date** | YYYY-MM-DD. Row-per-event: status flips append new rows. |
| **Session** | Build-batch session tag or YYYY-MM-DD. |
| **Component** | Matches MANIFEST entry where possible; plain English if cross-component. |
| **Test Description** | One sentence, re-runnable. |
| **Type** | `Look and click` / `Run and read` / `Trigger and observe` / `Generate and inspect`. |
| **Verifier** | `Claude` or `User`. |
| **Status** | `Pass` / `Fail` / `Skipped` / blank (open). Claude rows filled by after-build; user rows stay blank until planning read-back. |
| **Confirmed Explicitly** | `Yes (YYYY-MM-DD)` or `No`. Bulk confirmations don't count for specific rows. |
| **Notes** | Observations, skip reason (required), regression context. Tight prose. |

**Ordering.** Newest-first. New rows at top of table body. Within a batch: recap order (lowest # at top).

**Pruning rule.** Phase-based, not time-based.
- **Substantial change** → drift check 5 flags; status flip via new appended row.
- **Component removed** → planning subagent deletes rows with no MANIFEST match (step 2c). `Superseded` rows also deleted. Cross-component rows exempt. Git preserves history.

**Template.** Empty by default — header, HTML comment, empty table. No placeholder row.

**Backwards compatibility.** 8-column (pre-V48) migrated on `/setup` case 4: Type→`Look and click`, Verifier→`User`.

## Build log structure

**Location.** `build-log/` at project root. One file per build + `INDEX.md`.

**INDEX.md.** Header, HTML comment, newest-first bullet list:
> `- \`NNN-batch-name.md\` — YYYY-MM-DD — Summary`

After-build prepends one line per build.

**Per-build files.** `NNN-batch-name.md`:

```markdown
# <Session> — YYYY-MM-DD — Summary

**What shipped.** <deliverables; reference TEST-LOG rows>
**Decisions taken and why.** <load-bearing decisions>
**Pivots and surprises.** <if any>
**Carried forward.** <if any>

## Performance
- **Batch completion:** Complete / Partial (handoff)
- **Files in batch:** N
- **Carve-outs:** None / N prerequisite, N re-batch
- **Claude-verified tests:** N Pass, N Fail (of N total)
- **User-verified tests:** N pending
- **Session notes:** (optional — user-added)
```

**Session identifier.** Matches TEST-LOG convention.

**Ordering.** INDEX.md newest-first.

**Performance section.** Mechanical measures, queryable via grep. Optional `Session notes:` for user observations.

**Maintenance.** Entries permanent. Later builds reference earlier ones in their own Pivots section.

**Research cross-references.** Reference by path, don't embed.

**Template.** `plugin/templates/build-log/INDEX-TEMPLATE.md`. Path block: `"BUILD-LOG.md"` → `build-log/INDEX.md`.

## planning/drafts/ folder

`planning/drafts/<topic>.md`. Created by `/setup`. Destination-agnostic carryover for substantive content not yet ready for a specific doc — comparison tables, structural sketches, option matrices. Written at "good enough to walk away from"; deleted when consumed; dead-ends pruned with build-log note. One file per topic, kebab-case. Read/write to Claude, no locking.

## research/ folder

`research/<topic>.md`. Created by `/setup`. Home for research findings. When Claude investigates an external fact, it saves here and mentions in chat. Kebab-case filenames, no date prefix. Persists indefinitely — not deleted when consumed. No MANIFEST tracking, no BACKLOG entries. Zero maintenance. Valid on `Inputs:` lines. Read/write, no locking.

## Proposed edits pending sections

Every read-only doc (`UX.md`, `MANIFEST.md`, additional docs) carries `## Proposed edits pending` at its bottom — where Claude queues content it can't write directly.

**Placement.** Last section, immediately before footer.

**Block format.** Blockquote:
> `**[PROPOSED EDIT PENDING]**` `<DOC>.md` — [description]. [Proposed text]. **Action:** [replace | add] — [target heading details]. Surfaced [date]; origin: [source].

**Origins.** Planning-batch resolution, `/setup`, or intercepted mid-build edit.

**Lifecycle.** Empty by default. Removed after user applies. During planning/`/setup`, preview-then-apply convention applies.

**PreToolUse carve-out.** Edits within the proposed-edits section are allowed. Edits elsewhere in the locked doc are denied.

**Migration.** Pre-V43 centralised blocks in BACKLOG → redistributed to destination docs by planning subagent.

## BACKLOG structure

Two formats, auto-detected:
- **Single-file (legacy):** `BACKLOG.md` with everything inline. Path block → `BACKLOG.md`.
- **Folder (V48+):** `BACKLOG/` with `INDEX.md` + per-batch files. Path block → `BACKLOG/INDEX.md`. Default for new projects.

**Maintained by Claude during planning.** Claude edits directly; user reviews.

**Four sections, in order** (INDEX.md or BACKLOG.md):

- **Red flags.** Deferred security/privacy/data-integrity concerns. Each: `**[RED FLAG]**` [description]. Found during [batch] ([date]). Fix: [fix]. Concerns inside active batches stay there; concerns attached to planned features become batch questions. Red flags are specifically concerns deferred with no active plan.

- **Planning batches.** Two kinds: (a) blocking questions for a build batch, (b) scope-existence questions. Each ends with `Blocks:` line. Resolution: append answer + `[PROPOSED EDIT PENDING]` in destination doc. One batch per discrete decision.

- **Build batches.** Engineering work, priority-ordered. Top = next build. Two regions: scope context (Goal→Dependencies/Red flags) and build operations (Changes→Serves). Must be small enough to build and test in one session. Completed batches removed next planning session.

  Folder mode: per-batch files (`NNNN-name.md`), INDEX.md carries reference list. Single-file: inline `### Batch:` headings.

  **Batch structure — full shape:**
  ```
  # [name]                                          ← folder (H1)
  ### Batch: [name]                                  ← single-file

  Status: [queued|active|parked|shipped]             ← optional; absent = queued

  **Goal.** [Why this batch exists.]
  **Outputs.** [What changes the user experiences.]
  **Success criteria.** [Observable conditions for success.]
  **Decisions to make this batch.** [Unresolved questions. Omit if resolved.]
  **Dependencies.** [What's needed from outside. Omit if none.]
  **Red flags.** [Security concerns. Only when detected.]

  Changes:
  - [Requested] [Change description]
  - [Suggested] [Change description]

  Inputs:
  - `[path]` — [why needed]

  Files:
  - [ ] `[path]` — [summary]

  Tests:
  - [Description] [Look and click] [User]

  Serves UX.md: [entry name(s)].
  ```

  **Handoff notes:** Optional block before Serves line during mid-build handoffs. Contains build-time context for resume. Stripped by after-build when batch completes.

  **Status: line.** Tracks batch lifecycle. Four values: `queued` (default — no line needed), `active` (locked by before-build), `parked` (paused by planning), `shipped` (completed by after-build). Position: first line of batch body, before Goal. The parser skips `shipped` and `parked` batches when finding the top build batch. Absent = queued.

  **Scope-context sections.** Goal/Outputs/Success criteria always present. Decisions/Dependencies omitted when empty. Red flags only when security-shaped scope detected.

  **Changes: delimiter.** Separates scope-context from change list. Required for new batches; parser falls back for legacy.

  **Change-list labels.** `[Requested]`/`[Suggested]` after `- `. Written by planning, preserved by before-build, read by after-build for recap. Labels on changes, not files. Carve-out labels (`[Prerequisite]`/`[Re-batch]`) are recap-time only.

  **Inputs: line.** Non-standard resources between change list and Files:. Standard docs omitted.

  **Files: sub-section.** `- [ ]`/`- [x]` task list per file. PreToolUse blocks edits to files not on the list.

  **Tests: sub-section.** `- <desc> [<Type>] [<Verifier>]` per test. After-build uses these for TEST-LOG rows.

  **Serves name matching.** Case-insensitive whitespace-trimmed match against doc headings. PreToolUse blocks mismatches on locked docs.

- **Open questions.** Non-blocking parking. Each: question title, framing paragraph, *Why it matters*, *Next step* (trigger for promotion/resolution). Distinct from planning batches (which name what they block).

---
*No-code method — Version 65.*
