# [HASH] — Added the symmetric don't-under-file `[user]` rule (failure mode: user-work evaporation) and rebalanced the walkthrough gate

The `[user]`-earning rule was written almost entirely as an anti-over-tag brake, while under-filing — dropping real user work into a live chat question that evaporates when the session ends — had no named failure mode at all, so Claude minimized the loud risk and walked into the silent one. Made the Captures Flavor marker a matched pair: added the don't-under-file rule with its own named failure mode, "user-work evaporation," stated as sharply as its mirror — genuine user work must become a `[user]` line, never a live question or a "separate work you'd do yourself" aside; when the "can Claude do this at all?" test returns no, the answer is to file a `[user]` line. Rebalanced the walkthrough gate so not-yet-fully-scriptable steps still file the line with a rough walkthrough (sharpened at the keep-step), rather than the description bar becoming a reason to withhold the line. Reinforced the same at plan.md's keep-step and in next-build.md's mid-build discovery routing. Rejected leaving the pro-filing rules buried where they were — that burial is exactly why under-filing recurred.

**Files touched:** plugin-behaviour.md, plan.md, next-build.md

**Routed to Captures:** none
