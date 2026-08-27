# [HASH] — A release compares stamps before packaging, and "as planned" means read the record

Two halves of one failure: an instruction pointing at something written down was
resolved from memory instead of from the writing.

**The reading clause**, in the always-loaded Prior decisions rule. Where an
instruction points at a recorded plan by phrase — "as planned", "the way we
agreed", "like last time" — the record is read before acting. The phrase names
something that exists; resolving it from what seems likely substitutes a guess,
and the guess is indistinguishable from the real plan until the work is finished.
An amendment to a named parent, so it costs no slot.

**The stamp comparison**, ahead of packaging in the release ritual. It runs
`content_stamp()` over the target and compares it against the installed host's
stamp from the session opening. On a mismatch: one standalone warning turn saying
the release would ship code nobody has run, then proceeding only on the user's
word.

**Two sentences ride with it because the step is meaningless without them.** A
release releases a *tested rezip* — that is the invariant the step guards. And the
packaging reads the working tree exactly as it stands, with no reference to what
was last installed, so an edit landed since the tested rezip goes out silently
unless something compares. Stated as what the mechanism does rather than as a
warning about it.

**Blocking a mismatched release outright was refused.** Warn-don't-enforce
governs — built earlier in this same run — and the user may knowingly release the
working tree. Detecting "as planned" mechanically was refused too: it is a reading
discipline, and no hook parses intent.

**Files touched:** `resources/release-ritual.md` (new step 8, with the six later
steps renumbered); `plugin/throughliner/docs/skill-nonspecific-rules.md` (the
clause in Prior decisions).

**Routed to Captures:** none.

Rule gate: run — the reading clause is an amendment to the always-loaded Prior decisions rule, parent named, admission earned by this recorded failure; the stamp step is host-only ritual text, no method rule. Nothing evicted.
