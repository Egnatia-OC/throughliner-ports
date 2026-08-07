# [HASH] — Reversed the mover sequence to edit-then-move, so the file-changed-on-disk warning stops firing benignly

Twice in one session an Edit to QUEUE.md returned *"the file had been modified on disk since you last read it"*, both times caused by that same session's earlier mover run, which rewrites the whole file. Both were benign and both were verified benign.

**The concern is not the two instances; it is that the pattern is structural.** /plan moved an item with the mover and then edited the moved block in place — the prescribed sequence — so this fired on nearly every kept item. The file-safety rule correctly forbids reasoning past the warning, and states its own reason plainly: *"The innocent case trains the response to the dangerous one."* A warning firing several times a session, always innocently, is exactly that training happening on schedule. The rule is right; the frequency is what makes it fragile.

**Fresh evidence from its own processing session is stronger than the two instances.** That session processed seventeen dispositions, ran the mover on nearly every one, and the warning fired repeatedly — every time caused by its own mover run minutes earlier. Every occurrence was checked properly and every one was benign. **The session recorded the honest part: by the fourth identical occurrence the pull to skip the check was noticeable.** That is the training the rule warns about, observed rather than predicted, in the session processing the warning about it.

**The sequence fix was taken first, and the named-signature carve-out is the fallback, not the plan.** The two routes are not equal. A named benign signature is a **carve-out on a safety rule**, and every carve-out has to be drawn narrowly enough to keep catching the dangerous case — which here is real: a concurrent session's write once destroyed an item heading and reached a commit, and this warning is the layer that would have caught it. Writing an exception spends safety.

**Reversing the sequence spends nothing, because it removes the collision instead of excusing it.** Edit the block in place first, then move it — the warning never arises, so no exception has to exist and no judgment has to be made about whether *this* occurrence is the innocent kind.

The one constraint was checked against `reorder_queue.py`'s actual slug matching rather than assumed: the mover addresses blocks by the trailing `[slug]`, so that token must survive the edit. Slugs are immutable by design and survive reorders and renames anyway, so the ordinary keep — rewrite the description and rationale, slug untouched — is safe.

**The fallback turned out not to be needed at all**, which is the better outcome the item named: the sequence fix covers both sources, so the file-safety rule is left exactly as it is, with no carve-out written on it.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`, `plugin/si-plugin/docs-b/done-plan.md`

**Routed to Captures:** none
