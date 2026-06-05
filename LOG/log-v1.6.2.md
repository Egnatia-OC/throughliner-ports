# LOG

Full session entries, newest first. Each entry is written by /done. This file covers the current release — older entries are in per-release log files (LOG/log-v*.md).

## a9088e6 — Hash backfill moved out of /done into /plan and /next start

The previous /done flow committed a `[HASH]` placeholder, ran `rev-parse`, replaced the placeholder, then `--amend`ed — but the amend rewrites the hash, leaving every recorded value off by one (visible as 13c4612 / 44ab617 in the session that surfaced this). The fix moves infill out of /done entirely: the placeholder ships in the commit; the next /plan or /next session scans LOG/log.md and LOG/index.md at start, finds each placeholder, looks up the hash of the commit that introduced that entry, and writes it into the working tree. That edit folds into whatever commit the session itself later makes — no amend, no two-commit ceremony, hash matches what's actually in history. /done shrinks accordingly: 2.4 and Plan close-out 3 lose three steps each and a closing paragraph explains where the backfill now lives.

**Files touched:**
- plugin/si-plugin/docs/done.md: 2.4 and Plan close-out 3 retitled "Git commit," trimmed to 4 steps; closing paragraph added explaining backfill location
- plugin/si-plugin/docs/next.md: Step 1 gained sub-step 1 "Backfill LOG hashes" [BRIEF]; existing sub-steps renumbered 1→2..4→5
- plugin/si-plugin/docs/plan.md: Step 1 gained a backfill paragraph above the read-state instruction

**Routed to Captures:** none

**Pushed:** v1.6.2

## 734c8d2 — Audience anchor added to this project's CLAUDE.md

The plugin ships to external non-coders, but this project is built by a non-coder developing the plugin itself — a single person occupying both roles. Without a stated audience, skill-doc edits drift: language meant for the developer leaks into the chat narration, prompts, and headings the external user actually sees. The new Audience section makes the distinction the first thing any session editing skill docs encounters, names which strings the rule governs (chat narration, drafts, prompts, headings, status lines, error messages), and gives examples of the internal terms that must not leak ("behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Closes with a check-before-saving instruction so the rule fires at the right moment rather than living as background context.

**Files touched:**
- CLAUDE.md: added "## Audience" section between "What this is" and "Host and target"
- QUEUE.md: removed the now-built batch

**Routed to Captures:** none
