# Downstream calibration

*Single-instance. Read a mature downstream project's artefacts to find where the method is thin.*

## Trigger

Not a specific event and not routine maintenance. A *state*: at least one downstream project has been using the method long enough to have accumulated real, project-specific artefacts (not template-stage drafts), and to have grown one or more deviations from the standard templates. Without that, there's nothing to read.

Worth running when you have a sense the method might be quietly off-spec in production but you can't yet say where. The gap between what the method describes and what the project actually does becomes available as evidence about where the method is thin, vague, or silently wrong.

The strongest single signal that this pass would be wasted: if you can already name what's wrong with the method without looking at the downstream artefact, you don't need this pass — you need a targeted edit.

Distinguished from [[Catch consolidation]] by direction of data flow: Catch consolidation starts from already-named catches. Downstream calibration *produces* catches by reading.

## Steps

Unprompted:

- Read the current method state before looking at the downstream artefact. Necessary to distinguish "the method didn't cover this" from "the method covered this but the project didn't follow it."
- Read every file in the downstream artefact. Don't infer from the user's description; look at the actual files.
- Sort observations into method-shaped (would help any project) vs. project-shaped (only relevant to this one). Report only the first kind. *The patient is the method, not the project.*
- Report a headline summary plus a numbered list of method-shaped gaps. Each names what was observed in the artefact, what the current method says, and a sketch of the fix shape. No edits yet.
- After approval, disclose any interpretive calls (places where the approved list still has implementation ambiguity) before editing.
- Make the method update in a new version folder, including any required template-drift fixes spotted while editing.
- Flag minor scope-creep fixes after making them, rather than burying them.

User prompts (these should be baked in, not prompted — see refinements):

- The initial "go look."
- Approval to act on the gap list.
- Producing the downstream migration artefacts (updated project instructions + session-opening prompt).
- Harvesting any second-order catches that surface during the downstream migration.

## Output

- A new method version folder with the gap-driven edits.
- Updated project instructions and a session-opening prompt for the downstream project's migration to the new method version.
- A V(next) catches list of second-order gaps that surfaced during the downstream migration. Feed into the next [[Catch consolidation]] or [[Reorg priming]] pass.

Verifiable: the new method version exists, the project-instruction text matches what's pasted into the downstream's setup, and the V(next) catches name specific sections by sub-heading.

## When wasted

- No downstream project has matured enough yet. The artefact is still template-shaped, with placeholders and no project-specific deviations.
- The method was changed very recently and the downstream project hasn't migrated yet. Calibrating against a project that's still on an old version measures the wrong thing.
- The method was changed very recently *and* the downstream project has migrated, but hasn't had time to use the new version under real conditions. The downstream artefact looks compliant because nothing has stress-tested it yet.
- You want a single targeted change to the method, not a broad calibration. Then it's an editorial pass, not this.
- You're running it too often. Any one downstream project generates a finite amount of novel evidence per unit time; calibrating every session drops signal-to-noise.

## Refinements

- **Explicit template drift check at the start of method-editing.** Catch template drift as a deliberate step, not as something noticed incidentally.
- **Walk specific structural lines in the downstream artefact, not just high-level shapes.** Line-level reading of structured fields (`Serves`, `Blocks`, etc.) catches gaps that high-level reading misses.
- **Apply spirit-not-letter explicitly during the artefact read, not after.** Don't see a `[Open: ...]` marker and treat it as a single cleanup; ask "is there a class of soft placeholders the method should also forbid?" Same observation, examined with a spirit-check lens, produces a tighter rule directly.
- **Smaller per-step delivery for the downstream migration artefacts.** Don't dump two large code blocks in one response. Smaller per-step delivery is easier for the user to verify and harder to lose track of.
- **Bake the second-order catch-harvesting into the procedure.** Don't wait to be prompted. After handing off to downstream migration, watch the migration session, and capture anything that surfaces during it as V(next) candidates.
