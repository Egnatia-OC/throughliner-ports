# b485ee3 — Planning writes the SPEC sentence ahead of the build; a build that finds one missing files it

Raised by the user when a run stopped in its second minute to ask for one SPEC sentence.

**Her principle is the whole of this, and Claude missed it twice before she stated it.** SPEC is managed across a session boundary so that no one instance of Claude is both the party that made a choice and the party that certifies it in product truth. Claude proposed deferring the write to that same run's close; she refused it on exactly that ground — the close is the same session, so it moves the self-certification later rather than crossing anything. That refusal is now written into `next-build.md` and `done-build.md` as operative text, because a build reaching this branch will otherwise reinvent it.

The point was already settled one layer over: `CLAUDE.md` says a disposition written as an item is built "improves attribution and restores no power to refuse," and that only /plan can refuse. That failure has a recorded instance here — a build in an eighteen-item run wrote its own gate disposition rather than halting.

What changes, in three steps. The keep-step asks whether an item changes what SPEC says, and **planning writes the sentence then**, with the user present. The build then builds against it and never touches SPEC. Only where planning missed one does the build record the sentence, file it as work, and leave SPEC alone. So SPEC leads the build rather than trailing it, which is what "read at build time" requires. The cost, stated: on a miss, SPEC lags that sentence by one planning session — as a visible queue item rather than in silence, and the keep-step question is what makes the miss rare.

**Folded in from [batch-spec-writes-at-the-end-of-a-run], deleted at processing:** deferring SPEC writes inside a run was tried live on the user's instruction — four sentences held in the working file, written in one pass, nothing lost and the run never stopped again. That is the evidence the file-it fallback is safe. The rest of that item dissolved, because under this model a run owes no SPEC sentences at all.

The mid-build ask that this replaces was itself a fix for something real, and its failure is worth keeping: read cold, an unexpected request to edit product truth mid-build looks like a run asking permission to break a rule rather than a run following one — the method's own author read it that way. The file-it path removes the moment entirely rather than rewording it.

**The SPEC-contradiction halt is untouched and must not be softened** — built work conflicting with SPEC still stops the run and names the sentence. That is a different thing from a sentence SPEC does not yet carry, and `done-build.md` now says so.

**Files touched:** `plugin/throughliner/docs-b/plan.md`, `next-build.md`, `done-build.md`, `CLAUDE.md`, `plugin/throughliner/templates/CLAUDE-TEMPLATE.md`, `faq-template.md` and `faq-index-template.md` with their `FAQ/` copies. SPEC.md is **not** listed — its sentence was rewritten in the planning session that kept this, which is the rule applied to itself.

**Routed to Captures:** none.

Rule gate: run — admitted as a clause on plan.md's existing two-limb keep check, not a freestanding rule, so no always-loaded slot is spent. **The eviction is the build-asks route, repealed outright across seven live files.** Failure evidence is one recorded instance, which is thin for a new rule and is what the amendment-plus-eviction shape carries; the same defect is independently recorded for dispositions as the fifth instance in [standing-audit-programme].

Tick: done, confirmed by grepping the add-SPEC-to-Files route across the package afterwards; the only surviving mention is the sentence that repeals it.
