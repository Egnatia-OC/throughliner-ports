# de2f5fc — The keep-step now checks the research shelf and cites rather than restates, and the digest prints each item's citations

An item restated the findings of `resources/research/llm-length-instruction-following.md` in its own words and never named the file. A later session read the item, believed it had the picture, and proposed a design the research had already refused. Restating research inside an item is what produces an uncited dependency, and a restatement reads as complete, so nobody goes upstream.

Two halves, and the reading half is what makes the citing half possible: you cannot cite what you never looked for. The always-loaded research rule fires *before offering a search*, which never engages when a session is designing from what it believes it already knows. The keep-step already had the right site — it asks what would answer an item's open questions — but every example it gave was an outside-the-machine fact, so the step ran and pointed away from the shelf.

Both halves ship as one clause rather than two, on the accumulation ground: five separate clauses were proposed for this one step in a single planning session.

The digest change is small and deliberate about what it does not do. `RESEARCH_CITE_RE` already existed and fed only the superseded-research flag; each digest line now also prints `Cites research:`. `index.md` is excluded from citations — naming the shelf is not naming a finding, and printing it would put a citation on every item that had merely followed the new instruction to go and look.

The limit is stated in the shipped text and in the digest footer rather than only here: nothing detects an uncited dependency. An orphaned-research check was refused on the cry-wolf ground recorded at `[disposition-detector-is-format-brittle]` — it would fire on nearly every file and be learned past. What this makes possible is a visible citation and a named fault for restating one, and it must not be described as closing the hole.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py` (new `research_cited()` helper; `Cites research:` on each digest line; matching coverage limit in the footer), `plugin/throughliner/docs-b/plan.md` (keep-step clause: check the shelf, then cite rather than restate; plus the stated limit).

**Routed to Captures:** none.

**Rule gate:** run — admitted as a subordinate clause on `plan.md`'s existing keep-step, which already governs what a kept item must state; no freestanding rule and no always-loaded slot spent. Nothing evicted. One alternative refused: an orphaned-research check, on the cry-wolf ground. Failure evidence is one recorded instance, in the session that filed the item.

**FAQ:** not needed because a consumer's actions are unchanged — the digest line and the keep-step check are both Claude-side.
