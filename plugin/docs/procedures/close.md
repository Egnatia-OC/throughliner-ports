# Close procedure — Sovereign Implementer

Close a session after any session type. Post-build has two `[PROMPT]` stops; planning/general has one. Claude must wait for the user at each stop — never absorb close steps silently.

## Phase detection

1. Check whether `_method/active-build.md` exists.
2. Exists and all Files: ticked → **post-build path**.
3. Exists with unticked files → halt (build not finished).
4. No snapshot → **planning/general path**.

---

## Post-build path

### Step 1 — record

Load: `CLAUDE.md` (path block), `_method/active-build.md` (read `## Close handoff`), `TEST-LOG.md` (per-session files in `test-log/`), `MANIFEST.md`.

**Idempotency.** If TEST-LOG already has rows for this session covering the batch → close already done. Stop.

**Session ID.** Derive from `proxies/build-log.md` → first entry → per-build file H1 first token. Fallback: today's YYYY-MM-DD.

**MANIFEST update.** Per ticked file: add new entries (with `(path)` and `*Rationale: [why / vNN].*`), update changed entries, remove deleted entries. Alphabetical. Update `## Capabilities summary` — one paragraph derived from entries.

**TEST-LOG rows.** One row per observable behaviour, 10-column format per `DOC-STRUCTURE.md` → *TEST-LOG structure*. Draw from batch `Tests:` sub-section. Respect markers:
- **`[Build]` tests:** Claude runs the test now. Fill Status, `Confirmed Explicitly: Yes (YYYY-MM-DD)`, Notes.
- **`[E2E]` tests:** Status blank, `Confirmed Explicitly: No`. Defines the test session for future planning read-back.

Allocate per-session file in `test-log/` (scan for highest number, increment). Prepend index line to BACKLOG.md `## Test sessions`.

### Step 2 — recap `[PROMPT]`

Present to the user:

- **Changes shipped.** One bullet per change with `[Requested]`/`[Suggested]` labels. Carve-outs get `[Prerequisite]`/`[Re-batch]`.
- **Claude has verified.** One bullet per `[Build]` test with Pass/Fail.
- **Pending manual check.** One bullet per `[E2E]` test, in TEST-LOG order.
- **Flags.** Stale references found, out-of-scope improvements, UX.md changes implied (don't edit — flag only), red flag concerns.

`[PROMPT]` "Review the recap. When ready, I'll write the build-log entry and clean up."

### Step 3 — finalize

**Build-log entry.** Allocate file in `build-log/` (scan for highest number, increment). Write per `DOC-STRUCTURE.md` → *Build log structure*. Draw narrative from `## Close handoff`. Include `## Performance` section. Prepend index line to `_method/proxies/build-log.md`.

**Delete snapshot.** Delete `_method/active-build.md`.

**Sweeps.** Three checks — brief if findings, silent if not:
- **Staleness:** grep BACKLOG batches for old name/path references from renamed/deleted/moved files.
- **Frame correction:** scan BACKLOG and `[PROPOSED EDIT PENDING]` blocks for old-behaviour references.
- **Lost-feature:** scan parked batches for parking conditions just met. Surface and ask about unparking.

Route findings to BACKLOG `## Open questions` section if they need future resolution.

**Idea sweep.** Review session for unrouted ideas or observations. Triage: BACKLOG (batch or OQ) or flag for user. Nothing unrouted survives close.

**Footers and proxies.** Bump method-version footers if applicable:
```
python "${CLAUDE_PLUGIN_ROOT}/scripts/bump_version.py" <old> <new>
```
Regenerate proxies whose source was edited (MANIFEST, TEST-LOG index, build-log index at minimum):
```
python "${CLAUDE_PLUGIN_ROOT}/scripts/bump_version.py"
```
Then review proxy summaries for structural changes the script can't detect.

**After-build steps.** If CLAUDE.md has `## After-build steps`, execute each. Skip if absent.

### Step 4 — close `[PROMPT]`

`[PROMPT]` "Close complete. Run `/sovgit` to commit, tag, and push. After that, test — run `/sovtest` for a guided walkthrough of pending tests, or bring outcomes to your next planning session."

---

## Planning/general path

Lighter close for planning, deliberation, or general sessions.

### Step 1 — wrap up

**Idea sweep.** Review session for unrouted ideas or observations. Triage to BACKLOG (batch or OQ) or flag for user.

**Build-log entry.** Same allocation as post-build. Narrative sections only — no `## Performance`:
```markdown
# <Session> — YYYY-MM-DD — Summary

**What shipped.** <planning changes, OQ resolutions, BACKLOG edits>
**Decisions taken and why.** <if any>
**Pivots and surprises.** <if any>
```
Prepend index line to `_method/proxies/build-log.md`.

**Conditional sweeps** (only if this session consumed/restructured a BACKLOG batch):
- Staleness sweep for old references.
- Frame-correction sweep for old-behaviour references.
- Lost-feature check for met parking conditions.

**Footers and proxies.** Bump if applicable. Regenerate edited proxies.

### Step 2 — close `[PROMPT]`

`[PROMPT]` "Close complete. Run `/sovgit` to commit, tag, and push."

---

## What you must not do

- **Don't edit source files or build files.** Scope: method docs only (MANIFEST, test-log, build-log, BACKLOG, proxies).
- **Don't edit source-of-truth docs.** UX.md is locked. Flag changes in recap.
- **Don't infer test outcomes.** `[Build]` tests: run and report. `[E2E]` tests: blank Status, `Confirmed Explicitly: No`.
- **Don't start a new build.**
- **Don't perform git operations.** Commit, tag, push → `/sovgit`.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity.

---

*Sovereign Implementer — Version 112.*
