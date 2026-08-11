#!/usr/bin/env python3
"""The rule-lifecycle status board — five independent signals, computed.

Host-only. This lives in resources/ rather than the plugin's scripts/ folder
because consumers never author method rules, so the whole lifecycle would
misfire for them. The session-start surface that carries the output DOES ship;
it stays silent when this file is absent, which is the two-doors pattern.

## What this is, and what it is not

It is NOT a cycle. That was the design's first decision: a positional cycle —
one stage following another — is what failed before, because compression ended
up permanently downstream of machinery that never ran. These are five
independent mechanisms, each firing on its own trigger whether or not any other
ran, and what a session reads at start is which of them are currently
signalling. A board, not a position.

Nothing here is stored. The board is recomputed from the artifacts every time,
because a state file must be maintained and the first session that forgets to
update it makes the board lie. The one exception is the retired-terms list,
which is source data — a recorded event, authored once — not derived state.

## The five signals

MEASURED   a structural rule-statement count across the always-loaded files,
           against the 150-200 instruction ceiling.
AUDITED    fires when MEASURED is over the ceiling. Not downstream of MEASURED
           *completing* — both read the same computed number independently.
BORN       LOG entries that should carry a gate-disposition line and do not,
           matched against commits touching the rule-bearing file set.
MAINTAINED near-duplicate rule statements across the corpus. This is
           codification — one subject, one rule, stated once.
REPEALED   live rules naming a term on the retired list.

## What a signal does

It files a capture, once, and gets out of the way. It does not escalate (that
would need a bare number) and it does not go quiet on a standing signal (that
recreates the silent inaction the whole design exists to prevent). The work
goes where all work goes — the queue — where ignoring it is visible.

A signal counts as satisfied while an open capture with its slug exists, which
is the guard against filing the same capture every session.

Usage:
    python resources/rule_signals.py [project root]
"""

import os
import re
import subprocess
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass


# --- Configuration ------------------------------------------------------

# The always-loaded corpus: what every session pays for, in every session.
# MEASURED counts only these. Fetched docs cost nothing until opened and are
# deliberately out of scope — capping them would guard a cost the ceiling
# does not count.
ALWAYS_LOADED = [
    "plugin/si-plugin/docs-b/skill-nonspecific-rules.md",
]

# Files where a method rule can be born. A commit touching one of these is
# BORN's trigger — mechanical, with no judgment involved, which is what makes
# this stage buildable at all.
RULE_BEARING = [
    "plugin/si-plugin/docs-b/",
    "resources/self-authoring-rules.md",
    "resources/rule-maintenance.md",
    "CLAUDE.md",
]

RETIRED_TERMS_FILE = "resources/retired-terms.md"

# The ceiling, in the proxy's own units. The research figure is 150-200
# *instructions*; this is a structural proxy for them, so the ceiling is
# re-expressed here rather than reused raw. See calibrate() for the derivation
# and CEILING_NOTE for what it rests on.
#
# Derivation: the 2026-08-09 hand count of the always-loaded corpus came to
# ~218 instructions against a 150-200 ceiling, i.e. roughly 9-33% over. The
# proxy is calibrated so that the corpus as it stood then reads as over. A
# proxy consistently off by a fixed factor is fine; what would not work is a
# measure that is sometimes exact and sometimes not.
CEILING = 200

CEILING_NOTE = (
    "The 150-200 figure is from research on instruction-following, recorded in "
    "resources/research/instruction-file-bloat-and-subtraction.md. This script "
    "counts a structural proxy for an instruction, not instructions themselves. "
    "The proxy is the right shape because it moves when the corpus grows, holds "
    "still when it does not, and falls when rules are consolidated — which is "
    "exactly what the eviction techniques are for."
)

# A structural rule-statement: a bullet, a bolded lead-in, or a line inside a
# typed block. Counted by structure, never by judgment.
BULLET_RE = re.compile(r"^\s*[-*]\s+\S")
BOLD_LEAD_RE = re.compile(r"^\*\*[^*]+\*\*")
FENCE_RE = re.compile(r"^\s*```")


# --- MEASURED -----------------------------------------------------------

def count_statements(root):
    """Structural rule-statements across the always-loaded corpus."""
    total = 0
    per_file = {}
    for rel in ALWAYS_LOADED:
        path = os.path.join(root, rel)
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except OSError:
            continue
        count = 0
        in_fence = False
        for raw in lines:
            if FENCE_RE.match(raw):
                in_fence = not in_fence
                continue
            if in_fence:
                # A line inside a typed block carries a rule as surely as a
                # bullet does — the blocks are where this docset puts
                # structure. Blank and comment-only lines do not.
                stripped = raw.strip()
                if stripped and not stripped.startswith("#"):
                    count += 1
                continue
            if BULLET_RE.match(raw) or BOLD_LEAD_RE.match(raw.strip()):
                count += 1
        per_file[rel] = count
        total += count
    return total, per_file


