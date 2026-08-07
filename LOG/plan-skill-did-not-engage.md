# [HASH] — Documented the /plan name clash with Claude Code's own plan command, and named the qualified form that works

**Diagnosed at processing: it was never a silent failure — the harness said what was wrong and the message was read as noise.** The session's error was *"plan is a UI command, not a skill."* That is Claude Code stating that the bare name `plan` resolves to one of its own built-in commands — it has a plan mode of its own. The plugin's skill was not skipped silently; its short name was taken.

**And the working form was already in use.** A later planning session was invoked as `/sovereign-implementer:plan`, the plugin-qualified form, and the skill engaged normally. So there is a form that works, it is the one the app offers from its own command menu, and nothing about the plugin is broken.

**Why it was still worth building rather than closing.** A consumer who types `/plan`, gets a Claude Code UI command, and has no idea why has no route to the answer — and this lands on the **install path**, which the release ritual already singles out as the one path nobody exercises after their first day, so it can break completely and stay broken. Naming the clash and the qualified form costs a paragraph and removes an unrecoverable first-day confusion.

**The detection half is recorded as a limit, not a plan.** The capture asked whether something should *notice* a procedure being followed with no skill around it. As far as could be told, the plugin's hooks fire at session start and around tool use, and none receives a signal naming the invoking skill — so mechanical detection is probably unavailable. Stated as a belief needing confirmation against the documented hook contract, per the check-what-the-tool-documents rule, and deliberately not designed against. If a future hook event exposes it, this can be reopened.

**One consequence to carry:** the session where this was observed followed the procedure by reading the doc directly, which worked because the docset directive was in context. That makes it weak evidence about how /plan behaves when properly invoked — relevant to anything relying on its observations.

No code change: the skill is correctly named and the app's own command menu offers the qualified form.

**Files touched:** `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`, `INSTALL.md`, `README.md`

**Routed to Captures:** none
