# 455082b — Retired the push marker — and found two of that item's three claimed SPEC divergences were false

The item claimed three places where SPEC described a model the package doesn't ship. Checking each before editing — the discipline the sibling item in this same run was built to install — found only one was real.

**Divergence 1 (completion mode) is false for docset B.** The item said both docsets still ship the setting. Docset A does, in full: `docs/plugin-behaviour.md` §42–49, `docs/plan.md`'s Step 1 sweep, `docs/done-plan.md`. Docset A is frozen, and that is the question [docset-a-completion-ask-inconsistency] already owns. But docset B's only mention is a rule stating the setting is retired and a stale line should be ignored silently — which *agrees* with SPEC. `docs-b/done.md` and `docs-b/done-plan.md` contain no completion-mode text at all, contrary to the item. The claim came from grepping for the string rather than reading what the text says.

**Divergence 2 (stale-item retirement) is false.** SPEC does not describe a repeat-count mechanism. It says "when the same item has come back across several sessions without moving"; `docs-b/plugin-behaviour.md` says "after the same user-only condition has been asked about across several sessions with no change." Those match, and neither is a count.

No edit was invented for either. Manufacturing changes to fit an item's stated shape would have made SPEC worse to satisfy a premise that had already stopped being true.

**Divergence 3, the push marker, was real and is now retired.** `docs-b/plan.md` and `docs-b/done-plan.md` listed it as one of three dependency routes; `docs-b/next.md` said it was gone. So /plan placed a marker /next ignored, and an item needing a shipped, reinstalled host got built against the old host silently — with the wrong results reading as the design being wrong rather than the sequencing having failed. This project's own CLAUDE.md asserted the halt for months.

The user's call was option B: delete the route. It removes a mechanism rather than restoring one, it is the direction next.md already took, and the readiness line is the gate the method actually maintains and surfaces at every close, whereas the marker was maintained in two docs and honoured in none. The dependency model is now two routes: `Blocked by:` for queued work, a lift-condition below the line for everything else, with "waiting on a shipped host" simply being one kind of external event.

The cost is real and is written into every doc that carries the change rather than glossed: mid-run sequencing is gone. A run can no longer be "build these three, push, then build these two."

Scoped by the literal-value grep, which is what caught `AGENTS.md` — a near-duplicate governance file that would otherwise have kept asserting the retired behaviour.

**Files touched:** `SPEC.md`, `docs-b/plan.md`, `docs-b/done-plan.md`, `docs-b/plugin-behaviour.md`, `CLAUDE.md`, `AGENTS.md`, `templates/faq-template.md`
**Routed to Captures:** none from this item — both false premises are recorded here rather than as work, since neither leaves anything to do
