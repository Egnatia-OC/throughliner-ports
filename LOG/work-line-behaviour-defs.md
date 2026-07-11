# 8697a79 — Build [work-line-behaviour-defs] — behaviour docs + SPEC recut to the two-section work-line model

Founding build of the queue-redesign branch. The old model carried several parallel work-type structures — build/test/audit batches, parking, dependencies, red flags, deferred tests — each with its own machinery. This batch replaces them in the behaviour definitions with a single notion of *work* carrying two properties: who does it (Claude by default; user-work marked `[user]`) and whether it's processed (which of two sections it sits in). QUEUE.md's model collapses to exactly two headings — Processed and Unprocessed — and a capture becomes unprocessed work.

plugin-behaviour.md changes: the Captures section now defines a capture as unprocessed work appended to Unprocessed, with a four-part line format (one-line description, prose rationale, a lightweight slug for LOG traceability only, and a provenance label — "captured by you" / "by Claude" — that persists after processing); the `####` heading machinery, the processed/unprocessed divider, and `Blocked by:`-at-filing are gone. The Red flags section and its Flag states subsection were removed entirely. Dependency ownership was gutted down to what survives the new model — Claude still owns sequencing and placement, the slug stays as a lightweight LOG link, narrate-your-placement stays — while Depends on / Blocks / Blocked by / Parked headers, the Unpark and Staleness watches, the parked-shelf review, dependency tracing, the anti-nag stamp, and circular-incorporation all went. Why-pipeline, Routing and discipline, and Scope had their batch/capture/promote/route-to-Captures vocabulary rewritten to work-line vocabulary (append to Unprocessed; filing vs *processing*), and Scope now notes that /next self-scopes under the new model. Consequential vocab touch-ups landed in the Communication scan-consolidation and approval-time bullets, the Vocabulary list (Processed/Unprocessed are user-facing structure now, not background terms), and Index entries.

SPEC.md was brought into sync in the same commit (the spec-sync obligation): the QUEUE.md doc-list line now reads "processed and unprocessed work," and the standalone Red flags paragraph was removed. Per the founding batch's own trace (SPEC lines 23/41), those are the two sentences the change made stale; the risk-surfacing Principles survive as general behaviour, since only the dedicated section-plus-states machinery was removed, not the plain-English screening. The FAQ template gained a Processed/Unprocessed queue-shape entry (replacing Batches-vs-Captures) and lost the Red flags entry, with the index updated to match.

Part of a phased redesign: plan.md and done-plan.md follow in [plan-work-line-procedure]; next.md, the /done family, the hooks, templates, and this project's own QUEUE.md are the still-unshaped middle captured as [remaining-redesign-batches].

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- SPEC.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
