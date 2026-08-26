# [HASH] — Cycles due-ness check given the trigger it never had: a hook facts line, and three doc steps that speak whether or not they file

The check existed at three sites and fired at none of them. Two live failures on the same installed plugin had already been recorded, and the diagnosis settled at processing was structural rather than a wrong computation: `session_start.py` never mentioned `CYCLES.md`, so a fresh opening's payload said nothing about the file, and each doc step was silent when nothing was due — which made a step that ran and a step that never ran produce identical output.

Both halves are now built. The hook reads `CYCLES.md` where it exists and emits one facts line naming each definition's slug, its cadence and what its observable currently reads, surfacing any date inside the observable as the last completed turn. The three doc steps — plan.md, next.md, done.md — key on that line and are brief whenever a doc exists, naming each cycle as due or not whether or not anything was filed. Filing behaviour is unchanged. A project with no cycles doc gets no line and pays nothing, which was the property worth protecting.

**The alternative weighed, and why it lost.** The hook could have computed due-ness itself and reported a verdict. It does not, and the reason is stated in the code: a cycle's observable can be a release date, a line in a sent register or a file's presence, and a hook that guessed at all of those would report a verdict it cannot stand behind. Facts to the hook, judgment to the skills — the same split the queue dependency facts already use.

done.md keeps a second trigger deliberately: it reads the project root itself as well as the opening's line, because a cycles doc created during a session carries no opening line and would otherwise be invisible to its own close.

Files touched: `plugin/throughliner/hooks/session_start.py`, `plugin/throughliner/docs/plan.md`, `plugin/throughliner/docs/next.md`, `plugin/throughliner/docs/done.md`, `resources/testing/test_session_start_cycles_facts.py` (new)
Routed to Captures: [spec-sentence-cycles-opening-line] — SPEC's session_start bullet says nothing about cycles, so it owes two sentences; filed rather than written, since a build never writes product truth.
Rule gate: run — amendments to the existing cycles-check steps, their named parent, across the three docs; the silent-when-clean arm for doc-present projects is evicted, replaced by one brief line naming each cycle due or not. No freestanding rule added.

Verified by driving `session_start.py` over two scratchpad fixtures — one carrying a demo-shaped `CYCLES.md` with a past-due observable, which printed the line, and one with no doc, which printed nothing — and by all six session_start suites passing. Depth: full, alternative seriously weighed. Ticked as done, confirmed.

[cycles-due-check-verification] is held on this item and may now be liftable; that is the below-the-line revisit's call at the next planning run, not this close's.
