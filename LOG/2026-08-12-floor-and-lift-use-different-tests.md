# [HASH] — The below-line lift and the throughput floor named as different questions, stated once at the revisit

A clarifying clause, not a rule: it restates what two existing steps already do and adds no obligation, which is why it consumed no slot at the authoring gate.

**The confusion it removes.** The lift asks *has this already shipped?* and reads the answer off LOG. The floor asks *what can this session unblock?* and counts blockers **in Unprocessed only**. Read either alone, the other's criterion looks like an inconsistency — which is exactly what happened: the user inferred, reasonably, that a below-line item should only ever be blocked by something in Unprocessed, since a blocker in Processed would never be processed and the held item would never clear. The inference is wrong because a blocker in Processed-above is *built* by /next, leaves the queue, and the next revisit lifts what it held without /plan ever touching it.

**The block also names the case that genuinely strands work** — a blocker that is itself held below the line, a chain. One that terminates is slow; one that loops never resolves.

**Placed at Step 1's below-line revisit**, the earlier of the two both in the document and in a session, with the start-of-processing floor derivation naming it by reference rather than restating it.

**Live evidence from the session that settled it:** three items lifted at that opening purely on the shipped test, none of which the floor had counted, while the floor itself derived to zero on the same queue. The chain case occurred in the same session — [worktree-override-hook] was blocked by [concurrent-session-support], which was itself held below the line. It resolved by both being deleted, which is a resolution but not a reassurance.

**No FAQ entry.** Nothing user-facing changes: this clarifies reasoning Claude does, and the behaviour a consumer sees — items lifting when their blockers ship — is unchanged.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**Routed to Captures:** none.

Rule gate: run — admitted as a clarifying clause rather than a rule. It restates what two existing steps already do and imposes no new obligation, which is the shape the gate pushes toward and the reason it consumed no slot.
FAQ: not needed because the behaviour a consumer sees — items lifting when their blockers ship — is unchanged. This clarifies reasoning Claude does.
