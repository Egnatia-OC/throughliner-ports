# Planning procedure — Sovereign Implementer

Follow this procedure during the *planning* phase — not in the same session as a build, and not during setup or migration. Under V90 snapshot architecture, BACKLOG is unlocked during builds — planning in a parallel session is safe. Covers **structural planning**: reordering, splitting, merging, rescoping batches, revising dependencies, adding/removing batches, and housekeeping (test read-back, drift checks, batch pruning).

For working through open questions or exploring new ideas, use `/sovdeliberate`.

You hold structural authority over BACKLOG: every change (add, remove, reorder, split, reclassify) yours to make; user reviews after. **Default format:** single `BACKLOG.md` with all five sections and batch content inline using `### Batch:` headings. Legacy folder mode (`BACKLOG/` with per-batch files) still supported — resolve from `CLAUDE.md` path block.

## Classifying the opener

Classify the user's opener into one of:

- **test notes** — output from a previous build's tests.
- **scope question** — whether something should exist.
- **mixed** — primary named, e.g. `mixed (primary: test notes)`.

Feature requests and new ideas route to `/sovdeliberate`, not here. If the opener is a feature request, redirect. The UserPromptSubmit hook may have injected a routing hint — trust unless it clearly doesn't match intent. See *Mixed-input sort* for secondary items.

## First action — classify, then load

Classify project state before loading full doc set. Cold-start projects skip history-dependent steps.

**Step 1 — always load:**

1. `CLAUDE.md` — path block and project-specific notes.
2. `MANIFEST.md` — scan for entries. `TEST-LOG.md` — scan for data rows. Walk per-session files in `test-log/`.

**Step 2 — cold-start check:**

If MANIFEST has no entries and TEST-LOG has no data rows → **cold start**. Log: "Cold start — no prior builds. Skipping history-dependent steps." Steps 1–3 skipped.

**Step 3 — load remaining docs:**

- **Always:** `UX.md`, `BACKLOG.md` (resolves to `_method/BACKLOG.md`; legacy: `_method/proxies/backlog.md` + per-batch files), additional source-of-truth docs, `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *BACKLOG structure*, *Proposed edits pending sections*.
- **Not cold start only:** `BUILD-LOG.md` (resolves to `_method/proxies/build-log.md`), `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *TEST-LOG structure*.

## Procedure order

After loading state, perform in order:

**Cold-start gate.** If cold start (empty MANIFEST + empty TEST-LOG): skip steps 1–3 entirely. Jump to step 4.

1. **[BRIEF, SEQUENCE] Close previous build's test session.** Per-row read-back of pending TEST-LOG rows.
2. **[SILENT] Remove legacy completed batches.** Under V99+, `/sovclose` deletes the build snapshot without writing back — completed batches are already absent from BACKLOG. This step handles pre-V99 legacy: any batch with `Status: shipped` (or batches without Status where every `Files:` entry is ticked). Single-file: remove the `### Batch:` section. Legacy folder mode: delete per-batch file + remove index reference. Skip if no legacy shipped batches found.
2b. **[BRIEF] Flag aging batches.** Batches predating the most recently completed batch (identified by numbering gaps).
2c. **[BRIEF] Prune orphaned TEST-LOG rows.** Delete rows whose Component no longer exists in MANIFEST.md, plus `Superseded` rows.
3. **[BRIEF, SEQUENCE] Five drift checks.** Direct-edit detection, UX↔build, MANIFEST↔codebase, MANIFEST↔UX (loose), TEST-LOG↔code-touch.
4. **[BRIEF] Scan BACKLOG Open questions.** One-line summary per entry with `Surfaced` tag. Flag entries older than 5 build cycles as neglected. Empty/absent → note in one line. **Don't work through OQs here** — `/sovdeliberate` handles that. If 3+ OQs or any older than 5 cycles, nudge: "You have N open questions (oldest: <tag>) — consider `/sovdeliberate` before your next build."
5. **[BRIEF] Sort test notes** into Suggestions candidates (bugs against existing UX entries) and Discoveries candidates (new ideas). Skip if not `test notes`/`mixed`.
5b. **[DISCUSS] Discuss changes with user.** Propose better options; push back by default.
6. **[SILENT] Dedupe and reclassify.** Every candidate: already covered (skip), fits UX.md (build batch), or out of scope (Discovery).
7. **[BRIEF] Suggestions list.** Fixes fitting current scope. Label `[Requested]` or `[Suggested]`. Ask: next build or BACKLOG for later?
8. **[BRIEF] Discoveries list.** Outside current scope. Don't fix. Each needs a UX.md update via planning batch first.
9. **[SILENT] Edit BACKLOG directly.** Never describe edits for user to apply.
10. **[SILENT] Promote Discoveries** the user hasn't dropped into planning batches.
11. **[BRIEF] Recap.** What changed in BACKLOG + Suggestions/Discoveries lists. Name deferred decisions explicitly.
12. **[SILENT] Regenerate proxies.** If `_method/proxies/` (or legacy `.proxies/`) exists, regenerate any proxy whose source was edited this session per `DOC-STRUCTURE.md` → *Proxy files*. Skip if no proxies directory.

