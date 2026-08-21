# cc33c1e — Re-processing a layered queue item now rewrites it whole, and the advisory framing that stopped it is repealed

Build entry. The planning entry that processed this item is
`2026-08-21-processing-appends-where-it-should-rewrite.md`.

**Why this was worth doing.** The user asked whether a decision had landed: after the
ideation loop was made to write only on complete, she had asked that all planning work
the same way — the item under discussion rewritten in full at the end of each loop,
because it seemed to yield denser writing. It half landed. The ideation loop shipped,
and folding shipped as two typed operations (a merge rewrites the host item, a
supersession appends dated with why the old reasoning lost). What never existed is the
general rule. `plan.md` carried *"Read the ITEM AS IT STANDS, not the paragraph being
added"* and its own text marked it advisory — it "names an action and never blocks the
keep" — so the rewrite was reachable only through the merge branch, which fires only
where two paragraphs describe the same thing.

**The evidence is a session watched live rather than an argument.** In the planning
session that filed this, three items lifted from below the readiness line each gained a
settlement paragraph appended to prose written days earlier, and none was rewritten. A
fourth was rewritten only because splitting it triggered the merge branch. The rule the
user asked for would have fired four times and fired once. Against that,
`[split-action-defeats-the-bands-in-aggregate]` measured a queue growing 15% across one
session with the item count unchanged, because processing an item is what lengthens it:
every keep adds a settlement, a Files line and a disposition, and only building an item
out or deleting it shrinks the file.

**What was built.** The statement is now operative and carries its trigger inside it:
where an entry already carries a dated settlement or skip paragraph from an earlier
session, rewrite the entry whole rather than appending to it; where it does not, author
it as now. The advisory framing is deleted.

**Two bounds ride inside the operative sentence rather than beside it**, because a
rewrite that drops them is worse than an append: a defeated alternative and the reason
it lost survive the rewrite, and a paraphrase is never upgraded into a quotation claim.
Both are recorded failures, and the second was found live in this queue.

**The narrow trigger was taken over the general one.** Firing on every keep was
refused: on first processing a capture is authored into a work item, which is a rewrite
already, so a general rule would spend output on every item to change nothing on most.
The trigger reads a literal in the entry's own text and needs no judgment.

**Pointing the rule at the hooks' per-item word-growth report was refused**, and this
is the sharper refusal. That report already fires at the right moment and states no
threshold by design; a rule aimed at it would turn a fact into a target, which is the
circularity this project retired the word bands over.

The merge and supersession operations are unchanged — they are the folding case and
this is the ordinary re-processing case. `grep "names an action and never blocks the
keep"` in `plan.md` returns nothing. Statement count 312 → 311; the fall is the deleted
advisory clause, a deletion rather than a merge.

**Files touched:** `plugin/throughliner/docs/plan.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because a consumer's items get denser and they do nothing different.

Rule gate: run — admitted as an amendment converting an existing advisory statement at the keep-step into an operative one, subordinate to a step that already exists, sited in a fetched procedure doc so no always-loaded slot is spent. **The eviction is that statement's advisory framing** — "names an action and never blocks the keep" — repealed, with the action specified. **No figure is introduced.** Failure evidence is four re-processed items in one session producing four appends where one rewrite fired only because a merge triggered it, plus a measured 15% queue growth across one session with the item count unchanged. **A hook was considered and refused:** the growth report it would rest on states no threshold by design, and pointing a rule at it would make a fact into a target.

Depth: short. Built and confirmed.
