# /done procedure

You are closing the current session — recording what happened, updating docs, and committing.

## Mode detection

Check whether _build.md exists:
- **Yes → Build close-out.** A /next build just finished. Follow the full procedure below.
- **No → Plan close-out.** A /plan session just finished. Skip to the Plan close-out section.

---

## Build close-out

Use this after /next. The full procedure: verify, test, log, commit.

### Phase 1: Judgment (do this while context is fresh)

These steps capture meaning that would be lost after compaction.

#### 1.1 Verify completion

Read _build.md. Are all entries ticked in Progress?
- **All ticked:** Proceed.
- **Some unticked:** Ask the user — finish them (/next to continue), or close partial (mark unticked entries as deferred and route back to QUEUE.md).

#### 1.2 Generate tests

These are post-build verification tests — distinct from batch [test] entries. Batch [test] entries were already executed during /next and their results are recorded in _build.md. Generate /done tests only for [build] entries that changed code or app files — not for procedure doc or template edits, where the batch's own [test] entries already cover verification.

For each code/app file that was built or changed, write one test per observable behaviour:

Format each test as:
```
- [ ] [Type] Description — Verifier
```

Types:
- **[Look]** — visual check (open the page/screen, confirm it looks right)
- **[Run]** — execute a command or action, check the output
- **[Trigger]** — cause an event, observe the response
- **[Inspect]** — examine generated output or file content

Verifier is either `Claude` (can be checked programmatically or by reading code) or `User` (requires human eyes or interaction).

#### 1.3 Run Claude-verifiable tests

For any test marked `Claude`: run it now. Report pass/fail. Update the test line:
- `- [x] [Run] API returns 200 — Claude ✓`
- `- [x] [Run] API returns 200 — Claude ✗ (got 404, see note)`

Failed Claude tests: note the failure, suggest whether it's a bug (route to queue) or expected (user decides).

#### 1.4 Present user tests [SEQUENCE, PROMPT]

List remaining tests (User-verified) for the user. One at a time:
- State what to check and how.
- Wait for pass/fail.
- On failure: gather what happened, investigate if possible, route the fix to QUEUE.md. Do NOT fix during close.

If the user wants to skip testing: allow it, but note "tests skipped" in the log.

#### 1.5 Update REGISTRY.md

For each file that was created, renamed, deleted, or significantly modified:
- Add new entries (path + one-line description of what it is)
- Update descriptions if the file's role changed
- Remove entries for deleted files

#### 1.6 Route findings to Captures

During the build, Claude or the user may have noticed gaps, issues, or opportunities that weren't part of the current scope. Check _build.md and conversation for anything flagged. For each finding:

- Add it to the **Captures** section of QUEUE.md as an `[idea]` entry.
- Don't promote findings to batches during /done — that's /plan's job.
- If a test failure needs a fix, route the fix to Captures too (not directly to a batch).

This keeps /done mechanical and defers judgment to the next /plan session.

#### 1.7 Build recap [BRIEF]

Summarize for the user:
- What was built (from _build.md Changes section)
- Test results (passed / failed / skipped)
- Anything routed to Captures

### Phase 2: Mechanical (rote file operations) [SILENT]

#### 2.1 Write LOG entry

Prepend the log entry to `LOG/log.md` — insert it immediately after the `# LOG` header line and its description, before any existing entries. Use a placeholder for the commit hash — it gets filled in after the commit (step 2.4).

```markdown
## [HASH] — [one-line summary of what shipped]

**Files touched:**
- [from _build.md Changes section]

**Tests:** [X passed, Y failed, Z skipped]

**Why:** [what motivated the work and the approach — user direction, planning rationale, tradeoffs, constraints discovered during the build. Always present — every build has reasoning worth recording.]

**Routed to Captures:** [anything added to the Captures section, or "none"]
```

Prepend a one-line entry to `LOG/index.md` — insert it immediately after the `# LOG Index` header line and its description, before any existing entries:

```
- [HASH] — [one-line summary]
```

#### 2.2 Staleness sweep

Quick check of QUEUE.md:
- Do any remaining batches or Captures reference files that were renamed or deleted in this build?
- Do any reference old behaviour that this build changed?
- If so, flag them (don't edit without asking).

#### 2.3 Delete _build.md

Created by /next Step 2 when the batch was locked. Deleting it unlocks future builds. Only do this after everything above is complete.

#### 2.4 Git commit and hash backfill [BRIEF, PROMPT]

1. Stage the files listed in _build.md's Changes section plus the method docs (QUEUE.md — already modified by /next Step 2 when the batch moved to _build.md, REGISTRY.md, LOG/, _build.md deletion).
2. Never use `git add -A` or `git add .`.
3. Draft a commit message. Present it for approval.
4. Wait for the user's okay before committing.
5. After commit: run `git rev-parse --short HEAD` to get the hash.
6. Replace every `[HASH]` placeholder in LOG/log.md and LOG/index.md with the actual hash.
7. Stage the updated files and amend the commit (`git commit --amend --no-edit`).

### Phase 3: Handoff [BRIEF, PROMPT]

Evaluate the queue state and make one recommendation (check in this order):
1. If items were routed to Captures during this session and any of them affect the next batch → recommend /plan first, name the blocking item.
2. If QUEUE.md has more batches → recommend the next batch by name.
3. If QUEUE.md Batches section is empty → "Queue is clear. Run /plan when you have more to add."

Then: "Push to remote? (yes / not yet)" — never push automatically.

---

## Plan close-out

Use this after /plan. Lighter procedure: log what was decided, commit.

### 1. Recap

Summarize what happened during the /plan session:
- Batches created or modified
- Captures promoted, parked, or dropped
- Questions resolved
- Any spec changes

### 2. Write LOG entry

Prepend the log entry to `LOG/log.md` — insert it immediately after the header, before any existing entries. Use a placeholder for the commit hash.

```markdown
## [HASH] — [one-line summary of what was decided or organized]

**Queue changes:**
- [batches added, reordered, or modified]

**Why:** [what motivated the queue changes — user priorities, dependency analysis, captured observations. Always present.]

**Captures routed:** [what was promoted/parked/dropped from Captures, or "none"]
```

Prepend a one-line entry to `LOG/index.md` — insert it immediately after the header, before any existing entries:

```
- [HASH] — [one-line summary]
```

### 3. Git commit and hash backfill [BRIEF, PROMPT]

1. Stage only the method docs that changed (QUEUE.md, SPEC.md, REGISTRY.md, LOG/).
2. Never use `git add -A` or `git add .`.
3. Draft a commit message. Present it for approval.
4. Wait for the user's okay before committing.
5. After commit: run `git rev-parse --short HEAD` to get the hash.
6. Replace every `[HASH]` placeholder in LOG/log.md and LOG/index.md with the actual hash.
7. Stage the updated files and amend the commit (`git commit --amend --no-edit`).

### 4. Handoff [BRIEF, PROMPT]

Tell the user what's next:
- If QUEUE.md has batches: "Next up is [batch]. Run /next when ready."
- If QUEUE.md Batches section is empty: "Queue is clear."

Then: "Push to remote? (yes / not yet)" — never push automatically.

---

## Rules

- Do NOT skip Phase 1 (build close-out) even if the user says "just commit." The judgment steps prevent drift.
- One test at a time for user-verified tests. Don't dump the full list.
- Failed tests route to Captures — never fix during /done.
- Git push is always a prompt, never automatic.
- Mode detection is automatic. Don't ask the user which mode — check for _build.md.
