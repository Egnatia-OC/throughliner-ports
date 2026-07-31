# 29ba751 - plan.md: fold the recommend step into the action when the user already agreed to promote during the interview

In /plan's capture loop the standalone recommend-and-wait re-asked a route the user had already agreed to during present-and-interview, adding a round-trip with no added judgment. The fold is scoped to promote only, because promote is followed by the draft-approval step the user still owns - park and drop are terminal with no later approval, so they keep the recommend step. Fires only on explicit in-interview agreement; an open or ambiguous interview runs the recommend step as before.

**Files touched:**
- plugin/si-plugin/docs/plan.md

**Routed to Captures:** none
