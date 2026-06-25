# Authoring and sharpening rules in this project

This is the project's guide to writing the method's own rules well — the procedure docs, the behaviour rules, the hooks, the SPEC text. It has two parts:

- **Rules about writing rules** — model-agnostic guidance that holds whatever model the project targets: when a slipped rule earns a mechanical backstop versus sharper wording, and the like.
- **A per-model authoring pass** — the concrete checklist for the model the project currently targets. Each model steers on different things, so each gets its own section as it's adopted. The current target is Opus 4.8 (see CLAUDE.md Model target).

Run the relevant parts before authored method text ships. The current-model section is the per-text checklist; the rule-writing section is the judgment you reach for when a rule has slipped or a new rule needs a mechanism.

## Rules about writing rules

Model-agnostic guidance for authoring and sharpening the method's rules.

### When a slipped rule earns a hook vs. just sharper wording

The method enforces in two tiers (SPEC's two-tier principle): **hooks enforce what must never happen; hardened rules steer what should usually happen.** What that principle doesn't state is the *trigger* — what tips a should-usually rule into needing a must-never mechanism. This is it.

When a behavioural rule slips *despite already existing with its rationale* — so the slip isn't a missing why, the rule was there and complete — escalate to a mechanical backstop (a hook) only when the failure's cost justifies the hook's standing friction. Otherwise sharpen the wording and keep it behavioural. The deciding factor is the cost of the failure, not the fact of the slip: every hook adds friction every session forever, so a low-cost slip doesn't earn one.

Worked examples, both from the 2026-06-24/25 sessions:

- **Escalated — [subagent-ask-gate].** The "don't silently spawn a subagent" rule slipped at high cost: a single silent deep-research fan-out exhausted the user's Max usage for the first time in weeks. High, recurring, hard-to-undo cost → it earned a mechanical ask-gate hook (the Task tool prompts before any subagent runs) *on top of* the hardened wording. Belt and suspenders, because the failure mode is expensive enough to justify the friction.
- **Sharpened — [unpark-scan-mixed-trigger].** The unpark slug-check rule slipped at low cost: a mixed slug-plus-behavioural `Blocked by:` header skipped the mechanical slug check, so a parked item just sat parked until the user raised it by hand. Mild, self-correcting cost → procedure-sharpening only (an explicit clause in the unpark scan), no hook.

So: the same kind of failure (a complete rule slipped), opposite fixes, and the cost of the slip is what decides. A hook is the answer only when the cost of *not* having it outweighs the friction of always having it.

## 4.8 — the authoring pass

**What.** A short checklist for any doc, procedure, or SPEC text authored in this project. Run it over the text before that text ships.

**Why.** Every session here runs on Opus 4.8. 4.8 steers on positive, quantified, exemplified, explicitly-scoped instruction — and steers least on abstract adjectives and "don't" rules. Authoring against what it actually responds to is how the plugin's own method text lands.

**Aim.** Anti-overwhelm structure and plain English — never arbitrary terseness (see the last check).

**Sources.** Distilled from [opus-4-8-verbosity-steering.md](research/opus-4-8-verbosity-steering.md) and [model-instruction-compliance.md](research/model-instruction-compliance.md).

Run each check. Each names something to do, not something to avoid.

1. **Quantify the target; don't adjective it.** Give a number the model can hit instead of an adjective it has to interpret.
   - Good: "Answer in ≤2 sentences, then stop." — Bad: "Be brief."

2. **Show the shape; don't describe it.** Include a one-line positive exemplar of the output you want. This is the single strongest lever in the research.
   - Good: a model line — "Three captures waiting; none touches the next batch — nothing blocks it." — Bad: "keep the verdict concise."

3. **Lead with the decision or ask; gate the detail.** Put the one thing the user must see or act on in the first line. Offer the reasoning behind a request rather than front-loading it.
   - Good: "Commit and push, or just commit?" then stop. — Bad: three paragraphs of rationale before the question.

4. **State the scope in words.** 4.8 is literal and won't carry an instruction from one context to another, so name where the rule applies.
   - Good: "every message in every skill, including close-outs and walkthroughs, with no exception for short steps." — Bad: leaving scope implied.

5. **Name the verbosity pattern to kill, with its positive replacement.** A concrete offender plus what to do instead beats a general "don't ramble."
   - Good: "don't restate what you just showed — point to it." — Bad: "avoid redundancy."

6. **Write it as an action, not a prohibition.** Tell the model what to do; a rule framed as a positive action steers, a bare "don't" mostly doesn't.
   - Good: "say it in one line, then wait." — Bad: "don't write more than one line."

7. **Guard against over-terseness.** Concision comes from cutting bloat — meta-narration, restating what was shown, hedging — never from cramming or dropping plain-English explanation a non-coder needs. If a cut removes something the reader needs in order to act, it is the wrong cut.
   - Good: drop the "I'm now going to…" preamble, keep the plain-English what-and-why. — Bad: compress a non-coder explanation into jargon to save words.

This list is kept short enough to apply in one pass — it models its own advice.
