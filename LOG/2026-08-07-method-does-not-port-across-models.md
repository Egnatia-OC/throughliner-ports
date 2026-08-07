# 5993a10 — Ports don't preserve the method, stated in the form that survives the obvious counter

The user's own framing, from deciding what to say to a port's author: porting Throughliner means it *"doesn't respond right and you immediately have to start pulling threads and changing prose to find out why. it immediately becomes not Throughliner anymore… there is no method between that can be maintained perfectly. that doesn't exist, the codex port proved that."*

This was captured rather than assumed already recorded because CLAUDE.md and SPEC held the *decision* — ports are shelved, ports live downstream — and the two-docset design held the *premise* that different models need differently-worded rules. Neither stated the consequence: a port is not a translation job with a maintenance cost, it is a **different method wearing the same name**, and no amount of maintenance closes the gap because there is no neutral middle version to maintain toward. That is the claim that answers a contributor asking why their port cannot be merged.

**A tension in the record was found at processing and resolved as part of the build rather than walked into.** SPEC's two-docsets paragraph says the docsets *"carry the same method… so a project's behaviour does not change with the model it is built on"* — which reads as rewording *preserving* the method, while this item says it *is* a different method. A reader meeting both concludes one is wrong.

**They reconcile, and the reconciliation is the claim's strongest form — that is the version written, not the capture's.** The docsets carry the same method because somebody *made* them: one author, a known target, deliberate authoring by subtraction, and a fidelity audit with recorded restores where they drifted. Fidelity there is a **maintained property paid for continuously**, not a free consequence of careful wording. A port has neither the maintainer nor a neutral middle version to maintain *toward*. So the claim is not "rewording always changes the method" — it is **rewording changes the method unless fidelity is actively maintained, and a port has nothing to maintain it against.** That survives the obvious counter and leaves SPEC's existing sentence true.

Two homes, settled: **SPEC.md** as product truth beside the platform decision, because it describes a boundary of what the product *is*, the repo is public, and outsiders are who ask; and one sentence in **CLAUDE.md's Cross-platform ports section**, which recorded ports as shelved without saying why porting cannot work — so a session declining a port held the decision and not the reasoning. Plus a FAQ entry pair, since a non-coder asks "can I use this with another model or tool?" and that had no answer anywhere they would look.

**Deliberately not a separate public statement:** [rename-to-throughliner] owns the README positioning rewrite and should derive the outward phrasing from SPEC when it runs. A third copy written now would drift before it was read.

**Files touched:** `SPEC.md`, `CLAUDE.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`
**Routed to Captures:** none
**FAQ:** updated — new entry "Can I use this with a different AI model, or a different tool?" plus its index line
