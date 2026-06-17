# [HASH] — Rewrote CLAUDE.md's goal-session shape from interim to defined [formalize-goal-session]

From the /goal fork. /goal works in practice but the method had no defined goal-session shape — it assumed one batch per session, so earlier runs improvised the aggregate _build.md, the LOG entries, and the single commit. This rewrites CLAUDE.md's "Goal sessions (plugin off)" section from interim handling into a defined shape, structured as "The run" and "The close."

The run: Claude works the batches back-to-back, plugin off, owning the sequencing, using a single aggregate _build.md as a working-state / resume record — and because the scope-lock hook does not fire with the plugin off, that _build.md is explicitly state, not enforcement. The close: one manual /done writes a separate LOG entry per batch (one entry file and one index line each) in a single end-of-run commit, runs the shipped-slug cross-check from done.md's commit core, runs the deferred-test and staleness sweeps once across all batches rather than per batch, and does the LOG-hash backfill by hand because the session-start hook never fired. The handoff-claim provenance paragraph was kept intact; the claim-marking format decision still belongs to the cruise-control build. The "interim handling until /goal is formally supported" pointer was removed, since the shape is now defined.

The logging shape — a separate entry per batch, not one multi-thread entry — was the decision settled at the 2026-06-17 /plan and is reflected here. This very session is the first run executed against the defined shape. Step 1 of the cruise-control arc. No FAQ entry: goal sessions are the developer's host-only workflow; consumers never run them (cruise control is their version).

**Files touched:**
- CLAUDE.md — rewrote "Goal sessions (plugin off)" from interim to defined.

**Routed to Captures:** none.
