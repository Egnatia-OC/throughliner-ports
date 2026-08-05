# [HASH] — /next now removes work items from QUEUE.md one at a time as each is ticked, not bulk at scope-lock

Both defences of the bulk clear were weighed at processing and neither survived: "it frees the queue for concurrent sessions" dissolved under branch-per-session (a concurrent session has its own copy), and destination-first safety survives untouched because _build.md is still written in full at scope-lock — only the removal becomes progressive, so no item ever exists in neither file. Per-item removal is also safer on abandonment: a run that dies partway leaves the queue holding exactly the work that was never done, instead of an emptied queue whose contents survive only in a file the close deletes. The queue always tells the truth — an item still showing means not built yet — which was the user's original instinct arrived at from the correctness side. The mechanism is tick-then-remove: each item is ticked in _build.md Progress first, then removed from QUEUE.md, preserving destination-first at every individual step. next.md's Step 2.4 becomes leave-in-place, Step 3 gains the removal, and next-build.md's build list gains it as step 5.

The run that built this change already worked per-item itself, ahead of the doc edit, under the standing principle that a decided rule applies from the moment it is decided.

**Files touched:** docs-b/next.md, docs-b/next-build.md, docs-b/plugin-behaviour.md (Scope section note).
**Routed to Captures:** none for this item.
FAQ: not needed because the existing _build.md and cleared-to-run entries already describe the run's mechanics; the queue shrinking gradually explains itself.
