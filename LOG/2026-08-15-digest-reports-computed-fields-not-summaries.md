# [HASH] — The queue digest gains three computed fields, and its first test suite

The digest printed enough for the droppable skim and the ordering, and not enough for the judgments a consolidation pass actually needs — so a pass that needed them read QUEUE.md whole, 175KB and roughly 56,000 tokens. Three fields close most of that gap without asking anyone to maintain anything, because all three are extraction from text already parsed.

Shipped citations are the one that matters. The always-loaded rules say status is re-derived from LOG, and nothing performed that sentence until now; entries are named `<date>-<slug>.md`, so resolving a cited slug against shipped work is a directory listing rather than a history scan. Only shipped citations print, on the user's decision at processing — an unshipped citation is the ordinary state and would appear on nearly every line for nothing, while a shipped one is the stale-premise tell. Age is one git pass over QUEUE.md's own patch history rather than a `git log -S` per slug, and it returns every item's first-seen date in well under a second. Files named by two or more items get a block of their own rather than a per-item field, since a file named once surfaces nothing.

Two false-positive classes turned up on the first live run and were fixed rather than tolerated. A backticked `/plan` was being grouped as a file path, so a path now has to end in an extension or a slash. And `[freeform]` in an item's prose resolved as a citation of a slug by that name — this project has a LOG entry that matched — so the three flavor tags are excluded from citations.

The fact-not-verdict constraint went into the script's docstring rather than into plan.md, because it binds whoever next edits the script rather than a session. Rungs 3 and 4 were checked at processing and stay distinct: unblock-potential asks who cites me, decay asks whether what I cite has shipped. Same citation graph, opposite directions, so one field feeds both and neither absorbs the other.

The digest had no test suite at all, so one was written rather than extended.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs-b/plan.md`, `SPEC.md`, and a new `resources/testing/test_queue_digest.py`.

**Routed to Captures:** [digest-lowercases-file-paths] — the files-named block prints lowercased paths, because prose is lowercased at parse time for the phrase checks and the paths ride along.

Rule gate: not needed — this authors no rule.
