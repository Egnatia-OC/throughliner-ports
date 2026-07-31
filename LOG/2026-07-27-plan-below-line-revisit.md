# 053c608 — plan.md + plugin-behaviour + SPEC + FAQ: standing /plan revisit lifts shelved below-line work when its lift-condition clears

Readiness was set once at processing and never revisited, so an item correctly shelved below the cleared-to-run marker (because it waited on something outside the queue) depended on the user remembering to come back to it — the exact thing the queue exists to prevent (observed live: Stephanie abuse, Metro-admin). This build closed the gap in two halves.

1. **Enabling half — lift-conditions recorded in prose.** plan.md Step 3 now records, on every item it places below the marker, the specific event or dependency that would lift it ("cleared once [slug] is built and verified", "after a full computer restart", "once the manifest is pushed"). Prose, not a hook-parsed field — keeps faith with rationale-is-prose and needs no hook change. Without a recorded condition the revisit can't tell waiting from ready without nagging.
2. **The revisit — plan.md Step 1.** Walks the below-line items each session and classifies each by its lift-condition: mechanically checkable (dependency built+verified per LOG, a push, a file present) → check silently and propose lifting; user-only (an external event only the user knows) → gather all such into ONE consolidated question, never one ask per item (the batching is what prevents nagging); provably still-waiting → skip silently. Folds into the single Step-1 opening narration alongside the advisory-consume and the completion-ask. Lifting reuses Step 3's marker placement, narrated not asked.

Also folded in ([advisory-narrows-plan-scope] concern 1): sharpened Step 1's advisory-consume so the forward-recommendation advisory orients where the session *starts* and never narrows it to only the advised item — Step 2 still processes the full Unprocessed queue.

Coordinated with [user-handover-lifecycle], which edits the same Step 1 and deferred its dependent-re-clearing piece here; this built after it.

**Files touched:**
- plan.md (Step 1 below-line revisit + advisory-consume sharpen; Step 3 lift-condition recording)
- plugin-behaviour.md (new "Below-the-line revisit" section)
- SPEC.md ("Lifting shelved work" paragraph)
- templates/faq-template.md + faq-index-template.md (new entry)

**Routed to Captures:** none
