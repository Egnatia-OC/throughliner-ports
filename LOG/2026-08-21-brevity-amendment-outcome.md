# [HASH] — the audit that reads the brevity measurement, filed in the same session as the tool and held on a host-side dependency

Filed alongside [transcript-output-measurement] because `plan.md` requires it: where an item's build produces a tool that measures or reports, the audit that runs it is filed in the same planning session, placed immediately after. A measuring build that ships alone completes, leaves nothing outstanding, and the step that reads its output is never written down.

**What it reads and what it must not do.** The instrument, over transcripts from before and after [brevity-instruction-for-the-5-series] ships, reporting the difference. No pass or fail: there is no target, so there is nothing to declare against, and the finding is the direction and size of the change — including "no detectable change" where that is the answer.

**Held below the readiness line, and the dependency is host-side.** A shipped rule reaches a session only after a rezip and an app restart, so this cannot resolve in the session that builds the amendment. It carries `Blocked by: [brevity-instruction-for-the-5-series]` and its prose states that the wait is for the reinstall rather than only for the build.

**The audit is also the instrument's delete-time.** The close that records it removes `resources/transcript_output_length.py`, which carries that delete-time under the temp-file rule. The audit itself edits nothing, as an audit never does — the deletion is a close action recorded in the same entry.

**One limit stated in the item rather than discovered by whoever runs it:** an after-sample taken before a rezip measures the old rules, so the audit says which installed build each sample came from.

**Queue changes:** [brevity-amendment-outcome] written into Processed below the readiness line, naming its blocker.

**Work processed:** kept — [brevity-amendment-outcome], held.

**Routed to Captures:** none.

Rule gate: not needed — no rule is authored or amended. This applies an existing requirement that a measuring build's output gets an audit filed alongside it.

FAQ: not needed because the audit is host-only work on a script that does not ship.
