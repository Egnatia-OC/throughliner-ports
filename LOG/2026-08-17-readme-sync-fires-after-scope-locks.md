# dc52025 — the close gets a standing permitted set, so a required write finally has a permitted moment

The README feature-list sync rides the SPEC-sync trigger and fires at the close, after scope is locked — so the file it names is always outside the run's list and all three genuinely needed corrections were denied. Not a scoping mistake: a run self-scopes from the items it builds, none of which named README.md, and none should have, because the obligation is a consequence of several items together.

Of the two narrow shapes the item offered, the first was taken with one change that makes it implementable. "The close may add a file when a close obligation names it" cannot be checked by the hook, which has no way to know which obligation fired — but the obligations are fixed and written down, so the files they name are knowable in advance. The close therefore gets its own small standing permitted set, held separately from the build's agreed list and widening it not at all. A build still cannot touch README.md; a close can, because the close is where the method requires it.

The third shape was refused, correctly, by the item itself: README is not host-only, so the reasoning that admitted `plugin.json` does not transfer.

The cost is stated rather than discovered — a second standing list to maintain, and a close obligation added later that names a new file must join it in the same build or the identical denial recurs one file over.

The user asked whether this also covers the rezip. It is the same shape and is already fixed: the hook permits `plugin.json` unconditionally, with the reasoning recorded in the code. Read rather than reasoned about.

Rule gate: run — admitted as one entry added to the existing standing-list mechanism; no new mechanism and no always-loaded rule.

**Queue changes:** [readme-sync-fires-after-scope-locks] kept into Processed, cleared to run.
**Work processed:** kept — [readme-sync-fires-after-scope-locks].
