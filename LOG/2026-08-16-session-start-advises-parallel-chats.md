# d82f538 — The isolation messages stop coaching on running two chats at once

The session-start hook printed, into the payload of every chat: *"The parallel-sessions advice for this case: two appends to different parts of QUEUE.md don't collide and the file-modified warning catches it if they do — but avoid two sessions writing QUEUE.md or committing at the same instant."* Advice for coordinating concurrent chats, addressed to a reader whose always-loaded rules now say a project is worked on from one chat at a time.

**A real cost rather than a stale sentence.** It rode in every chat, it named a rule that no longer exists, and it read as permission — a chat told how to coordinate with another chat has been told it may have one. Same shape as two always-loaded texts disagreeing with the session left to pick. The closing clause is the sharpest part: telling a session to avoid two chats writing at the same instant is telling it how to run the thing the rules forbid.

**Deletion was the wrong instinct, and reading all three arms is what showed it.** Two of them carry real information with no other home.

The **shared** arm is wholly stale. Every part of it coaches on coordinating two chats the user opened. A shared working tree with one chat needs no advice at all, so nothing replaces it beyond naming the isolation.

The **worktree** arm is mixed, and the split is the finding. "A capture filed in another session never reaches this one… keep queue edits in one session until a merge lands" is parallel-chat coaching and goes. "This session's work is NOT merged back automatically — the close says which branch it is on and warns that choosing remove at exit would delete it" is about a worktree **the harness created**, where nobody opened a second chat. It is the strand-prevention warning and survives.

The **clone** arm survives almost entirely, for a third reason: a cloud session is not a second chat running alongside another, it is the only chat running somewhere else. "Work reaches the main machine only as a pushed branch" is essential and has nothing to do with parallelism. Only the framing phrase was wrong.

**The through-line for the rewrite:** each message says what this session's isolation means for **its own work reaching the user's machine**, and says nothing about coordinating with another session.

**One expectation of the item did not materialise, recorded rather than read as a passing check.** It predicted the `resources/testing/` suite pinning the payload would fail until updated. No suite pins these strings, so nothing failed. That is a gap in coverage, not a clean result.

**A related instance surfaced the same day.** The user met an FAQ entry making the same claim in consumer-facing prose and reacted in her own words: it *"has NEVER successfully happened and EVERY time we have tried to ship that behaviour, it has fallen over."* That entry was dropped by [own-faq-diverged-from-shipped-template], and the README's version of it was corrected at this close.

Depth: full — the alternative weighed was deleting all three messages, refused because two carry information with no other home.

Rule gate: run — no rule authored. **The disposition is an eviction: one clause removed outright and one narrowed**, in text that contradicted an always-loaded rule. Failure evidence is the payload of the chat that built it, quoted verbatim, read after the restart that made the withdrawal live.

FAQ: not needed — this text is context the hook gives Claude, never shown to the user.

**Files touched:** `plugin/throughliner/hooks/session_start.py`.

**Routed to Captures:** none from this item.
