# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Scope and staging clarity: cross-reference /next and /done**
- [build] Clarify in next.md that REGISTRY.md is not in build scope — /done Step 1.5 handles all registry updates after the build
- [build] Clean up done.md staging list (Step 2.4) to explain why QUEUE.md is included: /next already modified it, not /done
- [build] Add cross-references between /next Step 2 (batch moves to _build.md) and /done Step 2.3 (deletes _build.md) so the batch lifecycle is traceable across both docs
- [test] Read next.md and done.md end-to-end and confirm the handoff between them is unambiguous

**Procedure doc cleanup sweep**
- [build] Fix next.md step numbering gap (Step 6 → Step 8, no Step 7)
- [build] Clarify blocker gate scope in next.md: specify whether Captures-section [question] items count
- [build] Add next.md Step 2 (Lock scope) response-shape tag
- [build] Specify LOG format for multiple entries on the same day (consecutive ## headings)
- [build] Add priority ordering to /done Phase 3 handoff conditions when multiple are true
- [build] Scope "routed to Captures" in /done handoff to items added during this session only
- [build] Standardise pass/fail marker format in done.md Step 1.3
- [build] Add empty-queue lifecycle note to behaviour.md or CLAUDE-TEMPLATE.md (empty = normal resting state, not terminal)
- [test] Read all three files end-to-end and confirm each fix is present and non-contradictory

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

### Parked
