# Principle audit

*Single-instance. State-driven step-back to ask whether you're missing higher-leverage moves.*

## Trigger

A state, not an event: the doc structure is settled enough to step back from, and you have bandwidth to question the meta-design — not just the contents. The canonical opener: "are there principles I'm not using that I could be?"

The condition is that a recent version cut feels stable, *and* you have the energy to question the higher level. Without the second part, the audit produces tweaks instead of real principles.

## Steps

Unprompted:

- Anchor the audit by listing principles you are *already* using well. Without that anchor, an audit reads as a refactor-everything proposal.
- List principles you aren't applying, ranked by likely impact.
- For each principle in the initial list, include one concrete sentence about what applying it would look like in the current docs. Don't name principles abstractly and wait to be asked to translate.
- Be honest where you disagree with a prior decision (re-raise points walked back if the framing has shifted; flag if the user's earlier reasoning was incomplete).
- Close with an offer: dig further, or draft a concrete proposal.

User brings:

- The state of "I have bandwidth for this and the docs feel stable."
- Confirmation or pushback on each principle.
- A signal to draft the next-version queued prompt once the principles have settled.

## Output

- A ranked list of content-level principles you could apply more, each with a one-line concrete picture of what application would look like.
- For each confirmed principle, a structural sketch where one is needed (e.g. a new file's three-part structure).
- A queued prompt ready to paste into the next session as a [[Spec-driven version cut]] trigger. The audit's natural deliverable is a Pass A prompt.
- Separately: a list of process-level rules surfaced incidentally during the audit (these don't go into the spec — they go into this project's `CLAUDE.md`).

## When wasted

- You don't have time to follow through with a version cut afterwards. An audit that doesn't lead into execution is thinking out loud — fine for casual exploration, but the value compounds only if it ships.
- The doc structure is too unsettled — you're still deciding what the docs should *do*, not refining what they already do. Audits assume a stable target.
- You've recently run one. Run-frequency dilutes impact; the second pass surfaces low-impact tweaks instead of real principles.

## Refinements

- **Concrete-picture every principle in the first listing.** Don't just name it. One line of "here's what this would look like in your files" per principle, in the initial response. Removes the round-trip where the user has to ask for the translation.
- **Separate content-level principles from process-level rules at the start.** Don't bundle them — they have different homes (the spec doc vs. this project's `CLAUDE.md`).
- **Flag re-raises of walked-back principles explicitly.** Don't re-pitch a walked-back idea without saying "you walked this back in our last pass; here's why the framing has shifted." That gives the user a clean choice instead of feeling re-pitched.
- **Offer the meta-procedure write-up at the close**, not waiting for the user to ask. If the audit produced anything that worked well as a repeatable pass, name it before the session ends.
