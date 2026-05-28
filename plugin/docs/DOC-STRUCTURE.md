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

**When written.** `/sovsetup` populates the section through conversation — Claude asks, user answers, Claude writes. Not a form. The answer also seeds UX.md's *Project context*.

**When updated.** Planning sessions, when milestones shift or the product's framing evolves. Editable in both phases (CLAUDE.md is always read/write).

**Existing projects.** Projects adopted before this section won't have it. `/sovsetup` case 4 detects the missing section and asks the overview question as a backfill step.

## Language (CLAUDE.md)

`## Language` in CLAUDE.md, between Product overview and the path block. Single field:

- **Language: \<language\>.** The language Claude uses for responses, recaps, and doc content. Defaults to English. Control tokens (`Status:`, `Changes:`, `Serves UX.md:`, `Confirmed Explicitly:`, `[SECURITY]`) stay English regardless — hooks regex-match them.

**When written.** `/sovsetup` asks a 5th question; default is the language the user used for Q1–Q4.

**When updated.** Anytime. CLAUDE.md is always read/write.

**Existing projects.** `/sovsetup` case 4 adds the section if missing.

## Additional source-of-truth docs

Some projects need an extra source-of-truth doc the spine docs don't cover. Common examples: `SYSTEM-PROMPT.md` (Claude/MCP projects), `COPY.md` (user-facing text is the deliverable), `PATTERNS.md` (coding conventions), `API.md` (endpoint/payload specs). Not a required set — create as needed.

Same structural rules as `UX.md`:
- **Phase-aware editing.** Directly editable during planning; locked during build (with `[PROPOSED EDIT PENDING]` carve-out). See `universal-behaviour.md` → *Editing surfaces — phase-aware*.
- **No placeholders.** Source-of-truth docs describe decided behaviour. Open-question status lives in BUILD-PLAN only.
- **Intent level, not implementation.**
- **Planning answers** for the additional doc go into *it*, not `UX.md`.
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

**Optional: Risk accepted.** Known downside weighed and chosen — one or two lines at entry end. Only for conscious trade-offs.

**Cross-references.** Link by entry name in italics: *(see Drag-target icons)*. Don't duplicate content.

**Nested entries.** If a parent has sub-areas with distinct rationale: **Parent → Sub-area**. Use sparingly.

**Scope: intent-level only.** Features at user-intent level. Not every UI element, not implementation details. The "user needs this because..." line is the test.

Undecided behaviour → BUILD-PLAN as a planning batch, not here.

**Non-GUI projects.** Works for CLI tools, backends, MCP servers, plugins. The "user" is whoever the audience is; the "experience" is what they observe.

**Proposed edits pending section.** `## Proposed edits pending` at the bottom. See *Proposed edits pending sections* below.

## MANIFEST.md structure

**Header.** Glossary of named codebase elements, maintained by Claude during builds.

Starts empty. Entry-format reminder in HTML comment.

**Entries.** Flat, alphabetical. One line each:

> - **[Name]** (`path/to/file.ext`) — [plain-English description]. *Rationale: [why it exists / vNN].*

The rationale field records why the component was built — one clause, max 15 words, followed by the session tag when it was introduced. Italic suffix keeps it visually distinct from the description. Existing entries without rationale remain valid (graceful migration).

Include things the user might ask about. Skip trivial helpers and boilerplate.

**Paths field.** The `(path)` is the anchor for the V39 read-before-edit gate. When an edit targets a MANIFEST-pathed file, the hook denies the first attempt with the entry inlined; retry succeeds (hook scans for prior block-once deny). Entries without paths skip the gate.

**Paths-field shape:**
- Single file: `(app/src/TaskCard.kt)`
- Multi-file list: `(a.kt, b.kt)`
- Directory: `(app/src/settings/)` — trailing slash = prefix match
- No path: omit parens for non-file entries

**Migration is incremental.** After-build populates paths on create/update. Legacy entries stay skipped until touched. `/sovsetup` case 4 offers backfill.

**Proposed edits pending section.** At bottom. See below.

## TEST-LOG structure

**Location.** `test-log/` inside `_method/`. One file per build session. Index lives at `_method/proxies/test-log.md` (the proxy IS the index). Legacy: flat `TEST-LOG.md` at project root or inside `_method/`.

