# b485ee3 — The end-of-queue gate gains its precondition, and a named subset sets the order not the length

Filed by Claude from a live instance in a /plan session, caught by the user.

She named three items at the opening. When the third was processed, Unprocessed still held 35 items, and the session offered "anything else to capture or discuss, or shall we close out?" — `plan.md`'s **neutral end-of-queue gate**, specified for the case where Unprocessed *empties*. She had to ask why continuing was not offered.

The gap is a missing case rather than a misread one. `plan.md` states the four routes once at the start of processing and specifies the end-of-queue gate for an empty queue. Between those sat an unhandled state: a user-named subset exhausted while the queue is not. Nothing said what the session does there, so the nearest gate got reached for — and it names closing.

**Why that substitution is worse than a neutral miss.** The end-of-queue gate is carefully worded not to lean toward closing *given an empty queue*. Applied to a full one it stops being neutral: it silently reclassifies 35 unprocessed items as nothing left to do. That is the same failure the checkpoint recital was stripped back for.

**The fix is smaller than either option the item offered, because what to do next was already specified.** plan.md's checkpoint says that after every item you present the next item. Nothing was missing about the behaviour. What was missing is that the session took a subset the user *named* to be the length of the session. So: two clauses on statements that already exist. The neutral end-of-queue gate gains its precondition — it may fire only where Unprocessed holds nothing but items skipped this session — and the ordering ask at the opening gains one clause: a subset the user names sets the order, not the session's length. With the gate unavailable, the only thing left to reach for is the checkpoint, which is the correct behaviour.

Third instance of one family, with [close-invites-same-session-next] and [plan-gates-say-close-out-for-a-retired-phase], both shipped — a close offered where continuing was better.

**Files touched:** `plugin/throughliner/docs-b/plan.md` — the neutral end-of-queue gate and beat 2's ordering ask. SPEC.md is not listed: its processing-flow paragraph gained the matching sentence in the planning session that kept this. No FAQ entry: the user still answers one question there; only which question changes.

**Routed to Captures:** none.

Rule gate: run — both clauses are admitted as conditions on existing statements rather than freestanding rules, so no always-loaded slot is spent. **Nothing is evicted**, stated plainly. Failure evidence is three recorded instances of the same family.

Tick: done, confirmed by reading both clauses back in place.
