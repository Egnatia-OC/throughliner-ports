# [HASH] — session_start's missing-docset downgrade now says so in a plain state line instead of falling back to docset A in silence

The downgrade branch quietly reassigned to docset A when the selected docset's folder was missing from the installed plugin — and because the docset directive (which carries the self-check that would have caught exactly this) is only emitted for docset B, nothing reached the payload at all: a 5-series session on a mispackaged host would run the heavy docset with the project's Model field saying otherwise and no line anywhere admitting it. The branch now emits a one-line state line naming the three things a non-coder needs: which instruction set was selected, that its folder is missing from the **installed plugin** rather than the project (the distinction that is the whole diagnosis), and which set is running instead — phrased as a state line, not an error, since the session still works. Emitted on both the adopted and unadopted paths. Built now rather than waiting on [retire-docset-a] because that item inherits this logic either way: with A retired, a missing folder means no procedure docs at all, and saying so plainly becomes the only safe behaviour.

Verified two ways: the full hook schema check stayed green, and a scratch simulation (fake plugin root with no docs-b, fake project with `Model: Opus 5`) showed the state line arriving. That simulation is also what exposed the stale Editor catch-up ask retired under the working-mode item.

**Files touched:** hooks/session_start.py, SPEC.md (session_start description now names the never-silent fallback).
**Routed to Captures:** none for this item.
FAQ: not needed because a consumer only meets this if their install is broken, and the state line is self-explaining.
