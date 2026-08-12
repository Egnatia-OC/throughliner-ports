# e5d169b — The REPEALED signal reported 44 retired-term references and every one was noise

The item was filed on the board's report of 44 live references to retired terms, and it named two as genuine: `Blocks:` and `Depends on:` surviving in `done-plan.md` and `post_tool_use.py`. It also carried, honestly, that the others were "probably not faults" and instructed the build not to assume 44 defects. That instruction was the valuable part.

**Both named faults were checked and both are false.** `done-plan.md:49` is the line *"Do **not** reintroduce `Blocks:` / `Depends on:` headers"* — correct text saying the fields are retired, flagged only because "reintroduce" was not in the guard list. `post_tool_use.py:181` is the Python line `for b in blocks:`; the hook has no `Blocks:` field anywhere, its only dependency field being `BLOCKED_BY_LINE`. So there were **zero** genuine stale references in the whole corpus, and the entire item was detector-precision work.

Four distinct defects produced the 44:

1. **Colon-terminated field names matched as bare substrings.** `Blocks:` caught `for b in blocks:` and the prose "not only when it blocks:". A field name is now recognised only where a document actually names one — in backticks, bolded, or beginning a line.
2. **The retirement-context guard read a single line.** Prose splits sentences across lines constantly: *"still carry an `Editor:` … line — all three settings are retired"* puts the term and the word "retired" on different lines, so correct writing was flagged. The guard now reads the hit's whole paragraph, bounded structurally by blank lines rather than by a chosen window size.
3. **Archival files were scanned.** Research notes, captures, testing transcripts, the retired behaviour doc, INBOX archive and LOG all record what was true when written — editing a retired term out of one falsifies the record. They are excluded now, along with dated files at the top of `resources/` and this script itself, whose comments name retired terms as worked examples.
4. **No word boundary.** `docset A` matched the words "docset **and**" in this project's own CLAUDE.md — found only because the first three fixes left it as the last survivor.

Result: 44 → 0. The only real edits were two clarifications in `CLAUDE.md`: the example of an internal term to avoid named a document that no longer exists, and the docset-A sentence gained "— now retired, see below —" so it stands without depending on a later paragraph.

**The lesson worth keeping is about reading captures, not about this detector.** A capture's account of how a mechanism behaves is a claim to test, not a fact to build on. Building this item on its stated premise would have meant "fixing" two pieces of correct text and leaving the actual defect — a lint reporting 44 non-faults, which is the cry-wolf shape that teaches everyone to skim its output — completely untouched.

**Files touched:** `resources/rule_signals.py`, `CLAUDE.md`
**Routed to Captures:** none from this item
**Rule gate:** run — no rule admitted. The CLAUDE.md changes are two clarifications to existing text; nothing was added to the corpus and nothing needed evicting to make room.
