# ea272f6 — Drop mandatory provenance; keep an explicit user-credit marker, default-AI

Every work line carried a required author label ("captured by you" / "by Claude"), lint-enforced. The label was unused, inaccurate under mixed authorship, and impossible to trace fully; forcing a "by Claude" on every line added noise no one read. Changed to a one-directional convention: unmarked lines are assumed to come from the AI (no AI-authorship label is ever written), and a `captured by you` credit is written only when the user personally raised, pushed through, or wrote the item — the one signal with value. The credit tracks who *stood behind* the item, not who typed each fragment. Extended one level down as a prose convention: rationale is assumed Claude's unless credited as the user's stated intention, marked inline — consistent with the why-pipeline's rationale-is-prose rule, adding no hook-read field.

Hook-enforced-format change, so the ripple was traced by grepping the format across the repo before editing (SPEC/README carry no provenance sentence → no change there). The lint (post_tool_use.py) stopped *requiring* a label: check 2 (`_check_provenance` + the PROVENANCE regex) was removed, the remaining checks renumbered, and the docstring rewritten to state the asymmetric default-AI convention — the lint now neither requires nor forbids a label. Verified clean on the real QUEUE.md, an unlabeled item no longer flags, and both hooks compile. The convention was rewritten across plugin-behaviour.md (Captures line-format bullet, filing-stamp paragraph, hook-parse shape list, forward-advisory format, and a new rationale-provenance paragraph in why-pipeline Preserve), plan.md (discipline bullet + seed step), CLAUDE-TEMPLATE.md, faq-template.md, and migrate-checklist.md.

Note: the *installed* host still runs the pre-change lint until the next reinstall, so this session's AI-raised captures (written unmarked per the new convention) draw advisory missing-provenance flags — expected, harmless, and gone once the rezip lands.

**Files touched:**
- plugin/si-plugin/hooks/post_tool_use.py — removed the provenance requirement (check 2), renumbered, rewrote docstring
- plugin/si-plugin/docs/plugin-behaviour.md — Captures + why-pipeline rewritten to the asymmetric convention
- plugin/si-plugin/docs/plan.md — discipline bullet + seed-step provenance
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md, faq-template.md — user-credit descriptions
- plugin/si-plugin/docs/migrate-checklist.md — provenance references

**Routed to Captures:** none
