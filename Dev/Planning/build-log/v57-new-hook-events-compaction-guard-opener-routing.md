# v57 — 2026-05-22 — New hook events (compaction guard + opener routing)

**What shipped.** Scope 0055. Two new hook events: (1) PreCompact hook (`pre_compact.py`) — blocks compaction during active builds, surfaces paste-ready handoff prompt. Silent when no active build. (2) UserPromptSubmit hook (`user_prompt_submit.py`) — keyword-based first-prompt classification (setup/test notes/resume) as routing hint. Conservative thresholds; transcript-marker first-prompt detection. Session handoff protocol added to `universal-behaviour.md` (4-step process). Hook-assisted classification added to routing table. Doc-code parity across DOC-STRUCTURE, VOCABULARY, Reference manual, INVENTORY. "Six prose directives" OQ fully resolved. Footer V51→V52; plugin 0.51.0→0.52.0. Tests: 17 new (6+11); suite 147 passed.

**Decisions.** PreCompact can't inject `additionalContext` (platform limitation) — reframed to block+handoff instead of context preservation. Handoff notes in batch itself (already carries tick state). UserPromptSubmit uses transcript-marker for first-prompt detection (same V39 pattern).

**Pivots.** Scope assumed PreCompact could inject context — research disproved. Complete design reframe.

**Carried forward.** Deferred smoke tests unchanged from v56.

