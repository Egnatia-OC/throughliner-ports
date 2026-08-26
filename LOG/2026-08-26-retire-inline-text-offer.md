# 3b094b5 — The inline-paste offer is retired: pointing is now unconditional, with summaries serving the remote reader

Her decision, made in the session that designed summary-first consent. With every item's discussion now opening on an inline plain-English summary, the person reading on a phone is already served — so the chat-opening offer to paste doc-bound text inline, and the chat-held switch it turned on, no longer earned their place.

She accepted the cost by name: summaries replace verbatim. A reader away from the file sees the summary, not the exact wording, and seeing exact wording means opening the file.

The build removed the offer section from the always-loaded rules and every reference to the switch: the report rule's re-paste reservation, the view-in-doc override, plan.md's specimen narration and its two conditional arms, next.md's opening clause and render arm, next-build.md's reveal arm, and setup.md's retired-questions sentence. Pointing is now stated unconditionally, with no user override.

Two things went with the switch rather than surviving it. next.md's large-items advisory — the clause naming which items would swamp the run if displayed inline — had nothing left to condition, so it came out. And the build working file's `Edit display:` field, which existed only to carry the answer forward on a resumed run, was retired from both docs that referenced it.

Untouched deliberately: show-first-on-request, which governs approval timing rather than rendering and moves only toward more showing.

The planning session's repeal grep found no announcement ever claiming the inline offer, so no correction post is owed. The acceptance greps return no live-rule hits under `docs/`.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `docs/plan.md`, `docs/next.md`, `docs/next-build.md`, `docs/setup.md`, `CLAUDE.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an eviction from the view-in-doc rendering rule, its parent: the offer subsection and every reference to the switch come out; the summary-first consent rule shipped in [keep-approval-reading-burden] is the named replacement.
