# 3b094b5 — The reorder narration stops quoting two internal medians at the user

A compliance-audit finding on narration drift: plan.md's start-of-processing reorder directed the one-line narration to quote the section's line-count median and its first-seen median — two internal statistics with no user action attached, in text a non-coder reads at the start of every planning run.

The figures existed so the ladder's fixed membership stayed checkable, and that need is served elsewhere: both medians print in the digest's own output every run, which is where anyone checking would look. So the narration drops them and names the order picked in plain words instead.

Live evidence from the same day, recorded at planning: that session's own order-line skipped the medians and nothing was lost.

The medians' actual job is untouched — they still fix which entries belong to the ladder's long-and-old and alternating rungs for the whole pass, read from the digest rather than from the narration.

Refused at planning: keeping the figures and rewording them into plain words. A statistic with no user action attached does not become actionable by translation.

**Files touched:** `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment removing an internal figure from user-facing narration; the digest printout is the named replacement for the checkability job. Nothing else evicted.
