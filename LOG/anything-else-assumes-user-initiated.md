# ee238d1 — Differentiate the mid-capture closer by who raised it (plugin-behaviour.md)

Built in a six-batch goal session (plugin off).

The "anything else?" closer after a mid-skill capture presupposes the user was accumulating things to capture. But the discovery-routing flow — for things Claude notices mid-session — is always Claude-raised, and it borrowed that closer from the user-raised capture flow, so it misfired every time: the user, who didn't raise the topic, was handed the conversational initiative as if she had a list going. Observed in a Taskflowapp E2E build (2026-06-22): Claude noticed within-card reorder work, filed a capture, then asked "Anything else to capture before I trim scope and build?" — which felt off because she hadn't raised it.

Change (plugin-behaviour.md):

- **Captures rule.** The "always ask 'anything else?' before resuming" rule gains an initiator split: a user-raised mid-skill capture keeps "anything else?" (they may be accumulating more); a Claude-raised discovery uses confirm-and-resume ("I noticed X, filed it, resuming") — informing without inviting, while still leaving the door open for the user to correct the capture. Names that the split is clean rather than a per-case judgement, because the discovery-routing flow is Claude-raised by construction.
- **Routing and discipline, discovery-routing flow.** Its closer is switched from "ask 'anything else?'" to confirm-and-resume, with a pointer to the Captures rule and the reason the "anything else?" closer belongs only to a user-raised capture.

Deferred host-side line written; rides [scope-boundary-rule]'s existing deferred test, which already watches the discovery-routing flow. The doc text landing is a review, not a pass/fail test.
