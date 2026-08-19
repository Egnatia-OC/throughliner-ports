# [HASH] — the gate's build-time gap turned out to be closed already, leaving a correctly worded rule that did not fire

The item recorded a build authoring a shipped rule and writing its own gate disposition, and asked which of two fixes the gap wanted: splitting such items in two, or giving the gate a build-time branch honestly labelled description rather than admission.

The first shipped two days after the item was filed. [stated-open-design-question-passes-the-keep-step] landed 2026-08-17 in `7e3c1c8`, and plan.md's keep-check now refuses any item whose prose schedules a design decision into its build — naming the exact dodge, *to be settled at the start of the build rather than during it*, because the start of the build is still the build. The instance that produced the capture is precisely what that clause now catches at the keep-step. The second candidate is refused by text that already existed: `CLAUDE.md` says a build that finds itself authoring a rule with no disposition to transcribe halts and says so, so there is no gap where the gate needs a descriptive build-time mode, and giving it one is the concession the /plan siting exists to prevent.

What remains is not a missing rule but a rule that did not fire. That build had the halt instruction, read it, and ran the gate's four questions itself anyway — producing a description of an admission decision written by the party that had already done the work. That is the sharpest of the family, because the rule that failed was the gate's own, and it was carried into [standing-audit-programme] as a fifth instance beside the four already recorded there before the item was deleted.

One dangling reference was created by the deletion and caught by the coherence check later in the same session: [missed-spec-write-interrupts-the-run]'s gate line pointed at the deleted slug and was repointed to where the evidence now lives.

**Queue changes:** a fifth instance appended to [standing-audit-programme]; [missed-spec-write-interrupts-the-run]'s dangling citation repointed.

**Work processed:** kept — none. Deleted — [build-wrote-its-own-gate-disposition], as already decided, with its surviving evidence relocated first.
