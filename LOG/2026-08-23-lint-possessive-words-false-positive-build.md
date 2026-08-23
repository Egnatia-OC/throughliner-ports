# [HASH] — Quote-claim lint narrowed to introducer shapes, so ordinary prose stops firing it

From a consumer project's mailed defect report. Three of their correct items were flagged because the prose said "her words" about a third party — items of the shape "ask how she put the question, and her words as closely as he can recall" — where obtaining the quote *is* the work. Two of the three already carried the origin credit the flag itself offers as an escape, and were flagged anyway. The sting in their report is the part that decided this: the flag could not be cleared by writing correctly, and the lint re-runs on every queue write, so it re-fired roughly ten times in one session. An advisory that fires permanently on correct text is one the reader learns to skim, which costs the check its real findings too.

The trigger now requires an introducer — the phrase followed by a colon, or the "in <possessive> own words" form — which are the shapes this project's own recorded failures actually took, while the consumer's sentence escapes both. The accepted miss is stated in the check's own docstring rather than left to be discovered: a colon-less bare claim now passes. That is the price of not flagging ordinary prose, on an advisory check whose alternative was firing forever on correct text.

**One coverage change the item did not anticipate, recorded because it is a real loss rather than a tidy-up.** The suite's two existing must-fire examples — "In your words, this should be done differently" and "Her own words settled it: the ordering was wrong" — fall outside both introducer shapes and no longer fire. They were replaced with the shapes the narrowed check does catch, keeping the project's own recorded third-person failure ("Her words:" over a paraphrase) pinned, and a new must-not-fire test carries the consumer's sentence. The dropped constructions are part of the accepted miss, not an oversight, but nothing in the item predicted them.

The deeper cause is noted and not fixed here: the check can only imagine a possessive naming the user, which is the single-user assumption already captured elsewhere as the GitHub-identity naming idea.

**Files touched:** `plugin/throughliner/hooks/post_tool_use.py` (new `QUOTE_CLAIM_INTRODUCERS`, applied in the quote-claim check; module and function docstrings state the accepted miss), `resources/testing/test_queue_lint_flags.py` (must-fire cases retargeted, new must-not-fire test, runner updated).

**Routed to Captures:** none from this item.

Tick: done, confirmed — the full lint suite passes, run as a plain script with `py`; both the must-fire and must-not-fire cases hold.

Rule gate: not needed — a hook script's match pattern was narrowed and no method rule text changed.

FAQ: not needed because a warning firing less often changes nothing a user does.
