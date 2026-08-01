# [HASH] — Three method-design captures on the post-close tail

Post-close tail after `fa2f8e5`. A design discussion about the post-close state itself produced three captures, all filed to Unprocessed: [post-close-tail-state] (name the post-/done tail; route it cleanly and advise that the file scope-lock is off post-close, without adding a re-/done prerequisite — durability is already handled by the captures-ride-next-commit mechanism), [drive-testing-signals-skill-routing] (Claude driving testing/verification in a loose tail is a signal to route into a skill, not run it ad-hoc), and [done-delta-close] (a lightweight post-close delta close that commits since the last /done without a full-session rescan).

**Queue changes:** filed 3 captures to Unprocessed.

**Work processed:** none.
