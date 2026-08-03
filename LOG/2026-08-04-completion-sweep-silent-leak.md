# [HASH] — A suppressed or silent scan contributes nothing to a skill's opening narration — including no mention that it was suppressed

Observed live at a /plan opening: Claude narrated that a background setting was in one mode, so it wasn't sweeping for already-done `[user]` items. Two faults in one line — the mode suppresses that scan *entirely*, with the doc saying "say nothing about it," so narrating it at all was wrong; and the setting's name is background-only vocabulary that should never reach the user.

The jargon half needed no work here and was recorded rather than carried: [user-lines-walk-through-only-no-asks] retires that field outright in the same run, so the term stops existing and can't leak. Recorded so nobody built a vocabulary entry for a setting being deleted.

The half that survives is general and outlives the setting. The likely pull was the consolidate-the-scans rule, which invites a single opening summary of what the opening checks surfaced. A *silent* check got swept into that roundup rather than staying silent — and that failure mode isn't specific to this setting. Any future suppressed step can be pulled in the same way, because the rule asks for a roundup and a suppressed step is still a step that ran.

The carve-out is stated on the consolidate rule itself. The second clause is the load-bearing one: **including no mention that it was suppressed.** "I'm not doing X, because Y" is precisely the shape the live failure took, and a carve-out that only said "don't report its findings" would have permitted it. The wording now says a step told to stay silent produces no words at all, and the roundup summarises what the speaking checks turned up.

This is a wording fix rather than a hook, and the reasoning is recorded: the rule that slipped was already clear in plain terms and still leaked, which by the project's own rule-writing guidance points at the *neighbouring* rule creating a pull the clear rule doesn't answer — not at the clear rule needing enforcement. Nothing mechanical can detect a narration that mentions a scan.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md` (the consolidate-the-scans rule).
**Routed to Captures:** none.
