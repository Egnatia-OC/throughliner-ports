# v92 — 2026-05-26 — Planning: OQ promotion and BACKLOG cleanup

**What shipped.** Full OQ review session. Five new queued batches (0097–0101) promoted from resolved open questions. Seven OQs removed (promoted or resolved). Two OQs removed outright (covered by existing mechanisms). Session-protocol.md routing clarified. CLAUDE.md updated with dev-side convergence strategy.

**Decisions taken and why.**
- `/sovclose` (0097): dual-path skill replacing after-build.md. `/sovgit` split out for git handholding, with team vs. solo workflow detection.
- `/sovplan` (0098): wraps planning.md, adds ordering principles and `[SECURITY]` marker (universal inline marker for sensitive entries across UX and BACKLOG).
- `/sovrecap` (0099): rename from before-build, lock timing fix (Status: active delayed to post-confirmation).
- Bash write-guard (0100): close the Bash bypass hole in PreToolUse, add skill escape guidance to all write-lock denies.
- Structured-markdown validator (0101): extend PostToolUse validation beyond BACKLOG to TEST-LOG, build-log, scope-context, proxies.
- Timestamps in build-log resolved as "keep" — useful for timeline reasoning, proxies already surface dates.
- Settings layer OQ resolved — git workflow concern folded into `/sovgit` (0097), CLAUDE.md sections sufficient for everything else.
- "Separate planning/build content in batches" resolved as "no" — existing OQ→planning batch→build batch lifecycle already provides the separation.
- Prose-only rewrite and graduate-SI-onto-SI removed — both covered by the dev-side convergence strategy (prose mirroring, eventual dogfooding).

**Pivots and surprises.** `[SECURITY]` marker expanded from UX-only to universal (UX entries, BACKLOG build batches, planning batches, open questions) based on Alex's insight that the marker serves prioritization across all decision surfaces, not just spec review.

**Carried forward.** Three OQs remain parked: bulk-tersify skill, lost-feature sweep, plugin testing framework.
