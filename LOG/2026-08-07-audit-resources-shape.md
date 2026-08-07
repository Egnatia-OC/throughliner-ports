# [HASH] — resources/ brought back to the shape its own rule states, the mover's test suite wired into the rezip ritual, and scrub_sweep given its path

**The folder moved, not the rule.** `plugin-behaviour.md` says `resources/` holds research findings and re-read-later testing evidence and nothing else; `resources/captures/` existed with four files. The rule's stated reasoning is that `resources/` becomes a dumping ground without a hard limit, and a third folder of miscellaneous session artifacts is precisely that — so relaxing the rule would concede the thing the rule exists to prevent.

Each file was judged against the verbatim-re-read test rather than moved wholesale. All four are cited as evidence by LOG entries, which is the test being met: **three moved** to `resources/testing/` — two self-describing test-outcome records with verbatim transcripts, and the raw `.jsonl` an audit was performed from. **One deleted:** a preprocessed "slim" text derivative of that same `.jsonl`. Keeping both is redundant, and the raw file is the authoritative one — CLAUDE.md's own transcript-reading guidance says to read the raw `.jsonl` rather than a reconstruction. The folder is gone; `resources/` now holds only research and testing.

**The mover's test suite is not dead weight — it was wired up and extended, reversing the audit's framing on evidence.** The audit reported `test_reorder_queue.py` as guarding nothing, since no ritual, doc or queue item ran it. That was true and was the problem. But running it found it **passes**, with fifteen test functions including explicit marker-position cases — while the queue carried a live observed defect in exactly that area. So the suite was not stale; it had a specific coverage gap where the real defect lived, which is a much stronger argument for wiring it in than for deleting it.

It now sits in the rezip ritual beside `hook_schema_check.py`, with the same reasoning recorded: the mover is invoked many times per planning session, it rewrites the whole queue each time, and its failure mode is silent. The regression case was built with [mover-move-repositions-readiness-marker] — three cases targeting the anchor drag specifically, written from a live reproduction rather than the field report.

**`scrub_sweep.py` got its path written where it is actually invoked.** It was named by description in three places but its path appeared nowhere, unlike `reorder_queue.py`, whose invocations always give it — and this is a script reached for at exactly the wrong moment to be hunting for a file: when a privacy exposure has just come up.

**Two sites were left alone with the reason recorded**, per the leave-alone discipline this run built: `faq-template.md` and `SPEC.md` describe the sweep **to the user** rather than instructing Claude to run it, so a script path there is noise for a non-coder. The item's own test — "each invocation site that actually instructs a run" — is what settles it.

**Files touched:** `CLAUDE.md`, `plugin/si-plugin/docs-b/plugin-behaviour.md`, `resources/testing/test_reorder_queue.py`, `resources/captures/` (contents triaged, folder removed)
**Routed to Captures:** none
