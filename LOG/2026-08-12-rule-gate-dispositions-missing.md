# 0ae69d6 — The BORN signal gets a baseline commit, dropping its report from 15-of-15 to 1-of-1

`DISPOSITION_BASELINE = "7c9922a"` in `resources/rule_signals.py`. BORN now examines only commits **after** the one in which the disposition obligation shipped.

**Start clean rather than backfill**, as decided at processing. A backfilled disposition is written by someone reconstructing what a past session decided — it would look like evidence and not be, which is the handoff-provenance problem the method already names. Every one of the 15 commits BORN was reporting predates the obligation, so there is nothing dishonest about them.

**Why "start clean" needed a build rather than just a decision.** The board treats a signal as satisfied only while an open capture with its slug exists. Deciding to start clean and deleting the item would make the signal re-file an identical capture at the next session start, because those commits are still inside its window. The available outcomes were backfill (rejected), leave a queue item open permanently to suppress a check (rejected — it makes the queue a place where items live to silence signals), or give the signal a baseline.

**The constant is found, not remembered.** `git log -S'Rule gate: run —' -- CLAUDE.md` returns exactly `7c9922a`, the build that added the disposition block alongside the board itself. The comment records the command as well as the hash, because a bare hash nobody can date is a constant nobody dares change — the same reasoning the format-epoch history comment rests on.

**An unknown baseline is an error, not a silent fallback.** Where `git log <baseline>..HEAD` fails — a shallow clone, or the constant edited to a hash this repository doesn't carry — the signal says so and names the baseline, rather than falling back to the whole history and re-reporting everything the baseline exists to exclude.

**Verified by running the board:** BORN went from *15 of the last 15* to *1 of the 1 commits since 7c9922a*.

**What this deliberately does not fix**, kept separate on purpose: the signal checks a disposition line *exists*, never that it is true. That is [rule-gate-disposition-is-unverified], built in the same pass and recorded in its own entry.

**Files touched:** `resources/rule_signals.py`.

**Routed to Captures:** none.

Rule gate: not needed — no rule authored or amended. This is a detector narrowing its own window; the obligation it checks is unchanged in wording, scope and force.
FAQ: not needed because the board is a development artifact, host-only, and is not in the plugin package. No consumer ever sees it.
