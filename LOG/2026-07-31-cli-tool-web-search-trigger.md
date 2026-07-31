# [HASH] — plugin-behaviour.md Research + FAQ — added a "reach for a CLI tool before a GUI walkthrough" trigger (consider CLI self-service, then offer a web search)

From a legal project: Claude used a CLI tool (Tesseract OCR) productively — but only after the user asked "are there any CLI tools you could use for this?" Before that prompt it defaulted to explaining the task in GUI apps. A non-coder doesn't know CLI tools exist, so can't know to ask; the capability must not depend on the user prompting for it. Added a trigger to plugin-behaviour.md's "Research and evidence filing" with two halves that must both fire: (1) the consideration — before handing over a GUI walkthrough, Claude asks itself whether a tool would let it do the task instead; (2) the search offer — when a suitable tool plausibly exists, proactively offer a web search for one. The search offer alone is insufficient because without the consideration firing first, Claude never thinks to look. Three guards carried verbatim: surface the tool and its purpose (no blind installs), honour the existing consent rules (downloads, running commands, device access), and don't presume the user has a terminal (name the requirement per the surface-the-environment rule). Cross-referenced to the Communication rule "Run commands yourself" as its why rather than duplicated. FAQ entry + index line added.

**Files touched:**
- plugin/si-plugin/docs/plugin-behaviour.md (Research and evidence filing)
- plugin/si-plugin/templates/faq-template.md
- plugin/si-plugin/templates/faq-index-template.md

**Routed to Captures:** none
