# 5993a10 — /next got the red-flag backstop its behaviour rule already promised

`plugin-behaviour.md` says an uncleared flag in Processed should be impossible, so if /next meets one it stops and surfaces it rather than building. A grep found **zero** occurrences of "red flag" or "uncleared" across `next.md`, `next-build.md` and `next-audit.md` — **in both docsets**, so this was never implemented rather than implemented and lost. The /done side does carry it. The asymmetry was real and nothing on either side recorded why.

**The fork was whether the missing text is a missing implementation or a rule whose implementation is simply its residency in the always-loaded behaviour doc.** The alternative — adding a clause to `plugin-behaviour.md` saying /next needs no separate step — was weighed and rejected: it costs nothing and adds no duplication, but it leaves the next auditor finding the same gap and re-deriving the same answer.

**Implemented, the user's call, on this reasoning:** the red-flag posture is the method's actual risk guarantee — the thing standing between a security concern and its shipping unnoticed — and it is the one area where a should-be-impossible state earns a *visible* check rather than a trusted one. Making it explicit also settles the ambiguity permanently: the compression pass and every future audit see the rule and its implementation together, instead of inferring that residency was the intent.

**The cost is stated rather than glossed:** this is honest duplication, and it cuts against the compression pass the audit was run to prepare. Two sentences guarding a breach was judged the right trade.

`next.md`'s run-forming step gained an `UNCLEARED_FLAG` early exit alongside the existing ones, and a short branch that stops the run and states the risk in plain English — kept minimal, because the behaviour doc carries the full rule and this is the firing site, not a restatement. It names why meeting one means something went wrong upstream, and holds the flagging-not-fixing line: surface and route, don't quietly handle it.

**Docset A is not in scope:** this is new capability, which the freeze bars, and A's /next family has the same gap by the same never-implemented history.

**Files touched:** `plugin/si-plugin/docs-b/next.md`
**Routed to Captures:** none
