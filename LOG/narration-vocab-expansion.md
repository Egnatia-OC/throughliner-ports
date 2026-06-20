# [HASH] - plugin-behaviour.md + five done docs: expand the Vocabulary list and add a plain-language guard for the captures narration

A /done close-out narrated no-unprocessed-captures-remaining, leaking the background-only term processed/unprocessed captures and misleading the user (processed captures can still be waiting). The Vocabulary list now names processed/unprocessed captures plus staleness sweep, hash backfill/the placeholder, queue-lint flag, and newly-unblocked/unparked as background-only. A plain-language guard at the recommend-next step in all five done docs (build/test/audit/plan/freeform) keeps the structural term out of user-facing output and the plain statement accurate, while leaving the scan instruction's wording intact.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/done-build.md
- plugin/si-plugin/docs/done-test.md
- plugin/si-plugin/docs/done-audit.md
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/docs/done-freeform.md

**Routed to Captures:** none
