# [HASH] — Untracked core docs detected at every session opening, with their consequences stated

Filed from INBOX mail sent by a consumer project, and **reframed at processing against the sender's own reading** after checking the source.

What happened there: a planning session ran to completion — a red flag cleared, three SPEC edits, eight work items, nine captures — and staging at the close revealed `.gitignore` carried `SPEC.md`, `QUEUE.md` and `LOG/`. The adoption commit's message says it wrote SPEC.md as product truth; that commit contains no SPEC.md.

**The reframe changes the whole design: this is not a fault, it is an offer.** `setup.md` already offers to add exactly those three paths to `.gitignore`. So a check asserting the state is wrong would fire on a configuration the method itself creates on request — and would fire hardest right after the user chose it. What was actually missing is that nobody was ever told what follows.

Three rules go quietly false, and one already knows how to handle it. Write-first's own test is *"is the previous version recoverable without the user's help?"* — and for an untracked file the answer is no. The rule always had the right test and never had the fact, so **where a doc is untracked its writes become show-first, by the existing test rather than by a new rule.** The other two are stated rather than repaired: a deleted queue item is not kept by git history, and the close's `git diff HEAD -- QUEUE.md` returns nothing, so its mechanical record of its own work falls back to memory.

**Detection goes in `session_start`, not in setup, and that timing dissolves the deadlock the sender hit.** Setup fires once, and the reporting project was already adopted, so a setup-only check would have missed the very case that produced this. Their close could not fix it either — the planning scope-lock refuses `.gitignore`, correctly, and the close marker's permitted list omits it — so it became a `[user]` line asking a non-coder to hand-edit `.gitignore` mid-close. Detected at the session's opening, before any work, the same walkthrough costs nothing and interrupts nothing. **Their third suggestion, adding `.gitignore` to the close marker's permitted list, is therefore refused** — it widens a deliberate refusal to solve a problem that timing solves.

One build detail worth recording: the check was first written inside the shared-working-tree branch of the isolation report, which would have hidden it from worktree and cloud sessions. It is emitted unconditionally instead, because the consequences hold whatever kind of checkout this is.

**Files touched:** `plugin/throughliner/hooks/session_start.py` (`CORE_DOCS`, `_untracked_core_docs()` using one `git check-ignore` call, and the plain-words consequences), `plugin/throughliner/docs-b/skill-nonspecific-rules.md` (write-first's untracked branch), `setup.md` (the offer states the consequences at the moment of choosing), new `resources/testing/test_session_start_untracked_docs.py` (7 cases against real temporary git repositories), `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies. **No epoch bump** — no file changes shape.

**Routed to Captures:** none.

Rule gate: run — **no new rule.** Write-first gains a branch from a fact it can now read, which is its existing test applied rather than amended; the rest is a hook check and honest wording. Nothing evicted. **One refusal on the record:** widening the close marker's permitted list, rejected because the deadlock is caused by late detection rather than by the refusal. Failure evidence is one consumer instance in which three always-loaded rules were false for a whole session and the red flag's informed-consent trail went into an untracked file.

Tick: done, confirmed — the new suite passes, covering each path alone, all three together, no repository at all, and unrelated ignore lines.
