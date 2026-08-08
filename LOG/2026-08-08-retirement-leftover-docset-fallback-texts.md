# ffab488 — Two docset-A retirement leftovers repaired: the behaviour rules' docset-choice section and SPEC's fallback sentence

Docset A retired earlier the same day, and the retirement build's grep covered path references but not prose describing the machinery. The 2026-08-08 differential consistency audit over the `overnight-blitz-2026-08-08` span found the two places where that prose survived, and this build is the audit's reconcile — both repairs are corrections to already-decided behaviour, with no design call in either.

The behaviour rules carried a whole section, "When the host doesn't say which instruction set to read," describing the session-start substitution directive, choosing between docsets by the project's `Model:` field, and a follow-the-host-or-project fallback table. None of that machinery exists any more: there is one docset, every skill names `docs-b/` directly, and no directive is emitted. A consumer session was being instructed on a situation that cannot occur, in text that contradicted CLAUDE.md's own Model target section. It is replaced by a short section, "When the installed plugin is missing its procedure docs," stating the one live behaviour — the hook reports a missing `docs-b/` plainly, naming that it concerns the installed copy rather than the project, and there is nothing to fall back to, so the session has no procedure docs at all and the answer is to reinstall.

SPEC's `session_start` bullet had the same problem in one sentence, and in the more damaging direction: it claimed the hook "falls back to the fuller docset" and names "which one is running instead", which is the opposite of what the shipped hook does. Rewritten to the report behaviour, matching CLAUDE.md's "what replaces the no-strand guarantee" paragraph — that a report is weaker than a fallback and is exactly what was traded away.

The claim in the new text was checked against the code rather than inherited from the item: `session_start.py` carries `_DOCSET = "docs-b"` with the model-detection branch gone and `_missing_docset_note()` documenting in its own comment that there is nothing to drop to, so both rewrites describe what the hook actually does today.

FAQ: not needed because the shipped FAQ template already carries two accurate entries on the retirement (the removed `/setup` model question, and the 4.8-no-longer-supported answer), and it never described the fallback behaviour these two documents had wrong. The project copy's stale docset-choice entry is [faq-backfill]'s, as the work item's own dedupe note recorded.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md` (section replaced), `SPEC.md` (one sentence in the `session_start` bullet).

**Routed to Captures:** none.
