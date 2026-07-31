# [HASH] — plan.md + done-plan.md reorders made conditional and change-scoped; SPEC.md synced in the same commit

The reorder-by-reasoning runs at two moments — plan.md Step 2 (orders Unprocessed for this session's processing) and done-plan.md's close (orders Processed for /next's durable pick-order). Both stay — they serve different consumers — but re-reasoning over the whole queue's prose from scratch at both moments every session, even when the order is already right (the common case), is the felt token cost. The lighter fix (explicitly NOT a return to blocking): make both reorders conditional (reorder and narrate only when the order is genuinely wrong; silent no-op when already right), scope the re-reasoning to what changed this session, and lean on the prose slug-references items already carry rather than re-deriving dependencies. Explicitly do not reintroduce Blocks:/Depends-on: headers or a dependency lint — that would resurrect the stale-header machinery the two-section recut removed.

done-plan.md's reorder section gained a two-step conditional preamble (scope to this session's changes → reorder only if genuinely wrong, else silent no-op) and the no-headers/no-lint guard. plan.md's Step 2 start-of-processing reorder got the same conditional + change-scoped treatment, with the throughput-floor narration still firing either way (only the move is skipped when order is already right).

Spec-sync gate fired: SPEC.md described both reorders as unconditional ("a reorder that puts the biggest unblockers first"; "Claude walks both queue sections and reorders them"). Two sentences (lines 43 and 45) were synced in this same commit to say the reorder happens only when the order needs it. The FAQ "why did Claude reorder my queue…" entry was likewise updated so it no longer implies a reorder every session.

**Files touched:**
- plugin/si-plugin/docs/done-plan.md (close reorder)
- plugin/si-plugin/docs/plan.md (Step 2 start-of-processing reorder)
- plugin/si-plugin/templates/faq-template.md
- SPEC.md (lines 43, 45 — spec-sync)

**Routed to Captures:** none
