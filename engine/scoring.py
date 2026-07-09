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
    has_real_overlap: bool


def score_recipe(
    recipe: dict,
    user_ingredients: set[str],
    include_default_pantry: bool = True,
) -> MatchResult:
    """Score a recipe.

    Pantry items are allowed for cooking, but they must not create relevance by
    themselves. If the user says only "mantar", a recipe with zero overlap to
    mantar should get 0 and never appear as a suggestion.
    """
    real_user_ingredients = set(user_ingredients)
    available = set(real_user_ingredients)
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

    real_overlap = (required | optional) & real_user_ingredients
    has_real_overlap = bool(real_overlap)

    required_ratio = len(matched_required) / len(required) if required else 1.0
    optional_ratio = len(matched_optional) / len(optional) if optional else 0.0
    quality = max(0, min(100, int(recipe.get("quality_score", 75)))) / 100

    if not has_real_overlap:
        score = 0
    else:
        # Relevance and required coverage dominate. Quality only breaks ties.
        raw_score = (required_ratio * 78) + (optional_ratio * 10) + (quality * 12)

        # Strong missing-essential penalty. This prevents "sütlaç" style nonsense
        # when the user only entered an unrelated ingredient.
        raw_score -= len(missing_required) * 18

        # A recipe where the ingredient is only optional can be shown, but lower.
        if not matched_required and matched_optional:
            raw_score = min(raw_score, 28)

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
        has_real_overlap=has_real_overlap,
    )
