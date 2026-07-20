# 087be76 — Add narration-discipline clause for filing/deferring a capture, dropping day-scoped timing wording

Observed 2026-07-14 in a /plan: filing a discussion idea, Claude narrated "This is a design thread that won't be fully designed today, so it belongs as a capture in Unprocessed" — over-explaining the internal shelving mechanics the user doesn't need, and using day-scoped timing ("today") that misrepresents the model, where every idea is captured immediately and fleshed out at some later /plan rather than on a same-day boundary. This build adds a "Narration discipline when filing or deferring a capture" bullet to plugin-behaviour.md's Captures section with two rules: state what was filed in one line without narrating the shelving reasoning, and never use day-scoped timing — the accurate frame is "capture now, design later (loosely)." The model half of the original observation (capture-now/design-later) is handled by [single-shelf-model-hardening], built alongside this in the same session; this line is only the narration-wording fix, which is why both touch the same doc.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — added narration-discipline bullet to Captures section

**Routed to Captures:** none
