# 29ba751 - done.md + done-plan.md + done-test.md: commit first at /done, then offer push - do not bundle commit into the choice

The /done commit step asked Commit-and-push-or-just-commit before doing anything, bundling a certain action (the commit always happens) with a real choice (the push). The commit core now commits first - its message is the already-approved LOG entry, nothing new to confirm - then offers push only when a remote exists, matching the file-safety rule (do the safe local thing, gate the outward one). done-plan.md and done-test.md reword their overrides to commit-and-do-not-offer-push. A stale example in plugin-behaviour.md's approval-time rule was updated to the new shape.

**Files touched:**
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/docs/done-test.md
- plugin/si-plugin/docs/plugin-behaviour.md

**Routed to Captures:** none
