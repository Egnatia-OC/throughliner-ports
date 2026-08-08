# [HASH] — The merge cycle becomes queue machinery: rebranch seeds three standing items, and the branch-cycle section gains a which-audit-at-which-phase table

The user's closing question the day before was whether the cycle would ever be "a
designed and built thing rather than me constantly having to explain how it works".
This is the answer.

**The diagnosis came from CLAUDE.md's own admissions.** The cycle — branch →
blitz → soak → differential audit → reconcile → merge → branch again — existed only
as prose conventions. The branch-cycle section says outright that nothing enforces
its gate and that a merge item written without it would go unnoticed. The blitz ran
when the user asked; the audit ran only because the user pushed; the merge gate
existed only if whoever wrote the merge item remembered it. Every phase depended on
the user re-explaining the cycle to whichever session was in front of them — the
exact working-memory dependence the queue exists to remove.

**The fix is that the cycle's phases exist as ordinary queue items, seeded at
rebranch.** The soak-end sequence gains step 6a, immediately after the "branch
again" step — the single moment a cycle begins, already written down, and already
flagged as the easy one to skip, which is an argument for giving it visible output.
The three seeded items are written out in full so a future session copies rather
than re-derives them: a blitz run item, the differential audit as an `[audit]`
item, and a merge item whose prose carries the audit gate. All three sit below the
readiness line, and all three are written to be **re-added** each cycle rather than
re-derived — the sanctioned repeating-batch shape, so no new state and no new
machinery.

**The three open questions were settled at processing, all approved by the user,
and the reasoning is recorded because each could plausibly have gone the other
way.** The seeder is the rebranch step, because it attaches to an existing written
step rather than inventing a trigger. The blitz item is an **ordinary build held
below the line**, not `[user]`-flavored: the over-tag guard decides it, since Claude
can run a blitz and what Claude cannot do is decide that tonight is a blitz night —
a readiness question the readiness line already expresses. Tagging it `[user]`
would be the recorded mistake of confusing "Claude can't do this" with "Claude
can't do this yet". And seeding is a **documented step, not a hook**, because a
convention honoured in one written place beats a mechanism nobody built, with the
retired push marker as the standing evidence; a hook is the escalation if the
documented step proves unreliable.

**The phase table was folded in here at the user's approval, from
[compression-pass-plan-and-cycle-audit-roles], and added no files** because this
item was already rewriting the cycle sections. It states which audit runs at which
phase — today that has to be reconstructed from three documents. Four rows: the
blitz night, the differential audit as the merge gate at soak-end, the full-corpus
audit for big boundaries only, and the compression pass in its own phase with the
full audit as its precondition. Writing the table and the seeded-item list in one
pass was the point: they cannot disagree, which was the reconciliation risk before
the fold.

Both plan docs gained a section naming their own queue-item form, so a session
reading either one finds the item text where it is working rather than in CLAUDE.md.

**Files touched:**
- `CLAUDE.md` — soak-end sequence gains step 6a and a "Seeding the cycle" subsection with the three items written out; branch-cycle section gains the four-row phase table and its explanatory paragraph.
- `resources/overnight-blitz-plan.md` — new "This blitz's queue-item form" section; the soak-end bullet updated to name the audit as a queued `[audit]` run.
- `resources/consistency-audit-plan.md` — its queue-item form section (shared with [inline-audit-reconcile-procedure], which authored it).

**Routed to Captures:** none from this item.

**FAQ:** not needed because the branch cycle is host-only development machinery; consumers have no cycle to seed.
