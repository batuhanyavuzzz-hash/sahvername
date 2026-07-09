"""Scoring recipes against a user's available ingredients."""
from __future__ import annotations

from dataclasses import dataclass

from .normalizer import normalize_many


DEFAULT_PANTRY = {
    "su", "tuz", "karabiber", "zeytinyağı", "sıvı yağ", "pul biber"
}


@dataclass(frozen=True)
class MatchResult:
    recipe: dict
    score: int
    required_ratio: float
    optional_ratio: float
    matched_required: list[str]
    missing_required: list[str]
    matched_optional: list[str]
    missing_optional: list[str]


def score_recipe(
    recipe: dict,
    user_ingredients: set[str],
    include_default_pantry: bool = True,
) -> MatchResult:
    available = set(user_ingredients)
    if include_default_pantry:
        available |= DEFAULT_PANTRY

    required = normalize_many(recipe.get("required_ingredients", []))
    optional = normalize_many(recipe.get("optional_ingredients", []))
    pantry = normalize_many(recipe.get("pantry_items", []))
    if include_default_pantry:
        available |= pantry

    matched_required = sorted(required & available)
    missing_required = sorted(required - available)
    matched_optional = sorted(optional & available)
    missing_optional = sorted(optional - available)

    required_ratio = len(matched_required) / len(required) if required else 1.0
    optional_ratio = len(matched_optional) / len(optional) if optional else 0.0
    quality = max(0, min(100, int(recipe.get("quality_score", 75)))) / 100

    # Material match is dominant. Quality gently reorders close matches.
    raw_score = (required_ratio * 70) + (optional_ratio * 15) + (quality * 15)

    # Missing required ingredients hurt strongly. A recipe with 2 missing essentials
    # should not outrank a complete but slightly lower-quality recipe.
    raw_score -= len(missing_required) * 8

    # Keep in 0-100 range.
    score = int(round(max(0, min(100, raw_score))))

    return MatchResult(
        recipe=recipe,
        score=score,
        required_ratio=required_ratio,
        optional_ratio=optional_ratio,
        matched_required=matched_required,
        missing_required=missing_required,
        matched_optional=matched_optional,
        missing_optional=missing_optional,
    )
