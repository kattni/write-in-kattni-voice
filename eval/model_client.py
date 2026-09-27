"""The one place this eval talks to a model.

No API key required: we shell out to the `claude` CLI in headless mode
(`claude -p ... --output-format json`), which authenticates through your
existing Claude Code login. If you later set ANTHROPIC_API_KEY and would rather
call the SDK, this is the only function you need to swap.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

# The `claude` CLI resolves project skills relative to its working directory, so
# run it from the repo root (the parent of evals/) — that is where the
# write-in-kattni-voice skill lives.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent


class ModelError(RuntimeError):
    """Raised when the `claude` CLI is missing, fails, or returns no text."""


def complete(prompt: str, model: str, timeout: int = 300, disable_skills: bool = False) -> str:
    """Send ``prompt`` to ``model`` and return the model's text reply.

    Runs ``claude -p <prompt> --model <model> --output-format json`` and reads
    the ``result`` field out of the JSON envelope the CLI prints.

    ``disable_skills=True`` adds ``--disable-slash-commands``, which turns off
    all skills — including auto-invocation. Use it for the baseline conditions so
    the write-in-kattni-voice skill cannot leak into a run that is meant to be
    skill-free.
    """
    if shutil.which("claude") is None:
        raise ModelError(
            "The `claude` CLI is not on PATH. Install Claude Code and sign in, "
            "or point complete() at the Anthropic SDK instead."
        )

    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "json"]
    if disable_skills:
        cmd.append("--disable-slash-commands")

    proc = subprocess.run(
        cmd,
        cwd=str(_PROJECT_ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if proc.returncode != 0:
        raise ModelError(
            f"`claude` exited {proc.returncode}: {proc.stderr.strip() or proc.stdout.strip()}"
        )

    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise ModelError(
            f"Could not parse `claude` output as JSON: {exc}\n---\n{proc.stdout[:500]}"
        ) from exc

    if envelope.get("is_error"):
        raise ModelError(f"`claude` reported an error: {envelope.get('result')}")

    result = envelope.get("result")
    if not isinstance(result, str) or not result.strip():
        raise ModelError(f"No text result in `claude` output: {envelope}")

    return result
