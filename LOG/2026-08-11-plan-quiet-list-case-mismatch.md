# 08c885b — The planning quiet list fixed: it was case-inverted on Windows and had never matched once

The user reported constantly getting a permission dialog while in auto mode, and supplied a screenshot showing the hook naming QUEUE.md as outside a list that contains QUEUE.md. The diagnosis and the fix are Claude's.

`_is_plan_quiet_path` built its relative path with `_normalise`, which calls `os.path.normcase` — a lowercaser on Windows and the identity function on POSIX. So `rel` arrived as `queue.md` and was then compared against the literal `"QUEUE.md"`. That comparison could never be true. The gate whose entire purpose is that a planning session's own working surface passes **silently** was therefore asking on every single write to QUEUE.md, SPEC.md and LOG/ — and doing it in auto mode, where the user has already said they don't want to be asked.

The fix builds the relative path from paths that have **not** been normcased, and normcases each side of the comparison instead. `os.path.relpath` compares case-insensitively internally on Windows while returning the original components, so passing raw paths is safe; `normcase` is the identity on POSIX, so exact matching is preserved there. A comment records why, because the old shape looks correct at a glance — which is most of why it survived.

**Why it shipped and why nobody saw it.** On macOS and Linux the list matched and the gate behaved exactly as designed. The failure existed only on Windows, which is the platform every user of this project is on and the platform the method is developed on. A POSIX-only test would have passed throughout.

The regression suite is therefore built around mixed-case paths, since the whole class of defect is invisible without one. Thirteen cases, four of them Windows-specific: an all-lowercase absolute path, an all-uppercase one, a lowercased `LOG` folder, and a negative case pinning that case-insensitivity must not widen the list to files that aren't on it.

Verified against the real project paths before and after, not reasoned from the source.

**Files touched:**
- `plugin/si-plugin/hooks/pre_tool_use.py` — `_is_plan_quiet_path` rewritten as above, with the reasoning in a comment.
- `resources/testing/test_plan_quiet_list.py` — new, 13 cases, all passing. Host-only dev artifact.

**Routed to Captures:** none.

FAQ: not needed because nothing user-facing changed — the gate's visible behaviour returns to what the FAQ already describes, and the defect was that it never worked.

Note the fix is host-side: the dialogs continue until a rezip.
