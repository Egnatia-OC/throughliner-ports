# 8697a79 — Build [plan-work-line-procedure] — /plan and done-plan rewritten onto the work-line model

Second build of the queue-redesign branch, consuming the definitions [work-line-behaviour-defs] shipped in the same session. plan.md was built around capture-processing with promote/park/drop routing, dependency tracing, unpark and parked-shelf scans, and a Build/Test/Audit batch-structure section — most of which the new model deletes. Under the new model /plan does two things: it reads unprocessed work with the user and, on agreement, moves each item into Processed or deletes it; and it maintains the order of Processed work and the position of the one cleared-to-run line.

plan.md changes: Step 1 now reads the Processed and Unprocessed sections plus SPEC, with the unpark scan, parked-shelf review, deferred-test roll scan, and plan-marker read all removed; the plain entry question stays. Step 2 processes Unprocessed one item at a time — present, discuss, and on agreement either keep (move the line into Processed, Claude placing Claude-work by judgment and reporting placement, user-work placed where the user agrees) or delete it; promote/park/drop, the dependency scan, the downstream-impact/structural-rule scan, and the routing gate are gone, while the provenance label, `_plan.md` as the resumable state file, the view-in-doc pointer treatment, and the wind-down re-scan are kept. Settling who does the work (`[user]` marking) folds into the keep decision. The old Step 3 (batch structure) was removed entirely — a processed line is just work with rationale and a slug — and the old Step 4 close renumbered to Step 3: it keeps the SPEC-in-sync gate and the cleared-to-run line positioning (renarrated to the greenlit-vs-still-settling boundary the new model uses) and drops the dependency-graph walk.

done-plan.md moved in the same batch because its close-out coherence backstop read the `Depends on:` headers this redesign removes: that dependency-graph gate and the accepted-red-flag LOG line are gone, while the SPEC-sync hard gate and the cleared-to-run confirmation stay (the latter renarrated). The LOG-entry template and the recommend-next scan were recut to work-line vocabulary (kept/deleted rather than promoted/parked/dropped; unprocessed-work overlap rather than unprocessed-Captures-vs-top-batch). The FAQ template dropped the batch-structure, capture-as-headings, and Parked entries, gained a `[user]`-marking entry, and had the idea-capture entry reworded; the index was updated to match.

Known residual, left deliberately for a later templates batch or the pre-push consistency sweep (not in either batch's stated FAQ obligation): four FAQ entries still describe dependency machinery removed across these two batches — dependency tracing ("read through my files first"), out-of-order/dangling, circular dependency, and the tidied-up-queue met-dependency maintenance — and the Deferred-tests FAQ entries and section remain (they're removed only in [fresh-queue-clean-break]). This is part of the phased redesign captured as [remaining-redesign-batches]; consumers see none of it before the redesign is pushed.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
