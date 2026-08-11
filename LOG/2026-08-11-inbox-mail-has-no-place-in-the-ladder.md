# 08c885b — /plan's Step 1 gained the guaranteed moment waiting INBOX mail is opened

Captured by the user, whose words were that INBOX should be somewhere on the ladder and that items in the inbox should be ranked into the most-unblocking flow and simply processed like captures. The design is Claude's, agreed by the user.

**The gap, stated precisely.** `session_start` surfaced waiting mail in one line, and `feedback-and-inbox.md` said opening a message routes it through the three-way triage and then archives the file. **No doc said when a message gets opened.** /plan's Step 1 read QUEUE.md, SPEC.md and the advisory and never mentioned the mailbox, so mail could be surfaced every session and opened in none of them.

**The build.** At /plan's Step 1 read-state, if the mailbox holds waiting messages, fetch `feedback-and-inbox.md` — naming the fetch explicitly, since that doc is loaded on demand and its stated trigger is exactly this — open each message, route it, and archive the file. Placed **before** the droppable skim and the ordering ask, so anything it produces is ordinary Unprocessed work by the time the session orders itself.

**No new ladder rung, which was the user's instinct and is the cheap outcome.** Once a message is opened its contents are ordinary captures and rank by the existing ladder with nothing added. The missing step was the opening, not the ranking. A rung would have had to define how a raw, unread message competes with designed work before anyone knows what is in it.

**Who may open mail.** Any session, whenever the user asks — opening and routing is filing, and filing is open to every session, while deciding an item's fate stays /plan's. What Step 1 adds is a *guarantee*, which is the thing that was missing.

**Mid-session arrival is left unsolved deliberately.** A message landing mid-session waits for the next session start, because that is when the mailbox is scanned. The INBOX design already promises no delivery guarantee, so the honest move is to state the bound rather than build a watcher for it. Recorded in all three places a reader might look.

**Files touched:**
- `plugin/si-plugin/docs-b/plan.md` — new "Open any waiting INBOX mail" block in Step 1.
- `plugin/si-plugin/docs-b/feedback-and-inbox.md` — Inbound section gained "When mail is opened", the no-priority-rung statement and the mid-session bound.
- `SPEC.md` — the Cross-project INBOX paragraph now says when mail is read.
- `FAQ/faq.md`, `FAQ/index.md` — new entry, "Another project sent me a message. When does Claude actually read it?"

**Routed to Captures:** none.

FAQ: updated — new entry "Another project sent me a message. When does Claude actually read it?"
