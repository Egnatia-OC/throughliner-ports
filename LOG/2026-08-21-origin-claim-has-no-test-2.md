# [HASH] — The provenance split gains the test that asserts what it is for

The queue lint flags a QUOTE claim ("your words", "in her own words") showing no quoted text, and deliberately never flags an ORIGIN claim ("captured by you"). Every test covered the flagging side; nothing asserted the not-flagging side, which is the whole of the split.

Two cases added. A bare origin claim with nothing quoted anywhere goes unflagged, across three phrasings. A quote claim with no verbatim text is still flagged, so narrowing the phrase list has not narrowed it to nothing.

The acceptance said reverting the split should make the first case fail. That was executed rather than asserted: with the origin phrases folded back into `QUOTE_CLAIM_PHRASES`, the same item flags. So the test is a test of the split rather than of the lint in general.

Why the split matters, recorded in the test's own docstring: everything in these documents is written by Claude, so demanding a quotation for an origin claim would move every un-transcribed idea of the user's into Claude's column — and the cheapest way to satisfy such a rule is to ask the user to prove their own work is theirs.

**Files touched:** resources/testing/test_queue_lint_flags.py
**Routed to Captures:** none
Rule gate: not needed — tests only; the provenance split itself is untouched.