13. **[PROMPT] Commit.** "Ready to commit. I'll stage the changes and commit with a `plan:` prefix."

    On user okay:
    - Stage changed files explicitly (never `git add -A`).
    - Commit: `plan: <one-line summary of structural changes>`.
    - No tag. No push. `/sovgit` available afterward for ad-hoc push.

## Close previous build's test session

If TEST-LOG has rows from the previous batch with `Confirmed Explicitly: No`, walk them **one at a time** before other planning work. Already `Yes` rows skipped. All rows `Yes` or TEST-LOG empty → log one line, proceed.

**Per row:** Read `Test Description` aloud. Ask: "Pass, Fail, or Skipped?" Wait for this row's answer. Update: `Status`, `Confirmed Explicitly: Yes (YYYY-MM-DD)`, `Notes` (required for Fail/Skipped). Next row.

**No bulk asks.** Push back: "I need to record each row by name. Next: row #042, *<test description>* — Pass, Fail, or Skipped?"

**Order:** lowest unconfirmed `#` first. **Skipped requires a reason** — satisfies the gate as "accounted for," not as passing.

**Identifying previous batch rows:** `proxies/build-log.md` → first reference → per-build file H1 first token = session ID. Filter TEST-LOG rows by matching Session. Fallback: every `Confirmed Explicitly: No` row.

If read-back is pending but user came for a different reason, open with: *"Before your question — N pending tests from session X. First: <test description>?"*

## The two flows

- **test notes** → sort into two piles: bugs against existing UX entries (Suggestions) vs. new ideas without UX backing (Discoveries).
- **scope question** → planning batch in BACKLOG with `Blocks: scope decision — no build batch yet.`

**Feature requests** route to `/sovdeliberate`. Redirect: "That's a new idea — invoke `/sovdeliberate` to explore it."

Both flows converge into discuss-with-user.

### Doc-first ordering

Before exploring code via Glob/Grep/reads, check UX.md and BACKLOG for scope existence. Only explore code when docs can't answer (e.g. "does a partial implementation exist?"). Hard rule — code tells you what *is*, not what was *decided*.

## Mixed-input sort

Even when primary intent is e.g. `test notes`, the opener may carry secondary items. Per routing priority, those don't redirect — they get caught during sort, slotted into Suggestions/Discoveries based on UX.md coverage.

## Drift checks

Five checks, five separate passes. **Skipped on cold start** — cold-start gate handles this. Don't skip on "nothing since last planning" — no reliable signal, would miss manual edits.

1. **Direct-edit detection (V42).** Git-diff against last build's state. Per-file confirmation protocol.
2. **UX.md ↔ what's built.** Every UX entry → something experienceable; every observable behaviour → a UX entry.
3. **MANIFEST.md ↔ codebase.** Every MANIFEST entry → exists at named path; every new file with discrete purpose → has a MANIFEST entry.
4. **MANIFEST.md ↔ UX.md (loose).** Every MANIFEST entry plausibly traces to a UX entry. Plumbing exempt.
5. **TEST-LOG ↔ code-touch since each row's date.** Per-row judgement with reasoning trail. Changed-component rows get status flip via append.

Run as five separate passes — different abstraction levels. Don't bundle.

## Drift check 1 — direct-edit detection

Catches in-file changes the other checks miss — manual edits that leave no MANIFEST-level signal.

**Diff target:**

1. Tags exist: `git diff <last-tag>...HEAD` + `git diff` (uncommitted).
2. No tags: `git diff HEAD` only. Note in chat.
3. No git: skip with one-line note. Other four checks still run.

**Expected (no confirmation needed):**
- Files in most recent batch's `Files:` sub-section.
- Method writable surface (planning phase): all path-block docs (`UX.md`, `MANIFEST.md`, additional source-of-truth docs), `build-log/`, `BUILD-LOG.md`, `test-log/` files, BACKLOG files, `CLAUDE.md`, `_method/research/` files.

Everything else → confirmation protocol.

**Per file:**

1. Surface path, one-line diff summary, matching MANIFEST entry.
2. Ask: *"Was this you (direct edit)? Yes / No / not sure."*
3. Wait for *this file's* answer.
4. Route:
   - **Yes** — check for conflict with upcoming batch `Files:`. If conflict, flag and propose resolution. If no conflict, accept; propose MANIFEST addition if needed. If edit implies UX change, use preview-then-apply convention.
   - **No** — flag as unexpected. Surface diff and pause until source identified.
   - **Not sure** — treat as No.
5. Next file.

Walk one file at a time. If the user signals fatigue, offer to defer remainder — don't bulk-confirm.

## BACKLOG editing — do, then describe

Make every change yourself. Never list pending edits for the user.

When adding a `Serves UX.md:` line, verify every named entry exists in UX.md Functionalities (case-insensitive). PreToolUse blocks mismatches.

**Parking and unparking.** Pause: write `Status: parked` at batch body top (after heading, before Goal). Unpark: remove the `Status:` line (absent = queued). Parser skips parked batches.

**Scaffolding new build batches (V47):** full two-region structure per `DOC-STRUCTURE.md` → *Batch structure — full shape*:

