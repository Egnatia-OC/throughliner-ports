# [HASH] — Builds read the queue whole again; the generated view and build blocks are retired

A run used to read a generated file assembled from delimited `--- Build block ---`
regions, with the queue itself refused by the scope-lock. The reasoning was
structural rather than economical: a build transcribes what it reads, and
rationale written into work items had been measured reaching this method's own
shipped documents in near-verbatim form. Withholding the prose made that
impossible.

It worked, and it cost more than it saved. **A build that cannot see why a thing
is being built infers a why, and a wrong why aims the whole change wrong** — the
steps get followed and the point gets missed, which is a failure nothing
downstream catches because everything looks done.

So the withholding is replaced by a stated boundary. A run reads SPEC, then the
cleared region whole, each item's full text with its reasoning inline. The
reasoning is read **to aim the work** — it says what the change is for — and **the
action is what gets written, not the reasoning**. Reasoning lands in a file the
run writes only where that file is the record of the decision, which is the
session's own LOG entry, or where the item specifically instructs it.

**The cost is stated rather than hidden**, in the doc itself: the guard is now a
stated purpose rather than an absence, and a stated purpose can be ignored in a
way an absence cannot.

**Three alternatives were refused and are recorded.** Keeping the view but
carrying rationale alongside the block — the duplication survives it. Instructing
the build while still withholding the queue — the wrong-why inference survives it.
A per-step executable-or-checkable constraint — it duplicates the decision step's
existing two-limb check.

**What replaces the block, at the decision step**: an item's instructions are
ordinary prose naming which files change and what changes inside each, which files
are read but not changed, the observation that shows it landed, and any option
already refused. Written for a reader with less of the project in view and
possibly less capability — which is the same requirement the block encoded,
without the delimiters.

**Retired artifacts, deleted in this build:** `generate_build_view.py`;
`BUILD-VIEW.md` and its `.gitignore` line, here and in what `/setup` scaffolds;
and the generator's two suites, `test_build_view.py` and
`test_build_view_gate_disposition.py`. The suite count went 29 → 27.

**Two checks retired with it** — the queue lint's cleared-item-must-carry-a-block
check and the digest's matching report. Both are replaced by judgment at the
decision step rather than by another check: there is no block that can be missing
now, and whether an item says what changes inside its files is not something a
delimiter test can answer. Each site carries a note saying so, and the suites now
assert the **silence** — a leftover check would fire on every item in every real
queue from now on.

**FORMAT_EPOCH was NOT bumped, deliberately.** The epoch's stated test is whether
an existing project's files become structurally wrong, and they do not: old build
blocks survive untouched and read as part of the item, which is exactly how the
new model treats them. `migrate-checklist.md`'s epoch 4 section was refreshed
anyway to say the conversion is now a no-op and that old delimiters are left
alone.

**Files touched:** `next.md`, `next-build.md`, `plan.md`, `done.md`,
`done-build.md`, `skill-nonspecific-rules.md`, `setup.md`, `migrate-checklist.md`,
`pre_tool_use.py`, `post_tool_use.py`, `queue_digest.py`, `SPEC.md`, `CLAUDE.md`,
`.gitignore`, and two suites.

Verified: all 27 suites pass; the three hooks and the digest import cleanly; the
digest runs against the live queue with no blockless report; and no live reference
to the generated view remains outside retirement notes and epoch history.

**Routed to Captures:** none.

**Built last on the user's direction**, so the run's own machinery stayed stable
while the other twenty-three items went through — the view this run was reading
was produced by the script this item deletes.

Rule gate: run — supersession of the build-view architecture and of plan.md's build-block authoring rules; the purpose instruction and boundary rule are authored as amendments to next.md's existing run discipline; eviction is the block machinery itself.
Retired: the delimited `--- Build block ---` region as the thing a run builds from.
Retired artifacts: `plugin/throughliner/scripts/generate_build_view.py`, `BUILD-VIEW.md`, `resources/testing/test_build_view.py`, `resources/testing/test_build_view_gate_disposition.py`.
