"""Stylometric features and a style-similarity score.

Pure Python, no dependencies, no network. Given two texts, quantify how close
their *writing style* is on measurable dimensions and reduce that to a single
0..1 similarity score (1.0 == identical style).

The features here are the classic stylometric signals used in authorship
analysis: sentence-length rhythm, word length, lexical diversity, punctuation
habits, function-word frequencies, and readability. Function-word frequency is
the single most reliable authorship signal (Mosteller & Wallace), so it carries
half the weight of the final score; the measurable scalar features carry the
other half.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from math import sqrt

# The most common English function words. Their *relative frequencies* are a
# fingerprint of an author's voice that is largely independent of topic, which
# is exactly what we want when comparing style rather than subject matter.
FUNCTION_WORDS = [
    "the", "of", "and", "to", "a", "in", "that", "it", "is", "was", "for", "on",
    "with", "as", "be", "at", "by", "this", "had", "not", "are", "but", "from",
    "or", "have", "an", "they", "which", "one", "you", "were", "her", "all",
    "she", "there", "would", "their", "we", "him", "been", "has", "when", "who",
    "will", "more", "no", "if", "out", "so", "up", "its", "about", "into",
    "than", "them", "can", "only", "other", "some", "could", "these", "two",
    "may", "then", "do", "first", "any", "my", "now", "such", "like", "our",
    "over", "me", "even", "most", "made", "after", "also", "did", "many",
    "before", "must", "through", "back", "where", "much", "your", "way", "well",
    "down", "should", "because", "each", "just", "those", "how", "too", "very",
    "make", "still", "see", "own", "here", "between", "both", "being", "under",
    "never", "same", "another", "know", "while", "last", "might", "us", "off",
    "since", "against", "used", "take", "come", "i", "he",
]

_WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
_SENT_RE = re.compile(r"[^.!?]+(?:[.!?]+|$)")
_CONTRACTION_RE = re.compile(r"\b[A-Za-z]+'(?:t|s|re|ve|ll|d|m)\b", re.IGNORECASE)
_VOWEL_GROUP_RE = re.compile(r"[aeiouy]+")

_FIRST_PERSON = {"i", "me", "my", "mine", "myself", "we", "us", "our", "ours", "ourselves"}
_SECOND_PERSON = {"you", "your", "yours", "yourself", "yourselves"}

_EPS = 1e-9


def _normalize_markdown(text: str) -> str:
    """Reduce markdown to plain prose so style is measured on words, not
    formatting. Removes fenced/inline code, headers, list and blockquote
    markers, and link/emphasis syntax. Line-based, so a stray or example
    backtick can't swallow the document the way a greedy regex would.

    The generated essays are prose and your samples are markdown; normalizing
    both the same way is what makes the punctuation features comparable (a `- `
    bullet is not an em dash).
    """
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if re.match(r"\s{0,3}#{1,6}\s", line):  # ATX header
            continue
        line = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", line)  # list marker
        line = re.sub(r"^\s*>\s?", "", line)                # blockquote
        out.append(line)
    t = "\n".join(out)
    t = re.sub(r"`[^`\n]*`", " ", t)                     # inline code
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)     # links/images -> text
    t = re.sub(r"[*_]{1,3}([^*_\n]+)[*_]{1,3}", r"\1", t)  # bold/italic
    return t


def _syllables(word: str) -> int:
    """Heuristic syllable count: vowel groups, minus a silent trailing 'e'."""
    word = word.lower()
    count = len(_VOWEL_GROUP_RE.findall(word))
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


@dataclass
class Features:
    """A text's measurable style profile."""

    word_count: int
    scalars: dict[str, float] = field(default_factory=dict)
    function_word_freq: dict[str, float] = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "word_count": self.word_count,
            "scalars": self.scalars,
            "function_word_freq": self.function_word_freq,
        }


