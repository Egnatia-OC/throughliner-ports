# 32675a3 — `[freeform]` and `Runs alone` are assigned only against a re-read definition

The two uncommon execution markers were being reached for interchangeably. They
are rare enough that nothing keeps their difference fresh, similar enough in shape
to be confused, and each carries a consequence the other does not — so the
recorded failure cost the user two corrections at the moment ordering was being
settled.

The clause requires the marker's definition to be re-read in the same turn it is
assigned, with the recommendation naming why the work matches it. That costs one
look at two entries sitting a few lines above.

**The common markers are exempted in the text**, and the exemption is what keeps
this from spreading: no tag, `[audit]` and `[user]` are assigned constantly, and a
re-read requirement on them would be friction with no failure behind it.

**The contrast sentence was sharpened in the same pass**, because the old one
stated the difference in terms that did not survive contact with the confusion it
was meant to prevent. It said `[freeform]` is work /next must not build and
`Runs alone` is work /next should build alone. It now says `[freeform]` is work
done **without the method running it at all** — by hand, in its own session,
because the work is too large or because running it inside a run is the risk —
against `Runs alone`, which the method **does** build, in an isolated run.

**Dropping this as a recorded slip with no build was refused on the item**: the
clause is one line, and the failure had a price.

**Files touched:** `plugin/throughliner/docs/plan.md` — the disposition step.

**Routed to Captures:** none.

Rule gate: run — amendment to plan.md's disposition step, parent named; admission earned by the recorded double correction; nothing evicted.
