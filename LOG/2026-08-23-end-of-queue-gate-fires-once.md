# 007a16c — Kept and cleared: the end-of-queue gate asks once per rest, not on every return

Her feedback from live experience: the close-or-continue question re-fired three times in one sitting and reads as naggy for someone working slowly in /plan — unobservable until now, because her queues ran sixty items deep until Fable-only development began the day before. The fix keeps the gate's job (an empty queue is a resting state, never presumed over) and changes only the return edge: ask once when the queue first comes to rest, stay quietly available on later returns, re-fire only when new work has emptied the queue again. Applied in-chat from the decision.

Rule gate: run — amendment to plan.md's end-of-queue gate (parent named); the return edge reworded, nothing evicted; the recorded instance is this session's three firings, user-reported.

**Queue changes:** new cleared build item.
**Work processed:** kept — [end-of-queue-gate-fires-once].
