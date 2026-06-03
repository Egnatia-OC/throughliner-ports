# LOG

Full session entries, appended chronologically. Each entry is written by /done.

## Session 1 — Validated prose-only guardrail system

**Built:** Validated prose-only guardrail system (session_start → behaviour.md loading, setup → CLAUDE-TEMPLATE.md scaffolding, rule coverage).

**Files touched:**
- si-plugin/hooks/session_start.py (read-only)
- si-plugin/docs/behaviour.md (read-only)
- si-plugin/templates/CLAUDE-TEMPLATE.md (read-only)
- si-plugin/docs/setup.md (read-only)
- si-plugin/skills/setup/SKILL.md (read-only)

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** _build.md must be whitelisted as a method doc in pre_tool_use.py — currently blocked, creating a catch-22 where the hook prevents Claude from tracking build progress and prevents fixing the bug during an active build.

**Deferred:** _build.md whitelist bugfix queued.

## Session 2 — Fixed _build.md whitelist bug

**Built:** Fixed _build.md whitelist bug in pre_tool_use.py — hook now recognises _build.md as a method doc, unblocking build progress tracking.

**Files touched:**
- si-plugin/hooks/pre_tool_use.py (edited)

**Tests:** 3 passed, 0 failed, 0 skipped

**Decisions:** Self-listed _build.md in the build's own file list as a one-time workaround so progress could be tracked despite the bug being the thing we were fixing.

**Deferred:** None

## Session 3 — Added batch-sizing guidance to plan.md

**Built:** Added batch-sizing guidance to plan.md — specificity gate (name concrete outputs) and verification-burden gate (>5 items = split or sharpen).

**Files touched:**
- si-plugin/docs/plan.md (edited)

**Tests:** 3 passed, 0 failed, 0 skipped

**Decisions:** Placed both gates in Step 6 (Queue editing) as rules alongside the existing entry-format rule, rather than as a separate section.

**Deferred:** None

## Session 4 — Queue restructure

**Built:** Queue restructure — updated all 4 target procedure docs to use batch/ideas queue format instead of loose entries.

**Files touched:**
- si-plugin/docs/plan.md (edited)
- si-plugin/docs/next.md (edited)
- si-plugin/docs/done.md (edited)
- si-plugin/docs/setup.md (edited)

**Tests:** 6 passed (Claude inspection), 0 failed, 3 deferred (E2E — requires plugin reinstall)

**Decisions:** None

**Routed to Ideas:** CLAUDE.md management as explicit plugin concern (user-raised mid-build), 3 E2E tests deferred to queue

## Session 5 — Added three missing behaviour rules

**Built:** Added three missing behaviour rules to behaviour.md (SPEC.md read-only, one-build-at-a-time, between-skill compact nudge)

**Files touched:**
- si-plugin/docs/behaviour.md

**Tests:** 3 passed, 0 failed, 0 skipped

**Decisions:** None — these rules were already enforced mechanically by hooks and /next procedure; this build documented them as explicit behaviour rules.

**Deferred:** None

## Session 6 — Made /done stage-agnostic

**Built:** Made /done stage-agnostic — detects build vs plan mode automatically, runs full close-out after /next and lighter close-out after /plan. Added close-out step to /plan directing to /done.

**Files touched:**
- si-plugin/docs/done.md
- si-plugin/docs/plan.md

**Tests:** 5 passed, 0 failed, 0 skipped

**Decisions:** Dropped session_start.py from scope — mode detection lives in done.md via _build.md presence check, no hook changes needed.

**Routed to Ideas:** None

## a06d140 — Commit-based logging and DECISIONS.md

**Files touched:**
- si-plugin/docs/done.md
- si-plugin/docs/setup.md
- si-plugin/docs/behaviour.md

**Tests:** 10 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Ideas:** None

## 7867b1c — /plan session: route Ideas, form batches

**Queue changes:**
- Created 4 batches: DECISIONS.md full integration, tighten host/target language, CLAUDE.md template ownership, E2E consumer smoke tests
- Promoted 7 items from Ideas (1 question resolved, 1 idea promoted, 3 tests, 2 folded into DECISIONS.md batch)
- 5 items remain in Ideas (1 question, 4 ideas — all new this session or unrouted)

**Decisions:** None

**Ideas routed:** Added 4 new items to Ideas — drift check enforcement, type-agnostic disposition in /plan, host/target propagation gap, DECISIONS.md propagation scan

## f8146b2 — DECISIONS.md full integration

**Files touched:**
- CLAUDE.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/docs/behaviour.md

