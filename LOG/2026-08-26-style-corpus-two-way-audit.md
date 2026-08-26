# 3b094b5 — Style audit: three findings captured, and both research levers turn out to be already applied

An audit of the shipped brevity output style against the rule corpus, in both directions — rules duplicating the style flagged for eviction, pure tone-steering rules flagged as promotion candidates — plus a disposition on the two research levers the item recorded as never applied anywhere.

**Three findings, all captured.** The dedup-down policy is unsafe while the style is opt-in: six of the style's nine bullets restate always-loaded communication rules in substance, and SPEC says a style-level rule is stated there and nowhere below — but the style is enabled per project with the user's consent, so evicting those six would leave any project that declined it with no communication rules at all. Narration cadence is the mirror of that: it exists only in the style, so a project without it gets no cadence steering, which the research names as the largest identified gap. And the style is about a third prohibitions — four of nine bullets — against both the research's positive-instruction lever and the method's own rule that a prohibition means the action was never specified.

**Both levers are already applied, which the item did not expect.** The tail concision reminder is injected by `session_start.py`, and the written-deliverable length instruction is covered by the Authoring standard's deliverable arm. Recorded as clean passes rather than findings. The markdown-suppression lever remains correctly unapplied, on the user's own "the formatting helps" — the one documented lever in that research that is wrong for this reader.

**Clean pass on the skill docs.** Every tone-shaped statement found under `docs/` is a site-specific narration instruction, correctly placed; none is a free-floating tone rule that belongs at style level.

The first finding is the one worth carrying forward: it is not a wording defect but a policy that would do damage if followed literally, and it needs a decision rather than an edit.

**Files touched:** none — an audit edits nothing.
**Routed to Captures:** [style-dedup-unsafe-while-opt-in], [narration-cadence-promotion-candidate], [style-negatives-to-rewrite-positive].
**Depth:** short.
**Tick:** all three captured, none dropped.
Rule gate: not needed — an audit edits no rule text; each finding becomes a capture, and any rule change it proposes gets its own gate when that capture is processed.
