# [HASH] — The close's forward recommendation gains a required disposition line, and the step leaves the file's tail

The build of [advisory-step-does-not-fire]. The planning entry under the same slug — `2026-08-21-advisory-step-does-not-fire.md` — records the item being processed; this one records it being done.

**What was wrong, restated from the item because the build view carries no history.** Alex noticed forward advisories had "stopped being a thing" and that she was having to ask for them. The diagnosis narrowed that: the recommendations were still being made and had stopped being *written down*. Measured from git across the last five closes, three filed nothing — and the step in `done.md` was intact the whole time, not repealed, not reworded, carrying its reserved slug and its conditions-not-counts rule in full. A correctly worded obligation with a stated site that does not fire.

**What shipped.** `done.md`'s advisory step now produces an artifact:

```
Advisory: filed — <slug>
Advisory: not needed — <why>
```

The label is written plain, matching the `Rule gate:` and `FAQ:` lines it sits beside, and the step states that a close does not complete until the line is written. The field was added to the session-record entry template so the close writes it where it already writes the others.

**The step also moved out of the tail, and the item is explicit that this is not the fix.** It sat at line 880 of a 925-line file. Position is a guess — a step skipped at line 880 can be skipped at line 400 — so the move earns its place only because the file was open anyway. The whole step now lives in the LOG-entry-files section beside the field it produces, with a four-line pointer left at the Recommend-next site, which is where the close learns whether its recommendation was concrete.

**One instruction in the item could not be followed as written, and the deviation is small.** It said the entry template gains the field "alongside the existing `FAQ:` line". There is no `FAQ:` line in the shipped `done.md` — FAQ-sync is a host-only obligation living in this project's own CLAUDE.md, so consumers never write one. The field went into the template section regardless, which satisfies the acceptance; the locator was simply wrong about what that file contains.

**Acceptance, checked rather than asserted.** `done.md` carries the step naming both forms; the entry template carries the field; `grep "Advisory:"` returns the two form lines and nothing else; the step now sits at line 245 of 950, comfortably out of the final fifty. Net +25 lines.

**Files touched:** `plugin/throughliner/docs-b/done.md`.

**Routed to Captures:** [spec-silent-on-advisory-disposition] — SPEC owes a sentence for the new line. The item's own text says no SPEC sentence is owed, reasoning that a line in a session record is implementation detail the SPEC admission rule keeps out. The build disagreed and filed rather than wrote, which is the correct move either way: a build never writes product truth, and the next planning session settles which reading is right. Worth noting that the disagreement is on the record from both sides rather than resolved silently.

Rule gate: run — admitted as a third subject on the existing close-line obligation shape, subordinate to a mechanism already shipped twice, and sited in a fetched procedure doc so no always-loaded slot is spent. Nothing is evicted, stated plainly rather than dressed up as a merge. Failure evidence is three misses in five closes measured from git, plus one instance observed end to end where the recommendation was made in chat and reached the next session only because Alex carried it by hand. A hook was considered and refused: nothing can detect whether an advisory was *owed*, since the trigger lives in the conversation, so a check would fire wrongly on every legitimately generic close. Transcribed from the item, not composed here.

FAQ: not needed because the item dispositioned it — "No FAQ entry, on the FAQ trigger's own test: a consumer sees one more line in their session record and does nothing different." This close initially reached the opposite conclusion, wrote an entry and reverted it; see `2026-08-21-chat-3.md`.
