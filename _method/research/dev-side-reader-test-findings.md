# Dev-side reader test findings — v120

Reader test run against four dev-side docs at v119 HEAD: CLAUDE.md, session-protocol.md, session-reference.md, BACKLOG.md. Three scenarios: comprehension Q&A (14 questions), fresh dev session role-play ("Spare session. Start the next build session."), curveball multi-thread opener (E2E findings + structural proposal + doc contradiction report).

Weighted toward: "what would bite the next dev session."

---

## Top tier

Gaps that would bite a real dev session in the near term.

### T1 — Mixed/blended opener routing unaddressed

**Source docs:** session-protocol.md → Opener routing table.
**Found by:** All three agents.

The routing table says "pick the highest-priority match" but defines no priority ordering across the six session types. Real openers frequently blend types (e.g. test observations + planning proposal + doc question). The table assumes one type per opener. No rule for: which type takes precedence, whether threads are handled sequentially, or how to sequence disambiguation requests within a multi-thread opener.

The curveball agent had to improvise entirely — falling back to CLAUDE.md's E2E-observation rule as a tiebreaker because the table gave nothing.

### T2 — Batch removal timing asymmetry between close paths

**Source docs:** session-protocol.md → Implementation close step 10 vs. Lighter close step 5.
**Found by:** Comprehension Q&A agent.

Implementation close removes the consumed batch at step 10 — *after* commit and tag (steps 8–9). Lighter close handles batch removal inside the pre-commit checkpoint at step 5 — *before* commit. This means the batch is removed pre-commit in one path and post-commit in the other, with no stated reason.

### T3 — Stale step-number cross-reference

**Source docs:** session-reference.md → Planning artefacts vs. session-protocol.md → Implementation close.
**Found by:** Comprehension Q&A agent.

session-reference.md says queued batch entry is "removed (step 9)." session-protocol.md numbers this step 10. Appears to be a leftover from a previous version of the close procedure. Small but directly contradictory.

### T4 — Proxy format spec unlocated

**Source docs:** session-protocol.md → Implementation close step 6.
**Found by:** Comprehension Q&A agent.

Close step says "write the proxy per its format spec" but doesn't say where the format spec lives. The dev-side proxies don't follow the plugin-side proxy format (DOC-STRUCTURE.md → Proxy files) — they're a simpler line-number index. A dev-session Claude hitting this step would have to guess the format or read existing proxies and infer.

### T5 — Git-unavailable fallback undocumented

**Source docs:** session-protocol.md → Session open step 1.
**Found by:** Fresh-session agent.

Step 1 says "run `git describe --tags --abbrev=0`" with no fallback. The fresh-session agent fell back to CLAUDE.md's *Current state* section — a reasonable inference, but undocumented. Every session where the git command fails (tool unavailability, not-a-repo edge case) has no stated recovery.

---

## Middle tier

Real gaps that aren't urgent.

### M1 — Lighter close step reordering unexplained

**Source docs:** session-protocol.md → both close paths.
**Found by:** Comprehension Q&A agent.

Implementation close: parity → frame-sweep → footers → build-log → idea sweep → proxies → checkpoint. Lighter close: idea sweep → build-log → footers → proxies → checkpoint. No rationale for the reordering. A reader trying to understand the lighter close by analogy to the full close will be confused.

### M2 — Frame-correction sweep skip is categorical in lighter close

**Source docs:** session-protocol.md → Lighter close "Skipped explicitly."
**Found by:** Comprehension Q&A agent.

States "no feature frame changed" as the reason for skipping. But a doc-only session consuming a queued batch could change a load-bearing frame (e.g. rewriting how a concept works in BACKLOG scope text). The skip should be conditional on whether a frame actually changed, not categorical by session type.

### M3 — Doc-only batch-input check skip is conditional and underspecified

**Source docs:** session-protocol.md → Opener routing table, doc-only row.
**Found by:** Comprehension Q&A agent.

The table says doc-only sessions skip "Batch-input check (step 4) if no queued batch is being consumed." The positive case (doc-only session that *does* consume a batch) is left implicit. A reader might interpret the cell as "always skip for doc-only."

### M4 — Remote-control standby close path entirely unspecified

**Source docs:** session-protocol.md → Opener routing table.
**Found by:** Comprehension Q&A agent.

Close path is "Depends on work done." No guidance on how to classify work done in a standby session, or whether a commit/tag/push is expected if no work was done.

### M5 — Informal opener modifiers not addressed

**Source docs:** session-protocol.md → Opener routing table.
**Found by:** Fresh-session agent.

"Spare session," "quick one," "I have 10 minutes" — none mapped. The table is exhaustive for named session types but silent on informal modifiers. The fresh-session agent resolved "spare" by treating it as availability context, but flagged this was a judgment call.

### M6 — Dev-side session-open state summary has no template

**Source docs:** session-protocol.md → Session open; CLAUDE.md.
**Found by:** Fresh-session agent.

Plugin-side has the SessionStart hook mandating a specific status summary format (batch counts, next batch, pending tests). Dev-side has no equivalent. session-protocol.md says "report what was loaded and ask" if the task isn't clear, but gives no format for the session-open summary when the task *is* clear.

