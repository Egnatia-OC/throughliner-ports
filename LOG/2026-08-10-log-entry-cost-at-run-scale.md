# 94bba66 — LOG entry depth is now decided per item; one entry per built item stays unconditional

Captured by the user 2026-08-09 — they stopped a close part-way through and asked
what the purpose of the process was, on a run that had built twelve items.

`done-build.md`'s entry step now states both halves. One entry per built item is
unconditional however long the run, because a work item's queue text is *consumed*
when it builds — /next removes it — so afterwards the entry is the only surviving
record of what the work was for. Depth is judged per item: full where the reasoning
was contested or an alternative was seriously weighed, short where naming what
changed exhausts it. Per item, never by run size — a twelve-item run can still hold
the session's most contested decision.

**The rejected option, recorded so it is not re-proposed.** A single combined entry
per run with per-item sections is the cheapest and was declined: the retrieve path
is "search the index, then open the matched entry", so combining trades away
per-slug retrievability — the exact property the entries exist for. Cheapness is
not sufficient reason to break the retrieve.

The rule was written when a run was one to six items; the run that built this
shipped nineteen, and applied the new depth judgment to its own close — this entry
is one of the short ones.

**Files touched:** `plugin/si-plugin/docs-b/done-build.md`.

**FAQ: not needed because** the user sees the same one-entry-per-item structure in
LOG/ either way; what changed is how much prose each carries.

**Routed to Captures:** none from this item.
