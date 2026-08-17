# de2f5fc — The written-shape measurement was read at last, and five findings routed

The reading half of work whose building half shipped on 2026-08-15 and was then never read. It exists as its own item because a tool with nobody appointed to read it reported that every written shape had doubled, and nothing happened for three days — the output is even addressed to a reader who was never appointed.

Both modes were run: the distribution report, now carrying the pre-split baseline built earlier in the same run, and the new `--bands` mode.

The sharpest finding is that the bands shipped in this run will fire on the *typical* artifact in four shapes out of five. Captures run 329 against a 265 ceiling, work items 412 against 345, build entries 400 against 345, index lines 62 against 60; only plan entries sit under. So the breach action does not fire on an outlier, and will keep firing on nearly every write for as long as the corpus takes to come down. That is the cry-wolf shape this project has repealed measures for twice, arriving this time from the figures rather than the wording — and what needs settling is the transition, not the bands.

One finding was reframed by the user and is better for it. It was drafted arguing that a long index line costs a reader's patience, on a table-of-contents model. Her correction: the index is read by Claude, not by a human, and the human reaches the log by asking Claude to read it. So the cost is a fixed toll on every retrieve rather than a page someone skims past — at the current median the index runs about 37,000 words against about 24,000 at the band top. `skill-nonspecific-rules.md` already states that the index is Claude-facing; what it does not state is this cost model, which is the argument the band actually rests on.

One finding is a pass, recorded because a pass is a finding: the pre-split baseline corroborates the bands, and the earlier estimate of that era was wrong on the low side.

**Files touched (read, not edited):** `resources/measure_written_shape_length.py` output in both modes, over `QUEUE.md`, `LOG/log.md`, `LOG/log-v*.md`, the per-entry `LOG/` files and `LOG/index.md`.

**Routed to Captures:** `[bands-fire-on-the-median-artifact]`, `[index-line-length-is-a-toll-on-every-retrieve]`, `[plan-entry-split-action-underspecified]`, `[work-items-accrete-past-their-band]`, `[pre-split-baseline-corroborates-the-bands]`.

**Approval outcomes:** four findings approved as-is; finding 2 reworded on the user's correction about who reads the index, then approved.

**Rule gate:** not needed — an audit authors nothing and amends nothing.

**FAQ:** not needed because an audit files captures and changes nothing a user does.
