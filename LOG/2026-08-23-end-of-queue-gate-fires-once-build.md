# [HASH] — The end-of-queue gate asks once per rest, not on every return to it

Raised by the user from live experience minutes before it was filed: the close-or-continue question re-fired three times in one sitting, and reads as naggy for someone working slowly through a planning session. The gate was designed when nobody had ever reached an empty queue — her queues ran sixty items deep until Fable-only development began the day before — so its repetition had never been observable.

The gate keeps its job and drops the repetition. Its original point stands and is untouched: an empty queue is a resting state, and the session must not presume it is over. What changed is the return edge. The neutral question is asked once, when the queue first comes to rest; on later returns to rest within the same stretch the session ends plainly with no re-ask, and the question fires again only after further work has emptied the queue again. The bound is held in the conversation, which is all a per-stretch bound needs — a stored flag was refused for that reason.

Removing the gate outright was also refused: its precondition guard, that it may never fire while unprocessed work remains, is load-bearing and stays.

**Files touched:** `plugin/throughliner/docs/plan.md` — the once-per-rest bound stated at the gate, the return edge reworded to match, and the last-item off-ramps paragraph pointed at the bound as the gate's first firing.

**Routed to Captures:** [spec-owes-close-amend-and-gate-once] — SPEC's processing-flow paragraph says when the wrap-up question is available and not how often it may fire.

Tick: done, confirmed — plan.md states the bound at the gate, the return edge agrees with it, and a grep found no other doc asserting the repeat behaviour.

Rule gate: run — amendment to plan.md's end-of-queue gate, parent named; the return edge is reworded rather than a rule added, and nothing was evicted. The recorded instance is the three firings the user reported.

FAQ: not needed because the change removes a repeated question and no user action changes.
