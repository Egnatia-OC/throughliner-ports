# [HASH] — The differential audit becomes a queued [audit] run: both "inline" wordings removed, and the plan doc gains a queue-item form section

The shape this item originally praised failed on first contact with the user, and
the build is the correction.

**The user's verdict on experiencing an inline audit:** *"there was no audit of
any shape, just one small thing was built."* Two failures sat behind that, and the
second is the deeper one.

**Invisibility.** An audit run inside a planning chat produces no run the user can
see, no `[audit]` item in the queue, no dedicated LOG entry at the time, and no
sense that the cycle's gate actually fired. The user approved "keep and clear it"
believing the *audit* was being queued as the cleared work; what was queued was
only its repair. The approval and the thing approved diverged, silently.

**Depth.** The inline run was also genuinely shallower than the plan's own pass
list: the three changed hooks were never read in full (pass 9 as written), and the
pointer and duplicate passes were skimmed. "Usually cheap enough to run inline in
one session" licensed a light check to wear the audit's name. Compression of
effort followed compression of form.

**Both inline wordings were located at processing — there were two, not one, and
fixing only the obvious one would have left the licence in place.** The mode
description at line 12, and the Execution and reporting line at 116. Both are gone.

**What the plan doc now says.** The differential mode's description states that the
audit runs as its own queued `[audit]` work item, and a new *This audit's
queue-item form* section carries the seeded item text, the rebranch/soak-end
timing, and both failures above as the reason. /plan's role is stated positively —
seed the item at rebranch, clear it at soak-end, then process the findings the run
brings home — rather than only as a prohibition, since a prohibition at a moment of
real pressure is what produces invented escapes. The execution bullet now says to
run it through /next in one session reading the changed files in full, fanning out
only for an unusually wide span and asking first.

CLAUDE.md's branch-cycle section was aligned to match, including the ASCII cycle
diagram in both documents, so the two cannot read differently.

**Files touched:**
- `resources/consistency-audit-plan.md` — mode description (line 12) and Execution bullet (line 116) rewritten; new "This audit's queue-item form" section; cycle diagram updated.
- `CLAUDE.md` — branch-cycle section's cycle sentence and a new paragraph stating the audit is a run rather than a chat, with the 2026-08-08 failure named.

**Routed to Captures:** [audit-plan-cites-ripple-grep-as-unbuilt] — a stale citation noticed in this same file while editing it.

**FAQ:** not needed because the branch cycle and its audits are host-only development machinery; consumers run no cycle.
