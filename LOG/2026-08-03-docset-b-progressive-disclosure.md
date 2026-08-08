# f37e332 — Decided that docset B's monolithic plugin-behaviour.md is deliberate, and why

*Recovered 2026-08-09 after the emergency revert to `6ba51d3` discarded it. The original commit `f37e332` also wrote this decision into CLAUDE.md as a standing rule; that half was deliberately not restored — see the note at the end.*

Anthropic's skill conventions name progressive disclosure among the constraints the docset-B authoring item listed, and B kept docset A's monolithic shape anyway. Decided at /plan on 2026-08-02: don't split it.

**The decisive argument is what kind of content it is, not its size.** Progressive disclosure works for material looked up when triggered — a reference table, a rare procedure. It fails for standing behavioural rules, because those steer behaviour that happens with no trigger to fetch them. Most of plugin-behaviour.md is exactly that: Communication, response-shape tags, Captures, routing, scope, file safety. A session doesn't know to go and fetch "lead with the decision" — it either has it or it doesn't. Moving such rules behind an index doesn't defer their cost, it deletes their effect.

**The size premise is half-true and was measured.** Docset A is 373 lines / 89KB; docset B is 785 lines / 40KB. B's higher line count is an artifact of hard-wrapping at 80 characters — by bytes, which is what actually costs tokens, B is already 55% smaller than A. And the ~500-line figure in Anthropic's guidance is written for SKILL.md, the entry-point file, not for a reference doc a skill loads.

**The mechanism makes it worse here specifically.** Docset B is reached by an injected redirect telling Claude to substitute `docs-b/` for `docs/`, and that indirection holds only as long as the model follows it. A split would stack a second redirect on the first — an injected index pointing at sections that must then be fetched — and a skimmed directive would leave a session governed by rules it never read, with nothing detecting it.

**The splittable minority is real but not worth it.** The red-flag lifecycle, working-mode rendering and the feedback channel are genuinely consulted on a trigger. Splitting only those saves little, costs cross-reference fragility in every doc that points into the file by section name, and leaves it half-and-half — harder to reason about than either whole.

Reopen only if the docset redirect mechanism changes, or if the genuinely trigger-fetched minority grows into a majority.

**Why this is a LOG entry and not a CLAUDE.md rule (revised 2026-08-09).** The original decision put a ~250-word paragraph into CLAUDE.md so the question would stop recurring, reasoning that a LOG entry isn't read routinely while CLAUDE.md loads every session. That was rejected on recovery, for two reasons. First, CLAUDE.md loads every session, so an anti-recurrence rule spends tokens on every session to prevent a question that has arisen twice — the same accumulation pattern that took plugin-behaviour.md from 6,000 to 21,000 words and forced the 2026-08-09 revert. Restoring it would have repeated that mistake in the other always-loaded file, days after reverting for it. Second and decisive: the user identified that the recurrence isn't Claude spontaneously re-raising the split — it's the user raising it themselves while tired. A rule instructing Claude not to suggest something is aimed at the wrong party. What is actually needed is a retrievable answer, so that when the question is raised Claude can state the settled decision rather than agreeably re-deriving it. That is a record, which is what this entry is.

**Files touched:** none — the decision is recorded here only.

**Routed to Captures:** none. The queue item [docset-b-progressive-disclosure] was deleted, its content relocated here.
