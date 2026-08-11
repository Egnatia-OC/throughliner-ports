# 94bba66 — /next no longer proposes running fewer items than the cleared line allows

Captured by the user 2026-08-09, in their words: Claude consistently tries to
arbitrarily limit runs, when research restored from before the revert establishes
that we have 1M context.

`next.md`'s run presentation now says to present the whole cleared region and
never recommend a subset of it, and not to inherit such a suggestion from a
previous session's advisory. `done-build.md`'s recommend-next says the close
writes no size judgment about the next run.

The decision, restated: the cleared-to-run line already *is* the run bound and the
user sets it at /plan. No second, softer cap is invented downstream of it. Every
run-length cap proposed so far has been a guess dressed as prudence, because Claude
has no live gauge of context filling at all — which is the whole reason
[statusline-context-reader] exists.

**The counter-evidence is kept rather than flattened into the decision.**
`resources/research/context-window-cost-memory-trajectory.md` finds that bigger
nominal windows do not mean bigger usable ones — models degrade well before the
advertised limit, and degrade even where retrieval is perfect. So "we have 1M" is
not itself proof a long run is safe. Separately, overnight blitz mode was dropped
on evidence that big unattended runs break their own rules; that finding is about
rule-following, not context, and the two arguments stay separate. Neither supports
a length *number*; both support a behaviour-based stop, which the method already
has in the no-progress halt. If long runs degrade rule-following in practice, the
answer is a sharper observed-behaviour stop, not a cap.

The run that built this was itself twenty-two items presented uncapped, which is
the behaviour the item wanted.

**Files touched:** `plugin/si-plugin/docs-b/next.md`,
`plugin/si-plugin/docs-b/done-build.md`, `SPEC.md`, `README.md`.

**FAQ: not needed because** the user-visible effect is the absence of a suggestion
they never asked for; SPEC and README both now state that /next works everything
marked ready, which is where a reader would look.

**Routed to Captures:** none from this item.
