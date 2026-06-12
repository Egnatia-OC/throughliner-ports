# LOG entry — doc-crossrefs-by-name

## 9f1b80b — /next [doc-crossrefs-by-name]: cross-doc procedure-doc references converted to names; CLAUDE.md gains the authoring rule

Step-number cross-references between procedure docs break silently: adding, deleting, or reordering a step renumbers the rest, and a reference in another doc still resolves — to the wrong content. Observed at the [hash-backfill-as-hook] build, where deleting one pre-flight sub-step left three /done sub-docs and plugin-behaviour.md saying "Step 1.4" for a blocker gate that had become Step 1.3; that build caught them only because it chose to grep before renumbering, which no procedure requires. Two alternatives were weighed and rejected: a grep-before-renumbering process rule guards an empty set once this sweep lands and relies on a model recognizing mid-build that its edit renumbers; lint detection can't work at all, because a renumbered pointer doesn't dangle — it resolves, to the wrong content, and a lint can check that a reference resolves but not that it resolves to what the author meant. Names survive renumbering, so the rule — the procedure-doc twin of "locate by content, not line numbers" — is that cross-doc references name their target. Host-only: consumers never edit procedure docs, so the rule lives in this project's CLAUDE.md, not shipped docs. Within-doc references are exempt, since renumbering is visible in the file being edited.

The sweep found five cross-doc step-number references, all currently pointing at correct content (the prior build had fixed their targets) but still numeric — so the break would have recurred at the next renumbering. Three were the identical "(mirrors next.md Step 1.3)" in the recommend-next overlap scans of done-plan.md, done-build.md, and done-test.md, now "(mirrors the capture-overlap scan in next.md's pre-flight blocker gate)". Two were in plugin-behaviour.md: the Captures filing-time-blocker bullet's "/plan's Step 2 dependency-scan" (now "/plan's dependency scan") and the Unpark watch bullet's surfacing itinerary (now "/plan's read-state step … its capture-processing loop … /next's pre-flight blocker gate"). The verification grep confirms zero cross-doc step-number references remain under plugin/si-plugin/ — every surviving hit is a doc's own headings or same-file references, which stay by design.

**Files touched:**
- CLAUDE.md: Working conventions gains the cross-doc-references-by-name authoring rule (host-only, does not propagate via reinstall)
- plugin/si-plugin/docs/done-plan.md, done-build.md, done-test.md: overlap-scan line converted to the name-based form
- plugin/si-plugin/docs/plugin-behaviour.md: two bullets' step-number references converted to names
- QUEUE.md: batch removed at scope-lock
- LOG/git-add-safety-hook-gap.md + LOG/index.md: prior entry's hash placeholders backfilled to 61bfd2f at pre-flight

**Routed to Captures:** none
