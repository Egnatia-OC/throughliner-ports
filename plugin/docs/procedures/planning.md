# Planning procedure — no-code method

Follow this procedure during the *planning* phase — never during builds, setup, or migration. This procedure covers **structural planning**: reordering batches, splitting or merging them, rescoping batch content, revising dependency chains, adding or removing batches, and housekeeping (test read-back, drift checks, batch pruning).

For working through open questions, use `/sovdeliberate`. For exploring new ideas or feature requests, use `/sovideate`.

You hold structural authority over BUILD-PLAN: every change (add, remove, reorder, split, reclassify) is yours to make directly; the user reviews after. **Two BUILD-PLAN formats:** single `BUILD-PLAN.md` (legacy) or `BUILD-PLAN/` folder with `INDEX.md` + per-batch files (V48+). In folder mode, planning batches/Red flags/Open questions live in `INDEX.md`; build batches in per-batch files. Resolve format from `CLAUDE.md` path block.

## Classifying the opener

Classify the user's opener into one of:

- **test notes** — output from a previous build's tests.
- **scope question** — whether something should exist.
- **mixed** — primary named, e.g. `mixed (primary: test notes)`.

Feature requests and new ideas route to `/sovideate`, not here. If the opener is a feature request, redirect. The UserPromptSubmit hook may have injected a routing hint — trust it unless it clearly doesn't match intent. See *Mixed-input sort* for secondary items in the opener.

## First action — classify, then load

Classify project state before loading the full doc set. Cold-start projects skip history-dependent steps entirely.

**Step 1 — always load:**

1. `CLAUDE.md` — path block and project-specific notes.
2. `MANIFEST.md` — scan for entries. `TEST-LOG.md` — scan for data rows. In folder mode (path block → `proxies/test-log.md`): walk files in `test-log/`.

**Step 2 — cold-start check:**

If MANIFEST has no entries and TEST-LOG has no data rows → **cold start**. Log: "Cold start — no prior builds. Skipping history-dependent steps." Steps 1–3 of the procedure are skipped.

**Step 3 — load remaining docs:**

- **Always:** `UX.md`, `BUILD-PLAN.md` (resolves to `_method/proxies/build-plan.md` or legacy `BUILD-PLAN/INDEX.md`; + per-batch files in folder mode), additional source-of-truth docs, `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *BUILD-PLAN structure*, *Proposed edits pending sections*.
- **Not cold start only:** `BUILD-LOG.md` (resolves to `_method/proxies/build-log.md` or legacy `build-log/INDEX.md`), `${CLAUDE_PLUGIN_ROOT}/docs/DOC-STRUCTURE.md` → *TEST-LOG structure*.

## Procedure order

After loading state, perform in order:

**Cold-start gate.** If cold start (empty MANIFEST + empty TEST-LOG): skip steps 1–3 entirely. Jump to step 4.

1. **[BRIEF, SEQUENCE] Close previous build's test session.** Per-row read-back of pending TEST-LOG rows.
2. **[SILENT] Remove completed build batches.** Any batch with `Status: shipped` (or, for legacy batches without Status, every `Files:` entry ticked). In folder mode: delete per-batch file + remove INDEX.md reference.
2b. **[BRIEF] Flag aging batches (folder mode only).** Batches predating the most recently completed batch.
2c. **[BRIEF] Prune orphaned TEST-LOG rows.** Delete rows whose Component no longer exists in MANIFEST.md, plus `Superseded` rows.
3. **[BRIEF, SEQUENCE] Five drift checks.** Direct-edit detection, UX↔build, MANIFEST↔codebase, MANIFEST↔UX (loose), TEST-LOG↔code-touch.
4. **[BRIEF] Scan BUILD-PLAN Open questions.** One-line summary per entry with its `Surfaced` tag. Flag entries older than 5 build cycles as potentially neglected. If empty/absent, note in one line. **Don't work through OQs here** — `/sovdeliberate` handles that. If 3+ OQs exist or any are older than 5 build cycles, nudge: "You have N open questions (oldest: <tag>) — consider `/sovdeliberate` before your next build."
5. **[BRIEF] Sort test notes** into Suggestions candidates (bugs against existing UX entries) and Discoveries candidates (new ideas). Skip if not `test notes`/`mixed`.
5. **[DISCUSS] Discuss changes with user.** Propose better options; push back by default.
6. **[SILENT] Dedupe and reclassify.** Every candidate: already covered (skip), fits UX.md (build batch), or out of scope (Discovery).
7. **[BRIEF] Suggestions list.** Fixes fitting current scope. Label `[Requested]` or `[Suggested]`. Ask: next build or BUILD-PLAN for later?
8. **[BRIEF] Discoveries list.** Outside current scope. Don't fix. Each needs a UX.md update via planning batch first.
9. **[SILENT] Edit BUILD-PLAN directly.** Never describe edits for user to apply.
10. **[SILENT] Promote Discoveries** the user hasn't dropped into planning batches.
11. **[BRIEF] Recap.** What changed in BUILD-PLAN + Suggestions/Discoveries lists. Name deferred decisions explicitly.
12. **[SILENT] Regenerate proxies.** If `_method/proxies/` exists (or legacy `.proxies/`), regenerate any proxy whose source doc was edited this session. Read the source doc, write the proxy per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*. Skip if neither proxies directory exists.

13. **[PROMPT] Commit.** "Ready to commit. I'll stage the changes and commit with a `plan:` prefix."

    On user okay:
    - Stage changed files explicitly (never `git add -A`).
    - Commit: `plan: <one-line summary of structural changes>`.
    - No tag. No push. `/sovgit` available afterward for ad-hoc push.

## Close previous build's test session (V27)

Implements *Never infer completion* and unblocks the test-confirmation gate. If TEST-LOG has rows from the previous batch with `Confirmed Explicitly: No`, walk them **one at a time** before any other planning work. Rows already `Yes` are skipped.

**Per row:**

1. Read the `Test Description` aloud.
2. Ask: "Pass, Fail, or Skipped?" — Pass = works as expected; Fail = broken (I'll ask what happened); Skipped = didn't test (I'll ask why).
3. Wait for *this specific row's* answer.
4. Update: `Status`, `Confirmed Explicitly: Yes (YYYY-MM-DD)`, `Notes` (required for Fail/Skipped).
5. Next pending row.

**No bulk asks.** If the user says "they're all fine," push back with the next row:

> "I need to record each row by name. Next: row #042, *<test description>* — Pass, Fail, or Skipped?"

**Order:** lowest unconfirmed `#` first, sequential.

