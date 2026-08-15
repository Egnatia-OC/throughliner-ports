# [HASH] — Two shipped scripts now report what their writes did, saving the round-trips spent rediscovering it

Both gaps were measured rather than supposed. Deleting one item and repairing what followed took about ten round-trips for three edits' worth of work.

`reorder_queue.py --delete` said nothing about inbound references. It removed an item and stayed silent about the five items whose prose cited that slug; they were found by grepping afterwards and repaired across three passes, the first incomplete because the grep output was truncated. Two later deletes did the same, leaving dangling citations that had to be repaired by hand — four instances across three sessions. The delete path now names the items whose prose still cites the deleted slug, and deliberately does not assert the citation is wrong: a citation of shipped work is usually correct as written, while a citation of dropped work may leave the citing item's premise wrong, and the script cannot tell which happened. It fired on its own deletion during this run.

`queue_digest.py` named the phrase that fired a placement contradiction but not where it was. Three of the ten round-trips went on locating it, and the first repair fixed the wrong occurrence because the item contained the phrase twice. The flag now prints the line number and the matched sentence.

Merged in on the user's decision: the digest's files-named block printed `spec.md` and `claude.md` for files that are `SPEC.md` and `CLAUDE.md`, because each item's prose and files line are lowercased at parse time so the phrase checks can match case-insensitively — the paths rode along. An un-lowercased copy is now kept for rendering, leaving the matching path untouched. Merged because it was a third output fix to the same script, so one run opens it once instead of twice — which the digest's own files-named block is what flagged.

Recorded because it will be re-proposed otherwise: this is **not** a second instance of the general scripts-directory clause refused at `b4de5bf`. That refusal was about Claude not knowing a shipped script exists. Here the scripts were known, read and used correctly; they simply did not report what they had done.

**Files touched:** `plugin/throughliner/scripts/reorder_queue.py`, `plugin/throughliner/scripts/queue_digest.py`, `resources/testing/test_reorder_queue.py`

**Routed to Captures:** none

Rule gate: not needed — no rule is authored or amended. Three output fields are added to two scripts and no doc under `docs-b/` or `resources/` changes.

FAQ: not needed because both scripts are internal — a consumer never runs either directly.
