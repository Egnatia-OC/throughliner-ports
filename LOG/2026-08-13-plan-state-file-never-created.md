# [HASH] — The /plan close must name its planning state file, or name its absence

`done-plan.md`'s LOG entry now carries a `Planning state:` line unconditionally —
either the filename and the number of dispositions, or "none — no items were
processed". `plan.md`'s Step 2 gained a pointer at the step that creates the
file, so the obligation is visible where the file is made.

A session that processed work and cannot name its state file leaves a gap anyone
can see, and "no items were processed" is a claim a later reader can disagree
with by reading the queue's own history.

The two hook-shaped options were rejected, recorded so they are not re-proposed.
A `session_start` check fires before any planning has begun and cannot tell a
planning session from an ordinary chat. A `pre_tool_use` check on QUEUE.md writes
would fire on every capture from every session, and a check that cries wolf gets
worked around; distinguishing a capture from a processing move needs a stored
previous state, which this project refuses on principle. The close is the only
site that knows by construction that this was a planning session.

The honest limit is written into the rule text rather than left out: by the close
the information has already been reconstructed from memory if the file was never
made. What the line buys is that the reconstruction is labelled as one. It
detects; it does not prevent.

Rule gate: run — admitted as an amendment, copying the shape of FAQ-sync and the
gate disposition, the two obligations here with demonstrated teeth. One recorded
instance: a session processed eight items and never created the file, noticed
incidentally at the eighth.

FAQ: not needed because the line appears in a log entry the user can read and
describes Claude's bookkeeping rather than anything they do.

**Files touched:** `plugin/si-plugin/docs-b/done-plan.md`,
`plugin/si-plugin/docs-b/plan.md`
**Routed to Captures:** none
