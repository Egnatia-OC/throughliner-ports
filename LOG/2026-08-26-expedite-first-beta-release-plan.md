# 47d8625 — plan — release day settled into a run order: selector decided, fallback named, packaging closed, item rewritten as the release-pick [user] line

Processed at the 2026-08-26 evening planning opening, the /plan that is itself the live test of the test20 rezip. Three open questions on the item were settled with the user, and the item was rewritten down to its remaining job.

**The selector, the user's decision:** each Wednesday's **beta** pick is the most recent rezip labelled stable on the nerds list; the **stable release** is last week's beta promoted after its seven-day soak. This supersedes [weekly-release-cycle]'s newest-rezip-at-least-a-week-old pick — the week-old property moves to the promotion step. The prospective readiness question stays banned: the label was written when the rezip was posted, describing a build that already existed, so the Wednesday turn reads a recorded state. The supersession is written on [weekly-release-cycle] and noted on [beta-tester-pathway].

**Which build releases, the user's decision:** decided at the end of the next build run, not before — test20 is the hoped-for candidate, judged only after this /plan and that /next have run on it; the previously installed rezip (test19) is the named stable fallback, having held up in use. Checked at the opening: no release had run — newest GitHub release v1.20.0, 2026-08-09.

**Packaging, the user's agreement to Claude's recommendation:** no new rezip-packaging machinery — nerds-list entries carry label, version and date, no downloads until a nerd asks for one. The ref-pinned beta branch means the Wednesday pick needs only a commit.

**The chain question closed by the session's lift** of [cycles-due-check-verification] — no repoint needed.

**The item's shape, the user's direction:** `[user]`, not `[freeform]` — freeform implies a run of its own, and the pick belongs at the end of the next build run, in that session. Placed after the two builds and before the release-dependent walk-throughs.

**Queue changes:** item rewritten (−~900 words, history relocated to the two held items and this record), retagged `[user]`, cleared to run mid-list.
**Work processed:** kept — [expedite-first-beta-release].
