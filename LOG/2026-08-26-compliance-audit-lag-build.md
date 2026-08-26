# [HASH] — Delta compliance audit of nine rule-bearing docs: 8 findings, four of them against this run's own rule text

Scope recomputed at run time from the record rather than taken from the filing, which is what the item required — this run's own rule commits had to be inside it. The boundary is the most recent compliance-audit record, `2026-08-24-compliance-audit-lag-build.md` at `3ed3db1`. The delta came to nine files: `CLAUDE.md`, and `done.md`, `feedback-and-inbox.md`, `next-build.md`, `next.md`, `plan.md`, `rescan.md`, `setup.md` and `skill-nonspecific-rules.md` under `docs/`, plus this run's uncommitted edits to six of them.

Axis stated before the first read, and it is the parent axis: each doc against `skill-nonspecific-rules.md`, and `next-build.md` against `next.md`. No sibling comparison was run.

**What the four lenses found.** One distribution failure: `plan.md` declares "the ready list" the standing plain-English name used in every session's asks, while defining it in the one doc that only /plan loads — /next and /done present the same region and cannot read it. One consistency failure: the issue-channel check speaks only when it files, forty lines from a cycles check rewritten this session to speak either way, on the reasoning that the first shape cannot be told from a check that never ran. One missing-tag cluster: `setup.md`'s whole Case D pop-out section is untagged, and two of its steps wait on the user. And four instances of decision history inside operative text, caught by the delete-and-read test — one in the always-loaded write-first rule, and three written by this very run, in the log-index read, the cycles step, and the delete branch.

**Flagging this run's own text was the contested call, and it was kept.** The alternative — audit only what was already committed — would have made the audit's boundary the session rather than the record, and the item explicitly recomputes scope so that the newest batch is covered. Three of the eight findings are therefore against text written hours earlier in the same session.

One finding sits outside the delta and is filed as such: the audit checklist's own doubled-rules table listed narration cadence as carried by the method's shipped file when it was not — coverage this run created and the table had been claiming for days.

**Clean passes recorded:** no residue of the retired inline-text offer anywhere in the shipped docs; `next-build.md` restates nothing its parent carries; `rescan.md` and `done.md` both correctly gained `[PROMPT]` on their candidate-set steps.

Files touched: none — an audit edits nothing. Read: the nine files above, at their committed and working-tree states.
Routed to Captures: [ready-list-name-defined-where-only-plan-reads-it], [issue-check-silent-while-cycles-check-speaks], [setup-case-d-untagged], [write-first-rule-carries-its-why-inline], [plan-log-index-read-carries-rationale], [plan-cycles-step-carries-dated-history], [plan-delete-branch-commentary], [audit-checklist-table-overclaimed-cadence]
Approval outcomes: all eight findings approved as-is, in one pass.
Rule gate: not needed — an audit authors no rules; it reads shipped text and files findings as captures.

Depth: full, reasoning contested. Ticked as done, confirmed.
