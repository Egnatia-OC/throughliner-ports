# 96166c6 — A run may widen its own Files list and narrate it; underspecification still halts

**The capture's premise was corrected at processing, and the correction dissolved the fork as written.** `_build.md` is already editable during a build — `pre_tool_use.py` classes it alongside the queue and the log, and the hook's own denial text says as much. So the framing that this method locks its scope file where an independently-built tool deliberately leaves its own editable is **wrong about this method**. Mechanically the two designs already agree: the scope file is writable and an expansion lands in the diff where a human can read it. Verified by reading the hook rather than inferred.

**What actually enforced the halt was instruction, not the hook** — the procedure told a build that needs more files to stop and ask; nothing mechanical stopped it appending to its own list. That relocated the whole question from code to behaviour, and meant the change cost no hook work at all. Recorded explicitly in the shipped text so this is not reopened as a code question.

So the real question became a better one than the fork it replaced: **when may a run widen itself and narrate it, and when must it genuinely stop?** The answer hangs on the seam the method already has: **the work grew** → append the file, say in one line which and why, and continue; **the item was underspecified** → halt, because building it means inventing scope the user never agreed to, and no amount of narration fixes that.

**The cost the strict reading carried is why this was worth doing.** A halt is an interruption, and /next is unattended in practice, so every legitimate scope discovery ended a run that could have continued. Not hypothetical: a real build's self-scoping caught a genuine ripple and could only report it by halting mid-run — the interruption an unattended run should not need.

**The other design's cost is kept so the trade stays honest:** it relies on someone actually reading the diff. That is a real dependency, and it is the reason **the narration limb is not optional** — an expansion that is permitted but unannounced is strictly worse than one that halts.

Widening covers a file or two the work turns out to need; it is not a licence to absorb a second piece of work, so the significant case still proposes splitting.

SPEC's scope-lock paragraph already said the Files list is an approximation of the real boundary rather than the boundary itself; it now states the widening behaviour so that description stays true.

**Files touched:** `plugin/si-plugin/docs-b/next-build.md`, `SPEC.md`

**Routed to Captures:** none
