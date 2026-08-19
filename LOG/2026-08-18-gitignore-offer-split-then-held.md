# 02ec308 — the privacy offer splits per document, then is held the same day on a consumer report about the same code path

The user's question was whether QUEUE.md should be private by default. Her own objection defeated the default change — someone may want a visible queue for transparency — so the default does not move.

**The real gap turned out to be that the offer is bundled.** Scaffolding offers `SPEC.md`, `QUEUE.md` and `LOG/` as one all-or-nothing choice, so the combination someone most plausibly wants — plans private, history public — is unreachable rather than merely un-defaulted. Splitting the offer per document is the whole build, and it stays one question with three answers rather than becoming three questions.

**It was then held below the line before the session ended**, on mail that arrived mid-chat. A consumer project reported a planning session running to completion with all three documents gitignored: write-first, "git history keeps a deleted item", and the close's own `git diff HEAD -- QUEUE.md` were silently false for that whole session, including a red flag's clearance going into an untracked file. Setup checks that a `.gitignore` *contains* a `.throughliner/` line and never that it does not contain something fatal.

That is the same code path this item rewrites, so shipping a per-document offer while the check beside it cannot see a fatal pre-existing entry would put a second question in front of the user at the moment the first is already going wrong. The hold names [gitignored-core-docs] and the ordering is written into both entries.

**Queue changes:** [queue-privacy-default] rewritten, cleared, then moved below the line with a `Blocked by:` line.
**Work processed:** kept — [queue-privacy-default], held.
