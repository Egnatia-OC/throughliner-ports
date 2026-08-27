# 32675a3 — The queue mover's report is read before continuing, and no retry is blind

The mover prints what it moved and where the readiness marker ended up. That
report was going unread, and a second run fired on a guess can compound the first
rather than correct it — which matters here because the marker's position decides
what a whole run builds.

The clause sits with the existing mover hazards, where the `--position BOTTOM`
trap is already documented: read the report after every run, confirm the marker's
stated position matches the intent, and on a mismatch read the tool's usage before
attempting anything else.

**Two widenings were refused on the item.** Read-the-usage-first on every mover
run — that taxes routine moves the report already confirms. And widening the
general verify-before-handing-over rule — this is the mover's own hazard, and the
capture drew that boundary itself.

**Files touched:** `plugin/throughliner/docs/plan.md` — the mover guidance. The
verify-before-handing-over rule's text is untouched.

**Routed to Captures:** none.

**Exercised the same session**, roughly thirty times: every item removed from the
queue in this run printed a report, and several carried consequential notes — held
items whose blockers had just shipped, and prose citations left pointing at work
no longer in the queue. Reading them is how those were noticed at all.

Rule gate: run — amendment to plan.md's mover guidance, parent named; the general verify rule unchanged; nothing evicted.
