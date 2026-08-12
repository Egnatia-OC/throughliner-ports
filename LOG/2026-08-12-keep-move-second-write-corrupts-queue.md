# [HASH] — The keep-step's move is now three edits, because the two-write version corrupted the queue three times in one session

The move from Unprocessed to Processed was two writes in one turn: add at the destination, then remove the original. The order was right and stays right — an interruption between them leaves the item in Processed, where only a stale copy needs cleaning, rather than in neither section.

The failure was never the first write. It was the second, and it took three distinct forms in a single session. Once the removal matched the newly-written Processed copy instead of the original, silently undoing the move and leaving the file exactly as it started. Once it matched only the tail, leaving an orphaned heading and three paragraphs behind. Once the repair spliced a heading into the middle of a neighbouring item's paragraph, briefly making two work items unreadable as work items.

The cause is structural rather than careless. After the first write the file holds two near-identical copies differing only in their tail — the processed version's rationale is rewritten, the heading and opening paragraphs usually are not — so the most natural text to match is ambiguous by construction. The procedure already asked for care and got three failures from a session that had read it.

The move is now three edits: mark the original's heading with a unique placeholder, write the destination copy, delete the marked block by its now-unique heading. The marking edit's only job is to make the two copies tell each other apart. Destination-first safety is unchanged, and the surrounding paragraph explaining it was updated so the two do not disagree.

The digest re-run is now part of the step rather than a habit. All three failures were caught that way and by nothing else; it costs one command.

The evidential weight is stated in the doc rather than dressed up: the technique was found by trial in the session that hit the failures, and worked on every attempt afterwards — including the hardest case, moving an item to a different position as well as across sections. A handful of successes against three failures is a lead worth adopting, not a proof.

Routing the move through a queue tool was rejected as heavier than the problem: a second mechanism to maintain and keep in step with the format, where a sequencing change removes the hazard outright.

The limit, stated in the doc: this reduces a hazard created by two copies existing at once; it does not remove the window. An interruption between edits still leaves a placeholder-marked item in the file. That is ugly and obvious — and obvious is exactly what the current failure is not.

Written for a non-coder throughout: the two copies look alike, so the original is marked before the copy is written. No talk of string matching.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`

**Routed to Captures:** none

**Rule gate:** not needed — an existing step's mechanics changed from two edits to three. No rule authored, no obligation added, nothing in the always-loaded set.
