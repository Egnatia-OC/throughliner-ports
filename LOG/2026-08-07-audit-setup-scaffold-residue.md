# 5993a10 — Retired-interview residue cleared, the dead Language field removed after checking, and resources/testing/ added to the scaffold

`setup.md`'s SPEC and QUEUE scaffolds still carried `[filled by Q1]` through `[filled by Q4]`, and a step called "Peek before Q1", though Step 3 is now an adaptive interview whose only numbered question is Q6 — Q1 through Q5 exist nowhere. The placeholders now describe what fills them ("from the interview: what the project is") rather than pointing at questions that no longer exist, which is also more useful than the numbers ever were. The Step 3 heading promised "three settings" while the body carried one; corrected.

**The `Language:` field was confirmed dead before removal rather than assumed.** A grep across both docsets, all hooks and the templates found **no reader at all** — nothing fills it, nothing reads it. Removed from `CLAUDE-TEMPLATE.md`.

**And its retirement carried a ripple, found the way this run's new grep rule prescribes.** Projects set up before the removal still carry the line, and no migration reaches every project. `plugin-behaviour.md` keeps a list of retired fields to be **ignored silently** — never acted on, never flagged, never treated as a broken project. `Language:` joins it, with a one-line note on why. Without that, the very next session in an existing project would meet an unlisted stale field and have no rule for it.

**`resources/testing/` is now scaffolded alongside `resources/research/`.** The behaviour rules sanction both as the only two things `resources/` ever holds, but /setup created only one — and the research folder's own stated rationale ("so it exists before first use, rather than being conjured on first use") argues identically for testing. Both are now created together, with that shared reasoning stated once.

**Files touched:** `plugin/si-plugin/docs-b/setup.md`, `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`, `plugin/si-plugin/docs-b/plugin-behaviour.md`
**Routed to Captures:** none
