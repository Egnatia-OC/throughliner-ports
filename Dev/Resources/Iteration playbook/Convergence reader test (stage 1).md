# Convergence reader test (stage 1 — initial reconciliation)

*Experimental. First run pending.*

A diagnostic pass that builds the complete overlap map between the plugin-side method and the dev-side prose method — from scratch. The two sides were built up independently, with piecemeal patches applied through chat. They have never been systematically reconciled. This test produces the map that makes reconciliation possible.

The posture is not "find where they've drifted" (that's [[Convergence reader test (stage 2)]]) but "build the full inventory of what overlaps, what's one-side-only, what contradicts, and what's stale." The output is a reconciliation plan, not a patch list.

## How it differs from the stage 2 test

Stage 2 assumes alignment exists and looks for drift since the last check. Stage 1 assumes no prior alignment — it reads both sides cold and builds the map. Stage 2 is a maintenance pass you run after each batch. Stage 1 runs once (or until the map is clean enough to graduate to stage 2).

## The situation

The plugin-side method has been iterated through 131+ sessions of hook code, procedure docs, skill bodies, and canonical docs. The dev-side method was written earlier as prose conventions in `session-protocol.md`, `session-reference.md`, and project `CLAUDE.md`. Concepts have been shared in both directions — plugin patterns copied to the dev-side as prose, dev-side wisdom pushed to the plugin — but through ad-hoc chat edits, not a systematic pass.

The result: partial overlap with unknown gaps. Some rules exist on both sides but say different things. Some rules exist on one side only — some intentionally, some because the other side was never updated. Some rules have been superseded on one side but the old version persists on the other. The naming may not match. The level of detail may not match.

**Direction of reconciliation.** The plugin side is the reference — it's what ships, it's been more heavily iterated, and most dev-side wisdom has already been shared over. The dev-side will be rewritten to mirror the plugin as prose conventions (minus hooks, locks, skills, and consumer-only mechanics). Any dev-side-only rules that are genuinely worth preserving get flagged for review — they may need to flow to the plugin first, or they may be dev-specific and stay.

## The pairing surface

Same as stage 2:

| Dev-side | Plugin-side | What they share |
|---|---|---|
| `session-protocol.md` (routing, close, lifecycle) | `universal-behaviour.md` (routing, behaviours, prohibitions) | Routing table, session types, close procedure, editing surfaces, response-shape tags |
| `session-protocol.md` (close procedure) | `docs/procedures/close.md` | Close steps, two-turn structure, checkpoint lists |
| `session-reference.md` (entry shapes, terms) | `docs/DOC-STRUCTURE.md` | Entry formats, section ordering, proxy specs |
| `session-reference.md` (vocabulary usage) | `docs/VOCABULARY.md` | Term definitions, naming conventions |
| Project `CLAUDE.md` (collaboration rules) | `universal-behaviour.md` (required behaviours) | Pushback rules, flagging, research, routing to artifacts |

## Finding categories

Different from stage 2. These aren't ranked by severity — they're classified by what action they require.

**Overlap — aligned.** Both sides address the concept and agree. No action needed. Worth counting — it shows how much is already converged.

**Overlap — contradicts.** Both sides address the concept but say different things. Action: decide which version is correct (usually plugin-side), update the other.

**Overlap — stale.** Both sides address the concept but one is outdated (references old names, old step counts, old mechanisms). Action: update the stale side.

**Plugin-only (expected).** Plugin-side has it, dev-side doesn't, and the absence is structural (hooks, locks, skills, consumer-only). No action needed.

**Plugin-only (gap).** Plugin-side has it, dev-side doesn't, and the dev-side should have a prose equivalent. Action: add to dev-side.

**Dev-only (preserve).** Dev-side has it, plugin-side doesn't, and it's genuinely worth keeping — a rule or convention that applies to this project specifically, or wisdom that should flow to the plugin. Action: flag for review.

**Dev-only (stale).** Dev-side has it, plugin-side doesn't, and it looks like a leftover from before the plugin handled it. Action: remove from dev-side.

## What NOT to flag as gaps

Same structural exclusions as stage 2:
- The dev-side lacking hooks, skills, locks, or `_method/active-build.md`.
- Plugin-side features that are consumer-only by design (setup cases, `/sovsetup`, scaffold, adoption detection).
- Entry shapes or formats that the dev-side deliberately simplifies.

## Trigger

You're ready to reconcile the dev-side with the plugin-side. The plugin has stabilised enough that it's the reference, and the dev-side rules are known to be a patchwork of old prose and ad-hoc updates. Run once to produce the reconciliation map, then execute the reconciliation, then graduate to stage 2 for ongoing maintenance.

## Steps

1. **Spawn three sub-agents in parallel.** Each reads both sides of one pairing fresh — no prior context about the method's history.

2. **Synthesize.** Build a single reconciliation map organised by category (aligned, contradicts, stale, plugin-only expected, plugin-only gap, dev-only preserve, dev-only stale). Count each category.

3. **Confirm before acting.** Present the map. Wait for okay. The map is the input to reconciliation work — it doesn't prescribe a single session's worth of edits. It may need to be broken into batches.

## Output

A reconciliation map filed to `Dev/Resources/research/convergence-reconciliation-v<N>.md`. Organised by finding category, with counts. Each entry states: concept, where it lives on each side (file + section), what's wrong, and what the resolution would be.

The map doubles as a punch list — entries can be ticked off as they're resolved, across multiple sessions if needed.

## When wasted

- The dev-side has already been systematically reconciled to the plugin (graduate to stage 2).
- The plugin is about to absorb the dev-side entirely and `session-protocol.md` will be retired (just do the retirement).
- Neither side has changed since the last stage 1 run and no reconciliation work has been done (the map is still current).

## The prompt

Open a fresh session in the "No code method" project. Copy the prompt below. Replace `<PROCEDURE>` with the procedure doc to test (default: `close.md`). Paste and send.

---

Run a stage 1 convergence reader test between the dev-side prose method and the plugin-side method. The goal is NOT to find drift between aligned docs — it's to build the complete overlap map from scratch. The two sides were built up independently and have never been systematically reconciled. I need the full inventory before I can plan the reconciliation.

**Context the sub-agents need.** This project develops a Claude Code plugin. The plugin ships rules to consumer projects via hooks, procedure docs, and skills. The dev-side (this project's own sessions) has its own prose conventions in `session-protocol.md`, `session-reference.md`, and project `CLAUDE.md`. The two sides cover much of the same ground — routing, close procedures, entry shapes, terminology, collaboration rules — but they were built independently and patched piecemeal. Some rules match, some contradict, some exist on one side only, some are stale. Nobody has done a systematic comparison until now.

**Direction.** The plugin side is the reference — it's more heavily iterated and closer to correct. The dev-side will be rewritten to mirror the plugin (minus structural differences). But if you find dev-side rules that have no plugin equivalent and look genuinely useful, flag them — they may need to flow to the plugin.

**What NOT to flag as a gap.** The dev-side deliberately lacks hooks, skills, locks, `_method/active-build.md`, setup/scaffold/adoption mechanics, and PreToolUse enforcement. These are structural differences. Only flag when the dev-side has no prose equivalent at all for a rule the plugin enforces through these mechanisms.

**Step 1: spawn three sub-agents in parallel using the Agent tool.**

*Sub-agent A — Rule inventory.*
Read all three files fresh:
- `plugin/hooks/universal-behaviour.md`
- `Dev/session-protocol.md`
- `CLAUDE.md` (project root)

Build a rule-by-rule inventory. Walk through every rule, required behaviour, prohibited behaviour, and routing entry in `universal-behaviour.md`. For each one, search `session-protocol.md` and `CLAUDE.md` for the equivalent. Classify each pair:

- **Aligned** — both sides say the same thing. Note it briefly.
- **Contradicts** — both sides address it but disagree. Quote both versions.
- **Stale** — both sides address it but one uses old names, old step counts, or references removed mechanisms. State which side is stale and what's outdated.
- **Plugin-only (expected)** — plugin has it, dev-side doesn't, absence is structural. Note briefly.
- **Plugin-only (gap)** — plugin has it, dev-side doesn't, dev-side should have a prose equivalent. State what's missing.
- **Dev-only (preserve)** — dev-side has it, plugin doesn't, and it looks worth keeping. State why.
- **Dev-only (stale)** — dev-side has it, plugin doesn't, and it looks like a leftover. State why it's likely obsolete.

Then reverse: walk through `session-protocol.md` and `CLAUDE.md` for anything not yet covered.

End with category counts and the full classified list.

*Sub-agent B — Structure and terminology inventory.*
Read all four files fresh:
- `plugin/docs/DOC-STRUCTURE.md`
- `plugin/docs/VOCABULARY.md`
- `Dev/session-reference.md`
- `Dev/session-protocol.md` (for terminology usage)

Build two inventories:

Entry shapes: for each entry shape in `DOC-STRUCTURE.md` (batch entries, build-log entries, test-log entries, open questions, MANIFEST entries, proxy format), find the dev-side equivalent in `session-reference.md`. Compare field lists, required vs optional, format specs. Classify using the same categories as Sub-agent A.

Terminology: for each term in `VOCABULARY.md`, check whether `session-reference.md` and `session-protocol.md` use the same term with the same meaning. Flag terms used differently, terms missing from one side, and terms that appear to be the same concept under different names.

End with category counts and the full classified list.

*Sub-agent C — Workflow inventory.*
Read both files fresh:
- `plugin/docs/procedures/<PROCEDURE>`
- `Dev/session-protocol.md` (the matching section — close-procedure sections if testing `close.md`)

Trace both procedures step by step. Build a side-by-side comparison: each step on one side paired with its match (or absence) on the other. For each pair, classify:
- **Aligned** — same step, same action.
- **Contradicts** — same step, different action or output.
- **Stale** — same step, but one side references old names or removed mechanisms.
- **One-side-only** — step exists on one side with no match. State whether the absence looks structural or like a gap.

End with the side-by-side table and category counts.

**Step 2: synthesize.** Merge all three inventories into a single reconciliation map. Organise by category. Provide total counts:
- Aligned: N
- Contradicts: N
- Stale: N
- Plugin-only (expected): N
- Plugin-only (gap): N
- Dev-only (preserve): N
- Dev-only (stale): N

**Step 3: confirm before acting.** Present the map in plain English. This is a planning input, not a patch list — the reconciliation may need to be broken into multiple sessions. Wait for my okay.

---

## Notes

- The "aligned" count matters. If it's high, the reconciliation is mostly cleanup. If it's low, the two sides are further apart than expected and the rewrite scope is larger.
- Sub-agent A (rules) is the highest-value run. The rules surface is where contradictions cause the most damage — Claude following one version in a dev session and a different version in a consumer session.
- Sub-agent C's procedure pairing is the trickiest because `session-protocol.md` compresses all plugin procedures into one file. The sub-agent needs to be told which section maps to the procedure doc. Start with `close.md` — it has the most overlap and the most recent changes.
- The "dev-only (preserve)" category is small by expectation — most dev-side wisdom has already been shared to the plugin. But this is the category worth the most scrutiny, because anything genuinely worth preserving needs to flow to the plugin before the dev-side gets rewritten.
- The reconciliation map can be used as a punch list across multiple sessions. Each entry gets ticked off as it's resolved. When the list is clean, graduate to stage 2.
- The "stale" category deserves special attention. Staleness is the hardest to spot in normal sessions because both sides appear to address the concept — you only notice the problem when you compare the two versions side by side.