**Skipped requires a reason.** Skipped satisfies the gate only as "accounted for," not as passing.

**Identifying previous batch rows:** if `proxies/build-log.md` (or legacy `build-log/INDEX.md`) exists, read it → first reference → per-build file → H1 first token = session ID. Legacy `BUILD-LOG.md`: first `## <token>` heading. Filter TEST-LOG rows (across all per-session files in folder mode) by matching Session. Fallback: every row with `Confirmed Explicitly: No` counts.

**Already done:** if all previous-batch rows are `Yes` or TEST-LOG is empty, log one line and proceed.

If the user came for a non-planning reason but read-back is pending, open with: *"Before your question — N pending tests from session X. First: <test description>?"*

## The two flows

- **test notes** → sort into two piles: bugs against existing UX entries (Suggestions) vs. new ideas without UX backing (Discoveries).
- **scope question** → planning batch in BUILD-PLAN with `Blocks: scope decision — no build batch yet.`

**Feature requests** no longer route here — `/sovideate` handles new concepts and feature ideas. If the opener is a feature request, redirect: "That's a new idea — invoke `/sovideate` to explore it."

Both flows converge into discuss-with-user.

### Doc-first ordering

Before exploring code via Glob/Grep/reads, check UX.md and BUILD-PLAN for scope existence. Only explore code when docs genuinely can't answer (e.g. "does a partial implementation exist?"). Hard rule, not preference — code tells you what *is*, not what was *decided*.

## Mixed-input sort

Even when the opener's primary intent is e.g. `test notes`, it may carry secondary items. Per routing priority, those don't redirect the flow — they get caught during sort, slotted into Suggestions/Discoveries based on UX.md coverage. Catch them.

## Drift checks

Five checks, five separate passes. **Skipped entirely on cold start** — the cold-start gate handles this. Don't skip on "nothing since last planning" — no reliable signal, and would miss manual edits.

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
- Method writable surface (planning phase): all path-block docs (`UX.md`, `MANIFEST.md`, additional source-of-truth docs), `build-log/`, `BUILD-LOG.md`, `TEST-LOG.md`, BUILD-PLAN files, `CLAUDE.md`, `_method/research/` files.

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

## BUILD-PLAN editing — do, then describe

Make every change yourself. Never list pending edits for the user.

When adding a `Serves UX.md:` line, verify every named entry exists in UX.md Functionalities (case-insensitive). PreToolUse blocks mismatches.

**Parking and unparking batches.** When the user wants to pause a batch: write `Status: parked` at the top of the batch body (after heading, before Goal). When unparking: remove the `Status:` line entirely (absent = queued). The parser skips parked batches — they won't appear as the top batch for builds.

**Scaffolding new build batches (V47):** write the full two-region structure per `DOC-STRUCTURE.md` → *Build batches → Batch structure — full shape*:

1. **Scope context** — always Goal, Outputs, Success criteria. Omit Decisions/Dependencies if resolved/none.
2. **Red flags sub-section** — only if batch touches security-shaped surfaces. Don't write an empty one.
3. **Build operations** — `Changes:` delimiter + change-list bullets with `[Requested]`/`[Suggested]` labels. Leave `Inputs:`/`Files:`/`Tests:` for `/sovrecap`.

Folder mode: allocate number by Glob scan, create per-batch file, add reference to INDEX.md. Single-file mode: inline `### Batch:` heading.

Surface scope-context in recap before writing to BUILD-PLAN.

**Change-list labels (V27).** Every change bullet: `[Requested]` (user asked) or `[Suggested]` (Claude proposed). Labels attach to the *change*, not files. Missing labels break the close recap's source chain. Overlap: user confirmed your suggestion → `[Requested]`. Merge: combined item → `[Requested]`.

