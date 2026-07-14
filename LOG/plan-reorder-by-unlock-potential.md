# 04d59e6 — Added /plan-close reorder step: auto-reorders Unprocessed by unlock-potential and Processed by build-order, narrated not asked

Queue ordering was ad-hoc — Claude reordered when it remembered, with no defined step. Added a "Reorder both sections" sub-step to plan.md's Step 3 close-out, before the cleared-to-run line positioning. Unprocessed reorders by unlock-potential (process first what unblocks the most other work); Processed reorders by build-order (build first what unblocks later work). Fork resolved: Claude auto-reorders and narrates, does not ask — consistent with the existing ordering-ownership rule in plugin-behaviour.md. Narration scales: a reorder changing what /next picks next is flagged clearly; a trivial tidy gets one line; no reorder says nothing.

**Files touched:**
- plugin/si-plugin/docs/plan.md: new "Reorder both sections" step in Step 3
- SPEC.md: added "Close-out reorder" paragraph in How it works
- plugin/si-plugin/templates/faq-template.md: added "Why did Claude reorder my queue?" entry
- plugin/si-plugin/templates/faq-index-template.md: added index line

**Routed to Captures:** none
