# V110 — 2026-05-27 — OQ deliberation and ideation

**What shipped.** Combined commit covering two sessions. (1) v109 build: `/sovsetup` case 4 scaffold drift detection — pytest registry + 4 missing case 4 migrations fixed, method version bumped to V88 (plugin 0.88.0). (2) v110 ideation/deliberation: resolved 8 of 9 open questions — 4 promoted to new batches (0112, 0113, 0114), 2 folded into existing batches (0110), 1 dropped, 1 kept parked. Three new queued batches added. Significant architectural ideas captured in 0112 (build-snapshot, skill split, BACKLOG rename).

**Decisions taken and why.** Renamed BACKLOG to BUILD-PLAN (scoped in 0112) because "backlog" contains "log" as a substring, causing persistent confusion with "build log." Git conventions mechanized per procedure doc — each planning mode's close step commits directly (no tag, no push) rather than nudging users toward `/sovgit`; push reserved for builds only. Build-snapshot architecture (0112): `/sovbuild` extracts active batch into `_method/active-build.md` and removes it from BACKLOG, fully unlocking BACKLOG for parallel sessions. Phase detection shifts from status parsing to file existence.

**Pivots and surprises.** Key insight mid-session: phase-aware locking is file-state-based (reads `Status: active` from BACKLOG.md), so ALL sessions see the lock — not just the build session. This drove the snapshot architecture. Also discovered Claude has no visibility into its own context window usage, which shaped the session-length safeguards batch (0113) toward proxy signals.

**Carried forward.** Nothing.
