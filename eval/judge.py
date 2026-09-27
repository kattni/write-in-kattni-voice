"""LLM-as-judge: the second, independent half of the hybrid score.

Ask Claude to rate how closely a candidate essay matches the reference voice,
returning a small rubric as JSON. This catches nuance the deterministic
stylometrics miss (irony, cadence, characteristic moves) at the cost of being
non-deterministic.
"""
from __future__ import annotations

import json
import re

from model_client import complete

# Score direction is uniform: for EVERY key, higher = closer to the author, so
# the aggregate can treat them all the same way. That includes essayist_tells —
# read it as "avoids the essayist tells" (10 = none of them), not "has them".
SCORE_KEYS = (
    "tone", "sentence_rhythm", "vocabulary", "punctuation_habits",
    "essayist_tells", "overall",
)

_JUDGE_TEMPLATE = """\
You are judging how closely a candidate essay matches a reference author's
writing STYLE — not its topic, accuracy, or quality.

Reference writing samples from the author:
<samples>
{samples}
</samples>

Candidate essay:
<candidate>
{essay}
</candidate>

Rate the STYLE match on each dimension from 1 (nothing alike) to 10 (could pass
as the same author):
- tone
- sentence_rhythm
- vocabulary
- punctuation_habits
- essayist_tells: the author writes as a plain, first-person practitioner
  reporting what she did and what happened. Score 10 if the candidate does the
  same and shows NONE of the polished-essayist tells; score 1 if it leans on
  them. The tells are: aphoristic or epigrammatic closing lines, punchy
  sentence-fragment punchlines, rhetorical questions addressed to the reader,
  lyrical or thematic endings, and bolded slogans. (Higher = fewer tells.)
- overall

Respond with ONLY a JSON object, no markdown and no code fences, in exactly this
shape:
{{"tone": <int>, "sentence_rhythm": <int>, "vocabulary": <int>,
 "punctuation_habits": <int>, "essayist_tells": <int>, "overall": <int>,
 "rationale": "<one sentence>"}}
"""


def judge_style(samples_text: str, essay: str, model: str) -> dict:
    """Return the judge's rubric as a dict with SCORE_KEYS plus 'rationale'."""
    prompt = _JUDGE_TEMPLATE.format(samples=samples_text, essay=essay)
    raw = complete(prompt, model=model, disable_skills=True)
    return _parse_scores(raw)


def _parse_scores(raw: str) -> dict:
    """Extract the rubric from the judge's reply.

    Tries strict JSON first. Falls back to a per-key regex so that a rationale
    containing an unescaped quote — which makes the whole object invalid JSON —
    still yields the numeric scores instead of crashing the eval.
    """
    text = raw.strip()
    # Tolerate a ```json ... ``` fence around the object.
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()

    # Fast path: the whole object is valid JSON.
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            data = json.loads(match.group(0))
            scores = {key: int(data[key]) for key in SCORE_KEYS}
            scores["rationale"] = str(data.get("rationale", "")).strip()
            return scores
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            pass  # fall through to the tolerant path

    # Tolerant path: pull each integer score out individually.
    scores = {}
    for key in SCORE_KEYS:
        m = re.search(rf'["\']?{key}["\']?\s*:\s*(\d+)', text)
        if not m:
            raise ValueError(f"could not find score {key!r} in judge output:\n{raw[:500]}")
        scores[key] = int(m.group(1))
    # Rationale: greedy to the last quote before the closing brace, so inner
    # quotes are kept rather than truncating the string.
    r = re.search(r'["\']?rationale["\']?\s*:\s*"(.*)"\s*}', text, re.DOTALL)
    scores["rationale"] = r.group(1).strip() if r else ""
    return scores
