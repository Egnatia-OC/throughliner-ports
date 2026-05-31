# Merge Ideas into Open Questions + combine ideation/deliberation

**Goal.** Eliminate the Ideas → OQ promotion step. One BACKLOG section holds all unscoped captures — from raw one-liners to fleshed-out questions. One skill and procedure replaces `/sovideate` and `/sovdeliberate`.

**Scope.**

**Plugin-side — structure:**

1. `BACKLOG-TEMPLATE.md` — remove `## Ideas`. Update `## Open questions` to welcome light captures (heading + Surfaced + one sentence) alongside full entries. BACKLOG becomes 5 sections.
2. `DOC-STRUCTURE.md` — update BACKLOG spec: remove Ideas, loosen OQ entry format (Why-it-matters and Next-step become optional, not mandatory). Update proxy description to 5 sections.
3. `templates/.proxies/backlog.md` — update to 5 sections.

**Plugin-side — procedures and skills:**

4. Merge `procedures/ideate.md` and `procedures/deliberate.md` into one procedure doc. Combined flow: present existing OQs, explore user's new topic, route everything. Light captures get quick routing; fleshed-out entries get full deliberation. Delete the retired doc.
5. Keep one skill, delete the other. Update SKILL.md description to cover both activities.
6. `procedures/close.md` — update "planning, ideation, or general sessions" wording. Idea sweep routing already goes to "batch or OQ" — no functional change.

**Plugin-side — reference docs:**

7. `universal-behaviour.md` — update routing table entries referencing ideation/deliberation as separate activities.
8. `VOCABULARY.md` — retire "Ideas section" as distinct concept. Merge ideation/deliberation definitions.
9. `explain-reference.md` — check and update entries referencing Ideas vs OQs.

**Dev-side:**

10. `BACKLOG.md` — remove `## Ideas` section (currently empty).
11. `session-protocol.md` — routing table: merge Ideation row into a combined type covering both capture and resolution. Update idea-sweep and close references.
12. `session-reference.md` — update OQ entry shape if it references Ideas promotion.
13. `_method/proxies/backlog.md` — update Ideas section (or remove if merged into OQs).

**Consumer-facing docs:**

14. `Reference manual.md` — update skill descriptions, BACKLOG section list.
15. `crash-course/` — update relevant HTML sections (check `data-source` attributes).
16. `INVENTORY.md` — update component listings.

**Decisions to make this batch.**

- **Combined skill name.** `/sovideate` (more inviting for mid-build "I just had a thought"), `/sovdeliberate` (broader — "careful consideration" covers both capture and resolution), or something new?

**What it doesn't do.** No changes to other BACKLOG sections. No hook changes. No `/sovplan` changes. No migration tool for consumer projects with existing Ideas sections — the combined skill handles legacy format gracefully.

**Success criteria.** BACKLOG has 5 sections. One skill handles both "I just had a thought" and "let's work through the backlog." No references to Ideas as a separate concept remain in plugin or dev docs. Consumer projects with legacy Ideas sections don't break.
