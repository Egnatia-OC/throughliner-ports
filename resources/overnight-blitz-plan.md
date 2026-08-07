# Overnight autonomous queue blitz

> Reusable plan. First run 2026-08-05 (branch `overnight-blitz-2026-08-05`),
> second run the same night (branch `overnight-blitz-2026-08-05b`). What both
> runs learned is folded into the phases below — there is no separate learnings
> section to cross-read. Amend the phases in place after each future run.

## Context

Alex wants an unattended overnight run: clear the queue's cleared-to-run region, generate any captures needed of the blitz's own, build the safe subset of those, and leave the contentious ones for her /plan tomorrow. The work lands on a branch that is a perfect copy of current state, easy to test and merge (or discard) in the morning. The night ends with a test rezip installed so she can trial the new build on app restart.

## Structure: branch in place, not a worktree

Work happens on a new branch **`overnight-blitz-<date>`** (a `b` suffix if it's the night's second run) checked out in the main working tree — not a separate worktree. Reason: the local plugin marketplace registration points at this folder's path, so the end-of-night rezip snapshots whatever is checked out *here*. A worktree elsewhere would need the marketplace re-pointed (a config change to her setup) to be testable. A branch in place keeps rezip working and makes merge trivial (`git merge overnight-blitz-<date>` from main).

**Before branching:** commit any leftover uncommitted files on **main** first — the session-start hook flags them, and they are a prior session's finished work. This keeps the branch diff purely blitz work, so rejecting the branch tomorrow loses nothing of hers.

## Sanctioned departures from the method (recorded in the LOG per the override rule)

The behaviour rules require per-item approval, one-item-at-a-time delivery, and reserve processing for /plan with the user present. An overnight run can't wait on approvals, so these run in an autonomous mode **Alex is authorizing here**, recorded as a departure in each LOG entry:

