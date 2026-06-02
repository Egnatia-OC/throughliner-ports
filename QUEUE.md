# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Captures

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [question] Claude asked "reorder?" at end of summary, but reordering is Claude's responsibility — need full enquiry into when and where the plugin empowers Claude to own dependency management (per SPEC: "helps the user harness Claude's skills in dependency management")
- [build] Remove "design decisions" as a separate category everywhere — everything is a decision. The LOG should always record WHY things were implemented (reasons given by user or by Claude and approved). Reasons made explicit at planning time must also be preserved. The current framing causes important information to be lost and never recorded.
- [idea] Sizing gates in plan.md need future planning work — current rules may not be right
- [build] Find all instances of "open questions" and "questions" across plugin docs and rename to "captures" where applicable — "open questions" is a retired name for captures
- [question] Why is /plan showing a full summary of the batches queue at all? Everything in batches already went through /plan discussion to get there. The summary appeared when Captures was empty — is the procedure defaulting to "present queue state" when there's nothing to process? What should /plan actually do when Captures is empty?
- [build] /done Phase 3 handoff should not present options — Claude should evaluate the queue state (do any Captures block the next batch?) and make a single recommendation, not ask the user to figure it out
- [build] /next pre-flight presentation (Step 1.4) should not show raw type markers ([build], [test]) — group items under Build and Test headers instead. Type markers are for Claude's processing, not user-facing display.
- [build] /next Step 1.4 prompt should not offer "adjust scope / pick a different entry" — Claude owns dependency management and batch ordering. The presentation is the recommendation; the prompt should just be "Ready?" not a menu that invites the user to second-guess the sequencing.
- [build] /done Step 1.2 test generation is a blanket rule that doesn't distinguish code from docs. For procedure doc edits, the batch's own [test] entry already verifies correctness — /done tests just produce trivial "does line exist" checks. Step 1.2 should scope test generation to code/app changes, not all file changes.

### Parked