**Index (proxies/test-log.md).** Header, HTML comment, newest-first bullet list:
> `` - `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed) ``

`/sovclose` prepends one line per build. Path block: `"TEST-LOG.md"` → `_method/proxies/test-log.md`.

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

**Template.** `plugin/templates/.proxies/test-log.md` (index). `plugin/templates/test-log/ENTRY-TEMPLATE.md` (per-session). Path block: `"TEST-LOG.md"` → `_method/proxies/test-log.md`.

**Backwards compatibility.** Flat `TEST-LOG.md` (single file) still supported. 8-column (pre-V48) migrated on `/sovsetup` case 4: Type→`Look and click`, Verifier→`User`. `/sovsetup` case 4 migrates flat file → folder.

## Build log structure

**Location.** `build-log/` inside `_method/`. One file per build. Index lives at `_method/proxies/build-log.md` (the proxy IS the index). Legacy: `build-log/INDEX.md` at project root or inside `_method/`.

**Index (proxies/build-log.md).** Header, HTML comment, newest-first bullet list:
> `- \`NNN-batch-name.md\` — YYYY-MM-DD — Summary`

`/sovclose` prepends one line per build. Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`.

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

**Performance section.** Mechanical measures, queryable via grep. Optional `Session notes:` for user observations.

**Maintenance.** Entries permanent. Later builds reference earlier ones in their own Pivots section.

**Research cross-references.** Reference by path, don't embed.

**Template.** `plugin/templates/.proxies/build-log.md`. Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`.

## planning/drafts/ folder

`_method/planning/drafts/<topic>.md`. Created by `/sovsetup` inside `_method/`. Destination-agnostic carryover for substantive content not yet ready for a specific doc — comparison tables, structural sketches, option matrices. Written at "good enough to walk away from"; deleted when consumed; dead-ends pruned with build-log note. One file per topic, kebab-case. Read/write to Claude, no locking.

## research/ folder

`_method/research/<topic>.md`. Created by `/sovsetup` inside `_method/`. Home for research findings. When Claude investigates an external fact, it saves here and mentions in chat. Kebab-case filenames, no date prefix. Persists indefinitely — not deleted when consumed. No MANIFEST tracking, no BUILD-PLAN entries. Zero maintenance. Valid on `Inputs:` lines. Read/write, no locking.

## Search query files (research/search-queries/)

`_method/research/search-queries/YYYY-MM-DD-topic-slug.md`. Created by the `/sovresearch` flow (skill or proactive suggestion). Structured records of research queries and their results — distinct from general `_method/research/<topic>.md` files, which are free-form findings.

**Naming.** `YYYY-MM-DD-topic-slug.md`. Date is the query date; slug describes the topic. Same topic researched on different dates gets separate files.

**Template.** `plugin/templates/research/search-queries/QUERY-TEMPLATE.md`. Six sections:

- **Trigger** — what was happening when the need arose.
- **Decision it informs** — what choice is blocked without the answer.
- **Query** — the exact search query sent.
- **Good-answer criteria** — what a useful response would contain.
- **Response** — search results, filled after return.
- **Outcome** — what was done with the result.

**Frontmatter.** YAML: `status` (pending/complete/discarded), `date`, `session-context`.

**Lifecycle.** Created at `pending`. Updated to `complete` when response is filed and outcome recorded. `discarded` if the query was sent but the result wasn't useful and no action was taken. Files persist indefinitely — same as `_method/research/` files.

**Folder creation.** `/sovsetup` scaffolds `_method/research/search-queries/` alongside `_method/research/`.

## Proxy files (_method/proxies/)

Lightweight index files that summarize source-of-truth docs. Claude reads proxies first, dips into full docs via offset/limit when detail is needed. Location: `_method/proxies/` (inside the method subfolder). Created by `/sovsetup`; regenerated during planning after editing source docs. Legacy projects may have `.proxies/` at project root — check both locations.

**Missing proxies.** If the proxies directory is absent or a proxy file is missing, fall back to reading the full doc. Proxies are an optimization, not a requirement.

**File naming.** Lowercase, matching the source doc: `ux.md`, `manifest.md`, `test-log.md`, `research.md`, `build-plan.md`, `build-log.md`.

**Format — all proxies:**

```markdown
<!-- proxy | source: <relative-path> | generated: YYYY-MM-DD -->

# <title>

<state summary — key metrics, 2–4 lines>

## Entries

<one line per entry, format varies by type>
```

**HTML comment header.** `source` is the path relative to project root. `generated` is the date the proxy was last written.

**State summary.** Enough for Claude to decide whether to dip into the full doc. Counts, status breakdowns, date ranges.

**Entries section.** One line per entry. `L<N>` = starting line number in the source doc (for offset/limit reads).

### UX proxy (ux.md)

