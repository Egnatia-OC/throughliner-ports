# bebffe7 — done-plan.md + plan.md + plugin-behaviour.md + SPEC: clear the forward-advisory at the always-runs /done close

Moved the forward-recommendation advisory's consume-and-clear from the end of the /plan discussion ("once the order is agreed" — a beat an off-ramp or no-work /plan never reaches, so the clear was silently skipped and stale advisories survived) to the mandatory /done close, the one close that always runs however a /plan ends. Added a "Clear the consumed forward-recommendation advisory" section to done-plan.md that deletes the advisory if it oriented the session, honouring an explicit persist-condition (the live example being an advisory that says "persist until the cleared builds ship," tied to a build event rather than the next planning session). plan.md Step 1 was retitled Read (not Consume), noting the clear moved to /done. plugin-behaviour.md's advisory Lifecycle was rewritten as two placed halves — read at /plan Step 1, clear at the /done close — with the persist-condition and orient-once conditions spelled out. SPEC line 47 was synced in the same commit (spec-sync gate) to describe the clear happening at the /done close rather than at order-agreement.

**Files touched:**
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/plugin-behaviour.md
- SPEC.md

**Routed to Captures:** none
