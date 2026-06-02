# QUEUE

## Batches

Worked top to bottom. Each batch is one /next session — builds first, then tests.

**Session-start message tone**
Files:
- `plugin/si-plugin/hooks/session_start.py`
- [build] Reword the active-build branch (~line 96): "The previous session was interrupted mid-build" implies a crash. Make it neutral — the build is simply still open/unfinished, which is normal when the user closes the app deliberately.
- [build] Review the no-active-build branch (~line 103) and soften if needed so both branches share a calm, reassuring tone.
- [test] Trigger session_start in both states (active build present / absent) and confirm each message reads as reassuring, not alarming.

**LOG test-to-decision linkage**
Files:
- `plugin/si-plugin/docs/done.md`
- [build] Add rule to done.md: LOG keeps all test results in the Tests field. When a test outcome drove a design decision (failure caused requeue, rethink, or revealed a gap), the Decisions entry cites that test outcome as its rationale. Routine passes stay in Tests only — they don't generate decisions.

**E2E: consumer project smoke tests**
- [test] Run /plan in consumer project, verify it creates a batch with correct format (bold title, Files list, type-marked entries)
- [test] Run /next in consumer project, verify it picks up a batch and builds all items
- [test] Run /done in consumer project, verify it routes findings to Captures

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

- [idea] **FAQ reference resource** — Reader test produced 13 FAQ Q&A pairs covering: Captures vs Batches, crash recovery, SPEC.md protection, capturing ideas mid-build, empty queue meaning, silent steps, batch lifecycle, spec-first pipeline, prior decisions, batch ordering, testing without a framework, test failure routing, sequential confirmation. All high confidence. Ready to become a user-facing reference doc.

- [idea] **Response-shape tag system gaps** (6 findings) — "Default behaviour" for unlabelled steps is undefined; tag precedence (step-level vs phase-level) is unstated; user communication preferences vs procedure tags hierarchy is missing; SILENT violations in /done Phase 2 and /next Step 3 suggest the tag needs reinforcement or examples. Sources: all three simulations.

- [idea] **[BRIEF] tag conflicts** (3 findings) — next.md Step 1.4 tagged BRIEF but requires structured presentation exceeding 2 sentences; plan.md Step 7 close-out tagged BRIEF but needs summary + /done prompt; plan.md Step 2 "present the queue state" conflicts with Step 7 BRIEF. Either widen BRIEF for structured content or retag these steps.

- [idea] **Test entry lifecycle gaps** (4 findings) — No guidance on how to "execute" a [test] entry during /next (what does Claude mechanically do?); _build.md ticking format undefined for tests; no test-failure path in /next; relationship between batch [test] entries and /done-generated tests is unspecified. This is the biggest doc gap — it caused the worst simulation deviation (SILENT violation).

- [idea] **/plan Captures flow completeness** (5 findings) — Pipeline threshold for "changes the product" undefined; new batch placement approval not specified; "already decided" missing as explicit drop reason; no instruction to state item count before processing; Captures section structure after full processing unspecified.

- [idea] **Scope and staging clarity** (3 findings) — REGISTRY.md not in /next scope but /done expects it updated; done.md staging list implies QUEUE.md edits no step authorizes; batch removal timing between /next and /done is confusing.

- [idea] **Minor procedure issues** (7 findings) — next.md Step 7 missing (numbering gap); blocker gate scope for Captures-section questions ambiguous; LOG multi-entry format on same day unspecified; /done Phase 3 handoff conditions need priority ordering; "routed to Captures" in handoff needs scoping to this session; pass marker format inconsistency; empty queue lifecycle concept missing; next.md Step 2 needs a tag.

### Parked
