# 53e3a8e — Swept method docs to make "work item" the canonical unit name

Settled "work item" (or "item" in context) as the canonical name for a unit of work — a `####` heading plus its rationale block — replacing "work line". Three supporting rules drove the sweep: "build" is a flavor only (an untagged item is *a build*, never a synonym for the unit); "batch" is retired (excised wherever it lingered from the pre-two-section model, rephrased to "work item" / "model" / "step" as fit); and "line" is reserved for literal file lines — the cleared-to-run marker, push markers, heading/description/index lines, "one path per line", "45 lines" — all left untouched. The care the item flagged was real: "work line" and bare unit-"line" are pervasive, so each occurrence was judged unit-reference vs literal-line one at a time.

Files swept: plugin-behaviour.md, plan.md, next.md, next-build.md, next-audit.md, done.md, done-build.md, done-plan.md, done-audit.md, setup.md, skills/next/SKILL.md, templates/CLAUDE-TEMPLATE.md, templates/faq-template.md, templates/faq-index-template.md (including a renamed FAQ heading and its index anchor), SPEC.md, and QUEUE.md's header.

The three hooks (session_start.py, pre_tool_use.py, post_tool_use.py) still carry "work line"/"batch" — including user-facing lint strings — but were outside the item's enumerated doc-only scope; rather than expand scope mid-run, that was filed as capture [terminology-sweep-hooks-scope] for /plan to decide. A second capture, [next-surfaces-discovery-as-blocking-ask], records that /next first surfaced the hooks discovery as a blocking scope-ask instead of capturing it — the plan/next boundary reserves scope decisions for /plan, and the "third look" /next gives is preserved by capturing a discovery, not by halting the run to re-decide settled scope.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md
- plugin/si-plugin/docs/plan.md
- plugin/si-plugin/docs/next.md
- plugin/si-plugin/docs/next-build.md
- plugin/si-plugin/docs/next-audit.md
- plugin/si-plugin/docs/done.md
- plugin/si-plugin/docs/done-build.md
- plugin/si-plugin/docs/done-plan.md
- plugin/si-plugin/docs/done-audit.md
- plugin/si-plugin/docs/setup.md
- plugin/si-plugin/skills/next/SKILL.md
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md
- SPEC.md
- QUEUE.md (header)

**Routed to Captures:** next-surfaces-discovery-as-blocking-ask, terminology-sweep-hooks-scope
