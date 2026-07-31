# 08823b6 — Build [scaffold-field-topup]: session-start content-level top-up for missing settings, Editor field first

Extended `session_start.py`'s drift detection so it catches not just missing files/folders (the existing presence-based `missing_scaffold` path) but a scaffolded file that exists yet lacks a *setting* the current templates have since added. The first and only case is the Editor field: a project set up before `[editor-awareness-core]` shipped has a CLAUDE.md with no `## Editor` section, so it silently misses the token-saving view-in-doc pointer and the user never knows to re-run setup.

The check is built as a small list (`setting_checks`) so future settings join by adding one entry — each entry names the host file that must already exist, the marker whose absence means the setting is missing, and the plain-English instruction to inject. It's add-only by construction: the injected instruction tells Claude to open its first reply by asking, in one line, which editor the user works in (they can skip), then write the answer into a new `## Editor` section — changing nothing else. The list supports both kinds of setting (needs-an-answer like the editor, and add-silently-with-a-note), though only the editor exists today. No double-flag: each check fires only when its host file (CLAUDE.md) is present, so a folder with no CLAUDE.md at all is left to the existing missing-file path.

SPEC gained a "Keeping projects current" paragraph stating the two-way catch-up (missing files → /setup; missing settings → add-only top-up, ask-when-input-needed), since SPEC carried no scaffold/drift statement before. FAQ gained an entry for the user who meets it ("A session opened by asking which editor I use, or saying my project was missing something — what happened?").

Fixture test (run in-session, plugin off): a CLAUDE.md missing `## Editor` triggers the top-up; a CLAUDE.md that already has it stays silent; a folder with no CLAUDE.md gets no content top-up (no double-flag). 3/3 pass. The live host-side behaviour (first real session in an Editor-less project asks and writes add-only) is deferred — observed after push + reinstall.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py
- SPEC.md
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
