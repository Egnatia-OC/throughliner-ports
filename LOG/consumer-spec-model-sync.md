# [HASH] — Updated the consumer-facing SPEC model in the templates (read-only-during-builds → spec-edit-batch)

[spec-edit-batch-type] made SPEC a normal doc, changed only through a planned spec-edit batch, and removed the old "SPEC read-only during builds" rule — but it only updated this project's host-only CLAUDE.md. Two consumer-facing surfaces still taught the old model, so a new user would learn a rule the plugin no longer follows. This batch reworded both, in plain English for a non-coder.

CLAUDE-TEMPLATE.md's "Rules for Claude" replaced "SPEC.md is read-only during builds. Edit it only during /plan" with the accurate model: SPEC changes only through a planned spec-edit batch (one that lists SPEC.md), which /next runs like any other build, and an ordinary build can't touch it because the safety check blocks any file the batch doesn't list. The FAQ's "Can I edit SPEC.md while doing a build?" answer was reworded to match — explaining that changing SPEC takes a spec-edit batch (/plan queues it, /next runs it), with spec issues noted for /plan mid-build. The question wording didn't change, so the FAQ index stayed as-is. For consistency, this project's own dogfood FAQ copy got the same answer.

**Files touched:**
- plugin/si-plugin/templates/CLAUDE-TEMPLATE.md — Rules for Claude SPEC line reworded
- plugin/si-plugin/templates/faq-template.md — "Can I edit SPEC.md…" answer reworded (index unchanged)
- FAQ/faq.md — same answer synced (dogfood copy)

**Routed to Captures:** none