Source: `UX.md`. State summary: project context (one sentence), principle count, functionality count.

Entries: one line per UX principle, then one line per functionality. Format: `- L<N> **<name>** — <one-phrase summary>`.

### MANIFEST proxy (manifest.md)

Source: `MANIFEST.md`. State summary: entry count.

Entries: one line per MANIFEST entry. Format: `- L<N> **<name>** (<path>)`. Description and rationale omitted — dip for detail.

### TEST-LOG index proxy (test-log.md)

Source: `_method/test-log/` directory. Like the BUILD-PLAN and build-log proxies, this IS the operational index — carries the newest-first reference list to per-session test files. `/sovclose` prepends index lines here.

Path block: `"TEST-LOG.md"` → `_method/proxies/test-log.md`. Hooks resolve per-session files relative to `_method/test-log/`.

### Research index proxy (research.md)

Source: `_method/research/` directory (not a single file). State summary: file count.

Entries: one line per file. Format: `- <filename> — <first heading or one-phrase summary>`. No line numbers.

### BUILD-PLAN index proxy (build-plan.md)

Source: `_method/BUILD-PLAN/` directory. Unlike other proxies, this file IS the operational index — it carries the four BUILD-PLAN sections (Red flags, Planning batches, Build batches, Open questions) with batch reference lines pointing at per-batch files. Not a summary; the file is directly edited by Claude during planning.

Path block: `"BUILD-PLAN.md"` → `_method/proxies/build-plan.md`. Parser resolves batch files relative to `_method/BUILD-PLAN/`.

### Build-log index proxy (build-log.md)

Source: `_method/build-log/` directory. Like the BUILD-PLAN proxy, this IS the operational index — carries the newest-first reference list to per-build files. `/sovclose` prepends index lines here.

Path block: `"BUILD-LOG.md"` → `_method/proxies/build-log.md`. Session-start resolves per-build files relative to `_method/build-log/`.

### Regeneration rules

Proxies are regenerated, not hand-edited. To regenerate: read the source, write the proxy following the format above, set `generated` to today's date. Exception: `build-plan.md`, `build-log.md`, and `test-log.md` are directly edited (they ARE the operational indexes, not summaries).

- **`/sovsetup`** generates initial proxies after scaffolding.
- **Planning procedure** regenerates affected proxies after editing source-of-truth docs.
- **`/sovclose`** updates operational index proxies (test-log, build-log) and regenerates stale summary proxies (MANIFEST at minimum).

## Proposed edits pending sections

Every read-only doc (`UX.md`, `MANIFEST.md`, additional docs) carries `## Proposed edits pending` at its bottom — where Claude queues content it can't write directly.

**Placement.** Last section, immediately before footer.

**Block format.** Blockquote:
> `**[PROPOSED EDIT PENDING]**` `<DOC>.md` — [description]. [Proposed text]. **Action:** [replace | add] — [target heading details]. Surfaced [date]; origin: [source].

**Origins.** Planning-batch resolution, `/sovsetup`, or intercepted mid-build edit.

**Lifecycle.** Empty by default. Removed after user applies. During planning/`/sovsetup`, preview-then-apply convention applies.

**PreToolUse carve-out.** Edits within the proposed-edits section are allowed. Edits elsewhere in the locked doc are denied.

**Migration.** Pre-V43 centralised blocks in BUILD-PLAN → redistributed to destination docs by the planning procedure.

## `[SECURITY]` marker

Inline marker for entries that touch a sensitive surface — authentication, PII, payments, deletion, access control, etc. Works the same way on any entry in any doc.

**Format.** `[SECURITY]` at the end of the entry heading or first line, before any trailing punctuation.

**Applies to:**
- UX.md Functionalities entries: `**Feature name** [SECURITY]`
- BUILD-PLAN build batch headings: `### Batch: Name [SECURITY]` (single-file) or `# Name [SECURITY]` (folder)
- BUILD-PLAN planning batches: heading line carries `[SECURITY]`
- BUILD-PLAN open questions: heading line carries `[SECURITY]`

**Does not apply to:** MANIFEST.md, TEST-LOG (execution-level docs already covered by Red flags and the read-before-edit gate).

**Informational, not enforced.** No hook gates on the marker. Two audiences: the user sees it when reviewing their spec; Claude uses it as a prioritization input when ordering BUILD-PLAN (security-marked items bias earlier in the queue).

## BUILD-PLAN structure

