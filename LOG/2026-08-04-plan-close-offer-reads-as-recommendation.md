# f832385 — Reshape /plan's checkpoint into a two-sided either/or, with the last-item case worded so it can't collapse into "shall we close?"

From the method's first external user. At every checkpoint /plan presented its off-ramps, and the wording kept collapsing into "here's what's next — close out here?" That trailing question reads as a recommendation to stop, and the first-time user took it as the session being finished, repeatedly.

The diagnosis the procedure text supports: the fault is the *shape* of the ask, not its presence. The doc already required the ask to land as the message's closing bold question and already wrote the end-of-queue gate neutrally — but nothing said the alternatives must be worded as an explicit either/or, so statement-then-close-question is what it kept producing.

The first attempt at fixing it made things worse: a four-bullet menu at every checkpoint, which the user called excessive. The diagnosis that followed is what shipped. The four off-ramps don't all need *offering* — skipping an item and raising something else are always available in conversation, so reciting them each time teaches nothing and buries the ask. The only pair a novice misreads is carry-on versus stop. So: the next item in one line, then a single two-sided ask, with skip and raise-something-else named once at the session's opening instead. A real trial backs this rather than an argument — one session ran exactly that shape for thirteen consecutive items and it never once read as a nudge to stop. The session-start naming is the half still untested, and it is now written down rather than left implicit.

The gap the build had to close is the last item. There is no next item to name, so the two-sided ask has nothing in front of it — and an ask with nothing before it collapses straight back into "shall we close?", which is the exact failure being fixed. The final checkpoint of every session would have reintroduced it. That case is now worded explicitly, with continuing given a concrete face ("we can keep going — anything you want to capture or talk through — or stop here") rather than left as the unnamed alternative. The end-of-queue gate was aligned to the same shape.

Also settled: keep offering at every checkpoint. The capture wondered whether the off-ramps need offering that often; with the ask reduced to one line and two options the cost is negligible, and the user keeps a genuine exit at every step, which is the control the whole method is built on. The excess was the menu, not the frequency.

The ask shape is also stated once in the behaviour rules alongside the other response-shape rules, so it holds outside /plan too.

**Files touched:** `plugin/si-plugin/docs-b/plan.md` (Step 2's opening, the checkpoint, the skip-to-defer fold, the last-item case, the end-of-queue gate), `docs-b/plugin-behaviour.md` (the two-sided ask in Communication), `SPEC.md` (the Processing flow paragraph).
**Routed to Captures:** none.