def signal_measured(root):
    total, per_file = count_statements(root)
    over = total > CEILING
    detail = ", ".join(f"{k.split('/')[-1]}: {v}" for k, v in per_file.items())
    return {
        "stage": "MEASURED",
        "firing": over,
        "value": total,
        "slug": "rule-corpus-over-ceiling",
        "message": (
            f"Always-loaded rule-statement count is {total} against a ceiling of "
            f"{CEILING} ({detail}). {'OVER — eviction is due.' if over else 'Within the ceiling.'}"
        ),
    }


# --- AUDITED ------------------------------------------------------------

def signal_audited(root, measured):
    """Fires on the same number MEASURED reads, computed independently.

    Sharing an input is not the dependency the design forbids — being gated on
    another stage having finished is. If MEASURED were deleted, this would
    compute the number itself.
    """
    total, _ = count_statements(root)
    return {
        "stage": "AUDITED",
        "firing": total > CEILING,
        "value": total,
        "slug": "three-lens-compliance-sweep-due",
        "message": (
            "The corpus is over the ceiling, so the three-lens compliance sweep "
            "in resources/method-compliance-audit-checklist.md is due."
            if total > CEILING else
            "Corpus within the ceiling; no sweep due. Note the known gap: drift "
            "that is not growth goes uncaught here and is MAINTAINED's job."
        ),
    }


# --- BORN ---------------------------------------------------------------

DISPOSITION_RE = re.compile(r"^Rule gate:", re.IGNORECASE | re.MULTILINE)


