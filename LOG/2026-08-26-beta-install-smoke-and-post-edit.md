# PENDING — `#beta` install smoke test, deferred at step 1

`[user]` item [beta-install-smoke-and-post-edit], walked through in the second
2026-08-26 /next run and deferred by the user at the first step. First record
under this slug.

## What was checked from this side before handing anything over

`git ls-remote --heads origin beta` resolves to `2a96ce4` — the commit v1.21.0
was cut from. So the ref the install route names exists, which is the part most
likely to have been missing: until that branch was created during the release,
`README.md` and `INSTALL.md` had been pointing installers at a ref that did not
resolve at all.

What cannot be checked from here is the install itself. There is no tool on this
machine that installs onto another machine, so steps 1 and 2 are genuine user
work rather than work Claude is merely blocked from running.

## Where it stopped

Step 1 handed over: on the second machine, add the marketplace
`FlintcraftTech/throughliner#beta` and install `throughliner@flintcraft`, looking
for both commands succeeding with no unknown-ref error.

**Deferred by the user.** Nothing was run. The resume point is step 1, unchanged.

## What is still riding on it, stated so a later session does not have to derive it

Step 4 — editing the pinned "How to install" post so its install ask names
`#beta` — is the truth-condition under two claims already posted to Discord on
2026-08-26. The beta announcement calls the pinned post "the tested route" and
the channel pin calls the beta release "the safe route — pinned in the how-to
forum". Both are true if that post already names `#beta` and not otherwise, and
this project has no view of Discord to tell which. Recorded in `INBOX/sent.md`
against both lines.
