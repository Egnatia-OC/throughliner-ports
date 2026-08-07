# 96166c6 — Said which docset wins when a stale host emits no routing directive, and made the choice visible rather than silent

Most of this item was already resolved by shipped work: the session-start hook now emits a docset directive on every 5-series session, carrying its own self-check. So the manoeuvre the original capture recorded as a judgment call nothing permits — the skill naming one path and Claude reading another — is now issued by the plugin itself.

What remained is the narrow window the capture was born in: **an installed host too old to emit the directive at all.** With no directive there is no sanction, and a session is back to improvising between the skill's named path and the project's recorded `Model:` field. That window opens at every stale-host moment and closes at the next reinstall — real, but self-curing.

The answer is inherited rather than invented. The method already handles the neighbouring case: when the selected docset's folder is missing from the installed plugin, the hook falls back and says so in a plain state line — which docset was picked, that its folder is absent from the plugin rather than the project, and which is running instead. Never silently. The same posture now covers the disagreement case: follow the project where the host carries that docset, follow the host where it does not, and say which in one line either way.

**Why announce rather than halt**, since halting was one of three options on the table. A halt is heavy for a condition a reinstall cures, and it would fire hardest on exactly the user least able to diagnose it. And the recorded failure was never that the wrong choice was made — it was that **the choice was invisible**: nothing recorded it, and the opposite call would have looked equally reasonable to a later reader. A stated line fixes the actual defect. What is ruled out is silently preferring either side.

No hook change: the missing-folder fallback already exists and this is its no-directive sibling, governed by behaviour rather than code — because a host too old to emit a directive is equally too old to carry a new check.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`

**Routed to Captures:** none
