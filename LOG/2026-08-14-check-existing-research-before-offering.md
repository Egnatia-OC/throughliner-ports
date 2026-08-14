# [HASH] — The web-search offer now reads the research index first, and the coverage limit is written into the rule

Alex's own words filed this: Claude should always check existing research before offering research. The instance behind it was a search offered and run on worktree isolation when `resources/research/worktree-isolation-and-desktop-sessions.md` already existed, dated three days earlier, citing the same two documentation URLs and reaching the same conclusion — and the duplicate missed what the file carried beyond the docs, that the contradiction had already been reported to Anthropic as a numbered issue.

**The clause hangs off the search-offer trigger, not the research-filing section**, and that placement was settled at processing rather than here. Filing is the write path and it already works; the duplication happens at the moment a search is offered, so a clause attached to filing would sit after the waste has occurred.

**The wording changed because the research index shipped first.** The item was originally held below the line behind `[research-folder-index]`, on the reasoning that building it first would ship wording stale on arrival — a rule saying "list the folder and match filenames" would be obsolete the moment an index existed. The index landed in `78fa417`, the item was lifted, and the shipped rule says to read the index and open any entry whose *subject* covers the question. That is a better rule than the one originally designed, and the hold is why.

**The limit is written into the rule rather than left implicit.** An index line describes a finding's subject, so this reaches more than filename-matching would — but a finding whose index line does not describe the subject in the terms the question later uses is still missed. The rule says so. This project's standing position is that a check which over-claims makes the corpus look guarded when it is only partly guarded, and the same applies to a rule describing its own reach.

**Why a one-instance rule was admitted at all**, against a gate that normally asks for a failure seen more than once: the failure is silent by construction. A duplicated search returns a plausible answer and looks exactly like success, so instances do not accumulate visibly — waiting for a second one means waiting for a second one that gets noticed, which is a different and much rarer event.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`
**Routed to Captures:** none

Rule gate: run — admitted as an amendment to the existing web-search-offer trigger, written as a subordinate clause of it, so no slot is spent. One pointable failure, which is fewer than the gate's usual bar, admitted anyway on the silent-failure ground above. Always-loaded is correct: a session cannot fetch a rule telling it to check for a rule. Not hookable — no tool call marks the moment a search is about to be offered.
