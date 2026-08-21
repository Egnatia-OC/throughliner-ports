# [HASH] — The digest reads a planning record as work shipped, and the same signal decides what lifts out of the held region

Found while verifying an unrelated placement: the digest reported a newly filed item as citing [setup-migration-gate-is-epoch-3-shaped] and [convert-cleared-items-to-build-blocks] as **shipped**, while both sat cleared and unbuilt a few lines above in the same output.

**The mechanism, read in the code rather than inferred from the symptom.** `queue_digest.py`'s `shipped_slugs()` does one directory listing and matches `<date>-<slug>.md`. Nothing opens the file. Its own docstring calls the result *"slugs whose work shipped"*, which is false for every entry a planning close wrote — because a plan entry splits per item **processed**, settled and correct, so a discussed-and-kept item has a record named after it exactly like a built one.

**Why it is worse than a mislabelled line.** The below-the-line revisit decides what may lift by reading shipped-ness off LOG, and its own rule is right — *"blocker BUILT and VERIFIED per LOG"*. What is wrong is the fact fed to it. An item held against a blocker that was only processed reads as ready to lift, and lifting is a clearing move, so unbuilt work reaches the region /next builds from. That is the failure this queue has recorded four times, arriving through a door nobody was watching. The rule needs no change; the fact does.

**The two kinds are already mechanically distinguishable, which is what makes this fixable without judgment.** Across 747 entries: 541 carry `Files touched:`, written by a build close; 132 carry `Work processed:`, written by a planning close. `Tick:` would be the stronger signal, since it carries built-versus-confirmed and that is exactly what the revisit's rule asks for — but it appears on 23 entries only, being recent, so it cannot classify the history and is not used.

**Reporting both beats suppressing one.** An item leaning on a sibling that was merely agreed has a weaker premise than one leaning on shipped work, and that is worth seeing rather than hiding — the digest's standing posture is to state a fact and never a verdict. So `Cites shipped:` and `Cites processed:` become separate lists.

**What it cannot do, stated because partial coverage read as complete is what this project guards hardest against.** 74 of the 747 entries carry neither marker — chat-level records and older formats. Those are reported as a record found whose kind is unknown, never guessed at.

**This session demonstrates the bug on its own output, which is the strongest evidence available.** The five entries this close writes are named for slugs that were *processed*, not built — including this one and [advisory-step-does-not-fire], both sitting cleared and unbuilt. From the next session's opening they will read as shipped in every digest, and the four items above them in the cleared region will too. The defect is not hypothetical and it is not historical; it is being created by the act of recording it.

**SPEC was rewritten in this session rather than left to the build**, ahead of it, per the rule that a build never writes product truth. The clause asserting that work is *"recognised by its having a session record"* is gone, replaced by one that distinguishes a record of work built from a record of work processed, says why the difference matters, and states that older records are reported unclassified rather than guessed at.

**The ripple was traced by grep rather than written from the discussion.** The repealed claim reached two live sites outside the code: `plan.md` line 225 and the SPEC clause above. The revisit's own table in `plan.md` was excluded by name — its built-and-verified test is correct as written.

**Queue changes:** [log-entry-kind-not-distinguished] filed and kept into Processed, second in the cleared region, with a build block and four refusals recorded. `SPEC.md` edited in-session — the digest paragraph's shipped-ness clause.
**Work processed:** kept — [log-entry-kind-not-distinguished].

Rule gate: run — the disposition was written onto the item at the keep-step. No rule authored or amended; the disposition is a correction to a mechanism plus one repealed sentence, evicted at both live sites where it was stated. Failure evidence is one instance observed directly, plus the consequence for the lift test checked in `plan.md`'s revisit rather than assumed.

FAQ: not needed because nothing a user does changes — the label on a digest line differs and their actions do not.
