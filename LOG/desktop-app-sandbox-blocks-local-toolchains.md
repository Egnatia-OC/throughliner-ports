# [HASH] — Built the blocked-capability ladder — try, research, ask once, hand back — with the MSIX sandbox as its worked example

The finding underneath this was established by isolating a failure layer by layer rather than by inference: the Claude desktop app is an MSIX-packaged Windows application, so everything it launches inherits a package sandbox that permits *binding* an AF_UNIX socket but refuses *connecting* to one. That is exactly what Java's NIO selector needs, and therefore what every Gradle build needs. Plain TCP loopback works, which is why the surfaced error — `Unable to establish loopback connection` — points away from the real cause.

**But the item was re-scoped by the user before building, and the re-scope corrects its whole framing.** It had been processed as "warn the user about the sandbox and document it". That is not what went wrong. The user never needed the sandbox explained; they needed Claude to say *"I can't build this — build it in Android Studio"* and move on. They already owned the tool that does the job and were never asked to use it. In the user's words the actual failure was "spiralling around and around doing nothing" — the sandbox was only what triggered it.

So the deliverable is general, not a Gradle fix. The reach-for-a-CLI rule is strengthened into a fixed four-step order, and two changes carry the weight: **research becomes mandatory when blocked**, before involving the user at all — a non-coder cannot ask for a tool by name, so if Claude does not look, nobody does — and **asking for a named tool is stated as legitimate** rather than something to avoid, because the surrounding rules lean so hard against sending the user off that they discourage the one ask that actually helps. Repeated hand-off is named explicitly as the failure mode, since it is worse than either doing nothing or asking once.

The active check in `session_start` names the constraint **and the hand-off in the same breath**, so a user meets an answer rather than a diagnosis. It is worded conditionally — "if you are running in the Claude desktop app" — so the hook never has to detect its own surface, which sidesteps the one genuinely undesigned piece at the cost of a clause.

Also settled: **describe the blocked operation, not the tool.** The failure is AF_UNIX connect, so anything else depending on it fails the same way; Gradle is named as the case that surfaces it, never as the scope.

The terminal escape stays dead and must not be revived. An earlier version carried "run Claude Code from a terminal" as an untested workaround; the platform decision now in SPEC settles that the desktop app *is* the platform, and a workaround this audience cannot perform is not a workaround.

SPEC was already done — the ladder and the platform decision were written into it at the planning session that re-scoped this — so the build inherited SPEC rather than editing it.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`, `plugin/si-plugin/hooks/session_start.py`, `plugin/si-plugin/templates/faq-template.md`, `plugin/si-plugin/templates/faq-index-template.md`, `INSTALL.md`, `README.md`

**Routed to Captures:** none
