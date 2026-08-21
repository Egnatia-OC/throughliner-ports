# cc33c1e — A repeal now greps the send record too, and files a correction post where it finds a claim it has falsified

**Why this was worth doing.** Split from `[repeal-has-no-ripple-trace]` at processing on
2026-08-17, kept apart rather than merely trimmed because the two differ in readiness
rather than only in length: the live-doc trace was buildable then and this was not.

**The instance is the user's own spec-driven-development post**, which described a build
that "asks first, adds SPEC.md to its own file list, and edits it in the same commit".
`[missed-spec-write-interrupts-the-run]` inverted that — a build now hands the sentence
back rather than writing it — so a claim that was true when posted became wrong through
ordinary work, inside the same conversation that made it.

**The trace is identical to its sibling's.** Grep the distinctive words of the repealed
sentence. What differs is only where you grep: a repeal already greps live documents,
and this extends the same pass to the record of what was published.

**Why it could not be built before now.** There was nothing to grep. Posts were not
written down anywhere. `[send-record-lacks-destination-and-intent]` shipped 2026-08-20
and `INBOX/sent.md` now exists carrying a line per outbound artifact, which is the one
thing this item was missing.

**What was built.** The keep-step's repeal limb gains a second grep target: where an item
repeals shipped behaviour, run the same grep over `INBOX/sent.md`. A match files a
correction post as its own `[user]` line, naming what was announced and what is no longer
true; no match, nothing further. One sentence states why the line is filed rather than
assumed — the announcement went out under the user's own account, so only she can correct
it.

The host-only half is stated in `CLAUDE.md`'s Discord section, which is where a
correction post's obligation belongs. It names the trigger as the repeal limb's existing
grep, so there is no new detection point.

**The coverage limit ships with it and must not be softened.** `INBOX/sent.md` records
what a post *claimed* rather than merely that one happened, and that is what makes a
repeal checkable at all. But nothing recorded earlier posts, so this reaches only posts
made from now on. Earlier cases are unfindable — which is itself the argument for the
record rather than for this rule, and is why the failure evidence is one instance and no
more is claimed.

**Files touched:** `plugin/throughliner/docs/plan.md`, `CLAUDE.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because this changes what happens at planning and the user's action —
posting what Claude drafts — is unchanged.

Rule gate: run — one more site on the repeal limb its sibling item ships, so it is subordinate to a rule that will already exist by the time this builds, and spends no slot. Nothing evicted. Failure evidence is one instance, and it is the only one available: nothing records what was posted, so earlier cases cannot be found at all — which is itself the argument for the record rather than for this rule.

Depth: short. Built and confirmed by grep: the repeal limb names `INBOX/sent.md` and
states the `[user]` correction line, and the Discord section carries the obligation.

**One thing a later session should know.** This run added a second line to
`INBOX/sent.md` — the Discord post walked through at its end — so the mechanism now has
two claims on record to check future repeals against, rather than one.
