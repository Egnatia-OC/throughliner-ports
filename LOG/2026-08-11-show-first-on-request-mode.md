# [HASH] — Show-first became available on request, and /next's inline edit display folded into the offer that already exists

Captured by the user, whose words were that showing then writing is a sometimes thing, for on request only, remote control or workflows where users may request it. Mixed authorship: the /next half is the user's design, reached by correcting Claude's framing in the interview; the /plan half and the distinction below are Claude's.

**The distinction the design rests on, stated first because getting it wrong produced the wrong question.** Claude's first analysis treated these as one switch and asked whether turning it on should make /next attended. The user caught it: **show-before-write is approval; show-the-edit is visibility.** Only the first gates anything. In /next the item is already approved and stop is always available, so displaying an edit waits on nothing and the run stays unattended. The two halves were therefore designed separately.

**Half one — show-first for doc writes, on request.** A session-scoped switch, not a stored setting. The precedent is the inline-text offer, held in the session and never written to a file. The method has retired stored mode settings twice — working mode and Editor — both because the stored field recorded something that was not stable about the user, and a show-first preference is less stable still: it is about where they are right now. Remote control is **not** a distinct trigger; it is a case where the user asks, so no detection is built to reach an outcome asking already reaches. The switch moves in one direction only, toward more showing, so the structural show-first cases stay show-first unconditionally — one test governs the floor and the switch is purely additive, which is what stops the two designs fighting.

**Half two — inline edit display in /next.** The user's design. The constraint is not attendance but **volume**: some items rewrite enough text that inline display would bury the run, and volume varies by item, so a blanket switch is the wrong shape.

It is **not a second question**, which was the user's correction to the first draft of this item. Line references are already the default in every skill, so the inline choice belongs bundled into the session's existing opening offer, where a user who does not care can ignore it. A standalone run-start question would add an ask to reach an outcome the existing offer already covers — the over-asking the method keeps removing.

The per-item advice fires only if inline is on. Once it is, Claude names the items it judges too large and recommends leaving those on line references, in the user's own framing: item 6 is very large, so I would suggest no inline for that one. That advice needs the run's item list, so it happens when the run is presented, not at the offer. The judgment is Claude's and is narrated, like any other ordering judgment.

**Both open questions were settled at build, as the item asked.** "Too large" is judged as a share of the item's own files rather than a bare number — [derivation-required-for-limits] would forbid a guessed threshold, and a proportion of the thing being edited is the honest measure. And the per-run answer is written into the build working file as an `Edit display:` line, so a resumed run carries it forward instead of re-asking; re-asking would reopen a decision the user already made and would do it at the worst moment, mid-run.

Default is off — line references only — matching the view-in-doc pointer default, so a user who says nothing gets today's behaviour.

**Files touched:**
- `plugin/si-plugin/docs-b/skill-nonspecific-rules.md` — the on-request switch; the opening offer extended to cover edit display.
- `plugin/si-plugin/docs-b/next.md` — the large-item advice at run presentation; `Edit display:` added to the working-file template.
- `plugin/si-plugin/docs-b/next-build.md` — the reveal step reads the run's answer, and records the visibility-not-approval distinction.
- `SPEC.md` — the write-first paragraph and a new paragraph covering both halves.
- `FAQ/faq.md`, `FAQ/index.md` — new entry, "Can I see text before Claude writes it, instead of after?"

**Routed to Captures:** none.

FAQ: updated — new entry "Can I see text before Claude writes it, instead of after?", covering both the on-request switch and the inline edit display.
