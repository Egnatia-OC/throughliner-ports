# [HASH] — plan.md: neutral end-of-queue gate — an empty Unprocessed no longer presumes close

Observed in testing: when the last Unprocessed item was processed, /plan leaned toward closing — sometimes running the wind-down re-scan straight away — rather than asking whether the user had more to capture or discuss; and when the user did raise a further capture after that point, /plan filed it but re-leaned to close.

Fixed in plan.md, keyed on one principle: an empty Unprocessed is a resting state, not a signal the session is over. (1) The last-item checkpoint off-ramp is now neutrally worded ("anything else to capture or discuss, or close out?"), not a close-lean. (2) A "Neutral end-of-queue gate" fires when Unprocessed empties — the wind-down re-scan and Step 3 close only proceed once the user actually chooses to close. (3) After a further user-filed capture, the flow returns to the same neutral gate rather than re-leaning to close, honouring the "close by who raised it" rule in plugin-behaviour.md.

Does not conflict with [collapse-redundant-progress-gates]: that trims redundant gates at the session opening; this ensures one neutral off-ramp at the end of the queue. No SPEC/FAQ — interaction wording, not a new feature.

**Files touched:**
- plan.md (Step 2 checkpoint last-item wording; "Neutral end-of-queue gate" after all items)

**Routed to Captures:** none
