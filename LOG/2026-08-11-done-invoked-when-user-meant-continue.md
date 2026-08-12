# 7c9922a — The /plan off-ramps are stated once at the start, and the per-item checkpoint drops the menu [done-invoked-when-user-meant-continue]

Captured by the user, observed live. Mid-session they ran /done and then said: "i didn't want to close, i just thought you were saying the session was over." No close was intended; the /done was a misreading of Claude's own message.

**What produced it.** The checkpoint ended each item by offering four routes, one of which was closing out. The wording was a neutral either/or — carry on, or close here — which the procedure asked for and which is not wrong in itself. But delivered at the end of a long message, after a completed piece of work, an offer that *names* closing reads as an announcement that closing is what happens next. The user acted on the reading, not the offer.

**Why it was worth fixing rather than filing as a one-off.** The checkpoint fires after every processed item, so this is one of the most-executed strings in the method — a misread there is paid repeatedly. And the failure is silent in the worst way: the user does not report confusion, they simply run the command and the session ends. This instance was recoverable only because they said afterwards what they had thought.

**Why this rather than rewording the offer**, which is the intuitive fix and is rejected. The defect is not the words but the *position and repetition*. Rewording a string that fires after every processed item leaves it firing after every processed item. Stating the routes once at the start of processing and presenting only the next item at each checkpoint means **closing is never named immediately after completed work** — the exact moment it misreads — and every checkpoint gets several lines shorter, which serves the length problem the user raised twice in the same session ("there's too much text and i can't tell what you want").

All four routes stay genuinely available. Only the recital goes.

**The cost, stated rather than discovered:** a user who forgets the options mid-session gets no reminder. Judged small — "stop" needs no teaching, and they can ask.

**The neutral end-of-queue gate is deliberately untouched.** The item's own warning was that the fix must not undo it, and it does not.

**Evidence, with its weakness named.** Unlike the items merged into [message-shape-rule-three-clauses], this one *is* testable here, since the off-ramps come from `plan.md` rather than the global instruction layers. In one /plan the checkpoint fired roughly fifteen times with no misread. That is real but weak — one user, one session, and a user primed by having made the mistake once. It is not the reason for the change; the recorded instance is.

A third site needed updating that the item did not name: the skip-to-defer paragraph described skipping as "one option among four", which would have pointed at a menu that no longer exists.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none from this item
