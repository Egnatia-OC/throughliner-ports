# [HASH] — Red-flag lifecycle at ship: a flag must ride real work, and its resolve/accept is forced and recorded at close

Built the red-flag lifecycle-at-ship rule, folding in two captures that were halves of one question — what happens to a red flag when its work-line finishes. One half caught a flag lingering as a standalone workless line; the other caught a flag vanishing unrecorded when its line shipped. Both break the redesign's model, where a red-flag marker only ever rides a line carrying real work.

The rule: a red-flag marker must always sit on a line with real remaining work — never a pinned tracking line, never a silent disappearance. At the close of any line carrying a marker, the close forces an explicit resolve-or-accept decision and records it in the LOG before the line leaves the queue. A completed fix flips to **resolved** immediately (the code no longer carries the risk); if a live check is still needed, it rides an ordinary `[user]` verification line, not a lingering open flag. Wired in three places: the rule in plugin-behaviour.md (Red flags → Lifecycle at ship), a shared "Red-flag lifecycle at close" section in done.md, and a step in done-build.md's Phase 1 routing a red-flag-carrying built line through it. A consumer FAQ entry covers the close behaviour.

Immediate cleanup folded in: [device-access-consent] — whose fix shipped 2026-06-18, live verification riding [merged-plugin-live-verification] — flipped to **resolved** and its standalone line removed from the queue. [consumer-plugin-feedback-channel]'s flag, which had vanished unrecorded at its close (the exact failure this rule prevents), was backfilled to **resolved** in its own LOG entry (report scrubbed by construction + the user's review before any external paste). A sweep confirmed no other red-flag work lines remain in the queue.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — new "Lifecycle at ship" subsection under Red flags
- plugin/si-plugin/docs/done.md — new "Red-flag lifecycle at close" shared section
- plugin/si-plugin/docs/done-build.md — new step 1.4 routing to it
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line
- QUEUE.md — [device-access-consent] standalone red-flag line removed
- LOG/consumer-plugin-feedback-channel.md — backfilled the missing red-flag resolution record

**Routed to Captures:** none
