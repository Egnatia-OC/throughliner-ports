# f8dbe10 — plugin-behaviour.md's retirement processed into a build, and the stopped run's six machinery bugs consolidated into a hand-driven freeform brief

This planning session settled two things the previous session left open, and the second
reversed a decision made an hour earlier in this same session.

**The doc's retirement, processed.** The 2026-08-10 shortening session ended with the user
rejecting `plugin-behaviour.md`'s founding premise and calling for its retirement; the
forward advisory carried that into this session and it was taken first. Claude argued
against full retirement and lost the argument on the merits, which is worth recording
because the losing argument was the obvious one. The objection was that a large share of
the doc's rules fire in ordinary conversation with no skill running, so distributing them
into skill docs would leave them loaded by nothing. The user's answer: there is always a
skill running. Checking that, a skill doc once loaded stays in context for the rest of the
session, so the gap is not "no doc is loaded" but "a different doc is loaded" — and the
project's own captures on the post-close tail and on informally-driven verification both
prescribe *routing into a skill*, meaning the residue was already being closed from the
other end. What survived of the objection is narrower and is recorded on the work item: a
rule genuinely used by all four skills, if distributed, becomes four copies that can be
edited apart, which is the same duplication defect the user has already approved repealing
in five other places. That points at one shared fetched doc rather than at keeping an
always-loaded one.

**Research was run before the decision, at the user's request, and it corroborated them.**
The user asked whether anyone else had built an always-loaded universal behaviour document
requiring this level of maintenance, believing they had invented it and that it was
unsound. Findings are filed at `resources/research/universal-behaviour-doc-prior-art.md`.
They did not invent it — `CLAUDE.md` and `AGENTS.md` are the same artifact and the
accretion failure is documented across the ecosystem in terms that match this project's
history closely. But the published remedy is a small file plus on-demand loading, never a
larger maintenance apparatus; and the admission gates, instruction counts and compliance
sweeps this project has grown around the doc have no prior art at all. The honest reading,
recorded in the research file, is that the maintenance regime is a symptom of the file
having been allowed to reach a size where a rule can hide in it. One finding bears directly
on the build and is written into the work item: splitting one always-loaded file into
several always-loaded files saves nothing — only fetching does.

**The naming question, which the user treated as the load-bearing part.** Their first cause
for the doc's failure was that its title does the filing: "plugin behaviour" names a
category broad enough to swallow any rule. Several candidates were worked through, and the
principle that settled it is that the name should state a *test* rather than a category,
because a category attracts filings and a test repels them. The user chose
`skill-nonspecific-rules` — checkable against a list of four skills in a way "behaviour"
never was.

**The reversal, and it is the more important half of the session.** The six bugs exposed by
the stopped /next run (`d632d6a`) were first processed as five or six ordinary work items
cleared for /next to build. The user rejected that immediately after approving it, on a
point Claude had missed entirely: four of the six bugs are *in the machinery /next uses* —
the queue mover, the scope-lock's cut-into-`_build.md` step, and the queue lint — so
building them through /next means running the broken mechanism to repair itself. They were
consolidated instead into a single freeform brief at the top of the queue, to be driven by
a session pointed at it directly and closed with /done. The brief states plainly that
nothing mechanically prevents /next from picking it up and that the protection is simply
that the user will not invoke it — an honest limit in the file rather than an implied one.

The consolidation consumed seven captures, so each fix carries its own finding, evidence
and settled disposition in the brief rather than a pointer to a deleted item. Two are
deliberately excluded and left in Unprocessed because they need a decision before anything
can be built: the compounding-rationale item, whose two obvious remedies are both already
spent, and the self-authoring word ceiling.

**A live instance found during the session, folded into the brief rather than filed
separately.** The queue mover script aborts on the entire file when it meets the forward
advisory's slugless heading, so no queue move of any kind can run while an advisory is
present. Three approved deletions and seven consolidations had to be done by hand with the
editing tools — precisely the transcription exposure the mover exists to eliminate. That
sharpens an existing capture from "the advisory looks like work" to "the advisory disables
the queue tooling", and it is now fix 3 in the brief.

**Ordering.** The freeform repair sits above the extraction deliberately: the extraction is
an ordinary doc restructure /next can run, but only once the mover and the scope-lock are
sound, since /next's own queue removal is one of the broken parts.

**Queue changes:** three completed audit findings deleted from Unprocessed
([captures-timing-prohibition-only], [communication-bullets-should-subordinate],
[anti-invention-rules-stated-negatively-and-twice], all three built in the preceding
shortening session and marked ready for removal); two new items added at the top of
Processed above the cleared-to-run marker; seven captures consumed into the freeform brief
and removed from Unprocessed; the consumed forward advisory cleared. The cleared-to-run
marker did not move — both new items landed above it. No reorder was warranted.

**Work processed:** kept — [retire-plugin-behaviour-doc] as
[extract-skill-nonspecific-rules]; [shell-write-guard-points-at-wrong-mover-path],
[mover-path-hardcoded-in-plan-md], [advisory-indistinguishable-from-work-item],
[blocked-by-lint-blind-to-in-flight-items], [build-md-holds-the-only-copy-of-unbuilt-work],
[next-per-item-queue-removal] and [design-item-reaches-next-fix-lost-to-revert] all
consolidated into [queue-machinery-repair-freeform]. Deleted —
[captures-timing-prohibition-only], [communication-bullets-should-subordinate],
[anti-invention-rules-stated-negatively-and-twice].

**Routed to Captures:** [resurrect-freeform-sessions] — the user's call to revive freeform
as a first-class concept, now that they are confident enough in Claude Code to handle it;
the gap that surfaced it is that this session's freeform brief had to say "don't run this
with /next" in prose because nothing can mark an item as not-for-/next.
[lifecycle-design-may-be-the-wrong-answer] — the prior-art research puts a prior question in
front of [rule-lifecycle-system]: how much lifecycle machinery is load-bearing once the
artifact it was built to govern has been retired.
