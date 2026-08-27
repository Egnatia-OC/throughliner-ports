# 99865ab — plan — [session-date-anchor] kept: session_start emits today's date, and date decisions read computed fields

Caught live: after an app restart mid-chat, Claude assumed a new day, dated a fresh capture 2026-08-27 while it was still the 26th, and read a post item's `Not before:` date as arrived — nearly walking a post a day early against the one-a-day pacing the user set. The digest had computed the date as a day ahead; the session did its own arithmetic on an assumed "today". The user reports the failure recurs — mostly small, sometimes big — which put the fix at hook-plus-rule level: session_start emits the date read from the clock, and an always-loaded rule bars deriving "today" by assumption. SPEC's session_start sentence gained the date line at the keep.

**Queue changes:** [session-date-anchor] filed and cleared; the two wrong dates in the droppable-set item corrected.
**Work processed:** kept — [session-date-anchor].
Rule gate: to run at the build; the disposition is on the item.
