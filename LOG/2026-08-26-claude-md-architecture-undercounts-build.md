# 2c76e53 — CLAUDE.md's Architecture section corrected to the five skills and four hooks that ship

Found by the v1.21.0 release sweep. The Architecture section said "4 skills",
omitting `/rescan`, and "3 hooks — two enforcing, one advisory", omitting `stop.py`.
`plugin.json`'s description already named five skills and SPEC already described
both `/rescan` and the stop hook correctly, so this file alone had fallen behind.

Why it mattered beyond tidiness: this is the always-loaded project file every
session here reads to orient itself, so a session read it and learned the method
has no `/rescan` and no stop hook. That is the same class of failure the migration's
retired-term detection exists to catch in consumer projects — a description written
once and read at every session start, quietly describing a method that no longer
exists.

Both new bullets are worded from SPEC's existing descriptions rather than composed
fresh, so the two files cannot drift apart again on this.

**The folder tree four lines below carried the same undercount**, listing three
hooks and four skills. That was outside the item's stated scope — its acceptance
said no other CLAUDE.md text changes — so it was put to you rather than swept in,
with the recommendation to fix it: leaving a known-stale listing beside the one
just corrected invites the next reader to trust it. You agreed, and it is corrected
in the same edit.

**Files touched:** `CLAUDE.md` — Architecture section and the "Where things live"
tree.

**Routed to Captures:** none.

Tick form: done, confirmed — the counts checked against `plugin/throughliner/skills/`
and `plugin/throughliner/hooks/` on disk.

Rule gate: not needed — a stale description corrected to match what ships, no rule
authored or amended.

The original fix was attempted during the release sweep and refused by the
scope-lock, correctly: the build working file had been deleted at that close, so the
session was on the standing planning list and CLAUDE.md is not on it. It reached
this run as an ordinary build item, which is the route the refusal was pushing it
toward.
