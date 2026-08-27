# 32675a3 — Captures gain a bow-out: `Blocked by:` now works in both sections

`Blocked by:` belonged to the held region alone. That left an unprocessed capture
with no way to wait on something already in the queue: it returned to the top
every planning session and was set aside again, and the only alternative — a
`Not before:` date — guesses at a wait the queue could simply check.

So the field now means one thing on a work item and another on a capture, written
as the same per-section split `Not before:` already uses: do not BUILD this until
every named item resolves, versus do not OFFER this again while any named item is
still open.

**On a capture it needs no approval, unlike a date**, and the asymmetry is the
reasoning rather than an inconsistency: a blocker is an entry anyone can look up,
so the capture returns by itself the moment that entry is processed or built. The
date form removes an item from view with nothing resolving, which is why that one
stays the user's call.

**The lint change is where the real risk sat.** It was skipping every Unprocessed
entry before it ever looked at a `Blocked by:` line, so the slug resolution and
the names-itself check were hoisted to run in both sections. On a work item a
broken reference is at least visible — the entry sits below the readiness line
where the placement checks look at it. On a capture there is no position to give
the mistake away: the entry would just stop being offered, silently, for good.
Only the build-order warning stays scoped to Processed, since that one reads build
order.

**Two things the item asked for turned out to be already true**, and were checked
rather than edited: the digest already prints each named blocker's resolved state
on a capture's line (verified against a fixture), and session_start's
blockers-in-Unprocessed count is undistorted, because it only reads blocker lines
inside held Processed items.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md` (line-format
comment, the per-section split block, and three sites that asserted the
held-region-alone clause); `plugin/throughliner/docs/plan.md` (a silent pass-over
beside the date one, rung 3's bow-out sentence, and a `Blocked by:` provision at
the skip step); `plugin/throughliner/hooks/post_tool_use.py`;
`resources/testing/test_capture_blocked_by_lint.py` (new, nine cases).

**Routed to Captures:** none.

Rule gate: run — supersession of the field-belongs-to-the-held-region-alone clause, for this one added meaning; the old rule loses because it left in-queue waits with no bow-out, which the refused skip-marker design never addressed. Amendment to the existing Blocked-by rules, nothing freestanding.
