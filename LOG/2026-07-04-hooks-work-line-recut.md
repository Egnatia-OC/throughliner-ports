# ad295f8 — All three hooks recut to the two-section work-line model — post_tool_use.py lint drops removed-structure checks (parked headers, Captures divider, ALLOWED_SUBHEADINGS, dependency refs) and keeps slug/provenance/section-heading checks plus a new red-flag-state check; session_start.py drops the deferred-tests nudge and adds open-red-flag surfacing at session start; pre_tool_use.py adds resources/research/ to the scope-lock always-allowed set.

The three hooks still spoke the old queue structure (a pinned Red flags section, Deferred tests, Batches with Build/Test/Audit subheadings, a Captures divider, parked-item and dependency headers), while the behaviour defs and /plan had already moved to the two-section work-line model and [red-flags-restore-defs] had defined the red-flag work-line format. This batch brings the hooks into line so the redesigned plugin can be dogfooded and [fresh-queue-clean-break] can run.

post_tool_use.py: the QUEUE.md lint was rewritten. Every check tied to removed structure was dropped along with its helpers — batch-slug, parked-header, Captures-divider, dangling-ref, subheading/ALLOWED_SUBHEADINGS, prose dependency-vs-citation, and dependency-ordering. Four checks remain on the two-section model: each work line's `####` heading ends in a `[slug]`; each work-line block carries a provenance label ("captured by you" / "by Claude"); both `## Processed` and `## Unprocessed` headings are present; and a `Red flag · State:` marker names a valid state (open / resolved / accepted). The lint stays advisory and deny-list.

session_start.py: removed `_host_side_deferred_tests_present()` and the deferred-tests-gated confirm nudge (the version-change report is now a plain line), and added `_open_red_flags()`, which scans QUEUE.md for `####` work lines carrying `Red flag · State: open` and surfaces them first-thing after the behaviour rules. With no pinned Red flags section in the new model, this scan is what keeps an unaddressed risk unmissable.

pre_tool_use.py: added `_is_research_dir()` (mirroring the method-doc and memory exemptions) so every session type can file a research note under `resources/research/` without tripping the scope-lock.

Learned during the build and routed to Captures: the hooks now encode one literal work-line shape (a `####` heading ending in `[slug]`, provenance beneath), but that shape isn't stated in one place in the recut docs — it was inferred from the current captures and plan.md's existing pattern. If a later redesign batch renders work lines differently, all three hooks silently mis-detect. Captured as [pin-work-line-format]. Also noted, not captured: until [fresh-queue-clean-break] rewrites this project's own QUEUE.md, the recut lint will advisorily flag the still-old queue on every edit — an expected, advisory-only consequence of the chosen batch order.

Sixteen in-session module-import checks passed across all three hooks; the live host-side confirmations wait on rezip + reinstall and are recorded as a deferred test.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py: lint rewritten to the two-section model (four checks kept/added, old checks and helpers deleted)
- plugin/si-plugin/hooks/session_start.py: removed deferred-tests helper + nudge; added open-red-flag surfacing
- plugin/si-plugin/hooks/pre_tool_use.py: added resources/research/ to the scope-lock always-allowed set

**Routed to Captures:** [pin-work-line-format]
