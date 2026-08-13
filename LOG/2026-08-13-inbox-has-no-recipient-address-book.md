# 340e7ef — An address book inside INBOX/, so a reply doesn't need the path re-supplied

`feedback-and-inbox.md`'s outbound section now describes
`INBOX/.address-book.md`, recording correspondent name to absolute folder path,
written the first time the user supplies a path so the cost is paid once per
correspondent rather than once per reply.

The user's words: our messaging procedure has no storage system for recipient
projects; once communication has been picked up it should be able to be continued
without the user having to retrieve the path again. The instance was minutes
earlier — a reply to Understudy was drafted and could not be sent, because nothing
anywhere recorded where Understudy is, after at least four exchanges. Inbound
needs no address; outbound needs a filesystem path, and the method never made one
durable.

It defeats a rule the method deliberately adopted: an unprompted reply draft that
then stops to ask for an address puts the friction exactly where the rule was
trying to remove it.

**The privacy concern was designed out rather than flagged, and the check the item
insisted on was actually run.** `.gitignore` line 5 is `INBOX/`, `git check-ignore`
confirms `INBOX/.address-book.md` is matched by it, and `git ls-files INBOX`
returns nothing. The item's precision is preserved in the doc text: the rule
ignores the folder and everything beneath it, so *inside* is protected and a
sibling file placed *beside* `INBOX/` is not. That dependency is written into the
text because it is load-bearing — a later change moving the file would lose the
protection silently. No red-flag marker, and that is recorded here so a later
reader does not think it was missed: the risk is real and cleared by design before
anything is written.

**The cheaper alternative — putting the sender's path inside the message — is
rejected on privacy rather than on the weakness the item named.** It writes a path
from this machine into another project's repository, which may be committed and
may be public. So the cheaper option carries the exposure and the more expensive
one does not; "it only helps future messages" is the lesser objection.

Never a filesystem scan: the book records what the user gave and never goes
looking for other projects, per the operate-on-the-folder-you-opened rule.

`setup.md` needs nothing — first-use creation, as the item's own default said,
rather than scaffolding.

FAQ: updated — covered in "I sent a message to another one of my projects. How do
I know it arrived?", which carries the address book and its gitignore protection.

SPEC and README were synced at the close as an approved scope grow.

**Files touched:** `plugin/si-plugin/docs-b/feedback-and-inbox.md`, `SPEC.md`,
`README.md`

---

## After the close — the address book's first real use, and the correspondence it carried

Written after `340e7ef` was committed and pushed.

**The feature was exercised within the hour of shipping, and it worked.** A
message from Understudy arrived; a reply was owed; the recipient's `INBOX/` was
checked and found to exist, so nothing had to be created; the reply was written
there after the user approved the exact wording. `INBOX/.address-book.md` was
then created with Understudy's folder recorded, and `git check-ignore` confirmed
the file is matched by `.gitignore`'s `INBOX/` line — the verification the doc
text says is load-bearing, run rather than assumed.

**What the correspondence produced, recorded here because it belongs to no built
item.** Understudy sent four testing outcomes from a /plan session, then a
follow-up. One was already fixed by this run — carried in
[plan-move-ritual-ignores-the-mover]'s own tail. Three became captures:
[no-field-for-ordering-preference], [queue-edit-echo-costs-context] and
[adopted-claude-md-describes-retired-structure]. Earlier the same day, three
further captures came from their two other messages:
[in-session-parking-has-no-home], [close-cost-depth-line-never-surfaces] and
[tick-conflates-built-and-confirmed].

**Their sharpest contribution refines an item rather than this one**, and is
recorded on it: the forward advisory carries ordering intent for one session
because it is cleared at every close, while a `Blocked by:` persists until its
blocker ships — so the advisory cannot carry "whenever these two get built, this
one goes first". That distinction is the test any new-field proposal must answer.

**Two observations about the channel itself, from using it rather than designing
it.**

The reply cost roughly 900 output tokens to send, having already cost the same to
show — because a message that leaves the machine must be shown before it is
written, so draft-then-send charges twice by construction. That is a second live
instance of [approval-flow-token-doubling-simplification], not a new finding.

And the exchange does not stop on its own. Our reply prompted theirs, and a reply
to that would have prompted another; the user noticed the loop before Claude did.
The always-loaded rule requires drafting a reply when an inbound message *changes
work here* — theirs did, by refining two captures — but "changes work" and "needs
an answer" are different tests, and only the second should trigger a send. The
thread was stopped on that reasoning. Not filed as work: it is one instance, and
the user was offered a capture rather than one being written unasked.
**Routed to Captures:** none
