# 0e62afe — An outbound message carries a return path, and the doc's own refusal of that is superseded

A name says who wrote; only a path says where to write back. The shipped rule required the sender's name in the filename and the opening line and stopped there, so a recipient with the name and no path could not reply until the user looked the folder up by hand. Three replies stalled exactly there — two projects that reported real defects, and a third that reported one and had its proposed mechanism rejected for stated reasons, none of whom will hear so.

An outbound message now writes its own folder as a return path. The sender always knows where it lives, so nothing is looked up, nothing is scanned, and the path is user-supplied by construction since the sending project is the user's own.

**The build halted here, and the halt was wrong.** `feedback-and-inbox.md` carried an explicit prior refusal of exactly this, on the ground that it writes a path from this machine into another project's repository where it may be committed and may be public — a privacy reason the item's rationale never addressed, and one this project's own duty says must be surfaced rather than built past. The user answered it decisively: INBOX is gitignored, and the send already refuses unless the recipient's `INBOX/` is covered by that project's ignore rules. With that check in place the file is never committed and the refusal's premise no longer holds. She also observed that the two options offered were the same, which was fair — they differed by almost nothing and were dressed as a choice.

So the refusal is superseded in the doc rather than left standing beside the new rule, with the reason recorded: it predates the gitignore check, and it was costing real replies. The paragraph now also distinguishes the two mechanisms, which do different jobs and are both kept — the return path tells a recipient where a message came from, and the address book records where a correspondent lives on this side, which is what a *first* message needs.

**The backward half was deleted rather than built.** A `[user]` walkthrough for identifying the three stuck senders was written at processing from the method the user had improvised. It reached its first step — open your Claude Code session list — and stopped: she does not know how to find it. Her instruction: "delete this item. it doesn't matter who it was from. i'm sick of hearing about it." The three drafts stay preserved in earlier LOG entries and will not be sent. Only those three archived messages are unrecoverable; the channel itself is fixed going forward.

**Files touched:** `plugin/throughliner/docs-b/feedback-and-inbox.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** [walkthrough-step-user-cannot-perform]

Rule gate: run — admitted as an amendment to the shipped sender rule rather than a freestanding one; it extends an existing requirement from one field to two. Failure evidence is three undeliverable replies across two sessions. **Nothing is evicted**; one field is added to a message format, though one superseded paragraph is rewritten, which is a small net subtraction from the reasoning the doc carries.

FAQ: updated — new entry "What is a 'return path' on a message from another project, and what if one hasn't got one?"
