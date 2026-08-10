# 10d6474 — Rationale growth measured across 186 items: processing roughly doubles a work item, and the growth is concentrated

An `[audit]` item, run against git history rather than by watching future sessions
— the history already holds each capture's original text and the processed text
that replaced it, so the evidence for the past several weeks existed and only
needed reading.

## Method

A script walked every commit touching QUEUE.md since 2026-07-20 (113 commits),
parsed each `#### … [slug]` block with its section, and recorded three word counts
per slug: its first appearance in Unprocessed, its first appearance in Processed,
and its latest appearance in Processed. 186 slugs have both a capture form and a
processed form. Reproducible — the same script can be re-run later to see whether
any fix moved the number.

## What it found

- **Median growth factor 1.77**: median 290 capture words become 536 processed. In
  total, 59,216 → 107,795.
- **Concentrated, not uniform.** Long-tailed: worst case 17×, the top ten
  disproportionate, and roughly thirty items actually *shrank* during processing.
  So "processing adds" is not a property of processing — a minority does nearly all
  of it.
- **The worst grower was later cut by 56%.** [concurrent-session-support] went
  130 → 2,267 → 994 when a later session reworked it. The design survived.
- **Growth after processing is negligible**: 27 of 186 items, 1,815 words, against
  ~48,000 added at the capture→processed step.

## Why the fourth finding matters most

It contradicts a premise the queue has been reasoning from.
[invented-rationale-compounds-past-the-shipped-rule] describes rationale as
compounding, re-authored and added to at every stage. Measured, it does not: there
is one step where growth happens and the rest of the chain is nearly flat. Any fix
therefore has one moment to address rather than a pipeline, and the
re-author-forward design is not the leak it was suspected of being.

The third finding is the only one that speaks to whether the added words were worth
their cost, and for one item it says no — which suggests a lever nobody has
proposed: a rework pass over an already-processed item, where every previous
proposal tried to prevent growth at the moment of writing. Its bound is n=1.

## The limit, stated in the findings as the item required

Word counts measure volume and nothing else. They cannot separate reasoning Claude
produced unprompted from decisions the interview genuinely reached — which is the
question actually being asked — nor tell a rule holding from a session that
happened to write less. That limit is itself filed as a capture, because a number
in the record gets quoted later without its caveat, and these four numbers are
unusually quotable.

**Files touched:** none — an audit edits nothing. Read: QUEUE.md across 113
commits of git history.

**Approval outcomes:** all five findings approved as-is. None dropped, none
reworded.

**Routed to Captures:** [growth-measured-at-1-77x],
[growth-is-concentrated-not-uniform], [processed-items-compress-when-reworked],
[growth-happens-at-processing-not-after],
[growth-measure-cannot-separate-invention].

**FAQ: not needed because** an audit of the development project's own queue
history changes nothing a consumer sees.
