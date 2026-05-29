# Rule and procedure extraction

*Proven. End-of-session harvest of reusable rules and procedure shapes.*

The pass that built this playbook. Also the pass that maintains it — re-run after substantive sessions and update entries from what surfaces.

## Trigger

A substantive editing session has just concluded — especially a structured multi-step pass — and session events likely surfaced standing rules or procedure-shapes worth capturing. Triggered by *how the session went*, not by an external event.

Best run immediately after the main pass, before `/clear`. By next session, the rule-shapes are harder to extract — context fades.

## Steps

User prompts:

- "Is there anything covered in this chat that might work as a doc-development rule going forward?" (Rule extraction.)
- "Describe this whole thing as a procedure I could deliberately run again." (Procedure extraction.)

Two registers, asked separately on purpose. Bundling them collapses different kinds of output into one bucket.

Unprompted (within each prompt):

- Look back at the session for shapes or patterns that came up implicitly, especially anything that got corrected, surprised, or needed repeating.
- Distinguish individual rules (small judgement calls) from procedural shapes (named passes).
- Identify candidates with a concrete trigger ("when X happens, do Y").
- Rank by confidence. Explicitly reject weak candidates — anything already covered by existing instructions, anything that's an environment quirk rather than a doc rule.
- Recommend a home for each — project `CLAUDE.md`, method spec, memory, or this playbook.
- Mark whether each rule is a clarification of something implicit in the existing spec or a genuinely new addition.
- Separate rule candidates from leftover fixes when reporting back. Different registers; different asks.
- Hold the cap. 2–4 strong candidates plus rejections is the right depth. Expanding further starts manufacturing rules out of small judgement calls.

## Output

- A short, ranked list of candidate rules with confidence labels, recommended homes, and clarification-or-new flags.
- (If procedure extraction was also asked.) A named-procedure description with trigger, steps, output, when-wasted, refinements — the shape this playbook's entries follow.
- A list of explicit rejections with reasoning.

Verifiable by: do the rule candidates and procedure descriptions match the actual session if re-read? Did the strongest candidates get added to their recommended homes?

## When wasted

- The session was unstructured chitchat or a one-shot fact lookup. Nothing emergent to capture.
- The session was short enough that any rules in it are already obvious.
- The existing rule set already covers what came up.
- You're mid-iteration on another piece of work and the reflection is a distraction.

## Refinements

- **Offer the harvest unprompted at the end of any substantive pass.** Don't wait to be asked. The reflection is most accurate while session memory is fresh.
- **Ask where the rules should live before extracting.** Bin candidates by destination first (project `CLAUDE.md` vs upstream method vs general preferences vs this playbook). Binning first makes the candidates easier to action.
- **Separate rule candidates from leftover fixes** when reporting back. One needs a yes/no edit; the other needs discussion-then-edit. Don't bundle.
- **Hold the cap.** 2–4 strong candidates plus rejections. Manufacturing more rules from smaller judgement calls dilutes the playbook.
- **Mark clarifications vs. genuinely new.** Clarifications are easier to accept; genuinely new rules need more discussion.
- **For the procedure-extraction variant, the question is about the *shape of the work*, not the *content* of the work.** Skip individual rules and small judgement calls — those go through the rule-extraction prompt. Capture trigger, steps, output, when-wasted, refinements.
