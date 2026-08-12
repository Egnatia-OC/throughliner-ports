# [HASH] — Builds now read SPEC and are checked against it; the sync gate leaves the build close for the /plan close

Four parts, decided by the user at /plan: the doc stays, builds read SPEC, the sync gate moves to the end of /plan, and in its place the build close *checks what was built against SPEC* rather than syncing SPEC to match it.

**Why the gate was doing the opposite of its job** — the user's reasoning, in their own words: at the end of a build the gate ends up functioning as a place for the model to justify whatever it did within the scope. A close-time sync on a document the build never read can only record what the build did. It cannot catch a build that contradicted the spec, because it has nothing to compare against. That is a justification step wearing a check's clothing.

**The research backs the inversion rather than merely permitting it** (`resources/research/spec-document-standards.md`): spec-driven development — which this method already invokes by name to justify the gate — defines the spec as the source of truth *read at implementation time*. So this moves the method toward the standard it already cites.

## What shipped

- **`next.md`** — SPEC read **once at run start**, in the pre-flight, not per item.
- **`next-build.md`** — a new step 4 in the build loop: check the built item against SPEC, **silent unless it contradicts**. On a contradiction, name the sentence and let the user decide which is wrong; never rewrite SPEC to fit.
- **`done-build.md`** — 1.3 renamed from Spec-sync gate to **Spec check-against**, doing the run-level look over accumulated work.
- **`done.md`** — the shared gate is now plan-close only; the build-close branch removed from its table.
- **`plan.md`** — the SPEC ground rule now says the /plan close is the only sync gate, and that SPEC is read at build time.
- **SPEC.md** and a **FAQ** addition.

**The open question settled at build: per item, as recommended.** SPEC is loaded from run start so the marginal cost is near zero, and a contradiction caught at the item that caused it is far cheaper than one found after five more items built on top of it. The counter — turn cost on a run meant to be left alone — is answered by the check being silent on the pass path.

**The decided-but-unbuilt case written out explicitly**, rather than left for a later session to re-derive. With the sync gate living only at the /plan close, a decision made and not yet built is the state the gate now meets by default. Editing SPEC at the moment a retirement is *decided* would make it describe a product that doesn't exist — a false SPEC, not a synced one. So the gate is satisfied where SPEC still describes the shipped product accurately and the item carrying the change lists SPEC.md among its files. That is the judgment a previous session made on the working-mode retirement, now shipped as wording.

**A scope grow, approved mid-build:** `next-build.md` was not in the item's file list, which named `done-build.md`. The per-item placement the item itself recommended lives in `next-build.md`, so it was added with the user's approval rather than the check being relocated to fit the list.

**Files touched:** `plugin/si-plugin/docs-b/next.md`, `next-build.md`, `done-build.md`, `done.md`, `plan.md`, `SPEC.md`, `FAQ/faq.md`.

**Routed to Captures:** none.

Rule gate: run — net neutral to slightly negative on rule count. A gate was MOVED rather than added: the build close's sync obligation was repealed and replaced by a check, and the /plan close's gate is unchanged. `next-build.md` gains one step and `next.md` one read. Nothing lands in the always-loaded corpus. Admission rests on the user's decision plus the SDD research the method already cites to justify the gate it was contradicting.
FAQ: updated — the SPEC-during-build entry gained the builds-read-SPEC change and why the old close-time sync was replaced.
