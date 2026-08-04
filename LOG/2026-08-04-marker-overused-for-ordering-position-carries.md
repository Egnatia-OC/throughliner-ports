# f832385 — Restore one lint-checked `Blocked by:` field and stop expressing dependencies as prose lift-conditions or position

The original framing was "position already carries this," and the user's own correction is what made the item buildable: position expresses *order*, not *dependency*. It has no memory of why the order is what it is, so a dependency held only by position can be silently inverted by the close-time reorder that runs every planning session — which has no way to know a particular ordering was load-bearing. Explicit dependency edges survive reordering precisely because they don't rely on it.

The method used to have this, and the removal was deliberate, so this is recorded as a considered reversal rather than a rediscovery. The queue redesign demoted the slug to traceability-only and removed the dependency headers, the tracing that read them, the close-time backstop, and the lint. What that redesign bought was real and is not being undone — the old apparatus was not one field but several, plus parked states, unpark scans, a parked shelf and a staleness watch. **This restores one field, not the machinery.**

What the removal cost is what the evidence showed: dependencies did not stop existing, they moved into prose lift-conditions nothing validates, and into position. In a single planning session, five lift-conditions were written naming another queue slug — by a session that had just read the capture warning against exactly that. The information is already being written every time; it was simply going somewhere nothing could check. That is the argument that this formalises existing behaviour rather than adding burden.

Three-way routing is stated once so the choice isn't re-derived: `Blocked by:` for a dependency on other queued work, the push marker for work that must be shipped and running first, and lift-conditions shrunk to genuinely external events only. A lift-condition naming a queue slug is now named as the signature of a misrouted dependency, and the planning close fixes such a line as a pointer fix rather than deferring it as a fate decision.

The lint is what makes it real, and the reasoning is recorded: wording has demonstrably failed at this, and the method's own principle is that hooks enforce what must never happen. It's advisory like the rest — it flags a slug that resolves to nothing, one pointing at an item below the blocked one, a self-reference, and a field naming no slug at all. Verified against a fixture covering all four failures plus the valid case, and run live against this project's queue, which is clean.

Scope was traced by grepping the literal values across the repo before the build started, per the hook-enforced-format rule, rather than written from the discussion.

**Files touched:** `plugin/si-plugin/hooks/post_tool_use.py` (new check 4), `plugin/si-plugin/docs-b/plan.md` (the keep-step's routing choice), `docs-b/done-plan.md` (what a lift-condition may now say), `docs-b/plugin-behaviour.md` (the three routes stated once, and the below-line revisit), `SPEC.md`, `faq-template.md` and `faq-index-template.md`.
**Routed to Captures:** none.
