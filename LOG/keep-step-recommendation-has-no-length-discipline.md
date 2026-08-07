# [HASH] — Named the keep-step recommendation on the lead-with-the-decision rule, as an ordering fix rather than a length cap

After a recommendation message presenting three response options with reasoning for each, the user replied only *"please summarise"* — and the shortened version conveyed the same decision in about a fifth of the words. Earlier in the same session they twice asked for plain summaries because the analysis was not readable on its own, and once said *"I just do not get anything you are talking about here."*

It recurred at its own processing, which settles it as a pattern rather than one bad message: partway through that session the user again replied *"please summarise the capture to me"* — same moment in the loop, same shape. Two sessions, three or more instances, one of them while processing the item about it.

**Distinct from the vocabulary item shipped in the same run, and the distinction is the point.** That one is about unfamiliar *words*; this is about *length and shape*. Both were live in the same session, and fixing the vocabulary alone would have left this untouched — a message can be entirely plain-worded and still be too long to act on.

**The cheaper option was taken deliberately: name the moment in the existing rule; do not give the keep-step its own shape.** Two reasons, and the second would not be obvious later.

1. **The both-limbs requirement genuinely needs words and must not be squeezed.** Stating which files change and what changes inside them is load-bearing — it is the check that stops undesigned work reaching Processed. A bespoke length rule at the same moment would pull directly against it.
2. **Two rules governing one moment is a design smell, because the one that fires is whichever was read most recently** — not a property anyone controls. Naming the moment inside the rule that already governs it leaves exactly one rule in force there.

**What was actually missing is ORDER, not a length cap, and the fix says so.** The evidence points one way in every instance: decision first, options as a short list, reasoning on request. That is the standing lead-with-the-decision rule, simply never applied to this message type. Framing the fix as a cap would be wrong as well as unenforceable — the failing message was not over some limit, it was back-to-front.

No plan.md change: the keep-step's own requirements are correct and stay exactly as written.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`

**Routed to Captures:** none
