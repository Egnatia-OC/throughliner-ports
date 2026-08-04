# [HASH] — Editor field rescoped from reading to editing, and dropped as a condition on whether pointers are used at all

The `Editor:` field was introduced to answer "which app do we point the user to."
It never did that. Links open in the desktop app's own viewer whatever the field
says. What it actually did was act as a gate: a pointer was eligible only when
working mode was local *and* an editor was recorded — so a field controlling
nothing was deciding whether the pointer path ran at all. A project that skipped
an optional question got a different rendering rule as a side effect.

That condition is gone. Local mode alone decides, and a project with no editor
recorded still gets pointers, because the app opens the file either way.

The field keeps one real job, and it is a different one from the one it was given.
`.md` files are read-only in the desktop viewer — code files get an editable
buffer and a save affordance, markdown does not (filed as
anthropics/claude-code#83476). So an external `.md` editor still matters for
editing by hand, never for reading. /setup's Q6 was rewritten to ask that
question: where would you go to change something yourself, with skipping named as
a completely normal answer, since Claude does the writing and plenty of users never
edit a doc by hand. The old wording sold the setting as what makes doc links useful,
which was never true.

Worth recording because it was inherited for a while: this item's original title
and premise claimed the desktop app opened `.md` links "at the correct line".
Live testing on 2026-08-03 showed a line-anchored `.md` link is dead — the click
does nothing. Only the other half was true, that `.md` links open natively in the
app's viewer, always at the top.

Built alongside [write-first-link-dont-paste], deliberately and in one scope: both
rewrite the same paragraph, and this item removes a condition that item's rule
depends on, so building them apart risked two passes disagreeing.

**Files touched:** docs-b/plugin-behaviour.md (the editor-recorded condition
removed from the pointer gate), docs-b/setup.md (Q6 rewritten), docs-b/next.md and
docs-b/next-build.md and docs-b/plan.md (the same condition removed from their
render lines), SPEC.md (working-mode description plus a new Editor-field
paragraph), templates/CLAUDE-TEMPLATE.md (the Editor and Working mode field
comments), FAQ/faq.md + FAQ/index.md. Docset A is frozen and was not touched.
**Routed to Captures:** none from this item.
**FAQ:** updated — "/setup asked me which editor I use. What does that actually
change?"
