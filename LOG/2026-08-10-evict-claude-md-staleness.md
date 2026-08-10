# [HASH] — Three stale passages corrected in CLAUDE.md, including two retired /next markers it still documented as live

Audit findings 11 and 12, approved 2026-08-09, plus finding 13 found by the /next
run that returned this item unbuilt on 2026-08-10.

**Finding 11.** Current state said "Target v1.16.0" against an actual 1.20.0.

**Finding 12.** The file opened with a section describing the two-section merge as
recent and its rollout as pending — "the next steps are: rezip + reinstall… then
push + release" — for work that has since shipped, been released, and reached the
other projects. Recast to what is true now, and shortened: the merge is history,
not news.

**Finding 13, the one that mattered most.** `CLAUDE.md` documented
`--- Push required before continuing ---` and `--- Plan session here: <reason> ---`
as live /next behaviour. `docs-b/next.md`'s pre-flight says plainly there is no
blocker gate, push marker or unpark scan — those belonged to the old model and are
gone. So the always-loaded file was instructing sessions to write markers /next
would never act on. The section now says both are retired, says what replaced each
(readiness settled at /plan, host liveness read from the content stamp, dependency
carried by `Blocked by:` which survives a reorder where a positional marker does
not), and keeps the one thing the old note said that was repeatedly misread: **a
decided-but-unshipped rule is in force from the moment it is decided.** "Not
shipped yet" is never a reason to suspend decided reasoning.

Staleness is an eviction concern rather than tidying because the gate's own test is
"is this still true?", and it records that a confidently wrong rule is worse than a
missing one. An always-loaded file describing finished work as pending steers every
session that reads it.

**Files touched:** `CLAUDE.md`.

**FAQ: updated** — the "What does a 'Plan session here' line in the queue mean?"
entry documented one of the two retired markers to consumers. It is gone, replaced
in the same slot by the freeform-tag entry from [resurrect-freeform-sessions].

**Routed to Captures:** none from this item.
