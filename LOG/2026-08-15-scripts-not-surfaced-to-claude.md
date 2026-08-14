# [HASH] — The scrub rule names scrub_sweep.py as an additional pass, and the general scripts clause is refused

Captured by the user in her own words: maybe there should be a list of on-hand script tools available to Claude inside the always-loaded rules so Claude knows about them.

The evidence that makes it more than speculation: listing the plugin's scripts folder at her prompting returned four files, two of which are used constantly and named in `plan.md`, and two of which had never been mentioned in that session or, as far as it could tell, considered at all. One of those is `scrub_sweep.py` — and the always-loaded rules describe the scrub checklist as something Claude performs by reading its own writing, never mentioning that a script exists which sweeps for the same shapes. The method ships a tool for one of its own gates and does not tell the session running that gate.

**The general rule the user proposed was tested against the gate and failed it, and she chose the narrow fix after being shown the result.** Script references across the nine skill docs land in three of four skills, weakly in two of those, and zero in /setup. The always-loaded file's admission bar is that a rule fires in all four. And the evidence stops it at the gate's first question anyway: there is exactly one pointable instance, since a test file no session would routinely run is not one. One instance is below this project's own bar for a freestanding rule.

So what shipped is a subordinate clause on the existing scrub rule, with a named parent, spending no slot.

The wording matters more than its size. Naming the script must not let a session substitute it for the read: the rules already state that the script matches shapes only and cannot tell whether a sentence quietly identifies a real person. The clause says "run it alongside the read, never in place of it", so it names an additional pass and never the gate.

What is refused, recorded so it is not re-proposed without new evidence: a general "the plugin ships scripts — list that directory before doing by hand what a script may already do" clause. If a second instance turns up, that is the evidence it needs.

This is the same shape as the output style, one layer down — a shipped component sitting outside every map, so nobody reasons about it — and both were found the same day from the same direction.

Rule gate: run — one subordinate clause admitted onto the existing scrub rule, with a named parent, spending no slot. One proposal refused in the same move, on the four-skills test and on having a single pointable instance.

FAQ: not needed because the scrub checklist's promise to the user is unchanged, and this project's standing refusal to tell anyone their artifacts are clean is deliberately untouched.

**Files touched:** `plugin/throughliner/docs-b/skill-nonspecific-rules.md`.

**Routed to Captures:** none.
