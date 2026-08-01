# fa2f8e5 — Render-verification checks 1–3, six captures filed, and a Claude Code issue comment

Post-close tail after the 8-item build/audit run committed at `ea272f6`. Rezipped to 1.16.0-test1 and restarted onto the merged build. Began [working-mode-render-verification] as a `[user]` handover: checks 1–3 passed — a line-anchored doc link lands on the right line, an existing queue item renders as a one-line pointer/link, and a not-yet-written draft renders inline as text. Check 4 (the remote flip) was not run, so the item stays in Processed, partially verified. The check surfaced a significant finding: in the desktop app a `.md` link opens **natively in the app's own viewer at the right line**, not in the recorded editor — which questions the whole Editor-field / keep-a-reader-open premise.

Filed six captures (all post-commit, riding this close): [next-per-item-queue-removal], [user-line-underfiling-asymmetry], [claude-md-old-history-claim-wrong], [desktop-native-md-open-vs-editor-field], [approval-flow-token-doubling-simplification], [feedback-channel-claude-code-direction]. Investigated the pre-June history: both the local repo and the `FlintCraftTech/sovereign-implementer` GitHub repo start 2026-06-01, so CLAUDE.md's "pre-rebuild commits on GitHub" claim is wrong (captured). Posted a comment to `anthropics/claude-code#77134` on the approval-flow token-doubling "Direction B," then deleted an accidental duplicate of it.

**Queue changes:** filed 6 captures to Unprocessed; cleared the consumed forward-recommendation advisory ([advisory-next-cleared-doc-builds]) and filed a fresh one ([advisory-plan-captures-and-rename]).

**Work processed:** none (captures filed, not processed — that's the next /plan's job).
