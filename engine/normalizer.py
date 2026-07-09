"""Ingredient normalization utilities for Şahvername."""
from __future__ import annotations

import re
import unicodedata


SYNONYMS: dict[str, str] = {
    "sogan": "soğan",
    "kuru sogan": "soğan",
    "yesil biber": "yeşil biber",
    "carliston biber": "yeşil biber",
    "kapya": "biber",
    "kapya biber": "biber",
    "biber": "biber",
    "domates puresi": "domates",
    "konserve domates": "domates",
    "rendelenmis domates": "domates",
    "sivi yag": "sıvı yağ",
    "aycicek yagi": "sıvı yağ",
    "zeytinyagi": "zeytinyağı",
    "tereyag": "tereyağı",
    "tereyagi": "tereyağı",
    "tavuk gogsu": "tavuk",
    "tavuk but": "tavuk",
    "kiyma": "kıyma",
    "spagetti": "spagetti",
    "spaghetti": "spagetti",
    "pasta": "makarna",
    "tortilla": "lavaş",
    "yufka": "lavaş",
    "haslanmis nohut": "nohut",
    "haslanmis fasulye": "fasulye",
    "kirmizi mercimek": "kırmızı mercimek",
    "kasar": "kaşar",
    "yogurt": "yoğurt",
    "suzme yogurt": "yoğurt",
    "sarımsak tozu": "sarımsak",
    "sarimsak": "sarımsak",
    "pirinc": "pirinç",
    "bulgur pilavlik": "bulgur",
    "noodle": "noodle",
}

TURKISH_CHAR_FIX = str.maketrans({
    "İ": "i", "I": "i", "ı": "i", "Ş": "s", "ş": "s", "Ğ": "g", "ğ": "g",
    "Ü": "u", "ü": "u", "Ö": "o", "ö": "o", "Ç": "c", "ç": "c",
})


def ascii_key(value: str) -> str:
    """Return a stable ascii-ish key for fuzzy dictionary matching."""
    value = value.strip().lower().translate(TURKISH_CHAR_FIX)
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^a-z0-9\s-]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def normalize_ingredient(value: str) -> str:
    """Normalize ingredient names into canonical Turkish labels."""
    key = ascii_key(value)
    return SYNONYMS.get(key, value.strip().lower())


def normalize_many(values: list[str] | set[str]) -> set[str]:
    return {normalize_ingredient(v) for v in values if str(v).strip()}
