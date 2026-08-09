# 4f5e167 — FAQ-sync reframed from a soft self-check into a hard close gate whose disposition has to be written into the LOG entry

The clause added on 2026-07-30 asked a session carrying a user-facing change to "confirm the FAQ entry was written". It failed on its first real test: `ea272f6` synced SPEC and not the FAQ, which is the exact case it was added for.

The diagnosis is that it borrowed SPEC-sync's trigger but not its teeth. A self-check that produces no artifact is indistinguishable from a self-check that was skipped, so skipping it cost nothing and left no trace. SPEC-sync works because it blocks the close and because the result is visible in the commit.

So the disposition is now a required line in the session's LOG entry — `FAQ: updated <entry>` or `FAQ: not needed because <reason>` — and the close does not complete without it. The required artifact is the entire fix: "not needed because X" is a claim someone can later read and disagree with, and a missing line is a gap anyone can see. A silent omission becomes an auditable one.

A hook was considered and rejected. "Is this change user-facing?" is not mechanically detectable the way queue structure is, so a hook would either miss real cases or fire on false ones — and a gate that cries wolf gets worked around, which would leave the method worse off than the soft check it replaced. The gate instead rides a read that already happens, at the one close that always runs.

It stays host-only by residence, which is Alex's constraint and the cheapest possible enforcement: the rule lives in this project's CLAUDE.md, which consumer projects do not carry, so it never fires for consumers — who do not maintain the method's FAQ and would be baffled by the obligation.

The gate governs this very session's close: all twelve entries carry a disposition line.

**Files touched:** `CLAUDE.md` (the FAQ-sync clause in Working conventions, rewritten).

**Routed to Captures:** none from this item.

FAQ: not needed because the gate is host-only and governs how the method's own FAQ is maintained; a consumer never encounters it.
