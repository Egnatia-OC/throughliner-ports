# e5d169b — The growth report extends to the fetched procedure docs as their own group

Nothing measured the fetched procedure docs at all. `plan.md` alone is 226 structural statements — larger than the always-loaded corpus's 234 — and `done.md` 181, `setup.md` 126, `next.md` 124. The ceiling deliberately excluded them because they load only when their skill runs, but that exclusion was reasoned about when they were small.

`FETCHED_DOCS` now names eight documents and MEASURED reports them as a **distinct group**, with a statement count and direction of travel, no threshold and no verdict. At build time: 825 across the eight.

The grouping is the substance, not presentation. Redistribution to a fetched doc is how bloat gets hidden rather than cut — `resources/method-compliance-audit-checklist.md` says so in as many words — so a single combined figure would let text moved out of the always-loaded file read as a reduction. Two groups makes a relocation visible as a relocation, which mattered immediately: the same session moved the device-access rule from the always-loaded file into `next-build.md`.

A growth report with no threshold is the only form available. The item guessed as much on the ground that the compliance argument behind 150–200 is about competing for attention in every session and does not transfer to on-demand docs; that reasoning still holds and is now the second reason rather than the only one, since [board-reports-one-audience-not-two] found no defensible threshold exists for any document here.

`skill-nonspecific-rules.md` is named in the item's list of fetched docs but is deliberately **not** counted in this group: it is always-loaded and already counted above, and listing it twice would double-count the one file the report is most about.

**Files touched:** `resources/rule_signals.py`
**Routed to Captures:** none from this item
**Rule gate:** not needed — a reporting group added to a host-only script.
