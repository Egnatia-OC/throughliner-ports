# Document structure specifications

*Mode: planning, migration.*

Structural specs for project documents — required sections, entry shapes, additional doc rules. Not loaded every session.

Method terms defined in `VOCABULARY.md` (sibling). Each procedure doc's opening section names what that phase reads.

## Product overview (CLAUDE.md)

`## Product overview` at the top of CLAUDE.md, before the path block. Four fields:

- **What it is.** One-sentence product description.
- **Who it's for.** Intended user or audience.
- **What friction it solves.** The tension or problem the product addresses.
- **Milestones.** What the user is working toward, with rough timeframes if known.

**When written.** `/sovsetup` populates through conversation — Claude asks, user answers, Claude writes. Not a form. Also seeds UX.md's *Project context*.

**When updated.** Planning sessions, when milestones shift or the product's framing evolves. Editable in both phases (CLAUDE.md is always read/write).

**Existing projects.** Pre-date projects won't have it. `/sovsetup` case 4 detects the missing section and backfills.

## Language (CLAUDE.md)

`## Language` in CLAUDE.md, between Product overview and the path block. Single field:

- **Language: \<language\>.** The language Claude uses for responses, recaps, and doc content. Defaults to English. Control tokens (`Status:`, `Changes:`, `Serves UX.md:`, `Confirmed Explicitly:`, `[SECURITY]`) stay English regardless — hooks regex-match them.

**When written.** `/sovsetup` asks a 5th question; default is the language the user used for Q1–Q4.

**When updated.** Anytime. CLAUDE.md is always read/write.

**Existing projects.** `/sovsetup` case 4 adds the section if missing.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the spine docs don't cover. Common examples: `SYSTEM-PROMPT.md` (Claude/MCP projects), `COPY.md` (user-facing text is the deliverable), `PATTERNS.md` (coding conventions), `API.md` (endpoint/payload specs). Not a required set — create as needed.

Same structural rules as `UX.md`:
- **Phase-aware editing.** Editable during planning; locked during build (`[PROPOSED EDIT PENDING]` carve-out). See `universal-behaviour.md` → *Editing surfaces — phase-aware*.
- **No placeholders.** Source-of-truth docs describe decided behaviour. Open questions live in BACKLOG only.
- **Intent level, not implementation.**
- **Planning answers** go into *this doc*, not `UX.md`.
- **Build batches** add `Serves <DOC>:` alongside/instead of `Serves UX.md:`.

Starter shape: `ADDITIONAL-DOC-TEMPLATE.md`. Includes a *Proposed edits pending* section.

## UX.md structure

**Header.** What UX.md does, plus two rules: every entry corresponds to something experienceable; only decided behaviour belongs.

**Project context.** One paragraph: what the app is, what distinguishes it.

**UX principles.** Optional section. Project-specific principles, no fixed count. Each: one-line claim + reasoning. Act as guardrails. `/sovsetup` asks whether the user has any; if not, the section is omitted.

**Functionalities.** One entry per functionality:

> **Feature name**
> One paragraph: how the user experiences this.
> The user needs this because... [rationale].

**Optional: Risk accepted.** Known downside weighed and chosen — one or two lines at entry end. Conscious trade-offs only.

**Cross-references.** Link by entry name in italics: *(see Drag-target icons)*. Don't duplicate.

**Nested entries.** Sub-areas with distinct rationale: **Parent → Sub-area**. Use sparingly.

**Scope: intent-level only.** Features at user-intent level. Not every UI element, not implementation details. The "user needs this because..." line is the test.

Undecided behaviour → BACKLOG as a planning batch, not here.

**Non-GUI projects.** Works for CLI tools, backends, MCP servers, plugins. The "user" is whoever the audience is; the "experience" is what they observe.

**Proposed edits pending section.** `## Proposed edits pending` at the bottom. See *Proposed edits pending sections* below.

## MANIFEST.md structure

**Header.** Glossary of named codebase elements, maintained by Claude during builds.

Starts empty. Entry-format reminder in HTML comment.

