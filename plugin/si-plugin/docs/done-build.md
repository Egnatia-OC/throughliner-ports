# Build close-out

Close-out for build batches (including their test entries). Reached from done.md's router when _build.md's Entry carries a Build subheading — or a Spec-edit subheading, since a spec-edit batch closes like any build through these same steps.

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### Mid-close directive — new scope vs build-completing fix [PROMPT]

If a new directive arises during the close — the user raises a change, or verification turns one up — decide where it goes by one line: does it complete the just-built work's own verification, or is it new scope? A fix to a genuine bug in what this build was meant to deliver folds in (finish it, tick it — it's part of the build). New scope — a redesign, a new feature, a change to something that already worked — routes out: a fresh /next, or a capture if it isn't urgent, even if it looks small and even if the user raises it here. /done records and commits; it doesn't take on new build scope. This applies the general mid-close rule in plugin-behaviour.md (Routing and discipline) at the build close.

### 1.1 Verify completion

Read _build.md. All entries ticked?
- **Yes:** Proceed. A test ticked `deferred (reason)` counts as closed, not unfinished — it ran as far as this session could take it, and step 1.3 turns it into a queue line.
- **Some unticked:** [PROMPT] Ask — finish (/next) or close partial (defer unticked, route back to QUEUE.md). Wait for the user's call.

Reconcile the file against memory where the session is still remembered: if _build.md and what you recall disagree — work that happened but went unticked, a Changes note missing something memory knows was done — that mismatch is itself a finding about build discipline, and it routes to Captures (per 1.2). It's the only routine check _build.md's accuracy gets before a fresh session has to rely on it.

### 1.2 Route findings to Captures [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged is _build.md's notes plus any captures already routed at the moment of noticing — sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Route each finding to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Route test failure fixes too.

### 1.3 Write deferred tests

Any planned test from the batch that couldn't run in this session goes to QUEUE.md's "## Deferred tests" section, per done.md Deferred tests — never as LOG-entry prose alone. Each entry ticked `deferred (reason)` in Progress converts mechanically into one queue line: source batch slug, what to verify, what confirms it, and both axes done.md defines — the deferral reason (host-side / needs-user / external) and the runnability once unblocked (Claude-runnable / user-run).

### 1.4 Spec-drift check [SILENT] when nothing drifts, [BRIEF] when filing

Build closes only (test and audit land no product changes). Read SPEC.md against the changes this build landed and apply the spec-entry trigger test in its canonical form — the Spec-edit batches rule in plan.md (Step 3), whose test is whether any sentence in SPEC goes wrong or incomplete given these changes. Quote plan.md's wording rather than restating it, so the two don't drift. If the test fires, file a mandatory capture naming the gap — which SPEC sentence the build made wrong or incomplete. Never edit SPEC.md here: product-truth edits stay in /plan and ship through a spec-edit batch, so this is a detect-and-file backstop, not an author. The trigger exists because the prospective /plan gate has leaked before — a build landed a spec-affecting change with no prior spec entry, caught only by luck at /done. Path-split like the staleness sweep: silent when nothing drifts, one or two sentences when filing.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Narrate first [BRIEF]: one sentence noting the batch's reasoning is being carried from _build.md into the LOG entry — the file's last job before /done deletes it.

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the batch's rationale in _build.md, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files). This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and the build ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Path-split like next.md's pre-flight: stay silent when the sweep finds nothing; surface a flag in one or two sentences when it does. Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this build changed:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that this build (or any prior shift the queue hasn't caught up to) has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag — and split the flag by the fix path in plugin-behaviour.md Staleness watch: a fate-decision flag (drop / rewrite / keep) defers to /plan; a drifted pointer on an otherwise-valid item, whose target content is unchanged, may be fixed here with the user's approval, riding this commit. Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next [BRIEF, PROMPT]

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). State the scan's result either way, not only when it blocks: Captures empty — say nothing's waiting for /plan; Captures waiting but none overlap the next batch — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three captures are waiting; none touches the next batch, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
1. Captures routed this session that affect the next batch → recommend /plan, name the blocker.
2. Parked items unblocked by this session's work (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
4. Batches empty → "Queue is clear. Run /plan when you have more."
