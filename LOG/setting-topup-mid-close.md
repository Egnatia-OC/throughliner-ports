# 96166c6 — Deleted the session-start setting top-up and rehomed the catch-up in /plan's opening read

The top-up told a session to open its first reply with a missing-setting question. Three sightings: it wedged *"Which .md editor do you work in here?"* into an already stop-heavy close; it fired in this project the same day; and on remote control it opened a fresh session's `/next` and **held a queued run — four builds plus a walk-through — behind it.** The user's reaction is the design input: *"why do you need to know that?"* — the ask solicited a setting whose purpose they no longer even remembered, which is what an execution-gating question must never be.

Re-verified at processing rather than trusted: the hook carried an empty check list with the machinery intact, and the text it injected read *"Bring it up to date now, before /next or /plan."* **So the run-gating was not the mechanism misfiring; it was the mechanism doing exactly what it instructs.** That reframed the fix — this was not a timing bug to be retimed.

**Neither "retire it" nor "retime it inside the hook" is right, and the reason is structural.** A session-start hook fires **before anything knows what the session is for**, so its question cannot choose a good moment — it can only attach itself to whichever command comes first. Retiming it in place would mean writing a rule instructing the hook not to do the thing its position makes it do, which is the weakest kind of fix.

**Not deleted outright despite the user's lean**, because it is the only thing that reaches a project set up weeks ago when the method later adds a setting. Without it, a new setting arrives only if the user happens to re-run /setup — and that need is about to be concrete rather than hypothetical, since a queued item adds exactly such a field. Deleting the mechanism and rebuilding it for that item is churn.

So it moves to /plan's opening read, which already reads project state, already folds what it finds into one narration, and is **structurally incapable of holding a /next run** — the whole point of moving it.

**Whatever asks must say why it wants the answer.** The failed question failed on two counts and only one was timing: it was also unanswerable, because neither the user nor the session asking could say what the answer was for. Any catch-up question now names the setting, what reads it, and what changes once it is answered.

The presence-based missing-scaffold check is deliberately untouched: it detects whole files or folders absent, is a different check, and gates nothing.

**Files touched:** `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/docs-b/plan.md`, `SPEC.md`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`

**Routed to Captures:** none