**Capabilities summary.** `## Capabilities summary` section, between the header comment and the entries. One plain-English paragraph summarizing what the project has built — derived from entry names and descriptions. Generated/updated by `/sovclose` step 1b after each build. Starts as a placeholder comment; populated at first close. The MANIFEST proxy reproduces it verbatim so Claude reads it at session start for orientation without loading full MANIFEST.

**Entries.** Flat, alphabetical. One line each:

> - **[Name]** (`path/to/file.ext`) — [plain-English description]. *Rationale: [why it exists / vNN].*

The rationale field records why the component was built — one clause, max 15 words, followed by the session tag when it was introduced. Italic suffix keeps it visually distinct from the description. Existing entries without rationale remain valid (graceful migration).

Include things the user might ask about. Skip trivial helpers and boilerplate.

**Paths field.** The `(path)` anchors the read-before-edit gate — hook denies first edit to a pathed file with the entry inlined; retry succeeds. Entries without paths skip the gate. Shapes:
- Single file: `(app/src/TaskCard.kt)`
- Multi-file list: `(a.kt, b.kt)`
- Directory: `(app/src/settings/)` — trailing slash = prefix match
- No path: omit parens for non-file entries

**Migration is incremental.** After-build populates paths on create/update. Legacy entries skipped until touched. `/sovsetup` case 4 offers backfill.

**Proposed edits pending section.** At bottom. See below.

## TEST-LOG structure

**Location.** `_method/test-log/`. One file per build session. Test session index lives in `_method/BACKLOG.md` → `## Test sessions`. Legacy: flat `TEST-LOG.md` at project root or inside `_method/`.

**Index (BACKLOG.md → Test sessions).** Newest-first bullet list inside the `## Test sessions` section of `_method/BACKLOG.md`:
> `` - `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed) ``

`/sovclose` prepends one line per build. Path block: `"TEST-LOG.md"` → `_method/BACKLOG.md` (same file as `"BACKLOG.md"`).

**Per-session files.** `NNN-batch-name.md`:

```markdown
# Test session — <Session> — YYYY-MM-DD

| # | Date | Session | Component | Test Description | Type | Verifier | Status | Confirmed Explicitly | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 001 | ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

**Columns (10):**

| Column | Meaning |
|---|---|
| **#** | Stable three-digit ID. Never reused (global across all per-session files). |
| **Date** | YYYY-MM-DD. Row-per-event: status flips append new rows. |
| **Session** | Build-batch session tag or YYYY-MM-DD. |
| **Component** | Matches MANIFEST entry where possible; plain English if cross-component. |
| **Test Description** | One sentence, re-runnable. |
| **Type** | `Look and click` / `Run and read` / `Trigger and observe` / `Generate and inspect`. |
| **Verifier** | `Claude` or `User`. |
| **Status** | `Pass` / `Fail` / `Skipped` / blank (open). Claude rows filled by `/sovclose`; user rows stay blank until planning read-back. |
| **Confirmed Explicitly** | `Yes (YYYY-MM-DD)` or `No`. Bulk confirmations don't count for specific rows. |
| **Notes** | Observations, skip reason (required), regression context. Tight prose. |

**Session identifier.** Matches build-log convention.

