# 5993a10 — Eight cross-doc pointers repaired: four targets given the names they were already cited by, four citations corrected

About fifty cross-doc pointers resolved clean in the audit; these did not. The repair splits two ways, and choosing which way per case is the whole of the work.

**Named the target** where several docs cited a rule by a name the target never used — cheaper than editing every citation, and it makes the name real so a future compression pass can see it is load-bearing:

- **"stop self-sufficiency"** appeared nowhere in `plugin-behaviour.md`; the rule existed unnamed. It is now named in its own heading line, with a note that other docs cite it by that name.
- **"the Captures placement rule"** was cited by four docs; the target was an unnamed "**Placement.**" paragraph — one a compressor could rename, breaking four references invisibly. Now named, listing its callers.
- **"the diagnosis-order rule"**, cited from `plan.md`, was ambiguous between two different rules. The intended one now carries the name in its heading.
- **"the bulk-approval inversion"**, canonised by `next-audit.md` and `plan.md`, was a name the target never used (its own: result-set inversion, destination rule). Both names are now stated as one rule.

**Corrected the citation** where the pointer simply aimed wrong:

- `next.md` cited "plugin-behaviour.md (Context awareness)" as the canonical home of the don't-size-the-run trigger — that section is one sentence about resuming from `_build.md`. Repointed to the fresh-session-handoff bullet and `next-build.md`'s Context management section.
- `next-build.md` cited "the coherence rules", which exist nowhere as named criteria. The paragraph now says the test **is** the two conditions it already states, and says so explicitly so nobody goes hunting for a body of rules that was never written.
- `plugin-behaviour.md` named "the deep-research skill", which does not exist in the plugin or in harness naming the corpus can rely on. Generalised to the harness's subagent tool "whatever it is called in the build you are running", which is the durable form.
- `setup.md` pointed into `docs/` for migrate-checklist — the one docs-b→docs/ reference outside the sanctioned redirect, whose coverage rested on a generous reading of "wherever a skill names a procedure doc". It now points at the checklist in its own docset's folder, which is unambiguous under either docset. Verified after: no `CLAUDE_PLUGIN_ROOT}/docs/` references remain in docs-b.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/next.md`, `plugin/si-plugin/docs-b/next-build.md`, `plugin/si-plugin/docs-b/setup.md`
**Routed to Captures:** none
