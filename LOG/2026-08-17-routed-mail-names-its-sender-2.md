# 7e3c1c8 — a capture made from a message describes its source generically

One clause on `feedback-and-inbox.md`'s inbound routing step: a capture or LOG entry made from a message describes its source generically — "a consumer project running this method" — rather than naming it.

The address book is write-and-send only. A session may pass a recorded path to a send and may never name a correspondent in any document, and the mailbox is gitignored, so the leak was never the mailbox. It was a session reading a name out of it and copying it into `QUEUE.md`, which is committed. Three queue items filed from mail had done exactly that.

Claude's first reading was wrong and the user corrected it. The argument had been that the rule was over-broad, since the message convention requires a sender to identify itself, so routing appeared to compel the breach. Her correction: INBOX is supposed to be gitignored, so a sender naming itself inside a mailbox is safe, and only the copy into a committed document is not. The rule stands; the practice broke it.

Nothing is lost by the rewrite — an item's reasoning never depends on which project sent it — and it is the same rewrite-at-the-same-usefulness the scrub checklist already requires.

One residual stands rather than being fixed: a committed LOG entry cannot be rewritten, and one slug carries the name and is immutable by rule. Renaming it would move the name out of a live path and leave it in history, the trade already refused over the `docs-b/` rename.

Rule gate: run — a clause on the existing routing step. Nothing evicted; the address-book rule stands unchanged, which was the disputed point.

**Files touched:** `plugin/throughliner/docs-b/feedback-and-inbox.md`
**Routed to Captures:** none
