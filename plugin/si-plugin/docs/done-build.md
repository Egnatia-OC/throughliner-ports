# Build close-out

Close-out for build-flavor work lines. Reached from done.md's router for the run's build lines (work lines carrying no flavor tag). A build that changed SPEC.md (because it grew scope to include it mid-build, or a build line listed it) closes here like any other build — there is no separate spec-edit close.

A run may contain several build lines. The judgment and record steps below apply per built line where noted — one LOG entry per line — while the staleness sweep, commit, and recommendation run once for the whole close.

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### Mid-close directive — new scope vs build-completing fix [PROMPT]

If a new directive arises during the close — the user raises a change, or verification turns one up — decide where it goes by one line: does it complete the just-built work's own verification, or is it new scope? A fix to a genuine bug in what this build was meant to deliver folds in (finish it, tick it — it's part of the build). New scope — a redesign, a new feature, a change to something that already worked — routes out: a fresh /next, or a capture appended to Unprocessed if it isn't urgent, even if it looks small and even if the user raises it here. /done records and commits; it doesn't take on new build scope. This applies the general mid-close rule in plugin-behaviour.md (Routing and discipline) at the build close.

### 1.1 Verify completion

Read _build.md. Every build line in the run ticked in Progress?
- **Yes:** Proceed.
- **Some unticked:** [PROMPT] Ask — finish (/next) or close partial (defer the unticked lines, returning them to QUEUE.md's Processed section). Wait for the user's call.

Reconcile the file against memory where the session is still remembered: if _build.md and what you recall disagree — work that happened but went unticked, a Changes note missing something memory knows was done — that mismatch is itself a finding about build discipline, and it routes to Unprocessed (per 1.2). It's the only routine check _build.md's accuracy gets before a fresh session has to rely on it.

### 1.2 Route findings to Unprocessed [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged is _build.md's notes plus any captures already appended at the moment of noticing — sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Append each finding to Unprocessed, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Append any fix a build check surfaced too.

### 1.3 Spec-sync gate [SILENT] when nothing drifts, [PROMPT] when drift found

Build closes only (audits land no product changes). Read SPEC.md against the changes this build landed and apply the spec-entry trigger test — whether any sentence in SPEC goes wrong or incomplete given these changes. That is the test plan.md's "SPEC changes are normal build scope" rule names; quote its wording rather than restating it, so the two don't drift.

If the test fires, stop the close — don't commit yet. Surface the drift in plain words, naming which SPEC sentence the build made wrong or incomplete, and get the user's approval to fix it. Then add SPEC.md to _build.md's `Files:` list (so the scope-lock allows the edit), edit SPEC to match what the build landed, and commit SPEC together with the build in this same commit. Don't file it as a capture for a later session.

The why this is a stop-the-close gate, not a detect-and-file backstop: SPEC is in-session-editable now — the spec-edit batch type is retired (plan.md) — so a build that changed product truth can and must bring SPEC into line in the same commit. Spec-driven development's contract is that the spec moves in the same commit as the behaviour change (resources/research/spec-driven-development-edit-workflow.md); deferring the SPEC fix to a capture would close a commit with SPEC already behind, breaking that atomicity — the exact drift this gate prevents. The gate also catches the leak the old detect-and-file backstop existed for: a build landing a spec-affecting change with no prior spec entry, now fixed in-session rather than filed for luck to catch later. Path-split like the staleness sweep: silent when nothing drifts; stop and surface when it does. Scope: every build close where the build changed product truth.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Narrate first [BRIEF]: one sentence noting the work's reasoning is being carried from _build.md into the LOG entry — the file's last job before /done deletes it.

A run may have built several build lines. Write one LOG entry file per built line, each named after that line's slug (done.md LOG entry files), reusing that line's pre-generated Index entry candidate. Draft each as its own file under `LOG/`, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the work line's rationale in _build.md, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

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

If _build.md carries a matching `Index entry candidate` for the line and it built as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Stay silent when nothing's stale; surface a flag in one or two sentences when something is. Quick check of the remaining work lines in QUEUE.md — any staleness from any cause, not just what this build changed:
- Do any remaining Unprocessed or Processed work lines reference files this build (or an earlier shift the queue hasn't caught up to) renamed or deleted?
- Do any reference behaviour or rules that a shift since has moved past?
- Are any sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag it — and split by fix path: a fate decision (drop / rewrite / keep the affected line) is /plan's, so defer it; a pure pointer drift — a file reference whose target content is unchanged — is mechanical, so fix it here and report it in one line, riding this commit, with no approval ask (the same ride-along as the hash backfill).

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md.

**Under a cruise run:** the commit core's wind-down re-scan auto-files what it surfaces instead of prompting for approval, and no push is offered (the run commits per line and publishes nothing outward). See cruise.md's Autonomy adaptations — this note just marks that the same close runs with its user-approval moments answered unattended.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the queue situation in everyday words — never the background section-bookkeeping phrasing. Keep the plain statement accurate: don't say the queue is clear when work is still waiting to be sorted.

Before recommending, scan the still-unprocessed work for overlap with the top processed item — work that contradicts, invalidates, or would benefit it if sorted first. State the scan's result either way, not only when it blocks: nothing unprocessed — say nothing's waiting for /plan; unprocessed work waiting but none overlaps the next item — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three items are waiting to be sorted; none touches the next piece of work, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
1. Captures appended this session that affect the next work → recommend /plan, name the blocker.
2. Processed work exists → name the next item, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
3. Processed empty → "Queue is clear. Run /plan when you have more."
