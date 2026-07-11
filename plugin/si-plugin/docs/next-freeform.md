# Freeform procedure

Execution procedure for `[freeform]`-flavor work lines. Reached from next.md when a freeform line comes up in the run, or when the user runs `/next freeform` on-demand and the gate has confirmed the work fits neither build nor audit.

Freeform is the loosest flavor: a place for unqueued or loosely-scoped work — an ad-hoc change, a discussion of edits already made, surfacing something without the pressure of processing it. It's a refuge from ceremony, not from discipline. The scope lock still holds, problems are still stated plainly, and nothing unrouted survives the session. What's relaxed is structure: there's no fixed work to tick line-by-line and no completion signal, because freeform work doesn't always know its own shape up front.

## Scope lock, ask-by-ask

A build line self-scopes to named files up front; freeform usually can't, because the work is discovered as it goes. So the scope lock grows by asking:

1. **Create _build.md** with an empty `Files:` section — the same structure next.md Step 2 uses, but with no files listed. An empty `Files:` locks the session to the method docs only (QUEUE.md, LOG/, _build.md), exactly as an audit's empty list does. (When freeform is reached as a line within a confirmed run, next.md has already created _build.md; grow its `Files:` ask-by-ask from here.)
2. **Each file the work needs is requested and added before it's edited** [PROMPT]: name the file and why it's needed, and on the user's okay, append its bare path to _build.md's `Files:` section — then edit it. The scope lock denies any file not yet listed, so the ask comes before the edit, never after. This is the build's "scope grows" ask made the normal rhythm rather than the exception.

## Do the work

Make the changes, have the discussion, surface what needs surfacing. Accumulate close notes in _build.md's Changes as you go — what changed and why — so /done needn't re-explore. There's no fixed work list to tick, so Changes is the record the session leaves behind.

State problems plainly as they come up. If something looks like a security, privacy, or breach risk, raise it as a red flag (plugin-behaviour.md Red flags) — freeform doesn't relax that.

## Captures can be made, never processed [PROMPT]

Freeform may surface ideas and observations. Making a capture — drafting its wording and appending it to Unprocessed — is open here, same as any session. Processing a capture — moving it into Processed or deleting it — is /plan's alone, and freeform doesn't change that.

So when the session yields captures, warn the user plainly: /next can file these to Unprocessed, but it can't process them — that waits for /plan. Then offer the choice: move this work to /plan now to process them, or continue here and let /plan pick them up later. Wait for the user's call.

## No completion signal

Freeform has nothing to tick, so there's no "all done" moment and no Completion section. The session closes when the user runs /done — that's the only close. The one close prompt Claude initiates is the standing context-running-long nudge: if context gets tight mid-session, suggest wrapping up the current thread and running /done, so the next session resumes cleanly from _build.md.

Do NOT delete _build.md yourself. That's /done's job.
