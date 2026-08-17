# dc52025 — a ladder rung can become live again, and the throughput floor goes stale the same way

The user raised this from the session in progress: having just agreed to file an audit that blocks a corrections build, she observed that the ordering rung should now move back **up**, and that this is not obvious.

The rule to re-check the rung at every pick already exists. What it does not say is that a rung can become live again — "re-check" reads as *has this rung run out yet*, a downward-only reading, because the ladder is written as a fall-through.

Testing it against the session corrected the instance without weakening the point. The two blockers filed in that moment went straight into Processed, so nothing in Unprocessed changed and the rung did not in fact move. That is recorded, because the item would otherwise send a build looking for the fault at the wrong site. Where it genuinely fires is the route the method requires: where a held item names a blocker not yet in the queue, the blocker is written into Unprocessed first, and that is a new entry other work cites.

A second effect the capture had not reached: the session's throughput floor is derived from how many blockers sit in Unprocessed, so filing one mid-session makes the number stated at the opening quietly untrue. Both go into one clause.

Rule gate: run — admitted as a clause on plan.md's existing re-check sentence; no freestanding rule and no always-loaded slot.

**Queue changes:** [rung-can-move-back-up] filed, processed and cleared in the same session.
**Work processed:** kept — [rung-can-move-back-up].
