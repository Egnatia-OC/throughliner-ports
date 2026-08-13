# 16ed591 — A clean git status may no longer be reported as "no change was made", and the close names the method docs it stages

Two halves, weighted opposite to how the item first proposed them.

The substantive half is the misreport, and it is one clause. A clean `git status` means there is no *uncommitted* change; it never means no change was made. In the instance that produced this, the user asked Claude to look at their edit and Claude reported it did not exist — correctly reading a clean tree, while the edit had already been swept into a commit minutes earlier. A clean tree cannot distinguish "no edit was made" from "the edit is already committed", and the user was close to redoing work that existed. That clause now sits in the always-loaded file-safety block, because the question "has my edit landed?" can arrive whatever is running.

The sweep gets the cheap half. Where a close stages a method doc it now names the files in one line before committing — one sentence, no diff. The existing guard is blind to this case by construction: it compares dirty paths against the build's file list, so it cannot see anything inside a file the session already owns, and QUEUE.md is the file a planning session edits by design. A hand edit the user made there, or a line another session left deliberately, arrives inside a file Claude already considers its own.

Both limits are written in beside it and neither may be softened. Naming the staged files makes a swept edit **visible**, not **detected** — nothing cheap will ever tell the user that a particular line inside QUEUE.md was theirs rather than Claude's. And against the third and worst of the three recorded instances it does almost nothing: where another session has already *committed* this session's in-progress work under its own message, this line produces the word "QUEUE.md" — true, useless, and silent about whose work is inside. The item was explicit that the build must not ship this believing it covers that case.

The rejected route: having the close diff its own writes against the file's state at staging time would make a hand edit inside a Claude-owned file genuinely detectable. It is machinery out of proportion — the close would have to track every write it made all session — and the payoff is low, since nothing was lost in the actual instance.

One thing about the item itself is worth carrying, because it is this run's own subject applied to a person rather than a mechanism. Its central claim was that the user made a particular hand edit. Presented with it at /plan the user first said they had not, then on being shown what it described recognised the occasion and confirmed. The claim stands, but it stood for two days on nothing more than what Claude believed it saw, and the commit cannot settle it either way — a commit records content, never who typed it.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`, `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none

Rule gate: run — admitted as an amendment, consuming no slot. Parent named: the file-safety block in skill-nonspecific-rules.md, which already governs what may be reported about git state; the clause is written into that block. Distribution: always-loaded, and this is the item's own stated reason — the question can arrive whatever is running, which is that file's four-skills test. Eviction: nothing, since there was no prior statement about clean-tree meaning to supersede. Admission evidence: a recorded instance in which the user was close to redoing existing work. The done.md half is a narration step rather than a rule, and carries both its limits explicitly.
