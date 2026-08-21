# [HASH] — The build view now emits `Runs alone`, so a run can see its own second bound

A run reads the generated view and never QUEUE.md. `Runs alone` sits outside the `--- Build block ---` delimiters, so the projection dropped it — and /next reads that literal to decide where a run stops. The bound existed in the queue and was invisible to the only thing that acts on it.

The generator now emits it on its own line beside the item's block, tolerating the bold form for the same reason the queue lint does: `**Runs alone**` is the ordinary Markdown instinct, and a marker that silently fails to match is worse than one written two ways.

Emitting it only in the by-name listing stayed refused — the run's bound belongs with the work the run builds.

`next.md` needed no change; it already instructs stopping on the marker.

Noticed during this session's own pre-flight, which had to grep QUEUE.md directly to confirm no cleared item carried the marker.

**Files touched:** plugin/throughliner/scripts/generate_build_view.py, resources/testing/test_build_view.py
**Routed to Captures:** none
Rule gate: not needed — a generator emits a marker it was dropping; no method rule changes.
