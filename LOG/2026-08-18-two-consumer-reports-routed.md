# 02ec308 — two consumer reports arrive mid-chat, one of them verified against this repo before filing

Both messages landed after the session's opening, so neither was surfaced at session start — the case the close's own mail step exists to catch, reached here because the user asked.

**The first reports that a shipped rule cites a tool that does not ship.** Verified here rather than taken on trust: `resources/measure_written_shape_length.py` exists in this project only, a `find` over the plugin package returns nothing, and line 711 of the shipped rules tells every consumer to run it. Its own docstring reads "host-only dev artifact", so the defect is a shipped rule pointing at a deliberately unshipped tool. It also reports a third instance of the split-action failure from outside this project — an item reaching roughly 740 words with every addition in band, where splitting would have cut one design in half with both halves naming the same file.

**The second is the more serious.** A planning session ran to completion with `SPEC.md`, `QUEUE.md` and `LOG/` all gitignored, so write-first, "git history keeps a deleted item", and the close's own `git diff HEAD -- QUEUE.md` were silently false for that whole session — including a red flag's clearance and its informed-consent trail going into an untracked file. Setup checks that a `.gitignore` *contains* a `.throughliner/` line and never that it does not contain something fatal. Their close then deadlocked, because the scope-lock correctly refuses `.gitignore`.

Both captures describe the sender generically, since a capture is committed and the mailbox is not. Both files were archived.

**Queue changes:** two captures filed in Unprocessed; two messages archived.
**Work processed:** none — filed for a later /plan. Filed — [word-band-script-does-not-ship] (later kept), [gitignored-core-docs].
