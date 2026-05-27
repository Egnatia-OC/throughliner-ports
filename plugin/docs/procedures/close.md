# Close procedure — no-code method

Follow this procedure to close a session. Works after any session type — build, planning, or general.

## Phase detection

Determine the path:

1. Parse BACKLOG for the top batch with `Status: active` and all Files: ticked (`- [x]` only, no `- [ ]`).
2. If found → **post-build path** (full close workflow).
3. If not found → **planning/general path** (lighter close).

---

## Post-build path

Run when a build batch just completed (Status: active, all Files: ticked).

### First action — load project state (minimal)

Load only what's needed for batch identification and idempotency. Defer heavier reads to work-loop steps.

1. `CLAUDE.md` — path block and project notes.
2. `BACKLOG.md`/`INDEX.md` — find the just-completed batch. In folder mode, read INDEX.md → top per-batch file.
3. `TEST-LOG.md` — idempotency check. In folder mode (path block → `proxies/test-log.md`): read files in `test-log/`.
4. `MANIFEST.md` — for the MANIFEST update.

**Defer:** UX.md, BUILD-LOG/build-log, DOC-STRUCTURE.md sections — read when the step using them runs.

### Identify the just-completed batch

Walk Build batches top-to-bottom. The just-completed batch is the topmost with entirely ticked Files: (`- [x]` only, no `- [ ]`).

If topmost batch has unticked files → halt (build not finished). If no fully-ticked batch → halt with note and stop.

### Idempotency check

If TEST-LOG already has rows matching this session whose scope covers the batch's Files: → the close steps are already done. State it and stop. Don't duplicate rows or re-run.

### Session identification

TEST-LOG's Session column needs a stable build-session identifier:

- **Proxy-as-index:** `proxies/build-log.md` → first reference → per-build file H1 → first token.
- **Folder mode (legacy):** `build-log/INDEX.md` → first reference → per-build file H1 → first token.
- **Single-file:** `BUILD-LOG.md` → first `## <token>` heading.
- **Last resort:** today's YYYY-MM-DD.

### Work loop

1. **[SILENT] Update MANIFEST.md.** Use the batch's Files: as source. For each ticked file:
   - Added file with trackable element → add MANIFEST entry with `(path)` field and rationale (`*Rationale: [why it exists / vNN].*` — one clause, max 15 words + session tag). Alphabetical order.
   - Renamed → update name + path.
   - Deleted → remove entry.
   - Modified → update description only if substantive change. **If entry has no `(path)` yet** (legacy), add it now. **If entry has no rationale yet** (legacy), add it now.
   Trivial helpers stay out of MANIFEST.

2. **[SILENT] Read `[Requested]`/`[Suggested]` labels** from the batch's change list in BACKLOG. Prerequisite carve-outs bear `[Prerequisite, not in plan]` on Files: entries.

3. **[SILENT] Doc-parity check.** For each file in the batch's Files: list that was renamed, deleted, or moved: grep UX.md, BACKLOG, MANIFEST.md, and CLAUDE.md for references to the old name or path. Collect stale references — flag in step 11. Scoped to blast radius of what changed, not a full doc audit.

