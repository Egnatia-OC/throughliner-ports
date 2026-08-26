# 2c76e53 — Working-file rule-gate lines now carry their slug, so a later tick can't steal them

Each ticked item writes up to three lines into a build working file: the tick, a
slug-bound `Depth:` line, and where the item carries one, a transcribed
`Rule gate:` line. The depth line is slug-bound and next.md says plainly why — a
bare positional line attaches to whichever tick it happens to sit under. The gate
line carried no slug and had exactly that problem, three times in the run that
filed this.

The slug-bound fix won at planning on the depth line's own recorded ground: the
alternative, stating a per-item write order, depends on care rather than removing
the need for it. So the working-file form becomes `Rule gate: <slug> — …`, and the
close reads it by slug in the same pass as the depth field.

**This run supplied fresh evidence before it built the fix.** The same failure
happened twice here — a new tick written by matching on the previous item's last
line landed between that item's depth and gate lines, leaving a disposition sitting
under the wrong item's tick. Both were caught and repaired in the session. Nothing
would have caught them otherwise: the close reads depth by slug and so never has to
notice the gate line's position, and the working file is deleted at the close. The
consequence if one survives is a disposition attributed to the wrong slug in the
one artifact the gate produces as evidence.

**Two things were checked rather than assumed, and both came back needing no
change.** CLAUDE.md describes the *queue item's* gate line and the *LOG entry's*,
neither of which is the working file's — so the item's "updated only if it states
the slugless format" condition correctly resolved to no edit.
`resources/rule_signals.py` reads LOG entries only, and the LOG-entry format is
untouched and stays slugless, because that line describes the session rather than
one item. Both docs now say so at the point of change, so a later reader doesn't
have to re-derive it.

**Files touched:**
`plugin/throughliner/docs/next.md` — working-file gate line gains the slug, with a
typed specimen.
`plugin/throughliner/docs/done-build.md` — the close reads the gate line by slug.

**Routed to Captures:** none.

Tick form: done, confirmed.

Rule gate: run — amendment mirroring the depth line's slug-binding onto its sibling
gate line. The write-order alternative was refused at planning on the recorded
ground.
