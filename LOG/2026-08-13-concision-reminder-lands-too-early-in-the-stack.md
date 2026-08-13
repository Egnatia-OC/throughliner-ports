# [HASH] — A one-line tone reminder appended at the end of the session-start hook's injected context

Anthropic's guidance adds a placement rule that is easy to miss: in a long system prompt, pair the concision instruction with a short reminder near the end. That applies here more than it first appears. The output style is appended to the end of Claude Code's system prompt, which sounds like the last word, but three further layers land after it — the CLAUDE.md files, the `session_start` hook injection, and the skill's procedure doc. By the time the model is acting, the concision instruction sits a long way back behind several thousand words of procedure.

Alex chose the hook in her own words ("keep it in the hook"), on Claude's recommendation. The skill command prompts are the intuitive answer and sit genuinely later in the stack; that advantage was given up deliberately, because the same line would then be maintained in four places, in the layer this project is separately trying to shrink. The guidance asks for a reminder "near the end" rather than literally last, so the hook clears the bar at a quarter of the maintenance surface.

The line is appended as the final element of the injected context, after the FAQ pointer, which is the latest position available without touching anything else. Nothing else in the hook changed. The suites under `resources/testing/` were run and all pass, and the hook was invoked directly to confirm it still emits valid JSON with the new line last.

The honest case, stated so this is not overclaimed: it is cheap and officially recommended, and there is no evidence it works in this project specifically.

Rule gate: run — admitted, freestanding. One line, officially recommended, with the limit above stated rather than glossed.

FAQ: not needed because nothing about the workflow changes; the line steers Claude's own output.

**Files touched:**
- `plugin/throughliner/hooks/session_start.py` — a `<tone_preference>` line appended as the last element of the injected context.

**Routed to Captures:** see this session's other entries.
