# f37e332 — Recorded in CLAUDE.md that docset B's monolithic plugin-behaviour.md is deliberate, so the split question stops recurring

Anthropic's skill conventions name progressive disclosure among the constraints the docset-B authoring item listed, and B kept docset A's monolithic shape anyway. Decided at /plan on 2026-08-02: don't split it.

**Why CLAUDE.md and not just a LOG entry** — the alternative, weighed and rejected. A LOG entry records that a decision was made and is retrievable, but it isn't read routinely, whereas CLAUDE.md loads every session. A decision that only needs to sit in the record belongs in the LOG; this one has to actively stop something recurring. The question has already been raised once by someone reading the file's length, and the next person to notice 785 always-loaded lines won't think to search the LOG first. Had it not already proved it recurs, the LOG alone would have been the right home.

**The decisive argument is what kind of content it is, not its size.** Progressive disclosure works for material looked up when triggered — a reference table, a rare procedure. It fails for standing behavioural rules, because those steer behaviour that happens with no trigger to fetch them. Most of plugin-behaviour.md is exactly that: Communication, response-shape tags, Captures, routing, scope, file safety. A session doesn't know to go and fetch "lead with the decision" — it either has it or it doesn't. Moving such rules behind an index doesn't defer their cost, it deletes their effect.

**The size premise is half-true and was measured.** Docset A is 373 lines / 89KB; docset B is 785 lines / 40KB. B's higher line count is an artifact of hard-wrapping at 80 characters — by bytes, which is what actually costs tokens, B is already 55% smaller than A. And the ~500-line figure in Anthropic's guidance is written for SKILL.md, the entry-point file, not for a reference doc a skill loads.

**The mechanism makes it worse here specifically.** Docset B is already reached by an injected redirect telling Claude to substitute `docs-b/` for `docs/`; [docset-routing-mechanism] exists because that indirection holds only as long as the model follows it. A split would stack a second redirect on the first — an injected index pointing at sections that must then be fetched — and a skimmed directive would leave a session governed by rules it never read, with nothing detecting it.

**The splittable minority is real but not worth it.** The red-flag lifecycle, working-mode rendering and the feedback channel are genuinely consulted on a trigger. Splitting only those saves little, costs cross-reference fragility in every doc that points into the file by section name, and leaves it half-and-half — harder to reason about than either whole.

Two reopen conditions are named in the CLAUDE.md paragraph: the redirect mechanism changing, or the trigger-fetched minority growing into a majority. Host-only — a decision about how the method is authored, not something consumers act on.

**Files touched:** CLAUDE.md (Model target section).

**Routed to Captures:** none.
