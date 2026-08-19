# [HASH] — the planning record splits per item processed, settled by reading the code rather than weighing the wordings

Two statements disagreed: the always-loaded authoring standard says a plan entry splits per item processed, and `done.md` says per decision. The entry leaned toward per decision, on the ground that it survives a session settling several items together. Reading the code settled it the other way.

`queue_digest.py`'s `shipped_slugs()` resolves shipped-ness from **filenames** — `<date>-<slug>.md`, one directory listing. A slug has shipped if and only if an entry is named after it. So a decision settling three items produces one file named for one of them and the other two read as never shipped. The digest's shipped-citation flag misses them, and the below-the-line revisit — which reads shipped-ness off LOG to decide what may lift — would leave a held item waiting on a blocker that had in fact been settled. That is the failure this queue has recorded four times, reintroduced by a wording choice. Nothing about the argument is a judgment, which is what makes it stronger than the measured cost on the other side.

The measured cost is real and is not paid in full. The instance that filed this owed roughly 28 entries per item against 19 per decision, about 3,000 words plus an index line each. Where one decision settles several items, one entry carries the reasoning and its siblings cite it rather than restating it — each still named for its own slug, so every mechanical reader keeps working and the argument is written once. That is the relocate-and-cite pattern already used for research findings and for narrative moved into a chat entry, and this close is the first to apply it.

The entry's own premise was half wrong and was checked rather than trusted: it states that SPEC and `done.md` both carry the per-decision wording. SPEC says no such thing and never describes how a planning record splits, so the repeal is one file rather than two and no SPEC sentence was owed.

**Queue changes:** [plan-entry-split-wording-disagrees] kept into Processed, its premise corrected and its file list reduced to one document.

**Work processed:** kept — [plan-entry-split-wording-disagrees]. Deleted — none.
