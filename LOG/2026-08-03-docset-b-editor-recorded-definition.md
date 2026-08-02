# [HASH] — Defined "editor recorded" once in docset B's working-mode render rule and pointed next.md and plan.md at it, fixing a live bug where setup.md's literal `not recorded` string read as a recorded editor

Docset A stated the test twice — in next.md and plan.md — and the subtraction dropped both, leaving docset B saying only "editor recorded" with nothing defining it. That is not lost wording, it is a live bug: docset B's own setup.md writes the literal string `not recorded` into the Editor field when the user skips the question, so a B session reads that string as a recorded editor, sends a pointer to a file the user has no way to open, and — because it pointed — pastes nothing in chat. The user gets nothing at all.

The definition now lives in plugin-behaviour.md's render rule and carries that why with it; next.md and plan.md each gained one sentence pointing there rather than restating it, which is docset B's register: one home per rule.

Weighed and kept despite two items that may make it moot — [desktop-native-md-open-vs-editor-field] could remove the Editor field entirely, and [line-anchored-link-dead-in-desktop-app] found the pointer path itself failing — because the fix is one paragraph and corrects behaviour that is wrong today. If the field is later removed, this rule goes with it.

**Files touched:** plugin/si-plugin/docs-b/plugin-behaviour.md (the definition, inside the working-mode render rule), plugin/si-plugin/docs-b/next.md, plugin/si-plugin/docs-b/plan.md.

**Routed to Captures:** none.
