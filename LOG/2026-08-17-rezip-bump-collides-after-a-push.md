# dc52025 — the rezip reads its next test number from the installed builds instead of from plugin.json

Settled from the user's observation that the rezip and push had been getting steadily more complex, and that tying them together was a habit of hers rather than a requirement. She now rezips at every /next run, so a per-rezip judgment is paid constantly rather than occasionally.

Claude's first hypothesis was checked and was wrong. The `-testN` suffix is not a label that could simply be dropped: the update command matches on the version string, so an unchanged version reports "already at the latest" and re-snapshots nothing. The bump is what forces the install.

The real cause is the coupling she named. The push strips the suffix, so the next rezip sees a clean base and has to decide whether to restart at `-test1` or continue; getting it wrong installs nothing; and the file sits dirty in between, which every close then has to explain away. One coupling, three consequences.

So step 1 reads the highest test build present in the plugin cache and adds one, and the start-at-`-test1` branch is deleted rather than patched — it is the branch that misfires, and with the cache as the source there is nothing for it to do. Both recorded misfires were avoided only by listing the cache, which nothing in the ritual asked for; writing that in is the whole fix.

Full decoupling — stripping at the release instead of the push — was refused, because the committed version would then carry a test suffix between releases, and that reaching the public remote has happened once and was treated as a defect.

Rule gate: run — a rewording of an existing step. The eviction is the start-at-`-test1` branch.

**Queue changes:** [rezip-bump-collides-after-a-push] kept into Processed, cleared to run.
**Work processed:** kept — [rezip-bump-collides-after-a-push].
