# [HASH] — Retired the freeform session type — mode and flavor — across SPEC and the method docs

Removed freeform entirely. Its three claimed uses didn't hold: discussion-first sessions are /plan's (and freeform's talk-it-through licence had actively pulled /next into a plan/next boundary breach); ad-hoc audits are the first-class `[audit]` flavor; handmade wrap-up moved to /done via [git-panic-on-handmade-edits], which shipped first so the home existed before freeform's was removed. Deleted next-freeform.md and done-freeform.md; stripped the `[freeform]` flavor from the tag set, all routing lists, the on-demand `/next freeform` form, the FAQ, and the scaffolded QUEUE template; post_tool_use.py had no freeform handling to remove. Also carried Half C of [two-section-model-reconciliation]: rewrote SPEC's /next line to name build + `[audit]` first-class (freeform gone) and sharpen review-don't-edit. Converted the `[freeform]` tag on [two-section-model-reconciliation] to a plain build. Scope grew mid-build by four files beyond the line's list (next-build.md, cruise.md, CLAUDE-TEMPLATE.md, setup.md) with approval, to clean every reference. Keeping freeform was weighed and rejected — it added ceremony to the one thing that should be zero-ceremony.

**Files touched:**
- deleted plugin/si-plugin/docs/next-freeform.md + done-freeform.md
- plugin/si-plugin/docs/plugin-behaviour.md, next.md, done.md, plan.md, next-build.md, cruise.md, setup.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md, faq-template.md, faq-index-template.md
- SPEC.md, QUEUE.md

**Routed to Captures:** none
