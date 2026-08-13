# [HASH] — Outbound mail checks the recipient has a mailbox, and the docs stop implying delivery means arrival

Two complementary changes to `feedback-and-inbox.md`'s outbound section, kept
together rather than treated as alternatives. Before writing, check the
recipient's `INBOX/` exists and say plainly when one has to be created — the exact
failure the item was filed about, where a project whose installed method predates
INBOX scaffolding has nothing at its session start that surfaces waiting mail, so
the message sits unread indefinitely with nothing on this side knowing. And state
the guarantee honestly: sending places a file in the recipient's mailbox, and
nothing confirms it was read.

The completed round trip of 2026-08-10 bounds the worry without removing it. That
message was read, answered, and a date error corrected at its source — but it
worked because the other project happened to read its mailbox and chose to reply.
A good outcome, not a guarantee, and the docs must not let it read as one.

**The read-receipt option is rejected on a stronger ground than the
traffic-doubling the item argued, and the text records it so it is not
re-proposed.** Nothing leaves the machine without the user seeing the exact text
and giving an explicit yes, and that rule names outbound INBOX messages. An
automatic receipt is an automatic send: it would either break that guarantee
outright or stop to ask the user to approve a receipt for a message they never
wrote — worse than the problem it solves.

The pre-write check is largely writing down existing practice rather than
inventing a mechanism: a careful session already confirms the folder exists, and
one did so before delivering a message earlier the same day.

Two stale references in the item were corrected at processing, either of which
would have sent a build wrong: `plugin-behaviour.md` no longer exists, and the
live home is `docs-b/feedback-and-inbox.md`; and the pointer at
`[inbox-mail-has-no-place-in-the-ladder]` was spent, since that has shipped.

`SPEC.md` was checked at build time and judged to need nothing, since it already
said delivery is not guaranteed. That was revisited at the close and reversed:
the pre-write mailbox check and the explicit statement of what sending
guarantees are both user-facing, so SPEC and README were synced as an approved
scope grow.

FAQ: updated — added "I sent a message to another one of my projects. How do I
know it arrived?"

**Files touched:** `plugin/si-plugin/docs-b/feedback-and-inbox.md`, `FAQ/faq.md`,
`FAQ/index.md`
**Routed to Captures:** none
