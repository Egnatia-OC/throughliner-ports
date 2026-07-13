# Comparison page — maintenance plan

**Status.** Future build batch (post-V29).
**Date sketched.** 2026-05-15.
**Location.** `Marketing/comparison-page-maintenance-plan.md` (gitignored, local-only).

## Purpose

Keep `Marketing/platform-comparison.html` current. A scheduled task does landscape surveillance; I decide what makes it into the page.

## Shape

A Cowork **scheduled task** runs fortnightly, produces one file, never touches the HTML directly.

### What the task does

1. **Scan for new entrants.** Web-search for no-code platforms / AI coding assistants launched or updated since last run.
2. **Diff existing entries.** Fetch each tool's pricing and ToS pages; flag changes.
3. **Write the update file.** Output to `Marketing/landscape-updates/YYYY-MM-DD.md`.

### What stays manual

- Reading updates, deciding what enters the table/Watching section, editing HTML, verifying claims against primary sources.

Automation feeds a review queue. It does not publish.

## Output file shape

Each `landscape-updates/YYYY-MM-DD.md`:

> **## New entrants** — name, one-liner, source link, why it surfaced, recommendation (Watching / main table / ignore + reason).
>
> **## Existing entries — diffs detected** — what changed, source link, recommendation for affected cell.
>
> **## Closure** — one-paragraph summary. "Quiet fortnight" if nothing material.

## Prompt template (designed during the build batch)

The prompt must: pin the existing tool list with monitored URLs, instruct broad category search then narrow per-tool diffs, force structured output matching the shape above, cap output length.

**Open questions:**

- **Diff mechanism.** Snapshot-and-diff (reliable, adds state file) vs. web-search freshness signals (simpler). Lean: start without snapshots, revisit if noisy.
- **Watching section format.** Inline on same page (collapsed toggle) vs. separate page. Lean: same page.

## Prerequisites

The comparison table must first be restructured into **visual no-code builders** and **AI-assisted code generation** sections, plus a **Watching list**. The May 2026 Sonnet research feeds that restructure. Automation feeds an already-shaped page.

## Why this isn't part of the plugin

The plugin is the method itself. This is marketing infrastructure — different audience, different concerns, gitignored. Moves with the marketing site if that becomes tracked.

## Carry-forward

1. Read most recent `landscape-updates/` file (or generate one).
2. Confirm table shape matches the restructure above.
3. Decide the two open questions.
4. Build the scheduled task via `mcp__scheduled-tasks__create_scheduled_task`.
5. First two cycles: read outputs closely, refine prompt.
