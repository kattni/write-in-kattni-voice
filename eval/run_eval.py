#!/usr/bin/env python3
"""Style-match eval: does the write-in-kattni-voice skill beat a plain prompt?

This file reads top-to-bottom like a test. For each topic it:

  1. ARRANGE — loads your writing samples from evals/samples/ as the reference
     voice (the target every essay is scored against).
  2. ACT     — generates an essay under three conditions:
       skill            — via `/write-in-kattni-voice` (skill ON)
       baseline_samples — a prompt with your samples but no skill (skill OFF)
       baseline_naive   — a prompt that just asks for your voice (skill OFF)
  3. ASSERT  — scores each essay two independent ways, stylometric (offline) and
     judge (Claude), then reports whether the skill won.

Finally it AGGREGATES across topics: mean score per condition, and how often the
skill beats each baseline. That aggregate is the answer to the question.

No API key needed: generation and judging go through the `claude` CLI you're
already signed in to (see model_client.py).

    python3 evals/run_eval.py            # all topics
    python3 evals/run_eval.py --limit 1  # just the first topic (quick check)

Drop your writing into evals/samples/ as .txt or .md files first.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

import structure
import style
from generate import CONDITIONS, generate_essay
from judge import judge_style
from model_client import ModelError

HERE = Path(__file__).resolve().parent
SAMPLES_DIR = HERE / "samples"
RESULTS_PATH = HERE / "results.json"

# --- knobs ------------------------------------------------------------------
# Each topic is tagged with the skill register it exercises. The topics
# deliberately stay OFF the six sample posts — topic overlap flatters the echo
# baseline (see README "Caveats") — while staying in Kattni's domains: Python,
# open source, tooling, dev life. The "tutorial" tag also triggers the
# teaching-scaffold check (structure.py).
TOPICS = [
    {"topic": "writing your first test with pytest", "register": "tutorial"},
    {"topic": "why good error messages are worth the effort", "register": "opinion"},
    {"topic": "the bug that took me three days to find", "register": "narrative"},
    {"topic": "stepping back from a project you maintained for years", "register": "reflection"},
    {"topic": "the small tools that quietly changed how I work", "register": "personal"},
]
TUTORIAL_REGISTER = "tutorial"
GENERATION_MODEL = "claude-sonnet-5"
JUDGE_MODEL = "claude-opus-5"
# Generations per (topic, condition), averaged. The judge is non-deterministic
# enough (~±1 point on an unchanged baseline, observed run-to-run) that a
# single generation can't tell a small real change from noise; repeats do.
REPEATS = 1

# The skill is the thing under test; the baselines are what we compare it to.
SKILL_CONDITION = "skill"

# What bar the skill must clear against each baseline. baseline_samples is handed
# the exact posts the judge grades against, so "beat it" is the wrong test — its
# honest bar is "match" (tie or within tolerance). baseline_naive is the floor,
# so there the bar is a real "beat".
BASELINE_BARS = {
    "baseline_naive": "beat",
    "baseline_samples": "match",
}
# "Match" tolerance: how far below a baseline still counts as keeping pace.
JUDGE_MATCH_TOL = 1        # judge scores are integers 1..10
STYLO_MATCH_TOL = 0.02     # stylometric similarity is continuous 0..1


def _beats(skill_val: float, other_val: float) -> bool:
    """Strict improvement over a baseline."""
    return skill_val > other_val


def _matches(skill_val: float, other_val: float, tol: float) -> bool:
    """Keeps pace with a baseline: ahead, tied, or within ``tol`` below it."""
    return skill_val >= other_val - tol


def load_samples(directory: Path) -> tuple[str, list[str]]:
    """Concatenate every .txt/.md file in ``directory`` into one reference."""
    files = sorted(p for p in directory.glob("*") if p.suffix.lower() in {".txt", ".md"})
    files = [p for p in files if p.name.lower() != "readme.md"]
    if not files:
        sys.exit(
            f"No sample files found in {directory}.\n"
            "Add your writing as .txt or .md files there, then re-run."
        )
    text = "\n\n".join(p.read_text(encoding="utf-8") for p in files)
    return text, [p.name for p in files]


def _score_one(
    topic: str, condition: str, register: str, samples_text: str, reference: style.Features
) -> dict:
    """Generate one essay and score it against the reference.

    Voice is scored two independent ways (stylometric + judge). For
    tutorial-register topics we also score the teaching scaffold on the *raw*
    essay — the one thing the voice metrics are blind to, since style.py strips
    code and the judge rates style, not structure.
    """
    essay = generate_essay(topic, condition, samples_text, model=GENERATION_MODEL)
    stylo = style.style_similarity(style.extract_features(essay), reference)
    judged = judge_style(samples_text, essay, model=JUDGE_MODEL)
    result = {
        "condition": condition,
        "essay": essay,
        "stylometric_overall": stylo.overall,
        "stylometric": stylo.as_dict(),
        "judge_overall": judged["overall"],
        "essayist_tells": judged["essayist_tells"],
        "judge": judged,
        "tutorial_structure": None,
    }
    if register == TUTORIAL_REGISTER:
        result["tutorial_structure"] = structure.tutorial_structure(essay)
    return result


def score_condition(
    topic: str,
    condition: str,
    register: str,
    samples_text: str,
    reference: style.Features,
    repeats: int,
) -> dict:
    """Generate ``repeats`` essays for this (topic, condition) and average.

    Returns the same shape ``_score_one`` does, plus ``runs`` (every individual
    generation's full result, for inspection) and a ``*_stdev`` alongside each
    averaged score (population stdev; 0.0 when repeats == 1).
    """
    runs = [
        _score_one(topic, condition, register, samples_text, reference)
        for _ in range(repeats)
    ]

    def _avg(key):
        vals = [r[key] for r in runs]
        return statistics.mean(vals), statistics.pstdev(vals)

    stylo_mean, stylo_sd = _avg("stylometric_overall")
    judge_mean, judge_sd = _avg("judge_overall")
    tells_mean, tells_sd = _avg("essayist_tells")

    result = {
        "condition": condition,
        "repeats": repeats,
        "stylometric_overall": stylo_mean,
        "stylometric_overall_stdev": stylo_sd,
        "judge_overall": judge_mean,
        "judge_overall_stdev": judge_sd,
        "essayist_tells": tells_mean,
        "essayist_tells_stdev": tells_sd,
        "tutorial_structure": None,
        "runs": runs,
    }
    if register == TUTORIAL_REGISTER:
        struct_vals = [r["tutorial_structure"]["score"] for r in runs]
        result["tutorial_structure"] = {
            "score": statistics.mean(struct_vals),
            "score_stdev": statistics.pstdev(struct_vals),
        }
    return result


def run_topic(
    entry: dict, samples_text: str, reference: style.Features, repeats: int
) -> dict:
    topic, register = entry["topic"], entry["register"]
    print(f"\n{'=' * 70}\nTOPIC: {topic}  [{register}]\n{'=' * 70}")
    scored = {}
    for condition in CONDITIONS:
        print(f"  generating [{condition}] x{repeats} ...", flush=True)
        result = score_condition(topic, condition, register, samples_text, reference, repeats)
        scored[condition] = result
        line = (
            f"    stylometric {result['stylometric_overall']:.3f}"
            f"±{result['stylometric_overall_stdev']:.3f}   "
            f"judge {result['judge_overall']:.2f}±{result['judge_overall_stdev']:.2f}/10   "
            f"essayist_tells {result['essayist_tells']:.2f}±{result['essayist_tells_stdev']:.2f}/10"
        )
        if result["tutorial_structure"] is not None:
            line += (
                f"   tutorial_structure {result['tutorial_structure']['score']:.2f}"
                f"±{result['tutorial_structure']['score_stdev']:.2f}"
            )
        print(line)
    _print_topic_verdict(scored)
    return {"topic": topic, "register": register, "conditions": scored}


def _print_topic_verdict(scored: dict) -> None:
    skill = scored[SKILL_CONDITION]
    for baseline in (c for c in CONDITIONS if c != SKILL_CONDITION):
        b = scored[baseline]
        bar = BASELINE_BARS.get(baseline, "beat")
        if bar == "beat":
            s_ok = _beats(skill["stylometric_overall"], b["stylometric_overall"])
            j_ok = _beats(skill["judge_overall"], b["judge_overall"])
            s_word, j_word = ("WIN" if s_ok else "no"), ("WIN" if j_ok else "no")
        else:  # match: keeping pace is the win, because samples echoes the key
            s_ok = _matches(skill["stylometric_overall"], b["stylometric_overall"], STYLO_MATCH_TOL)
            j_ok = _matches(skill["judge_overall"], b["judge_overall"], JUDGE_MATCH_TOL)
            s_word, j_word = ("MATCH" if s_ok else "behind"), ("MATCH" if j_ok else "behind")
        print(
            f"    skill vs {baseline} (bar: {bar}): "
            f"stylometric {s_word} "
            f"({skill['stylometric_overall']:.3f} vs {b['stylometric_overall']:.3f}), "
            f"judge {j_word} "
            f"({skill['judge_overall']:.2f} vs {b['judge_overall']:.2f})"
        )


def aggregate(topics: list[dict]) -> None:
    """Mean score per condition, and how the skill fares against each baseline.

    The bar is per-baseline: against baseline_naive (the floor) it is *beat*;
    against baseline_samples (handed the exact posts the judge grades against)
    the honest bar is *match*. See README "Caveats".
    """
    n = len(topics)
    print(f"\n{'=' * 70}\nAGGREGATE over {n} topic(s)\n{'=' * 70}")

    print(
        f"  {'condition':18s}  {'stylo (mean)':>12s}  {'judge (mean)':>12s}  "
        f"{'essayist (mean)':>15s}"
    )
    for condition in CONDITIONS:
        s_mean = sum(t["conditions"][condition]["stylometric_overall"] for t in topics) / n
        j_mean = sum(t["conditions"][condition]["judge_overall"] for t in topics) / n
        e_mean = sum(t["conditions"][condition]["essayist_tells"] for t in topics) / n
        print(f"  {condition:18s}  {s_mean:12.3f}  {j_mean:12.2f}  {e_mean:15.2f}")

    for baseline in (c for c in CONDITIONS if c != SKILL_CONDITION):
        bar = BASELINE_BARS.get(baseline, "beat")
        skill_ = [t["conditions"][SKILL_CONDITION] for t in topics]
        base_ = [t["conditions"][baseline] for t in topics]
        if bar == "beat":
            s_hits = sum(_beats(s["stylometric_overall"], b["stylometric_overall"])
                         for s, b in zip(skill_, base_))
            j_hits = sum(_beats(s["judge_overall"], b["judge_overall"])
                         for s, b in zip(skill_, base_))
            verb = "beats"
        else:
            s_hits = sum(_matches(s["stylometric_overall"], b["stylometric_overall"], STYLO_MATCH_TOL)
                         for s, b in zip(skill_, base_))
            j_hits = sum(_matches(s["judge_overall"], b["judge_overall"], JUDGE_MATCH_TOL)
                         for s, b in zip(skill_, base_))
            verb = "matches"
        print(
            f"\n  skill {verb} {baseline}:  "
            f"stylometric {s_hits}/{n} topics,  judge {j_hits}/{n} topics"
        )
        if bar == "match":
            print(
                "    (bar is 'match', not 'beat': baseline_samples was handed the "
                "exact\n     posts the judge scores against — see README.)"
            )

    _print_structure_summary(topics)


def _print_structure_summary(topics: list[dict]) -> None:
    """Teaching-scaffold scores, averaged per condition over tutorial topics.

    This is the skill's instructional strength, which the voice metrics can't
    see. Only tutorial-register topics carry a structure score.
    """
    tutorials = [t for t in topics if t["register"] == TUTORIAL_REGISTER]
    if not tutorials:
        return
    print(f"\n  tutorial-structure (mean over {len(tutorials)} tutorial topic(s), 0..1):")
    for condition in CONDITIONS:
        mean = sum(
            t["conditions"][condition]["tutorial_structure"]["score"] for t in tutorials
        ) / len(tutorials)
        print(f"    {condition:18s}  {mean:.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--limit", type=int, default=None,
        help="only run the first N topics (for a quick check)",
    )
    parser.add_argument(
        "--repeats", type=int, default=REPEATS,
        help="generations per (topic, condition), averaged (default: %(default)s)",
    )
    args = parser.parse_args()

    topics = TOPICS[: args.limit] if args.limit else TOPICS
    samples_text, names = load_samples(SAMPLES_DIR)
    reference = style.extract_features(samples_text)

    print(f"Reference voice: {len(names)} sample(s) — {', '.join(names)}")
    print(f"Conditions: {', '.join(CONDITIONS)}")
    print(f"Topics: {len(topics)}   Generation: {GENERATION_MODEL}   Judge: {JUDGE_MODEL}"
          f"   Repeats: {args.repeats}")

    try:
        results = [run_topic(t, samples_text, reference, args.repeats) for t in topics]
    except ModelError as exc:
        sys.exit(
            f"\nModel call failed: {exc}\n\n"
            "This eval reaches Claude through the `claude` CLI (no API key). Make "
            "sure the CLI is signed in for non-interactive use:\n"
            "  - run `claude -p \"hello\"` in your terminal; if it says 'Not "
            "logged in', run `claude setup-token` (Pro/Max) or `claude login`.\n"
            "Then re-run this eval."
        )

    aggregate(results)

    RESULTS_PATH.write_text(
        json.dumps({"topics": results}, indent=2), encoding="utf-8"
    )
    print(f"\nWrote {RESULTS_PATH.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()
