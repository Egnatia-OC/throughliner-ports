# b4de5bf — done.md stops instructing the close to clear the forward advisory

`done.md` told a closing session that the advisory is "read at the next /plan's opening to orient where that session starts, and cleared at that session's /done close (done-plan.md)". The clear was moved to the read itself; grepping `done-plan.md` for "advisory" returns nothing at all. So a shipped doc named a step in another shipped doc that does not exist.

It matters past a stale cross-reference. Immediately beneath that sentence sat a fenced `clear IF … / keep IF …` block — a decision procedure, which in `done.md` reads as an instruction to the closing session. A close was handed a rule for a step it does not own, so it would either look for a step that is not there or perform a clear that already happened at the opening. The second is silent, which is the worse branch.

The one thing the item said to check rather than assume was checked before deleting: `plan.md` carries the persist-condition branch itself, at its advisory step, in both limbs. So the block in `done.md` was a duplicate and removing it deletes no rule. Had it existed only here, the fix would have been to reword rather than cut.

The sentence now says the advisory is read and cleared at the next /plan's opening, names `plan.md`, and adds that clearing is not the close's job — which is the half that stops a session performing a clear that already happened.

This is an instance of a general shape rather than a new kind of fault: the clear step was moved and the doc that *described* it was not touched. Prose left behind when the mechanism it described was retired.

Rule gate: not needed — this corrects a doc's description of a step repealed elsewhere. No rule authored or amended; one stale instruction removed.

FAQ: not needed because the advisory's behaviour is unchanged and was already correct in practice; only the doc describing it was wrong.

**Files touched:** `plugin/throughliner/docs-b/done.md`.

**Routed to Captures:** none.
