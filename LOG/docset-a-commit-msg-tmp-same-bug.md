# [HASH] — Corrected docset A's commit-message temp file to the session scratchpad, and removed a false claim about the scope-lock

`docs/done.md` told a closing session to write `COMMIT_MSG.tmp` into the project root, justified by a sentence saying the scope-lock is not active there once `_build.md` has been deleted. That sentence is **false about `pre_tool_use.py`**, the hook both docsets run underneath: the file scope-lock is indeed inactive with no active build, but the planning-session file gate then applies, and a write outside the small set a session touches by design returns *ask*. So the instruction produced a permission prompt at every close, on a step with nothing for the user to decide, at the very end of a session — where an unexplained prompt costs most, because there is no way to tell a routine mechanism from something going wrong.

**Why this was permitted despite the freeze.** The freeze bars development, not correction, and a frozen fallback that contradicts the hooks running underneath both docsets is not a safe fallback. This is that shape exactly.

**Two things settled the call.** The sentence is not merely dated — it is a false statement about shared machinery. And the counter-argument inverts on inspection: "nobody currently runs docset A" is true, but A's whole job is to be there on the day something goes wrong with B, which is precisely the moment a close raising an unexplained prompt costs most. A fallback that misbehaves only when it is finally needed is the worst available failure.

**The speculative counter was refused explicitly:** leaving a known-false instruction in place because a queued item might delete the file altogether is a bet rather than a decision, and that item is blocked behind a branch merge, so the wait is open-ended.

The scratchpad is also correct on its own merits, independently of the prompt: the behaviour rules already route every temporary file the project does not keep there, the hook treats it as always-editable, and the folder clears itself — so there is no deletion step to remember and no stray file left for a later session to puzzle over.

**Authored fresh in docset A's register**, never pasted from B. B is lighter by subtraction and the why-clauses it sheds are exactly what 4.8 needs to follow a rule reliably, so B's text imported back into A would regress it.

**Files touched:** `plugin/si-plugin/docs/done.md`

**Routed to Captures:** none
