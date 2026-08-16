# [HASH] — A build producing a measuring or reporting tool now files the audit that runs it

The gap was a missing rule, not a missing mechanism. Ordering a dependent audit after its tool already works by placement, and `Blocked by:` exists for the cases that need it. What was missing was anything saying the audit must be filed at all — so a measuring build completes, the queue shows nothing outstanding, a session record says the item shipped, and the step that reads the output was never written down. Nothing detects the absence of a step that never existed.

Two recorded instances rather than one. `measure_written_shape_length.py` shipped on 2026-08-15 and was read by nobody until a user question three days later. And `resources/rule_signals.py` ran for its entire life with nothing invoking it, which `CLAUDE.md` records as exactly that.

The pair carries no `Blocked by:` line, and that is deliberate: a dev tool run directly is live the moment it is written, so one run can build the tool and then use it. Placement carries the order, and a holding field would push the audit below the readiness line and stop it running at all.

The ripple that had to ship with it: `done-plan.md`'s close moves `[audit]` and `[user]` lines to the end of the cleared region, which would separate a tool-paired audit from the tool it runs — and the close happens after `/next`, so the separation arrives in time to break the *next* run rather than the current one. The end-preferred reorder therefore now excepts an audit sitting immediately after the tool item it reads. Found by tracing this item's own placement, which is what the ripple rule exists to catch.

The rule proved itself inside the same run: the audit paired with `[measurement-excludes-legacy-logs]` ran immediately after it and filed five findings that would otherwise have waited on somebody noticing.

**Files touched:** `plugin/throughliner/docs-b/plan.md` (keep-step clause: where a build produces a measuring or reporting tool, the audit that runs it is filed in the same planning session, placed immediately after), `plugin/throughliner/docs-b/done-plan.md` (end-preferred reorder excepts that pair).

**Routed to Captures:** none.

**Rule gate:** run — admitted as a clause on `plan.md`'s existing keep-step, which already settles an item's flavor and placement, plus an exception on `done-plan.md`'s existing end-preferred reorder; no freestanding rule and no always-loaded slot spent. Nothing evicted. Shipped rather than host-only: a consumer can build a reporting tool and hit the same gap. Failure evidence is the two instances above.

**FAQ:** updated — a new entry, *"Claude queued an audit right after a piece of work. Why two items instead of one?"*, since a consumer now sees a second item appear in their own queue alongside a measuring build.
