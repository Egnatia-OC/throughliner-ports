# [HASH] — A Claude-runnable check blocked by a circumstance of the moment gets a row in next-build.md's table, and the migration checklist's wrapped condition is reflowed

Filed 2026-08-13 by Claude at the opening of a /next run, from a message the
Understudy project left in this project's INBOX.

**What they reported.** A thirteen-item run had built eight items whose
verification needed the app visible on screen, and each screen capture stole window
focus from the session their user was working in — so she asked for the on-screen
checks to be parked and the run to carry on. There was nowhere designed to put
them: the checks are not `[user]` work, because Claude can run every one and they
were blocked only by a circumstance of the moment; they are not captures, because
the items were already processed and mid-build; and they are not below-the-line,
because nothing in the queue blocked them. An ad-hoc note was invented inside the
build working file, which survives only until the close deletes it.

**The sender explicitly did not ask for a mechanism**, noting that inventing a
fourth work-item state is the move the rules warn hardest against, and that the
useful output might be a sentence saying what to do when it happens. That framing
was respected rather than treated as modesty.

**The site was already half-built.** `next-build.md` carried a two-row table — a
check Claude can run is just building, a check needing the user is a `[user]` item
— with no row for the third case, which is why a build meeting one invents
something. The third row needs no new state: the check stays outstanding in the
run's own working file, is retried before the close, and if the circumstance still
has not cleared the close files it as a capture. Both mechanisms already existed.

**The other half of the report was a doc-comprehension finding, not the fix she
asked for.** Their user called the rule converting a deferred test into a `[user]`
item nonsensical, on the ground that tests are not necessarily user work. The rule
was never saying that. Inside its fenced block the condition wrapped: `a deferred
test only` on one line and `the user can run` on the next. Read whole it says "a
deferred test only the user can run" — correct and consistent with the rest of the
method; read as it rendered, it appeared to convert every deferred test into user
work. She was right about what the doc communicated and wrong about what it
intended, so the fix is a reflow rather than a change to the rule.

**One paragraph was written and then cut on the purpose-clause test** — deleted,
the new row still applied correctly, so it was rationale: the row needs nothing
built because the working file already tracks outstanding work and filing at the
close is what the built-but-unverified rule already does. Second time in this run
that the test caught a why-paragraph at the moment of writing rather than after.

**Rule gate: run** — the reflow authors nothing; the new row is an amendment,
subordinate to an existing two-row table, sharing its grammatical form, no
complete sentences. Nothing evicted, because nothing was added.

**Files touched:** `plugin/throughliner/docs-b/migrate-checklist.md`,
`plugin/throughliner/docs-b/next-build.md`.

**Routed to Captures:** none. A reply to Understudy is owed on both halves —
particularly the second, where their read of the doc was correct and their read of
the rule was not.