**Ordering.** Index newest-first. Within a per-session file: recap order (lowest # at top).

**Pruning rule.** Phase-based, not time-based.
- **Substantial change** → drift check 5 flags; status flip via new appended row.
- **Component removed** → planning procedure deletes rows with no MANIFEST match (step 2c). `Superseded` rows also deleted. Cross-component rows exempt. Git preserves history.
- **Empty files** → when pruning empties a per-session file, delete it and remove its index line.

**Template.** Test session index section is part of `plugin/templates/BACKLOG-TEMPLATE.md`. Per-session file template: `plugin/templates/test-log/ENTRY-TEMPLATE.md`. Path block: `"TEST-LOG.md"` → `_method/BACKLOG.md`.

**Backwards compatibility.** Flat `TEST-LOG.md` still supported. 8-column (pre-V48) migrated on `/sovsetup` case 4: Type→`Look and click`, Verifier→`User`. Case 4 also migrates flat file → folder.

## Build log structure

**Location.** `_method/build-log/`. One file per build. Index lives at `_method/proxies/build-log.md` (the proxy IS the index). Legacy: `build-log/INDEX.md` at project root or inside `_method/`.

**Index (proxies/build-log.md).** Header, HTML comment, newest-first bullet list:
> `- \`NNN-batch-name.md\` — YYYY-MM-DD — Summary`

`/sovclose` prepends one line per session (both build and lighter close). Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`.

**Per-build files.** `NNN-batch-name.md`:

```markdown
# <Session> — YYYY-MM-DD — Summary

**What shipped.** <deliverables; reference TEST-LOG rows>
**Decisions taken and why.** <load-bearing decisions>
**Pivots and surprises.** <if any>

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

**Performance section.** Mechanical measures, queryable via grep. Optional `Session notes:` for user observations. Included for post-build entries only — lighter-close entries (planning, ideation, deliberation) omit it.

**Maintenance.** Entries permanent. Later builds reference earlier ones in their own Pivots section.

**Research cross-references.** Reference by path, don't embed.

**Template.** `plugin/templates/.proxies/build-log.md`. Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`.

## planning/drafts/ folder

`_method/planning/drafts/<topic>.md`. Destination-agnostic carryover for content not yet ready for a specific doc — comparison tables, structural sketches, option matrices. Written at "good enough to walk away from"; deleted when consumed; dead-ends pruned with build-log note. One file per topic, kebab-case. Read/write, no locking.

## research/ folder

`_method/research/<topic>.md`. Home for research findings. When Claude investigates an external fact, it saves here and mentions in chat. Kebab-case filenames, no date prefix. Persists indefinitely — not deleted when consumed. No MANIFEST tracking, no BACKLOG entries. Zero maintenance. Valid on `Inputs:` lines. Read/write, no locking.

## Search query files (research/search-queries/)

`_method/research/search-queries/YYYY-MM-DD-topic-slug.md`. Created by the `/sovresearch` flow. Structured records of research queries and results — distinct from general `_method/research/<topic>.md` files (free-form findings).

**Naming.** `YYYY-MM-DD-topic-slug.md`. Date is the query date; slug describes the topic. Same topic researched on different dates gets separate files.

**Template.** `plugin/templates/research/search-queries/QUERY-TEMPLATE.md`. Six sections:

- **Trigger** — what was happening when the need arose.
- **Decision it informs** — what choice is blocked without the answer.
- **Query** — the exact search query sent.
- **Good-answer criteria** — what a useful response would contain.
- **Response** — search results, filled after return.
- **Outcome** — what was done with the result.

**Frontmatter.** YAML: `status` (pending/complete/discarded), `date`, `session-context`.

**Lifecycle.** Created at `pending`. Updated to `complete` when response filed and outcome recorded. `discarded` if result wasn't useful and no action taken. Files persist indefinitely.

**Folder creation.** `/sovsetup` scaffolds both `_method/research/` and `_method/research/search-queries/`.

## Proxy files (_method/proxies/)

Lightweight index files summarizing source-of-truth docs. Claude reads proxies first, dips into full docs via offset/limit for detail. Location: `_method/proxies/`. Created by `/sovsetup`; regenerated during planning after editing source docs. Legacy projects may have `.proxies/` at project root — check both.

**Missing proxies.** Fall back to the full doc. Proxies are an optimization, not a requirement.

**File naming.** Lowercase, matching the source doc: `ux.md`, `manifest.md`, `research.md`, `backlog.md`, `build-log.md`.

**Format — all proxies:**

```markdown
<!-- proxy | source: <relative-path> | generated: YYYY-MM-DD -->

# <title>

<state summary — key metrics, 2–4 lines>

## Entries

<one line per entry, format varies by type>
```

**HTML comment header.** `source` is the path relative to project root. `generated` is the date the proxy was last written.

**State summary.** Enough to decide whether to dip into the full doc. Counts, status breakdowns, date ranges.

**Entries section.** One line per entry. `L<N>` = starting line number in the source doc (for offset/limit reads).

### Summary proxies

| Proxy | Source | State summary | Entry format |
|---|---|---|---|
| `ux.md` | `UX.md` | Project context, principle count, functionality count | `- L<N> **<name>** — <summary>` (principles then functionalities) |
| `manifest.md` | `MANIFEST.md` | Entry count, capabilities summary (verbatim) | `- L<N> **<name>** (<path>)` (description/rationale omitted) |
| `research.md` | `_method/research/` | File count | `- <filename> — <summary>` (no line numbers) |

### BACKLOG (single-file, V110+)

Default format: `_method/BACKLOG.md` is the primary file — all five sections (Red flags, Planning batches, Build batches, Test sessions, Open questions) with batch content inline using `### Batch:` headings. No proxy needed. Path block: `"BACKLOG.md"` → `_method/BACKLOG.md`. `"TEST-LOG.md"` also points here (Test sessions section serves as the test-log index).

### BACKLOG index proxy (legacy, backlog.md)

Legacy format (V73–V109): `_method/proxies/backlog.md` as operational index with reference lines pointing at per-batch files in `_method/BACKLOG/`. Still supported by parser and hooks for existing projects. Path block: `"BACKLOG.md"` → `_method/proxies/backlog.md`.

### Build-log index proxy (build-log.md)

Source: `_method/build-log/` directory. Like the BACKLOG proxy, this IS the operational index — carries the newest-first reference list to per-build files. `/sovclose` prepends index lines here.

Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`. Session-start resolves per-build files relative to `_method/build-log/`.

### Regeneration rules

Proxies are regenerated, not hand-edited. To regenerate: read source, write proxy per format above, set `generated` to today. Exception: `backlog.md` and `build-log.md` are directly edited (operational indexes, not summaries).

- **`/sovsetup`** generates initial proxies after scaffolding.
- **Planning procedure** regenerates affected proxies after editing source-of-truth docs.
- **`/sovclose`** updates operational index proxies (backlog test sessions section, build-log) and regenerates stale summary proxies (MANIFEST at minimum).

## Proposed edits pending sections

Every read-only doc (`UX.md`, `MANIFEST.md`, additional docs) carries `## Proposed edits pending` at bottom — where Claude queues content it can't write directly.

**Placement.** Last section, immediately before footer.

**Block format.** Blockquote:
> `**[PROPOSED EDIT PENDING]**` `<DOC>.md` — [description]. [Proposed text]. **Action:** [replace | add] — [target heading details]. Surfaced [date]; origin: [source].

**Origins.** Planning-batch resolution, `/sovsetup`, or intercepted mid-build edit.

**Lifecycle.** Empty by default. Removed after user applies. During planning/`/sovsetup`, preview-then-apply convention.

**PreToolUse carve-out.** Edits within the proposed-edits section allowed. Edits elsewhere in the locked doc denied.

**Migration.** Pre-V43 centralised blocks in BACKLOG → redistributed to destination docs by planning procedure.

## `[SECURITY]` marker

Inline marker for entries that touch a sensitive surface — authentication, PII, payments, deletion, access control, etc. Works the same way on any entry in any doc.

**Format.** `[SECURITY]` at the end of the entry heading or first line, before any trailing punctuation.

**Applies to:**
- UX.md Functionalities entries: `**Feature name** [SECURITY]`
- BACKLOG build batch headings: `### Batch: Name [SECURITY]` (single-file) or `# Name [SECURITY]` (folder)
- BACKLOG planning batches: heading line carries `[SECURITY]`
- BACKLOG open questions: heading line carries `[SECURITY]`

**Does not apply to:** MANIFEST.md, TEST-LOG (execution-level docs already covered by Red flags and the read-before-edit gate).

**Informational, not enforced.** No hook gates. Two audiences: the user sees it reviewing their spec; Claude uses it to bias security-marked items earlier in BACKLOG ordering.

## BACKLOG structure

Two formats, auto-detected:
- **Single-file (V110+, default):** `BACKLOG.md` with everything inline. Path block → `_method/BACKLOG.md`.
- **Folder (legacy, V48–V109):** `BACKLOG/` with per-batch files. Index at `_method/proxies/backlog.md` or `BACKLOG/INDEX.md`. Still supported by parser and hooks for existing projects.

**Maintained by Claude during planning.** Claude edits directly; user reviews.

**Five sections, in order** (INDEX.md or BACKLOG.md):

- **Red flags.** Deferred security/privacy/data-integrity concerns. Each: `**[RED FLAG]**` [description]. Found during [batch] ([date]). Fix: [fix]. Active-batch concerns stay there; planned-feature concerns become batch questions. Red flags are specifically deferred with no active plan.

- **Planning batches.** Two kinds: (a) blocking questions for a build batch, (b) scope-existence questions. Each ends with `Blocks:`. Resolution: append answer + `[PROPOSED EDIT PENDING]` in destination doc. One per discrete decision.

- **Build batches.** Engineering work, priority-ordered. Top = next build. Two regions: scope context (Goal→Dependencies/Red flags) and build operations (Changes→Serves). Must fit one session. Completed batches removed next planning session.

  Single-file (default): inline `### Batch:` headings. Legacy folder mode: per-batch files (`NNNN-name.md`) with index carrying reference list.

  **Batch structure — full shape:**
  ```
  # [name]                                          ← folder (H1)
  ### Batch: [name]                                  ← single-file

  Status: [queued|active|parked]                      ← optional; absent = queued

  **Goal.** [Why this batch exists.]
  **Outputs.** [What changes the user experiences.]
  **Success criteria.** [Observable conditions for success.]
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

  **Handoff notes:** Optional block before Serves line during mid-build handoffs. Build-time context for resume; stripped by `/sovclose` on completion.

  **Status: line.** `queued` (default — absent means queued) or `parked` (paused by planning). Position: first line of body, before Goal. Parser skips `parked` when finding top batch. Legacy `active`/`shipped` recognized but no longer written.

  **Changes: delimiter.** Separates scope-context from build operations. Required; parser falls back for legacy.

  **Change-list labels.** `[Requested]`/`[Suggested]` after `- `. Written by planning, read by `/sovclose` for recap. Labels on changes, not files. Carve-out labels (`[Prerequisite]`/`[Re-batch]`) recap-time only.

  **Inputs:** Non-standard resources; standard docs omitted.

  **Files:** `- [ ]`/`- [x]` task list per file. PreToolUse blocks edits to unlisted files.

  **Tests:** `- <desc> [<Type>] [<Verifier>]` per test. Used for TEST-LOG rows.

  **Serves:** Case-insensitive match against doc headings. PreToolUse blocks mismatches on locked docs.

- **Test sessions.** Index of per-session test files from `test-log/`. Newest-first bullet list: `` - `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed) ``. `/sovclose` prepends one line per build. The test-confirmation gate and TEST-LOG tripwire resolve test data from the per-session files in `test-log/`; this section is the index. In single-file mode, this lives inline in BACKLOG.md. See *TEST-LOG structure* above for column specs and per-session file format.

