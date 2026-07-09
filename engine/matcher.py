"""Recipe matching engine."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .normalizer import normalize_many
from .scoring import MatchResult, score_recipe


def load_recipes(path: str | Path) -> list[dict]:
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def all_ingredients(recipes: Iterable[dict]) -> list[str]:
    pool: set[str] = set()
    for recipe in recipes:
        for key in ("required_ingredients", "optional_ingredients", "pantry_items"):
            pool |= set(recipe.get(key, []))
    return sorted(pool, key=lambda x: x.lower())


def match_recipes(
    recipes: list[dict],
    selected_ingredients: list[str],
    cuisine: str = "Tümü",
    category: str = "Tümü",
    max_time: int | None = None,
    max_missing_required: int | None = 2,
    include_default_pantry: bool = True,
    min_score: int = 0,
) -> list[MatchResult]:
    user_ingredients = normalize_many(selected_ingredients)
    results: list[MatchResult] = []

    for recipe in recipes:
        if cuisine != "Tümü" and recipe.get("cuisine") != cuisine:
            continue
        if category != "Tümü" and recipe.get("category") != category:
            continue
        if max_time is not None and int(recipe.get("time_min", 999)) > max_time:
            continue

        result = score_recipe(recipe, user_ingredients, include_default_pantry)
        if max_missing_required is not None and len(result.missing_required) > max_missing_required:
            continue
        if result.score < min_score:
            continue
        results.append(result)

    return sorted(
        results,
        key=lambda r: (
            r.score,
            -len(r.missing_required),
            r.recipe.get("quality_score", 0),
            -int(r.recipe.get("time_min", 999)),
        ),
        reverse=True,
    )
