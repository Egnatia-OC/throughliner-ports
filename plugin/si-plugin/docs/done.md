# /done procedure

Close the current session — record what happened, update docs, commit.

## Mode detection

Check for _build.md:
- **Exists → Build close-out.** Full procedure below.
- **Missing → Plan close-out.** Skip to Plan close-out section.

---

## Build close-out

### Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

#### 1.1 Verify completion

Read _build.md. All entries ticked?
- **Yes:** Proceed.
- **Some unticked:** Ask — finish (/next) or close partial (defer unticked, route back to QUEUE.md).

#### 1.2 Update REGISTRY.md

For each file created, renamed, deleted, or significantly modified:
- Add new entries (path + one-line description)
- Update descriptions if role changed
- Remove entries for deleted files

#### 1.3 Route findings to Captures

Check _build.md and conversation for anything flagged during the build. Route each to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Route test failure fixes too.

#### 1.4 Build recap [BRIEF]

- What was built (from _build.md Changes)
- Anything routed to Captures

### Phase 2: Mechanical

#### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry for `LOG/log.md` using this template (placeholder hash — backfilled at the next /plan or /next session start):

```markdown
## [HASH] — [one-line summary]

[Prose rationale — re-authored from the batch's rationale, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. After approval, prepend to `LOG/log.md` after the header, before existing entries.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries:

```
- [HASH] — [index entry]
```

If _build.md contains an `Index entry candidate:` line and the build ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

#### 2.2 Staleness sweep

Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this build changed:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that this build (or any prior shift the queue hasn't caught up to) has moved past?
- Items sitting long enough that the surrounding code or rules have drifted away from them?
- If so, flag (don't edit without asking). Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

#### 2.3 Delete _build.md

Unlocks future builds. Only after everything above is complete.

#### 2.4 Git commit and push [BRIEF, PROMPT]

1. Stage files from _build.md Changes plus method docs (QUEUE.md, REGISTRY.md, LOG/, _build.md deletion).
2. Never `git add -A` or `git add .`.
3. Draft commit message title and body. Present both in the same message, each in its own fenced code block (see plugin-behaviour.md "Verbatim-copy strings"), and ask in the same approval moment: "Commit and push, or just commit?"
4. Wait for okay, then commit — and push if the user chose to push.

The LOG entry keeps its `[HASH]` placeholder for now. The next /plan or /next session backfills it as a working-tree edit that folds into whatever commit that session makes — no amend, no two-commit flow.

### Phase 3: Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors next.md Step 1.4). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
1. Captures routed this session that affect the next batch → recommend /plan, name the blocker.
2. Parked items unblocked by this session's work (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
4. Batches empty → "Queue is clear. Run /plan when you have more."

---

## Plan close-out

### 1. Recap

- Batches created or modified
- Captures promoted, parked, or dropped
- Spec changes

### 2. Write LOG entry [DISCUSS, PROMPT]

Draft the entry for `LOG/log.md` using this template (placeholder hash):

```markdown
## [HASH] — [one-line summary]

[Prose rationale — what motivated these queue changes, as inline prose. No `Why:` label.]

**Queue changes:**
- [batches added, reordered, or modified]

**Captures routed:** [promoted/parked/dropped, or "none"]
```

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. After approval, prepend to `LOG/log.md` after the header.

Prepend to `LOG/index.md`, per plugin-behaviour.md Index entries:

```
- [HASH] — [index entry]
```

### 3. Git commit and push [BRIEF, PROMPT]

1. Stage only changed method docs (QUEUE.md, SPEC.md, REGISTRY.md, LOG/).
2. Never `git add -A` or `git add .`.
3. Draft commit message title and body. Present both in the same message, each in its own fenced code block (see plugin-behaviour.md "Verbatim-copy strings"), and ask in the same approval moment: "Commit and push, or just commit?"
4. Wait for okay, then commit — and push if the user chose to push.

The LOG entry keeps its `[HASH]` placeholder for now. The next /plan or /next session backfills it as a working-tree edit that folds into whatever commit that session makes — no amend, no two-commit flow.

### 4. Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors next.md Step 1.4). If any are found, recommend /plan first and name the overlap.

Otherwise, based on queue state:
- Parked items unblocked by this session's planning work (per plugin-behaviour.md Dependency ownership Unpark watch) → mention the unpark candidate(s) as part of the recommendation.
- Batches exist: name the next batch, then ask whether the user is continuing into a /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
- Batches empty: "Queue is clear. Run /plan when you have more."

---

## Rules

- Do NOT skip Phase 1 even if the user says "just commit."
- Git push is always a prompt, never automatic.
- Mode detection is automatic. Don't ask — check for _build.md.
