# [HASH] — A repealed sentence is grep-traced before its Files line is written

Filed by Claude from a failure observed twice in one run rather than reasoned about.

[spec-control-model-not-what-happens] repealed one sentence from the always-loaded rules and its Files line named that one file, stating in its own prose that "the defect is in the always-loaded rules, not in SPEC." The repealed clause was in fact restated verbatim in three more live places — `SPEC.md`, the shipped FAQ template, and the FAQ copy. The run therefore stopped twice to grow scope, in a run whose whole premise is that it does not stop.

The existing rule did not reach it. `CLAUDE.md` required a grep-traced ripple when an item changes a format or enum the hooks enforce; a repealed sentence is neither, though the trace is identical and just as mechanical. **And it needs no judgment: a repealed sentence is a literal string, so the item either grepped for it or did not.**

So: a third limb on the keep-step's two-limb check, **in the shipped doc rather than in this project's own file.** Where an item repeals or rewords a specific sentence or value, grep its distinctive words across the project before writing the Files line. That is where the omission happens, and a consumer repealing a sentence in their own SPEC has the identical problem — so a host-only rule would miss everyone the method ships to. Anything the grep finds that the item does not want changed is stated as an exclusion in its own sentence, outside the Files line, because the digest cannot tell an excluded path from an included one.

**The existing host-only rule is subordinated to it rather than left beside it.** `CLAUDE.md`'s hook-enforced-format rule traces the same ripple for a narrower trigger and adds one requirement of its own — that the grep name the enforcing hook — so it now declares itself a specialisation. **Two rules on one subject, at the same level, with no declared relationship is the exact signature the law-prose pass is being sent to find**; leaving them as peers would author the defect that pass exists to catch.

**Files touched:** `plugin/throughliner/docs-b/plan.md` (the third limb) and `CLAUDE.md` (the existing rule declaring the relationship). SPEC.md is not listed: it describes no part of the keep check, and how a Files line is derived is not product truth.

**Routed to Captures:** none.

Rule gate: run — a third limb on an existing check, subordinate rather than freestanding, so no always-loaded slot. **The eviction is the standalone status of `CLAUDE.md`'s ripple-trace rule**, which stops being a peer. Failure evidence is three instances: the repeal that stopped one run twice, and one session's seven-file repeal caught only because the grep was run by hand with nothing requiring it.

Tick: done, confirmed by reading both sites back and checking they now declare their relationship.
