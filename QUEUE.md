# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Test entry lifecycle: define mechanics and close gaps**
Files:
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`
- [build] Define what "executing a [test] entry" means in next.md: Claude runs every test it can verify itself (read code, run commands, inspect output); only tests requiring real user interaction go to the user; avoid visual-confirmation tests Claude could do by inspecting code/DOM
- [build] Add _build.md ticking format for test entries (not file-based — needs its own format showing pass/fail)
- [build] Add test-failure path to next.md: what happens when a test fails mid-build (route to Step 5 course-correction, or note and continue?)
- [build] Clarify relationship between batch [test] entries (executed during /next) and /done-generated tests (verification after build) in done.md
- [build] Add nudge to CLAUDE-TEMPLATE.md Project rules comment: mention users can put project-specific test procedures here or point to them from here
- [test] Walk through a hypothetical batch with mixed [build] and [test] entries and confirm the procedure is unambiguous at each step

**Response-shape tag rules: fill gaps in behaviour.md**
Files:
- `plugin/si-plugin/docs/behaviour.md`
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/plan.md`
- [build] Define default behaviour for unlabelled steps (e.g. "brief acknowledgment unless the step is purely internal, in which case no output")
- [build] Add tag precedence rule: step-level tags override phase-level tags when they conflict
- [build] Add hierarchy rule: procedure response-shape tags govern during skill execution; user communication preferences from CLAUDE.md apply to unlabelled steps and general conversation
- [build] Fix [BRIEF] tag conflicts: either retag steps whose content requirements exceed two sentences (next.md Step 1.4, plan.md Step 7, plan.md Step 2 queue-state presentation) or add a carve-out to the [BRIEF] definition — structured content (lists, option sets) doesn't count against the sentence limit
- [test] Re-read behaviour.md and all procedure docs to confirm tag rules are clear, non-contradictory, and cover all nine findings from the reader test (6 tag system + 3 BRIEF conflicts)

**FAQ reference: create templates and wire into /setup**
Files:
- `plugin/si-plugin/templates/faq-template.md`
- `plugin/si-plugin/templates/faq-index-template.md`
- `plugin/si-plugin/docs/setup.md`
- `plugin/si-plugin/hooks/session_start.py`
- `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`
- [build] Create faq.md template with 13 Q&A pairs from reader test (source: workflow output in reader-test-workflow.js results)
- [build] Create index.md template with thin question list, each pointing to the relevant section in faq.md
- [build] Update /setup to scaffold FAQ/ directory with both files into consumer projects
- [build] Update session_start.py to detect FAQ/index.md and load it into session context
- [build] Update CLAUDE-TEMPLATE.md to list FAQ/ in the project docs section
- [build] Add FAQ freshness check to the push-and-rezip procedure in CLAUDE.md — when repackaging, check if procedure docs changed since the last FAQ update; if so, update the FAQ templates before packaging
- [test] Verify FAQ/index.md content loads at session start in an adopted project
- [test] Verify Claude can match a user question to the index and read the right answer from faq.md

**/plan Captures flow: define thresholds and fill gaps**
Files:
- `plugin/si-plugin/docs/plan.md`
- `plugin/si-plugin/docs/behaviour.md`
- [build] Define the pipeline threshold in behaviour.md: "if a user would see or experience the difference, it changes the product — update SPEC.md first"
- [build] Add "already decided (found in DECISIONS.md)" as an explicit drop reason in plan.md Step 3
- [build] Specify whether new batch placement needs user approval or Claude places using ordering logic and reports
- [build] Add instruction to state the item count before processing Captures ("3 items in Captures. First: ...")
- [build] Specify what the Captures section looks like after all items are processed (empty section with Parked subsection intact)
- [test] Walk through the Captures flow with the updated plan.md and confirm all five fixes are clear

**Scope and staging clarity: cross-reference /next and /done**
Files:
- `plugin/si-plugin/docs/next.md`
- `plugin/si-plugin/docs/done.md`
- [build] Clarify in next.md that REGISTRY.md is not in build scope — /done Step 1.5 handles all registry updates after the build
- [build] Clean up done.md staging list (Step 2.5) to explain why QUEUE.md is included: /next already modified it, not /done
- [build] Add cross-references between /next Step 2 (batch moves to _build.md) and /done Step 2.4 (deletes _build.md) so the batch lifecycle is traceable across both docs
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

- [idea] /plan Captures processing skips real discussion — items go from Captures straight to batches without the thinking that turns a problem into a plan. The "discuss" step in Step 3 is treated as a speed bump between present and dispose, not actual planning.
- [idea] /plan moves to the next item before the current one is resolved — Claude previews or describes the next agenda item before agreement that the previous one is done. Needs an explicit gate: no next item until the user signals the current one is finished.
- [idea] Decisions aren't being captured — /done writes "Decisions: none" on nearly every entry even when the user made real design decisions during the build. The procedure doesn't define what counts as a decision, so Claude defaults to "none" unless it feels architecturally significant. Needs a definition or examples in done.md so Claude recognises user decisions when they happen (e.g. "session-start message should reference prior session" is a decision about user-facing tone).
- [build] LOG format is wrong — currently writes to one file per date (LOG/YYYY-MM-DD.md) with multiple entries stacked inside. Should be one file per commit (LOG/<hash>.md) plus a lightweight index file (one-line summaries with links). This was decided 2026-05-22 but never implemented. Affects done.md (both build and plan close-out sections), setup.md (LOG scaffolding), and possibly session_start.py if it reads LOG.

### Parked
