# PENDING — Beta day-one posts: re-verified and handed over

`[user]` item [beta-day-one-posts], walked through in the second 2026-08-26
/next run. A sibling record from earlier the same day is
`2026-08-26-beta-day-one-posts-walkthrough.md`.

## Step 1, Claude's: re-verify both drafts against the shipped build

Checked against the released commit `2a96ce4` and the repository as it stands,
not against the working tree:

- *"Today's release is brand new — today's build, patched and re-run this
  afternoon on top of the version I've been living in since it landed late last
  night."* — holds. test19 landed 01:15, test20 was cut at 14:32 on top of it,
  and the run that afternoon patched it.
- *"keep your projects in git (Throughliner sets this up by default)"* — holds;
  the released `setup.md` initialises a repository.
- *"report anything odd in the support channel"* / *"it'll draft a GitHub issue
  on the Throughliner repository and post it with your yes (or, without the
  GitHub CLI, draft a report for the form for you to paste)"* — holds; the
  released `feedback-and-inbox.md` carries that route.
- *"The beta release will be the safest pick"* — holds; `#beta` resolves to the
  release commit.

## The one claim this project cannot verify, named rather than used to withhold

Both drafts point at the pinned "How to install" post — the announcement calls it
*"the tested route"*, the channel pin calls the beta release *"the safe route —
pinned in the how-to forum"*. This project has no view of Discord. What it knows
is that `README.md` and `INSTALL.md` both name `FlintcraftTech/throughliner#beta`
correctly, and that editing the pinned post's install command is step 4 of
[beta-install-smoke-and-post-edit], which has not been reported done. So the
claim is true if that post already names `#beta`, and not otherwise — a thing
only the user can see.

**Handed the drafts over with that caveat stated beside them rather than held
back.** Withholding approved drafts on a truth-condition Claude cannot check is
the failure recorded in [walkthrough-answers-request-with-sequencing], filed from
this session's own audit of the run where it happened. The corrected behaviour is
to give the user the text and name what to check.

## Outcome — and the drafts should never have been presented at all

The user reported, on being shown them, that **both posts went up hours earlier**,
immediately after the release, exactly as she had told the previous session she
would: *"I said in that session I would post them after done, and I did."* Taken
at her word, per the rule that a volunteered completion is enough. Both register
lines written into `INBOX/sent.md` and the item removed from Processed.

**Why this run re-presented finished work.** The only record of the item said it
was *deferred*. That line was written by the session that handed the drafts over,
before she posted them, and nothing afterwards corrected it — the posting happened
outside any skill, so no session was running to notice.

The sharp part: that record is one of the very records this session's own audit
flagged this morning. Finding 3,
[deferred-recorded-for-items-never-offered], is that the previous run wrote "all
six user steps deferred in place" when only two were deferred by the user. This
run then read one of those lines, believed it, and made her explain herself. The
defect found in the morning caused a fresh instance of itself in the afternoon,
which is about as direct a piece of evidence for it as the record will ever hold.

Filed as [walkthrough-represents-work-completed-outside-a-session].
