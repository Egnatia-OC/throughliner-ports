# [HASH] — CONTRADICTED, a sixth board signal: a commit whose rule count rose while its LOG entry says the gate wasn't needed

The user's question at /plan was what checks the dispositions against what was queued. The answer was **nothing**. BORN is a presence check: a session that added four rules and wrote `Rule gate: not needed — typo fix` satisfies it completely, and nothing anywhere contradicted that.

**The failure family the method already knows.** A claim Claude makes about its own work with nothing verifying it is exactly what the Stop hook was built for. The disposition obligation was itself adopted on the reasoning that a required artifact turns a silent omission into a visible one — and that reasoning holds against *omission* while doing nothing against a **false** artifact. Nobody had separated the two.

## The check

For each commit in the signal's window touching the rule files, the always-loaded rule-statement count is computed at that commit and at its parent, via `git show <rev>:<path>` through the existing counter.

```
count ROSE  +  "Rule gate: not needed"   ->  FLAG
count ROSE  +  "Rule gate: run — ..."    ->  fine
count FELL or unchanged                  ->  fine, always
```

**One-directional by design:** an eviction pass lowers the count and owes no disposition defence, so a fall is never a finding. Only the rise-with-"not needed" pair is a contradiction — and it is the case that actually happens, the gate skipped and the line written anyway.

**It runs as a board signal, NOT as a check at the close, and that placement is the item's whole point.** A check at the close would be the session judging its own disposition in the same breath as writing it — the self-report problem this exists to close, wearing a different hat. The board runs at the *next* session's start, over a commit already written and no longer editable to suit the check. Later and cheaper is exactly right here; earlier would be worthless.

**What it cannot do, said where the signal is described and in `CLAUDE.md`:** it cannot tell whether a gate recorded as *run* ran honestly. A dishonest "run — considered and kept" defeats it completely. It catches omission-dressed-as-disposition, not bad judgment. A check that over-claims is worse than none, because it makes the corpus look guarded when it is only partly guarded.

**The proxy caveat rides with it** — the count is a structural proxy, so the signal reports a *contradiction between two artifacts* rather than a measured fact about rules. Still worth having: the two are supposed to agree, and their disagreeing is checkable with no judgment.

**Implementation note.** `count_text_statements()` was split out of `count_statements()` so one counter serves both the on-disk read and the git-blob read — a second implementation is what would drift. Bounded by the same `DISPOSITION_BASELINE` as BORN; without it this would run over pre-obligation commits and flag every one.

**A real bug caught by running the board:** its header printed a hardcoded "of 5" while six signals were listed. Now `len(signals)`.

**Files touched:** `resources/rule_signals.py`, `CLAUDE.md`.

**Routed to Captures:** none.

Rule gate: run — one amendment to `CLAUDE.md`'s disposition block, admitted. It states what the two signals check and, more importantly, what neither can check. Admitted because a check that over-claims is worse than none: without this paragraph the pair reads as full coverage of the obligation, when a dishonest "run" defeats both. The rule the paragraph attaches to is unchanged; this describes its enforcement honestly rather than adding an obligation. Raises this project's always-loaded count, and the disposition says `run`, so the new CONTRADICTED signal is satisfied by its own commit.
FAQ: not needed because the board is host-only and not in the plugin package.
