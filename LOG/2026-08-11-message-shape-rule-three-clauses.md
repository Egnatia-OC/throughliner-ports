# [HASH] — Two clauses added to the message-shape rule; the third was already shipped [message-shape-rule-three-clauses]

Merges three captures that turned out to amend the same rule — `skill-nonspecific-rules.md`'s "Shape every message the same way". The merge is Claude's recommendation, agreed by the user. Two of the three were originally theirs.

**Clause 1 was found already shipped, and not re-added.** It required the ask to sit at the end of the message. Checked against git HEAD rather than assumed: the wording "at the end of the message" is already there. Writing it again would have been the doubled-text defect the eviction rules name. Its origin stands as the reason the rule reads as it does — an audit once put the ask in the third line of a long message above thirteen numbered findings, the user answered "noted", and the run stalled until the ask was repeated alone.

**Clause 2 — the consolidated opening carries its own `[BRIEF]`.** The user's words: openings are getting long so we might need `[BRIEF]` labelling in more places. The pressure is structural rather than a slip. The consolidate-the-scans rule requires everything a skill's opening turns up to arrive in **one** narration — which is right, since several separate notifications would be worse — but the opening then grows with every check added to it, and checks keep being added. The individual scans are tagged where they run; the narration they feed carried no tag at all. Each part bounded, the sum unbounded.

**Clause 3 — a suppressed or `[SILENT]` scan contributes nothing to that narration.** Observed live: Claude narrated a scan the procedure says to keep silent about, and named a background-only setting while doing it. Mostly overtaken, since that setting is retired and the instance cannot recur — what survives is the general defect it exposed, that the consolidation invites a summary of what the scans surfaced and a silent scan gets swept into it. It belongs with clause 2 because it constrains the same sentence.

**Admission:** clauses on one existing rule, so no new slot — and this file is always-loaded, which is exactly where a freestanding version would have been expensive. Both original items independently reached that conclusion.

**What this session is NOT evidence for**, recorded so a later reader does not mistake it. The session ran with the bold ask at the end of every message and no misread off-ramp. That proves nothing: the user's global instructions and the active output style each independently assert the same thing, so no session in this project can tell which layer produced the behaviour. The clauses rest on the recorded instances, not on today.

**Files touched:** `plugin/si-plugin/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none from this item
