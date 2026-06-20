# [HASH] - plan.md + plugin-behaviour.md: rewrite the parked-staleness review as its own run-not-skimmed step with an anti-nag stamp

The parked-staleness review was buried as a clause inside a [SILENT] scan, so it got skimmed - 16 parked items had piled up unreviewed (36% of the queue). plan.md now lifts it into its own Parked-shelf review step covering only Parked: (trigger-less) items, evaluated silently with only genuinely-stale ones surfaced. plugin-behaviour.md adds the anti-nag mechanism: a keep decision stamps the item Reviewed <date>: keep, suppressing re-surfacing until an interval elapses or a new staleness signal appears, so a still-valid item that merely looks stale is not re-asked every session.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/plugin-behaviour.md

**Routed to Captures:** none
