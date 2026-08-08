# c4cf5af — The cycle-status greenlight ask becomes a real close step, with a logged disposition as its teeth

The user reported trying to greenlight a merge across several sessions and it never happening. The investigation found why, and the finding is the uncomfortable kind: every individual session behaved correctly. Seven queue items said "greenlight it at any /plan close" and `done-plan.md`'s close carried no such step — in either docset. The only place a greenlight could be raised was plan.md Step 1's opening question, which is the wrong shape at the wrong end of the session: a greenlight is a judgment about whether things have gone well enough, not an external event that has or hasn't happened, and the opening is where a session holds the least evidence to make it with.

Only the user's report could have surfaced this. Nothing internal was ever going to notice a step that was referred to but never written, because every reference read as a pointer to something real.

**The fix is host-only, and that was the user's call.** The draft included a greenlight step in the shipped /plan close; the user ruled it out on the grounds that self-hosting rules belong in CLAUDE.md. The check agreed with the ruling — the merge cycle, the soak-end audit and the greenlight all live in CLAUDE.md's branch-cycle section, and the shipped docs never promised a greenlight step. Verified by grep before building: "greenlight" appears in each docset only as a passing noun (plan.md's "seeding never greenlights a build", plugin-behaviour.md's "awaiting greenlight" in the state table), both describing a state rather than promising a step, both left alone.

**The teeth are the point, and they are modelled on the one rule in this file that has grown them.** A plain convention was rejected explicitly as the retired push marker's shape — stated in one place, performed in none. The branch-cycle section already admits nothing enforces its own audit gate, so adding a second unenforced convention beside it would have been the same mistake twice. Instead the close carries a required `Cycle:` line in the session's LOG entry, so a close that skipped the ask is visibly missing something rather than silently clean. That is the FAQ-sync gate's shape, which is this project's one demonstrated case of a soft rule acquiring enforcement after failing softly.

**One item needed no rewording and one was deliberately left alone.** [retire-docset-a] was named in the capture as one of six, but its greenlight had already happened, so the stale pointer was gone before the build reached it. [merge-blitz-2026-08-06-to-main] is complete rather than waiting, and closes at this session's /done instead.

**Files touched:** `CLAUDE.md` (new "The cycle-status ask at every /plan close — with a logged disposition, host-only" section, placed after the soak-end sequence), `QUEUE.md` (five items repointed: [release-docset-b-work], [docset-b-register-decision-weaker-than-recorded], [setup-as-migration-home], [rename-to-throughliner], [concurrent-session-support]).

**FAQ:** not needed because nothing shipped — the rule lives in this project's CLAUDE.md, which consumer projects don't carry, and consumers have no branch cycle to report on.

**Routed to Captures:** none from this item.
