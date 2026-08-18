# 7e3c1c8 — the close gets a permitted moment for the files its own obligations name

`pre_tool_use.py` gains `CLOSE_PHASE_FILES` — today just `README.md` — permitted only while this session's close has declared itself with a `.throughliner-close-active` marker in the scratchpad. `done.md` gains the step that writes the marker first and deletes it last.

The problem was structural rather than a scoping mistake. The README feature-list sync rides the SPEC-sync trigger, which fires at the close; /next self-scopes from the items it is about to build, and no item named `README.md` because the obligation is a consequence of several items *together*. The file could not have entered the list by any correct application of the scoping rule, and three genuinely required corrections were denied — one of them stale text about a permission that had already been withdrawn.

The item specified the permitted set but not how the hook tells a close from the build it follows; they share one working file, and the build's list is what denies the write. Settled by reusing /setup's declaration marker rather than inventing a mechanism, and it is strictly narrower: /setup's marker permits everything, this one permits a fixed short list. Driven both ways — README denied with no marker, allowed with it.

The cost is stated rather than discovered: a second list to maintain. A close obligation added later that names a new file must be added here in the same build, or the identical denial recurs one file over.

Rule gate: run — one entry on an existing standing-list mechanism; no new mechanism, no always-loaded rule.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `plugin/throughliner/docs-b/done.md`
**Routed to Captures:** none
