# f832385 — Check the documented contract before blaming or building on the tooling, and separate "it ran" from "it worked"

A session spent most of its length diagnosing a dead hook. Two hypotheses were built and argued in detail — that the app silently drops oversized injected context, and that it doesn't run these hooks at all. Both were wrong. The actual cause was our own hook emitting an output shape the harness doesn't accept, and one search found the documented contract and three matching reports in about a minute. That search should have been the first move, not the fourth.

The ordering rule now shipped: check our own conformance to the documented contract first, then look for the problem already being reported, and only then theorise about a fault in the tool. The default assumption is that we are wrong, because our code is unverified against the contract while the tool is used by very many people. That session inverted the default and came close to reporting someone else's tool broken for our own defect.

It was extended to design time at processing, and this build supplied the second instance directly: the docset detection was *built* on a field the documentation explicitly declines to guarantee, with the hook's own docstring citing the research that said so. Nobody read the contract at design time either. Two instances in one project makes it a pattern, so the rule covers depending on a harness behaviour as well as blaming one.

The most transferable part is stated as its own rule rather than a closing paragraph: **"it ran" and "it worked" are different claims.** Running the hook through the CLI with a hook-events flag showed its full output in the stream, and that was read as proof the injection worked. It wasn't — the flag echoes raw stdout whether or not the harness accepts it, and that run failed authentication before any model call. Paired with it: when checking, ask what actually arrived, never whether the result looks right, because the second question invites a plausible reconstruction indistinguishable from success.

The wording constraint mattered because this ships to consumers. A non-coder doesn't know what an issue tracker is, that one exists, or how to search it. The rule reads as plain guidance — check what the tool says it does, and see whether someone has already hit this — with the mechanics kept out.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md` (a new rule in the Research and evidence filing section, beside the research-offer rule it extends).
**Routed to Captures:** none.