1. **Approvals deferred.** Captures, LOG entries, and commits proceed without live approval; everything is reviewable in the branch diff and the LOG tomorrow.
2. **Autonomous processing under a softened bar (Alex's rule, set at plan approval).** The blitz may process and build **any** Unprocessed capture — pre-existing or blitz-generated — that is *practically already designed* (the build is describable, files are known, no open fork) **or** whose presented choices are a *strawman* (one option is obviously right and the alternatives exist only to be rejected). **`[audit]` items are explicitly cleared under this bar** (confirmed after the first run): an audit reads and reports, edits nothing, and its findings wait for approval anyway — the safest possible blitz work, so run every reachable one by default. Genuine design forks, user-owned decisions, and anything red-flagged-uncleared stay for her /plan. Reducing the queue's length is an explicit goal of the run.
3. **No push, no release, overnight.** Routine push and the mechanical release trigger are suspended for this run: everything stays local on the branch. Publishing unreviewed autonomous work to the public repo overnight contradicts the branch's provisional framing (and outward publication needs per-action approval anyway). The release check fires normally at the first /done after she merges.

## Hard boundaries (never touched overnight)

- **[history-rewrite-third-party-scrub]** — force-push rewrite; explicitly must never be reached unattended.
- Any **[user]** item — walk-throughs need her live.
- Any item with an **uncleared red flag**. A *cleared* red flag is not a boundary — that item builds.
- Any item the queue itself says is spent, superseded, or in need of reprocessing.
- Unprocessed items carrying a **genuine design fork or user-owned decision** — processed only if they meet the softened bar above; otherwise left with a one-line triage note.
- **Taskflowapp** — read-only always.
- **No push, no GitHub release, no Discord, nothing outward-facing.**
- The orphan tag range `v17`–`v157` — never deleted (standing rule).

## Run mechanics (learned across the first two runs — apply throughout)

These are cheap to follow and each one cost real time when it was learned:

- **Page every large read to completion.** Large-file reads come back capped in the desktop app; the first run's own opening queue read was truncated and needed explicit paging. A triage from a partial read silently sees a different queue and reads as complete. Read QUEUE.md whole, every time, before triaging (relates to the [queue-chunked-read-fail-closed-unlanded] capture).
- **Name standing lint noise once, at the start.** A pre-existing advisory flag fired on every queue edit all night. Note it in the first narration and ignore it thereafter, so real flags stay visible.
- **Reach for `resources/testing/reorder_queue.py` before scripting.** It has `--move-section`, relative `--move`, `--position`, and `--marker-after`. Script only what the mover genuinely can't do (bulk removals at scope-lock remain the one scripted case).
- **`--move-section` into Processed lands at the BOTTOM — below the readiness line.** An item moved into Processed because it passed the bar needs `--position`, or a follow-up `--marker-after` reorder, or the file reads as though nothing was cleared.
- **Run bulk mechanical passes before drafting targeted edits to the same files.** A corpus-wide find-replace changed text that a later prepared edit exact-matched on, and the edit failed mid-run. Bulk first — or re-grep the exact string immediately before each targeted edit.
- **Delete `_build.md` before writing the commit-message file.** The scope-lock correctly denies `COMMIT_MSG.tmp` while a build is active; the close's delete-then-commit order is load-bearing, not cosmetic. That denial is the hooks working — don't read it as a fault.
- **Run `hook_schema_check.py` only after committing**, never between entry-writing and commit. It drives the real `session_start`, which performs the commit-hash backfill as a side effect — benign after a commit, corrupting if it fires while `[HASH]` placeholders are still meant to be pending.

## Phase 1 — Run the cleared region (via the method's own /next → /done cycle)

Run every item above the `--- Cleared to run above this line ---` marker, top-down, following `docs-b/next.md` / `next-build.md` / `next-audit.md` / `done*.md` (docset B), with proper `_build.md` scope-locking, per-run LOG entries, FAQ-disposition lines, and commits on the branch. Take the items as the queue lists them — no re-litigating a cleared item's design overnight.

Two things to carry from the first run's cleared region, because they recur:

- **A cleared item can contain a step that is out of bounds anyway.** The worktree fix was cleared, but deleting the remote half (`origin/queue-redesign`) is a remote-state change — done locally, deferred to Alex, and named in the LOG. Do the in-bounds part, defer the rest explicitly, never silently.
- **An audit's findings land where the work already lives.** The FAQ audit's findings were appended to the existing [faq-backfill] item's rationale rather than filed as a new capture, leaving that item below the line for Alex's patch-vs-rebuild call. Findings feed the item that owns the work; a contentious recommendation still waits for her.

## Phase 2 — Triage the existing Unprocessed section + generate new captures

**Triage every pre-existing Unprocessed item** against the softened bar, reading the whole file first (see Run mechanics). What the first two runs found the shapes to be:

- **Passes:** doc fixes whose wording is already settled; script extensions whose shape is already stated; small named fixes whose direction is already decided; every `[audit]`.
- **Holds:** `[user]` items, genuine design forks, anything where the item states a problem but not a fix, and anything red-flagged uncleared.

Every held item gets a one-line triage note **in the blitz-close LOG entry** saying why — not in the morning handoff message, which scrolls away. The committed entry hands the next /plan its triage pre-done and durable.

**Generate new captures** via systematic sweeps, filed as proper captures in Unprocessed. **There is no capture target, and deliberately no number here.** Two runs swept honestly and found 5, then 2, against an original "~10–15" — the docs were simply healthier than assumed, and a number reads as a quota no matter what qualifier sits beside it. Never manufacture findings to look productive; a clean sweep is the finding. The run's success measure is the queue getting *shorter*, not more captures filed.

Sweeps: **the systematic consistency sweeps have one home now — the soak-end differential audit** (`resources/consistency-audit-plan.md`), which runs over the whole branch just before the merge and covers what the three sweep bullets that used to sit here covered (compliance checklist, cross-doc consistency greps, hook code read) with a fuller pass list. Running them on blitz night too would double the work and produce findings the night's own later builds immediately stale. The blitz's capture generation is what its builds and triage surface in course, not a standing sweep.

## Phase 3 — Build everything that passes the bar

Process-and-build any capture (existing or new) meeting the softened bar: practically designed, or strawman-choice-only. Additional holds regardless of design completeness:

- Privacy/security dimension or any red flag → held for her.
- Outward-facing output (Discord text, PR replies, GitHub issues) → held.
- Hook *behaviour* changes where the fix isn't already fully stated in the item → held.
- **A ready-looking fix that lives *inside* a bigger undesigned item → held, whole.** Building the fragment can't remove the item, so it leaves the docs changed and the queue item still standing, now describing a problem that is half-fixed — drift by construction, and the opposite of a shorter queue. Name the ready fragment in the closing advisory instead, so Alex's /plan can lift it deliberately. (Hit live on the second run's stale-viewer mitigation.)

No hard cap on build count — a shorter queue is the goal — but each build runs through the /next → /done cycle with its own scope-lock, LOG entry, and commit, so the branch stays reviewable item by item.

## Phase 4 — Test rezip (ritual as written, minus nothing)

1. Bump `-testN` suffix in `plugin/si-plugin/.claude-plugin/plugin.json` (never the release line).
2. Delete `__pycache__` folders under `plugin/si-plugin/`.
3. Prune the plugin cache to current + 3 most recent.
4. CLI check by full path (`~/.local/bin/claude.exe --version` vs app; update CLI first if behind), then `claude.exe plugin update sovereign-implementer@flintcraft` — snapshots the branch's checked-out state, which is exactly what she's testing.
5. Run `python resources/testing/hook_schema_check.py` (shape check). The delivery check ("what actually arrived in context") cannot run tonight — it needs the restart — so it is handed to the next session rather than to Alex's memory; see the delivery check below.
6. **Record the expected host version everywhere the next session will look.** Write the exact `-testN` string just installed (e.g. `1.19.0-test1`) into the blitz-close LOG entry *and* the forward advisory, as a literal to compare against. This is the artifact the delivery check compares to; without it the next session has nothing to check against and the question collapses into "does this look right?", which invites a plausible reconstruction instead of an observation.

## The delivery check — the next /plan runs it, not Alex

**Alex always runs /plan after a blitz.** So the delivery check belongs at the opening of that session, as something it does, not as something she has to remember. Framed as her job in the morning it rolled forward across two blitzes unrun — the same failure the status-line probe hit, and the same fix: **don't wait for someone to catch the moment; put the check where the next run cannot miss it.**

So the blitz's forward advisory and closing message both state it as an instruction to the *next session*, in these terms:

```
the next /plan opens by:
    quoting its own session-start lines VERBATIM     # what arrived, not a
                                                     # summary of what arrived
    comparing the reported host version against the
      -testN string recorded in the blitz-close entry
    saying plainly which it found
```

**It is a comparison, never a self-assessment.** The session is matching one string against a recorded one — the compare-never-explain shape — so there is nothing for it to reconstruct. Never word it as "confirm the state lines look right": a session that received nothing can rebuild plausible-looking lines from CLAUDE.md, and that reconstruction is indistinguishable from success. Ask what arrived.

**A mismatch is a finding, stated plainly and not worked around.** An older version means the restart did not take — on Windows a normal quit can leave the process running — and the run is testing the wrong build. This has already happened once: a restart silently left 1.18.0 live while 1.19.0 sat installed, and nothing noticed until the next advisory chased it. Say which version was found, name the likely cause, and offer the full quit-and-relaunch before the session goes further.

Worked on 2026-08-06: the /plan following the blitz opened by reporting host `1.19.0-test1`, matching the recorded string, and the delivery question was answered in the session's first message without Alex doing anything.

## Phase 5 — Close and handoff

**Closing is /done, run at the end of each run and again at the end of the night — logging happens there, not along the way.** Each /next-style run finishes with its own /done close: that close is where the LOG entries are written (one per built item, per the method), where captures ride into the record, and where the run's commit lands. The night's final close is a /done too, producing the blitz-close LOG entry below. Nothing waits for the morning to be logged — by the time Alex reads the branch, every run is already recorded and committed exactly as an attended session's would be.

- **Save this plan for reuse:** commit a copy as `resources/overnight-blitz-plan.md` on the branch (host-only dev artifact), so a future blitz can rerun it without re-deriving the structure and departures.
- Final /done-family close on the branch: LOG entry for the blitz's tail, forward advisory at the top of Unprocessed orienting tomorrow's /plan.
- Handoff (in the final LOG entry + final chat message): what was built (by slug), what captures were generated, which were auto-built vs held and why, the departures exercised, the branch instructions below, and the reminder: **fully quit and relaunch the app** to load the test build.
- **The soak ends with the differential audit, and the audit is what "earned trust" means.** Before the merge is offered, run the differential consistency audit (`resources/consistency-audit-plan.md`) over the whole branch — blitz plus soak in one span — and clear its repair captures through one /plan + /next. The full cycle: branch → blitz builds → soak → differential audit → reconcile → merge → branch again. A merge offered before the audit has run and reconciled is the gamble, not the default.
- **Recommend a soak, not an immediate merge.** The branch's whole point is that Alex can run on the blitzed state for a day or two — the test build is snapshotted from the branch, so daily sessions exercise the new behaviour with main untouched — before deciding. So the handoff and the forward advisory present **soak first** as the default: stay on the branch, work normally, and merge (`git checkout main && git merge overnight-blitz-<date>`) once it has earned trust, or revert (checkout main, re-run the plugin update to re-snapshot main, restart) if it hasn't. Merge-on-morning-one remains available but is named as the gamble it is, never the recommendation — the first run's advisory pushed straight to merge and that was wrong as general practice. One honest caveat to state in the handoff: work done during the soak lands on the branch, so a late revert discards the soak days' work too — the decision gate covers blitz-plus-soak together, and the longer the soak runs well, the more the decision has already made itself.

## Verification

- Every commit lands on the branch; `git log main..overnight-blitz-<date>` is the complete reviewable delta.
- Queue lint (post_tool_use) advisories heeded after every QUEUE.md edit.
- `hook_schema_check.py` passes before the night ends.
- Nothing pushed: `git status` shows branch ahead of nothing remote; no `gh release` calls made.
- Delivery check: carried by the next /plan, not by Alex's memory — it quotes its own session-start lines verbatim and compares the host version against the `-testN` string recorded in the blitz-close entry (see "The delivery check" above). The blitz's own job is only to *record the expected string* and *state the instruction* in the advisory; the checking happens in the session that has the evidence.
- **Any check the blitz cannot finish tonight follows the same rule: leave the next session an instruction and something to compare against, never a reminder for Alex.** Two checks have now rolled forward across multiple blitzes because they were written as moments to catch — the delivery check, and the status-line probe. A check that depends on someone remembering is a check that does not happen.
