# Rule-application sweep

*Single-instance. Sub-pass. Often nested inside [[Catch consolidation]], [[Spec-driven version cut]], or a downstream migration session.*

## Trigger

A targeted cleanup edit revealed a class of violation broader than the brief's explicit examples. The first edit under a rule exposed that the rule covers more cases than the prompt named. The sweep extends the rule across the rest of the doc — and ideally across every doc the rule applies to.

Signal that you're in sweep territory: "the brief said to clean up X, but X is one instance of a wider pattern, and the pattern isn't named in the brief."

## Steps

Usually the trigger step has to be asked for — Claude won't widen scope unprompted. The first refinement below addresses this.

Once triggered:

1. Re-read the doc end-to-end with the rule in mind.
2. Identify candidate sentences.
3. Classify each as: clear violation / borderline / fine. State reasoning briefly.
4. For each clear violation, propose a rewrite that preserves decided content and removes the gesture or marker.
5. Surface all candidates in one turn; ask for the call.
6. Make the approved edits.
7. Verify with grep that no old phrasing remains and all new phrasing is present.

## Output

A small set of concrete edits to a single doc (or several, if the sweep extends), plus an articulated detection rule capturing what the sweep was actually looking for. The detection rule is often the seed of a refinement to the spec doc — feed it into [[Rule and procedure extraction]] at session end.

## When wasted

- The doc was authored after the rule was tightened, so soft drift hasn't accumulated.
- The doc is small enough that the relevant check is implicit in a normal read.
- You're inside a *build* session. Source-of-truth docs are locked; the sweep is a planning-session activity.

## Refinements

- **Offer the sweep without being asked.** The moment a targeted cleanup finds something the brief didn't name, propose the wider sweep before applying the first edit. Don't wait for the user to notice.
- **Sweep all source-of-truth docs, not just the one the brief names.** A rule that applies to one source-of-truth doc usually applies to the others too.
- **Batch the edit confirmations.** With a clear shared rule and several clean rewrites, a single "here are all of them; approve?" turn is faster than one rewrite per turn.
- **Re-sweep when the method doc itself is edited mid-session.** A new rule landing mid-pass triggers an immediate sweep of every source-of-truth doc for violations — don't wait for the next session.
