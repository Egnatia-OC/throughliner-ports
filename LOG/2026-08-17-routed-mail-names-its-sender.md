# [HASH] — a routed message names its sender in a committed document, against a rule that already forbids it

Found while sending a reply, and worked immediately on the user's instruction rather than deferred.

The address-book rule is write-and-send only: a session may pass a recorded path to a send, and may never name a correspondent in any document. Three queue items filed from mail named the sending project in their prose, and those items are committed.

Claude's first reading was that the rule was over-broad, because the message convention requires a sender to identify itself, so routing appeared to compel the breach. The user's correction defeated it: the mailbox is gitignored. So a sender naming itself inside a mailbox is safe, and the only exposure is a session copying a name out of the mailbox into a document that does get committed — which is exactly the move the rule names, and exactly what had happened. The rule stands; the practice broke it.

The fix is therefore at the routing step rather than in the rule: a capture or LOG entry made from a message describes its source generically, the same rewrite-at-the-same-usefulness the scrub checklist already asks for. Nothing is lost, since an item's reasoning never depends on which project sent it.

Two residuals are stated rather than fixed. Committed LOG entries cannot be rewritten, and one slug carries the name and is immutable by rule and already in git history — renaming it would move the name out of a live path and leave it in history, the trade already refused over the docs-b rename.

Every mention still in QUEUE.md was reworded generically in this session.

Rule gate: run — admitted as a clause on the existing inbound routing step. Nothing evicted; the address-book rule stands unchanged, which was the disputed point.

**Queue changes:** [routed-mail-names-its-sender] filed, processed and cleared in the same session; QUEUE.md prose reworded throughout.
**Work processed:** kept — [routed-mail-names-its-sender].
