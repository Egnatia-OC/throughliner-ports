# d82f538 — The rezip's version bump gets one permitted path on the planning standing list

The rezip's first step is bumping the `-testN` suffix in the plugin's version manifest, and that write was denied outright. The close deletes the build working file, `pre_tool_use` classifies any chat without one as planning, and the manifest is not on the planning standing list. Since the rezip is *defined* to run after a close, **there was no chat shape in which its own first step was permitted** — the `-testN` history proves it used to work, which means earlier rezips happened while a build working file still existed.

The fix is one path added to the list that already enumerates what a planning chat may write. **No marker and no class-wide exemption**, both refused on the record. The `/setup` marker is a full bypass a session declares for itself — proportionate for migration writes that are genuinely unbounded, disproportionate for one field in one file, and weaker than an ask because nobody sees it. The broader reading, that the deny is wrong for host-only maintenance rituals as a class, was refused too: two of its three instances are already fixed by other means and the third is one line, so a class exemption would trade a precise fix for a broad one in the mechanism the user had just spent weeks arguing back into place.

**Why widening the list is safe here when it was not for /setup.** That objection was that widening opens a shipped file to every planning chat in every consumer project. `plugin/throughliner/` exists only in this repository, so the permission is a no-op everywhere else. The cost is exactly that a planning chat in this repo may edit one version field.

**The suite caught a real defect in the first attempt, which is why it was written first.** The initial comparison used `os.path.normcase` on a multi-component literal — and on Windows that rewrites `/` as `\`, while the relative path being compared carries forward slashes. The permission was inert: it looked correct and could never match. The single-component literals elsewhere in the function escape this because they contain no separator. The new test case is what exposed it, and a comment now states why the separator normalisation is load-bearing.

Depth: full — the reasoning was contested by measurement: a change that read correctly did nothing at all.

Rule gate: run — admitted as one path added to `pre_tool_use.py`'s existing standing list; no new mechanism, no marker, no always-loaded rule. Nothing evicted, and two alternatives refused outright. Failure evidence is one reported instance with a repro, in a ritual that had no permitted path at all.

FAQ: not needed — the permitted path does not exist in a consumer project.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `resources/testing/test_plan_quiet_list.py`.

**Routed to Captures:** none from this item.
