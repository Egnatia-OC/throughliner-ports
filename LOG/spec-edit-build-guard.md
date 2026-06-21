# 29ba751 - plan.md + post_tool_use.py + FAQ: stop a spec-edit being folded into a feature build (authoring rule + lint backstop)

During /plan a Spec-edit section was folded into a feature-build batch with SPEC.md listed in Files; nothing mechanical caught it (the scope-lock permits the edit once SPEC.md is listed, and the lint allowed both subheadings). The fix is belt-and-suspenders: plan.md adds an authoring rule that a single batch never carries both a Build and a Spec-edit subheading (the load-bearing guard, since the scope-lock cannot catch this), and post_tool_use.py adds an advisory lint flag (check 8) as the mechanical backstop. A FAQ entry explains why a spec change cannot ride inside a build. An in-session fixture test confirmed both-subheadings flagged, Build-only and Spec-edit-only clean.

**Files touched:**
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/hooks/post_tool_use.py
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
