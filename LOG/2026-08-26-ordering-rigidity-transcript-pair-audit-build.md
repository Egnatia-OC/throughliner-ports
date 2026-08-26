# [HASH] — Ordering-rigidity audit of two frustrating sessions: ten findings, no clean pass on either transcript

The audit you asked for after a pair of sessions you described as a very
frustrating experience. Your framing was the lens, and it is worth restating as
you gave it: there is no point enforcing order inside the same session — the user
needs to be warned, but they shouldn't have to swear at Claude to be able to get
things done. You widened it at the same opening with a second lens, the release
failure: why, after two planning sessions had settled the pick with Fable, did an
untested build ship as v1.21.0, and where in the transcripts did the recorded
decision get lost.

Both transcripts were read end to end after a preprocessing pass wrote
conversation-only files to the scratchpad. Neither produced a clean pass.

**The first lens found the shape you predicted.** Four findings are enforcement
where a warning would have served, and the sharpest is that the run withheld two
approved Discord drafts across four of your turns, answering each ask with
sequencing, until the anger was explicit. Underneath it sits a defect that fired
earlier and silently: the walk-through pass dropped four `[user]` items as a batch
on its own judgment that their preconditions were unmet, presenting none of them.
Its own words — "I didn't put these to you individually because every one of them
opens on a step conditioned on the release being published" — describe a filter
the walk-through branch does not have. A third finding is that the records then
called all six items "deferred" when you had deferred two, crediting you with
decisions nobody asked you to make.

**The second lens traced the release failure to one sentence.** The sequence
recorded on the release item was: build closes, rezip, a planning run on that
rezip, a patch build, **rezip and reinstall**, release last. The build run wrote
instead that "what stands between here and the release is a rezip of this patched
build plus a reinstall — which is part of the release ritual anyway." It is not:
the ritual reinstalls the build it has just published, which is after the fact and
soaks nothing. That is where the pre-release soak was lost. Two further findings
sit around it — your instruction said "as planned" and the plan was never
re-opened, and the release ran after the close outside any skill, so the item
carrying the decision had no reader at the moment it was executed and was never
closed.

The remaining findings are smaller: `[freeform]` recommended against its own
definition and corrected by you twice from the docs, the queue mover run three
times to place the readiness marker with its usage read only afterwards, and the
wrong draft shown as the channel's first entry.

**One capture is not a finding.** You directed, during the same beat, that audit
findings should be written unapproved rather than approved at the point of write,
so the run carries on and the single evaluation happens at processing. Filed as
[audit-captures-need-no-write-time-approval]; it repeals this procedure's own
present-and-wait step, which is the step that produced the double evaluation you
were objecting to.

**Files touched:** none — an audit. Read:
`d3f8b9c7-62e2-40ea-9fb2-5f4559f03d61.jsonl` and
`04ea9e77-fd46-4bed-83a8-60e936b66273.jsonl`.

**Routed to Captures:** walkthrough-answers-request-with-sequencing,
user-items-batch-skipped-on-precondition-judgment,
deferred-recorded-for-items-never-offered, release-ran-outside-any-skill,
as-planned-accepted-without-rereading-the-plan,
pre-release-rezip-dissolved-into-the-ritual,
expedite-release-item-stale-in-ready-region,
freeform-recommended-against-its-own-definition,
queue-mover-help-read-after-two-wrong-placements,
first-entry-draft-wrong-and-unverified,
audit-captures-need-no-write-time-approval.

**Approval outcomes:** all ten findings approved as-is, in one pass, with no
finding dropped or reworded.

Tick form: done, confirmed.

Rule gate: not needed — an audit edits nothing and authored no rule.

**Also worth recording:** one finding filed here,
[expedite-release-item-stale-in-ready-region], was spent within the same session.
It reported that the release-pick item was still cleared to run describing a
release that had already happened; that item was closed later in this run, so the
capture describes a state that no longer exists.
