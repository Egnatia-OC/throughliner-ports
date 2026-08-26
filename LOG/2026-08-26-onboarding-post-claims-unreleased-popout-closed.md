# Onboarding post's pop-out claim — now true of the shipped build

`[user]` item [onboarding-post-claims-unreleased-popout], closed in the second
2026-08-26 /next run without any step being handed to the user.

## What was checked

Step 1 of the walkthrough was Claude's: confirm the release went out from a
commit carrying the pop-out case. Checked directly against the released commit
rather than the working tree — `git show 2a96ce4:plugin/throughliner/docs/setup.md`
carries the Case D section, "popping a subpart out into its own project", along
with its precedence rule over Case B. `2a96ce4` is the commit the `beta` branch
points at and the one v1.21.0 was cut from.

So the claim in the "Running your first session" post — that /setup in a
subfolder detects the parent, reads its spec, asks which part the subfolder
covers, and pops it out — is true of what a beta tester installs today.

## What was done, and what was NOT handed over

The item's step 2 asked the user to re-read the post's pop-out paragraph and find
nothing to change; step 3 asked her to report back so the register line could be
updated. Neither was driven. The outcome of step 2 is "nothing to change", which
is a conclusion the check above already establishes, and step 3 corrects a
factual line in this project's own register — ordinary work rather than the
user's.

`INBOX/sent.md`'s line for that post previously read that the pop-out claim
"was untrue of the installed plugin when posted and still is". The second half
was false as of this morning. It now records when the claim became true and
names the commit and the file checked.

Not handing these over is deliberate and follows
[walkthrough-hands-over-cleanup-that-stalls-the-run], filed minutes earlier in
this same run: a `[user]` step whose whole content is "confirm what Claude has
already established" is not user work.
