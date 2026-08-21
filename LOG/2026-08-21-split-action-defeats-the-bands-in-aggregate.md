# ae84933 — 360 log index lines rewritten by hand, cutting the retrieve's fixed toll by 27%

The build of [split-action-defeats-the-bands-in-aggregate].

**Why the index's length is a toll rather than a preference.** `LOG/index.md` is Claude-facing. It is read in full, by Claude, on every retrieve, so its total length is paid whether or not any line is useful. The extreme case the item cites is the argument in one line: a 337-word index line pointing at a 1,710-word entry, where reading the pointer costs a fifth of opening the thing it exists to save you opening.

**What was done.** Every line at or above 61 words was rewritten from its own text to the artifact touched, the nature of the change, and the entry filename. No entry file was opened. A long line is long because it restates the entry it points at, so the material for the shorter line was already in the line — which is what made this a rewrite rather than a re-derivation.

**The 61 selected the work list and was not a target to write to.** Each line was judged against the index line's own contract: does it carry enough to decide open-or-skip, and does it avoid restating the entry? That is stated in the item and it governs the result below.

**Measured before and after:**

```
entry lines           898  ->  898     (none lost, none added)
total words        52,115  ->  37,872  (-27%)
median line            51  ->  46 words
lines at/above 61     360  ->  52
commit hashes         398  ->  399     (none lost)
entry filenames       748  ->  748     (all resolve)
```

**The cut is 27%, not the "about 40%" the item's own heading predicted, and that is not rounded up anywhere.** Two reasons. The baseline had grown since the item was written — 52,115 words against the 48,165 it measured, and 360 target lines against 351. And the item's own instruction accounts for the rest: judge each line against the contract, never against a word figure. Lines in the 61–90 band carry real open-or-skip content and compress far less than the 200-word ones; squeezing them to reach 28,000 would have stripped the thing the index exists for. The 52 lines still above the cut-off are the compressed forms of the longest entries, where 65 words pointing at 2,000 reads correctly.

**Hash preservation needed a correction mid-build.** A first verification pass found 21 commit hashes missing — all of them secondary citations inside prose ("restored from `c4cf5af`", "the reverted merge cycle read out of `335fa97`/`7a4b377`/`7dd5d2b`"), never a leading hash. The leading hashes and every entry filename had survived intact. The item's acceptance says *every* commit hash, so each of the 21 was written back into the sentence it belonged to rather than the shortfall being explained away. The final count is 399 against 398, one higher because a repointing entry now cites a hash it previously only implied.

**Files touched:** `LOG/index.md` only. `git status` shows that file and no entry file, which is the item's stated boundary.

**Routed to Captures:** none from this item.

Rule gate: not needed — no rule authored and no always-loaded text touched. This rewrites a backlog of index lines against the index line's own stated contract: carry enough to decide open-or-skip, and do not restate the entry. Reworded 2026-08-19 — it previously invoked the index-line band, which [retire-word-band-caps-keep-measurement] retires. Transcribed from the item.

FAQ: not needed because this rewrites this project's own historical index lines. Nothing shipped changed and no consumer does anything differently.

**What this does not claim.** The saving is in what a retrieve costs to read, and nothing here tested whether the shorter lines still support the open/skip decision as well as the long ones did. They were written against that contract, one at a time, by judgment — which is the only instrument available, and is not the same as evidence.
