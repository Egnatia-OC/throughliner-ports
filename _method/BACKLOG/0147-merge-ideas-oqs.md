# Merge Ideas into Open Questions + combine ideation/deliberation

**Goal.** Eliminate the Ideas → OQ promotion step. One BACKLOG section holds all unscoped captures — from raw one-liners to fleshed-out questions. One skill and procedure replaces `/sovideate` and `/sovdeliberate`.

**Outputs.** BACKLOG drops from 6 sections to 5. One combined skill replaces two. All plugin and dev docs updated to remove Ideas as a separate concept.

**Success criteria.** BACKLOG has 5 sections. One skill handles both "I just had a thought" and "let's work through the backlog." No references to Ideas as a separate concept remain in plugin or dev docs. Consumer projects with legacy Ideas sections don't break.

**Decisions to make this batch.**

- **Combined skill name.** `/sovideate` (more inviting for mid-build "I just had a thought"), `/sovdeliberate` (broader — "careful consideration" covers both capture and resolution), or something new?

**What it doesn't do.** No changes to other BACKLOG sections. No hook changes. No `/sovplan` changes. No migration tool for consumer projects with existing Ideas sections — the combined skill handles legacy format gracefully.

Changes:
- [Requested] `BACKLOG-TEMPLATE.md` — remove `## Ideas`. Update `## Open questions` to welcome light captures (heading + Surfaced + one sentence) alongside full entries. BACKLOG becomes 5 sections.
- [Requested] `DOC-STRUCTURE.md` — update BACKLOG spec: remove Ideas, loosen OQ entry format (Why-it-matters and Next-step become optional). Update proxy description to 5 sections.
- [Requested] `templates/.proxies/backlog.md` — update to 5 sections.
- [Requested] Merge `procedures/ideate.md` and `procedures/deliberate.md` into one procedure doc. Combined flow: present existing OQs, explore user's new topic, route everything. Delete the retired doc.
- [Requested] Keep one skill, delete the other. Update SKILL.md description to cover both activities.
- [Requested] `procedures/close.md` — update "planning, ideation, or general sessions" wording.
- [Requested] `universal-behaviour.md` — update routing table entries referencing ideation/deliberation as separate activities.
- [Requested] `VOCABULARY.md` — retire "Ideas section" as distinct concept. Merge ideation/deliberation definitions.
- [Requested] `explain-reference.md` — check and update entries referencing Ideas vs OQs.
- [Requested] `_method/proxies/backlog.md` — remove `## Ideas` section.
- [Requested] `Reference manual.md` — update skill descriptions, BACKLOG section list.
- [Requested] `crash-course/` — update relevant HTML sections.
- [Requested] `INVENTORY.md` — update component listings.

Serves UX.md: Planning sessions.
