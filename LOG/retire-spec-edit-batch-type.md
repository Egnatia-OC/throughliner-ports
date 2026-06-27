# 3a12926 — [retire-spec-edit-batch-type] SPEC becomes a normal file; spec-edit batch type removed, two close-out spec-sync gates replace it

Built in the goal run (second of four). The spec-edit batch type had become a time sink — often a whole /next cycle to change one SPEC line. This retires it entirely: SPEC.md is now a normal doc any batch can list in its Files. Three paths replace the batch — a SPEC change decided in /plan is edited in that /plan session; a build that discovers it needs a SPEC change asks the user, adds SPEC.md to scope, and edits it inline; a large SPEC rework is a normal build batch that lists SPEC.md.

The load-bearing piece is drift prevention, because last time SPEC was editable in /plan it got left behind. Two spec-sync checks at the commit boundaries carry it, both authored rationale-first (they're behavioural — "did this make a SPEC sentence wrong?" is a semantic judgment no hook can make and no lint can backstop, so the rationale is the only enforcement). New gate at the /plan close (done-plan.md): if a planning decision changed what SPEC says and SPEC wasn't updated, the close stops and SPEC is updated with approval before committing — placed before the LOG entry so the edit lands in the same commit, and explicitly *not* bounced to /plan (editing SPEC to match a decision the user already made is recording, not re-planning). The existing /done-build spec-drift check is hardened from detect-and-file-a-capture to a stop-the-close gate: on real drift it stops, gets approval, adds SPEC.md to the build's Files, edits SPEC to match, and commits together — deferring to a capture would close a commit with SPEC already behind, breaking SDD same-commit atomicity. This aligns with spec-driven development better than the batch did (research: spec-driven-development-edit-workflow.md): SDD wants the spec to move in the same commit as the behaviour change, which is exactly what commit-boundary gates enforce; SDD never required a spec change to be its own gated step.

The Spec-edit subheading, its routing, the Build+Spec guard ([spec-edit-build-guard]), and the lint that backed it all go. The spec-sync gate at this run's own close passed silently with no drift: SPEC.md line 28 already named the subagent ask-gate accurately, and SPEC never described the spec-edit batch type, so nothing this run built made a SPEC sentence wrong.

Run-now test passed: post_tool_use.py no longer flags a Build+Spec mix (check 8 and its function are gone) and "Spec-edit" is no longer in ALLOWED_SUBHEADINGS; a clean queue still lints empty. The live /plan-and-build behaviour is a deferred test ([retire-spec-edit-batch-type], host-side, observed after reinstall).

**Files touched:**
- plugin/si-plugin/docs/plan.md — ground-rules pipeline rewritten to the three-path model; Step 3 Spec-edit subheading + "Spec-edit batches" + "never both" guard removed, replaced with "SPEC changes are normal build scope"; Step 4 spec-sync obligation noted
- plugin/si-plugin/docs/done-plan.md — new /plan-close spec-sync gate (before the LOG entry)
- plugin/si-plugin/docs/done-build.md — Phase 1.4 hardened from detect-and-file to a stop-the-close spec-sync gate; header line de-spec-edited
- plugin/si-plugin/docs/next-build.md — Scope management: build-discovered SPEC change named as a legitimate scope-grow
- plugin/si-plugin/docs/next.md — Spec-edit routing line removed
- plugin/si-plugin/docs/done.md — router Spec-edit mention removed
- plugin/si-plugin/hooks/post_tool_use.py — `_check_spec_edit_build_mix` (check 8) + its call removed; "Spec-edit" dropped from ALLOWED_SUBHEADINGS; docstring + SUBHEADING comment + check-5 message updated
- plugin/si-plugin/hooks/pre_tool_use.py — docstring SPEC handling de-spec-edited (the spec-edit-batch comment was rewritten during batch 1's docstring edit; scope-lock SPEC handling unchanged)
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md — consumer SPEC model updated to the new behaviour
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — two spec-edit FAQ entries collapsed into one ("Can I change SPEC.md, and how?")
- CLAUDE.md (project) — Rules entry rewritten; Spec-edit removed from the "four places" enumeration

**Routed to Captures:** none
