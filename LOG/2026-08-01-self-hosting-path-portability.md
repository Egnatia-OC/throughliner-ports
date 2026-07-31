# [HASH] — Make SI's self-hosting rituals path-portable so a fresh clone can run them

CLAUDE.md hard-coded machine-specific absolute paths (`C:\Users\Alex\…`), some stale — saying `Alex` where the real path is now `Alex 2`, and carrying the `Prioritiy` typo — so on another machine (and in places on this one) the Rezip/Push rituals and E2E pointers couldn't be followed as written.

Fixed the four live-ritual paths in CLAUDE.md: the sub-folder-lookup example, the `claude plugin marketplace add` command, the Codex-port source path, and the Taskflowapp path. Each became a clearly-marked substitutable placeholder (`<PROJECT_ROOT>`, `<TASKFLOWAPP_ROOT>`) with an inline note, and the stale `Alex`/`Prioritiy` spellings were fixed in the same pass.

Judgment made rather than halting: the `resources/` matches (captures, a saved transcript, and observational lines in research/claude-code-plugin-install-paths.md) were left untouched. They are historical records — "the user invoked /setup in `<path>`", "the CLI was installed at `<path>`" — not rituals a fresh clone runs, so rewriting them would falsify a record of what was true then, the same principle that leaves LOG history alone. Host-doc only (not shipped in the plugin package).

**Files touched:**
- CLAUDE.md — 4 hard-coded paths → portable placeholders; stale spellings fixed

**Routed to Captures:** none
