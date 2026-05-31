# Close procedure — no-code method

Follow this procedure to close a session. Works after any session type — build, planning, or general.

Two turns: **judgment** (while context fresh) then **mechanical** (after `/compact`). Turn boundary `[PROMPT]` is recommended, not enforced — short sessions can close in one turn.

## Phase detection

Determine the path:

1. Check whether `_method/active-build.md` exists.
2. If it exists and all Files: are ticked (`- [x]` only, no `- [ ]`) → **post-build path** (full close workflow).
3. If the snapshot exists but has unticked files → halt (build not finished).
4. If no snapshot → **planning/general path** (lighter close).

---

## Post-build path

Run when a build just completed (`_method/active-build.md` exists, all Files: ticked).

### First action — load project state (minimal)

Load only what's needed for batch ID and idempotency. Defer heavier reads to work-loop steps.

1. `CLAUDE.md` — path block and project notes.
2. `_method/active-build.md` — single source of truth for the completed batch. Read `## Close handoff` — primary source for what changed (names introduced, concepts renamed, frames shifted, doc references invalidated).
3. `TEST-LOG.md` — idempotency check. Folder mode: read `test-log/` files.
4. `MANIFEST.md` — for the MANIFEST update.

**Defer:** UX.md, BUILD-LOG/build-log, DOC-STRUCTURE.md sections — read when the step using them runs.

### Idempotency check

If TEST-LOG already has rows matching this session covering the batch's Files: → close already done. State it and stop.

### Session identification

TEST-LOG's Session column needs a stable build-session identifier:

- **Proxy-as-index:** `proxies/build-log.md` → first reference → per-build file H1 → first token.
- **Folder mode (legacy):** `build-log/INDEX.md` → first reference → per-build file H1 → first token.
- **Single-file:** `BUILD-LOG.md` → first `## <token>` heading.
- **Last resort:** today's YYYY-MM-DD.

### Turn 1 — judgment

Run while build context is fresh.

1. **[SILENT] Update MANIFEST.md.** Batch Files: as source. Per ticked file:
   - Added with trackable element → add entry with `(path)` and rationale (`*Rationale: [why / vNN].*` — one clause, max 15 words + tag). Alphabetical.
   - Renamed → update name + path.
   - Deleted → remove entry.
   - Modified → update description if substantive. **No `(path)` yet** (legacy) → add. **No rationale yet** → add.
   Trivial helpers stay out.

2. **[SILENT] Read `[Requested]`/`[Suggested]` labels** from the batch's change list in `_method/active-build.md`. Prerequisite carve-outs bear `[Prerequisite, not in plan]` on Files: entries.

3. **[SILENT] Doc-parity check.** Read `## Close handoff` for names introduced, renamed, or invalidated. Grep UX.md, BACKLOG, MANIFEST.md, CLAUDE.md for stale references. If Close handoff empty/absent, fall back to scanning Files: for renames/deletes/moves. Flag in step 11.

