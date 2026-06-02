# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Drop file lists from batches**
Files:
- `plugin/si-plugin/docs/plan.md`
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- `plugin/si-plugin/templates/faq-template.md`
- `plugin/si-plugin/templates/faq-index-template.md`
- [build] Remove Files: list from batch format in plan.md Step 5 — entries name their own targets
- [build] Rewrite next.md scope enforcement: remove "only touch files on the list" rule, replace with "stay within the work described by the entries — if you need to touch something unrelated, say so first"
- [build] Update _build.md structure in next.md Step 2: remove Files section, keep Progress and Changes
- [build] Update done.md staging references to use _build.md Changes section instead of file list
- [build] Update FAQ templates: remove/rewrite the "what happens if Claude needs to edit a file outside scope" Q&A
- [build] Strip Files: lists from all existing batches in QUEUE.md
- [test] Read plan.md, next.md, and done.md to confirm no remaining references to batch file lists

**/plan Captures flow: define thresholds and fill gaps**
Files:
- `plugin/si-plugin/docs/plan.md`
- `plugin/si-plugin/docs/behaviour.md`
- [build] Define the pipeline threshold in behaviour.md: "if a user would see or experience the difference, it changes the product — update SPEC.md first"
- [build] Add "already decided (found in LOG/index.md)" as an explicit drop reason in plan.md Step 3
- [build] Specify whether new batch placement needs user approval or Claude places using ordering logic and reports
- [build] Add instruction to state the item count before processing Captures ("3 items in Captures. First: ...")
- [build] Specify what the Captures section looks like after all items are processed (empty section with Parked subsection intact)
- [test] Walk through the Captures flow with the updated plan.md and confirm all five fixes are clear

**Scope and staging clarity: cross-reference /next and /done**
Files:
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- [build] Clarify in next.md that REGISTRY.md is not in build scope — /done Step 1.5 handles all registry updates after the build
- [build] Clean up done.md staging list (Step 2.4) to explain why QUEUE.md is included: /next already modified it, not /done
- [build] Add cross-references between /next Step 2 (batch moves to _build.md) and /done Step 2.3 (deletes _build.md) so the batch lifecycle is traceable across both docs
- [test] Read next.md and done.md end-to-end and confirm the handoff between them is unambiguous

**Procedure doc cleanup sweep**
Files:
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- `plugin/si-plugin/docs/behaviour.md`
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
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
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
