# 1332c55 — file-safety gains the disk-change-halt rule for method docs: stop and establish what changed before the next write

The Edit tool's "file modified on disk since you last read it" warning fired twice in one planning session and was dismissed both times as the queue mover's doing — a plausible reading, since the mover really does rewrite the file, and that is precisely the trap: the innocent case trains the response to the dangerous one. The second warning was a concurrent session having destroyed an item's heading, and the corruption rode two further edits into a commit. The rule shipped as the item stated it, one line with its narrowness intact: on a disk-change warning for QUEUE.md, SPEC.md or LOG/, stop and establish what changed before the next write — a cheap `git status` and a re-read, never an inferred cause. Deliberately scoped to the method's own documents, where a session reasons over the whole artifact; a blanket every-file rule would fire constantly and get ignored, reproducing the failure it fixes. Home: plugin-behaviour.md's file-safety section, beside the uncommitted-changes rule.

Overnight blitz run 2, phase 3 (branch overnight-blitz-2026-08-05b): processed and built under the blitz plan's softened bar and sanctioned departures — approvals deferred to branch review, no push.

**Files touched:** plugin/si-plugin/docs-b/plugin-behaviour.md
**Routed to Captures:** none
FAQ: not needed because the rule governs Claude's own write discipline, invisible to the user except as fewer silent corruptions.
