# [HASH] — Named the post-/done tail in the close routing, with a bounded cue and the safety half recorded as closed

Two halves, and one was already fixed before the build started.

**The safety half is CLOSED and must not be reopened.** The capture said the post-close tail runs with the file scope-lock fully off, so any file is editable and the user is never told. That was true when written. It stopped being true when `pre_tool_use.py` gained its planning-session file gate: with no active build there is no agreed file list, so a write outside the files planning touches by design returns **ask** — never deny. The hook's own note gives the intent: *"visibility, not containment: such a write should not be stopped, it should be impossible to make unremarked."* Verified by reading the hook rather than inferred from the commit.

Stated precisely in the shipped text, because the imprecise version invites a wrong reopening: **containment is still off after a close — nothing is blocked — but visibility is now on. The item's actual complaint was that the tail had neither.**

**What remained is the naming half, and it is genuinely small.** `done.md` did not name the post-close tail in its close routing, so a session reaching the end of one had to work out from scratch what kind of session it had become, landing on "a session that changed only the project docs" by inference. It still routes there; it just no longer has to derive it.

**The light-cue limb is kept bounded, and the bound is written beside it so a later edit does not harden it.** At most one line of awareness that captures filed after the commit are on disk and will ride the next session's commit. **It must never read as "you must run /done again"** — durability is already handled by the captures-filed-after-commit mechanism, and this exists to let the tail happen *gracefully*, never to add a re-close requirement.

**One insight carried across from a deleted item, because this is its proper home.** That item proposed a second, cheaper close path, and its hardest open question was *detection* — how a session would know it had already committed, which was going to need a session marker or a git-log comparison. **Naming the tail state dissolves that question rather than answering it.** If a cheaper close is ever wanted, it hangs off this named state as a *behaviour*, not as a second close path with detection machinery of its own. Recorded so the idea survives without a queue item and nobody rebuilds the detection — and it stays bound by the never-a-prerequisite rule: a lighter close is something the user may ask for, never something the method requires.

**Files touched:** `plugin/si-plugin/docs-b/done.md`

**Routed to Captures:** none
