#!/usr/bin/env python3
"""Fixture suite for the queue lint's never-fired flags.

Run: py resources/testing/test_queue_lint_flags.py
(Plain script, never pytest — see CLAUDE.md's scripting constraints.)

Why a fixture rather than an observation. Only the blocked-by flag has ever
fired in practice, because the real queue has never contained the other faults:
a work-item heading with no slug, a missing section heading, a red-flag state
that is neither cleared nor uncleared, and prose sitting under no work item.
Exercising those means writing bad queue lines on purpose. An unexercised check
is not a passing check — it is a check nobody has ever seen work.

One correction to the item that asked for this. It listed "missing provenance"
as a fourth lint flag. There is no such check and there should not be:
provenance is a prose convention, and the rules state explicitly that it is not
a lint-checked field. Orphaned prose is the fourth check that had never fired,
so it is what this suite covers in its place.
"""

import importlib.util
import os
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

HOOK = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "plugin", "throughliner", "hooks", "post_tool_use.py",
)

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else f" — {detail}"))
    if not ok:
        failures.append(label)


def load_lint():
    spec = importlib.util.spec_from_file_location("post_tool_use", HOOK)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.lint


CLEAN = """# QUEUE

## Processed

#### A perfectly ordinary work item [alpha]
Filed by Claude. Rationale for alpha.

--- Cleared to run above this line ---

## Unprocessed

#### Another ordinary work item [beta]
Filed by Claude. Rationale for beta.
"""


def test_clean_queue_is_silent():
    """The control. A suite that fires on correct input proves nothing."""
    lint = load_lint()
    warnings = lint(CLEAN)
    check("a well-formed queue produces no warnings", not warnings,
          f"got: {warnings}")


def test_slugless_heading_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("#### A perfectly ordinary work item [alpha]",
                        "#### A work item nobody gave a slug")
    warnings = lint(bad)
    hit = any("no [slug]" in w for w in warnings)
    check("a heading with no slug is flagged", hit, f"got: {warnings}")


def test_missing_section_heading_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("## Unprocessed\n", "")
    warnings = lint(bad)
    hit = any("Unprocessed' section heading is missing" in w for w in warnings)
    check("a missing section heading is flagged", hit, f"got: {warnings}")


def test_invalid_red_flag_state_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("Rationale for beta.",
                        "Rationale for beta.\nRed flag · State: probably fine")
    warnings = lint(bad)
    hit = any("cleared / uncleared" in w for w in warnings)
    check("a red-flag state outside cleared/uncleared is flagged", hit,
          f"got: {warnings}")


def test_valid_red_flag_states_are_not_flagged():
    """The other half of the same check — it must not fire on correct markers."""
    lint = load_lint()
    for state in ("cleared", "uncleared"):
        ok = CLEAN.replace("Rationale for beta.",
                           f"Rationale for beta.\nRed flag · State: {state}")
        warnings = [w for w in lint(ok) if "cleared / uncleared" in w]
        check(f"'{state}' is accepted as a red-flag state", not warnings,
              f"got: {warnings}")


def test_orphaned_prose_is_flagged():
    lint = load_lint()
    bad = CLEAN.replace("## Processed\n",
                        "## Processed\n\nProse belonging to no work item.\n")
    warnings = lint(bad)
    hit = any("no #### heading" in w or "belongs to no work item" in w
              for w in warnings)
    check("prose under no work item is flagged", hit, f"got: {warnings}")


HELD = CLEAN.replace(
    "## Unprocessed",
    "#### A held item [gamma]\nRationale for gamma.\n{hold}\n\n## Unprocessed",
)


def test_date_held_item_needs_no_blocker():
    """A `Not before:` date holds an item on its own.

    It is the one holding fact that resolves itself — no session and no user
    confirms that a day has passed — so it needs no blocker item standing in
    for it.
    """
    lint = load_lint()
    warnings = lint(HELD.format(hold="Not before: 2099-01-01"))
    hit = [w for w in warnings if "gamma" in w or "Not before" in w]
    check("a date-held item is not flagged for missing a blocker", not hit,
          f"got: {warnings}")


def test_held_item_with_neither_is_flagged():
    lint = load_lint()
    warnings = lint(HELD.format(hold="Waiting for a bit."))
    hit = any("Not before" in w and "Blocked by" in w for w in warnings)
    check("a held item with no blocker and no date is flagged", hit,
          f"got: {warnings}")


