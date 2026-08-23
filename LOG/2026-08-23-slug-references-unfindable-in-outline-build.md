# [HASH] — A queue item named in output leads with its heading's words, slug after

The user's reported failure, repeatedly: she reads her queue through an outline view, the outline shows heading text, and Claude names items by slug — so the name given in chat is not a name she can find. The existing vocabulary rule only required saying what a slug is *for*, which explains the item without locating it, and explanation was never the missing half.

The fix reworks the vocabulary table's slug arm in place rather than adding a rule. It now requires leading with the heading's opening words — the same words the outline shows, which the put-distinguishing-words-first heading rule already front-loads — with the slug following for the record, and keeps the per-message scope the arm already had. Queue prose is untouched and the arm says so explicitly: slugs written into rationale stay bare, because a slug in prose is what makes a cross-reference exist at all and what survives a reorder.

Dropping slugs from chat entirely was refused at processing — the slug is what stays grep-able and what record traceability keys on.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, the Vocabulary section's third arm.

**Routed to Captures:** none from this item.

Tick: done, confirmed — the table still has three arms, the reworded arm names both the heading-first form and the per-message scope, and queue prose is explicitly excluded.

Rule gate: run — amendment to the vocabulary slug arm, parent named; the arm is reworded in place, nothing freestanding and nothing evicted. A recurring user-reported failure clears the more-than-once bar.

FAQ: not needed because this changes how Claude refers to items, not anything the user does.
