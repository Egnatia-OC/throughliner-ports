# 16ed591 — The wind-down caveat is now a fixed sentence, because the version that described its intent got improved into something measurable-sounding and false

A session introduced the close's capture re-scan with "this has been a long session, so I can only re-read what's still in view." Session length is a proxy Claude *can* observe, standing in for the variable that actually determines the result — whether the conversation has been compacted — and that is not observable at all.

The shipped wording was already right. `plan.md` and `done.md` both said the step re-reads "whatever discussion is still in view" and that a surfaced-nothing result is no guarantee. The document did not fail; the session improved it into something wrong. That is what the fix has to stop, so the step now carries a sentence to state **as written** rather than a limit to convey:

> I can't tell whether any of our earlier conversation has dropped out of view, so this is what I could still see rather than a guarantee I've caught everything.

An instruction to "explain the limit honestly" invites the same improvement again, which is why paraphrase is the thing being closed off. Naming session length, duration, message count, or any other observable proxy is now explicitly barred.

On the underlying question the user asked — whether compaction is visible to Claude — the answer is no, not reliably. There is no signal announcing it. It is sometimes inferable from oddities, a summary block where an earlier exchange used to be or a session-start block arriving mid-conversation, but those are inferences from anomalies rather than a flag, and a compaction that lands cleanly leaves nothing to notice. The failure is silent in the same way a truncated file read is: what remains looks complete from the inside, which is the reasoning behind the page-the-whole-queue rule.

Why this is worth catching rather than shrugging at: a caveat's job is to tell the user how much to trust the result. "This session was long" invites them to discount it by a factor they can reason about, and the factor is fictional. "I cannot tell whether anything has dropped out of view" is less satisfying and is true.

The limit on the fix is written in beside it. A fixed string is harder to improve on than an intent, but nothing prevents a session rewording it and no check will catch that. This reduces the odds; it does not close the hole.

**Files touched:** `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none

Rule gate: not needed — an existing step's described caveat replaced by a fixed wording of the same caveat. No new obligation, no always-loaded change.
