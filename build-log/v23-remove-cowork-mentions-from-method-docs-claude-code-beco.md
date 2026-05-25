# V23 — 2026-05-17 — Remove Cowork mentions from method docs; Claude Code becomes explicitly required

**What shipped.** Cowork-removal sweep: NO-CODE-METHOD makes Claude Code explicitly required; Reference manual rewritten (two-phase framing, new-project-route walkthrough, single-column editing table); DOC-STRUCTURE, templates (×4), planning.md, pre_tool_use.py, session_start.py, init-project/SKILL.md all stripped. Dev-project CLAUDE.md left unspecified (Alex mid-migration). OQ prose-only-rewrite entry noted framing shift. PLAN.md renumbered. Footers V22 → V23; `plugin.json` → 0.23.0.

**Decisions.** Claude Code is required, not recommended — method ships as plugin, can't run elsewhere. Replacement wording "by hand during planning sessions" preserves fold-in mechanism while updating location. Dev-project CLAUDE.md unspecified — Alex has no fixed migration timeline. Internal planning artefacts left alone (historical record).

**Pivots.** Reference manual rewrite bigger than anticipated — "Where each tool fits" was load-bearing framing. "Edit by hand" introduces a soft discipline that didn't exist in Cowork era — user *can* now edit UX.md mid-build (only Claude's edits blocked). Cowork parallel-session corruption during prep (CRLF mangling; recovered via `git restore .`).

**Carried forward.** Live install + back-test of V18–V23 owed. Soft-discipline risk for mid-build SoT edits recorded. OQ cross-version entry still has Cowork vocabulary.

