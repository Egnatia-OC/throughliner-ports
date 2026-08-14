# [HASH] — Four shorter restatements in plan.md: two cut, one trimmed, one kept

Four audit findings grouped because they are one file and one pass.

**"Never build" is KEPT, and the audit's own hedge resolves against its finding.** The canonical rule says only that /plan plans and /next builds. This clause says something it does not: that work changing anything outside the quiet list is queued rather than done here, *whether or not it is code*. That qualifier is the operative content — it is what stops a planning session editing a doc on the grounds that editing prose is not building. Not a restatement, so not cut.

**The `[freeform]` definition is TRIMMED, not cut.** Its first two sentences reproduced the canonical statement including the identical example list and the identical reasoning about running the broken mechanism to build past it. Those went. What stays is everything canonical does not carry: that either the user or Claude may designate it, the placement rule with both ends and the reason for each, and the `Blocked by:` fallback for a genuine dependency.

**Filing-versus-processing is CUT.** Inside the doc that *is* the processing skill, "processing is /plan's" states the obvious, and its second sentence — that keeping or deleting is the user's decision — is separately canonical under dependency ownership. The canonical version is also the fuller one, carrying a consequence this copy dropped: that when the user runs a test and judges its outcome, that judging is the test work itself, not planning.

**Write-first is REDUCED to one operative line plus its existing pointer, not deleted.** The audit is right that the restatement was lossy — the canonical rule carries the recoverability test and this copy did not — but deleting the body outright would leave a pointer where a session needs an instruction. Showing text for approval before writing it is /plan's most common drift, and the one line that prevents it is *write, then report*. That line stays; the surrounding explanation goes.

**Files touched:** `plugin/throughliner/docs-b/plan.md`
**Routed to Captures:** none

Rule gate: not needed — no rule authored or amended. Two restatements evicted, one trimmed to its non-duplicated remainder, one refused for eviction on the recorded ground that it carries operative content the canonical rule lacks.
