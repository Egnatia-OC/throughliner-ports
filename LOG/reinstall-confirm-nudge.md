# 29ba751 - session_start.py + FAQ: reword the update message into a plain-English confirm-session nudge, narrowed to host-side deferred tests

When a user reinstalls an update, the natural next step is a quick session to confirm the new behaviour - really a test session a non-coder does not recognise. The version-change report's deferred-tests sentence was written in mechanic's terms (deferred tests / live-testable / roll into a test batch) and pointed at plumbing. It is now a plain-English nudge: an update was installed, run a quick session to confirm it behaves, framed as a testing session, with a plain pointer that /plan can line up the checks. The trigger is narrowed to host-side deferred-test lines (the ones a reinstall makes checkable). An in-session hook test confirmed host-side fires the nudge, needs-user-only does not, and no version change fires nothing.

**Files touched:**
- plugin/si-plugin/hooks/session_start.py
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
