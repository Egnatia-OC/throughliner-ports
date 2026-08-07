# 5993a10 — next-build.md's Claude-raised capture closer fixed, and the build loop's removal step pointed at the mover

Two repairs on the same file, run as one pass.

**The closer.** `plugin-behaviour.md` says in two places that a Claude-noticed capture closes with confirm-and-resume, never an invitation for more — while `next-build.md`'s "Claude discovers user-runnable testing is needed" step instructed *"ask 'anything else?' — repeat until no"*, in a procedure that is Claude-raised by construction. The step now confirms and resumes, and carries the reason inline: the distinction is **who raised it**. The "anything else?" loop belongs to a *user*-raised capture, where asking respects that they were the one interrupting; inviting more on something Claude raised turns its own observation into an open-ended interruption of a build the user already approved. The user-raised sibling a few lines above uses the loop correctly and was left alone.

**The removal step.** `next-build.md`'s per-item removal read *"remove the item from QUEUE.md"* and named no tool — verified, the file had **zero** references to `--delete`, its only mention of "delete" being the instruction not to delete `_build.md`. Meanwhile `plan.md` and `done.md` both spell the command out in full. It now names the mover with the same shape as those two, plus the reason: the mover removes the block byte-exactly, refuses rather than guessing on an unresolvable or ambiguous slug, and re-anchors the readiness marker if the removed item was its anchor.

**Why that omission mattered more than its size.** The parent build that added `--delete` pointed the two lower-frequency removals at the new tool and left this one bare — and this is the **highest-frequency** instance of the operation, once per item in every build loop, and the one that runs with no user present to notice a shortcut being taken. Two of that item's three recorded shell-write slips happened inside /next runs, and the decisive third inside an unattended blitz. Pointing the safe removals at the tool while leaving the risky one unpointed is close to backwards.

It was captured rather than folded into the parent at the time because the parent named its three docs explicitly and this file was not among them — folding it there would have been a build widening its own described work.

**Files touched:** `plugin/si-plugin/docs-b/next-build.md`
**Routed to Captures:** none
