# [HASH] — The forward advisory is cleared at the /plan read that consumes it, not at the close, so a build session can no longer leave a spent note behind

Observed 2026-08-13 at a session opening: the advisory said to start with the
rename because it had been starved rather than blocked, and the rename had already
shipped in `989c38b`.

**The sequence that produced it.** The clear lived only in `done-plan.md`, and
`done-build.md` had no equivalent — so a /plan files an advisory, a /next builds
the very thing it points at, the build close commits and clears nothing, and the
next /plan opens on advice about work that already shipped. This is the failure the
advisory step had already been hardened against twice, arriving by a route neither
fix anticipated: both assumed the next reader would be a /plan, and neither
expected a build session passing straight through the middle.

**Settled at processing on 2026-08-13: the clear moves to the read.** It is the
smallest change and it puts the clear where the knowledge is — the session reading
the advisory is the one that can tell it is spent. Giving the build close its own
clear step was rejected because it would put the deletion in a session that never
read the note and cannot judge whether it was used. A written expiry condition was
rejected as more machinery for the same result.

**The persist-condition branch travelled with the step rather than being
re-authored**, which is what kept SPEC's existing promise intact: an advisory
naming an unmet condition still stays in place.

**One consequence stated in the doc rather than discovered later.** Clearing at the
read means the advisory is gone even if the planning session then ends without
doing anything with it. That is acceptable — the advisory is orientation, not
work, and a session that opened and read it has had the orientation it was for.
Holding it back against that case is precisely what produced the stale note.

**Scope grew with approval, and the ripple was found by grepping rather than from
the item's file list.** Both `SPEC.md` and the shipped FAQ template described the
old timing: SPEC said the clear happens at the close, "the one close that always
runs, so the clear isn't skipped when a /plan ends early" — the exact reasoning
being reversed — and the FAQ template told users the note is deleted once the
processing order is agreed. Both were corrected in the same commit.

**Rule gate: run** — an amendment. A step relocates rather than a rule being
added, so the corpus loses a step and gains none. Evicted: `done-plan.md`'s clear
step and the note explaining why the clear lived at the close, which is the
reasoning being reversed and so goes rather than standing contradicted in place.

**Files touched:** `plugin/throughliner/docs-b/plan.md`,
`plugin/throughliner/docs-b/done-plan.md`, `SPEC.md`,
`plugin/throughliner/templates/faq-template.md`.

**Routed to Captures:** none.
