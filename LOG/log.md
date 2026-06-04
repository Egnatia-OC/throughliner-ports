# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## 734c8d2 — Audience anchor added to this project's CLAUDE.md

The plugin ships to external non-coders, but this project is built by a non-coder developing the plugin itself — a single person occupying both roles. Without a stated audience, skill-doc edits drift: language meant for the developer leaks into the chat narration, prompts, and headings the external user actually sees. The new Audience section makes the distinction the first thing any session editing skill docs encounters, names which strings the rule governs (chat narration, drafts, prompts, headings, status lines, error messages), and gives examples of the internal terms that must not leak ("behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Closes with a check-before-saving instruction so the rule fires at the right moment rather than living as background context.

**Files touched:**
- CLAUDE.md: added "## Audience" section between "What this is" and "Host and target"
- QUEUE.md: removed the now-built batch

**Routed to Captures:** none
