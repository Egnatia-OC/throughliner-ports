# Convergence reader test (stage 2 — maintenance)

*Experimental. Not yet applicable — use [[Convergence reader test (stage 1)]] until initial reconciliation is complete.*

A diagnostic pass that finds semantic drift between the plugin-side method (what ships to consumer projects) and the dev-side prose mirror (what governs this project's own sessions). Assumes initial convergence has already been achieved — the two sides say the same things, and this test catches where they've drifted apart since. For the initial reconciliation (building the overlap map from scratch), see [[Convergence reader test (stage 1)]].

## How it differs from the plugin reader test

The [[Plugin reader test]] asks "can a stranger-Claude follow these instructions?" — it tests comprehension of one side in isolation. This test asks "do both sides agree?" — it tests alignment between two instruction sets that are supposed to mirror each other.

No mock project state needed. The comparison is doc-to-doc, not scenario-based.

## The pairing surface

Dev-side docs and their plugin-side counterparts:

| Dev-side | Plugin-side | What they share |
|---|---|---|
| `session-protocol.md` (routing, close, lifecycle) | `universal-behaviour.md` (routing, behaviours, prohibitions) | Routing table, session types, close procedure, editing surfaces, response-shape tags |
| `session-protocol.md` (close procedure) | `docs/procedures/close.md` | Close steps, two-turn structure, checkpoint lists |
| `session-reference.md` (entry shapes, terms) | `docs/DOC-STRUCTURE.md` | Entry formats, section ordering, proxy specs |
| `session-reference.md` (vocabulary usage) | `docs/VOCABULARY.md` | Term definitions, naming conventions |
| Project `CLAUDE.md` (collaboration rules) | `universal-behaviour.md` (required behaviours) | Pushback rules, flagging, research, routing to artifacts |

## What counts as a convergence issue

**Semantic drift** — same concept, different meaning or specification. Always a real gap. Example: dev-side close has 11 steps, plugin-side close has 8, and the missing 3 aren't explained by the "dev-side has no hooks" difference.

**Missing mirror** — rule or concept exists on one side with no equivalent on the other. May be intentional or accidental. Example: plugin-side has a `[PROPOSED EDIT PENDING]` mechanism; dev-side session-protocol.md says nothing about it (intentional — dev-side doesn't lock docs during builds). Versus: dev-side has a batch-input check at session open; plugin-side has no equivalent (accidental — should it?).

**Naming mismatch** — same concept, different name. Always worth fixing. Example: one side still says "BUILD-PLAN" where the other says "BACKLOG."

**Structural difference (expected)** — enforcement via hook on plugin-side, enforcement via prose convention on dev-side. Expected and not flagged *unless* the dev-side has no prose convention at all for a hook-enforced rule.

## What NOT to flag

- The dev-side lacking hooks, skills, locks, or `_method/active-build.md`. That's the structural difference between the two sides, not drift.
- Plugin-side features that are consumer-only by design (setup cases, `/sovsetup`, scaffold, adoption detection).
- Entry shapes or formats that the dev-side deliberately simplifies (e.g. dev-side BUILD-LOG is lighter than plugin-side build-log template).

## Trigger

After a batch that changes rules, routing, close procedure, entry shapes, or terminology on either side — once both sides have been through the stage 1 reconciliation and are known-aligned. Also useful after a cluster of changes (like v129's BACKLOG rename) where accumulated drift is likely but invisible.

Not triggered by code-only changes (hook logic, script changes) unless they alter the instruction text Claude reads.

## Steps

1. **Spawn three sub-agents in parallel.** Each reads both sides of one pairing fresh — no prior context about the method's convergence strategy.

2. **Synthesize.** Cluster findings into a single deduplicated list, ranked:
   - **Semantic drift** — both sides address the concept but say different things.
   - **Missing mirror** — one side has it, the other doesn't, and the absence isn't explained by the structural difference.
   - **Naming mismatch** — same concept, different label.

3. **Confirm before acting.** Present the ranked list. Wait for okay. Don't start editing.

## Output

A ranked convergence-issue list. Each entry states: which concept, which side is ahead (or whether they contradict), and which file(s) would need to change to resolve it. Filed to `Dev/Resources/research/convergence-test-v<N>.md`.

## When wasted

- Neither side's instruction text has changed since the last run.
- You're about to rewrite one side anyway — test after, not before.
- Initial reconciliation hasn't happened yet — run [[Convergence reader test (stage 1)]] first.
- The convergence strategy has been retired (the plugin has absorbed the dev-side rules and session-protocol.md no longer exists).

## Refinements

- **Rotate Sub-agent C's procedure doc** across runs. `close.md` first (richest overlap with session-protocol.md), then `planning.md`, then `build.md`.
- **Run in a separate session from fixes.** Same rationale as the other reader tests — distance between finding and fixing reduces over-correction.
- **Sub-agent B (structural alignment) is probably lowest-yield.** Entry shapes change rarely. If time is tight, run A and C only.
- **Directionality matters for "missing mirror."** A dev-side rule missing from the plugin is a potential plugin gap (should it ship?). A plugin-side rule missing from the dev-side is a potential dev-side gap (should it be mirrored as prose?). The sub-agents should state direction, not just "missing."

## The prompt

Open a fresh session in the "No code method" project. Copy the prompt below. Replace `<PROCEDURE>` with the procedure doc to test (default: `close.md` — richest overlap with session-protocol.md). Paste and send.

---

Run a convergence reader test between the dev-side prose method and the plugin-side method. The goal is to find semantic drift — places where the two sides address the same concept but say different things, or where one side has a rule the other side should mirror but doesn't. Don't edit anything — find the issues, present them, get my okay.

**Context the sub-agents need.** This project develops a Claude Code plugin. The plugin ships rules to consumer projects via hooks, procedure docs, and skills. The dev-side (this project's own sessions) mirrors those rules as prose conventions — no hooks, no locks, no skills. The two sides are supposed to say the same things about routing, close procedures, entry shapes, terminology, and collaboration rules. They sometimes drift apart after one side gets updated and the other doesn't. Your job is to find where they've drifted.

**What NOT to flag.** The dev-side deliberately lacks hooks, skills, locks, `_method/active-build.md`, setup/scaffold/adoption mechanics, and PreToolUse enforcement. These are structural differences, not drift. Only flag a structural difference when the dev-side has no prose equivalent at all for a rule the plugin enforces.

**Step 1: spawn three sub-agents in parallel using the Agent tool.**

*Sub-agent A — Rule alignment.*
Read both files fresh:
- `plugin/hooks/universal-behaviour.md` (plugin-side rules, routing, prohibitions, editing surfaces)
- `Dev/session-protocol.md` (dev-side lifecycle, routing, close procedure, parity rules)
Also read `CLAUDE.md` (project root — the "Design constraints," "Dev-side convergence strategy," and collaboration-rule sections).

Walk through `universal-behaviour.md` section by section. For each rule, required behaviour, prohibited behaviour, and routing entry: find the dev-side equivalent in `session-protocol.md` or `CLAUDE.md`. Compare them. Flag:
- Rules present on one side only (state which side, and whether the absence looks intentional or accidental).
- Rules present on both sides but with different specifications (quote both, note the discrepancy).
- Naming mismatches (same concept, different label).
- Routing table entries that don't match.

Then reverse: walk through `session-protocol.md` section by section and find anything the plugin-side doesn't cover.

End with a list of findings, each tagged [semantic drift], [missing mirror — plugin ahead], [missing mirror — dev ahead], or [naming mismatch].

*Sub-agent B — Structural alignment.*
Read both files fresh:
- `plugin/docs/DOC-STRUCTURE.md` (plugin-side entry shapes, section ordering, proxy format)
- `Dev/session-reference.md` (dev-side entry shapes, footer bumps, planning artefact lifecycles)
Also read `plugin/docs/VOCABULARY.md`.

For each entry shape in `DOC-STRUCTURE.md` (batch entries, build-log entries, test-log entries, open questions, MANIFEST entries, proxy format), find the dev-side equivalent in `session-reference.md`. Compare field lists, required vs optional fields, format specs. Flag discrepancies.

For each term in `VOCABULARY.md`, check whether `session-reference.md` or `session-protocol.md` uses the same term with the same meaning. Flag terms used differently or not at all on the dev-side.

End with a list of findings, each tagged as above.

*Sub-agent C — Workflow alignment.*
Read both files fresh:
- `plugin/docs/procedures/<PROCEDURE>` (plugin-side workflow)
- `Dev/session-protocol.md` (dev-side equivalent, specifically the close-procedure sections if testing `close.md`)

Trace both procedures step by step from invocation to completion. For each step on one side, find the matching step on the other. Flag:
- Steps present on one side only.
- Steps present on both but with different actions, ordering, or outputs.
- Cross-references that point to different locations.
- Checkpoint lists that don't match.

End with a side-by-side step comparison and a list of discrepancies.

**Step 2: synthesize.** Cluster findings from all three sub-agents into a single deduplicated list, ranked:
- **Semantic drift** — both sides address the concept but disagree.
- **Missing mirror** — one side has it, the other doesn't, and the absence isn't structural.
- **Naming mismatch** — same concept, different label.

For each finding, state: which concept, which side is ahead (or whether they contradict), and which file(s) would need to change.

**Step 3: confirm before editing.** Present the ranked list in plain English. Wait for my okay.

---

## Notes

- The "walk both directions" instruction for Sub-agent A is load-bearing. If it only walks plugin → dev, it misses dev-side rules that should flow to the plugin. Bidirectional sweep catches both directions of drift.
- Sub-agent C's procedure pairing is the trickiest because the dev-side compresses multiple plugin procedures into one file (`session-protocol.md`). The sub-agent needs to be told which section of session-protocol.md maps to the procedure doc it's reading.
- Unlike the plugin reader test, no mock project state is needed — this is a doc-to-doc comparison, not a scenario simulation.
- The "what not to flag" section is critical. Without it, sub-agents will produce dozens of findings about the dev-side lacking hooks, which is expected and not useful.
- First run should use `close.md` for Sub-agent C — the close procedure is the area with the most overlap and the most recent changes on both sides (v128 two-turn restructure on plugin-side, mirrored to dev-side in session-protocol.md).
