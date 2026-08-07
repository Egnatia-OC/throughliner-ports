# /done procedure

Close the current session — record what happened, update docs, commit. This doc routes to a per-flavor close-out and states the commit core once; the sub-docs carry the flavor-specific steps.

## Route by session shape [SILENT]

Check for _build.md. The check is automatic — don't ask, and don't narrate the routing; just route:

**The _build.md read is unconditional.** When _build.md exists, read it in full before the close-out runs — regardless of how much of the session you remember. Conversation memory enriches the LOG entry (tradeoffs, learnings, colour the file doesn't capture) but never substitutes for the read. The why: a "read it only if you don't remember the session" condition hangs on Claude assessing its own memory, which fails exactly post-/clear and post-compaction — when the session feels remembered but the details are gone. Stated once here; the sub-docs route through this rule rather than restating it.

- **_build.md exists** → read it, then route by the flavor of the run's work items (its `Run:` and `Entries:` — the same flavors /next routed on):
  - **Build** items (no flavor tag) → read and follow `done-build.md`. A build that changed SPEC.md closes here like any other build — same steps, same commit core.
  - **`[audit]`** items → read and follow `done-audit.md`.
  - A run of one flavor follows that flavor's close-out. A mixed run — say a build item and an audit item built back-to-back — closes each item through its own flavor's close-out (build items via done-build.md, audit items via done-audit.md), writing one LOG entry per item and sharing the single end-of-session commit.
- **No _build.md** → no build ran this session. Three shapes:
  - **A completed `[user]` item** — the user ran a `[user]` item that a past session walked them through (or presented) and wants it recorded. Detect by asking: if Processed holds any `[user]` item, ask whether the user just completed one (a fresh chat won't remember it, so the ask is what surfaces it). If yes → follow **Completed `[user]`-item close** below. This can coincide with a planning session; when it does, close the item through that section and let done-plan.md handle the rest.
  - **A planning session** — the session managed the queue, processed captures, or moved the readiness line (or _plan.md exists) → read and follow `done-plan.md`.
  - **A standalone handmade-work close** — no planning happened either, and the working tree holds uncommitted edits the session didn't make through a skill (the user changed files by hand) → follow **Standalone handmade-work close** below. Read those edits as the user's own expected work, not a broken repo (plugin-behaviour.md, the don't-panic reading), confirm with the user, then log and commit them.

The sub-doc runs the close-out. When it reaches its Commit step, run the commit core below, then return to the sub-doc for the recommendation.

There is no test close-out — the test flavor is retired. A check Claude can run is part of building, closed by done-build.md. A check only the user can run is a `[user]` work item, which /next walks the user through and which never enters a _build.md — so /done doesn't close it *as a build*, but once the user has run it, /done does record its completion and remove it from the queue, through the Completed `[user]`-item close below.

## Completed `[user]`-item close [BRIEF, PROMPT]

Reached when the user has done a `[user]` item and wants it recorded. A `[user]` item never entered a _build.md, so it isn't ticked and closed like a build — this is the close that records it and removes it from Processed, so a finished `[user]` item doesn't strand in the queue and get re-presented by the next /next. It also runs inside a /plan close (done-plan.md points here) when the user mentions async-completed `[user]` items at planning.

1. **Confirm which `[user]` item(s) completed** [PROMPT]. Name the `[user]` items still in Processed and confirm which the user actually finished. Only the confirmed-done ones close here; the rest stay in Processed for a later walk-through.
2. **Write a LOG entry per completed item**, named after its slug (done.md LOG entry files). The entry records what the user did and its outcome — draft the one-liner and rationale and show them for approval, per plugin-behaviour.md Captures and the LOG entry files section below. If a completed item carried a red-flag marker, run the Red-flag lifecycle at close below.
3. **Remove each completed item from Processed** — this is what stops it being re-presented. (The shipped-slug cross-check in the commit core backstops it.)
4. **Run the wind-down re-scan, then the commit core** (both below), staging QUEUE.md and the LOG changes. A remote-gated push offer applies as normal — a completed `[user]` item is real project progress, not bookkeeping.

## Standalone handmade-work close [BRIEF, PROMPT]

Reached when /done runs with no _build.md and no planning work — the user made ad-hoc edits by hand and wants them recorded. This is the case the retired freeform close used to own. It is never required: hand edits left uncommitted are simply swept into the next /done (build or planning) that runs. It exists for when the user wants their handmade work logged and committed as its own clean record.

1. **Read the edits as the user's own work — don't panic.** Uncommitted changes the session didn't make are most likely the user's expected work (plugin-behaviour.md, the don't-panic reading). Run `git status --porcelain`, and where what changed isn't self-evident, look. Confirm with the user that these are theirs and meant to be saved. Never report them as a broken repo or a problem, and never try to undo them.
2. **Decide LOG granularity by judgment.** If the edits are one coherent change, write a single date-named entry — `LOG/<YYYY-MM-DD>-handmade.md` (`-2` if the name is taken). If they span several distinct logical changes, write a separate entry per logical change rather than one lumped entry — better recall when the log is referenced later. (The right unit converges with the two-section LOG-index question and defers to whatever that resolves.) Draft each entry's one-liner and rationale and show them for approval, per the LOG entry files section below and plugin-behaviour.md Captures.
3. **Run the wind-down re-scan, then the commit core** (both below), staging the hand-edited files explicitly. The commit message is the approved entry; for several entries, the title names the handmade-work close and the body carries each entry's summary. Unlike a planning close, a handmade-work close does offer push when a remote exists — it's real project work, not bookkeeping — following the commit core's remote-gated push exactly.

## Verify completion [PROMPT when unticked]

Stated once here; the build and audit close-outs point at this section for their Phase-1 completion check.

Read _build.md. Is every item in the run ticked in Progress — each build item done, each audit finding captured or dropped?
- **Yes:** proceed.
- **Some unticked:** [PROMPT] Ask — finish the rest (/next) or close partial (defer the unticked items, returning them to QUEUE.md's Processed section). Wait for the user's call.

**Build-close delta — reconcile against memory.** At a build close, where the session is still remembered, reconcile _build.md against what you recall: if the file and memory disagree — work that happened but went unticked, a Changes note missing something memory knows was done — that mismatch is itself a finding about build discipline, and it routes to Unprocessed (via the build close's findings-routing step). It's the only routine check _build.md's accuracy gets before a fresh session has to rely on it. An audit close carries no such reconcile.

## Spec-sync gate [SILENT] when in sync; [PROMPT] when drift found

Stated once here; the build and plan close-outs point at this section. (Audits land no product changes, so an audit close has no spec-sync gate.)

Before recording, check one thing: did this session's work change what SPEC says? Apply the spec-entry trigger test — whether any SPEC sentence goes wrong or incomplete given the changes this session landed. For a build close, that is the test plan.md's "SPEC changes are normal build scope" rule names; quote its wording rather than restating it, so the two don't drift.

If the test fires, stop the close — don't commit yet. Surface the drift in plain words, naming which SPEC sentence the session made wrong or incomplete, and get the user's approval to fix it. Then edit SPEC to match what the session landed, and commit SPEC in this same commit. Don't file it as a capture for a later session.

The why — the same for both flavors: spec-driven development's contract is that the spec moves in the same commit as the behaviour change (resources/research/spec-driven-development-edit-workflow.md). Deferring the SPEC fix to a capture would close a commit with SPEC already behind, breaking that atomicity — the exact drift this gate prevents. SPEC is in-session-editable now (the separate spec-edit step is retired — plan.md), so a session that changed product truth can and must bring SPEC into line in the same commit. Path-split like the staleness sweep: silent when nothing drifts; stop and surface when it does.

Two flavor deltas in *how* the edit is permitted:
- **Build close:** SPEC.md is scope-locked, so add SPEC.md to _build.md's `Files:` list before editing (so the scope-lock allows the edit), then edit SPEC to match. The gate also catches the leak the old detect-and-file backstop existed for: a build landing a spec-affecting change with no prior spec entry, now fixed in-session rather than filed for luck to catch later. Scope: every build close where the build changed product truth.
- **Plan close:** no scope-lock is active, so edit SPEC.md directly in-session. Editing SPEC to match a decision the user already made this session is recording, not re-planning — the decision is settled, SPEC is just brought into line. A session that changed only queue ordering or captures touched no SPEC sentence and passes silently. Scope: every plan-type /done close (plan, setup, method-doc-only sessions).

## Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Stated once here; the build and audit close-outs point at this section for their Phase-2 sweep.

Stay silent when nothing's stale; surface a flag in one or two sentences when something is. Quick check of the remaining work items in QUEUE.md — any staleness from any cause, not just what this session changed:
- Do any remaining Unprocessed or Processed work items reference files anything since has renamed or deleted?
- Do any reference behaviour or rules that a shift since has moved past?
- Are any sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag it — and split by fix path: a fate decision (drop / rewrite / keep the affected item) is /plan's, so defer it; a pure pointer drift — a file reference whose target content is unchanged — is mechanical, so fix it here and report it in one line, riding this commit, with no approval ask (the same ride-along as the hash backfill).

## LOG entry files

Stated once here; every sub-doc's entry-writing step points at this section.

**One text, several positions.** The session authors two texts, not four. The one-liner is the same authored text in three positions: the entry heading's summary, the index line's body, and the commit title. The rationale prose is the same authored text in two positions: the entry body and the commit body. The user approves both once — at the entry-writing step — and the commit step (commit core above) reuses them verbatim, with nothing new to read.

**Entry template and approval (shared).** Stated once here; every sub-doc's entry-writing step points at this template and approval frame, adding only its per-flavor body fields. Draft each entry as its own file under `LOG/`, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the work's rationale in _build.md (or, for a planning session, what motivated these queue changes), expanded with what was learned along the way. Inline prose, no `Why:` label.]

[per-flavor body fields — see the flavor deltas below]
```

Per-flavor body fields (the only delta between flavors):
- **Build:** `**Files touched:**` (from _build.md Changes) and `**Routed to Captures:**` (items added, or "none").
- **Audit:** `**Files touched:**` (the target artifacts read — the audit edited nothing), `**Routed to Captures:**` (findings captured, or "none"), and `**Approval outcomes:**` (what happened at bulk approval — findings dropped or reworded, each with the user's reason; or "all findings approved as-is"). Recording the Approval outcomes line means a decision made at audit time doesn't vanish — without it, the only trace of a dropped or reworded finding is its absence.
- **Plan / setup:** `**Queue changes:**` (work processed, reordered, or modified — for a setup session, the first rough build item and the docs scaffolded) and `**Work processed:**` (kept / deleted, with slugs, or "none").

The approval frame, identical for every flavor: show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. If this run shipped only this one item, this approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see Commit core above and the one-text identity). If the run shipped several items, the commit message is instead a one-line summary of the whole run, drafted and approved at the commit step — each item's entry here still stands on its own. This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

Reuse the pre-generated candidate where one exists: if _build.md carries a matching `Index entry candidate` for the item and it built/ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim; if scope shifted, author fresh against the same rule. Planning sessions have no pre-generated candidate — author the index entry fresh against the Index entries rule.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

Each LOG entry is written as its own file under `LOG/`, **date-prefixed** so the folder sorts newest-first on a name sort — never appended to a shared log file. Every entry filename starts with `<YYYY-MM-DD>-` (the session's date):

- **Session closing work items with slugs** (build, audit): name each entry file `LOG/<YYYY-MM-DD>-<slug>.md` (e.g. `LOG/2026-06-09-drop-log-per-release-split.md`). A run that built several work items writes one entry file per item, each named after that item's slug — all sharing the session date.
- **Session with no work-item slug** (planning, setup, standalone handmade-work): name it `LOG/<YYYY-MM-DD>-<type>.md` (e.g. `LOG/2026-06-09-plan.md`, `LOG/2026-06-09-handmade.md`) — date first, so it sorts alongside the slug-named entries rather than clumping under the type word.
- **Name already taken** (a re-run work item, a second planning session the same day): append `-2`, `-3`, and so on (e.g. `LOG/2026-06-09-plan-2.md`).
- The matching `LOG/index.md` line ends with the entry's filename, so a later lookup goes straight from the index line to the file.

The date prefix is the entry's session date, not the commit date — write it from the current date at close. Its only job is a newest-first name sort; it is not a second copy of the hash (the hash still lives only in the heading and index line, per below).

The hash lives in the entry file's heading and the index line, never in the filename — the commit hash doesn't exist yet when the file is written, which is why the `[HASH]` placeholder pattern exists (see Commit core below).

One authoring rule: entry prose never writes the literal placeholder token — the token belongs only in hash position (the entry heading and the index line), where the automatic backfill treats any match mechanically. A prose mention is one find-replace away from corrupting the entry. When an entry needs to describe the placeholder mechanism, say it indirectly ("the placeholder", "the unfilled hash").

Entries from before the per-entry split live in `LOG/log.md` and `LOG/log-v*.md`. Those files stay in place, untouched — their entries are found by hash or title search, not by filename.

**Captures filed after the commit.** A capture sometimes comes up in the session's post-commit tail, after the LOG entry's "Routed to Captures:" line is already written and committed saying "none" or listing only what existed then. When that happens, the same move that appends the capture to QUEUE.md also updates this session's just-written entry — edit its "Routed to Captures:" line to include the new capture, as a working-tree edit with no separate commit. The edit rides into the next session's commit, exactly as the hash backfill does. The why: the entry is the session's record, and a capture belongs to the session it came up in, so the entry should converge to the truth of what that session produced. (The committed copy keeps the as-of-commit wording; the entry file — the canonical record — carries the correction, and git shows it landing in the next commit.)

## Checks the closing session couldn't run

The `## Deferred tests` section is retired — there is no separate test queue. The work-item model handles an unrun check directly: a verification only the user can run is a `[user]` work item, and /plan would have set it as its own item for /next to walk the user through; a check Claude can run is just part of building.

So the only thing /done does with a check it couldn't run is the ordinary capture move: if the closing session discovers a needed verification that isn't already a `[user]` item — one that needs the user, a device, or a reinstall before it can run — file it as a `[user]` work item appended to Unprocessed, drafting and showing the wording per plugin-behaviour.md Captures. A later /plan sorts it like any other captured work. Nothing tracks it in a dedicated section, and no LOG-only prose stands in for the queue line — an unrun check recorded only in a log entry never surfaces again.

## Recording a cleared red flag

Stated once here; every sub-doc's LOG-entry step points at this section.

A red flag is cleared at processing — the /plan moment its line is judged ready (plugin-behaviour.md Flag states). When a flag was cleared this session, record how in the session's LOG entry: either how the risk was **designed out or fixed**, or — if the user was told a security, privacy, or breach risk plainly and chose to proceed — the **informed-consent trail** (what they were warned about, and that they chose to proceed). The LOG is where the how-it-cleared lives; the marker on the work item only carries `State: cleared` (plugin-behaviour.md Red flags), not a dedicated section. Recording is unconditional once a flag clears — the record never rides only in chat or on the marker, because no later session re-reads those for clearing history. Nothing to record when no flag was cleared this session.

## Red-flag lifecycle at close

Stated once here; the sub-doc close-outs point at this section when the closing line carries a red-flag marker.

A red-flag marker never leaves the queue silently and never lingers as a workless standalone item (plugin-behaviour.md Red flags, Lifecycle). By the time a red-flagged item reaches a build or audit close, its flag was already cleared at processing — so the close does not re-decide it. It does two things:

1. **Carry the cleared flag into this item's LOG entry** — note the item carried a red flag and that it was cleared. The substantive how-it-cleared record was written at the /plan close that cleared it (Recording a cleared red flag); this is the lightweight carry-through, so the flag never leaves the queue unrecorded.
2. **Backstop** [PROMPT]: if the closing item's marker still reads `State: uncleared` — which should be impossible, since an uncleared flag never reaches Processed — stop and surface it rather than committing. An uncleared flag at a ship close means the model was bypassed; don't let the item leave the queue until the risk is cleared or the item is returned to Unprocessed.

Nothing to do when the closing item carries no red-flag marker.

## Wind-down re-scan (file-only) [BRIEF, PROMPT]

Stated once here; Commit core points at it, so it runs at every /done close regardless of session type.

Before committing, re-read this session's own discussion and surface candidate captures — things the user thought out loud but never explicitly flagged. This is the same safety net /plan runs at its wind-down, in a file-only form: /done may **file** the surfaced captures, but it does not **route** them (keep — move into Processed — or delete). Routing stays /plan-only, which keeps this on the allowed side of the no-planning-in-execution boundary — filing is capture-making, allowed in any session; routing is planning, /plan's alone (see plugin-behaviour.md Routing and discipline). Frame it to the user as capture-making, exactly like the post-close capture step: surface, file the approved ones to Captures with no routing, and leave them for a later /plan to sort.

Present all surfaced candidates as ONE numbered set of fully-drafted captures for a single approval (the bulk-approval inversion in plugin-behaviour.md's [SEQUENCE] rule): the user contests by number, and only contested items then go one at a time. Append the approved ones to Unprocessed — each as its own `####` work item per the filing format in plugin-behaviour.md Captures — and add them to this session's LOG entry's "Routed to Captures:" line as a working-tree edit that rides this commit (the same mechanism as a capture filed after the commit, above).

Name the step's best-effort nature in plain words when it runs — it re-reads whatever discussion is still in view, so a surfaced-nothing result is "nothing jumped out in what I could still see," not a guarantee nothing was missed. Two things to state, not fix: a fresh-chat /done has none of the session's thinking in view, so there is nothing to re-scan — only capturing-as-you-go covers that case; and when /plan already ran its own wind-down re-scan this session, this is a harmless no-op — re-reading the same discussion surfaces the same items, already filed. Exemplar of the no-op: "Re-read our discussion — nothing came up that isn't already captured."

## Session-file cleanup (throwaway artifacts) [BRIEF, PROMPT]

Stated once here; Commit core points at it, so it runs at every /done close regardless of session type.

The working files _build.md and _plan.md are deleted by the close already. This step generalises that lifecycle to *other* throwaway files this session created — a scratch script, a one-off intermediate the build wrote into the project, a temporary artifact with no future use. (Prevention comes first: temp files should have gone to the scratchpad directory and never reached the project — see plugin-behaviour.md, Temporary files and session artifacts. This close-time step catches the ones that landed in the project anyway.)

Offer to delete only files that meet **all** of these:
- **Claude created or wrote them this session** — established from _build.md Changes (where one existed) and this session's own edits. A file Claude did not create this session is **never** presumed rubbish: uncommitted changes the session didn't make are the user's own expected work (plugin-behaviour.md, the don't-panic reading), so they are left alone, not offered for deletion.
- **They have no future use** — not a deliverable, not a research finding, not evidence a later session must re-read (those have proper homes per the triage in plugin-behaviour.md). Purely throwaway.

How the offer runs:
- **One at a time, user approves each** [PROMPT] — never auto-delete. Name the file and why it looks throwaway, and wait for a yes before removing it. If nothing session-created looks throwaway, say so in one line and move on.
- **Warn by recoverability.** A git-tracked file is recoverable from history, so its deletion is low-stakes — say so plainly. An untracked file, or one outside the repo, is **not** recoverable once deleted — give a clear warning before removing it, so the user approves knowing it's permanent.

## Commit core [BRIEF, PROMPT]

Stated once here; every sub-doc's Commit step points at this section.

**Run the wind-down re-scan (the section above) before staging** — it files any un-flagged captures from this session's discussion so they land in this same commit. File-only: it never routes them. Skip nothing; on a fresh chat with no discussion in view it correctly finds nothing.

**Run the session-file cleanup (the section above) before staging too** — offer to remove this session's throwaway files, one at a time with the user approving each, so any deletions the user accepts fold into this same commit. It only ever offers files Claude created this session with no future use, and never auto-deletes.

**Shipped-slug cross-check (work-item closes).** Before staging, when this session shipped one or more work items, cross-check each shipped work-item slug named in this session's LOG entries against QUEUE.md's Processed section and confirm it has been removed. A work item is normally removed from Processed when /next locks its scope, so the slug should already be gone — this step is the safety net that confirms it. If a shipped slug is still sitting in Processed as active work, surface it in one line and remove it (or halt and ask) before committing. The why: a multi-item close removes many items in a loop with no mechanical check that each actually left the queue — a prior multi-item run shipped fourteen work items but left one in QUEUE.md, genuinely built yet never removed, so it re-presented the next session as unbuilt and wasted the first move rediscovering it was done. Trivial for a single-item close, where the one slug is self-evidently gone; the net earns its place on multi-item and unattended closes. A planning close names no shipped work-item slug, so there is nothing to cross-check. Output stays silent unless a stray slug is found.

1. Stage explicitly — name each path: files this session changed (from _build.md Changes where one existed), method docs updated during the session or close-out (QUEUE.md, SPEC.md, LOG/), and the _build.md deletion where one was removed.
2. Detect out-of-scope dirty paths: run `git status --porcelain` and compare what it lists against the active build's file list (from _build.md, where one existed). Any dirty path outside that list is a user edit made between or during sessions that no build staged.

   **Recognise the hash-backfill signature first, and skip the investigation for it.** A dirty LOG path — `LOG/index.md` or a `LOG/<slug>.md` entry file — whose only change is a placeholder hash becoming a real commit hash, in an entry heading or the start of an index line, is the session-start hook's automatic backfill. The hook runs that backfill every session after a /done and announces it in its opening housekeeping line, so a dirty LOG path matching it is already accounted for — don't open a git diff to investigate it and don't explain it file-by-file. Fold it into this commit with at most a one-line note ("folding in the previous session's hash backfill"). The why: this exact dirt appears every single session and the answer is always "it's the backfill, stage it," so re-investigating it each time is pure delay for zero decision value.

   For any other out-of-scope dirty path, keep the full treatment: surface it in a one-line summary and offer to stage it into this commit, investigating where the change isn't self-evident. The reason: otherwise these edits sit dirty across sessions until the push ritual's sweep catches them — this is the earlier catch point, not a replacement for that safety net.
3. The commit message is not drafted fresh — it derives from the LOG entry (or entries) already approved at this session's entry step, and its shape follows how many work items this session shipped:
   - **One work item shipped** (and the planning/setup closes, which have their single entry): the message *is* that entry (see LOG entry files below for the one-text identity), in two positions — **Title:** the index line's one-liner, verbatim; **Body:** the approved rationale prose, verbatim. Both were approved when the user approved the LOG entry, so the commit step reviews nothing new. Present it by stating that identity plainly — "the commit title is the entry's summary line and the body is the approved rationale, both already approved above."
   - **Several work items shipped** (a multi-item /next run): each item kept its own LOG entry (done-build.md 2.1), so no single entry is the whole message. **Title:** a one-line summary of what the run shipped across all its items; **Body:** each shipped item's one-liner, one per line. This roll-up is genuinely new text — the per-item entries were each approved, but their summary was not — so draft it and show it for approval before committing.
   Never write a meta-description of the derivation (e.g. "the rationale as approved, plus an appended line naming the backfill…"); a meta-description reads as a third text the user has to check, which defeats the nothing-new-to-read point.
   - **Allowance for staged extras:** when the commit stages work beyond the session story — hash backfills, staleness-sweep edits, rolled-in user edits (step 2 above) — the body appends one line naming them. In the single-item case that appended line is the only genuinely-new text, so it is the one thing the presentation surfaces; in the multi-item case it rides alongside the summary.
4. No pre-commit ask — the commit always happens at /done, and its message is the LOG entry already approved at the entry step, so there is nothing new to confirm before committing. Only the push is genuinely optional. So: commit first (the safe, local action), then gate the outward push on consent. After committing, run one `git remote` check — with a remote, offer push as a plain yes/no ("Committed. Also push to the remote?"); with no remote, say it's committed and offer no push (a push would error with nowhere to send). This matches the file-safety rule: do the safe local thing, ask before the outward one. A sub-doc may override to fit its session shape — done-plan.md commits and doesn't offer push — but the commit-first mechanics here stay canonical.
5. Pass the message shell-agnostically. Write it to a file in **the session's scratchpad directory** — the temporary working folder the harness gives this session, outside the project — and commit with `git commit -F <scratchpad path>/COMMIT_MSG.tmp`. One mechanism on every machine, and it sidesteps inline-quoting fragility, which is the reason a file is used at all rather than `-m`: a multiline body passed inline is brittle to generate, because embedded newlines vary by shell and a PowerShell here-string requires its closing token at column 0, so a body that is correct on one machine can be mangled on another.

   **The scratchpad rather than the project root, and this correction matters because the old instruction was wrong about the hook, not merely untidy.** This doc previously said to write the file into the project root, on the stated grounds that the scope-lock is not active there once `_build.md` has been deleted. That reasoning does not hold against `pre_tool_use.py`, which both docsets run underneath. The file scope-lock is indeed inactive with no active build — but the same hook then applies its planning-session file gate, and a write to a path outside the small set a session touches by design (the queue, SPEC, the log, the session's own working notes) returns **ask**. So the instruction as written produced a permission prompt at every close, on a step that has nothing for the user to decide, at the very end of a session — which is precisely where an unexplained prompt costs most, because the user has no way to tell a routine mechanism from something going wrong.

   The scratchpad is the correct home on its own merits, independently of the prompt: the behaviour rules already route every temporary file the project does not keep to that directory, the hook treats it as always-editable so no prompt arises, and the folder clears itself, so there is no deletion step to remember and no stray file left in the working tree for a later session to puzzle over. Nothing about the message itself changes — only where it is written on its way to `git commit -F`.
6. Commit with `git commit -F`. The commit needs no fresh okay — its message was approved at the entry step. Then offer push only when a remote exists (per step 4), and push only if the user accepts.

The LOG entry keeps its `[HASH]` placeholder. The session-start hook backfills it automatically at the next session, as a working-tree edit that folds into that session's commit — no amend, no two-commit flow.

## Recommend next [BRIEF, PROMPT]

Stated once here; every sub-doc's final "recommend next" step points at this section, adding only its flavor delta.

**Plain-language guard.** Narrate the queue situation in everyday words — never the background section-bookkeeping phrasing. Keep the plain statement accurate: don't say the queue is clear when work is still waiting to be sorted.

**Overlap scan (shared).** Before recommending, scan the still-unprocessed work for overlap with the top processed item — work that contradicts, invalidates, or would benefit it if sorted first. State the scan's result either way, not only when it blocks: nothing unprocessed → say nothing's waiting for /plan; unprocessed work waiting but none overlaps the next item → name what's waiting and give the plain verdict that nothing blocks it; overlap found → recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three items are waiting to be sorted; none touches the next piece of work, so nothing blocks it," never "there may be overlap worth checking."

**Queue-state ladder (shared).** When nothing blocks, recommend by queue state:
1. Captures appended this session that affect the next work → recommend /plan, name the blocker.
2. Processed work exists → name the next item, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
3. Processed empty → "Queue is clear. Run /plan when you have more."

**File the forward-recommendation advisory (shared).** When this step made a concrete recommendation — naming what to plan or build next and why — file it per plugin-behaviour.md Forward-recommendation advisory: a capture at the top of Unprocessed, worded as advice, consumed and cleared by the next /plan. When the recommendation is generic ("run /plan when you have more"), no advisory is filed.

Flavor deltas:
- **Build close:** the shared ladder above is the whole recommendation.
- **Audit close:** findings appended this session sit unprocessed, so the default recommendation is /plan, to sort them into work — name the count. Only when nothing was appended does the overlap scan run and the ladder apply (ladder steps 2–3).
- **Plan / setup close:** a fresh setup session whose only work item is the rough first build item recommends /plan to scope it, **never /next** — the interview wrote that item deliberately unscoped, so it isn't ready to build. Otherwise the shared overlap scan + ladder apply.

## Rules

- Do NOT skip the sub-doc's judgment steps even if the user says "just commit."
- Routing is automatic. Don't ask — check for _build.md.
