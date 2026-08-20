# b485ee3 — A hook change is verified by driving the new code, never by performing the guarded action live

Filed by Claude at its own close, from a data-destroying mistake made minutes earlier and recovered from git. The full account is in `LOG/2026-08-17-chat-2.md` and is cited rather than restated.

In one line: having just built the guard that refuses a Write onto an existing file under `LOG/`, the run deliberately performed that write to watch the guard refuse it — and overwrote a committed entry, recovered whole with `git checkout HEAD --`.

**The one distinction the fix turns on.** Every existing statement of host-versus-target asks whether a change is *live*. This is a session choosing to **exercise** the change to confirm it, which turns passive staleness into an active write against the old, unguarded behaviour.

The parent was already in place: `CLAUDE.md` requires a close whose staged paths include `plugin/throughliner/hooks/` to run the suites under `resources/testing/`, as plain scripts. That rule already says how a hook change is verified, so this is a clause on it rather than anything new — verify by driving the new code directly, via the suites or `py` against the target file, which that run did successfully three times before making the mistake.

**The unsafe form is named as its consequence rather than as a prohibition:** performing the guarded action in the live project exercises the **installed host**, which is the old code, so the guard never fires and the action completes for real.

**A hook was considered and refused.** A write made to watch a guard refuse it is byte-for-byte a write meant to succeed, so nothing mechanical can separate them — which is also why the safe test and the destructive one look identical from the inside. Failure evidence is one instance, and it is carried by its cost rather than its weight: a committed session record destroyed, and the destroyed entry's own text had predicted exactly this, was read during that run, and the mistake followed anyway.

**Files touched:** `CLAUDE.md` — the hook-suite close gate. Nothing shipped: consumers never author hooks.

**Routed to Captures:** none.

Rule gate: run — a clause on the existing hook-suite rule, subordinate rather than freestanding, though it does cost a slot in this project's always-loaded file. Nothing evicted. **A hook was considered and refused:** a write made to watch a guard refuse it is byte-for-byte a write meant to succeed, so nothing mechanical can separate them. Failure evidence is one instance, carried by its cost: a committed session record destroyed, and the destroyed entry's own text had predicted it, was read during that run, and the mistake followed anyway.

Tick: done, confirmed by reading the amended gate back in place.
