# d82f538 — The shipped FAQ template is canonical and this project's FAQ is a copy of it, with the authoring rule keeping them in step

`CLAUDE.md`'s FAQ-entry rule told a batch to carry an entry into `templates/faq-template.md` plus its index line, and named nothing else. This project also has its own `FAQ/`, which `session_start` points every session at. So every entry authored under that rule landed in the shipped template and not in the FAQ this project actually reads. **The divergence was produced by the rule, every time it fired**, rather than left behind by an event — which is why it widened between two consecutive days of measurement.

The rule now names both: after writing an entry into the template and its index, re-copy both into `FAQ/`.

**`FAQ/` is kept rather than deleted, and that is the whole value of self-hosting.** The obvious alternative — delete this project's copy and read the template directly — was refused: `session_start` points every session at `FAQ/index.md`, consumers have `FAQ/`, and a host that reads its documentation from a different path than its users stops detecting anything about that path. A copy rather than generation, because the trigger already exists in the authoring rule and fires exactly when the template changes, so a copy at that moment costs one clause and no machinery.

**The salvage was larger than the item predicted, and that changed what had to be judged.** The item expected six unique entries, mostly older phrasings. The actual diff was **29**. Nineteen were genuinely older wordings of questions the template answers better and were replaced. **Nine were material the template had never carried** and were migrated in: the filing-claim check, the queue dependency facts line, why a planning session opens knowing recent history, the keep-or-remove prompt on an isolated session, self-contradicting queue items, why session records got shorter, message delivery guarantees, insisting on something mid-build, and the after-the-close tail.

**One entry was dropped rather than migrated, and it is the most useful thing this item found.** "Can I run two conversations on the same project at once?" answered **yes** and gave rules for coordinating queue edits between them. That permission has been withdrawn — the always-loaded rules now say one chat per project. Shown the entry, the user's reaction was immediate and in her own words: it *"has NEVER successfully happened and EVERY time we have tried to ship that behaviour, it has fallen over."* It never reached consumers: the template has no equivalent. The same advice survived in `session_start`'s payload and was removed by [session-start-advises-parallel-chats] in this same run.

The wholesale replacement of `FAQ/faq.md` and `FAQ/index.md` was shown before it happened and approved, being a conversion of a document the project owns. All four files now measure identical at 90 entries.

Depth: full — the item's premise about the salvage size was wrong by a factor of five, and one entry turned out to be actively wrong rather than merely stale.

Rule gate: run — admitted as one clause on the existing FAQ-entry rule, which already names a destination and now names both; no freestanding rule, no slot spent. Nothing evicted. Failure evidence is the measured divergence and its movement between two consecutive days.

FAQ: not needed for this item's own change — it alters where Claude writes an entry in the method's repository and nothing a consumer does.

**Files touched:** `CLAUDE.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/faq.md`, `FAQ/index.md`.

**Routed to Captures:** none from this item.
