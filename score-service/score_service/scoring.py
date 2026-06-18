from typing import Final

WEIGHTS: Final[dict[str, float]] = {
    "governance": 0.25,
    "innovation": 0.20,
    "operations": 0.20,
    "finance": 0.20,
    "sustainability": 0.15,
}


def calculate_composite_score(dimension_scores: dict[str, float]) -> float:
    """Calculate the weighted average score rounded to one decimal place."""

    score = sum(dimension_scores[dimension] * weight for dimension, weight in WEIGHTS.items())
    return round(score, 1)


def classify_grade(composite_score: float) -> str:
    """Return the grade that matches a composite score."""

    if composite_score >= 85:
        return "A"
    if composite_score >= 70:
        return "B"
    if composite_score >= 55:
        return "C"
    return "D"