### M7 — Sub-agent warning rule boundary unclear for scoped work

**Source docs:** CLAUDE.md → Subagent usage.
**Found by:** Fresh-session agent.

The rule says "warn before spawning a subagent for a single simple operation." When the batch scope explicitly designs for three sub-agents, it's unclear whether the warning still applies. The fresh-session agent flagged it anyway as a courtesy — reasonable but the docs don't draw the line.

### M8 — Step 2 doesn't say what to look for in each plugin doc

**Source docs:** session-protocol.md → Session open step 2.
**Found by:** Curveball agent.

Tells you to read four plugin docs but not what information you're extracting or how large they are. A fresh reader doesn't know whether "read at HEAD" means a 10-line file or a 200-line file. The batching cost is invisible.

### M9 — Dev-side/plugin-side disambiguation hard to apply to user speech

**Source docs:** CLAUDE.md → Dev-side vs plugin-side.
**Found by:** Curveball agent.

The mandatory prefix rule works for Claude's own writing. When the user says "the close procedure is too long," both layers have a close procedure. The rule says "stop and clarify" — but in a multi-thread opener with the one-item-at-a-time rule, when does the disambiguation happen? No guidance on sequencing disambiguation within blended openers.

---

## Bottom tier

Small precision issues, wording polish.

### B1 — Duplicate 0102 entry in BACKLOG shipped batch table

**Source docs:** BACKLOG.md → The batch list.
**Found by:** Comprehension Q&A agent.

Two rows with batch number 0102. First occurrence has no shipped tag; second says "Shipped v99."

### B2 — Step 4 explanation relies entirely on a forward pointer

**Source docs:** session-protocol.md → Session open step 4.
**Found by:** Curveball agent.

"per session-reference.md → Drafts in flight" is the only explanation of what a batch input check actually does. No inline description of the check's purpose or mechanics.

### B3 — Build-log entry shape references DOC-STRUCTURE.md without path

**Source docs:** session-reference.md → BUILD-LOG entry shape.
**Found by:** Curveball agent.

"See DOC-STRUCTURE.md" without specifying the path. Assumes the reader has been through step 2 of session open, but that dependency isn't stated.

### B4 — Proxy instruction ordering inconsistency

**Source docs:** CLAUDE.md vs. session-protocol.md → Session open step 3.
**Found by:** Fresh-session agent.

CLAUDE.md says "read proxy files before session-reference.md." session-protocol.md step 3 says "read Dev/Planning/BACKLOG.md in full" without mentioning proxies. For BACKLOG specifically, the "in full" instruction overrides the proxy question — but the relationship between the two instructions isn't explicit.

### B5 — Checkpoint cross-referencing between close paths uses different step numbers

**Source docs:** session-protocol.md → both close paths.
**Found by:** Comprehension Q&A agent.

Each checkpoint references its own path's step numbers. Internally consistent but confusing to cross-reference between paths.

### B6 — "Lighter close" naming vs. doc-only batches that consume queued batches

**Source docs:** session-protocol.md → Lighter close.
**Found by:** Curveball agent, Comprehension Q&A agent.

"Run when the session didn't ship code." But a doc-only batch that consumes a queued batch may need more than "lighter." The conditional note about batch removal reads as an afterthought rather than a clean rule. The distinction is really "consumed a queued batch with code changes" vs. everything else.

---

## Side observation (not a doc gap)

CLAUDE.md *Current state* says v113 / V91 / 0.91.0 but HEAD is v119 / V95 / 0.95.0. Six sessions behind. This is a recurring close-step miss, not a documentation gap — the instruction exists but keeps getting skipped under context pressure.

---

## Adapted prompt (for reuse)

The reader test was adapted from `Dev/Resources/Iteration playbook/Reader test.md` for dev-side docs. Three scenario prompts were used:

**Scenario A (Comprehension Q&A):** 14 questions covering session types/routing, close paths, three-number versioning, footer bumps, dev-side/plugin-side disambiguation, batch-ordering audit, doc-code parity six-item check, idea sweep routing, proxy regeneration, frame-correction sweep bar, batch removal timing, pre-commit checkpoint, response-shape tags, and mixed-session close path.

**Scenario B (Fresh dev session role-play):** Claude opens its first build session with opener "Spare session. Start the next build session." Produces the actual response, then reflects on which instructions were followed, which were unclear, and what information was missing.

**Scenario C (Curveball role-play):** Claude receives a multi-thread opener blending E2E test observations, a structural change proposal, a reported doc contradiction, and a request for opinion. Produces the response showing routing decision, then reflects on disambiguation, blended-opener handling, and dev-side/plugin-side boundary application.

**Reuse notes:** Comprehension Q&A surfaced the most mechanical gaps (stale references, timing asymmetries). Curveball surfaced the most judgment gaps (routing ambiguity, disambiguation sequencing). Fresh session was intermediate — confirmed the session-open procedure is mostly mechanical but found undocumented fallbacks. For future runs: rotate questions in Scenario A to probe new areas; vary the curveball opener to stress different routing edges.
