# [HASH] — A `[user]` walkthrough step names what to click and what to look for, not just where to go

A `[user]` item's walkthrough opened with "open your Claude Code session list". The run reached that step, gave it, and the user said she does not know how to find it. **Every other check had passed:** the item was correctly tagged, the capability check confirmed Claude could not do the work, and the walkthrough named an observable result. Nobody had asked whether the person doing it knew how to do the first step.

**What the existing checks cover, and why they are adjacent rather than overlapping.** The keep-step confirms a step *can produce the observation* the item names; /next's pre-hand-off runs the light capability check, asking whether a tool could do the work instead. Neither asks whether the user can carry the step out. A step can be perfectly capable of producing its evidence and still be unperformable by the person handed it.

**No new check anywhere. The existing walkthrough requirement is sharpened instead.**

The do-nothing candidate was weighed as the item asked, and it is half right: a walk-through stops for the user by design, so she was in the room, and the cost was one exchange. That is not an unattended run failing silently; it is a walk-through working slowly. The failure is cheap and no gate is warranted.

**But the defect is not a missing check, which is why "nothing" is also wrong.** The walkthrough was under-specified. "Open your session list" is a destination, not a step. A walkthrough naming what to click and what to look for would have worked with no check anywhere — and the existing rule already requires "which steps, in what order, what to check". It simply did not require the steps to be followable by someone who has never used that surface.

**Why this generalises rather than accommodating one person.** Every consumer of this method is a non-coder, and most will not have used the surface a walkthrough names. A step assuming familiarity is under-specified for the whole audience, not for one user — which is what makes it a rule rather than a courtesy. It fires at authoring time, where the cost is wording, and it replaces a question that would otherwise be asked per item.

**What it explicitly does not become:** a per-item can-you-do-this check, at either the keep-step or the hand-off. That is the over-asking this method keeps removing, against a failure costing one sentence.

`plan.md`'s keep-step was checked and found to *refer* to the requirement rather than restate it, so it gained a pointer at the sharpened rule and no second copy exists.

Depth: short.

Rule gate: run — admitted as a clause on the existing walkthrough requirement in the always-loaded rules; **no slot spent, because it sharpens a rule rather than adding one.** Nothing evicted, one alternative refused outright. Failure evidence is one recorded instance, thin and admitted as such on two grounds — the cost is wording at authoring time rather than a question at run time, and the affected population is every non-coder handed a walkthrough for a surface they have not used.

FAQ: not needed — walkthroughs get more specific; nothing the user does changes.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `plan.md`.

**Routed to Captures:** none from this item.