1. **Scope context** — Goal, Outputs, Success criteria always. Omit Decisions/Dependencies if resolved/none.
2. **Red flags** — only if security-shaped scope. No empty section.
3. **Build operations** — `Changes:` delimiter + bullets with `[Requested]`/`[Suggested]` labels. Leave `Inputs:`/`Files:`/`Tests:` for `/sovrecap`.

Add inline `### Batch:` heading in the `## Build batches` section. Allocate batch number by scanning existing batch headings. Legacy folder mode: create per-batch file + add index reference.

Surface scope-context in recap before writing to BACKLOG.

**Change-list labels (V27).** Every bullet: `[Requested]` (user asked) or `[Suggested]` (Claude proposed). Labels attach to the *change*, not files. Missing labels break the close recap. Overlap: user confirmed your suggestion → `[Requested]`. Merged item → `[Requested]`.

**Source-of-truth docs (V67).** UX.md and additional docs directly editable during planning — no `[PROPOSED EDIT PENDING]` needed. Edit on user approval. PreToolUse allows because no active batch exists.

**Check MANIFEST rationale before rewriting UX entries (V79).** Before editing or removing a UX.md entry, read MANIFEST entries whose rationale references the feature. The rationale records *why* the component was built — editing UX without it risks removing the design reason.

## How a new feature enters the project

Fixed pipeline — no shortcuts. Entry point is `/sovdeliberate`; structural work happens here:

1. **Idea raised** via `/sovdeliberate`. Conflicts with UX principles surfaced first.
2. **Planning batch** in BACKLOG asking questions needed for UX.md entry.
3. **Questions answered** this or future session. Resolved → edit UX.md directly (V67 — open during planning).
4. **Planning batch removed** once UX.md entry exists.
5. **Build batch** enters BACKLOG with `Serves UX.md:` pointing at the new entry.

Proposing a build batch with no UX.md match? Stop — you've skipped a step.

## Discoveries promotion

Before finishing, promote every undropped Discovery into a BACKLOG planning batch asking "should this be added to UX.md?" No Discovery survives `/clear` unrecorded.

## Recap

Present what you changed in BACKLOG + Suggestions/Discoveries lists. No pending edits for the user. Name deferred decisions explicitly.

## Migration: centralized → distributed proposed edits

If BACKLOG contains `[PROPOSED EDIT PENDING]`/`[FOLD-IN PENDING]` blocks (pre-V43), redistribute to destination docs' `## Proposed edits pending` sections (create if absent). Remove from BACKLOG. Surface in recap.

## Deferred build-material aging

Scan batch headings for numbering gaps (completed batches leave gaps). Batches below the highest gap are aging. Surface one line each: "Batch NNNN predates completed MMMM — consider pairing or scheduling." Don't reorder automatically. No aging items → skip silently.

## TEST-LOG row pruning

Prune before drift checks. Bounds file growth and reduces check 5's workload.

1. Read MANIFEST.md — collect all entry names.
2. Walk TEST-LOG rows (across all per-session files in `test-log/`):
   - `Superseded` status → delete.
   - Component matches MANIFEST entry (case-insensitive) → keep.
   - Cross-component descriptive phrase → keep (exempt).
   - Specific element not in MANIFEST → delete.
3. If an entire per-session file is emptied by pruning, delete the file and remove its index line from BACKLOG.md's Test sessions section.
4. Surface: "Pruned N rows — [row #s, components, reasons]." Nothing pruned: skip silently.

Deleted rows recoverable via git. Rows for existing components stay regardless of age.

## Ordering principles

When reordering BACKLOG build batches, apply these principles (override insertion order):

1. **Dependency flow.** Every batch's Dependencies must point at shipped or earlier-queued batches. If B depends on A, A comes first.
2. **Project-structure reasoning.** Infrastructure batches (folders, schemas, shared components) before consumers.
3. **Security bias.** `[SECURITY]`-marked batches or auth/PII/payments/deletion/access-control scope bias earlier. Security gaps compound.
4. **Stale-reference avoidance.** If a batch renames/deletes/moves a file, update later batches' scope text in the same pass.

These principles make ordering explicit and auditable.

## Batch-ordering audit

Run as part of any planning session that adds, removes, or reorders batches. Four checks:

1. **Forward-dependency scan.** For each batch, verify its Dependencies resolve to shipped batches or earlier queued batches. Flag violations.
2. **Stale-reference scan.** For each batch that renames/deletes/moves a file or skill, grep later batches for references to the old name. Flag hits.
3. **Reorder if needed.** Propose reordering with one-line justification per move. Apply ordering principles: dependency flow first, then project-structure reasoning, then security bias (`[SECURITY]`-marked batches earlier), then stale-reference avoidance.
4. **Fix scope text.** Update stale references in affected batch scope in the same pass as the reorder.

Skip if no structural changes to BACKLOG were made this session.

## Behavioural rules

Universal-behaviour rules apply — push back, plain English, ask on ambiguity. Internal reasoning concise — shorthand bullets, not paragraphs. Reserve detail for judgment calls.

---

*Sovereign Implementer — Version 112.*
