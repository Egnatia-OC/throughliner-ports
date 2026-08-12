# 0ae69d6 — The keep-check gains a mixed-item rule framed as a design question, plus a finding-versus-work clause

Two additions to `plan.md`'s two-limb keep-check.

**The mixed-item rule.** Where one item is half fully specified and half not designable yet, the mixed state is surfaced to the user as a choice about **designing** — *"shall we design the remainder now, or split it off?"* — never about **filing**. The rejected phrasing is named in the doc: "shall I split this item or keep it whole?", which is what was actually asked the time this was captured, and which hid the decision that was the user's.

If the answer is design-it-now, the item is completed in-session and kept whole. If it is split, the buildable half is kept and must pass both limbs on its own, and the undesigned half returns to Unprocessed with the design progress written into its prose and its own slug, cross-referenced from the kept half.

**The split's mechanics are pointed at, not restated.** They are the decomposition sub-step the document already carries for mixed Claude-prep-plus-user-action work — the same operation applied to a different seam. A second copy is what drifts.

**And the rule against papering over is stated explicitly**, because that is what actually happened: the captured instance was kept with its second half failing the second limb, held together by a close condition requiring the unbuilt half to be re-filed later. That is a workaround for a check that should have stopped the keep, and it ships an item that will stall a run.

**The finding-versus-work clause.** Ask what changes inside which files, get "nothing" back, and the item is a *finding* rather than work — its home is `resources/` or the LOG under the three-way triage. Previously an implication of the second limb that a session had to reach on its own; now said outright, at the cost of one clause.

**What was deliberately not built, recorded so it is not re-proposed:** extending the placement-contradiction detector's empty-file-list signal from Processed into Unprocessed. It does not transfer — in Processed an empty file list is a contradiction because the item is marked ready; in Unprocessed it is normal, since a capture is undesigned by definition, so the signal would fire on most of the section and be learned past.

**Files touched:** `plugin/si-plugin/docs-b/plan.md`.

**Routed to Captures:** none.

Rule gate: run — admitted on a recorded instance (the wrong question asked at [write-first-report-without-write], caught by the user). Modelled on the decomposition rule the same document already carries, and pointing at it rather than restating, so it adds a case to an existing shape rather than a new mechanism. Fetched doc, no ceiling cost.
FAQ: not needed because nothing user-facing changes — this governs a question Claude asks during planning, and the user experiences it as being asked a better question, not as a new feature.
