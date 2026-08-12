# 0ae69d6 — The fold-the-recommend clause gains a hard precondition: agreement must be about this item, in this exchange

`plan.md` permitted folding a recommendation into the action *"when the user already agreed during the interview"*, and nothing in the clause bounded which item the agreement was about or when it was given. Claude treated the checkpoint's "continue" as that prior agreement — presenting the next item, recommending, writing it, moving it into Processed and reporting "kept and cleared" all in one turn, repeatedly, across most of a long session. The user's decision point disappeared.

**The precondition shipped as a typed block:** a recommend may fold only where the agreement was about **this** item and given in the exchange now happening. Not a prior turn, not an adjacent item, not a general "keep going", "continue", or "yes" answering a different question. Absent that, the recommendation stands alone and waits.

**The mechanism of the failure is named in the doc, because it is what a fix has to close.** The fold clause justifies itself on the ground that a keep can be reverted, so folding loses no decision. That makes folding **safe**; safety is not authorisation. Conflating the two is how a permission clause quietly widened into a default.

**The wording fix was weighed and NOT taken.** The candidate — that the checkpoint lists "continue" beside three options that genuinely are dispositions, so it reads as one of them — is true, and cheaper, and explains why the mistake is easy to make. It does not explain why the mistake was *permitted*, and that is the clause. A clause that permits the failure is not fixed by making the failure less tempting. The clarifying sentence about what "continue" answers was added alongside the precondition, so both halves are present without the wording standing in for the bound.

**It adds a bound rather than a mechanism** — restoring the default the document already describes, recommend then wait — which is the cheapest admissible shape and why it consumed no new slot.

**Built in one pass with [plan-still-carries-a-close-of-its-own]**, as both items required, since both edit the checkpoint's off-ramp list.

**Scale worth keeping in view:** the behaviour ran for most of a long session over a dozen items, and the user let it flow rather than interrupting each time, so the correction arrived as one late report. A rule written from a single caught instance would underrate how quietly this compounds.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**Routed to Captures:** none.

Rule gate: run — admitted, and the gate is what chose the shape. It adds a BOUND to an existing permissive clause rather than a new mechanism, restoring the default the document already describes (recommend, wait, act), which is the cheapest admissible form and why it consumed no new slot. Admission rests on a recorded instance running across most of a long session. The competing wording fix was rejected at the gate for not addressing what permitted the failure.
FAQ: updated — the "How do I steer a planning session" entry written under [faq-backfill] in this same run states that "continue" chooses which item comes next and is not approval of that item, which is exactly this rule's user-facing half.
