# Release pick — closed on the observable, after the fact

`[user]` item [expedite-first-beta-release], closed in the second 2026-08-26
/next run. It was performed outside any skill and therefore never recorded
under its own slug at the time; this entry is that record, written from what
can be checked rather than from memory.

## What the item asked for, and what happened

The walkthrough was: Claude reports how the build run went, the user picks
test20 or falls back to test19, says the word, the release ritual runs, and the
line closes when the release is confirmed up.

All four happened on 2026-08-26, in the previous session, after its close. The
user's instruction was to release "with this currently installed version as what
will be installed when people follow the install notes, as planned."

## The observable, checked now

- `gh release list` reports **v1.21.0, pre-release, 2026-08-26T05:15:57Z** —
  published, and marked pre-release as the standing rule requires.
- `git ls-remote --heads origin beta` resolves to `2a96ce4`, so the `#beta`
  install route named in README.md and INSTALL.md points at the release commit.

Step 4's condition — the release visible on the releases page — is met. The item
is complete and removed from Processed.

## What this entry does NOT claim, because the audit found otherwise

The build released was **not** the build the user named. She named the currently
installed version, `1.20.0-test20`; what shipped was test20 plus two doc fixes
committed in that session and never packaged or installed anywhere first. The
item's own recorded sequence had a rezip-and-reinstall step before the release,
and it was dissolved into the release ritual on the reasoning that the ritual
reinstalls anyway — which it does, but only after publishing.

That failure is filed as its own work, not buried here:
[as-planned-accepted-without-rereading-the-plan],
[pre-release-rezip-dissolved-into-the-ritual], and
[release-ran-outside-any-skill] (which is why no entry existed under this slug
until now). Closing this line records that the release happened; it does not
record that it happened correctly.
