# [HASH] — plan.md keep-step — read-the-mechanism clause extended: reversibility claims checked against the actual target

From two recorded failures, both git-recoverability claims ([processing-asserts-reversibility-without-checking]): [delete-codex-port-from-history] was cleared on a paragraph recording that the cheap operation "is also the reversible one" — true of commits, false of the 722 lines of uncommitted work the deleted worktree held — and [runs-alone-premise-never-tested] was the same failure one layer up. Nothing at the keep-step asked a session to look at the thing about to be destroyed; the build's halt worked only because it happened to run `git status` unprompted. The fix is one sentence extending the existing "read the mechanism before describing the build" clause: a reversibility or recoverability assertion is such a claim, and checking it means inspecting the actual target — what would be destroyed, and whether it is genuinely held elsewhere — before the item clears. The broad alternative, inspecting every destructive item's target, stays refused as firing on work that destroys nothing.

Tick: done, confirmed (clause reads whole; no new freestanding rule or heading).

Rule gate: run — amendment to the named keep-step parent; two recorded instances satisfy the has-it-failed-more-than-once test; nothing evicted, since the sentence extends an existing clause rather than adding a rule.
FAQ: not needed because the keep-step is Claude's procedure; no user action changes.

**Files touched:** plugin/throughliner/docs/plan.md
**Routed to Captures:** none
