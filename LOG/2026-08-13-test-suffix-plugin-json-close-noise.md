# 340e7ef — CLAUDE.md's Push section stops asserting something the working tree contradicts

The Push section claimed `plugin.json` "is dirty only between a rezip and that
same session's push", and concluded that there is therefore no recurring
close-time noise to carve out. That holds only if every rezip is followed by a
push in the same session, and one was not: `git diff` at processing showed the
file carrying `1.20.0-test8` against a committed `1.20.0`, already dirty when the
session opened, so the window had spanned sessions and every close in between
would have surfaced it as an out-of-scope dirty path.

The section now states that the window is normally one session but spans sessions
whenever a rezip is not followed by a push, and that a close meeting a
`plugin.json` diff whose only change is the `-testN` suffix recognises it as the
known rezip artifact and skips the investigation — at most a one-line note, never
a per-close question. Sibling in shape to the hash-backfill signature skip.

The item's stated destination was rejected, and `CLAUDE.md` was right about why: a
carve-out in shipped `done.md` would ship a rule about `-testN` to consumers who
never rezip and can never produce that signature. So the change is host-side,
where the rezip ritual already lives, and `done.md` is confirmed out of scope —
correcting the item's own guess.

Deleting the item as overtaken was weighed. Most of it is overtaken by the
rezip-before-push ordering. What is not is that an always-loaded file every
session reads asserted something false, which is worth one sentence to correct.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none
