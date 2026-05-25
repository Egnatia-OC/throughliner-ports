# V40 — 2026-05-21 — Shelve the two-write rule for canonical docs

**What shipped.** Dev-internal. V32 two-write rule shelved. Repo-root prose docs (`NO-CODE-METHOD.md`, `DOC-STRUCTURE.md`, `VOCABULARY.md`) and `templates/` frozen at V39 with FROZEN notices. Plugin-side becomes sole operational source. Method version stays V39. BUILD-METHOD's two-write section annotated as shelved. Project CLAUDE.md, README, plugin-side references, INVENTORY, OQ, PLAN.md all updated. Scope files renumbered (V40→V41, etc.).

**Decisions.** Freeze (not archive or delete) — lowest blast radius, resume path is one OQ promotion away. Annotate BUILD-METHOD section in place (resume-ability). Own session (not folded into drift-detection — one tag at a time). Method version stays V39 (dev-internal, no method substance).

**Pivots.** CLAUDE-TEMPLATE references `NO-CODE-METHOD.md` — adjusted to "frozen prose snapshot." `pre_tool_use.py` still cites `NO-CODE-METHOD.md` at 4 sites — flagged, not fixed. V42 bundling rationale dissolves (only plugin side now) — note added.

**Carried forward.** `pre_tool_use.py` citations unfixed. Three pre-v40 OQ entries committed alongside (part of same thinking arc).

