# 15e10c9 — Recommending against a surfaced advisory now requires checking its reasons first

Build entry; the planning record is `2026-08-21-advisory-surfaced-then-overridden.md`. The advisory was surfaced correctly and then contradicted in the same session with its reasons never checked — the user caught it, and one grep showed a live reason sitting on the exact items being recommended. Built as one limb on plan.md's advisory step, sited at the contradiction rather than the surfacing: before this session recommends a course contradicting the advisory it surfaced, check the advisory's stated reasons against the current state — a grep or a file read — and say in the recommendation what was found, including where a reason is dead. Per-session checking stays refused; surfacing and delete-at-read are textually unchanged.

**Files touched:** `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none from this item.
Tick: done, confirmed — the limb carries its trigger; neighbouring text unchanged.
FAQ: not needed because the user sees a better-grounded recommendation and does nothing different.
Rule gate: run — admitted as an amendment to plan.md's advisory step, parent named. Nothing freestanding, nothing evicted.
