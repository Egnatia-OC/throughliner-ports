# 3b094b5 — Subprojects: /setup gains a pop-out case, and upward-only holds are checked by reading the child's log

The user's design, for coaching clients with massive differentiated projects — business plan, software, timeline, contracts, client management in one project — where one subpart has become unmanageable and deserves its own queue.

setup.md gains a fourth folder state. Running /setup inside an already-adopted project is a pop-out: walk up to the parent's marker, read its SPEC, infer which subpart this folder covers, and put that to the user in clarifier form rather than proposing the answer. The irreversibility is stated plainly in the same confirmation — there is no scripted way back in — and at the close the pop-out message to the parent's INBOX is drafted, shown, and sent only on a yes. Case D takes precedence over the existing-content case, so a folder inside a project is not mistaken for a migration.

Two experimental parts from the original capture were resolved rather than built. **Mediation is the mailbox**: no session ever writes another project's queue, so a cross-boundary dependency travels as approval-gated mail the receiving project files with its own hands — which makes the risk evaporate rather than being made safe, and keeps the companion app out of the load-bearing path. **One-way blocking** was kept on examined grounds: cross-project loops become structurally impossible, the child never reads outward and gains no new steps, and nothing real is forbidden, since a child genuinely waiting on its parent uses the existing outside-the-project pattern.

No subprojects list is kept. A subproject is a subfolder and `session_start` already detects nested projects, so the set is recomputed from the filesystem each session — a list file could go stale, the folders cannot. The one circumscribed cross-read is in plan.md's below-line revisit: a parent item held on subproject work is checked by reading that child's log index.

The retrieve at planning found the prior visit this extends — July's nested-projects build. Multi-spec stays retired.

**Files touched:** `plugin/throughliner/docs/setup.md`, `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed — no session writes another project's queue anywhere in either doc.
Rule gate: run — amendments to setup.md's case detection, a pop-out case joining Cases A–C, and to plan.md's below-line revisit, one arm joining its check set; the one-way rule and mailbox mediation are design carried by the item, not new always-loaded rules. Nothing evicted.
