# 2ccbadf — README + INSTALL refresh: desktop-app UI + content overhaul

The desktop Claude app's UI changed, so README.md and INSTALL.md had drifted out of step with what a new user actually sees. Install is now "add" (Customise > Plugins > add > Upload plugin), not the old "+ icon → Create a plugin"; uninstall is now Customise > Plugins > Sovereign Implementer > three-dots > Uninstall, replacing the old "gear icon > Uninstall". Both files were brought back in line: README's install line, and INSTALL's upload-screen walkthrough, its two uninstall spots, and the screenshot-pointer note (the screenshot itself still waits on [install-upload-path-clarity], which needs a real desktop capture).

Alongside the UI fix, several README descriptions had drifted or were never general enough. The pitch was generalised beyond "apps" — the tagline and "Who it's for" now cover any project a non-coder wants to build, with apps kept as the headline example for appeal, so non-app projects see themselves. The /setup bullet drops the "five questions" count and fixes "answers" → "asks" (now "a short questionnaire"); the /done bullet drops "test" (testing happens during /next); the tested environment moves to Opus 4.8 on effort level high; auto mode gains a short why (it's optional, it spares approving each step by hand, turn it off to confirm each action); "/clear after every skill" → "/clear after every /done"; and Getting started drops the count and says "run /setup". The "spec read-only during builds" line was reviewed and kept — accurate for every build but a spec-edit.

The user-review (Alex reads the refreshed README + INSTALL.md and says if any wording's off) is a review, not a pass/fail test, so it's held as a plain reminder rather than a deferred-test line.

**Files touched:**
- README.md
- INSTALL.md

**Routed to Captures:** none
