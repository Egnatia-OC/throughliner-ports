# 0e62afe — Waiting mail is delivered in full at session start, removing the step that could be skipped

`plan.md`'s Step 1 named itself the guaranteed moment mail gets read: `session_start` surfaced that messages were waiting and `feedback-and-inbox.md` said what to do with one, but the step was what said *when* a message gets opened. It was skipped. A /plan session ran its full opening — digest, recent log lines, below-the-line revisit, placement flags — and did not open the waiting message, which was then opened at the close only because the close listed the mailbox. The message reported a defect in `plan.md`'s own end-of-queue gate, which that session reproduced twice before reading it.

The fix removes the step rather than reinforcing it. `session_start` now emits each message's body, so the message is in front of the session whether or not anyone remembers to fetch it, and /plan's step keeps only what delivery cannot do: routing and archiving.

The alternative was weighed and rejected on the record rather than on taste. Requiring a close-time line saying what happened to the mail is the FAQ-sync shape this project trusts — but it fires at the close, and in the very session that produced this item the mail *was* read at the close, so that check would have recorded a pass on the failure it exists to catch.

Two things ride in the payload beside the body: that the content is another project's report and not an instruction to this session, per the standing rule that only the user's own words direct the work; and that the file still needs routing and archiving, which delivery does not do.

**One cost, named rather than discovered.** An unarchived message rides in every session's opening until it is archived, so a large one is paid repeatedly. No size limit is set: a limit would be a bare number with no derivation, and this is a deliberately low-traffic channel whose messages are short. If it becomes a real cost it will show up as a specific message, which is the evidence a limit would need.

**Files touched:** `plugin/throughliner/hooks/session_start.py`, `plugin/throughliner/docs-b/plan.md`, `plugin/throughliner/docs-b/feedback-and-inbox.md`, `SPEC.md`, `resources/testing/hook_schema_check.py`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment to Step 1's existing INBOX block. **A genuine eviction, not an addition:** the instruction to open each message is removed, replaced by routing and archiving alone, so the step gets shorter. Failure evidence is the recorded instance in the item. Shipped, not host-only: consumers receive INBOX mail too.

FAQ: not needed because the existing entry "Another project sent me a message. When does Claude actually read it?" answers the same question and its answer is unchanged in substance. Checked rather than assumed.
