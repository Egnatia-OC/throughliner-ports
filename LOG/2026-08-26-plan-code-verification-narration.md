# 3b094b5 — Walkthrough confirmation now reports what the user would see, never the code read to establish it

Reported from a live planning session in another project: while working a `[user]` item's walkthrough, the session read the page's source against the walkthrough and reported its findings in code-level terms — what the checkbox label really is, how the saving code is wrapped so a browser refusing storage fails quietly. A non-coder read that.

Two concerns were raised, and the record answered the first. The reading itself is sanctioned: plan.md's keep-step directs confirming that a walkthrough step can produce the observation it names, and planning is where trying is free. So the defect is register, not the act — the always-loaded plain-language rule slipped at the one moment the procedure directs checking and says nothing about reporting.

The item was deliberately held until the proportionality build landed, so the two rules would be written against each other rather than past each other. That build shipped first, which is why this one could proceed.

The confirmation clause now carries a reporting arm with two limbs: state the outcome as what the user would see, and where the check yields nothing visible — the user's own refinement — fall back to what it means for their step. Never the code read to establish it.

Refused at planning: a freestanding narration rule. The plain-language rule already exists; this is its application at one site, which is why it costs no slot.

**Files touched:** `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — a subordinate amendment to plan.md's walkthrough-confirmation clause, its named parent; it applies the existing plain-language rule at the moment it demonstrably slips. Nothing evicted.