def test_malformed_date_is_flagged():
    lint = load_lint()
    warnings = lint(HELD.format(hold="Not before: next Tuesday"))
    hit = any("not a date in YYYY-MM-DD form" in w for w in warnings)
    check("a date nobody can read is flagged", hit, f"got: {warnings}")


def test_date_above_the_line_is_flagged():
    """Cleared work has nothing holding it, a date included."""
    lint = load_lint()
    bad = CLEAN.replace("Filed by Claude. Rationale for alpha.",
                        "Filed by Claude. Rationale for alpha.\n"
                        "Not before: 2099-01-01")
    warnings = lint(bad)
    hit = any("sits ABOVE" in w and "Not before" in w for w in warnings)
    check("a date on a cleared item is flagged", hit, f"got: {warnings}")


def test_credit_without_a_quote_is_flagged():
    """A credit to the user rests on words they actually said.

    The check cannot tell invented reasoning from real reasoning and is not
    described as if it could. What it does is make an unsupported credit
    visible, raising its cost from nothing to fabricating a quotation.
    """
    lint = load_lint()
    bad = CLEAN.replace("Filed by Claude. Rationale for alpha.",
                        "Captured by you 2026-08-15, in your own words: you "
                        "wanted this done differently.")
    warnings = lint(bad)
    hit = any("quotes nothing" in w for w in warnings)
    check("a user credit with no quotation is flagged", hit, f"got: {warnings}")


def test_credit_with_a_quote_is_not_flagged():
    lint = load_lint()
    for quoted in ('"do it the other way"', '“do it the other way”'):
        ok = CLEAN.replace(
            "Filed by Claude. Rationale for alpha.",
            f"Captured by you 2026-08-15, in your own words: {quoted}.")
        warnings = [w for w in lint(ok) if "quotes nothing" in w]
        check(f"a credit quoting {quoted[:1]}…{quoted[-1:]} is accepted",
              not warnings, f"got: {warnings}")


def test_blockquote_counts_as_showing_the_words():
    lint = load_lint()
    ok = CLEAN.replace(
        "Filed by Claude. Rationale for alpha.",
        "Captured by you, in your own words:\n> do it the other way")
    warnings = [w for w in lint(ok) if "quotes nothing" in w]
    check("a blockquote counts as quoting them", not warnings,
          f"got: {warnings}")


def test_uncredited_item_is_not_asked_for_a_quote():
    """The other half — an unmarked item reads as Claude's and owes nothing."""
    lint = load_lint()
    warnings = [w for w in lint(CLEAN) if "quotes nothing" in w]
    check("an unmarked item is never asked to quote anyone", not warnings,
          f"got: {warnings}")


def test_growth_reports_a_delta_per_edited_item():
    """Word growth is a bare fact per item, with no threshold anywhere.

    Driven through the module's own counter rather than a git repository, so
    the case pins the arithmetic and the shape. The git baseline degrades to
    nothing when there is no repository, which is why the report can be absent
    without being wrong.
    """
    import importlib.util

    spec = importlib.util.spec_from_file_location("post_tool_use", HOOK)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    before = mod._item_word_counts(CLEAN)
    grown = CLEAN.replace("Rationale for alpha.",
                          "Rationale for alpha, now with five extra words.")
    after = mod._item_word_counts(grown)
    check("an edited item's word count rises", after["alpha"] > before["alpha"],
          f"{before.get('alpha')} -> {after.get('alpha')}")
    check("an untouched item's count is unchanged",
          after["beta"] == before["beta"],
          f"{before.get('beta')} -> {after.get('beta')}")


if __name__ == "__main__":
    print("test_queue_lint_flags")
    test_clean_queue_is_silent()
    test_slugless_heading_is_flagged()
    test_missing_section_heading_is_flagged()
    test_invalid_red_flag_state_is_flagged()
    test_valid_red_flag_states_are_not_flagged()
    test_orphaned_prose_is_flagged()
    test_date_held_item_needs_no_blocker()
    test_held_item_with_neither_is_flagged()
    test_malformed_date_is_flagged()
    test_date_above_the_line_is_flagged()
    test_credit_without_a_quote_is_flagged()
    test_credit_with_a_quote_is_not_flagged()
    test_blockquote_counts_as_showing_the_words()
    test_uncredited_item_is_not_asked_for_a_quote()
    test_growth_reports_a_delta_per_edited_item()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
