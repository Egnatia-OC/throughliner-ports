# [HASH] — Five places where the shipped FAQ told consumers something the procedures no longer do

All in `templates/faq-template.md`, the copy every project receives.

**1. Readiness-line narration.** It promised Claude "tells you where it sits" at every planning session; `done-plan.md` mandates narrating only when the line actually **moves**, confirming silently otherwise. Corrected, with the reason visible to the reader — repeating an unchanged boundary every session is noise.

**2. The forward advisory's clear trigger.** It said the note is deleted "once you and Claude have agreed on the order" — the exact retired trigger, which `done-plan.md` names as the failure the /done-close clear replaced. Corrected, and the *why* kept: a session ending some other way never reached that moment, so the note survived and went on orienting sessions it no longer described.

**3. The missing-setting catch-up.** It said this runs at session start, contradicting another answer in the same file and `plan.md`, where it moved to /plan's first step. Corrected.

**4. Docset selection.** It said the plugin picks from the running model with "no setting for it" — contradicting three other places, `setup.md`'s question, and the template. Detection is unavailable in the desktop app, which is precisely why a recorded `Model:` setting exists. Corrected to describe what actually happens, including that the one question asks which model you run rather than which instructions you want.

**5. A retired section name.** An audit's findings were said to go "into Captures"; the live name is Unprocessed. Corrected.

The pattern across all five is the one the ripple-grep rule built this same run exists to stop: a rule changed at its home site and shipped, leaving the FAQ's statement of it behind. The FAQ is the worst place for that, because it is what a consumer reads *instead of* the procedure docs — they have no second source to check it against.

Distinct from [faq-backfill], which covers this project's own FAQ copy; this is the shipped template that reaches every consumer.

**Files touched:** `plugin/si-plugin/templates/faq-template.md`
**Routed to Captures:** none
**FAQ:** updated — five existing entries corrected
