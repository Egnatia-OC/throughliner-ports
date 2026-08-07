# [HASH] — The ripple-grep generalised from hook-enforced formats to any rule change, with the leave-alone line as its gate

CLAUDE.md already required that a change to a format or enum the hooks enforce trace its ripple by grepping the literal values. That rule now has a sibling immediately beside it, aimed at prose: **when a work item alters what a rule *says*, grep the rule's key terms and names across the corpus before the file list is finalised, and record every statement site found — each one either joins `Files:` or carries an explicit one-line `left alone because …`.**

The evidence is why this is stated as a rule rather than an intention. The 2026-08-07 pre-compression audit found that nearly every contradiction it turned up had one cause: a rule changed at one of its statement sites and shipped, leaving its other statements behind — the Claude-raised capture closer, the write-order split, the scaffolded red-flag text, the scope-lock's allow-set stated three different ways. None was an authoring error at the changed site. Each was ripple that nothing traced. The planning session that processed those findings demonstrated it live: the write-first rule had changed in `plugin-behaviour.md` while six step-level instructions kept saying the opposite, and `setup.md` kept scaffolding a contradicting red-flag line into every consumer's queue.

**The grep pays immediately, which is the argument for it.** In that one session it found a sixth show-first site the capture's own list had missed, falsified a capture's confident "docset A's copy is correct too" by finding the identical bug in A, and established that no third instance existed so nobody re-runs that sweep. Each cost under a minute and each changed the file list.

**The leave-alone line is what makes this a gate rather than an intention, and that asymmetry is the whole mechanism.** "Grep for ripples" cannot be checked after the fact — nothing distinguishes a grep that found nothing from a grep nobody ran. "Every hit either joins `Files:` or carries a one-line reason" is visible in the item, so a reader can tell whether it happened.

Host-only, exactly like its sibling: a consumer's corpus is SPEC plus CLAUDE.md plus a queue, a restatement surface too small for the payoff to cover a grep per rule-change. Not shipped to `plan.md`.

**Files touched:** `CLAUDE.md`
**Routed to Captures:** none
