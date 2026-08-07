# 96166c6 — An interrupted pending ask is re-asked alone, never bundled with the interruption's handling

Mid-session, Claude put a fresh capture confirmation and a pending work-item approval into one message. The user's "approve" was meant for the capture, and the work item was executed on it — caught only because the user said so: *"I didn't realise you'd bundled the ask."* The one-item-at-a-time rule was loaded and explicit, and it still slipped at exactly the moment it protects: two live asks in flight after an interruption.

**Not judged a one-off, because the same condition recurred during its own processing.** The user interrupted a pending work-item approval with two screenshots of an unrelated problem; that interruption was handled to completion and the pending item re-presented alone before any decision was asked for. The right shape happened — but by judgment rather than by rule, since nothing in the docs names this case. **A fix that works only when the session happens to notice is not a fix.**

**Two properties make it worth a rule rather than vigilance.** A short affirmative — "ok", "approve", "go ahead" — **binds to the most recent ask**, so the instant two asks are live, every cheap approval word is ambiguous, and cheap approval words are exactly what a well-run session trains the user to give. And the failure is **silent**: an approval landing on the wrong ask leaves no trace anywhere. Last time it surfaced only because the user happened to mention it, which is not a detection mechanism.

The rule is narrow and stated as the hardest case of an existing one: new input arriving while an ask is pending is never answered in the same message as that pending ask. Handle the interruption to completion, then re-ask the pending item on its own, **restating what it is** — because after a detour the user has lost the thread as well, so a bare "so, approve?" is not a re-ask.

**Authored as a named case rather than a firmer general rule**, because firmness was never what was missing. In the moment it does not feel like two items; it feels like one item plus some housekeeping, and housekeeping does not feel like an ask. Naming that specific misperception is the whole value.

**Files touched:** `plugin/si-plugin/docs-b/plugin-behaviour.md`

**Routed to Captures:** none
