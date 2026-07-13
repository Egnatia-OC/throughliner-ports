# ca03428 — Point-and-work: operate on the folder the session opens in; session_start flags nested SI projects

Made explicit that Claude works on the folder the session was opened in and never scans parent/child folders to pick a different project or asks which project to work in — the folder it's pointed at *is* the project. This supports the intended shape (several independent SI projects nested under one parent) and replaces the retired "multi-spec" idea. Two edges: an unadopted opened folder → offer /setup here, don't hunt for an adopted folder nearby; an opened parent that visibly contains nested SI projects → name what's there so the user can course-correct, since /setup would otherwise adopt the parent. Backed by a session_start change: the not-adopted branch now detects child folders holding their own SPEC.md/QUEUE.md and appends a heads-up naming them. Detection only — the choice stays the user's. Hook compiles clean.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py — State-1 nested-SI detection
- plugin/si-plugin/docs/plugin-behaviour.md — new "Operate on the folder the session opens in" section
- plugin/si-plugin/templates/faq-template.md + faq-index-template.md — new entry + index line

**Routed to Captures:** none
