# [HASH] — A dispatching work item now records an observable return-check, and /next halts rather than walking the user through finished work

A `[user]` item said, in effect, "open the other project, have the signal format designed, then bring it back." That happened. The format came back and was filed as a fresh capture. But **nothing updated the dispatching item**, which still read "go and design it" — so running its walk-through would have asked for work already done.

**The general shape:** nothing in the method links a returned answer back to the item that requested it. A work item can dispatch a question outward; when the answer arrives it arrives as new material with its own life, and the requesting item is not a party to that. So the request stands unamended and reads as still-outstanding, indefinitely.

It was caught only because the wind-down re-scan happened to notice a contradiction between two things in the same session. That is luck, not a mechanism: a session later, nothing would have been holding both halves, and the next /next would have walked the user through finished work — which is exactly the failure the never-ask-if-it's-done rule *assumes cannot happen*, because it assumes an item's text is current.

**The counter the item carried is what decided the design, so it is recorded as a resolution rather than a warning.** The returning answer is usually filed by a different session in a different project, which cannot see this queue at all. That rules out the back-reference direction outright — a mechanism depending on the answering side remembering to look back will never fire. So the check lives on the **requesting** side, the only side that can run it.

Two clauses. `plugin-behaviour.md`'s `[user]` lifecycle, beside check-the-world: an item that sends a question outward records what its answer coming back looks like, as an observable check, written alongside its walkthrough. And `next.md`'s walk-through pre-flight gains a second check beside the capability one — if the answer appears to have returned, /next does **not** walk the user through it: it states what it found, leaves the item in place, and files it for /plan. **It halts rather than amends**, because amending a work item is processing and /next does not process.

The firing site already existed and needed no invention: that pre-flight already re-runs the capability check, justified as nearly free because the run is about to act on the tag. Same moment, same reasoning, same outcome shape.

**The limit, stated so it is not later mistaken for solved:** this only helps where the return is observable. Where nothing observable exists, the item still goes stale silently — the same deliberate gap the completion rule accepts, and better than a mechanism that pretends otherwise. **A second limit was found the same day and filed:** the fix is blind across projects, because the requesting item may live in a queue this project cannot see — [dispatch-return-check-blind-across-projects], observed live when a companion project asked for work that had already shipped.

**A boundary deliberately not crossed:** a cleared *build* item can rest on a stale premise the same way, and nothing checks that either. Folding it in would turn a two-clause fix into an open design.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/next.md`
**Routed to Captures:** [dispatch-return-check-blind-across-projects]
