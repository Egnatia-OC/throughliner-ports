# [HASH] — Fifteen rules stated twice or three times in the always-loaded file reduced to one statement each

Audit findings B1–B15, consolidated into one item at Alex's instruction on
2026-08-13 because the fix is identical for each and fifteen builds would have
meant fifteen passes over one file.

**Why a restatement is as bad as an accidental duplicate**, which is the audit's
own note and the reason this mattered: when the canonical text changes, nothing
forces the copy to follow. Every one of the fifteen was a copy rather than a
pointer.

**Deleted, never stubbed.** A pointer paragraph in place of each copy would have
kept most of the words while looking like a fix, and words are this file's problem.
Where the audit noted that a losing copy carried a reason the survivor lacked,
that reason was folded into the survivor rather than both being kept — B5's
one-reorder-away-from-losing-it and B7's grep-ability.

**Three canonical choices differed from the audit's guess, and one finding needed
no edit at all.** B13 was already a pointer: the paste-target bullet names the
rendering section rather than restating it, so there was nothing to merge —
checked rather than assumed either way. B2's canonical home is the `[SEQUENCE]`
tag definition, which now carries the count-upfront and working-file clauses the
Communication bullet had been holding. B1's is the research section, which gains
the user's-choice half that the deleted Communication bullet carried.

**B4's dedicated "Below the line" section was deleted whole** rather than trimmed.
Its remaining content is stated in the work-item states table, the capture line
format and the over-tag guard; the one /plan-specific line it added had already
moved out under the sibling relocation item.

**One incidental correction, made because the dedupe created it.** The
`[SEQUENCE]` definition now says to write the full set to the session's working
file "where the session has a working file" — the unconditional form became wrong
later in the same run, when the planning working file was deleted from the method.

**Rule gate: run** — pure subtraction, nothing admitted. Measured: 240 to 236 rule
statements, with a larger prose reduction inside the statements that survived,
since much of what went was sentences within rules rather than whole rules.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none. The fifteen original captures were consumed by the
consolidated item and their per-finding detail remains in
`resources/research/skill-nonspecific-rules-conflicts-audit.md`, section B.
