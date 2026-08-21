# cc33c1e — The scope-lock's file boundary is stated plainly, and `[freeform]` is pinned as a flavour rather than a mode

Build entry. The planning entry that processed this item is
`2026-08-21-scope-lock-guards-files-not-work.md`.

**Why this was worth doing.** Filed from INBOX mail sent by a consumer project running
1.20.0-test12. Their user raised it; that project's Claude wrote the diagnosis, and she
asked for both halves to be sent. Identifying details from the message — the
correspondent's folder path and the people it names — are deliberately not carried here.

**What happened there.** In one /plan session, that chat drafted a substantive letter to
an external professional and the user sent it — the most consequential act of the session
by a wide margin — and nothing gated it, because an email is not a file in the project.
In the same session the scope-lock twice refused a four-line correction to that project's
own `CLAUDE.md`, which the user had already read and approved. The guard fired on the
trivial thing and was silent on the serious one.

**Their user's framing, which is the part worth carrying.** Throughliner governs work
wherever it is conducted, not only work touching this machine. Her example: a `[user]`
item in another project that involves unpicking a physical dress — nowhere near a
filesystem, still work, still governed, still running under /next. The principle exists
in the method; the enforcement stops at the file boundary.

**Two parts of the item's own account were overturned at processing, and both are kept
standing here because the reasoning that fell is what stops the same conclusions being
reached again.** First, "nothing gated it" does not survive the detail: their user read
the letter and sent it herself, so the never-send-unseen rule was satisfied — Claude
drafted, she approved by sending. What was missing was a record, not consent. Second, the
record half shipped the day after the item was filed:
`[send-record-lacks-destination-and-intent]` landed 2026-08-20 and a letter to an
external professional is squarely inside its wording, so any project on the current
version now leaves a trace of exactly the act this item said left none.

**And the reason no hook can reach it is sharper than the one first recorded**, which
matters because it rules out a whole class of fix rather than one option. It is not that
a hook cannot see an email. It is that **the send was never Claude's action**: no tool
call carried it, so there is nothing to intercept by construction. A guard cannot fire on
an act performed by the human, outside the session, through a surface the session never
touches.

**What was built — the honest-limit statement.** The Scope section now says the
scope-lock covers files, so a message that leaves the machine, a post, a decision reached
in conversation and a step handed to the user are governed by the approval rules and by
nothing mechanical. It is stated as what the mechanism does rather than as an apology for
what it does not. Nothing anywhere said this, and that silence is what let a file-lock
read as general coverage: their user's framing is true of the *method* and false of the
*mechanism*.

**What was built — the vocabulary clause, kept deliberately small.** That session's
Claude had reached for `[freeform]` as though it were a mode a /plan session could slip
into. The flavour-marker block now says a flavour names how a work item is executed,
`[freeform]` is one like the rest and never a mode, and hand-work in a chat with no queue
item behind it has no name and needs none. **Naming the unqueued-hand-work case was
refused**: the always-loaded rules warn that invented states, tags and session containers
are a recurring failure here and that the user has caught each one.

A grep of the diff for a new state, tag, mode or session type returns exactly one hit —
the clause *denying* a mode. Nothing was invented.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.

**Routed to Captures:** none from this item.

FAQ: not needed because nothing a user does changes.

Rule gate: run — admitted as two clauses on existing always-loaded statements, the Scope section and the flavour-marker block, subordinate rather than freestanding. **They sit in the always-loaded file and each spends a slot**, stated plainly rather than waved past: the first must fire wherever a session reasons about what the lock protects, and the second wherever a flavour is reached for, so neither can be fetched. **Nothing is evicted.** Failure evidence is one consumer instance for each half, both in a single reported session. **A hook was considered and refused**, on the record in the block above.

Depth: short. Built and confirmed.

**A count limitation, recorded rather than papered over.** The item's acceptance asks for
the rule-statement count to be accounted for, "since this adds two".
`skill-nonspecific-rules.md` measured 312 after the law-prose pass and 318 at the end of
the run — but four items in this run edited that file, so the +6 is their combined effect
and cannot be attributed to this item's two clauses alone. The process lesson: a per-item
count has to be taken immediately before and after that item, and this run did not do
that consistently for the always-loaded file.
