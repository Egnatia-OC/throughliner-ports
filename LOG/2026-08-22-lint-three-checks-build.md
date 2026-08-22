# c904687 — post_tool_use.py queue lint — three new advisory checks: duplicate gate lines, cleared rule-path item with no gate disposition, cleared item naming QUEUE.md

Three sibling escalations to the hook, each refused as method text and settled at processing; this entry carries the shared reasoning and the design detail, and the three items' grounds are below. All three checks are judgment-free reads of item blocks, flagged by slug, and the lint stays advisory — it reports, never blocks. One implementation decision made here: the two path-scoped checks read only an item's `Files:`/`Changes:` lines, not the whole block, because a path mentioned in rationale prose is not a claim the build touches it and whole-block matching would flag every item that merely discusses the queue or a doc.

- **Duplicate `Rule gate:` lines** ([duplicate-gate-line-on-a-processed-item]): a processed item carried the line twice, the second a truncated draft — two dispositions on one item make the record ambiguous, and revision passes that append rather than replace will produce it again. Kept as a lint check on the user's stated preference for mechanisation; a method-text rule was refused at one occurrence, below the gate's bar.
- **Cleared rule-path item with no gate disposition** ([keep-step-skipped-gate-disposition]): the autonomous keep-step kept two rule-amending items with no `Rule gate:` line and the next build halted on it. Sharper keep-step wording refused (tenth-instance class); a plan-close check refused as too late, since /next can run the same day. The lint fires at the write, before a run exists, on the gate's own trigger-path set; consumer items never name those paths, so it structurally never fires for them.
- **Cleared item naming QUEUE.md** ([queue-content-items-are-unbuildable-by-a-run]): an item whose described work is queue content passes both buildability limbs and is still unbuildable, because the scope-lock refuses a build the queue by design. Flagged whatever the flavor — widened at processing to absorb [audit-cannot-read-queue-prose], since an audit pointed at queue prose can't reach it from a run either. A sixth keep-step clause refused on the accretion ground. The stated residual: the check reads Files lines only, so an audit scoped at queue prose solely in its rationale escapes.

Tick (all three): done, confirmed — the extended suite passes as a plain script via `py` (39 cases), including the below-the-line and other-files non-firing halves.

Rule gate: run — escalations to a hook rather than rules; no method text changes and no slot is spent; the lint's advisory posture is unchanged. (One line covering all three items; each item's block carried this disposition.)
FAQ: not needed because the lint is advisory context Claude reads; no user action changes.

**Files touched:** plugin/throughliner/hooks/post_tool_use.py, resources/testing/test_queue_lint_flags.py
**Routed to Captures:** none
