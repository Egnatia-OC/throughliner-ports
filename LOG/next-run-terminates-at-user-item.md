# [HASH] — next.md: /next hands over `[user]` items without terminating the run

Reworked /next's run model so a `[user]` handover no longer ends the run. Previously the run was defined as the cleared items "down to — but not including — the first `[user]` item," and Step 3 said "Don't build past it" — so a cleared order like [Claude-A, user-X, Claude-B] built only A, handed over X, and stranded B though it was cleared. The design intent (user, 2026-07-30) is that stopping at `[user]` was only ever meant to keep contiguous Claude blocks from being split mid-stream — never to terminate a run whose principle is "run continuously wherever possible."

The run is now bounded by the `--- Cleared to run above this line ---` marker alone, and *includes* any `[user]` items among the cleared work. Non-termination is achieved by a two-pass split rather than new logic: Step 2 moves the run's Claude-work items into _build.md and builds them all first; the `[user]` items stay in QUEUE.md and are handed over in a final pass (Step 3). This falls out of the existing _build.md/QUEUE split — so /next gains no reorder logic (that stays the /plan close's job). A strict top-down alternative (hand over mid-run, then continue) was rejected: it would still interrupt the Claude block for the handover PROMPT, where the two-pass split keeps the build contiguous. Step 2.4 clarified only Claude-work items are removed from QUEUE (a `[user]` item extracted into _build.md would strand, since _build.md is deleted at close); the "top item is `[user]`" early exit became "all cleared work is handovers"; the FAQ's build/audit-flavors entry had its now-stale "stops to hand over at the first `[user]` item" line corrected.

**Files touched:**
- plugin/si-plugin/docs/next.md: Step 1 run definition, Step 2.4, Step 3 handover branch + intro, copy-discipline heading
- plugin/si-plugin/templates/faq-template.md: build/audit-flavors entry

**Routed to Captures:** [multi-handover-presentation] — how /next presents multiple `[user]` handovers at a run's end (one at a time vs bundled)
