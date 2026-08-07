# [HASH] — Promoted shared-scope grouping from a tie-breaker to the unit work moves and runs in

The item arrived as a cost complaint about the close reorder and was reframed by the user into something better founded: **group by shared scope, not by priority.** Work items whose file lists overlap are gathered so the group **moves into Processed together and runs as one unit**.

Two things that reframe closed, recorded so they are not reopened. The **cost question is dead**: a finding banked at the item's earlier skip established, by reading the shipped doc, that the close reorder is already conditional and change-scoped — it opens in bold saying so and carries an explicit silent-no-op branch for the common case. So the fix this item expected to propose was already built. And the **"what are priorities" question is dropped rather than answered**: groups are drawn from Files lists, which is mechanically derivable, so nothing has to be named or refreshed by hand.

**Why it is worth building.** Items touching the same files build better together — one coherent pass over a file instead of three sequential ones — and if they move as a unit that is one decision instead of three. The method already half-agreed: scope-sibling clustering existed, but only as a tie-breaker applied where it was free. This promotes it to the unit work actually moves in.

**The risk the design had to defeat is the exact thing the old tie-breaker bound was written to prevent.** If a group moves as a unit, an undesigned item can ride in on a well-designed sibling's coat-tails because it happens to touch the same file. **Sharing a scope is not evidence that work is ready.** So the group moves while every item in it still passes the keep-step on its own merits — the grouping changes the packaging, never the standard, and that sentence survives into the shipped text.

The precedence is unchanged and stated in all three places it now appears: dependencies first whatever the file scope, unblock-potential second, grouping third. Otherwise a blocking item is starved because it belongs to a different group, invisibly.

**One insight carried across from a deleted item, because this reframe is what dissolved it.** That item wanted /plan to file a forward handoff carrying per-item placement rationale so /next could *explain* the order. Under scope grouping there is no per-item rationale to carry: the ordering unit is the group and its reason is derivable from the Files lists at presentation time. So naming the group and its shared scope **is** the explanation — one line, derived on the spot, with no handoff artifact and no second advisory lifecycle to maintain. It is built into /next's run presentation and bounded to one line, since that step is `[BRIEF]` and carries a deliberate passage forbidding caveats there.

Prior art was read before designing rather than after: the reorder's narrate-don't-ask ownership and its unlock-potential principle both survive intact under grouping, so nothing settled was relitigated.

**Scope note:** the item's Files list omitted `next.md` while its own text explicitly required the run-presentation line. The described work is the contract, so the line was built; `next.md` was already in the run's file list.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/done-plan.md`, `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/docs-b/next.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
