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

Check _build.md and conversation for anything flagged during the build. Route each to Captures. Route test failure fixes too.

#### 1.4 Build recap [BRIEF]

- What was built (from _build.md Changes)
- Anything routed to Captures

### Phase 2: Mechanical

#### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry for `LOG/log.md` using this template (placeholder hash — filled after commit at 2.4):

```markdown
## [HASH] — [one-line summary]

[Prose rationale — re-authored from the batch's rationale, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in behaviour.md. After approval, prepend to `LOG/log.md` after the header, before existing entries.

Prepend to `LOG/index.md` after the header:

```
- [HASH] — [one-line summary]
```

#### 2.2 Staleness sweep

Quick check of QUEUE.md:
- Remaining batches or Captures reference renamed/deleted files?
- Reference old behaviour this build changed?
- If so, flag (don't edit without asking).

#### 2.3 Delete _build.md

Unlocks future builds. Only after everything above is complete.

#### 2.4 Git commit and hash backfill [BRIEF, PROMPT]

1. Stage files from _build.md Changes plus method docs (QUEUE.md, REGISTRY.md, LOG/, _build.md deletion).
2. Never `git add -A` or `git add .`.
3. Draft commit message. Present for approval.
4. Wait for okay.
5. After commit: `git rev-parse --short HEAD` for the hash.
6. Replace `[HASH]` in LOG/log.md and LOG/index.md.
7. Stage updated files, amend (`git commit --amend --no-edit`).

### Phase 3: Handoff [BRIEF, PROMPT]

"Push to remote? (yes / not yet)"

Then recommend based on queue state:
1. Captures routed that affect next batch → recommend /plan, name the blocker.
2. More batches → "Next up is [batch]. Run /next or /plan when ready."
3. Batches empty → "Queue is clear. Run /plan when you have more."

Tell the user to run `/clear` before the next skill — a commit (and possibly a push) just happened.

---

## Plan close-out

### 1. Recap

- Batches created or modified
- Captures promoted, parked, or dropped
- Questions resolved
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

Show the wording to the user for approval before writing — see Why-pipeline in behaviour.md. After approval, prepend to `LOG/log.md` after the header.

Prepend to `LOG/index.md`:

```
- [HASH] — [one-line summary]
```

### 3. Git commit and hash backfill [BRIEF, PROMPT]

1. Stage only changed method docs (QUEUE.md, SPEC.md, REGISTRY.md, LOG/).
2. Never `git add -A` or `git add .`.
3. Draft commit message. Present for approval.
4. Wait for okay.
5. After commit: `git rev-parse --short HEAD`.
6. Replace `[HASH]` in LOG/log.md and LOG/index.md.
7. Stage, amend (`git commit --amend --no-edit`).

### 4. Handoff [BRIEF, PROMPT]

"Push to remote? (yes / not yet)"

- Batches exist: "Next up is [batch]. Run /next or /plan when ready."
- Batches empty: "Queue is clear."

Tell the user to run `/clear` before the next skill — a commit (and possibly a push) just happened.

---

## Rules

- Do NOT skip Phase 1 even if the user says "just commit."
- Git push is always a prompt, never automatic.
- Mode detection is automatic. Don't ask — check for _build.md.
