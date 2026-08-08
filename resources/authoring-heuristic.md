# Authoring and sharpening rules in this project

This is the project's guide to writing the method's own rules well — the procedure docs, the behaviour rules, the hooks, the SPEC text. Everything in it is model-agnostic: it holds whatever model the project targets.

Run it before authored method text ships. The three checks are the per-text pass; the hook-versus-wording section is the judgment you reach for when a rule has slipped or a new rule needs a mechanism.

**There is no per-model authoring pass, and that is deliberate.** This doc used to carry one for Opus 4.8 — the model docset A was tuned for. That docset retired on 2026-08-08 and 4.8 is no longer a supported model, so the checklist was deleted rather than marked historical: a document that reads as live gives live instructions, and its four model-specific checks were all prescription-*adding*, which is the opposite of what the 5-series wants. A 5-series pass is written only if something shows one is needed; the raw material is banked in [opus-5-instruction-compliance.md](research/opus-5-instruction-compliance.md) and [fable-5-instruction-compatibility.md](research/fable-5-instruction-compatibility.md).

The honest cost: SPEC's position is that the method *is* model-tuned prose, and there is now no written account of what the current models steer on. There has been no such account since the retirement anyway — this only stops the document pretending otherwise.

## Rules about writing rules

Model-agnostic guidance for authoring and sharpening the method's rules.

### The three checks — run these over any authored method text

Each names something to do, not something to avoid.

1. **Lead with the decision or ask; gate the detail.** Put the one thing the user must see or act on in the first line. Offer the reasoning behind a request rather than front-loading it.
   - Good: "Commit and push, or just commit?" then stop. — Bad: three paragraphs of rationale before the question.

2. **Show the shape; don't describe it.** Include a one-line positive exemplar of the output you want.
   - Good: a model line — "Three captures waiting; none touches the next batch — nothing blocks it." — Bad: "keep the verdict concise."

3. **Guard against over-terseness.** Concision comes from cutting bloat — meta-narration, restating what was shown, hedging — never from cramming or dropping plain-English explanation a non-coder needs. If a cut removes something the reader needs in order to act, it is the wrong cut.
   - Good: drop the "I'm now going to…" preamble, keep the plain-English what-and-why. — Bad: compress a non-coder explanation into jargon to save words.

Two of the three are also stated in `docs-b/plugin-behaviour.md`, which is itself the evidence that they are universal rather than tuned to any one model — they were promoted out of the deleted 4.8 pass for exactly that reason.

### When a slipped rule earns a hook vs. just sharper wording

The method enforces in two tiers (SPEC's two-tier principle): **hooks enforce what must never happen; hardened rules steer what should usually happen.** What that principle doesn't state is the *trigger* — what tips a should-usually rule into needing a must-never mechanism. This is it.

When a behavioural rule slips *despite already existing with its rationale* — so the slip isn't a missing why, the rule was there and complete — escalate to a mechanical backstop (a hook) only when the failure's cost justifies the hook's standing friction. Otherwise sharpen the wording and keep it behavioural. The deciding factor is the cost of the failure, not the fact of the slip: every hook adds friction every session forever, so a low-cost slip doesn't earn one.

Worked examples, both from the 2026-06-24/25 sessions:

- **Escalated — [subagent-ask-gate].** The "don't silently spawn a subagent" rule slipped at high cost: a single silent deep-research fan-out exhausted the user's Max usage for the first time in weeks. High, recurring, hard-to-undo cost → it earned a mechanical ask-gate hook (the Task tool prompts before any subagent runs) *on top of* the hardened wording. Belt and suspenders, because the failure mode is expensive enough to justify the friction.
- **Sharpened — [unpark-scan-mixed-trigger].** The unpark slug-check rule slipped at low cost: a mixed slug-plus-behavioural `Blocked by:` header skipped the mechanical slug check, so a parked item just sat parked until the user raised it by hand. Mild, self-correcting cost → procedure-sharpening only (an explicit clause in the unpark scan), no hook.

So: the same kind of failure (a complete rule slipped), opposite fixes, and the cost of the slip is what decides. A hook is the answer only when the cost of *not* having it outweighs the friction of always having it.

This doc is kept short enough to apply in one pass — it models its own advice.
