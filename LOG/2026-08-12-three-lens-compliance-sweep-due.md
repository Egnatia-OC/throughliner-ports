# [HASH] — The three-lens compliance sweep: 330 against a ceiling of 200 in this project, and ten findings filed

The first run of the sweep since the AUDITED signal was given a trigger. All eleven docs in scope read; no files edited, per the audit contract.

## The count, split by audience as the checklist requires

| | always-loaded statements | vs ceiling 200 |
|---|---|---|
| a consumer project | 234 (`skill-nonspecific-rules.md`) | 17% over |
| **this dev project** | **330** (+ `CLAUDE.md` at 96) | **65% over** |

**That split is itself the sweep's largest finding.** `rule_signals.py`'s `ALWAYS_LOADED` names one file, so MEASURED has been reporting the *consumer* number as "the always-loaded rule-statement count". Every reading of the board so far has understated this project's position by 96 statements — including the scoping of the eviction work queued off it.

Per-doc statement counts recorded for the eviction pass to work from: `skill-nonspecific-rules` 234, `plan` 226, `done` 181, `setup` 126, `next` 124, `next-build` 86, `done-plan` 52, `done-build` 24, `done-audit` 12, `next-audit` 6.

## The ten findings, all approved as-is at bulk approval

Lens 1 — self-authoring compliance: the audience split above; `plan.md` at 226 statements with no measure watching fetched docs at all; the write-first block's ~200 words of authoring rationale in always-loaded text; `next.md`'s red-flag backstop stating its full justification inline; device-and-hardware-access failing the file's own four-skills admission test; and the paging rule now living in two places since the digest clause arrived.

Lens 2 — tag placement: `plan.md`'s skip-to-defer recommendation carrying `[DISCUSS]` with no `[PROMPT]`, so nothing makes it wait; and a conditional written inside the tag brackets rather than as a tag.

Lens 3 — narration drift: Step 1 now firing seven scans at one opening with nothing bounding additions; and the context-adjacency offer as a flat three-option menu.

**Two findings are about work built earlier in this same run** — the seven-scan opening (the LOG-index read took it from six to seven) and the flat menu (built from its item's own specified wording). Both were filed rather than exempted; flagging Claude's own output from the same session is the honest reading of the contract.

## Ordering, recorded because it was got wrong twice before

This audit runs **before** [rule-corpus-over-ceiling], and the path is the ordinary one: the audit files findings, a later /plan processes them into work items, and the eviction builds from them. Claude twice treated the intervening /plan as an obstacle rather than the cycle — the second time reversing a correct recommendation on that basis. The work-cycle block shipped earlier in this run exists because of that, and this ordering is the first thing it protects.

**Files touched:** none — an audit reads. The target artifacts read were the eleven procedure docs in scope plus `CLAUDE.md`.

**Routed to Captures:** [board-reports-one-audience-not-two], [fetched-docs-have-no-measure], [step-1-scan-count-unbounded], [write-first-rationale-belongs-in-log], [backstop-rationale-inline], [device-access-rule-could-be-fetched], [paging-rule-has-two-homes], [skip-to-defer-missing-prompt-tag], [conditional-written-as-a-tag], [context-adjacency-offer-is-a-flat-menu].

**Approval outcomes:** all ten approved as-is; none contested, none dropped.

Rule gate: not needed — an audit authors no rules and edits no files. Its output is the ten captures above, which a later /plan will process into work.
FAQ: not needed because nothing shipped and nothing user-facing changed.
