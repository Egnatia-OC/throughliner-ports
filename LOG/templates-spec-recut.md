# 969af5b — CLAUDE-TEMPLATE.md + setup.md recut to the two-section work-line model (Processed/Unprocessed, build/audit/freeform flavors with `[user]` handover, red flags as tagged state-carrying lines); setup.md scaffolds `resources/research/` and writes the onboarding answer as an Unprocessed work line; SPEC.md consistency-checked.

The consumer-facing scaffolding was the last part of the plugin still describing and creating the old five-section queue. CLAUDE-TEMPLATE.md documented Red flags / Batches / Deferred tests / Captures, and /setup scaffolded a fresh QUEUE.md with those same sections plus a "Build subheading" onboarding entry — so a new consumer would have started on the old model. This batch brings both onto the two-section work-line model that the earlier redesign batches settled.

CLAUDE-TEMPLATE.md: recut the Project docs QUEUE line to describe Processed (vetted, cleared-to-run line) and Unprocessed (captured, not yet discussed) work, the `#### ` heading + `[slug]` + provenance line format, the build/`[audit]`/`[freeform]`/`[user]` flavor tags, and red flags as tagged work lines carrying a state; recut the Workflow /next line to build/audit-by-flavor with no separate test type; and pointed the Route-discoveries rule at the Unprocessed section.

setup.md: replaced the five-section QUEUE.md scaffold with the two-section shape (Processed with the cleared-to-run marker at its top, Unprocessed below); updated the SPEC scaffold's "Project docs" QUEUE line; added a `resources/research/` folder to the Step 2 scaffold so research notes have a home from day one (the folder every session may now write to); and recut Q4 and Step 4 so the onboarding answer is written as an Unprocessed work line (slug + "captured by you") rather than a Build-subheading entry.

SPEC.md needed only a consistency check — it was already synced to the two-section model in [work-line-behaviour-defs], and the scan found no stale old-model vocabulary, so no edit. This is the last batch above the cleared-to-run line; the redesign now moves to dogfooding and the fresh-queue clean break.

**Files touched:**
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md — recut QUEUE-doc line, /next workflow line, discoveries rule
- plugin/si-plugin/docs/setup.md — two-section QUEUE scaffold, resources/research/ folder, Q4 + Step 4 Unprocessed work line
- SPEC.md — consistency-checked only (no edit)
- QUEUE.md — batch removed at scope-lock; one host-side deferred test filed

**Routed to Captures:** none
