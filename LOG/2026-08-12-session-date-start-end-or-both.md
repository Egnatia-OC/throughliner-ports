# 16ed591 — Every date written at a close is the close date, and a session that spanned two days says so in one sentence

The method settled the filename prefix for a one-day session — the session date, written from the current date at close — and said nothing about a session that runs across two. That is not an exotic case: it is what happens whenever someone stops for the night or hits a usage limit and resumes in the morning, which is exactly what produced the question.

The larger half was unaddressed entirely. Dates written *into* the text — "processed 2026-08-12", "cleared 2026-08-12", "captured by you 2026-08-12" — are read later to judge staleness and reconstruct when a decision was made, and no rule governed them at all. In the session that raised this, Claude first stamped everything with the start date, then on noticing the calendar had moved restamped that session's writes to the close date for consistency: a defensible choice made on the spot with nothing behind it.

The convention is now one rule covering both. Every date written at a close is the close date — filename prefix and in-text stamp alike. Where a session ran across more than one calendar day, its record says so in one plain sentence. No format change, no second datestamp anywhere.

The why is two different arguments, and both are recorded because they do not share a reason. For the filename, its only job is the name sort: the close date already does that, a two-day session sorts correctly either way, and carrying both would lengthen every filename forever for an occasional case. For an in-text stamp, which is read for meaning, the close date is right because the stamp records **when the decision was made** — and a decision reached in a session's final hour was reached on the close date whatever day the session opened.

Two conventions lost. "Both" pays a permanent cost in every filename and every stamp for an occasional case, and makes each stamp ambiguous about what it asserts, so a reader must work out which date answers their question. "Start date only" goes stale the moment a session runs long, which is precisely the case being solved.

One thing that is coincidence rather than compliance: the /plan session that settled this opened and closed on the same day, so it matches the new convention by accident and is not evidence the convention works.

**Files touched:** `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none

Rule gate: not needed — a close-time convention stated where the close reads it, widening an existing rule from the filename to every date the close writes. Nothing added to the always-loaded set, deliberately.
