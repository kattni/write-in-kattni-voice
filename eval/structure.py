"""Tutorial-structure signals: does a tutorial-register essay actually teach?

The stylometric and judge scores measure prose *voice*. Both are blind to the
skill's instructional scaffolding: style.py strips code and formatting before
scoring, and the judge rates style, not teaching structure. So an essay can nail
Kattni's voice and still fail to be a usable tutorial — and nothing else in this
eval would notice.

This module scores the teaching scaffold on the RAW essay (markdown and code
intact), for tutorial-register topics only. It is a coarse *presence* check, not
a quality judgment: four independent signal categories, score = fraction present
(0..1). Deterministic and offline, like style.py.
"""
from __future__ import annotations

import re

# A fenced code block — the thing the reader is meant to run or type.
_FENCE_RE = re.compile(r"(?m)^\s{0,3}(?:```|~~~)")

# Verbs that commonly open a tutorial step. Present tense only: `\b` keeps
# "run" from matching past-tense narration like "ran" or "running", so a
# recounting ("I opened the file, I ran the tests") is not mistaken for steps.
_IMPERATIVE_VERBS = (
    "install", "open", "run", "create", "add", "save", "import", "type",
    "click", "connect", "plug", "download", "copy", "paste", "edit", "set",
    "define", "write", "call", "press", "navigate", "enter", "select",
    "replace", "build", "start",
)
# An imperative verb at a step boundary: start of a line, or the start of a new
# sentence mid-line. List/number markers before the verb are allowed.
_IMPERATIVE_RE = re.compile(
    r"(?im)(?:^|[.!?]\s+)[\s>*\-\d.]*(" + "|".join(_IMPERATIVE_VERBS) + r")\b"
)
_NUMBERED_RE = re.compile(r"(?m)^\s*\d+\.\s+\S")

# Language that tells the reader what they should see when it works.
_EXPECTED_OUTPUT_PHRASES = (
    "you should see", "you'll see", "you will see", "you should get",
    "you should now", "you'll get", "expected output", "the output",
    "outputs", "prints", "printed", "displays", "the result is", "it returns",
)

# An invitation to change something and observe — the "now make it yours" move.
_EXPERIMENT_PHRASES = (
    "try changing", "try swapping", "try adjusting", "try replacing",
    "try modifying", "try running", "experiment with", "play with", "tweak",
    "swap out", "change the", "try it with",
)


def tutorial_structure(essay: str) -> dict:
    """Score the teaching scaffold in a raw (un-normalized) essay.

    Returns ``{"score": float, "signals": {name: bool, ...}}`` where ``score``
    is the fraction of the four signal categories present.
    """
    lower = essay.lower()

    signals = {
        "code_block": bool(_FENCE_RE.search(essay)),
        "steps": bool(_NUMBERED_RE.search(essay)) or len(_IMPERATIVE_RE.findall(essay)) >= 2,
        "expected_output": any(p in lower for p in _EXPECTED_OUTPUT_PHRASES),
        "invite_experiment": any(p in lower for p in _EXPERIMENT_PHRASES),
    }
    score = sum(signals.values()) / len(signals)
    return {"score": score, "signals": signals}
