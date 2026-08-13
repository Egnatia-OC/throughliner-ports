# [HASH] — An address book inside INBOX/, so a reply doesn't need the path re-supplied

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
**Routed to Captures:** none
