# b4de5bf — Every documented queue-mover command checked, one syntax defect fixed and one silent hazard documented

`plan.md`'s below-the-line lift gave the invocation without the section name the script requires before `--move`. Run exactly as written it exits non-zero with a usage message and writes nothing.

That is worse than a typo because of how these are meant to be used: `plan.md` presents them as copy-and-run commands, and the always-loaded rules class a verbatim command as a paste target. A session following the doc precisely is the session that fails, and a session improvising succeeds. It also failed at the below-the-line revisit, a step /plan runs at every opening.

The item widened the build's scope deliberately: check every invocation, not just the caught one, on two axes — against the script's usage text, and against what each does when the held region is non-empty. Five were checked. `plan.md`'s `--delete`, `done-plan.md`'s full-order form and `next.md`'s `--delete` are correct as documented. Only the within-section `--move` had the syntax defect.

**The second defect is semantic and was invisible in the doc.** `--position BOTTOM --marker-after` is documented as the convenient single command for keeping an item and clearing it. `BOTTOM` means the bottom of the whole Processed section — which is *below* the held items — so the marker follows the item down and every held item lands above it, cleared. It happened during the session that found it: four held posts became cleared silently, caught only afterwards by the queue lint. The hazard grows with the held region, and nothing in the doc mentioned it.

Both fixes carry the same underlying correction: `--marker-after` names the last item that should stay cleared, never the item just placed, because the marker's correct position is defined by what should remain above it. That is now stated at both sites, with a two-branch safe form for the held-region case.

The code half of the same hazard is `[move-section-does-not-report-line-crossings]`, built in this same run, and the two were built together deliberately.

Rule gate: not needed — this corrects documented command invocations. No rule authored or amended.

FAQ: not needed because these commands are Claude's to run, not the user's; nothing they do changes.

**Files touched:** `plugin/throughliner/docs-b/plan.md`.

**Routed to Captures:** none.
