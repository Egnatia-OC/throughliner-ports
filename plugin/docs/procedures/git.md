# Git procedure — no-code method

Follow this procedure to commit, tag, and push the current session's work. Plain-English narration throughout — the user may have minimal git experience.

## First-use detection

Check CLAUDE.md for a `## Git workflow` section. If absent:

1. **[SEQUENCE] Ask the user's setup.** "Are you working solo on this project, or with a team? Solo means commit straight to main; team means branches and pull requests."
2. **Write the section** to CLAUDE.md based on their answer:
   - **Solo:** `## Git workflow\n\nSolo. Commit to main, tag, push.`
   - **Team:** `## Git workflow\n\nTeam. Branch per batch, commit, push, open PR. No direct main commits.`
3. Proceed with the matching workflow below.

If the section exists, read it and follow the matching workflow.

## Solo workflow

### Step 1 — Stage

`[BRIEF]` Stage all method-doc and source-code changes from this session. Narrate what's being staged:

> "Staging N files: [short list]. These are the changes from this session."

Run `git add` with the specific file paths. Never use `git add -A` or `git add .` — list files explicitly.

### Step 2 — Commit

`[BRIEF]` Draft a commit message. Format: one summary line (imperative, ≤72 chars), blank line, optional body with bullet points for what changed.

Present the message to the user:

> "Proposed commit message:\n\n```\n<message>\n```\n\nLook good?"

`[PROMPT]` Wait for okay or edits.

### Step 3 — Tag

`[BRIEF]` If the session warrants a version tag (build sessions always do; planning sessions may or may not — ask if unclear):

> "Tagging as `v<N>`. This marks the session in git history."

Run `git tag v<N>`.

### Step 4 — Push

`[PROMPT]` "Ready to push to remote. This sends your commit and tag to GitHub. Go ahead?"

On okay: `git push origin main && git push origin v<N>` (or just `git push origin main` if no tag).

On refusal: stop. Don't push. Session can still close cleanly without pushing.

### Step 5 — Done

`[PROMPT]` "All committed. `/clear` when you're ready for a fresh session."

## Team workflow

### Step 1 — Branch

`[BRIEF]` Check if already on a feature branch. If on main:

> "Creating a branch for this work: `<branch-name>`. This keeps main clean until you're ready to merge."

Branch name: kebab-case from batch heading (e.g. `add-dark-mode`).

### Step 2 — Stage

Same as solo step 1.

### Step 3 — Commit

Same as solo step 2.

### Step 4 — Push branch

`[PROMPT]` "Ready to push your branch to remote. This doesn't affect main — it just uploads your branch. Go ahead?"

On okay: `git push -u origin <branch-name>`.

### Step 5 — PR guidance

`[BRIEF]` "Your branch is pushed. To merge into main, open a pull request on GitHub. You can do that at: `https://github.com/<owner>/<repo>/pull/new/<branch-name>`"

If `gh` CLI is available, offer: "I can open the PR for you with `gh pr create`. Want me to?"

### Step 6 — Done

`[PROMPT]` "All committed and pushed. `/clear` when you're ready for a fresh session."

## What you must not do

- **Don't force-push.** Never `git push --force` or `--force-with-lease` unless the user explicitly asks.
- **Don't amend commits.** Create new commits, not amends.
- **Don't skip hooks.** Never `--no-verify`.
- **Don't commit secrets.** Scan staged files for `.env`, credentials, API keys. If found, unstage and warn.
- **Don't push without asking.** Push is always a `[PROMPT]` — never automatic.
- **Don't assume remote exists.** If `git push` fails with "no remote," explain how to add one and ask.

## Behavioural rules

Universal-behaviour rules apply. Push back, plain English, ask on ambiguity, engage with pushback.

---

*No-code method — Version 87.*
