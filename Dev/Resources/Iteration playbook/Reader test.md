# Reader test

*Proven. Existing tool — the only entry in this playbook that includes a saved paste-ready prompt.*

A diagnostic pass that produces understanding, not edits. Uses parallel sub-agents to read a candidate version of the method *as a stranger would*, then ranks gaps before you commit to the version.

## Trigger

You're about to deploy a version of the method to a fresh context — a new Claude Code project, a new Cowork pre-pass on existing docs, anywhere a stranger-Claude will read it. The deployment is what surfaces latent gaps, so the audit goes immediately before it. Not routine maintenance; not failure-driven. The trigger is an upcoming use.

## Steps

1. Spawn three sub-agents in parallel reading the four V N files fresh, each treating them as a stranger would — no prior context.
2. Each sub-agent runs a different scenario (comprehension Q&A, new-project role-play, mid-project curveball role-play).
3. Cluster findings into a single deduplicated, ranked, tiered gap list (Top / Middle / Bottom).
4. Present the gap list and hold for confirmation. Do **not** start editing on the list alone — the decision gate between the audit and any revision is load-bearing.
5. *(Optional, see refinements.)* Save the gap list as a file in the version folder so it survives `/clear`.

If you confirm and want fixes applied, that's a different pass — [[Spec-driven version cut]] or [[Catch consolidation]], driven by the gap list.

## Output

A ranked gap list with three tiers (Top / Middle / Bottom). Top-tier gaps are weighted toward whatever your immediate next use of the method is.

## When wasted

- The docs haven't changed and the context hasn't changed since the last audit. Same input, same output.
- You don't have a near-term deployment to weight findings against — without that, you can't tell top-tier from middle-tier.
- You haven't accumulated either new method edits or new real-session observations since the last audit.

## Refinements

- **Save the gap list as a file** (e.g. `Version N — audit findings.md` in the version folder), not just in chat. If you `/clear` after the audit, the ranked list is currently lost.
- The three default scenarios (comprehension Q&A, new-project role-play, mid-project curveball) were a first-pass guess. The comprehension Q&A surfaced the most gaps; the new-project role-play surfaced the fewest. Future audits can weight scenarios accordingly or rotate fresh ones in.
- Run the audit in a *separate session* from the edits. Sleeping on the gap list before committing to fixes reduces the pressure to over-fix in the moment.

## The prompt

Open a fresh Cowork session in the "No code method" project. Copy the prompt below. Replace every `N` with the version number you want tested. Paste and send.

---

Run a reader test on Version N of the no-code method, located at `C:\Users\Alex\Desktop\Taskflow Planning\No code method\Version N`. The goal is to find document-level gaps in NO-CODE-METHOD.md and the three templates before I commit to this version. Don't edit anything yet — find the gaps, present them, get my okay, then draft.

**Step 1: spawn three sub-agents in parallel using the Agent tool.** Each one reads the four V N files fresh (NO-CODE-METHOD.md, UX-TEMPLATE.md, BACKLOG-TEMPLATE.md, MANIFEST-TEMPLATE.md) and treats them as a stranger would — no prior context.

*Sub-agent A — Comprehension Q&A.* Give it 10–14 direct questions covering at least these categories:

- Session-start routing (test notes / new project / existing non-conforming docs / feature request / other)
- Permissions (rename, refactor, mid-build scope changes, editing UX.md during a build)
- Where things go (each kind of flag, Discoveries lifecycle, completed-batch removal)
- Document scope boundaries (UX.md inclusion criteria, Suggestions vs Discoveries, bugs vs new-feature ideas in test notes)
- Tag interactions ([PROMPT] inside [SEQUENCE], [BRIEF] vs [DISCUSS])
- User disagreement (what to do when I push back on a Claude suggestion)

Instruct it to say "the document does not say" rather than invent a plausible answer, cite the section for each answer, and end with a list of ambiguities or contradictions.

*Sub-agent B — New-project role-play.* Tell it to act as Claude Code in a fresh project where the four files are loaded as the working state (templates still in template form). Give it an opening user message simulating a new-project kickoff — one or two sentences of project description, e.g. "New project — [name]. It's a [platform] app for [purpose]." Have it produce the actual response Claude Code would send. Then reflect on which method instructions it actively followed, which were unclear, and which moments it had to guess.

*Sub-agent C — Mid-project curveball role-play.* Tell it to act as Claude Code several builds into a project with a populated UX.md, BACKLOG.md, and MANIFEST.md. Give it a user message designed to stress-test the method — ideally a feature request that conflicts with established UX principles AND has obvious privacy or security implications (third-party sync, analytics, biometric login, etc.). Have it produce the actual response and reflect as above.

**Step 2: synthesize.** Cluster the three reports' findings into a single deduplicated gap list, ranked by impact:

- **Top tier:** gaps that would bite a real session in the near term, especially anything blocking my immediate next use of the method.
- **Middle tier:** real gaps that aren't urgent.
- **Bottom tier:** small precision issues, wording polish.

**Step 3: confirm before editing.** Per the project's CLAUDE.md, present the ranked gap list to me in plain English. Wait for my okay before creating Version N+1. If I confirm, copy the current version's files into a new Version N+1 folder verbatim and edit only there.

If I'm only spot-checking and don't intend to make a new version, stop after Step 2.

---

## Notes

- The question categories above are the ones that proved fruitful in the V6 → V7 reader test. Add more categories as new method areas develop and you want to probe them.
- The "stranger would" framing matters — it stops the test agents from filling in plausible-sounding answers from background knowledge of how Claude usually behaves.
- Top-tier gaps tied to your *immediate next use* are worth fixing before you commit. Lower-tier gaps can be deferred to the next reader test.
