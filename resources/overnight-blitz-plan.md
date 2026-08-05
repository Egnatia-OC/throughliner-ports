# Overnight autonomous queue blitz

## Context

Alex wants an unattended overnight run: clear the queue's cleared-to-run region, generate roughly 2–3x more captures of the blitz's own, build the safe subset of those, and leave the contentious ones for her /plan tomorrow. The work lands on a branch that is a perfect copy of current state, easy to test and merge (or discard) in the morning. The night ends with a test rezip installed so she can trial the new build on app restart.

## Structure: branch in place, not a worktree

Work happens on a new branch **`overnight-blitz-2026-08-05`** checked out in the main working tree — not a separate worktree. Reason: the local plugin marketplace registration points at this folder's path, so the end-of-night rezip snapshots whatever is checked out *here*. A worktree elsewhere would need the marketplace re-pointed (a config change to her setup) to be testable. A branch in place keeps rezip working and makes merge trivial (`git merge overnight-blitz-2026-08-05` from main).

**Before branching:** commit the four leftover files from the previous session (`LOG/2026-08-05-plan.md`, `LOG/index.md`, `QUEUE.md`, `resources/research/codex-port-postmortem.md`) on **main** first — they are a prior session's finished work that the session-start hook already flagged for pickup. This keeps the branch diff purely blitz work, so rejecting the branch tomorrow loses nothing of hers.

## Sanctioned departures from the method (recorded in the LOG per the override rule)

The behaviour rules require per-item approval, one-item-at-a-time delivery, and reserve processing for /plan with the user present. An overnight run can't wait on approvals, so these run in an autonomous mode **Alex is authorizing here**, recorded as a departure in each LOG entry:

