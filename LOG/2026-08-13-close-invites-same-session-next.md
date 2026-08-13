# 340e7ef — The close stops inviting a build in the same session, and learns the readiness marker

`done.md`'s rung 2 no longer asks whether the user is continuing into another
/next now. It names the next item as information and says a build wants a fresh
session, with no command string ending the message. `next-build.md`'s completion
step stops ending on "run /done" for the same reason. Rung 3 loses its literal
command too, for consistency.

The user was tricked by the chip at the end of a close: it contained `/next`, and
she hit tab and enter thinking it was an affirmative on something the close had
just said. A message that ends by asking a question whose answer looks like a
command is one keystroke from being run by accident.

The precedent is near-exact and went the other way round. `plan.md` used to recite
four routes after every processed item, naming /done among them; it was removed
because an offer naming closing, delivered just after finishing a piece of work,
reads as an announcement that closing is what happens next — and a user acted on
that reading. The fix there was to stop naming the command, not to reword it,
which is why rewording rung 2 was not enough here.

The substance is the user's decision, recorded as such rather than dressed up as
a pre-existing fact: /next is not for running in the same session — you clear or
start a new chat first. It is well grounded, since a run inheriting a full build
and its close is the opposite of the fresh short session the method is built for.

A new rung 2b was folded in from a deleted capture: rung 2 keyed only on
"Processed work exists", which cannot tell work /next can run from work needing
/plan to clear it, so a close that had just emptied the cleared region still
pointed at /next — straight into `next.md`'s nothing-cleared soft stop, costing a
round trip. `plan.md`'s mid-session routes line was deliberately left untouched;
it fires at the start of processing, not after finished work.

Rule gate: run — admitted as amendments to the ladder and the completion step.
Live instance recorded above.

FAQ: updated — added "Why can't I just start the next build in the same
conversation?"

SPEC and README were synced at the close as a scope grow the user approved — the
/plan close that decided this had caught only the mail item, so four user-facing
changes from this run had reached neither document.

**Files touched:** `plugin/si-plugin/docs-b/done.md`,
`plugin/si-plugin/docs-b/next-build.md`, `FAQ/faq.md`, `FAQ/index.md`,
`SPEC.md`, `README.md`
**Routed to Captures:** none