4. **Open test session + run Claude tests.** Two sub-steps.

   **4a. Write TEST-LOG rows.** One row per distinct observable behaviour. Draw from batch's `Tests:` sub-section if present, else derive from recap (default: `Look and click` / `User`). 10-column format:
   - `#` — next three-digit ID (global across all per-session files).
   - `Date` — YYYY-MM-DD.
   - `Session` — per identification above.
   - `Component` — match MANIFEST entry name where possible.
   - `Test Description` — one sentence, re-runnable.
   - `Type` — `Look and click` / `Run and read` / `Trigger and observe` / `Generate and inspect`.
   - `Verifier` — `Claude` or `User`.
   - `Status` — blank initially (Claude rows filled in 4b).
   - `Confirmed Explicitly` — `No`.
   - `Notes` — blank initially.

   **Folder mode (path block → `proxies/test-log.md`):**
   - **4a-i.** Allocate filename: scan `test-log/` for `[0-9]*-*.md`, highest number + 1 (start at `001`). Kebab suffix from batch heading. Write per-session file with H1 `# Test session — <Session> — YYYY-MM-DD` followed by the table.
   - **4a-ii.** Prepend index line to `_method/proxies/test-log.md`: `` - `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed) ``. Idempotency: skip if same-numbered line exists. Fallback: `TEST-LOG.md` (single-file legacy).

   **Single-file mode (path block → `TEST-LOG.md` directly):**
   - Position rows at top of table body (below header separator). Within batch: recap order (lowest # at top).

   **4b. Run Claude-automatable tests.** For each `Verifier: Claude` row, execute the test. Pass → set Status/Confirmed/Notes. Fail → same, and flag prominently in recap. User-verified rows stay blank — they define the test session for next planning's read-back.

5. **[BRIEF] Build recap.** Three parts:
   - **Changes shipped.** One bullet per change, labeled `[Requested]`/`[Suggested]`. Carve-outs get their labels.
   - **Claude has verified.** One bullet per Claude-verified row with Pass/Fail result.
   - **Please manually check.** One bullet per user-verified row, in TEST-LOG order.

6. **[SILENT] Write build-log entry.**
   - **6a.** Allocate filename: scan `build-log/` for `[0-9]*-*.md`, highest number + 1 (start at `001`). Kebab suffix from batch heading.
   - **6b.** Write per-build file:
     ```markdown
     # <Session> — YYYY-MM-DD — Summary

     **What shipped.** <plain-English deliverables; reference TEST-LOG rows>
     **Decisions taken and why.** <load-bearing decisions>
     **Pivots and surprises.** <if any>
     **Carried forward.** <if any>

     ## Performance
     - **Batch completion:** <Complete | Partial (handoff)>
     - **Files in batch:** <N>
     - **Carve-outs:** <None | N prerequisite, N re-batch>
     - **Claude-verified tests:** <N Pass, N Fail (of N total)>
     - **User-verified tests:** <N pending>
     ```
   - **6c.** Prepend index line to `_method/proxies/build-log.md` (the build-log index). Idempotency: skip if same-numbered line exists. Fallback: `build-log/INDEX.md` (legacy), then `BUILD-LOG.md` (single-file legacy).

7. **[SILENT] Set Status: shipped.** Replace the batch's `Status: active` line with `Status: shipped`. This marks the batch as complete for the parser.

8. **[BRIEF if found, SILENT if not] Frame-correction sweep.** If the build substantively changed how a feature works, scan BACKLOG batches and `[PROPOSED EDIT PENDING]` blocks for references to old behaviour. Flag candidates. UX.md drift is caught by planning's drift check 2.

9. **[BRIEF if found, SILENT if not] Queued-pipeline staleness sweep.** For each file in the batch's Files: list that was renamed, deleted, or moved: grep all queued and parked BACKLOG batches and open questions for references to the old name or path. Same grep pattern as step 3, but targeted at queued pipeline instead of spine docs. Flag stale references in recap. This is pattern-match only — check literal path strings and names, not semantic meaning.

10. **[BRIEF if found, SILENT if not] Lost-feature check.** Scan for items that silently fell off the roadmap:
   - **Parked batches** whose parking rationale references a condition that was just met by this build (e.g. "parked until X ships" where X just shipped). Surface and ask the user if it should be unparked.
   - **Carried-forward items** in recent build-log entries that were never picked up by subsequent builds or BACKLOG entries. Scan the last 3–5 build-log files for non-empty "Carried forward" sections, check whether each item appears in current BACKLOG or was addressed. Flag orphans.
   - Skip if the batch didn't change anything that could satisfy a parking condition, and no recent carried-forward items exist.

11. **End-of-recap flags:**
   - Stale references found by doc-parity check (step 3) and staleness sweep (step 9).
   - Out-of-scope improvements.
   - UX.md changes implied (don't edit — flag only).
   - Red flag concerns (confirm BACKLOG entry written if deferred).

12. **[BRIEF] Idea sweep.** Review the session for ideas, suggestions, or observations raised but not implemented. Triage each to one destination: add to BACKLOG (new item or open question); note in build-log entry's *Carried forward* as "not pursued, reason: ..."; or flag in recap for user to decide. Don't leave ideas unrouted.

13. **[SILENT] Regenerate proxies.** If `_method/proxies/` exists (or legacy `.proxies/`), regenerate any proxy whose source doc was edited this session (MANIFEST, TEST-LOG, build-log at minimum — `/sovclose` always touches these). Read the source doc, write the proxy per `DOC-STRUCTURE.md` → *Proxy files (_method/proxies/)*. Skip if neither proxies directory exists.

14. **[SILENT] After-build steps from CLAUDE.md.** If CLAUDE.md has a `## After-build steps` section, read and execute each step. These are project-specific — the section defines what they are. Skip silently if absent.

15. **[SILENT] Pre-commit checkpoint.** Verify before prompting commit: MANIFEST updated (step 1), TEST-LOG rows written (step 4a), build-log entry written (step 6), staleness sweep done (step 9), idea sweep done (step 12), proxies regenerated (step 13), doc-parity check done (step 3). If any missing, complete now.

16. **[PROMPT] Closing.** "Ready to commit. Invoke `/sovgit` to commit, tag, and push. After that, refresh and test — invoke `/sovtest` for a guided walkthrough of your pending tests, or bring per-row outcomes to your next planning session."

---

## Planning/general path

Run when no active-with-ticked-files batch exists. Lighter close for planning, ideation, or general sessions.

### Steps

1. **[BRIEF] Idea sweep.** Review the session for ideas, suggestions, or observations raised but not acted on. Triage each: add to BACKLOG (new batch or open question), or flag in chat for user to decide. Don't leave ideas unrouted.

2. **[SILENT] Regenerate proxies.** If `_method/proxies/` exists (or legacy `.proxies/`), regenerate any proxy whose source doc was edited this session. Skip if no source docs were edited or no proxies directory exists.

3. **[PROMPT] Closing.** "Ready to commit. Invoke `/sovgit` to commit, tag, and push."

---

## What you must not do

- **Don't edit source files, build files, or any non-method file.** Your scope is method docs only: MANIFEST.md, test-log/, build-log/, BACKLOG status lines, proxies. Never edit application source code, build scripts, configuration files, or any file that isn't part of the method's doc set. If a build failed or produced errors, surface it in the recap and TEST-LOG notes — don't attempt to fix it. Mention `/sovrevert` if the user needs to undo the build.
- **Don't create conditions that override a user refusal.** If the user declines an action, that decision stands.
- **Don't edit source-of-truth docs.** UX.md locked. Flag changes in recap.
- **Don't remove completed batches from BACKLOG.** Planning does that next session.
- **Don't start a new build.**
- **Don't infer test outcomes.** Write rows with blank Status and `Confirmed Explicitly: No`.
- **Don't write carve-out labels into BACKLOG change list.** Those are recap-time labels only.
- **Don't perform git operations.** Commit, tag, and push belong to `/sovgit`.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 89.*
