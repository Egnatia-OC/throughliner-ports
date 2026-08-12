# [HASH] — The /plan-side wind-down re-scan was already gone, so what shipped was the removal of a dead reference to it and a do-not-reintroduce

This item asked for a subtraction: remove the wind-down re-scan from `plan.md`, and remove the now-dead "when /plan already ran its own, this is a no-op" clause from `done.md`. **The first half was already done.** Grepping `plan.md` for both "wind-down" and "re-scan" returns a single line, and that line already says /done runs the re-scan at every close whatever the session type. There is no step there to remove.

That is recorded plainly rather than logged as work performed, because a build that reports a subtraction it did not make leaves the next reader believing a file changed when it did not.

What genuinely remained was the dead clause in `done.md`, which pointed at a step that no longer exists. It is gone, and in its place is a positive statement: this is the method's only wind-down re-scan, there is no second one to coordinate with, and it is not to be reintroduced. The diagnosis rides with it, because it is the part worth carrying forward — the beat was defined by a *position*, "after every item is processed", and a session that processes in batches at the user's direction never reaches that position, so the step attached itself to the nearest thing that felt like a pause and ran three times in one session, twice at a moment no document names. Each run is a stop-and-ask, so an invented cadence spends the user's turns on a beat they did not ask for and cannot predict.

The item's own instruction to check whether the close's version does everything the /plan-side one did could not be run as written, since there is no /plan-side version left to compare against. Noted rather than silently skipped.

The fresh-chat clause beside it — a /done in a new chat has none of the session's thinking in view, so there is nothing to re-scan — is still true and untouched.

**Files touched:** `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none

**Rule gate:** not needed — a dead cross-reference removed and replaced with a statement of the status quo. No rule authored.
