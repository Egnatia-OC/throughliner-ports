# 087be76 — Harden the queue to one honestly-named shelf: redefine Unprocessed, state the single-shelf rule, add an anti-invention guardrail

The method repeatedly re-invented a fifth shelving category because its definitions left a gap: the rules said undesigned-but-worth-doing work "stays a capture in Unprocessed," yet Unprocessed was defined as "captured, not yet discussed" — and such work *has* been discussed. Claude filled the gap three times (a "below-line = external-waits only" category on 2026-07-13, a red-flagged line parked below the cleared-to-run marker on 2026-07-14, a below-the-line home for a never-to-be-built note on 2026-07-18), each caught by the user. This build closes the gap by sharpening definitions rather than adding machinery. In plugin-behaviour.md's four-state section: Unprocessed is redefined as "captured, not yet fully processed" (covering both never-discussed captures and discussed-but-not-yet-designed work, with a can-you-describe-the-build discriminator); Processed-below-the-line is sharpened to designed/buildable-but-not-greenlit and explicitly *not* a shelf for undesigned work; a "One shelf, one shelving move" rule states there is exactly one holding place (Unprocessed) and one shelving move (return to its bottom); an anti-invention guardrail forbids deriving a fifth state/tag/category and carries the three logged instances as its why; and a "Proper homes for recurring meta-items" list routes standing design considerations to SPEC/CLAUDE.md, durable findings to docs, and forward-recommendations to the transient advisory. The other eight files carry one-phrase gloss alignments to "not yet fully processed" so no doc, template, or hook lint contradicts the canonical definition. SPEC line 23 was already synced at the /plan close that filed this line, so this build left SPEC untouched.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md — four-state section rewrite (canonical definition, single-shelf rule, guardrail, proper-homes)
- plugin/si-plugin/docs/plan.md, next.md, setup.md (×2) — gloss alignment
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md, faq-template.md (×2) — gloss alignment
- plugin/si-plugin/hooks/post_tool_use.py — missing-section lint string alignment
- QUEUE.md — this project's header gloss alignment

**Routed to Captures:** none
