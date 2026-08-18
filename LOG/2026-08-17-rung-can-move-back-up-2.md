# 7e3c1c8 — a rung can become live again, and the throughput floor goes stale with it

One clause on `plan.md`'s existing re-check-the-rung sentence: a rung can become live again rather than only run out, filing a blocker into Unprocessed is the move that does it, and the throughput floor is re-derived at the same moment.

The check already existed and fires at every pick. What it did not say is that "re-check" reads naturally as *has this rung run out yet* — a downward-only reading, since the ladder is written as a fall-through. Filing a blocker creates unblock-potential where there was none, which is rung 2 becoming live after the session has already fallen past it.

It matters in the ordinary case rather than an edge one: a planning session that files blockers is routine, and each time, the item that now blocks something else is the one worth processing next.

One correction to the case that prompted it, recorded so a later build does not go looking for a fault at the wrong site: the two blockers filed in that moment went straight into Processed, so nothing in Unprocessed changed and the rung did not in fact move. Where it genuinely fires is the route the method requires — a held item naming a blocker not yet in the queue, which is written into Unprocessed first.

The second effect the capture did not reach is folded in: the throughput floor derives from how many blockers sit in Unprocessed, so filing one leaves the number stated at the opening quietly untrue.

Rule gate: run — a clause on an existing sentence in a fetched doc; no always-loaded slot. Failure evidence is one instance, thin and admitted as such.

**Files touched:** `plugin/throughliner/docs-b/plan.md`
**Routed to Captures:** none
