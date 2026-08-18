# [HASH] — a hook change is verified by driving the new code, never by performing the guarded action in the live project

Having just built the guard that refuses a Write onto an existing file under `LOG/`, a run deliberately performed that write to watch the guard refuse it — and overwrote a committed entry, recovered whole from git. The hook that actually runs is the installed host, a frozen snapshot, so the guard never fired.

**The distinction the fix turns on is why knowing the host-versus-target rule was not enough.** Every existing statement of it asks whether a change is *live*. This is a session choosing to **exercise** the change to confirm it, which turns passive staleness into an active write against the old, unguarded behaviour. The urge to verify is the method's own instruction, and here it points the wrong way.

The parent already exists: `CLAUDE.md` requires a close whose staged paths include the hooks folder to run the suites as plain scripts. That rule already says how a hook change is verified, so this is a clause on it — verify by driving the new code directly, which that run did successfully three times. The unsafe form is named as its consequence rather than as a prohibition.

A hook was considered and refused at the gate: a write made to watch a guard refuse it is byte-for-byte a write meant to succeed, which is also why the safe test and the destructive one look identical from the inside.

The item breached its ceiling at 558 words and was trimmed to 407 by relocating the narrative to the record and citing it — knowingly short of 345, since splitting would have made two items for one clause.

**Queue changes:** [live-testing-a-hook-change-hits-the-old-host] settled, trimmed and cleared.
**Work processed:** kept — [live-testing-a-hook-change-hits-the-old-host].