def extract_features(text: str) -> Features:
    """Turn raw text into a :class:`Features` profile.

    Markdown is normalized to prose first, so formatting (bullets, code, links)
    doesn't masquerade as style.
    """
    text = _normalize_markdown(text)
    words = _WORD_RE.findall(text)
    lower = [w.lower() for w in words]
    n_words = len(words)
    sentences = [s.strip() for s in _SENT_RE.findall(text) if s.strip()]
    n_sents = max(1, len(sentences))

    if n_words == 0:
        # Degenerate input — return zeros rather than dividing by zero.
        return Features(word_count=0, scalars={}, function_word_freq={w: 0.0 for w in FUNCTION_WORDS})

    # --- sentence-length rhythm ---------------------------------------------
    sent_lengths = [len(_WORD_RE.findall(s)) for s in sentences] or [n_words]
    mean_sent = sum(sent_lengths) / len(sent_lengths)
    var_sent = sum((x - mean_sent) ** 2 for x in sent_lengths) / len(sent_lengths)
    sent_cv = sqrt(var_sent) / (mean_sent + _EPS)  # coefficient of variation

    # --- word length ---------------------------------------------------------
    avg_word_len = sum(len(w) for w in words) / n_words

    # --- lexical diversity: MATTR (moving-average type-token ratio) -----------
    mattr = _mattr(lower, window=50)

    # --- readability: Flesch Reading Ease ------------------------------------
    syllables = sum(_syllables(w) for w in words)
    flesch = 206.835 - 1.015 * (n_words / n_sents) - 84.6 * (syllables / n_words)
    flesch = max(1.0, min(100.0, flesch))  # clamp to a sane band for comparison

    # --- punctuation habits (per 1000 words) ---------------------------------
    per_1k = 1000.0 / n_words

    def rate(pattern: str) -> float:
        return len(re.findall(pattern, text)) * per_1k

    scalars = {
        "avg_sentence_len": mean_sent,
        "sentence_len_cv": sent_cv,
        "avg_word_len": avg_word_len,
        "mattr": mattr,
        "flesch": flesch,
        "comma_rate": rate(r","),
        "semicolon_rate": rate(r";"),
        "colon_rate": rate(r":"),
        # True em/en dashes only. NOT `--` (CLI flags in technical prose) or
        # ` - ` (ranges/hyphens) — counting those conflates flags with the
        # em-dash habit, which is a defining voice tell.
        "dash_rate": rate(r"[—–]"),
        "question_rate": rate(r"\?"),
        "exclaim_rate": rate(r"!"),
        "paren_rate": rate(r"[()]"),
        "contraction_rate": len(_CONTRACTION_RE.findall(text)) * per_1k,
        "first_person_rate": sum(1 for w in lower if w in _FIRST_PERSON) * per_1k,
        "second_person_rate": sum(1 for w in lower if w in _SECOND_PERSON) * per_1k,
    }

    # --- function-word frequencies (fraction of all words) -------------------
    fw_freq = {w: lower.count(w) / n_words for w in FUNCTION_WORDS}

    return Features(word_count=n_words, scalars=scalars, function_word_freq=fw_freq)


def _mattr(words: list[str], window: int) -> float:
    """Moving-average type-token ratio — lexical diversity that, unlike plain
    TTR, does not shrink just because a text is longer."""
    if len(words) <= window:
        return len(set(words)) / max(1, len(words))
    ratios = []
    for i in range(len(words) - window + 1):
        chunk = words[i : i + window]
        ratios.append(len(set(chunk)) / window)
    return sum(ratios) / len(ratios)


@dataclass
class SimilarityResult:
    overall: float          # 0..1, weighted blend of the two below
    fw_sim: float           # 0..1, function-word cosine similarity
    scalar_sim: float       # 0..1, mean per-scalar closeness
    scalar_closeness: dict[str, float] = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "overall": self.overall,
            "function_word_similarity": self.fw_sim,
            "scalar_similarity": self.scalar_sim,
            "scalar_closeness": self.scalar_closeness,
        }


# Function words are the strongest style signal, so weight the two halves evenly
# rather than letting fifteen scalar features outvote them.
_FW_WEIGHT = 0.5

# Per-scalar weights inside the scalar half. Punctuation habits are among the
# most defining voice tells (em-dash and semicolon absence, exclamation
# calibration, parentheticals doing real work), so they are weighted up: the
# rest carry weight 1.0. Without this, a single feature like dash_rate is only
# 1/15 of the scalar mean and an essay full of em dashes can still score well.
_SCALAR_WEIGHTS = {
    "dash_rate": 3.0,
    "semicolon_rate": 3.0,
    "exclaim_rate": 3.0,
    "paren_rate": 3.0,
    "comma_rate": 2.0,
    "colon_rate": 2.0,
    "question_rate": 2.0,
    "contraction_rate": 2.0,
}
_DEFAULT_SCALAR_WEIGHT = 1.0


def style_similarity(candidate: Features, reference: Features) -> SimilarityResult:
    """Compare two :class:`Features` profiles → a 0..1 similarity (1 == identical)."""
    # Function-word vectors → cosine similarity.
    a = [candidate.function_word_freq.get(w, 0.0) for w in FUNCTION_WORDS]
    b = [reference.function_word_freq.get(w, 0.0) for w in FUNCTION_WORDS]
    fw_sim = _cosine(a, b)

    # Scalars → per-feature closeness = 1 - relative difference, then a *weighted*
    # mean so punctuation habits pull their proper weight.
    closeness: dict[str, float] = {}
    for key, ref_val in reference.scalars.items():
        cand_val = candidate.scalars.get(key, 0.0)
        rel_diff = abs(cand_val - ref_val) / (abs(cand_val) + abs(ref_val) + _EPS)
        closeness[key] = 1.0 - rel_diff
    if closeness:
        weights = {k: _SCALAR_WEIGHTS.get(k, _DEFAULT_SCALAR_WEIGHT) for k in closeness}
        scalar_sim = sum(closeness[k] * weights[k] for k in closeness) / sum(weights.values())
    else:
        scalar_sim = 0.0

    overall = _FW_WEIGHT * fw_sim + (1.0 - _FW_WEIGHT) * scalar_sim
    return SimilarityResult(
        overall=overall,
        fw_sim=fw_sim,
        scalar_sim=scalar_sim,
        scalar_closeness=closeness,
    )


def _cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = sqrt(sum(x * x for x in a))
    nb = sqrt(sum(y * y for y in b))
    if na < _EPS or nb < _EPS:
        return 0.0
    return dot / (na * nb)
