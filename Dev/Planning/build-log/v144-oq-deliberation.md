# v144 — OQ and idea deliberation

**Date.** 2026-05-30
**Type.** Planning (OQ deliberation)
**Batch.** None (planning session)

## What happened

Deliberated three OQs and began reviewing three ideas. Session cut short by remote-control disconnect — ideas 1–3 not fully deliberated.

## Decisions taken and why

1. **Orientation gap (plugin-side):** Generate a capabilities summary at `/sovclose` time (during doc-parity, when MANIFEST is already read in full), write it to the top of MANIFEST, let the proxy pick it up. Zero extra full-reads at session start. Dev-side approach still open.

2. **`/sovexplain` routing:** `/sovexplain` is strictly about the method/plugin, not the user's project. It becomes a router: "what" pulls from MANIFEST capabilities summary, "how" routes to procedure docs/skills, "why" uses the explain-reference. No inflation of the reference into an everything-doc. Separate concern: when users ask project-specific "why" questions about their own codebase, Claude checks MANIFEST rationale fields — that's general Claude behaviour, not `/sovexplain`.

3. **Design-decision sweep:** Folds into the existing doc-parity step at close. After writing the build-log entry, scan its decisions, route UX-relevant ones to UX.md and implementation ones to MANIFEST rationale fields. Both destinations already exist. MANIFEST rationale fields then double as the read path for project-specific "why" questions.

4. **New OQ filed:** Session-start hook doesn't re-fire after `/clear` or context loss. The build cycle is taught, not programmed — `/clear` leaves Claude with no build-cycle awareness.

## What changed

- BACKLOG.md: Two OQs resolved and removed (/sovexplain routing, design-decision sweep). One OQ partially resolved (orientation gap — plugin-side decided, dev-side open). One new OQ added (hook re-fire after /clear).

## What's next

Three ideas still need deliberation (premature /sovbuild, idea/OQ misrouting, /sovexplain E2E test). Resolved OQs need implementation batches scoped.
