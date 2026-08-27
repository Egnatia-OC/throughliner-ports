# [HASH] — Sessions read the date from a fact line instead of assuming it

Sessions were deriving today's date by assumption and writing wrong ones into
records, captures and holds. The user reported it recurring across sessions
rather than as a one-off, which is what decided the shape of the fix: correcting
the two wrong dates would have left the next session deriving the next wrong one.

The failure is invisible downstream, and that is why it needed machinery rather
than care. A wrong date reads exactly like a right one — nothing later can tell
them apart, and a date is what holds work back, releases it, and orders the
queue's decay rungs.

So two halves. `session_start.py` now emits the date read from the system clock,
worded as the date **at session start** rather than "today" — a long chat can
cross midnight, and an anchor that silently goes a day stale while still reading
as current would be worse than none. And an always-loaded rule tells sessions to
read a computed field where one exists and the clock where none does.

**The rule was authored as an amendment rather than freestanding**, which is what
kept it from costing a slot. Its parent is the Research-and-evidence trigger —
"what would answer this?" — whose whole subject is taking an answer from a route
rather than from your own confidence. A date is that rule's sharpest case, so it
reads as one more limb of it. Nothing was evicted: the parent keeps every limb it
had.

**Files touched:** `plugin/throughliner/hooks/session_start.py` (the fact line,
emitted after the SPEC/QUEUE lines); `plugin/throughliner/docs/skill-nonspecific-rules.md`
(the rule, as a bold-led paragraph); `resources/testing/test_session_start_date_anchor.py`
(new, four cases, driving the hook as a subprocess against a fixture project
because the line is emitted in main() rather than by a helper).

Verified: the suite passes, and SPEC's session_start sentence — written at the
planning session ahead of this build — already matched the shipped behaviour.

**Routed to Captures:** none.

Rule gate: run — the always-loaded rule was authored at this build from the decision step's disposition; it amends the Research-and-evidence "what would answer this?" trigger rather than standing free, and nothing is evicted for it.