**Source-of-truth docs (V67).** UX.md and additional source-of-truth docs are directly editable by Claude during planning phase — no `[PROPOSED EDIT PENDING]` ceremony needed. Edit them directly on user approval. PreToolUse allows these edits because no `Status: active` batch exists.

**Check MANIFEST rationale before rewriting UX entries (V79).** Before editing or removing a UX.md Functionalities entry, read the MANIFEST entries whose rationale references the feature. The rationale records *why* the component was built — editing UX without it risks removing the design reason a component exists.

## How a new feature enters the project

Fixed pipeline — no shortcuts. The entry point is `/sovideate`; the structural work happens here in `/sovplan`:

1. **Idea raised** via `/sovideate`. If it conflicts with an existing UX principle, `/sovideate` surfaces the conflict first.
2. **Enters BUILD-PLAN as planning batch** asking questions needed for UX.md entry.
3. **Questions answered** in this or future planning session. Resolved → append to batch + edit UX.md directly (V67 — source-of-truth docs are open during planning).
4. **Planning batch removed** once UX.md entry exists.
5. **Only then** does a build batch enter BUILD-PLAN with `Serves UX.md:` pointing at the new entry.

If you're proposing a build batch with no UX.md match, stop — you've skipped a step.

## Discoveries promotion

Before finishing the planning phase, promote every undropped Discovery into a BUILD-PLAN planning batch asking "should this be added to UX.md?" No Discovery survives `/clear` unrecorded.

## Recap

Present what you changed in BUILD-PLAN + Suggestions/Discoveries lists. No pending edits for the user. Name deferred decisions explicitly.

## Migration: centralized → distributed proposed edits

If BUILD-PLAN contains `[PROPOSED EDIT PENDING]`/`[FOLD-IN PENDING]` blocks (pre-V43), redistribute each to the destination doc's `## Proposed edits pending` section (create if absent). Remove empty section from BUILD-PLAN. Surface in recap.

## Deferred build-material aging

Folder mode: completed batches leave gaps in `NNNN` numbering. Any batch with a number below the highest gap is aging.

**Detection:** Scan `BUILD-PLAN/` for `NNNN-*.md`. Find missing numbers in `[1, max]`. Most recently completed = max(missing). Batches below that threshold are aging.

**Surfacing:** One line per aging batch: "Batch NNNN (*<heading>*) predates completed batch MMMM. Consider pairing with current top batch or scheduling next."

Prefer pairing but respect session-length constraint. Don't reorder automatically.

Single-file mode: skip. No aging items: skip silently.

## TEST-LOG row pruning

Prune before drift checks. Bounds file growth and reduces check 5's workload.

1. Read MANIFEST.md — collect all entry names.
2. Walk TEST-LOG rows (in folder mode: across all per-session files in `test-log/`):
   - `Superseded` status → delete.
   - Component matches MANIFEST entry (case-insensitive) → keep.
   - Cross-component descriptive phrase → keep (exempt).
   - Specific element not in MANIFEST → delete.
3. In folder mode: if an entire per-session file is emptied by pruning, delete the file and remove its index line from `proxies/test-log.md`.
4. Surface: "Pruned N rows — [row #s, components, reasons]." Nothing pruned: skip silently.

Deleted rows recoverable via git. Rows for existing components stay regardless of age.

## Ordering principles

When reordering BUILD-PLAN build batches, apply these principles — they override insertion order.

1. **Dependency flow.** Every batch's Dependencies must point at batches above it (already shipped or earlier in the queue). If batch B depends on batch A, A must come first. Check: for each batch, verify every named dependency resolves to a shipped batch or a batch earlier in the queue.
2. **Project-structure reasoning.** Batches that create infrastructure other batches consume (folders, schemas, shared components) go before the batches that consume them.
3. **Security bias.** Batches carrying a `[SECURITY]` marker — or whose scope touches auth, PII, payments, deletion, or access control — bias earlier. Security gaps compound; shipping them later means building on an insecure foundation.
4. **Stale-reference avoidance.** If an earlier batch renames, deletes, or moves a file/skill/doc, later batches that reference the old name need their scope text updated in the same reordering pass.

Claude already understands dependency ordering and project structure. These principles make the application explicit and auditable.

## Batch-ordering audit

Run as part of any planning session that adds, removes, or reorders batches. Four checks:

1. **Forward-dependency scan.** For each batch, verify its Dependencies resolve to shipped batches or earlier queued batches. Flag violations.
2. **Stale-reference scan.** For each batch that renames/deletes/moves a file or skill, grep later batches for references to the old name. Flag hits.
3. **Reorder if needed.** Propose reordering to the user with one-line justification per move.
4. **Fix scope text.** Update stale references in affected batch scope in the same pass as the reorder.

Skip if no structural changes to BUILD-PLAN were made this session.

## Behavioural rules

Universal-behaviour rules apply — push back, plain English, ask on ambiguity, engage with pushback. Keep internal reasoning concise — shorthand bullets, not full paragraphs. Reserve detailed thinking for judgment calls.

---

*No-code method — Version 94.*