**Tests:** 6 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Ideas:** None

## 049cf69 — Tighten host/target language in CLAUDE.md

**Files touched:**
- CLAUDE.md

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Ideas:** None

## 448efdb — /plan session: response-shape tags, Captures processing, drift check removal

**Queue changes:**
- Created 3 batches: response-shape tags + annotation, /plan Captures processing fix, rename Ideas to Captures + remove drift check
- Processed 6 items from Ideas (4 promoted into batches, 2 dropped)
- Ideas section now empty
- Added default-to-target rule to project CLAUDE.md

**Decisions:**
- All 5 response-shape tags restored including [SEQUENCE] — labelling choice, capability already existed as prose rule
- Blanket sequencing rule replaced by tag annotations — unannotated steps get Claude's default
- Drift check dropped as standalone /plan step — /done's safeguards (REGISTRY.md update, staleness sweep, SPEC.md read-only hook) already cover it
- Host/target propagation gap is a self-hosting concern, not a plugin problem — dropped

**Ideas routed:** None remaining

## 433beb9 — Fix /plan Captures processing: discussion step and type-agnostic disposition

**Files touched:**
- plugin/si-plugin/docs/plan.md

**Tests:** 5 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## e954603 — Rename Ideas to Captures and remove drift check

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md

**Tests:** 6 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** Rephrase "no active build" wording, LOG test results discussion

## aaddae4 — /plan session: route reader-test findings, define pipeline threshold

**Queue changes:**
- Processed 7 Captures items from reader test (all promoted, none parked or dropped)
- Created 6 new batches: test entry lifecycle, response-shape tag rules, FAQ reference, /plan Captures flow, scope/staging clarity, procedure cleanup sweep
- BRIEF tag conflicts folded into response-shape tag batch
- Captures section now empty
- Queue now has 9 batches total

**Decisions:**
- Pipeline threshold for SPEC.md gate: "if a user would see or experience the difference, it changes the product — update SPEC.md first"
- SPEC.md kept as-is (separate file, pipeline gate retained, role narrowed to onboarding context + drift guard)
- REGISTRY.md kept as-is (Claude lookup table, not user-facing reference)

**Captures routed:** All 7 promoted — none parked, none dropped

## 0a82fd3 — /plan session: design reader-test workflow

**Queue changes:**
- Created batch "Reader-test workflow: build, run, and route findings" at top of queue
- No existing batches modified

**Decisions:** none — design details (fake scenario, doc delivery format, findings routing) are settled but no product-level decisions were made

**Captures routed:** none (inbox was empty)

## ab36e39 — CLAUDE.md template ownership markers

**Files touched:**
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** none

**Routed to Captures:** none

## 09573ac — /plan session: route Captures, add batches, LOG decision

**Queue changes:**
- Promoted "rephrase session-start messages" from Captures → new batch "Session-start message tone" (corrected file ref from next.md to session_start.py)
- Promoted "LOG test results" question from Captures → new batch "LOG test-to-decision linkage" against done.md
- Captures section now empty

**Decisions:**
- LOG keeps all test results organised by commit; decision entries may cite a test outcome as rationale when one drove the call; routine passes don't generate decisions (asymmetric rule)

**Captures routed:** Both items promoted — none parked, none dropped

## e935cfb — /plan session: LOG and planning process observations

**Queue changes:**
- No batches created or modified
- 3 new items added to Captures: /plan skips real discussion, /plan moves to next item prematurely, decisions not captured by /done
- 1 existing Captures item rewritten: LOG file format should be per-commit not per-date (decision from 2026-05-22 never implemented)

**Decisions:** None

**Captures routed:** None promoted — all items remain in Captures for future processing

## 694fbc9 — LOG test-to-decision linkage

**Files touched:**
- plugin/si-plugin/docs/done.md

**Tests:** 1 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** LOG Decisions field is empty in this project — decision-logging machinery built but not exercised during method development

## 6a3b843 — Session-start message tone

**Files touched:**
- plugin/si-plugin/hooks/session_start.py

**Tests:** 2 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## 2513f2e — Reader-test workflow: build, run, and route findings

**Files touched:**
- reader-test-workflow.js

**Tests:** 7 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** 7 items — 1 FAQ resource bundle (13 Q&A pairs), 6 themed finding groups (response-shape tags, BRIEF conflicts, test lifecycle, Captures flow, scope/staging, minor procedure issues — 29 findings total)

## 687d31f — Test entry lifecycle: define mechanics and close gaps

**Files touched:**
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md

**Tests:** 6 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## ac78fc9 — Restore response-shape tags and annotate procedure docs

