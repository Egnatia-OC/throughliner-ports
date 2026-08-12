# [HASH] — Six FAQ entries added for behaviours with no coverage, and the last surviving stale entry corrected

**Scoped from a comparison rather than from the item's own list**, as [faq-backfill-partly-overtaken] instructed. That capture was right: four of the five entries this item named as documenting retired mechanisms were already corrected in `08c885b`. The remaining job was coverage of undescribed changes, not correcting falsehoods — with one exception the capture did not know about.

**The surviving falsehood.** "Can I edit SPEC.md while doing a build?" still described the **retired spec-edit batch type** as the way to change SPEC. Rewritten to the three live routes: decided in /plan and edited there, discovered mid-build and asked for, or a large rework as ordinary work listing SPEC.md. The retirement is noted in the parenthetical the FAQ uses for this.

**One more stale vocabulary hit:** "What happens if Claude needs to touch something outside the current batch?" — retitled and reworded off "batch".

## The six new entries

Chosen by comparing the 24 existing entries against `LOG/index.md`, taking behaviours a consumer meets and the FAQ never mentions:

- **The forward advisory** — what "last session recommends starting with…" is, that it is orientation rather than an instruction, and that it clears itself.
- **Why Claude never asks whether a `[user]` step is done** — including that it checks an observable trace instead, and the deliberate gap that leaves.
- **Where a method or Claude Code problem goes**, as against an app problem — the three-way routing, and that nothing is sent without the exact text and a yes.
- **Whether the queue and log are safe to publish** — the honest answer, holding the never-claim-scrubbed line: the checklist and the shape-scan are described, and then plainly that neither can tell whether a sentence identifies a real person.
- **How to steer a planning session** — the four routes, why they are stated once rather than recited, and that "continue" is not approval of the next item.
- **The old-file-shape halt** — what the format epoch does, and that it stays silent when nothing would actually be wrong.

**Index reconciled:** one link renamed, six added.

**Two further entries were written in the same run under their own items** and are recorded there rather than here: the five-line LOG orientation read ([plan-reads-recent-log-index]), the keep-or-remove worktree prompt ([concurrent-session-support]), and the builds-read-SPEC change folded into the rewritten SPEC entry ([spec-is-write-only-during-builds]).

**Files touched:** `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none.

Rule gate: not needed — no rule was authored or amended. This is FAQ content: six new answers and two corrections to existing ones.
FAQ: updated — six entries added (forward advisory, the no-completion-ask rule, three-way feedback routing, publishing safety, the four planning off-ramps, the format-epoch halt), the SPEC-during-build entry rewritten off the retired spec-edit batch, and the out-of-scope entry reworded off "batch". Index reconciled.
