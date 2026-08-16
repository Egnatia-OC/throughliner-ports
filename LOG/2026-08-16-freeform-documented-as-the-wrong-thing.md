# d82f538 — `[freeform]` reconciled to mean work done by hand, and the freeform close it named now exists

The user's account, in her words: freeform is not for running things alone, it is for big sessions or things that characteristically can't run within /next; the vast majority of freeform sessions are run by her ad hoc and never planned, and the tag exists so /done knows what it is looking at.

The shipped docs described something else — a work-item flavor marking work /next must not build, whose "defining case is a repair to the machinery /next itself uses". Different mechanism, different primary user.

**Three findings from reading the shipped text made this a reconciliation rather than a rewrite.** First, the docs already contradicted themselves one line apart: the flavor table says `[freeform]` is "work done by hand rather than by /next", which is her meaning, while the paragraph immediately beneath calls the machinery repair the defining case. So this was never her account against the docs — it was the docs against themselves, with her account matching the half already right. Second, `done.md` mentioned "a freeform close" exactly once, in an aside, and had **no branch for one**: it routed on the build working file, present meaning build and absent meaning planning. The job her account gives the tag as its main one was asserted in the shipped text and implemented nowhere. Third, the mechanism was not missing, only unnamed — SPEC already records that /done run on its own after hand edits records and commits them as the user's expected work. That is the ad-hoc path, working today and never called freeform.

So the paragraph now leads with the by-hand meaning, the machinery repair is demoted from definition to one example, `plan.md`'s placement guidance is prefaced as the uncommon case where a freeform item reaches the queue at all, and `done.md`'s router **names** its third no-build shape as the freeform close. The phrase was implemented rather than deleted, since a named route that does not exist is what produced the item. `next.md` was checked and left unchanged — its halt wording already said "done by hand rather than built from the queue".

**One consequence deliberately not acted on.** [runs-alone-premise-never-tested] records `[freeform]` being rejected twice as the vehicle for solo work because it "means something else", and those rejections did reason from the wrong definition. Their conclusion survives anyway: under the corrected meaning freeform is work done *by hand*, while `Runs alone` is work /next *should* build and merely must not share a run. Right for a wrong reason — do not reopen `Runs alone` on the strength of this.

Depth: short.

Rule gate: run — no rule admitted. **The eviction is the substance:** the machinery-repair sentence comes out as the definition and returns as one example, and `done.md` gains the route it named. Failure evidence is three artifacts rather than an opinion — the user's own correction, the flavor table contradicting the paragraph beneath it, and a session type named with no branch behind it.

FAQ: updated — "What is 'freeform' work, and when would I use it?", with its index line.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plan.md`, `done.md`, `next.md` (read, unchanged), `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/`. SPEC already carried the corrected wording from the planning session that settled this.

**Routed to Captures:** none from this item.
