# Discord post: the spec inversion — [discord-post-spec-inversion]

Walked through and completed 2026-08-14, during the /next run that built sixteen
items ahead of it. The post is written; Alex posted it.

## What the item was

A `[user]` line: Claude drafts a Discord post, Alex edits and posts it, because
Claude has no route to Discord. Kept as `[user]` on a recorded decision rather
than a judgement call — the over-tag check names no tool to try, and the two
halves were deliberately not decomposed into a build item plus a user step,
because the draft needs live editing and is one interactive exchange rather than
a build with a hand-off bolted on.

The angle was Alex's: how backwards the project's spec-driven development was,
and how it now runs the right way round.

## What was done in the walk-through

**The precondition was confirmed rather than re-checked.** The standing rule is
that every claim in a post is true of the installed plugin at the moment it is
posted. [spec-is-write-only-during-builds] shipped on 2026-08-12
(`LOG/2026-08-12-spec-is-write-only-during-builds.md`), and the installed host is
1.20.0-test3, so every claim in the draft describes behaviour that is live.

**Claude drafted inside Discord's 2,000-character limit.** The first draft came to
1,549 characters and carried Alex's own words for what the old gate did — that it
ends up functioning as a place for the model to justify whatever it did within a
scope that can still vary — lightly trimmed to fit the sentence around it.

**Alex questioned one paragraph, and the question was worth more than the
answer.** The draft closed on the research finding that no length standard for a
spec exists in any source, "which is why the size question was measured rather
than argued". She asked whether that was another bare number of the kind the rule
gate bans.

It is not, and the distinction is the one the derivation rule turns on: the gate
bans a **limit** stated without a stated derivation, and what happened here was a
**measurement** of an artifact that already existed — SPEC was 6,159 words, of
which the editing-state contract was 1,035 (`LOG/2026-08-12-plan.md`,
`resources/research/spec-document-standards.md`). No threshold was declared and
none exists. The measurement is what led to moving the contract into its own
file. Measuring rather than inventing a figure is the rule working, not an
exception to it.

**She then cut the paragraph anyway, on a better ground than the one Claude was
defending:** it does not describe the value of SPEC, so users do not care about
it. The final post is 1,231 characters.

## What the post says

That the method cited spec-driven development to justify a gate doing the
opposite of what SDD says; that /next now reads SPEC once at run start and checks
each item against it as it is built; that a contradiction stops the run and names
the SPEC sentence in plain English, with the user deciding which is wrong, rather
than SPEC being rewritten to fit; that a build establishing new product truth
asks first and edits SPEC in the same commit; and that the close-time sync is
gone from the build, because a sync on a document the build never read had
nothing to compare against.

## What came out of the walk-through that was not the post

Two captures, both from Alex's questions after the draft was approved.

**She proposed deleting `EDITING-STATE-CONTRACT.md`** as vestigial MANIFEST
material. Claude pushed back on the premise and was half right and half wrong,
and the half that was wrong matters more.

Right: it is not MANIFEST material. It documents a shipped feature — the hooks
write a marker before every editing-tool call and clear it after — and Understudy
is a live consumer, its `src/main.js` reading `.throughliner/`, scanning every
`editing-*.json`, and applying the published reader rule that editing is
happening if any marker is active and fresh.

Wrong: Claude concluded from that consumer that a delete was "off the table".
Alex's correction defeats it. What Understudy has is *code* that reads the
markers; Understudy's Claude can read the hook that writes them, and that source
is strictly better — the marker-writing function **is** the format, so it cannot
drift, where the document can and has nothing checking it. Her words for it: it
is probably way more accurate too. The document would only be load-bearing if
Understudy could not reach this repository, and it can; the v2 format change in
fact travelled by INBOX message rather than by anyone reading the contract.

Filed as [editing-state-contract-status], carrying her three questions: whether
the dependency should be visible from both ends, when the document is maintained
or whether it is quietly decaying, and whether a published field-level contract
is standard practice or an invention duplicating code already in the repository.
The third is load-bearing after her correction and turns on an external fact, so
the capture records that it needs a web search rather than a judgement.

**And the audit's follow-up.** After approving the eight rationale-cut findings,
she asked for a capture describing an audit that might pick up more. Filed as
[rationale-audit-second-pass], naming the shapes the first pass structurally
could not see.

## Notes

The walk-through's LOG entry should have been opened when the walk-through
started, with each action appended as it happened; it was written at the end
instead. Recorded rather than smoothed over — the requirement exists so a crash
mid-walk-through leaves a partial record, and writing it at the end is exactly
the failure mode the rule names.

Completion is known the third permitted way: Alex said she posted it. There is no
observable check available, since Claude cannot see Discord — so nothing was
checked against the world here, and this entry does not claim otherwise.
