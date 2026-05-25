# 0081 — Proxy format and companion proxies

## Goal

Define the proxy file format and create companion proxies for UX.md, MANIFEST.md, TEST-LOG.md, and a new index proxy for research/. This establishes `.proxies/` as the universal lightweight-index layer. Claude reads proxies first, dips into full docs for detail via offset/limit.

This is Session A of a three-way split. Session B (0089) relocates BACKLOG and build-log INDEX.md content into `.proxies/`. Session C (0090) splits TEST-LOG.md into a folder with `.proxies/test-log.md` as its index.

## Inputs

- A consumer project's `UX.md` and `MANIFEST.md` (e.g. Taskflow's) — to design proxy content against real docs.
- `plugin/docs/DOC-STRUCTURE.md` — current doc structure spec (receives proxy format section).
- `plugin/docs/procedures/planning.md` — receives "regenerate proxies" step.
- `plugin/docs/procedures/setup.md` — receives "generate initial proxies" step.
- `plugin/hooks/universal-behaviour.md` — receives "read proxy first" rule.

## Outputs

**Proxy format spec:**
- `plugin/docs/DOC-STRUCTURE.md` — new section defining proxy format: location (`.proxies/`), terse-markdown shape (header block + entry index with line numbers), regeneration rules.

**Proxy templates (4 files):**
- `plugin/templates/.proxies/ux.md` — template for UX proxy.
- `plugin/templates/.proxies/manifest.md` — template for MANIFEST proxy.
- `plugin/templates/.proxies/test-log.md` — template for TEST-LOG proxy.
- `plugin/templates/.proxies/research.md` — template for research index.

**Procedure doc updates (2 files):**
- `plugin/docs/procedures/planning.md` — regenerate affected proxies after editing source-of-truth docs.
- `plugin/docs/procedures/setup.md` — generate initial proxies after scaffolding.

**Behaviour rule (1 file):**
- `plugin/hooks/universal-behaviour.md` — add "read proxy first, dip into full doc for detail" required behaviour.

**Vocabulary (1 file):**
- `plugin/docs/VOCABULARY.md` — proxy definition.

**Scaffold update (1 file):**
- `plugin/skills/setup/scripts/scaffold.py` — create `.proxies/` and generate initial proxy files during `/setup`.

## Success criteria

1. Proxy format spec defined and documented in DOC-STRUCTURE.md.
2. Templates exist for all four proxy types.
3. `/setup` scaffolds `.proxies/` with initial proxy files.
4. Planning procedure includes proxy regeneration as a final step.
5. universal-behaviour.md includes the "read proxy first" rule.
6. Projects without `.proxies/` still work — all proxy reads have a full-doc fallback.

## Open questions for this session

All resolved:
1. ~~Proxy format~~ → Terse markdown.
2. ~~Which docs~~ → UX, MANIFEST, TEST-LOG, research (companions). BACKLOG and build-log proxies come in 0089 (INDEX relocation).
3. ~~Proxy location~~ → `.proxies/`.

## Risks / dependencies

- Depends on 0079 (procedure docs — shipped v77) and 0080 (phase-aware editing — shipped v78).
- Low blast radius. Additive — new files, new format spec, procedure and behaviour updates. Nothing breaks if proxies are missing (fallback to full doc).
- TEST-LOG proxy starts as a companion to the single file; 0090 upgrades it to the folder index when TEST-LOG splits.
