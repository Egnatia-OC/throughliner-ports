# c904687 — done-build.md reply-to-mail step — trigger narrowed from message-changed-work to message-asked-a-question

The reply obligation was narrowed to question-asking messages under [inbound-replies-not-drafted], and done-build.md's step 1.5 still fired on "a message that changed work here" — the broad trigger the amendment evicted elsewhere ([done-build-reply-trigger-stale]). The step now reads: a message that asked a question is owed a drafted reply; a defect report is owed nothing by default. Straight alignment with the already-decided narrowing, no new decision.

Tick: done, confirmed (grep: "changed work here" gone; wording matches feedback-and-inbox.md's triage).

Rule gate: run — transcription of an amendment already admitted under [inbound-replies-not-drafted]; nothing new authored.
FAQ: not needed because replies were already drafted at the close; only the trigger wording aligned.

**Files touched:** plugin/throughliner/docs/done-build.md
**Routed to Captures:** none
