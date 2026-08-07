# [HASH] — Turned the check-the-documentation rule inward onto the method itself, including claims made in passing

The rule to extend already existed and was quietly scoped wrong. The diagnosis-order rule says to check what a tool documents about itself before depending on its behaviour — and it is written throughout in terms of *external* tools, its justification reading that the tool is used by very many people while our own setup is the unverified thing. So it excluded the one tool Claude speaks about with the most authority and the least verification: **the method itself**, whose documentation is the procedure docs already loaded in the session. Nobody noticed the exclusion until the advice went wrong.

**The trigger had to be widened, and that is measured rather than feared.** A second instance was folded in at processing, and it happened *in the session that was processing this very item*, minutes after its rule had been authored. The wrong claim was **not advice at all** — it was a one-clause explanation offered while answering an unrelated question about queue counts. A rule scoped to advisory moments would not have caught it. So the trigger is any claim about what a skill, hook, plan or queue mechanism does, including one made in passing.

**The second limb is the one with consequences**, so it is stated separately rather than left implied: an inference built on such a claim is not presented as a finding or a recommendation until the claim itself has been checked. In the recorded case a false claim about what a run may build became a conclusion about where the project's bottleneck now was — a wrong premise stated in passing propagating into advice about how the user should change their working rhythm.

**A general "be careful" would not have caught the first instance either**, which is why the trigger is concrete. Claude enforced the plan/build boundary *correctly* one paragraph earlier; what it got wrong was narrower and less visible — **where work items come from**. The advice silently deleted the queueing step, turning a two-command rhythm per batch into a one-command one. A rule aimed at the boundary would have passed.

**The severity argument is about who catches it.** Both instances were caught because the person present develops the method. A consumer taking the same advice has no way to know it describes a capability that does not exist; they would build their project's operating rhythm around it, and the failure would surface much later as the method seeming broken rather than the advice having been wrong.

Placed on the existing rule so it inherits that rule's why, and repeated in plan.md where domain-mapping discussions actually happen.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/plan.md`

**Routed to Captures:** none