Three formats, auto-detected:
- **Single-file (legacy):** `BUILD-PLAN.md` with everything inline. Path block → `BUILD-PLAN.md`.
- **Folder with INDEX (V48–V72):** `BUILD-PLAN/` with `INDEX.md` + per-batch files. Path block → `BUILD-PLAN/INDEX.md`.
- **Proxy-as-index (V73+, default):** `BUILD-PLAN/` with per-batch files only. Index lives at `_method/proxies/build-plan.md`. Path block → `_method/proxies/build-plan.md`.

**Maintained by Claude during planning.** Claude edits directly; user reviews.

**Five sections, in order** (INDEX.md or BUILD-PLAN.md):

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

  **Handoff notes:** Optional block before Serves line during mid-build handoffs. Contains build-time context for resume. Stripped by `/sovclose` when batch completes.

  **Status: line.** Tracks batch lifecycle. Three values under V90+: `queued` (default — no line needed), `parked` (paused by planning), `shipped` (completed by `/sovclose`). Legacy `active` value still recognized by hooks but is no longer written — the build-snapshot architecture uses `_method/active-build.md` existence instead. Position: first line of batch body, before Goal. The parser skips `shipped` and `parked` batches when finding the top build batch. Absent = queued.

  **Scope-context sections.** Goal/Outputs/Success criteria always present. Decisions/Dependencies omitted when empty. Red flags only when security-shaped scope detected.

  **Changes: delimiter.** Separates scope-context from change list. Required for new batches; parser falls back for legacy.

  **Change-list labels.** `[Requested]`/`[Suggested]` after `- `. Written by planning, preserved by `/sovrecap`, read by `/sovclose` for recap. Labels on changes, not files. Carve-out labels (`[Prerequisite]`/`[Re-batch]`) are recap-time only.

  **Inputs: line.** Non-standard resources between change list and Files:. Standard docs omitted.

  **Files: sub-section.** `- [ ]`/`- [x]` task list per file. PreToolUse blocks edits to files not on the list.

  **Tests: sub-section.** `- <desc> [<Type>] [<Verifier>]` per test. After-build uses these for TEST-LOG rows.

  **Serves name matching.** Case-insensitive whitespace-trimmed match against doc headings. PreToolUse blocks mismatches on locked docs.

- **Open questions.** Non-blocking parking. Each: question title, *Surfaced* (session tag or build-cycle identifier when created — so planning can detect neglected entries), framing paragraph, *Why it matters*, *Next step* (trigger for promotion/resolution). Distinct from planning batches (which name what they block).

- **Ideas.** Raw, unprocessed ideas captured during any session type. Lighter than open questions — just a date and a one-liner. Claude can write here regardless of build phase (BUILD-PLAN is unlocked under the build-snapshot architecture). `/sovideate` or `/sovdeliberate` promotes ideas to OQs or batches. Entry format: `- YYYY-MM-DD — [one-line description]`.

### Build-snapshot architecture (V90)

When `/sovbuild` is invoked, the active batch's full content is extracted from BUILD-PLAN into `_method/active-build.md` and removed from BUILD-PLAN entirely. The build reads and ticks files in the snapshot. BUILD-PLAN is fully unlocked — parallel sessions can run `/sovplan`, `/sovdeliberate`, or `/sovideate` freely. At `/sovclose`, the batch is written back to BUILD-PLAN as shipped and the snapshot is deleted.

**Phase detection.** The snapshot file's existence replaces `Status: active` as the build-in-progress signal. `_method/active-build.md` exists → build phase. Absent → planning phase. Legacy fallback: `Status: active` in BUILD-PLAN still detected for pre-V90 projects.

**Snapshot format.** The snapshot is a standalone markdown file containing the batch's heading (H1), scope context, build operations, and a `## Close handoff` section at the bottom — the same content that would appear in the per-batch file or inline BUILD-PLAN section, but extracted to its own file, plus the handoff section appended at creation.

**Close handoff section.** `## Close handoff` at the bottom of the snapshot. Created empty by `/sovbuild`; appended to incrementally during the per-file work loop. One bullet per file, recording what changed — new consumer-facing names introduced, concepts renamed, frames shifted, doc references invalidated. Mechanical changes with nothing for `/sovclose` to act on are skipped.

`/sovclose` reads this section as its primary source for doc-parity checks, frame-correction sweeps, and build-log narrative — replacing codebase re-exploration. If the section is empty or absent (legacy snapshots), `/sovclose` falls back to scanning the batch's Files: list.

The section is not written back to BUILD-PLAN when the batch is marked shipped — it's build-time context, not permanent scope.

---
*No-code method — Version 95.*
