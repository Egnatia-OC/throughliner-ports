# [HASH] — The planning opening's mail step now covers the issue channel too, in both directions

Captured from a live instance: an upstream issue this project had filed got a substantive answer that went against our design, and it was found only because the user happened to ask. The mailbox covers project-to-project mail and nothing covers GitHub, which is the one correspondence channel with a return path already in use.

Three open decisions were settled at planning. Shipped rather than host-only, because consumers file issues through the same route and the check degrades silently where `gh` is absent, exactly as the existing feedback route does. "New since last seen" is computed rather than stored: comments dated after the last planning session's record are new, and a surfaced answer files one capture that satisfies the check while it stays open — the same shape the cycles check uses. Planning only, not /next's pre-flight, since this is planning material.

Per the scan-displacement rule it folds into the existing mail step as one correspondence scan rather than standing as a new step, so it displaces nothing and costs one lookup per open outbound issue. The incoming arm came from the user's unification question during processing: where the project has a repository that can receive issues, the same clause surfaces new incoming issues the way mail is surfaced.

Issues stay on GitHub. Nothing is copied into `INBOX/`.

Refused at planning, and recorded so it is not re-proposed: replacing the outbound register with a GitHub query by account. That cannot scope to a project — many projects share one account, and only the per-project register says which project filed which issue, and carries what each issue claimed for the repeal check to grep. The register stays the record; the CLI is the reader. Also refused: host-only scoping, /next's pre-flight, and a state file for last-seen, since a forgotten update makes a state file lie where a computed anchor cannot.

**Files touched:** `plugin/throughliner/docs/plan.md`.
**Routed to Captures:** none.
**Depth:** short.
**Tick:** done, confirmed.
Rule gate: run — an amendment extending plan.md Step 1's mail scan to the issue channel, its named parent; nothing displaced, one clause added to an existing step.
