# [HASH] — The five unaudited sub-docs read, and seven findings captured

The outside redundancy audit stated as its own limit that `next-build.md`, `next-audit.md`, `done-build.md`, `done-audit.md` and `done-plan.md` were never supplied to it, and that since `next.md` and `done.md` delegate substantial material to them it expected more duplication at those boundaries than it could see. This audit went and looked. All five were read in full; nothing was edited.

**Its scope had already narrowed on evidence gathered earlier.** Processing `[red-flag-lifecycle-restated-five-times]` had checked three of the five for that one rule and found all three pointing at `done.md` rather than restating it. So the expectation of heavy duplication at the delegation boundary was already partly refuted, and this pass started from that rather than from a blank assumption. `next-build.md` and `next-audit.md` were entirely unexamined until now.

**Seven findings, all approved as-is in one pass, none contested.** The strongest is that `done-build.md` and `done-audit.md` carry near-identical route-to-Unprocessed steps — same write-first justification, same fenced "the RECORD this step sweeps" block down to the conversation-memory line — which is duplication twice over, since that justification is separately canonical. Then the depth field defined in three places; `next-audit.md` restating the bulk-approval inversion's justification; `done-build.md` restating `next.md`'s no-subset rule in full; and three lower-rated findings in `done-plan.md` — the retired-headers rule, the four-way routing discriminator, and dependency ownership.

**Two findings are flagged at processing as possible promote-rather-than-cut cases.** `done-build.md`'s no-subset copy fires at a genuinely different moment from `next.md`'s, and a session at one moment does not read the other doc — which is the distribution shape, not the eviction shape. And `done-plan.md`'s routing table is flagged *against* an argument this same run accepted: `next.md`'s routing map was saved from the flavor-table cut precisely because a table is the operative form at the moment of application, and the same may hold here.

**So the audit's original expectation is confirmed for three docs and refuted for one rule.** `next-build.md`, `done-build.md` and `done-audit.md` do carry duplication at the boundary; the red-flag lifecycle, which it predicted would be among the worst, is clean there.

**A related finding was captured during an earlier build rather than here.** `done-plan.md` carries two more copies of the never-ask rule, found while building `[promote-never-ask-user-item-done]` and filed as `[never-ask-restated-in-done-plan]`. This audit would have found it independently; it is recorded once, not twice.

**Files touched:** none — read only: `next-build.md`, `next-audit.md`, `done-build.md`, `done-audit.md`, `done-plan.md`
**Routed to Captures:** `[route-to-unprocessed-duplicated-across-close-subdocs]`, `[depth-field-defined-three-times]`, `[next-audit-restates-inversion-justification]`, `[done-build-restates-no-subset-rule]`, `[done-plan-restates-retired-headers]`, `[done-plan-restates-routing-discriminator]`, `[done-plan-restates-dependency-ownership]`
**Approval outcomes:** all findings approved as-is

Rule gate: not needed — an audit edits nothing and authored no rule.
