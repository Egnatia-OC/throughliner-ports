# 7bc2c58 — The migration now quotes a plain-prose section preamble, and this project turned out to have nothing to fix

The item's premise was that this project carries thirteen standing lint flags. Checked first, as the item asked, and it is no longer true: the lint reports **zero** here, because this project's preamble sits above `## Processed` rather than inside it. So the local half was moot and only the shipped half was built.

The lint reads un-quoted, un-headed prose inside a section as an orphaned rationale and warns that a heading may have been overwritten. A section preamble legitimately has no heading. The scaffold has shipped these as blockquotes since 2026-08-15 — and a blockquote is exempt — so only projects adopted before that date carry the warnings, on text `/setup` wrote itself. Both fire at every queue edit, which is what teaches a user to read past the lint.

`setup.md` gains a migration step and `migrate-checklist.md` a matching section: prefix each preamble line with `> `, wording untouched.

Carried across unchanged rather than re-decided: the 2026-08-15 refusal to widen the lint's exemption to any first paragraph, which would exempt genuinely orphaned prose — the thing the check exists to catch.

**Files touched:** plugin/throughliner/docs/setup.md, plugin/throughliner/docs/migrate-checklist.md
**Routed to Captures:** none
Rule gate: not needed — a migration step is added; it authors no method rule, and the earlier refusal is carried rather than re-made.
