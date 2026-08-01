# ea272f6 — Give /plan a "seed the queue from SPEC" capability so setup-seeded scope doesn't die in SPEC

When /setup writes a rich SPEC, that whole feature set is buildable work with no path into the queue — it "dies in SPEC" (proven live in a Verso /plan: full Gmail-client SPEC, empty Processed, only an ad-hoc save when Claude happened to notice).

Added a "Seed the queue from SPEC" step to plan.md's Step 1. It offers automatically only in the narrow thin-queue/rich-SPEC state (Processed empty/near-empty while SPEC describes real unbuilt features, checked against LOG so built features don't count) — deliberately not whenever SPEC merely outruns the queue, which would mean per-session whole-queue diffing (the staleness/cost trap). The user can also invoke it manually any time. On firing, the user chooses granularity (coarse milestones vs granular per-feature), and the derived items land in Unprocessed as ordinary captures for later processing — never straight into Processed. Seeding lives in /plan, not /setup: /setup stays scaffolding + interview and never auto-spawns work.

SPEC.md gained a "Seeding the queue from SPEC" paragraph under How it works, and a new FAQ entry describes the /plan behaviour.

**Files touched:**
- plugin/si-plugin/docs/plan.md — the seed-from-SPEC step (auto-trigger + manual invoke)
- SPEC.md — "Seeding the queue from SPEC" paragraph
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line

**Routed to Captures:** none
