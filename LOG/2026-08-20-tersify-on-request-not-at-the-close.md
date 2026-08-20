# [HASH] — The tersify pass runs on request, never at a close, with its procedure on the shelf

Raised by the user as a step at the close, and filed against that placement on the evidence she then supplied. The write-up of the two passes is at `resources/research/tersifying-the-queue.md`, reproduced verbatim.

**Why not at the close.** Its measured yield was 8% then 3%, and its own conclusion is that the queue is not verbose — the length is accumulated decision history. Against that, a close already carrying the session's heaviest work would take on a whole-file read and rewrite. **And its two failure modes are the kind that must not run unattended:** a silent duplication of fifteen items that reading could not see, and a probable upgrade of a paraphrase into a quotation claim, one instance of which was found live in this queue and repaired the same day.

So `CLAUDE.md` gains a short entry saying a tersify pass exists, runs when the user asks for it, and points at the write-up. **The pass-2 method is mandatory when it runs** — item-level splice keyed by slug, unchanged blocks carried byte-identical, a slug-uniqueness assertion, per-block deltas so nothing grows silently — and pass 1's rewrite-from-memory is named as the method not to repeat. **Fenced blocks are untouchable**, on the write-up's §8d and [two-column-fences-wrap-unreadably].

**The close reports nothing about length**, revised by [retire-word-band-caps-keep-measurement], which shipped earlier in this same run. This item had given the close a breach report in place of the pass; with the ceilings retired there is no breach to report, and a distribution printed at every close would be a measurement nobody asked for at the moment they are least able to act on it. The on-request pass is the whole of what this item ships.

**Files touched:** `CLAUDE.md`. Host-only — the write-up is a dev artifact and consumers have no such pass.

**Routed to Captures:** none.

Rule gate: run — no rule authored for the corpus; one host-only entry naming an on-request pass and pointing at a procedure already on the shelf. **Nothing evicted.** The disposition is a refusal of the placement rather than of the work: at the close, rejected on measured yield and two unattended failure modes.

Tick: done, confirmed — the write-up it points at exists at the path named.
