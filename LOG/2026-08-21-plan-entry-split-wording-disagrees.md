# [HASH] — The sibling-citation clause lands, and the item's repeal half turns out to have been a no-op against both files it named

**Why this was worth doing.** Filed at a close that had to choose between two live
statements. `skill-nonspecific-rules.md` says a plan entry "splits per item processed",
reasoning that a planning decision IS a disposition on a queue item, so the build case's
machinery applies unchanged. The item recorded that `SPEC.md` and `done.md` both said
"per decision" instead.

The difference is not cosmetic. They diverge whenever one decision settles several
items, which is common — the filing session settled two SPEC items together, five
mailbox items as one group, and two restyle items as a pair. Counted per item that close
owed roughly 28 entries; per decision, 19. At the measured 316–329 words per split entry
that is around 3,000 words, plus an index line each on a file read in full at every
retrieve.

**Why "per item processed" wins, settled at processing by reading the code.**
`queue_digest.py`'s `shipped_slugs()` resolves shipped-ness from **filenames** —
`<date>-<slug>.md`, one directory listing — so a slug has shipped if and only if an entry
is named after it. "Per decision" therefore breaks two mechanisms rather than merely
costing less: a decision settling three items produces one file named for one of them,
and the other two read as never shipped. The digest's shipped-citation flag misses them,
and the below-the-line revisit, which reads shipped-ness off LOG to decide what may lift,
would leave a held item waiting on a blocker already settled. That is the failure this
queue has recorded four times, reintroduced by a wording choice. Verified at build time:
`shipped_slugs()` is at `queue_digest.py:342` and does resolve from filenames.

**The premise correction, which is this entry's substance and is the SECOND one on this
item.** The item already carried a note that its claim about SPEC was false — SPEC never
describes the split at all. The same is true of its claim about `done.md`.
`git show HEAD:plugin/throughliner/docs/done.md | grep "per decision"` returns nothing:
the committed file read *"A build entry splits per item built and a planning entry splits
per item processed"*, which is already the wording the item proposed to repeal *to*.

So the repeal half was a no-op against both files it named, and the real work was the
sibling-citation clause alone. That was built rather than halting, because nothing about
what to build was in doubt — only whether half of it was necessary.

**What was built.** The entry-split provision gains a subordinate unit: where one
decision settles several items, one entry carries the reasoning and its siblings cite it
rather than restating it, each still named for its own slug so `<date>-<slug>.md`
resolves for every one. That is the relocate-and-cite pattern already used for research
findings and for narrative moved into a chat entry; nothing new is invented, and it is
how the measured cost stops being paid in full while every mechanical reader keeps
working.

**Siting the clause in the always-loaded file was refused** — the close is where it is
read.

**Files touched:** `plugin/throughliner/docs/done.md`. `skill-nonspecific-rules.md` and
`SPEC.md` untouched, as the acceptance test requires.

**Routed to Captures:** none from this item. The premise correction is recorded here
rather than filed, because the item is now built and gone.

FAQ: not needed because this changes how records are written, not anything the user does.

Rule gate: run — admitted as an amendment reconciling two live statements to the one already in the always-loaded file, plus one clause on `done.md`'s existing entry-writing step; no freestanding rule and no always-loaded slot spent. **The eviction is the "per decision" wording, repealed in two live files.** Failure evidence is one measured divergence and one mechanical dependency, the second of which involves no judgment at all.

**The disposition is transcribed unchanged and is now partly inaccurate**, which is
recorded rather than quietly corrected: it says the eviction is repealed "in two live
files", and in fact the wording was in neither. The gate ran at planning on the item's
stated premise, and the premise was wrong. That is worth a later reader knowing, because
it is an instance of a gate disposition resting on a false claim about the code — which
nothing in the gate's own machinery can catch.

Depth: full — reasoning contested: half the item's premise turned out to be false
against the committed file, so the build had to establish which half was real before
doing anything.

Built and confirmed.
