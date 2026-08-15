# [HASH] — Every written shape measured, and every one of them roughly doubled in August

The user's question was whether Claude is mirroring the length it sees rather than writing what the matter calls for. That is not observable to Claude from the inside and is entirely observable from outside, so this measured it rather than designing a fix for an unestablished cause.

The script replays QUEUE.md's whole patch history — one `git log --reverse` plus a single `git cat-file --batch`, rather than a `git show` per commit — and reads every per-entry LOG file off disk, since entries are immutable and carry their date in the filename. It runs in under a second over 459 queue commits and 550 entries.

The finding is unambiguous. Planning entries went from a 323-word median in July to 895 in August, mean 1,010, longest 3,658. Build entries went from 229 to 478. Index lines went from a 40-word median to 76, with the longest at 337 words pointing at a 1,710-word entry. Captures nearly doubled at first filing, 176 to 336, and a work item now in Processed has typically gained another 141 words between being captured and being kept. That confirms the user's structural point rather than merely the mirroring hunch: the per-entry split shrank each entry's scope, and the entries grew anyway.

The script states no band and no threshold, which is the item's scope and also the point — this is the bloated corpus, so a range read off its middle would enshrine the bloat as the target. The band is derived afterwards, in conversation, from specimens judged good. A note in the docstring says so, because a future edit adding a "too long" column would make the finding worthless.

One coverage limit is stated in the output rather than left to be discovered: the queue used a different section structure before the two-section model, so snapshots older than 2026-07-02 parse to no items and contribute nothing.

**Files touched:** a new `resources/measure_written_shape_length.py`, its output at `resources/research/written-shape-length-growth.md`, and that file's line in `resources/research/index.md`.

**Routed to Captures:** none.

Rule gate: not needed for this item — it authors no rule. No rule text, no `docs-b/` file and no number was written; the wording this may later justify is a separate admission at the /plan session that reads the findings.
