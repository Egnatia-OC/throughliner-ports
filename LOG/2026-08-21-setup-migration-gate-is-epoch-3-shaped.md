# [HASH] — /setup's migration gate tests for a queue shape no live project still has, so every epoch after 3 is unreachable

Alex asked how items had reached Processed without describing any work. The answer corrected Claude twice, and what survived is worse than what was first filed.

**Correction one: the items do describe their work.** Calling them underspecified was Claude's error, borrowed from the queue lint's wording. A cleared item kept before 2026-08-20 carries a "What changes" paragraph and a Files line — the two limbs the keep check asked for, honestly passed. What changed is the reader: the delimited build block shipped on 2026-08-20, `generate_build_view.py` copies that region byte-for-byte keyed by slug, and a run no longer reads QUEUE.md at all. Prose spread through a rationale cannot be extracted by that.

**Correction two, and it withdrew both faults Claude had just filed.** The first version of this capture said the format epoch was never bumped and no migration recipe existed. Both are false: `FORMAT_EPOCH` is 4 and its history comment defines epoch 4 as this exact change, and `migrate-checklist.md` carries a well-designed "Epoch 4 — build blocks on cleared work" section — lift the sentences the item already has, move an item that never said what it changes back below the readiness line rather than inventing instructions for it, do nothing to held items, captures, `[user]` or `[freeform]` work, and write the blocks with the user rather than for them. That capture was deleted and replaced by this item and its sibling.

**The single fault is the gate deciding whether the checklist is opened at all.** `setup.md`'s migration step loads it only for a queue in the old multi-section shape, and skips a queue that is already two-section. Two-section is what every project has had since epoch 3, so the gate now tests for a shape no live project still has and every later epoch's migration sits behind a condition that can only fail.

**Why it was written that way, which is not carelessness.** At epoch 3 the queue conversion *was* the migration, so "is the queue old-shaped?" and "is this project behind?" were the same question. They came apart the moment an epoch changed something other than the section layout, and nothing revisited the gate.

**The instance is this chat's own /setup run, observed end to end** rather than reasoned about — see `2026-08-21-setup-outstanding-here.md`. It skipped the checklist, converted nothing, and wrote the epoch marker, which is what silences the halt.

**What was refused, recorded because the intuitive move is the wrong one.** Adding epoch 4 to the existing gate as a second condition leaves the identical defect for epoch 5, which is how this one arrived. Detecting the shape by inspecting the documents was refused on grounds `CLAUDE.md` already records: it guesses about files users legitimately hand-edit.

Rule gate: run — no rule authored or amended; a condition inside one procedure step is replaced. The eviction is the queue-shape test, repealed outright rather than extended. Failure evidence is one instance, and it is this session's own migration.

**Queue changes:** [build-block-backlog-unmigrated] deleted as a wrong diagnosis and replaced by this item and [convert-cleared-items-to-build-blocks]; both kept into Processed and cleared.
**Work processed:** kept — [setup-migration-gate-is-epoch-3-shaped]; deleted — [build-block-backlog-unmigrated].
