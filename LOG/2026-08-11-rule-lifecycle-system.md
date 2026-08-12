# 7c9922a — The rule-lifecycle status board: five independent signals over the method's own rules, each filing a capture when it fires [rule-lifecycle-system]

The largest item in the run, and the one the previous /plan session designed in full after demoting it for having no build list. This close records what shipped and the two build-time questions it answered.

**What it replaces, and why "cycle" is gone.** The predecessor was the merge cycle — branch → blitz → soak → differential audit → reconcile → merge — which failed persistently; the user's recorded words were that it "is still a total mess that looks different every single time." Its fourth and worst failure was that compression sat permanently downstream of machinery that never ran. A positional cycle reproduces that by construction, so this is five independent mechanisms and a status board rather than a position. Constraint B is preserved rather than dropped: what a session reads at start is *which stages are signalling*, which a board cannot misremember.

**What shipped.**
- **MEASURED** — a structural rule-statement counter over the always-loaded corpus, calibrated against the 2026-08-09 hand count of ~218 against the 150–200 research ceiling. It reads 234 today.
- **AUDITED** — no new mechanism. `resources/method-compliance-audit-checklist.md` gained the trigger it never had: the same number MEASURED reads, computed independently so it is not gated on that stage finishing.
- **BORN** — `CLAUDE.md` gained a close-time `Rule gate:` disposition line, authored as an amendment to FAQ-sync's shape rather than a freestanding rule, with a detector matching LOG entries against commits touching the rule-bearing file set.
- **MAINTAINED** — a near-duplicate detector, plus the artifact half: §2 Eviction and the why-moving rule split out of the authoring gate into `resources/rule-maintenance.md`, which the duplicate signal names.
- **REPEALED** — `resources/retired-terms.md` as recorded source data, and a detector for live rules naming a retired term.
- **Shared** — capture-on-signal with a slug guard, riding the session-start surface.

**The two open questions answered at build time.** Placement: host-only by residence, in `resources/`, with the shipped hook silent when the file is absent — consumers never author method rules, and the two-doors pattern already exists for exactly this. Storage: the board is computed every run and nothing is stored, except the retired-terms list, which is source data — a recorded event authored once, not derived state that must be kept in sync.

**Why a firing signal files a capture rather than standing as a notice.** This is the answer to the question that killed every previous attempt: what stops the board becoming wallpaper. Escalating a signal over time needs a bare number, which the same run's [derivation-required-for-limits] bans. Showing only *new* signals recreates silent inaction, the precise failure Constraint D exists to prevent. So the board's job shrinks to one question per stage, and the work goes where all work goes — the queue, where ignoring it is visible. Nobody acts on a board; everyone already acts on the queue. Four captures were filed at this close by that mechanism.

**Two defects found by running it, both in the detector's precision rather than its design.** The retired-terms file's own format example was being parsed as a term, loading the literal word "term" and flagging half the corpus — the parser now reads only under the list heading. And a doc that *says* a term is retired was counting as a live reference, which would have fired on every doc doing the right thing; a retirement-context guard cut 96 hits to 44. Remaining false positives are accepted: the item specifies a flag for a human, never a gate.

**An uncomfortable result worth recording rather than burying.** The board's first real reading is that the corpus is over its ceiling, the audit is due, and no commit in recent history carries a gate disposition. The run that built the measure also pushed the number from 210 to 234. That is captured as [this-run-grew-what-it-measured] rather than left as an aside — the board working as designed on its first day means it is telling us something we would rather not hear.

## Filed in the post-commit tail

[spec-is-write-only-during-builds] — the user asked what SPEC is for if it is only
loaded at the close for spec-sync, and suggested the doc could go. Checked rather
than agreed: /plan *does* read SPEC every session, both as a ground rule and at
Step 1, so the premise is half wrong. The half that holds is real and had not been
named — /next never reads SPEC at all, so during a build the doc is write-only, and
this very run edited it four times without once consulting it. Claude recommended
against deletion (this project is atypical: the author holds the product truth that
a consumer and a fresh short session do not) and reframed the item onto the sharper
question, whether a close-time gate on a doc no build reads earns its cost.

## Session-level dispositions

Carried here rather than repeated across all 21 entries, because both obligations
are per session and this is the entry that introduced one of them.

```
Rule gate: run — this session authored and amended method rules across
skill-nonspecific-rules.md, plan.md, next.md, next-build.md, done.md,
done-plan.md, setup.md, CLAUDE.md and resources/self-authoring-rules.md. The
gate was applied per rule at authoring time. Its findings, recorded rather than
smoothed over: the great majority of what shipped were AMENDMENTS naming an
existing parent, which is why 21 items consumed few new slots — but the
always-loaded count still rose 210 → 234, and several additions wrote reasoning
into the operative rule where the gate says the why belongs in the LOG. That is
filed as [this-run-grew-what-it-measured] rather than left unsaid.
Retired: none this session. resources/retired-terms.md was CREATED and seeded
with 14 previously-retired mechanisms, which is not the same as retiring
something new.
FAQ: updated — two new entries, "Can I run two conversations on the same project
at once?" and "Claude flagged some queue items as contradicting themselves. What
does that mean?", plus both working-file entries rewritten for the session-scoped
names, in FAQ/faq.md and the shipped faq-template.md.
```

**Files touched:** `resources/rule_signals.py` (new), `resources/retired-terms.md` (new), `resources/rule-maintenance.md` (new), `resources/self-authoring-rules.md`, `resources/method-compliance-audit-checklist.md`, `CLAUDE.md`, `plugin/si-plugin/hooks/session_start.py`
**Routed to Captures:** [rule-corpus-over-ceiling], [three-lens-compliance-sweep-due], [rule-gate-dispositions-missing], [live-rules-name-retired-terms], [this-run-grew-what-it-measured]
