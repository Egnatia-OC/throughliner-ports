# V30 — 2026-05-20 — Method docs relocated into plugin; Reference manual rewritten as standalone primer

**What shipped.** Doc relocation (`NO-CODE-METHOD.md` + `DOC-STRUCTURE.md` → `plugin/docs/` via `git mv`; subagent bodies updated to `${CLAUDE_PLUGIN_ROOT}/docs/...`). Reference manual fully rewritten as standalone primer (install + first session up front; planning-input paragraph tightened; Risk-accepted example corrected). Plugin README gains Reference manual link. NO-CODE-METHOD *Before build* closing prompt reframed defensively re plan mode. BUILD-METHOD gains *Graduation paths* sub-section for OQ entries. CLAUDE-TEMPLATE (×2) rewritten for plugin-bundled location. INVENTORY updated for new doc locations. V31/V32 scope files frame-corrected. OQ git-workflow entry refreshed with Sonnet web-search; `planning/drafts/git-integration-research.md` committed. Ten new OQ entries surfaced (five from retrospective, five from Reference manual review). 21 footers bumped V29 → V30; `plugin.json` → `0.30.0`.

**Decisions.** Bundled doc + sister-doc symmetry — DOC-STRUCTURE as reference doc, not skill body; scope expanded to relocate NO-CODE-METHOD alongside. Full Reference manual rewrite, not surgical — standalone-primer criterion required it. Reference manual stays at repo root — audience is humans, not plugin runtime.

**Pivots.** Subagent read-spec-on-entry was silently failing pre-V30 — `CLAUDE_PLUGIN_ROOT` substitution wasn't applied; relocation surfaced and fixed it. Git index corruption from bash mount + Drive sync; recovered via PowerShell `git read-tree HEAD`. Session split across two Cowork conversations (length limits). Ten OQ entries surfaced — largest blind-spots: no consumer-side BUILD-LOG, no git workflow, GUI-centric phrasing.

**Carried forward.** Ten OQ entries parked for V31+. Git-workflow research at `planning/drafts/`. Reference manual review pass parked pending OQ planning session. Next session is OQ planning, not V31 directly.

