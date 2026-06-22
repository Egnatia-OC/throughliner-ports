# [HASH] — Mechanical queue cleanup is narrate-and-do, not ask-for-approval

Across several sessions Claude over-asked on routine queue bookkeeping — for example, finding batches whose "depends on" was now met and asking permission to clear the redundant notes as cleanup riding the commit. Clearing a met dependency is bookkeeping on a batch that's otherwise fine: it drops nothing, reorders nothing, changes nothing the user owns. So asking defers a call Claude already owns and trains the user to rubber-stamp routine maintenance.

The mis-firing piece was plugin-behaviour.md's Dependency-ownership Staleness watch, whose fix-path let Claude make mechanical fixes "with the user's approval." That path is now narrate-and-do: mechanical maintenance — a drifted pointer whose target content is unchanged, and clearing a met `Depends on:` / `Blocked by:` note whose blocker has already shipped — Claude fixes and reports in one line, riding the commit, with no approval ask. Fate decisions (drop / rewrite / keep) still defer to /plan, unchanged; a content change in referenced material (the quoted wording itself moved, which may signal the item's premise shifted) is not mechanical and still goes to /plan. The four done-*.md close-out staleness lines (build, test, audit, freeform) were updated to match, and a plain-English FAQ entry was added for a user who sees Claude tidy queue bookkeeping during a commit without being asked. Scoped broader than the dependency case at the user's call — both met-dependency cleanup and the other small mechanical fixes.

This change also makes the [staleness-flag-fix-path] deferred-test line in QUEUE.md stale: it verifies the old "pure pointer drift offers an in-session fix with approval" behaviour, which this batch supersedes with narrate-and-do. Rewriting or dropping that line is a fate decision, so it was flagged for /plan rather than edited here.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/done-build.md
- plugin/si-plugin/docs/done-test.md
- plugin/si-plugin/docs/done-audit.md
- plugin/si-plugin/docs/done-freeform.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
