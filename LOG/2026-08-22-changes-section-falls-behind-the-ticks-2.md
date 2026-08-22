# [HASH] — The Changes entry joins the per-item completion set as its fourth required write

The 2026-08-17 reconcile found a twenty-item gap: ticks, depth fields and index candidates all held because they are an enumerated set the close reads, while `Changes:` — described only as accumulate-as-you-go — carried almost nothing, costing the close its `Files touched:` source in exactly the fresh-session case the method designs for. The keep chose the per-item write over the close-side mismatch check, because detection at the close arrives when a crashed or fresh session can no longer fill the gap.

Built: the per-item completion step (next.md) now enumerates four writes — tick, depth field, index candidate, and the item's `Changes:` entry, files touched one line each, at the tick and never later — and next-build.md's close-notes section is repointed at that set rather than standing as a second, unenforced description. done-build.md's sourcing of `Files touched:` is unchanged and now fed per item.

Tick: done, confirmed — grep shows no remaining accumulate-as-you-go framing; the set enumerates four writes.

**Files touched:** plugin/throughliner/docs/next.md, plugin/throughliner/docs/next-build.md
**Routed to Captures:** none
Rule gate: run — amends next-build.md's per-item completion set, its named parent, from three required writes to four; subordinate to the existing enumeration, nothing evicted. Failure evidence: the twenty-item gap the 2026-08-17 reconcile found.
FAQ: not needed because this is run bookkeeping; nothing a user does changes.
