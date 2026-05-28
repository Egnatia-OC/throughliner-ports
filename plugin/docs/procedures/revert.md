# Revert procedure — no-code method

Follow this procedure to undo a failed build. Plain-English narration throughout — the user may have minimal git experience.

## When to use

The user says something like "that broke everything," "undo the last build," or invokes `/sovrevert`. Restores the project to the last committed state.

## Pre-flight check

### Step 1 — Confirm a commit exists

`[SILENT]` Run `git log --oneline -1`. If this fails (no commits), skip to *No commit exists* below.

### Step 2 — Identify what changed

`[BRIEF]` Run `git status` and `git diff --stat`. Narrate:

> "Since your last commit, N files have been modified and N files are new. Here's the list:"

Show the file list grouped by type:
- **Modified** — changed since last commit
- **New** — created by this build
- **Deleted** — removed since last commit

### Step 3 — Confirm the revert

`[PROMPT]` Explain what reverting means in plain terms:

> "Reverting will put every file back to the way it was at your last commit. Modified files go back to their old version. New files get removed. Deleted files come back. This can't be undone — the changes from this build will be gone. Want to go ahead?"

Wait for explicit confirmation. If refused, stop — don't revert.

## Revert

### Step 4 — Restore tracked files

`[SILENT]` Run `git checkout -- .` to restore all tracked files.

### Step 5 — Remove untracked files

`[BRIEF]` Check `git status` for untracked files (new files the build created). If present:

> "The build also created N new files that weren't in the last commit. Want me to remove those too, or leave them?"

- **Remove:** `git clean -fd` (removes untracked files and directories).
- **Leave:** skip — narrate that untracked files remain.

### Step 6 — Verify

`[BRIEF]` Run `git status` to confirm a clean working tree. Narrate:

> "Everything is back to where it was at your last commit. Your project matches [commit message / short hash]."

If CLAUDE.md or MANIFEST.md shows a dev server or build command, offer:

> "Want me to start the app to confirm it's working?"

### Step 7 — Guidance

`[PROMPT]` Close with forward-looking guidance:

> "Before your next build, committing first gives you a clean restore point. `/sovgit` walks you through that."

## No commit exists

If `git log` showed no commits:

`[PROMPT]` Explain plainly:

> "There's no previous commit to go back to — this project hasn't been saved to git yet. I can't undo the build because there's no snapshot of what things looked like before. For future builds, committing first (with `/sovgit`) gives you a restore point."

Stop here. Don't attempt to reconstruct prior state.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

- **Never force-revert.** Always confirm before `checkout` and `clean`.
- **Never revert selectively without asking.** If the user wants to keep some changes, walk file-by-file instead of bulk revert.
- **State what's happening.** Every git command gets a plain-English explanation.

---

*No-code method — Version 98.*
