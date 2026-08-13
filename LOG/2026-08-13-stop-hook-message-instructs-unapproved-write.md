# [HASH] — The filing-claim hook states what it observed instead of instructing a write

`stop.py`'s block message dropped the imperative *"Make the write now if it is
missing"*. It keeps the observation, keeps the stakes sentence — they may already
be acting on the report — and keeps the escape for an item that genuinely lives
elsewhere. Claude then does whatever the rules in force require, which under
write-first is to make the write, reached by the current rules rather than by a
sentence frozen in a hook.

The conditional rewording lost. It keeps the hook deciding what should happen,
which means its text has to anticipate every presentation shape the method might
later adopt — and failing to anticipate one is precisely how this defect arose. A
hook is frozen text; the rules move. Today they agree, which is what makes this a
cheap moment to separate them rather than a reason to leave it.

The concern was carried out of a deleted parent item at the user's instruction
rather than folded into a note, and processing it was that instruction being
honoured. Claude's earlier read — that this was a standing consideration rather
than work — was rejected as a fate decision on an item the user had already
decided to keep.

No assertion in `resources/testing/` matched the removed sentence; all suites
pass unchanged.

**Files touched:** `plugin/si-plugin/hooks/stop.py`
**Routed to Captures:** none
