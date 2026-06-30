# 77ef065 — [readiness-line] "cleared to run" queue boundary: SPEC capability + plan.md Step 4 positioning + done-plan confirm + next.md line-aware pre-flight + FAQ

Added the readiness line — a `--- Cleared to run above this line ---` marker /plan maintains in Batches, splitting work vetted and safe to build (above) from work that still needs planning (below). It's the boundary the user was filling by hand in goal sessions ("how many batches are safe to run?"), and cruise control later inherits it as its run bound — a clean finish at the line rather than running into unvetted work. SPEC.md How-it-works gains it as a user-facing capability. plan.md Step 4 positions or moves the line at every /plan close against the [dependency-tracing-pass] readiness definition (traced + complete + correctly ordered + not still exposed to a raw capture below the divider) and narrates where it lands. done-plan.md confirms and narrates it at the planning /done close. next.md's pre-flight is line-aware: while cleared batches sit above it the line is informational and skipped like any marker; when it reaches the top of Batches /next soft-stops and recommends /plan to vet the work below (distinct from the hard push/plan-marker halts). Added a consumer FAQ entry on what above/below means. Built on [dependency-tracing-pass] for its readiness definition; verification is deferred host-side.

**Files touched:**
- SPEC.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none (this batch). The run's audit filed [readiness-line-narration-frequency] against this batch's text — double-narration across plan.md Step 4 and done-plan.md, plus an anti-nag tension in narrating the line every close — for a later /plan to route.
