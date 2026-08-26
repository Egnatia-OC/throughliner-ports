# [HASH] — Walkthrough-heading patch kept and cleared first: the generator's label match widens and its halt message stops blaming the item

From a consumer project's mailed report, routed at this session's opening: an approved seven-step walkthrough never reached a run because its headings read `Walkthrough — part one:`, which the generator's punctuation-immediately-after-the-word match drops silently, and the run's message then says the item carries no walkthrough at all — two sessions lost to a walkthrough that was never missing. The mechanism was read before designing: the copy runs from the label line to the entry's end, so a word-boundary match carries their multi-part shape whole. The fix sits at the mechanism rather than as an authoring rule in plan.md — code that accepts the shape leaves such a rule policing nothing. Cleared first so it rides into today's beta release.

**Queue changes:** capture filed from mail, kept with a build block, cleared at the top of the ready list.
**Work processed:** kept — [build-view-walkthrough-heading-mismatch].