1. **Approvals deferred.** Captures, LOG entries, and commits proceed without live approval; everything is reviewable in the branch diff and the LOG tomorrow.
2. **Autonomous processing under a softened bar (Alex's rule, set at plan approval).** The blitz may process and build **any** Unprocessed capture — pre-existing or blitz-generated — that is *practically already designed* (the build is describable, files are known, no open fork) **or** whose presented choices are a *strawman* (one option is obviously right and the alternatives exist only to be rejected). Genuine design forks, user-owned decisions, and anything red-flagged-uncleared stay for her /plan. Reducing the queue's length is an explicit goal of the run.
3. **No push, no release, overnight.** Routine push and the mechanical release trigger are suspended for this run: everything stays local on the branch. Publishing unreviewed autonomous work to the public repo overnight contradicts the branch's provisional framing (and outward publication needs per-action approval anyway). The release check fires normally at the first /done after she merges.

## Hard boundaries (never touched overnight)

- **[history-rewrite-third-party-scrub]** — force-push rewrite; explicitly must never be reached unattended.
- Any **[user]** item — walk-throughs need her live.
- Any item with an **uncleared red flag** ([private-info-rule-scope-rewrite]'s flag is cleared, so it builds).
- **[release-docset-b-work]** — queue itself says it's largely spent and needs reprocessing.
- Unprocessed items carrying a **genuine design fork or user-owned decision** — processed only if they meet the softened bar above; otherwise left with a one-line triage note.
- **Taskflowapp** — read-only always.
- **No push, no GitHub release, no Discord, nothing outward-facing.**
- The orphan tag range `v17`–`v157` — never deleted (standing rule).

## Phase 1 — Run the cleared region (5 items, via the method's own /next → /done cycle)

Follow `docs-b/next.md` / `next-build.md` / `next-audit.md` / `done*.md` procedures (docset B), with proper `_build.md` scope-locking, per-run LOG entries, FAQ-disposition lines, and commits on the branch:

1. **[agents-md-undocumented-duplicate]** — reduce AGENTS.md to a pointer at CLAUDE.md; add it to the file map.
2. **[claude-md-worktree-claim-wrong-and-stale-trees]** — fix the wrong worktree claim in CLAUDE.md; `git worktree remove` the merged queue-redesign tree (safety check already recorded: `git log main..queue-redesign` is empty); record the worktree list in the file map. **Exception:** deleting `origin/queue-redesign` (the remote half) is deferred to Alex — it's a remote-state change and in scope for the history-rewrite's branch-coverage decision; noted in the LOG instead.
3. **[private-info-rule-scope-rewrite]** — retitle the private-info section in `docs-b/plugin-behaviour.md`, add the solicitation clause and the self-disclosure rephrase clause; touch `docs-b/plan.md`, `docs-b/next.md` as listed; FAQ entry. Docs-b only (A frozen).
4. **[setup-creates-unnamed-public-exposures]** — extend `docs-b/setup.md` Step 3b: read `git config user.email`, name the noreply option, state plainly what the planning record exposes; FAQ entry; SPEC.md if user-visible behaviour changes.
5. **[faq-audit-wrong-missing-and-shape]** — the audit: reads only, edits nothing; findings land as one consolidated set into [faq-backfill]'s scope (its rationale block gets the findings appended, staying in Unprocessed/below-line for her call on patch-vs-rebuild — that recommendation is contentious by design and left for her).

## Phase 2 — Triage the existing Unprocessed section + generate new captures (target ~10–15 new)

**Triage every pre-existing Unprocessed item** against the softened bar. Likely process-and-build candidates on a first read (final call at triage, per item): [claude-md-orphan-tags-understate-what-they-hold] (a two-sentence doc fix), [advisory-filed-after-commit-unnecessarily] (fix already scoped: move the write before the commit), [unscoped-advisory-fires-once-ever] (small named fix, fail-open direction already settled), [reorder-mover-demands-full-slug-set] and [no-mechanical-mover-for-cross-section-moves] (script extensions with the shape already stated), [codex-port-handoff-debt-audit] (an [audit] — run it, findings become captures), [retired-plan-closeout-still-produced] (the design note already picks the fix: retire the heading, add the term to background vocabulary). Likely holds: the [user] items, [concurrent-session-support], [session-sizing-and-break-lines], [throughline-*] design items, the docset-A freeze-meaning pair, [scope-file-editable-vs-locked], [shell-writes-bypass-file-scope-lock] — genuine forks. Every held item gets a one-line triage note in the morning handoff (not written into the queue) saying why.

**Generate new captures** via systematic sweeps, filed as proper captures in Unprocessed:

- **Method compliance sweep** over `docs-b/` using `resources/method-compliance-audit-checklist.md` (authoring compliance, response-shape tag placement, narration drift).
- **Cross-doc consistency greps**: retired terms (push marker, batch types, `Completion mode`), stale cross-references, hook-enforced literals vs docs, template-vs-procedure drift.
- **Hook code read**: `session_start.py`, `pre_tool_use.py`, `post_tool_use.py` for defects of the kind already found (fail-open holes, once-ever markers).

## Phase 3 — Build everything that passes the bar

Process-and-build any capture (existing or new) meeting the softened bar: practically designed, or strawman-choice-only. Additional holds regardless of design completeness:

- Privacy/security dimension or any red flag → held for her.
- Outward-facing output (Discord text, PR replies, GitHub issues) → held.
- Hook *behaviour* changes where the fix isn't already fully stated in the item → held.

No hard cap on build count — clearing the queue is the goal — but each build runs through the /next → /done cycle with its own scope-lock, LOG entry, and commit, so the branch stays reviewable item by item.

## Phase 4 — Test rezip (ritual as written, minus nothing)

1. Bump `-testN` suffix in `plugin/si-plugin/.claude-plugin/plugin.json` (never the release line).
2. Delete `__pycache__` folders under `plugin/si-plugin/`.
3. Prune the plugin cache to current + 3 most recent.
4. CLI check by full path (`~/.local/bin/claude.exe --version` vs app; update CLI first if behind), then `claude.exe plugin update sovereign-implementer@flintcraft` — snapshots the branch's checked-out state, which is exactly what she's testing.
5. Run `python resources/testing/hook_schema_check.py` (shape check). The delivery check ("what actually arrived in context") is hers in the first session tomorrow — stated in the handoff.

## Phase 5 — Close and handoff

- **Save this plan for reuse:** commit a copy as `resources/overnight-blitz-plan.md` on the branch (host-only dev artifact), so a future blitz can rerun it without re-deriving the structure and departures.
- Final /done-family close on the branch: LOG entry for the blitz's tail, forward advisory at the top of Unprocessed orienting tomorrow's /plan.
- Handoff (in the final LOG entry + final chat message): what was built (by slug), what captures were generated, which were auto-built vs held and why, the departures exercised, merge instructions (`git checkout main && git merge overnight-blitz-2026-08-05`), reject instructions (checkout main, re-run `claude.exe plugin update` to re-snapshot main, restart app), and the reminder: **fully quit and relaunch the app** to load the test build.

## Verification

- Every commit lands on the branch; `git log main..overnight-blitz-2026-08-05` is the complete reviewable delta.
- Queue lint (post_tool_use) advisories heeded after every QUEUE.md edit.
- `hook_schema_check.py` passes before the night ends.
- Nothing pushed: `git status` shows branch ahead of nothing remote; no `gh release` calls made.
- Morning test: Alex restarts the app, first session confirms the docs-b directive and state lines actually arrived in context.
