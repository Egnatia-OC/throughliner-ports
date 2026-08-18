# 7e3c1c8 — the chat-level record gets its own entry when a close writes several

`done.md`'s LOG entry format gains one condition. A close writing a **single** entry keeps `Also in this chat:` inline, unchanged — every planning close is that case, so that path is untouched. A close writing **several** entries writes the chat-level record as its own entry, named for the chat rather than for a slug, with its own line in `LOG/index.md`.

The gap was that the section shipped against one entry per session, which is what a planning close writes. A build close writes one entry per built item, and the chat-level content belongs to none of them: on every entry it duplicates one text across twenty-odd files, on one it makes a later reader guess which. The close that first applied the rule put it on the first item's entry with a sentence saying so, and recorded that as arbitrary rather than a decision.

Both placement conventions were weighed and lost for the same reason — "the first entry" and "the last entry written" each attach chat-level content to an item it does not belong to, and then need a convention for a reader to find it. Its own entry matches what the content *is*, and it is findable the ordinary way.

The condition falls out of the close's own shape rather than being an exception: it reads off how many entries are being written and needs no carve-out. Cost: one extra file and one extra index line per multi-item close. Not a new kind of artifact either — a log entry with a different filename — so the index format is unchanged.

Applied for the first time by this close, which writes twenty-seven entries.

Rule gate: run — a condition on a section shipped the day before; nothing evicted.

**Files touched:** `plugin/throughliner/docs-b/done.md`
**Routed to Captures:** none
