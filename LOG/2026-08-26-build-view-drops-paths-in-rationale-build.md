# [HASH] — Build blocks gain an optional Inputs: line, and a rule that anything the work needs to start travels in the block

Noticed while running this session's own transcript audit. The audit item named the
exact `.jsonl` paths to read, but those paths sat in its rationale prose rather
than its `Changes:` line — so the generated view, which carries the block and no
decision history, showed "preprocess both transcripts" with nothing saying which
two. The run had to open QUEUE.md to find them, against the standing rule that a
build leaves the queue closed.

This is the view's stated cost landing on a case its design did not anticipate.
The view drops history deliberately and that is not in question. What the instance
shows is that a path can be *instruction* while sitting in a sentence that reads
like *context*, and nothing at the keep-step caught it — the item passed the
two-limb buildability test perfectly well, because its `Changes:` line does say
what happens.

The cheaper of the two candidate directions won at planning. The block template
gains an optional `Inputs:` line for files the work reads but does not change, and
the block-authoring rule gains one sentence: anything the work needs in order to
start — paths, names, values — travels in the block, never only in the rationale.
A new limb on the buildability test was refused as duplicating that sentence at a
cost paid on every keep.

**Both acceptance conditions were checked rather than assumed**, and the checking
is the part worth recording. `generate_build_view.py` copies the delimited region
line by line with no per-field parsing, so an `Inputs:` line rides through
unchanged — and this run's own view proves it, since two of today's items already
carried one. The queue lint holds no list of block fields at all; its build-block
check looks only for the two delimiters.

**Files touched:** `plugin/throughliner/docs/plan.md` — build-block template gains
`Inputs:`, plus one authoring sentence.

**Routed to Captures:** none.

Tick form: done, confirmed.

Rule gate: run — amendment to the build-block authoring rule (template line plus
one sentence). The extra test limb was refused at planning as a duplicate.
