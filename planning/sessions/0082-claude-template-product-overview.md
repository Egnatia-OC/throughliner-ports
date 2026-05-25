# 0082 — CLAUDE template product overview section

## Goal

Add a product overview section to the CLAUDE template that `/setup` populates through conversation with the user. Claude starts every session knowing what the product is, who it's for, what friction it solves, and what milestones the user is working toward — without reading any other doc.

Currently CLAUDE.md is just path configuration and plugin management notes. Claude has no orientation until it reads UX.md or MANIFEST.md.

## Inputs

- `plugin/templates/CLAUDE-TEMPLATE.md` — current template (paths, plugin management, project-specific notes).
- `plugin/docs/procedures/setup.md` (from 0079) — setup procedure, needs a step for populating the overview through conversation.

## Outputs

**Template update (1 file):**
- `plugin/templates/CLAUDE-TEMPLATE.md` — new `## Product overview` section at the top (before path block), with four fields:
  - **What it is** — one-sentence description of the product.
  - **Who it's for** — the intended user/audience.
  - **What friction it solves** — the tension or problem the product addresses.
  - **Milestones** — what the user is working toward in its development, with rough timeframes if known.

**Setup procedure update (1 file):**
- `plugin/docs/procedures/setup.md` (from 0079) — add a conversational step where Claude asks the user about their product and fills in the overview. This is the onboarding conversation — Claude asks, the user answers, Claude writes. Not a form to fill out.

**Docs (1 file):**
- `plugin/docs/DOC-STRUCTURE.md` — document the product overview section: what it contains, when it's written (setup), when it's updated (planning, when milestones shift).

## Success criteria

1. After `/setup`, CLAUDE.md contains a filled-in product overview that orients any future session without reading other docs.
2. The overview is written by Claude based on a conversation with the user — not a blank template the user fills in manually.
3. The overview is editable during planning (per 0080's permission model) so milestones can be updated as the project evolves.
4. Session start hook can read the overview for richer state summaries (e.g. "Taskflow — task management app, working toward MVP by Q3").

## Open questions for this session

1. ~~**Milestones format.**~~ Resolved: free text. Natural for the setup conversation.

## Risks / dependencies

- **Depends on 0079** (setup procedure doc exists to receive the new step).
- **Depends on 0080** (overview is editable during planning for milestone updates).
- **Very low blast radius.** One template, one procedure doc, one spec doc. Additive only.
- **Existing projects.** Projects adopted before this change won't have the section. The setup procedure should handle backfill — next planning session, Claude notices the missing section and asks the user to fill it in.