**Files touched:**
- plugin/si-plugin/docs/behaviour.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/done.md

**Tests:** 7 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Ideas:** None

## e022197 — Response-shape tag rules: defaults, precedence, hierarchy, BRIEF carve-out

**Files touched:**
- plugin/si-plugin/docs/behaviour.md

**Tests:** 13 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## 474fd41 — FAQ reference: create templates and wire into /setup

**Files touched:**
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/hooks/session_start.py
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- CLAUDE.md

**Tests:** 9 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** File list in batches may not be pulling its weight — duplicates entry info, omission went unnoticed

## a08b65b — /plan session: remove DECISIONS.md, drop file lists, process Captures

**Queue changes:**
- Created 2 batches: "Remove DECISIONS.md, restructure LOG to index + log" (top), "Drop file lists from batches" (second)
- Processed 5 Captures items: 2 dropped (resolved by user's plan.md rewrite), 2 promoted into new batches, 1 absorbed into DECISIONS.md/LOG batch
- Updated "/plan Captures flow" batch: DECISIONS.md reference changed to LOG/index.md
- Captures section now empty

**Decisions:**
- DECISIONS.md removed as a project doc — it was never properly planned through the pipeline; decisions belong in LOG entries, no separate file needed
- File lists dropped from batches — overly prescriptive, Claude can't perfectly anticipate every surface an edit touches; entries name their own targets

**Captures routed:** None (all processed)

## f11be10 — /plan session: rewrite plan.md, add Captures for plan behaviour

plan.md was rewritten from scratch because the original was too long, unreadable, had principles in the wrong order, repeated itself, and buried ground rules at the bottom. The routing step ("Determine what the user wants") was removed because it caused Claude to dump a full queue summary when Captures was empty — batches already went through /plan to get there, so summarising them serves no purpose. Compression was removed because it was a leftover from the old plugin shoved in as an afterthought; it shouldn't come back until the plugin is working much better.

5 new items added to Captures for future processing: remove "design decisions" as a separate category (reasons are being lost), sizing gates need rethinking, rename "questions" to "captures" across docs, what /plan should do when Captures is empty, and Claude's dependency-management ownership model. 2 items were added then removed (summary format ideas, superseded by the broader question about whether the summary should exist at all).

## 77c1557 — Remove DECISIONS.md, restructure LOG to index + log

**Files touched:**
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/docs/behaviour.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md
- SPEC.md
- CLAUDE.md
- DECISIONS.md (deleted)
- LOG/index.md (created)
- LOG/log.md (created)
- LOG/2026-06-01.md (deleted)
- LOG/2026-06-02.md (deleted)

**Tests:** 9 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## e6432a5 — Drop file lists from batches

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md
- QUEUE.md

**Tests:** 10 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## a24e5ad — Captures flow: thresholds, drop reasons, placement, empty state

**Files touched:**
- plugin/si-plugin/docs/behaviour.md
- plugin/si-plugin/docs/plan.md

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## f6d4a78 — Scope and staging clarity: cross-reference /next and /done

**Files touched:**
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/done.md

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## 50a0d73 — Procedure doc cleanup sweep

**Files touched:**
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/behaviour.md

**Tests:** 1 passed (batch end-to-end read), 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** /done Phase 3 should be single recommendation; /next presentation should group by Build/Test headers not show type markers; /next prompt should be "Ready?" not a menu; /done test generation should scope to code changes not all file changes

## 409b0b7 — /plan session: process Captures, create batches, file sizing research

**Queue changes:**
- Created 5 batches: Dependency ownership (absorbed 2 Captures), LOG reasoning, Rename "open questions" to "captures", Tighten /plan Captures step 2, Scope /done test generation to code changes
- Processed 9 Captures items: 5 promoted (2 absorbed into dependency batch), 2 dropped (already fixed in target), 1 parked with research
- 1 new Captures item added: planning-time test entry inflation
- Pushed v1.3.0 repackage before planning

**Decisions:** None

**Captures routed:** All 9 processed — 5 promoted, 2 dropped, 1 parked, 1 new item added

## 6a5ec81 — Dependency ownership: state the principle and audit for violations

**Files touched:**
- plugin/si-plugin/docs/behaviour.md: added "Dependency ownership" section (Claude owns sequencing, user owns scope)
- plugin/si-plugin/docs/next.md: removed "pick a different entry" from Step 1.4, added /plan routing note
- plugin/si-plugin/docs/plan.md: changed "proposes" to "determines" in Step 3 Ordering

**Tests:** 4 passed, 0 failed, 0 skipped

**Decisions:** None

**Routed to Captures:** None

## cf3217e — LOG reasoning: replace Decisions field with mandatory WHY

**Files touched:**
- plugin/si-plugin/docs/done.md: replaced **Decisions:** with **Why:** in both build and plan close-out LOG templates

**Tests:** 4 passed, 0 failed, 0 skipped

**Why:** The Decisions field was too narrow — it only captured explicit "decisions" and defaulted to "none" in almost every entry. Reasoning existed for every build (user direction, planning rationale, tradeoffs) but didn't register as a "decision." Replacing with a mandatory **Why:** field ensures reasoning is always recorded.

**Routed to Captures:** None

## dee7e5e — Verify "open questions" rename complete; tighten pre-push sweep

**Files touched:**
- CLAUDE.md: restructured push-and-rezip step 2 — two-pass sweep with explicit feed, separated target consistency from project staleness
- QUEUE.md: added push-marker Capture

**Tests:** 1 passed (grep for "open question" — 0 hits), 0 failed, 0 skipped

**Why:** The batch was queued to catch lingering "open questions" references, but the rename had already been completed in session e954603. All remaining "question" uses are the [question] type marker, pipeline stage, disposition, or plain English. The mid-build CLAUDE.md edit came from a user question about what feeds the pre-push staleness sweep — the original step 2 said "check for staleness" without specifying against what. Now explicitly fed by `git log origin/main..HEAD` → LOG entries.

**Routed to Captures:** Push markers in LOG (added during build)

## 8512268 — Tighten /plan Captures processing step 2

**Files touched:**
- plugin/si-plugin/docs/plan.md: merged sub-steps 1 (present) and 2 (discuss/recommend) into single sub-step with explicit four-disposition list

**Tests:** 2 passed, 0 failed, 0 skipped

**Why:** The two-step split (present without assessing → then discuss and recommend) forced Claude to produce an empty first turn before engaging. Merging into one turn is more natural and ensures substance engagement always accompanies presentation. Adding the explicit disposition list (promote / question first / park / drop) prevents Claude from omitting options or defaulting to promote without surfacing alternatives.

**Routed to Captures:** None

## 994ca84 — Scope /done test generation to code changes

**Files touched:**
- plugin/si-plugin/docs/done.md: added scoping rule to Step 1.2 — post-build tests limited to code/app file changes, excluding procedure doc and template edits

**Tests:** 1 passed, 0 failed, 0 skipped

**Why:** Claude was generating arbitrary post-build tests for procedure doc and template edits even though those batches already include their own [test] entries for verification. Scoping Step 1.2 to code/app files only eliminates the redundancy and stops Claude from inventing tests where the batch already has coverage.

**Routed to Captures:** Session-start "no active build" message is confusing when user is about to start a build

## cc0ccb9 — /plan session: process Captures, create batches, rework E2E scope

**Queue changes:**
- Created 5 batches: add entry question to /plan Step 1, push markers in LOG, move /done handoff before push prompt, rephrase session-start status messages, scope planning-time test entries
- Reworked E2E batch from 3 smoke tests to just /setup verification
- Processed 6 Captures: 4 promoted into batches, 2 parked (self-hosting support with sweep design note, /done spec check)
- 1 new Capture added: capture moments should loop across all skills

**Why:** User observed that /plan jumps straight into Captures processing without asking what brought them here — led to a new batch for an entry question loop. E2E batch was redundant because self-hosting already exercises /plan, /next, /done every session; only /setup on a fresh project is untested. Push markers, handoff ordering, session-start tone, and planning-time test inflation were all concrete fixes from recent build observations.

**Captures routed:** 4 promoted, 2 parked, 1 new added

## fe48e89 — Add entry question to /plan Step 1

**Files touched:**
- plugin/si-plugin/docs/plan.md: rewrote Step 1 to include entry question loop before Captures processing

**Tests:** 0 (procedure doc change — no code/app tests generated)

**Why:** /plan was jumping straight into Captures processing without asking the user what brought them here. Users often invoke /plan because they have something top of mind, not because they want to process Captures. The entry question loop lets them share and route their items first, repeating "anything else?" until they explicitly say they're ready for Captures.

**Routed to Captures:** None

## 52be5d4 — Add push markers to push-and-rezip procedure

**Files touched:**
- CLAUDE.md: inserted step 3 ("Append push marker to last LOG entry") into push-and-rezip procedure, renumbered steps 3-8 → 4-9

**Tests:** 0 (procedure doc change — no code/app tests generated)

**Why:** Release boundaries were invisible in LOG without running git commands. Adding a `**Pushed:** v<VERSION>` line to the last LOG entry during push-and-rezip makes it clear which entries shipped in each release, directly in the log.

**Routed to Captures:** None

## bcf24cc — Move /done handoff before push prompt

**Files touched:**
- plugin/si-plugin/docs/done.md: moved push prompt from step 2.4.8 to after Phase 3 handoff (build close-out); moved push prompt from step 3.8 to after step 4 handoff (plan close-out)

**Tests:** 0 (procedure doc change — no code/app tests generated)

**Why:** The handoff recommendation ("next up is X") gives the user context for whether to push now or keep building. Having the push prompt before the handoff meant the user was deciding blind. Reordering both close-out paths so the user sees what's next before being asked about pushing.

**Routed to Captures:** None

## 20de57d — Rephrase session-start status messages

**Files touched:**
- plugin/si-plugin/hooks/session_start.py: replaced "No unfinished builds from a previous session" with "Ready."; trimmed redundant "A build is still open from a previous session" from active build message

**Tests:** 2 passed, 0 failed, 0 skipped

**Why:** The no-active-build message defined the state by what was absent, reading as a failure report rather than neutral status. "Ready." states what's true. The active build message had a redundant sentence restating what "ACTIVE BUILD in progress" already conveyed.

**Routed to Captures:** None

## 81135bc — Scope planning-time test entries

**Files touched:**
- plugin/si-plugin/docs/plan.md: added "Test entries" rule to Step 3 between batch structure example and sizing gates

**Tests:** 0 (procedure doc change — no code/app tests generated)

**Why:** Claude was inflating batches with [test] entries for behaviours already self-evident from the build entries, and /done already generates post-build tests for code changes. The new rule makes [test] entries opt-in at planning time — only when there's a distinct behaviour to verify that the build entries don't cover.

**Routed to Captures:** None

**Pushed:** v1.5.0

## 9edb8fa — E2E: verify /setup on fresh project

**Files touched:**
- Polite Fart Announcer 3/ (temporary test project, read-only inspection)

**Tests:** 1 passed (with 2 deviations), 0 failed, 0 skipped

**Why:** First E2E test of /setup against a fresh consumer project. Needed to verify that the host plugin scaffolds all project docs correctly from templates before testing more complex scenarios. All 8 files scaffolded correctly and templates matched exactly. Two deviations found from the same root cause: /setup oversteps into /plan territory — Q4 expands a single user answer into a fully scoped batch (procedure says singular [build] entry), and the closing message directs to /next first (implying the batch is build-ready when scope decisions belong in /plan).

**Routed to Captures:** /setup oversteps into /plan territory (Q4 entry expansion + closing message directing to /next)

## 388f68e — README overhaul

**Files touched:**
- README.md (rewritten)

**Tests:** 1 passed (download link URL), 1 deferred (GitHub render — post-push)

**Why:** The README was written for someone already familiar with the project. Repo browsers landing on the GitHub page need to quickly understand what this is, why they'd want it, and how to get it running. Rewrote the pitch from feature description to user benefit, added a direct download link so users don't need to clone the repo, and expanded "Getting started" to set expectations about the setup → plan → next flow.

**Routed to Captures:** None

**Pushed:** v1.5.1

## ef416bc — /plan session: 5 batches from Captures, post-update migration design

**Queue changes:**
- Created 5 batches: LOG multi-file split, Why pipeline polish, Skill handoff polish, Mid-build scope expansion protocol, Post-update migration detection
- Processed 6 Captures: 4 promoted to batches, 1 rolled into mid-build scope expansion batch, 1 parked (batch cohesion ordering heuristic)
- 2 new items from conversation: LOG multi-file split (promoted), batch cohesion heuristic (parked)
- Resolved 3 design questions for post-update migration: dotfile for version storage, guided walkthrough via /setup, warning not blocking

**Why:** Captures had accumulated from the E2E testing session and prior builds. Post-update migration was the meatiest item — design questions needed resolving before it could become a batch. User identified that the project-docs portion of the pre-push sweep would be superseded by the migration process (same problem for consumers and self-hosters). LOG multi-file split arose from user observing that a single log file becomes unwieldy — per-push files with reversed index keeps the most relevant context where Claude reads first. Several captures naturally grouped: /done handoff and /setup closing message merged into a cross-skill handoff polish batch; capture moments loop rolled into mid-build scope expansion.

**Captures routed:** 6 processed (4 promoted, 1 rolled in, 1 parked), 2 new from conversation (1 promoted, 1 parked)
