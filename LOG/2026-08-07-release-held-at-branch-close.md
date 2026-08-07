# [HASH] — Departure recorded: the automatic release was held at a branch close, on the user's decision

**This is a departure from a ritual that fires mechanically, and it is written down because a departure that isn't recorded is indistinguishable from a violation.**

At the close of the thirty-item run on `overnight-blitz-2026-08-06`, the release check ran as specified — `git diff` against the last release tag showed commits touching `plugin/si-plugin/`, so the ritual's answer was "release due". CLAUDE.md is emphatic that this trigger stays mechanical: *"don't ask whether a release is warranted, don't propose holding one back until something is tidier, and don't add a quality condition to the trigger."* That emphasis is well-founded — welding release to a readiness judgment is what once stopped releases happening at all.

**The release was not run.** The user was told plainly why the ritual's silence mattered here, given both options with a recommendation, and chose to hold until the merge.

**Why this was raised rather than decided silently in either direction.** The ritual says nothing about *which branch* a release comes from, so there was no rule to follow and no rule to break — a gap, not a bendable instruction. Two consequences made it worth stopping for. Releasing from this branch would publish work that has not passed the **pre-merge differential audit gate**, which was built in this very run and recorded in CLAUDE.md; a release puts code in front of consumers, which is further than a merge does, so it would defeat that gate more completely than an unaudited merge would — on the day the gate was written. And the version line would fork, since v1.19.0 came from main and a branch release would carry work main lacks.

**What was explicitly not done:** no readiness judgment was made. Nobody asked whether this work was good enough to publish. The question was structural — which branch a release comes from — and the mechanical trigger is untouched.

**The cost, stated rather than glossed:** holding delays a privacy fix reaching consumers. This run removed a hook that silently wrote the user's absolute path into their repository, and that removal now waits for the merge. The user made that trade knowingly. Any rule written from this must answer what happens when a held release contains something actively exposing users — the red-flag triage's spreading-versus-sitting-still distinction is probably where that answer lives.

**What happens next:** the branch soaks, the differential audit runs over its whole span, its repair captures are cleared, the branch merges, and the release fires from main. The work is committed and pushed, so nothing is at risk in the meantime.

The underlying gap is filed as [release-ritual-silent-on-branches] so the next branch close does not have to stop here.

**Files touched:** none — this entry records a process decision.
**Routed to Captures:** [release-ritual-silent-on-branches]
