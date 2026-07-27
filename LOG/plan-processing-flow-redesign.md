# [HASH] — Redesign /plan's processing flow: triage bulk-drop, start-of-processing reorder + throughput floor, skip-to-defer, process-now offer

Reworked plan.md's Step 2 so /plan feeds the single queue-clearing /next runner a well-ordered, well-vetted cleared region. Four changes, merging three captures ([quickplan-skill], [skip-to-defer-in-plan-loop], [capture-then-offer-process-now]). (1) A triage bulk-drop pass before the one-at-a-time loop skims Unprocessed for items with a one-sentence uncontestable drop-reason and offers them as one bulk-approval set — subtractive only, never advancing work into Processed, so undesigned work can't slide in unread. (2) A start-of-processing reorder orders Unprocessed by unblock-potential and narrates a throughput floor ("process at least N before your next /next") — explicitly a planning-throughput target, not a context-budget count, keeping session-sizing out of /plan. (3) Skip-to-defer is folded into the checkpoint's existing off-ramp as a fourth option rather than a standalone gate — a separate skip prompt would re-create the over-asking pattern the method just removed; skipped slugs are tracked in _plan.md so they don't re-surface that session. (4) A capture the user files mid-/plan now comes with a process-now-or-carry-on offer instead of a bare "anything else?", so a new idea never reads as parked.

Concern weighed during the build: skip-to-defer moves an item to the bottom of Unprocessed, which risked reading as a new shelving state against plugin-behaviour.md's "One shelf, one shelving move" / anti-invention guardrail. Resolved by framing skip as an instance of the single existing shelving move (place/return at the bottom of Unprocessed), not a new state — and updating that rule to name skip as one of its three triggers, rather than adding a state.

**Files touched:**
- plugin/si-plugin/docs/plan.md — Step 2 rewrite (two pre-loop passes, skip off-ramp, process-now paragraph, _plan.md skip tracking)
- plugin/si-plugin/docs/plugin-behaviour.md — "close by who raised it" process-now branch; "One shelf, one shelving move" skip note
- SPEC.md — new "Processing flow" paragraph; "Close-out reorder" distinguished from start-of-processing reorder
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new consumer FAQ entry

**Routed to Captures:** none