def signal_born(root):
    """LOG entries that should carry a gate-disposition line and do not.

    Over-fires by design: touching docs-b/ for a typo is not authoring a rule.
    A false fire costs one line — "not needed, typo fix". FAQ-sync makes
    exactly this trade and it is why it works.
    """
    try:
        out = subprocess.run(
            ["git", "log", "-30", "--format=%H%x00%s", "--name-only"],
            cwd=root, capture_output=True, text=True, timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return {"stage": "BORN", "firing": False, "value": 0,
                "slug": "rule-gate-dispositions-missing",
                "message": "git unavailable; BORN not computed."}
    if out.returncode != 0:
        return {"stage": "BORN", "firing": False, "value": 0,
                "slug": "rule-gate-dispositions-missing",
                "message": "git log failed; BORN not computed."}

    touching = []
    current = None
    for line in out.stdout.splitlines():
        if "\x00" in line:
            sha, subject = line.split("\x00", 1)
            current = {"sha": sha[:7], "subject": subject, "hits": False}
            touching.append(current)
        elif line.strip() and current is not None:
            if any(line.startswith(p) for p in RULE_BEARING):
                current["hits"] = True

    rule_commits = [c for c in touching if c["hits"]]

    # A commit is satisfied when some LOG entry carries a disposition line
    # naming it, or when the entry for it carries one at all. Entries are
    # matched by the commit hash they record.
    log_dir = os.path.join(root, "LOG")
    dispositions = set()
    if os.path.isdir(log_dir):
        for name in os.listdir(log_dir):
            if not name.endswith(".md"):
                continue
            try:
                with open(os.path.join(log_dir, name), "r", encoding="utf-8") as f:
                    text = f.read()
            except OSError:
                continue
            if DISPOSITION_RE.search(text):
                for sha in re.findall(r"\b([0-9a-f]{7,40})\b", text):
                    dispositions.add(sha[:7])

    missing = [c for c in rule_commits if c["sha"] not in dispositions]
    return {
        "stage": "BORN",
        "firing": bool(missing),
        "value": len(missing),
        "slug": "rule-gate-dispositions-missing",
        "message": (
            f"{len(missing)} of the last {len(rule_commits)} commits touching "
            "rule-bearing files have no 'Rule gate:' disposition line in any LOG "
            "entry: " + ", ".join(f"{c['sha']}" for c in missing[:8])
            if missing else
            f"All {len(rule_commits)} recent rule-bearing commits carry a gate disposition."
        ),
    }


# --- MAINTAINED ---------------------------------------------------------

def _normalise_statement(line):
    text = re.sub(r"[*`_\[\]]", "", line).strip().lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return " ".join(text.split())


def signal_maintained(root, threshold=0.82):
    """Near-duplicate rule statements across the always-loaded corpus.

    This IS codification — one subject, one rule, stated once — which is the
    eviction technique the authoring gate never absorbed. It catches drift
    that is not growth, which is precisely the hole AUDITED's ceiling trigger
    leaves open.

    Flags for a human to judge, never a gate: two rules may legitimately say
    similar things in different contexts.
    """
    statements = []
    for rel in ALWAYS_LOADED:
        path = os.path.join(root, rel)
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except OSError:
            continue
        for n, raw in enumerate(lines, 1):
            if BULLET_RE.match(raw) or BOLD_LEAD_RE.match(raw.strip()):
                norm = _normalise_statement(raw)
                if len(norm.split()) >= 6:
                    statements.append((rel, n, norm))

    pairs = []
    for i in range(len(statements)):
        _, ln_i, a = statements[i]
        words_a = set(a.split())
        for j in range(i + 1, len(statements)):
            _, ln_j, b = statements[j]
            words_b = set(b.split())
            union = words_a | words_b
            if not union:
                continue
            score = len(words_a & words_b) / len(union)
            if score >= threshold:
                pairs.append((ln_i, ln_j, round(score, 2)))

    return {
        "stage": "MAINTAINED",
        "firing": bool(pairs),
        "value": len(pairs),
        "slug": "near-duplicate-rule-statements",
        "message": (
            f"{len(pairs)} near-duplicate rule statement pair(s): "
            + "; ".join(f"lines {a}~{b} ({s})" for a, b, s in pairs[:8])
            if pairs else "No near-duplicate rule statements found."
        ),
    }


# --- REPEALED -----------------------------------------------------------

def load_retired_terms(root):
    """Terms recorded as retired. Source data, not derived state."""
    path = os.path.join(root, RETIRED_TERMS_FILE)
    terms = []
    # Only read under the "## The list" heading. The file explains its own
    # format above that point, and the format example is a line of exactly the
    # shape the parser matches — which on the first run loaded the literal word
    # "term" as a retired term and flagged half the corpus.
    in_list = False
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if re.match(r"^##\s+The list\s*$", line.strip(), re.IGNORECASE):
                    in_list = True
                    continue
                if not in_list:
                    continue
                match = re.match(r"^-\s+`([^`]+)`\s*—\s*(.*)$", line.strip())
                if match:
                    terms.append((match.group(1), match.group(2)))
    except OSError:
        return []
    return terms


# A line that says a term IS retired is correct text, not a stale reference.
# Without this the signal fires on every doc doing the right thing — including
# the rules that record the retirement — which is how a lint becomes noise.
RETIREMENT_CONTEXT = (
    "retired", "retire", "no longer", "is gone", "are gone", "was removed",
    "repealed", "superseded", "deprecated", "stays retired", "never write",
    "don't write", "do not write", "not a", "vestigial",
)


def signal_repealed(root):
    """Live rules naming a term on the retired list.

    This is where the sunset research finally transfers. A sunset clause works
    because inaction repeals; a duty to review fails because inaction is
    silent. Time-based expiry does not transfer here — no calendar pressure,
    and a doc that silently expires is not safe. What transfers is the
    default-state principle: retiring a mechanism automatically puts every
    rule that mentions it into question, and leaving the references standing
    produces a visible signal. No number, no calendar.
    """
    terms = load_retired_terms(root)
    if not terms:
        return {"stage": "REPEALED", "firing": False, "value": 0,
                "slug": "live-rules-name-retired-terms",
                "message": f"No retired-terms list at {RETIRED_TERMS_FILE}."}

    scan_roots = ["plugin/si-plugin", "resources", "FAQ", "CLAUDE.md", "SPEC.md"]
    hits = []
    for rel in scan_roots:
        base = os.path.join(root, rel)
        files = []
        if os.path.isfile(base):
            files = [base]
        else:
            for dirpath, dirnames, filenames in os.walk(base):
                dirnames[:] = [d for d in dirnames if d != "__pycache__"]
                files.extend(
                    os.path.join(dirpath, n) for n in filenames
                    if n.endswith((".md", ".py"))
                )
        for path in files:
            if os.path.abspath(path) == os.path.abspath(
                    os.path.join(root, RETIRED_TERMS_FILE)):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()
            except OSError:
                continue
            rel_path = os.path.relpath(path, root).replace("\\", "/")
            seen = set()
            for n, raw in enumerate(lines, 1):
                low = raw.lower()
                if any(c in low for c in RETIREMENT_CONTEXT):
                    continue
                for term, _why in terms:
                    key = (rel_path, term)
                    if key in seen:
                        continue
                    if term.lower() in low:
                        seen.add(key)
                        hits.append((f"{rel_path}:{n}", term))

    return {
        "stage": "REPEALED",
        "firing": bool(hits),
        "value": len(hits),
        "slug": "live-rules-name-retired-terms",
        "message": (
            f"{len(hits)} live reference(s) to retired terms: "
            + "; ".join(f"{p} names '{t}'" for p, t in hits[:8])
            if hits else "No live references to retired terms."
        ),
    }


# --- Board --------------------------------------------------------------

def board(root):
    measured = signal_measured(root)
    return [
        measured,
        signal_audited(root, measured),
        signal_born(root),
        signal_maintained(root),
        signal_repealed(root),
    ]


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    signals = board(root)
    firing = [s for s in signals if s["firing"]]
    print(f"## Rule-lifecycle board — {len(firing)} of 5 signalling")
    for s in signals:
        mark = "FIRING" if s["firing"] else "ok"
        print(f"- {s['stage']} [{mark}] {s['message']}")
    if firing:
        print()
        print("Each firing signal files one capture in Unprocessed, under the slug "
              "shown below, unless an open capture with that slug already exists:")
        for s in firing:
            print(f"  [{s['slug']}]")
    print()
    print(CEILING_NOTE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
