# [HASH] — FAQ-sync reframed from a soft confirm into a hard /done close gate requiring a logged disposition line

The FAQ-sync clause added on 2026-07-30 failed on its first real test. It rode the
SPEC-sync close trigger and asked the close to "confirm the FAQ entry was written"
— and a close ran that synced SPEC, skipped the FAQ, and left no trace of the
skip. It had borrowed SPEC-sync's trigger but not its teeth: SPEC-sync works
because it is a blocking gate whose result lands in the same commit, which a close
cannot step past.

So the clause is now a hard gate. A session whose commits carry a user-facing
change cannot close until the FAQ is dispositioned, and the disposition is written
into the LOG entry as its own line — `FAQ: updated <entry>` or `FAQ: not needed
because <reason>`. The required artifact is what makes it bite. Skipping is still
allowed, because plenty of user-facing changes genuinely need no entry; what is no
longer allowed is skipping invisibly. A skip becomes a statement someone can later
disagree with.

A pure hook was rejected and the reason is recorded in the file: "is this change
user-facing?" is not mechanically detectable the way QUEUE structure is, so a hook
would either miss cases or fire falsely. The gate rides a read that already
happens, which is why it costs nothing extra to run.

The rule stays host-only by residence rather than by detection. It lives in this
project's CLAUDE.md, which consumer projects don't carry, so it never fires for
consumers — who don't maintain the method's FAQ. Keeping the method's own FAQ
current is the developer's job, so it does not belong in the shipped done-plan.md
or done-build.md.

Evidence gathered this session, which is the concrete case for the gate: the FAQ
has been touched by 3 commits out of 386 — created 2026-06-16, updated
2026-06-18, then a single 9-line entry on 2026-08-02. Six weeks with nothing at
all, across a stack of shipped user-facing changes. That is what a soft confirm
produced.

**Files touched:** CLAUDE.md (the FAQ-sync clause in Working conventions).
**Routed to Captures:** [gitignore-scaffolded-faq], [faq-as-claude-readable-reference].
**FAQ:** updated — three entries written this session (see the sibling entries for
this run).
