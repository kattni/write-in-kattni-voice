"""Generate an essay under each condition the eval compares.

The question this eval answers: does the write-in-kattni-voice skill produce a
closer voice match than a plain prompt? So the conditions are:

* skill            — invoke the skill via `/write-in-kattni-voice`. Skill ON.
* baseline_samples — a standalone prompt that includes the same writing samples
                     the skill draws on, but none of the skill's guidance.
                     Skill OFF.
* baseline_naive   — a standalone prompt that just asks for Kattni's voice, with
                     no samples and no guidance. Skill OFF.

Every condition writes the same topics with the same generation model, so the
skill (and what the prompt carries) is the only thing that varies.
"""
from __future__ import annotations

from model_client import complete

WORD_TARGET = 500

_TASK = (
    f"Write an essay of about {WORD_TARGET} words on this topic:\n\n"
    "    {topic}\n\n"
    "Output only the essay itself."
)

_NAIVE_TEMPLATE = (
    f"Write an essay of about {WORD_TARGET} words, in the writing voice of "
    "Kattni (a developer and technical writer), on this topic:\n\n"
    "    {topic}\n\n"
    "Output only the essay itself."
)

_SAMPLES_TEMPLATE = """\
Below are writing samples from a single author, delimited by <samples> tags.

<samples>
{samples}
</samples>

Write an essay of about {words} words on this topic:

    {topic}

Match the author's style as closely as you can — their tone, sentence rhythm,
vocabulary, and punctuation habits. Do not comment on the style or explain what
you are doing. Output only the essay itself.
"""


def _skill_prompt(topic: str, samples: str) -> str:
    # The slash command loads the skill; the rest is the task it works on.
    return "/write-in-kattni-voice " + _TASK.format(topic=topic)


def _naive_prompt(topic: str, samples: str) -> str:
    return _NAIVE_TEMPLATE.format(topic=topic)


def _samples_prompt(topic: str, samples: str) -> str:
    return _SAMPLES_TEMPLATE.format(samples=samples, topic=topic, words=WORD_TARGET)


# condition -> (prompt builder, whether to disable skills for this run)
_CONDITIONS = {
    "skill": (_skill_prompt, False),
    "baseline_samples": (_samples_prompt, True),
    "baseline_naive": (_naive_prompt, True),
}

# Ordered tuple of condition names, skill first.
CONDITIONS = tuple(_CONDITIONS)


def generate_essay(topic: str, condition: str, samples_text: str, model: str) -> str:
    """Return an essay for ``condition`` (one of CONDITIONS)."""
    try:
        builder, disable_skills = _CONDITIONS[condition]
    except KeyError:
        raise ValueError(f"unknown condition: {condition!r}") from None
    prompt = builder(topic, samples_text)
    return complete(prompt, model=model, disable_skills=disable_skills).strip()
