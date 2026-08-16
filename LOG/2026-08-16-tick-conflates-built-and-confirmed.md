# d82f538 — The build tick takes two forms, so "written" and "ran" stop being the same mark

A consumer project reported closing a case where seven items had their code written and about to be committed, with confirmations outstanding. Neither of /done's two paths fitted: a partial close leaves those items in Processed, so the next run would present them as unbuilt and rebuild over existing code. They ticked and removed the seven — the building genuinely happened — and filed the outstanding confirmations as new items. Their general point, in their words: a build that ships code it never ran is not rare enough to leave to judgement, and the tick is the only signal, so it has to mean both.

**The finding that decided this arrives from the other end and is stronger than the report.** `done-plan.md` already carries a hold-back rule: an item whose prose names a slug that LOG records as **built but not yet verified** is placed below the readiness line. So a shipped safety rule already depended on the built-versus-confirmed distinction — and its input was whatever prose a previous session happened to write. The reporting project's complaint was that their eleven entries recorded it "only because a session chose to". The same gap, met from the consuming side: one rule writes the distinction by choice, another reads it as though it were guaranteed.

The tick now reads either `done, confirmed` or `done, UNCONFIRMED:` followed by what still needs running. The close transcribes whichever form it finds into that item's entry and **announces any unconfirmed items** rather than leaving the mention to judgment. `done-plan.md`'s hold-back rule was reworded to read that field rather than infer from prose, with an entry predating the field treated as unconfirmed.

**Why a second mark rather than requiring the LOG entry to say so.** Requiring the entry is effectively what the method already did, and it is what failed: an obligation discharged by remembering to write a sentence is indistinguishable from one skipped. The mark is written at the moment the knowledge exists — the build has just run or just not run the thing — rather than at the close, where it has to be reconstructed. Same reasoning that moved the rule gate's disposition onto the queue item.

The queue lint needed no change, verified rather than assumed: the tick lives in the build working file, which no hook parses.

Depth: short.

Rule gate: run — admitted as an amendment to `next-build.md`'s existing tick step, which already defined one mark and now defines two; no freestanding rule and no always-loaded slot spent. Nothing evicted, though the hold-back rule is reworded to read a field rather than prose, which makes it shorter and no longer dependent on a judgment. Failure evidence is two instances from opposite directions: a consumer project's seven items ticked with confirmations outstanding, and a shipped rule here reading a distinction nothing guaranteed.

FAQ: updated — "At the end of a build Claude told me some work was 'unconfirmed'. What should I do?", with its index line.

**Files touched:** `plugin/throughliner/docs-b/next-build.md`, `done-build.md`, `done-plan.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`, `FAQ/`.

**Routed to Captures:** none from this item. Their incidental observation — that a message is final the instant it is sent, with no warning that follow-up in place is impossible — was deliberately left out, belonging with the INBOX items rather than inside a change to the tick.
