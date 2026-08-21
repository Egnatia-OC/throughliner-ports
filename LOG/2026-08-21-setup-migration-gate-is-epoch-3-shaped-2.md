# [HASH] — /setup's migration gate stops testing the queue's shape and asks the question it means

Build entry. The planning entry that processed this item is
`2026-08-21-setup-migration-gate-is-epoch-3-shaped.md`.

**Why this was worth doing.** It came from the user's question — how did items reach
Processed without describing any work? — which corrected Claude twice: the items do
describe their work, and both faults Claude first filed were false. Recorded so nobody
re-derives them: the format epoch *was* bumped (`FORMAT_EPOCH` is 4, and its history
comment defines epoch 4 as the build block), and the migration recipe *does* exist
(`migrate-checklist.md` carries a well-designed "Epoch 4" section). What survived is
worse than either.

**The single fault was the gate deciding whether the checklist is opened at all.**
`setup.md` tested whether the queue used an old multi-section shape — Red flags,
Batches, Parked, Deferred tests, Captures — and skipped otherwise. **Two-section is what
every project has had since epoch 3.** So the gate tested for a shape no live project
still has, and every epoch after 3 sat behind a condition that could only fail.

**The live instance is this project, end to end.** /setup ran here, found a two-section
queue, skipped the checklist, and wrote `4` into `.throughliner-format-epoch`. It
converted nothing. The marker is what `session_start`'s halt compares against, so
writing it is what silences the warning — the project reported itself current while
cleared items sat in format 3's shape, and that run's close reported a clean migration.

**Why the gate was written this way, which is not carelessness.** At epoch 3 the queue
conversion *was* the migration, so "is the queue old-shaped?" and "is this project
behind?" were the same question. They came apart the moment an epoch changed something
other than the section layout, and nothing revisited the gate.

**What was built.** The gate now reads `.throughliner-format-epoch` against
`FORMAT_EPOCH` and branches three ways: behind → load the checklist and follow every
epoch section from the recorded number up to the current one, in order; equal → do not
open the checklist at all; no marker → the project predates it, treat as epoch 1 and run
the whole thing. The step's heading and lead sentence no longer name the queue
conversion as though it were the whole migration.

`migrate-checklist.md` needed one structural change for "every section from the recorded
number" to resolve: the previously unlabelled pre-epoch-4 material gained the heading
"Epochs 1–3 — the two-section queue" with its own applicability sentence, its two
sub-sections demoted so epoch sections are the top level, and its entry conditions
restated in epoch terms — with the old multi-section shape kept as an illustration of
the oldest case rather than as the test. "How to run it" now states the
run-every-section rule and the marker-written-last step.

**Adding epoch 4 to the existing gate as a second condition was refused** — it leaves
the same defect for epoch 5, which is how this one arrived. **Detecting the shape from
the documents instead of the marker was refused** on `CLAUDE.md`'s recorded ground that
it guesses about files users legitimately hand-edit; the refusal is written into the doc
itself, because extending or inferring are both the intuitive moves.

**The marker is still written last, at step 3a**, which this run's outcome shows is
load-bearing: the instruction to write it "once the conversions above have actually
landed" was satisfied vacuously when the gate skipped, because there were no conversions
to land.

**Files touched:** `plugin/throughliner/docs/setup.md`,
`plugin/throughliner/docs/migrate-checklist.md`.

**Routed to Captures:** none from this item. This project's own unconverted queue is
`[convert-cleared-items-to-build-blocks]`, filed separately — the repair here is the
recipe, and running it on this queue is separate work.

FAQ: not needed because this changes when a migration is reached, and the user's action
— running /setup when told to — is unchanged.

Rule gate: run — no rule is authored or amended; a condition inside one procedure step is replaced. **The eviction is the queue-shape test**, repealed outright rather than extended, and the refusal to extend it is recorded in the block above because extending is the intuitive move. Failure evidence is one instance, and it is this session's own migration, observed end to end rather than reasoned about.

Depth: short. Built and confirmed against the acceptance test: a project recorded at
epoch 3 with an already-two-section queue now reaches the Epoch 4 section, a project at
`FORMAT_EPOCH` opens the checklist not at all, and the marker is written only after
conversions land.
