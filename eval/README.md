# Voice-match eval: skill vs. plain prompt

Does the `write-in-kattni-voice` skill produce a closer match to Kattni's
writing voice than a plain prompt does? This eval answers that by generating
essays three ways and scoring each against a reference set of Kattni's own
writing.

## The three conditions

For each topic, one essay is generated under each condition (same generation
model throughout, so the only variable is the prompt/skill):

| Condition | What it is | Skill |
|---|---|---|
| `skill` | `/write-in-kattni-voice <task>` | **on** |
| `baseline_samples` | a prompt containing the same writing samples, but none of the skill's guidance | off |
| `baseline_naive` | a prompt that just asks for "Kattni's voice," no samples | off |

`baseline_samples` isolates the skill's *guidance* (does the distilled advice
keep pace with just handing the model samples?). `baseline_naive` is the floor
(the model otherwise doesn't know the voice).

**The bar against `baseline_samples` is *match*, not beat.** It receives the
exact reference posts in its prompt, and the judge is shown those same posts as
the reference — so it is scoring against text it was handed. Asking the skill to
*beat* that echo isn't fair; the honest question is whether the distilled
guidance keeps pace with it while comfortably beating the naive floor. The
scoreboard reflects this: a win-rate against naive, a match-rate against samples.

## How to run

```bash
python3 eval/run_eval.py            # all topics
python3 eval/run_eval.py --limit 1  # just the first topic (quick check)
```

**No API key needed.** Generation and judging go through the `claude` CLI you're
already signed in to (see `model_client.py`). If a call reports "Not logged in,"
run `claude setup-token` (Pro/Max) or `claude login` and re-run.

Put your reference writing in `samples/` as `.txt`/`.md` files first.

## How scoring works (hybrid)

Each essay is scored against the reference two independent ways:

1. **Stylometric** (`style.py`) — deterministic, offline. Markdown is normalized
   to prose first (bullets, code, links removed) so formatting can't masquerade
   as style. Then it measures sentence rhythm, word length, lexical diversity,
   readability, function-word frequencies, and punctuation habits, and reduces
   the comparison to a 0–1 similarity. Function words are half the score;
   punctuation habits are weighted up within the other half, because they're a
   defining tell.
2. **Judge** (`judge.py`) — Claude rates the style match on a rubric (tone,
   rhythm, vocabulary, punctuation, **essayist_tells**, overall) from 1–10.
   Catches nuance the numbers miss. `essayist_tells` tracks the one failure the
   judge named on every run: the model drifting into a polished opinion-essayist
   voice — aphoristic closers, fragment-punchlines, rhetorical-question hooks,
   lyrical endings, bolded slogans — instead of Kattni's plain, first-person
   practitioner voice. 10 = none of those tells; 1 = saturated with them (higher
   is better, same as every other dimension).

They can disagree; that's the point of having both.

### Tutorial-structure check (tutorial topics only)

The two scores above measure prose *voice*. Both are blind to the skill's
teaching scaffold: `style.py` strips code before scoring and the judge rates
style, not structure. So for tutorial-register topics, `structure.py` adds a
third, deterministic score computed on the **raw** essay — the fraction of four
teaching signals present: a runnable code block, sequential/imperative steps,
expected-output language ("you should see", "prints"), and an invitation to
experiment ("try changing…"). It scores the instructional value the voice
metrics can't see. It does not feed the voice verdict; it's reported on its own.

### Note on the em-dash tell

Kattni's real prose uses **zero true em-dashes** (`—`). A generic model prompt
sprinkles them liberally — the classic "AI writing" signature — so em-dash rate
is one of the sharpest discriminators here. `dash_rate` deliberately counts only
`—`/`–`, **not** `--` (command-line flags in technical prose) or ` - `
(hyphens/ranges), which would otherwise drown out the signal.

## Reading the output

Per topic you get each condition's stylometric, judge, and `essayist_tells`
scores (plus a tutorial-structure score for tutorial topics), then a head-to-head
verdict — a *win* against the naive floor, a *match* against the samples echo. At
the end, an **aggregate** shows the mean of each score per condition, the skill's
win-rate against naive and match-rate against samples, and the mean
tutorial-structure score. Full detail (including every generated essay) is
written to `results.json`.

## Caveats

- **The samples echo the answer key.** `baseline_samples` is handed the exact
  reference posts, and the judge grades every essay against those same posts — so
  it's scoring text it was given. That's a bar the skill isn't meant to *beat*,
  only *match* (see "The three conditions"); the verdict reflects this.
- **Topics stay off the corpus.** The topics avoid the six sample posts'
  subjects, so the echo baseline can't win on shared subject matter. (The skill
  still reads its own `examples/`, some of which are these reference posts — that
  can flatter the `skill` condition slightly, more on stylometrics than judge.)
- **Small N.** A handful of topics is a signal, not proof. The judge is
  non-deterministic; re-runs will vary a little.
- **Prose only for voice.** Code blocks are stripped before *voice* scoring, so
  the stylometric and judge scores measure prose voice, not tutorial formatting.
  The tutorial-structure check scores that formatting separately.

## Knobs (top of `run_eval.py`)

- `TOPICS` — the essay prompts, each tagged with a register; the `tutorial` tag
  also triggers the teaching-scaffold check. Kept off the sample-post subjects.
- `BASELINE_BARS` / `JUDGE_MATCH_TOL` / `STYLO_MATCH_TOL` — the per-baseline bar
  (beat vs match) and how close still counts as a match.
- `GENERATION_MODEL` / `JUDGE_MODEL`.
- `REPEATS` (or `--repeats N`) — generations per (topic, condition), averaged.
  The judge is noisy enough (~±1 point run-to-run on an unchanged baseline,
  observed in practice) that `REPEATS=1` can't tell a small real change from
  noise; each topic's printed line shows `±stdev` so you can see the spread.
- Punctuation weighting lives in `_SCALAR_WEIGHTS` in `style.py`; the teaching
  signals live in `structure.py`.
