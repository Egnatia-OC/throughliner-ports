# [HASH] — The four deleted rezip verification steps restored, the version-bump rule written down for the first time, and the three hook suites wired in

The evidence for this was a whole session run on the wrong plugin. The 2026-08-09 /plan session loaded its procedure from an installed host predating `f9326dc`: that snapshot still contained the retired `docs/` folder and its skill files still pointed at it, so every procedure the session followed came from a docset that had been deleted two commits earlier. Nobody noticed for half the session, and then only because Alex thought to ask.

The cause is mechanical. `claude plugin update` matches on the **version string**, so re-running it against an unchanged version reports "already at the latest version", re-snapshots nothing, and reports success however far the source has moved. A rezip had installed `-test1` while the source was two commits behind; every later update was a silent no-op. Bumping to `-test2` fixed it instantly.

Four steps that would have caught this existed before the emergency revert and were deleted by it, so this was restoration rather than design: pruning the plugin cache (nothing else ever removes those, and the pile is what makes "which host is actually live?" hard to answer), comparing the content stamp of the source against the installed copy immediately after installing, checking the CLI's version against the app's, and proving the hooks are alive in the first session after the restart.

One thing here is new rather than restored, and it is the sentence whose absence caused the failure: **a source change made after a rezip needs a fresh `-testN` bump before another update will take.** Without it written down, "I already rezipped today" reads as sufficient when it is not, and the no-op reports success.

`[hook-tests-not-in-rituals]` was consolidated into this item rather than built separately, since both edit the same ritual steps and building them apart would have had two sessions fighting over the same text. Its honest limit is preserved and must never be dropped: **the schema check asserts output shape, not delivery.** A correctly-shaped hook can still be discarded before it reaches a session, which is precisely what the post-restart liveness ask exists for. Adding the suites does not replace that ask.

The ritual was then exercised end to end in this same session, which is the strongest test available: the rezip bumped to `-test3`, all three suites passed, the cache was pruned from six builds to four, the stamps matched exactly at `0854a34f2336`, and the first session after the restart reported a hook payload carrying this run's work — including a queue lint firing after a Bash command, which was structurally impossible before today.

**Files touched:** `CLAUDE.md` (the Rezip ritual grown from three steps to nine, with the `-testN` bump rule as its own named paragraph).

**Routed to Captures:** none from this item.

FAQ: not needed because rezipping is host-only — a consumer installs from the marketplace and never runs this ritual.
