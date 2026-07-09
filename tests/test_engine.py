from engine.matcher import match_recipes
from engine.normalizer import normalize_ingredient


def test_normalizer_handles_turkish_aliases():
    assert normalize_ingredient("sogan") == "soğan"
    assert normalize_ingredient("yogurt") == "yoğurt"
    assert normalize_ingredient("tavuk gogsu") == "tavuk"


def test_matcher_prefers_complete_recipe():
    recipes = [
        {
            "name": "Basit Menemen",
            "cuisine": "Türk",
            "category": "Kahvaltı",
            "time_min": 20,
            "required_ingredients": ["yumurta", "domates"],
            "optional_ingredients": ["soğan"],
            "quality_score": 80,
        }
    ]
    results = match_recipes(recipes, ["yumurta", "domates"], min_score=0)
    assert len(results) == 1
    assert results[0].missing_required == []
    assert results[0].score > 80


def test_unrelated_recipe_is_not_returned():
    recipes = [
        {
            "name": "Sütlaç",
            "cuisine": "Türk",
            "category": "Tatlı",
            "time_min": 45,
            "required_ingredients": ["pirinç", "süt", "şeker"],
            "optional_ingredients": ["tarçın"],
            "quality_score": 90,
        },
        {
            "name": "Mantar Sote",
            "cuisine": "Türk",
            "category": "Pratik",
            "time_min": 18,
            "required_ingredients": ["mantar", "sarımsak", "tereyağı"],
            "optional_ingredients": ["maydanoz"],
            "quality_score": 90,
        },
    ]
    results = match_recipes(recipes, ["mantar"], min_score=0, max_missing_required=None)
    names = [result.recipe["name"] for result in results]
    assert "Mantar Sote" in names
    assert "Sütlaç" not in names