- **Open questions.** Unscoped captures — from quick one-liner thoughts to fleshed-out questions. `/sovdeliberate` works through accumulated entries. Full entries: question title, *Surfaced* tag, framing paragraph, *Why it matters*, *Next step*. Light entries: heading, *Surfaced* tag, one sentence. Why it matters and Next step are optional — useful when the question has enough shape to benefit from them. Distinct from planning batches (which name what they block).

### Build-snapshot architecture (V90)

When `/sovbuild` is invoked, the active batch is extracted from BACKLOG into `_method/active-build.md` and removed from BACKLOG. The build reads and ticks files in the snapshot. BACKLOG is fully unlocked — parallel sessions can plan or deliberate freely. At `/sovclose`, the snapshot is deleted — the build-log entry serves as the permanent shipped record; the batch is not written back to BACKLOG.

**Phase detection.** Snapshot existence replaces `Status: active` as the build-in-progress signal. `_method/active-build.md` exists → build phase. Absent → planning phase. Legacy: `Status: active` in BACKLOG still detected for pre-V90 projects.

**Snapshot format.** Standalone markdown: batch heading (H1), scope context, build operations, plus `## Close handoff` at bottom.

**Close handoff section.** Created empty by `/sovbuild`; appended incrementally during per-file work. One bullet per file recording what changed — new names, renamed concepts, shifted frames, invalidated doc references. Mechanical changes skipped. `/sovclose` reads this as its primary source for doc-parity, frame-correction, and build-log narrative. If empty or absent (legacy snapshots), falls back to scanning Files:. Consumed by `/sovclose` and deleted with the snapshot.

---
*Sovereign Implementer — Version 112.*