4. **Open test session + run Claude tests.**

   **4a. Write TEST-LOG rows.** One row per distinct observable behaviour. Draw from batch's `Tests:` if present, else derive from recap (default: `Look and click` / `User`). 10-column format per `DOC-STRUCTURE.md` → *TEST-LOG structure*. Status blank initially (Claude rows filled in 4b); Confirmed Explicitly: `No`.

   **Folder mode (path block → proxy in `proxies/`):**
   - **4a-i.** Allocate filename: scan `test-log/` for `[0-9]*-*.md`, highest number + 1 (start at `001`). Kebab suffix from batch heading. Write per-session file with H1 `# Test session — <Session> — YYYY-MM-DD` followed by the table.
   - **4a-ii.** Prepend index line to the BACKLOG proxy's `## Test sessions` section: `` - `NNN-batch-name.md` — YYYY-MM-DD — N rows (N unconfirmed) ``. Idempotency: skip if same-numbered line exists. Fallback: `TEST-LOG.md` (single-file legacy).

   **Single-file mode (path block → `TEST-LOG.md` directly):**
   - Position rows at top of table body (below header separator). Within batch: recap order (lowest # at top).

   **4b. Run Claude-automatable tests.** For each `Verifier: Claude` row, execute the test. Pass → set Status/Confirmed/Notes. Fail → same, flag in recap. User-verified rows stay blank — they define the test session for planning read-back.

5. **[BRIEF] Build recap.** Three parts:
   - **Changes shipped.** One bullet per change, labeled `[Requested]`/`[Suggested]`. Carve-outs get their labels.
   - **Claude has verified.** One bullet per Claude-verified row with Pass/Fail result.
   - **Please manually check.** One bullet per user-verified row, in TEST-LOG order.

6. **[SILENT] Write build-log entry.**
   - **6a.** Allocate filename: scan `build-log/` for `[0-9]*-*.md`, highest number + 1 (start at `001`). Kebab suffix from batch heading.
   - **6b.** Write per-build file. Draw the narrative from `## Close handoff` — it lists what changed per file during the build:
     ```markdown
     # <Session> — YYYY-MM-DD — Summary

     **What shipped.** <plain-English deliverables; reference TEST-LOG rows>
     **Decisions taken and why.** <load-bearing decisions>
     **Pivots and surprises.** <if any>

     ## Performance
     - **Batch completion:** <Complete | Partial (handoff)>
     - **Files in batch:** <N>
     - **Carve-outs:** <None | N prerequisite, N re-batch>
     - **Claude-verified tests:** <N Pass, N Fail (of N total)>
     - **User-verified tests:** <N pending>
     ```
   - **6c.** Prepend index line to `_method/proxies/build-log.md` (the build-log index). Idempotency: skip if same-numbered line exists. Fallback: `build-log/INDEX.md` (legacy), then `BUILD-LOG.md` (single-file legacy).
   - **6d.** **[SILENT] Decision sweep.** Read the entry's "Decisions taken and why." For each decision:
     - UX-relevant → flag in step 11 (UX.md is locked — flag only).
     - Implementation-relevant → update MANIFEST rationale for the matching existing entry. Step 1 handles per-file rationale for batch files; this catches cross-cutting decisions that apply to existing MANIFEST entries not in the current batch.
     - Neither → skip.

7. **[SILENT] Delete build snapshot.** Delete `_method/active-build.md`. The build-log entry is the permanent shipped record; the batch is not written back to BACKLOG.

8. **[BRIEF if found, SILENT if not] Frame-correction sweep.** Read `## Close handoff` for frame shifts. Scan BACKLOG batches and `[PROPOSED EDIT PENDING]` blocks for old-behaviour references. If Close handoff empty/absent, assess from Files:.

9. **[BRIEF if found, SILENT if not] Staleness sweep.** For each renamed/deleted/moved file in Files:: grep queued and parked BACKLOG batches for old name/path references. Pattern-match only.

10. **[BRIEF if found, SILENT if not] Lost-feature check.** Scan parked batches for parking conditions just met. Surface and ask about unparking.

11. **End-of-recap flags:**
   - Stale references found by doc-parity check (step 3) and staleness sweep (step 9).
   - Out-of-scope improvements.
   - UX.md changes implied (don't edit — flag only).
   - Red flag concerns (confirm BACKLOG entry written if deferred).

12. **[BRIEF] Idea sweep.** Review session for unimplemented ideas, suggestions, or observations. Triage each: BACKLOG (batch or OQ) or flag for user. Nothing unrouted.

13. **[PROMPT] Turn boundary.** Judgment done. State: whether footers need bumping (old → new if so), whether proxies need regeneration. Recommend `/compact` — mechanical pass needs only these values. Low context pressure → continue directly.

### Turn 2 — mechanical

Needs only the values from the turn boundary.

14. **[SILENT] Bump method-version footers.** Only if session-start reported a version mismatch between the plugin and the project's doc footers. Run from project root:
    ```
    python "${CLAUDE_PLUGIN_ROOT}/scripts/bump_version.py" <old> <new>
    ```
    Skip if footers already match the plugin version.

15. **[SILENT] Regenerate proxies.** First, mechanical updates (headers + line-number pointers):
    ```
    python "${CLAUDE_PLUGIN_ROOT}/scripts/bump_version.py"
    ```
    Then review proxies whose source was edited — update summaries, entries for structural changes the script can't detect. MANIFEST, TEST-LOG, and build-log proxies at minimum. Skip if no proxies directory.

16. **[SILENT] After-build steps from CLAUDE.md.** If `## After-build steps` exists, execute each. Project-specific — the section defines them. Skip if absent.

17. **[SILENT] Pre-commit checkpoint.** Verify before prompting commit:
    - [ ] MANIFEST updated (step 1)
    - [ ] TEST-LOG rows written (step 4a)
    - [ ] Build-log entry written (step 6)
    - [ ] Decision sweep done (step 6d)
    - [ ] Build snapshot deleted (step 7)
    - [ ] Staleness sweep done (step 9)
    - [ ] Idea sweep done (step 12)
    - [ ] Footers bumped if applicable (step 14)
    - [ ] Proxies regenerated (step 15)
    - [ ] Doc-parity check done (step 3)
    Complete any missing steps now.

18. **[PROMPT] Closing.** "Ready to commit. Invoke `/sovgit` to commit, tag, and push. After that, refresh and test — invoke `/sovtest` for a guided walkthrough of your pending tests, or bring per-row outcomes to your next planning session."

---

## Planning/general path

Run when no active-with-ticked-files batch exists. Lighter close for planning, ideation, or general sessions.

### Turn 1 — judgment

1. **[BRIEF] Idea sweep.** Review session for unacted-on ideas, suggestions, or observations. Triage: BACKLOG (batch or OQ) or flag for user. Nothing unrouted.

2. **[SILENT] Write build-log entry.** Same allocation as post-build step 6 (scan `build-log/`, next number, kebab suffix). Narrative sections only — `## Performance` omitted:
     ```markdown
     # <Session> — YYYY-MM-DD — Summary

     **What shipped.** <planning changes, OQ resolutions, BACKLOG edits>
     **Decisions taken and why.** <load-bearing decisions, if any>
     **Pivots and surprises.** <if any>
     ```
   Prepend index line to `_method/proxies/build-log.md`. Idempotency: skip if exists.

3. **[PROMPT] Turn boundary.** Judgment done. State whether footers need bumping (old → new if so) and whether proxies need regeneration. Recommend `/compact` if session was long. Short sessions can continue directly.

### Turn 2 — mechanical

4. **[SILENT] Bump method-version footers.** Only if the session made substantive method or plugin changes — most planning/ideation sessions skip. Run from project root:
   ```
   python "${CLAUDE_PLUGIN_ROOT}/scripts/bump_version.py" <old> <new>
   ```
   Skip if footers already match or no version change.

5. **[SILENT] Regenerate proxies.** If proxies directory exists, regenerate any proxy whose source was edited. Run script for mechanical updates, then review summaries. Skip if no edits or no proxies directory.

6. **[BRIEF] Pre-commit checkpoint.** Verify before prompting commit:
   - [ ] Idea sweep done — nothing unrouted (step 1)
   - [ ] Build-log entry written + index line prepended (step 2)
   - [ ] Frame-correction sweep done (if this session consumed a batch)
   - [ ] Staleness sweep done (if this session consumed a batch)
   - [ ] Lost-feature check done (if this session consumed a batch)
   - [ ] Footers bumped if applicable (step 4)
   - [ ] Proxies regenerated if applicable (step 5)
   - [ ] Batch removed from BACKLOG if this session consumed one
   Complete any missing steps now.

7. **[PROMPT] Closing.** "Ready to commit. Invoke `/sovgit` to commit, tag, and push."

### Conditional steps (when this session consumed a batch)

Skip all three unless the session removed, merged, or restructured a BACKLOG batch.

- **Frame-correction sweep.** Scan remaining BACKLOG batches for references to old behaviour. `[BRIEF if found, SILENT if not]`.
- **Staleness sweep.** Grep remaining BACKLOG batches for old name/path references from renamed/deleted/moved files. Pattern-match only. `[BRIEF if found, SILENT if not]`.
- **Lost-feature check.** Scan parked batches for parking conditions just met. Surface and ask about unparking. `[BRIEF if found, SILENT if not]`.

---

## What you must not do

- **Don't edit source files, build files, or any non-method file.** Scope: method docs only (MANIFEST.md, test-log/, build-log/, BACKLOG status, proxies). If a build failed, surface in recap and TEST-LOG notes — don't fix. Mention `/sovrevert` if the user needs to undo.
- **Don't override user refusals.** Declined = final.
- **Don't edit source-of-truth docs.** UX.md locked. Flag changes in recap.
- **Don't start a new build.**
- **Don't infer test outcomes.** Write rows with blank Status and `Confirmed Explicitly: No`.
- **Don't write carve-out labels into BACKLOG change list.** Those are recap-time labels only.
- **Don't perform git operations.** Commit, tag, and push belong to `/sovgit`.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 105.*
