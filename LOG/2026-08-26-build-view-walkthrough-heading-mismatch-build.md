# [HASH] — Walkthrough label match widened to accept a qualifier, and a mislabelled block now says so rather than claiming none exists

The generator required punctuation immediately after the word `Walkthrough`, so a two-part label — `Walkthrough — part one:` — matched nothing and the view told the run no walkthrough travelled. The fix sits at the mechanism rather than as an authoring rule in plan.md, which is the disposition the item carried: code that accepts the shape leaves such a rule policing nothing.

Two changes. The label pattern now accepts the word followed by an optional qualifier and then its colon; the bare-word arm still requires a `.` immediately, deliberately left narrow, because widening that arm the same way would swallow an ordinary sentence opening with the word. And where no label matches but a line beginning with the word exists, the message names the mislabelling instead of asserting the item has no steps.

That second half turned out to matter more than it looked. The AFK-cats transcript pair, audited later in this same run, shows the old message in use: a build told the user an item carried no written walkthrough at the moment its own planning session had just sharpened one into ten numbered steps. The claim blamed the queue, so a user reading it would have gone looking for something already there.

Files touched: `plugin/throughliner/scripts/generate_build_view.py`
Routed to Captures: none
Rule gate: not needed — generator code, no method rule text.

Verified by driving the generator over a four-item fixture in the session scratchpad — a split label, a plain label, a mislabelled block and an item with no walkthrough at all — and by `test_build_view.py` passing. Depth: short. Ticked as done, confirmed.
