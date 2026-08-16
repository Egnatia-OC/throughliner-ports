# 0e62afe — Two always-loaded statements evicted so the rules stop contradicting the work cycle they describe

A consumer project's user asked to plan and build in one chat and record both with one close. Claude opened with a concern, argued the method separates the two deliberately, and offered a truncated run as a compromise. It was reading the corpus correctly: the work cycle block lists /plan, /next and /done as steps and puts the loop's boundary after /done, while the parallel-sessions bullet glossed "don't cross plan and next" as forbidding mixed modes inside one session. Two always-loaded texts, read at every session start, disagreeing.

The fix was subtraction. The corpus already states the real rule precisely — "No planning work in any execution skill. The boundary is filing vs processing" — which is about doing planning work *during* a build, not about which commands may be typed in one conversation. So the bare prohibition and the session-level gloss both came out, and the third statement carries the rule alone. The work cycle block was not touched: it is the text that was right.

**The build's own wording then failed three times, and the user corrected each.** The first rewrite used "session" for both a chat and a run of a command — which is the ambiguity underneath the original bug, not a separate slip. Her instruction: say "plan session" or "next session", and "chat" for the conversation. The second carried forward a claim that concurrent chats are allowed; her decision is that they are not, because it was tried and never made to work, so the shared-tree / worktree / clone isolation block and its don't-interrupt paragraph were deleted with it. The third problem was shape: both rewrites were phrased as prohibitions, against the standing rule that a rule states the action it requires. The bullet now says one chat runs /plan and /next repeatedly, one after another; that /done closes the chat rather than a single run; and that a project is worked on from one chat at a time.

Two of those corrections were larger than this item and were filed rather than half-done: [session-conflates-chat-and-run] and [log-records-the-run-not-the-chat].

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`, `FAQ/faq.md`, `FAQ/index.md`, `plugin/throughliner/templates/faq-template.md`, `faq-index-template.md`

**Routed to Captures:** [session-conflates-chat-and-run], [log-records-the-run-not-the-chat], [terminology-corpus-audit]

Rule gate: run — admitted, and it is a **pure subtraction**: two always-loaded statements are removed and none is added, which is the eviction this corpus rarely gets. Failure evidence is one live consumer instance, brought by the user as a screenshot, plus a git check confirming the contradiction dates from `5234ec8` on 2026-08-12 rather than being long-standing. **Nothing is added, so nothing needs evicting to make room.**

FAQ: updated — new entry "Can I plan and build in the same conversation?"
