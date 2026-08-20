# b485ee3 — A build now reads a generated view carrying instructions and no decision history

Raised by the user as a read-cost saving and redesigned at processing once the rationale hypothesis was tested. The saving stands and is now the *second* reason. The first is that a build cannot transcribe rationale it was never given — and it does transcribe it, confirmed against git in `resources/research/rationale-flows-from-items-into-shipped-docs.md` rather than argued.

Each cleared item now carries a delimited build block — what changes in which files, the acceptance test, the red-flag state, and any recorded refusal — authored at the keep-step with the user present. `generate_build_view.py` copies those blocks byte-for-byte, keyed by slug, into a generated view, and lists every entry in both sections by heading and slug alone so a build filing something can still tell whether it is already queued. **Refusals travel and nothing else does:** a build that cannot see why an option was rejected proposes it again and stops to ask, which is the one interruption the saving would otherwise buy. The separation is authored rather than computed because telling history from instruction is a judgment — the same siting the rule gate uses, for the same reason.

The throughline rule is untouched. The queue keeps every item's reasoning inline and whole; the view is a projection, regenerated rather than merged, so nothing is reconciled back.

**Two conflicts surfaced during the build, and they are the substance of this entry.**

The item's Files line said the scope-lock should "refuse QUEUE.md to a build". Taken flat that breaks three shipped mechanisms: the per-item removal at each tick, capture-and-continue, and abort-and-requeue. The build halted and put it to the user rather than choosing. Narrowed on her approval to refusing a build's **reads** of QUEUE.md and its direct edits, leaving the queue tool permitted — which is what the item's own SPEC sentence asks for, *"A build does not read this file."*

The second surfaced while writing the close and was resolved without asking, because git answers it: the tick removes each item from the queue, so the close could never read its reasoning back. The run has not committed when the close runs, so `git show HEAD:QUEUE.md` still holds every built item whole. Where a project's queue is untracked that route is closed, and `done-build.md` now requires the close to say so plainly rather than imply the history was carried.

**Bumps the format epoch, 3 to 4** — every existing project's cleared items are structurally wrong until each gains a block, so `migrate-checklist.md` gained an epoch-4 section in the same build. A cleared item whose own prose never said what changes inside its files never passed the keep check, and the migration sends it back below the readiness line rather than inventing instructions for it.

**The capture-quality cost is recorded rather than denied.** A consumer project sent evidence deliberately ahead of this change. Two of its four limbs land, and both are queue-wide knowledge: knowing a capture is not already filed, and knowing what queued work depends on the detail. The heading-and-slug listing restores the first at almost no cost. The second stays lost — a heading says an item exists and nothing about what depends on it.

**Files touched:** new `plugin/throughliner/scripts/generate_build_view.py` (~290 lines); `plan.md` (the keep-step authors the block), `next.md`, `next-build.md`, `done-build.md`, `pre_tool_use.py`, `post_tool_use.py` (new check 8), `session_start.py` (the epoch), `migrate-checklist.md`; new `resources/testing/test_build_view.py` (16 cases), plus cases in `test_queue_lint_flags.py`; `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies.

**Routed to Captures:** none.

Rule gate: run — no freestanding rule. The build block is a clause on the existing two-limb keep check, which already governs what a kept item must state. **The eviction is the always-loaded assumption that a build reads QUEUE.md**, repealed across the readers named above. Failure evidence is two transcription cases confirmed against git, plus the measured proportion in one hunk: eight lines of rule against seventeen of explanation.

Tick: done, confirmed — five suites pass, and the generator was run against this live queue.
