"""Expanded starter recipe catalog for Şahvername.

This module keeps the curated JSON seed clean, while giving the MVP a much
larger useful recipe pool. The entries are compact specs expanded into the
same recipe schema used by data/recipes_seed.json.
"""
from __future__ import annotations

import re


COMMON_SUBSTITUTIONS = {
    "tereyağı": ["zeytinyağı", "sıvı yağ"],
    "zeytinyağı": ["sıvı yağ", "tereyağı"],
    "yoğurt": ["süzme yoğurt", "labne"],
    "krema": ["süt + un + tereyağı", "yoğurt + az makarna suyu"],
    "pirinç": ["bulgur", "dünden kalma pilav"],
    "bulgur": ["pirinç", "kuskus"],
    "makarna": ["spagetti", "noodle"],
    "spagetti": ["makarna"],
    "noodle": ["makarna", "spagetti"],
    "lavaş": ["tortilla", "ekmek"],
    "ekmek": ["lavaş", "tost ekmeği"],
    "kaşar": ["peynir", "parmesan", "eski kaşar"],
    "peynir": ["kaşar", "beyaz peynir"],
    "domates": ["konserve domates", "rendelenmiş domates", "domates sosu"],
    "domates sosu": ["salça + su", "konserve domates"],
    "salça": ["domates sosu", "domates + az tuz"],
    "nohut": ["konserve nohut", "fasulye"],
    "fasulye": ["kuru fasulye", "nohut"],
    "tavuk": ["hindi", "mantar"],
    "kıyma": ["tavuk kıyma", "mantar", "yeşil mercimek"],
    "limon": ["sirke", "nar ekşisi"],
    "soya sosu": ["az tuz + sirke", "tuz + limon"],
    "yumurta": ["tofu", "nohut unu karışımı"],
    "un": ["yulaf unu", "galeta unu"],
    "yulaf": ["un", "granola"],
    "mantar": ["kabak", "biber"],
    "ıspanak": ["pazı", "semizotu"],
    "kabak": ["patlıcan", "havuç"],
    "patlıcan": ["kabak", "mantar"],
    "salatalık": ["kabak", "marul"],
    "avokado": ["süzme yoğurt", "labne"],
    "muz": ["elma püresi", "armut"],
    "elma": ["muz", "armut"],
}

DEFAULT_PANTRY_BY_CATEGORY = {
    "Tatlı": ["su", "şeker"],
    "Kahvaltı": ["tuz", "karabiber", "zeytinyağı"],
    "Salata": ["tuz", "zeytinyağı"],
    "Meze": ["tuz", "zeytinyağı"],
    "Çorba": ["su", "tuz", "karabiber"],
}

EQUIPMENT_BY_CATEGORY = {
    "Çorba": ["tencere"],
    "Makarna": ["tencere", "tava"],
    "Pilav": ["tencere"],
    "Kahvaltı": ["tava"],
    "Salata": ["kase"],
    "Meze": ["kase"],
    "Tatlı": ["tencere", "kase"],
    "Atıştırmalık": ["tava"],
    "Pratik": ["tava"],
}

# id, name, cuisine, category, time_min, required, optional, tags, quality
EXTRA_RECIPE_SPECS = [
    ("tr-ezogelin", "Ezogelin Çorbası", "Türk", "Çorba", 40, ["kırmızı mercimek", "bulgur", "soğan", "salça"], ["nane", "limon", "pirinç"], ["çorba", "ekonomik"], 90),
    ("tr-yayla", "Yayla Çorbası", "Türk", "Çorba", 30, ["yoğurt", "pirinç", "un", "yumurta"], ["nane", "tereyağı", "limon"], ["çorba", "yoğurtlu"], 88),
    ("tr-domates-corbasi", "Domates Çorbası", "Türk", "Çorba", 25, ["domates", "un", "tereyağı"], ["süt", "kaşar", "salça"], ["çorba", "vejetaryen"], 86),
    ("tr-sehriyeli-tavuk-corbasi", "Şehriyeli Tavuk Çorbası", "Türk", "Çorba", 35, ["tavuk", "şehriye", "limon"], ["havuç", "maydanoz", "tereyağı"], ["protein", "çorba"], 89),
    ("tr-nohut-yemegi", "Nohut Yemeği", "Türk", "Ana yemek", 45, ["nohut", "soğan", "salça"], ["kıyma", "sucuk", "domates"], ["bakliyat", "doyurucu"], 89),
    ("tr-taze-fasulye", "Taze Fasulye", "Türk", "Ana yemek", 45, ["taze fasulye", "soğan", "domates"], ["salça", "sarımsak", "şeker"], ["sebze", "zeytinyağlı"], 88),
    ("tr-kabak-mucver", "Kabak Mücveri", "Türk", "Ara sıcak", 30, ["kabak", "yumurta", "un"], ["dereotu", "peynir", "taze soğan"], ["sebze", "vejetaryen"], 90),
    ("tr-kabak-yemegi", "Kabak Yemeği", "Türk", "Ana yemek", 35, ["kabak", "soğan", "domates"], ["pirinç", "dereotu", "yoğurt"], ["hafif", "sebze"], 86),
    ("tr-imam-bayildi-pratik", "İmam Bayıldı Pratik", "Türk", "Ana yemek", 50, ["patlıcan", "soğan", "domates", "sarımsak"], ["maydanoz", "biber", "şeker"], ["zeytinyağlı", "vejetaryen"], 88),
    ("tr-kiymali-patates", "Kıymalı Patates Yemeği", "Türk", "Ana yemek", 35, ["patates", "kıyma", "soğan", "salça"], ["havuç", "domates", "bezelye"], ["ev yemeği", "doyurucu"], 89),
    ("tr-patates-oturtma", "Patates Oturtma", "Türk", "Ana yemek", 45, ["patates", "kıyma", "soğan", "domates"], ["biber", "kaşar", "salça"], ["fırın", "doyurucu"], 88),
    ("tr-kiymali-makarna", "Kıymalı Makarna", "Türk", "Makarna", 25, ["makarna", "kıyma", "soğan", "salça"], ["domates", "sarımsak", "kaşar"], ["hızlı", "doyurucu"], 88),
    ("tr-ev-koftesi", "Ev Köftesi", "Türk", "Ana yemek", 35, ["kıyma", "soğan", "ekmek içi", "yumurta"], ["maydanoz", "kimyon", "sarımsak"], ["protein", "klasik"], 91),
    ("tr-cilbir", "Çılbır", "Türk", "Kahvaltı", 20, ["yumurta", "yoğurt", "sarımsak"], ["tereyağı", "pul biber", "sirke"], ["kahvaltı", "protein"], 90),
    ("tr-peynirli-omlet", "Peynirli Omlet", "Türk", "Kahvaltı", 12, ["yumurta", "peynir"], ["maydanoz", "kaşar", "domates"], ["hızlı", "protein"], 86),
    ("tr-kasarli-tost", "Kaşarlı Tost", "Türk", "Kahvaltı", 10, ["ekmek", "kaşar"], ["domates", "sucuk", "tereyağı"], ["hızlı", "az malzemeli"], 84),
    ("tr-mercimek-koftesi", "Mercimek Köftesi", "Türk", "Meze", 45, ["kırmızı mercimek", "bulgur", "soğan", "salça"], ["maydanoz", "limon", "kimyon", "taze soğan"], ["vejetaryen", "meze"], 90),
    ("tr-kisir", "Kısır", "Türk", "Salata", 25, ["bulgur", "salça", "limon"], ["domates", "salatalık", "maydanoz", "nar ekşisi"], ["salata", "ekonomik"], 88),
    ("tr-patates-salatasi", "Patates Salatası", "Türk", "Salata", 30, ["patates", "soğan", "limon"], ["maydanoz", "sumak", "yumurta", "turşu"], ["salata", "vejetaryen"], 86),
    ("tr-havuc-tarator", "Havuç Tarator", "Türk", "Meze", 18, ["havuç", "yoğurt", "sarımsak"], ["ceviz", "mayonez", "dereotu"], ["meze", "pratik"], 87),
    ("tr-haydari", "Haydari", "Türk", "Meze", 10, ["yoğurt", "sarımsak", "nane"], ["beyaz peynir", "dereotu", "ceviz"], ["meze", "hızlı"], 85),
    ("tr-tavuklu-patates-firin", "Tavuklu Patates Fırın", "Türk", "Ana yemek", 50, ["tavuk", "patates", "soğan"], ["domates", "biber", "salça", "sarımsak"], ["fırın", "protein"], 89),
    ("tr-yogurtlu-patates", "Sarımsaklı Yoğurtlu Patates", "Türk", "Pratik", 25, ["patates", "yoğurt", "sarımsak"], ["nane", "pul biber", "tereyağı"], ["ekonomik", "meze"], 86),
    ("tr-ispanakli-yumurta", "Ispanaklı Yumurta", "Türk", "Kahvaltı", 18, ["ıspanak", "yumurta", "soğan"], ["yoğurt", "sarımsak", "pul biber"], ["kahvaltı", "sebze"], 86),
    ("tr-mantarli-yumurta", "Mantarlı Yumurta", "Türk / Modern", "Kahvaltı", 15, ["mantar", "yumurta", "tereyağı"], ["kaşar", "maydanoz", "sarımsak"], ["kahvaltı", "protein"], 85),
    ("it-carbonara-esintili", "Carbonara Esintili Makarna", "İtalyan", "Makarna", 22, ["makarna", "yumurta", "peynir"], ["sucuk", "karabiber", "sarımsak"], ["hızlı", "protein"], 88),
    ("it-arrabbiata", "Arrabbiata Makarna", "İtalyan", "Makarna", 20, ["makarna", "domates", "sarımsak"], ["pul biber", "maydanoz", "zeytin"], ["vejetaryen", "hızlı"], 89),
    ("it-kremali-mantarli-makarna", "Kremalı Mantarlı Makarna", "İtalyan", "Makarna", 25, ["makarna", "mantar", "krema"], ["sarımsak", "kaşar", "tavuk"], ["kremalı", "doyurucu"], 88),
    ("it-ton-balikli-makarna", "Ton Balıklı Makarna", "İtalyan", "Makarna", 18, ["makarna", "ton balığı", "domates"], ["mısır", "zeytin", "sarımsak"], ["hızlı", "protein"], 86),
    ("it-pesto-benzeri", "Pesto Benzeri Yeşil Makarna", "İtalyan", "Makarna", 18, ["makarna", "fesleğen", "zeytinyağı"], ["ceviz", "sarımsak", "kaşar", "limon"], ["vejetaryen", "hızlı"], 86),
    ("it-lavas-pizza", "Lavaş Pizza", "İtalyan esintili", "Pratik", 15, ["lavaş", "domates sosu", "kaşar"], ["sucuk", "mantar", "zeytin", "biber"], ["hızlı", "çocuk dostu"], 85),
    ("it-bruschetta", "Bruschetta", "İtalyan", "Atıştırmalık", 12, ["ekmek", "domates", "sarımsak"], ["fesleğen", "zeytinyağı", "peynir"], ["atıştırmalık", "hafif"], 84),
    ("it-caprese", "Caprese Salata", "İtalyan", "Salata", 10, ["domates", "peynir", "zeytinyağı"], ["fesleğen", "sirke", "zeytin"], ["salata", "vejetaryen"], 85),
    ("it-minestrone", "Sebzeli Minestrone", "İtalyan", "Çorba", 40, ["soğan", "havuç", "domates", "makarna"], ["kabak", "fasulye", "kereviz", "peynir"], ["çorba", "sebze"], 86),
    ("it-tavuklu-alfredo", "Tavuklu Alfredo Benzeri", "İtalyan esintili", "Makarna", 30, ["makarna", "tavuk", "krema"], ["sarımsak", "kaşar", "mantar"], ["protein", "kremalı"], 87),
    ("mx-fasulyeli-burrito", "Fasulyeli Burrito", "Meksika", "Pratik", 20, ["lavaş", "fasulye", "kaşar"], ["pirinç", "yoğurt", "salça", "mısır"], ["doyurucu", "pratik"], 86),
    ("mx-tavuklu-burrito", "Tavuklu Burrito", "Meksika", "Ana yemek", 30, ["lavaş", "tavuk", "pirinç"], ["kaşar", "yoğurt", "mısır", "biber"], ["protein", "doyurucu"], 87),
    ("mx-huevos-rancheros", "Huevos Rancheros Benzeri", "Meksika", "Kahvaltı", 20, ["yumurta", "domates", "lavaş"], ["fasulye", "kaşar", "biber", "avokado"], ["kahvaltı", "protein"], 86),
    ("mx-chili-con-carne", "Chili Con Carne Pratik", "Meksika", "Ana yemek", 40, ["kıyma", "fasulye", "domates", "salça"], ["mısır", "kimyon", "biber", "kaşar"], ["bakliyat", "protein"], 88),
    ("mx-guacamole", "Guacamole Benzeri Ezme", "Meksika", "Meze", 10, ["avokado", "limon", "sarımsak"], ["domates", "soğan", "kişniş"], ["meze", "hızlı"], 84),
    ("mx-salsa", "Domates Salsa", "Meksika", "Meze", 10, ["domates", "soğan", "limon"], ["biber", "maydanoz", "sarımsak"], ["meze", "hafif"], 83),
    ("mx-nachos", "Tavada Nachos", "Meksika", "Atıştırmalık", 15, ["lavaş", "kaşar", "salça"], ["kıyma", "mısır", "fasulye", "yoğurt"], ["atıştırmalık", "pratik"], 82),
    ("mx-misir-salatasi", "Mısır Salatası", "Meksika esintili", "Salata", 12, ["mısır", "yoğurt", "limon"], ["biber", "kaşar", "maydanoz", "pul biber"], ["salata", "hızlı"], 82),
    ("mx-kahvalti-burritosu", "Kahvaltı Burritosu", "Meksika", "Kahvaltı", 18, ["lavaş", "yumurta", "kaşar"], ["patates", "sucuk", "biber", "yoğurt"], ["kahvaltı", "doyurucu"], 85),
    ("in-aloo-curry", "Aloo Curry", "Hint", "Ana yemek", 35, ["patates", "soğan", "domates"], ["köri", "sarımsak", "zencefil", "yoğurt"], ["vejetaryen", "ekonomik"], 87),
    ("in-yumurtali-curry", "Yumurtalı Curry", "Hint", "Ana yemek", 30, ["yumurta", "soğan", "domates"], ["köri", "yoğurt", "sarımsak", "zencefil"], ["protein", "baharatlı"], 86),
    ("in-dal-tadka", "Dal Tadka", "Hint", "Ana yemek", 35, ["kırmızı mercimek", "soğan", "sarımsak"], ["domates", "kimyon", "zerdeçal", "tereyağı"], ["bakliyat", "vejetaryen"], 89),
    ("in-butter-chicken-like", "Tereyağlı Tavuk Benzeri", "Hint esintili", "Ana yemek", 40, ["tavuk", "domates", "yoğurt"], ["tereyağı", "köri", "sarımsak", "zencefil"], ["protein", "baharatlı"], 88),
    ("in-ispanakli-peynir", "Ispanaklı Peynir Tava", "Hint esintili", "Ana yemek", 30, ["ıspanak", "peynir", "soğan"], ["sarımsak", "yoğurt", "köri", "domates"], ["vejetaryen", "protein"], 85),
    ("in-sebzeli-biryani", "Sebzeli Biryani Benzeri", "Hint", "Pilav", 45, ["pirinç", "soğan", "sebze"], ["yoğurt", "köri", "bezelye", "havuç"], ["vejetaryen", "doyurucu"], 85),
    ("in-tavuk-biryani", "Tavuk Biryani Pratik", "Hint", "Pilav", 50, ["tavuk", "pirinç", "soğan"], ["yoğurt", "köri", "sarımsak", "limon"], ["protein", "pilav"], 88),
    ("in-raita", "Raita", "Hint", "Meze", 8, ["yoğurt", "salatalık", "nane"], ["kimyon", "limon", "sarımsak"], ["ferah", "hızlı"], 83),
    ("ea-soya-sarimsak-noodle", "Soya Sarımsaklı Noodle", "Uzak Doğu", "Noodle", 18, ["noodle", "sarımsak", "soya sosu"], ["yumurta", "tavuk", "susam", "taze soğan"], ["hızlı", "az malzemeli"], 87),
    ("ea-sebzeli-stir-fry", "Sebzeli Stir Fry", "Uzak Doğu", "Ana yemek", 20, ["sebze", "sarımsak", "soya sosu"], ["tavuk", "mantar", "havuç", "biber"], ["sebze", "hızlı"], 86),
    ("ea-tavuklu-stir-fry", "Tavuklu Stir Fry", "Uzak Doğu", "Ana yemek", 25, ["tavuk", "sebze", "soya sosu"], ["sarımsak", "zencefil", "bal", "mantar"], ["protein", "hızlı"], 88),
    ("ea-egg-drop", "Egg Drop Çorbası", "Uzak Doğu", "Çorba", 15, ["yumurta", "tavuk suyu", "nişasta"], ["mısır", "taze soğan", "soya sosu"], ["çorba", "hızlı"], 85),
    ("ea-omurice", "Omurice Benzeri", "Japon esintili", "Ana yemek", 25, ["pirinç", "yumurta", "domates sosu"], ["tavuk", "soğan", "bezelye"], ["yumurta", "pratik"], 86),
    ("ea-pratik-ramen", "Pratik Ramen", "Japon esintili", "Çorba", 20, ["noodle", "yumurta", "soya sosu"], ["mantar", "tavuk", "taze soğan", "sarımsak"], ["çorba", "hızlı"], 84),
    ("ea-ton-pirinc-kasesi", "Ton Balıklı Pirinç Kasesi", "Uzak Doğu esintili", "Ana yemek", 12, ["pirinç", "ton balığı", "soya sosu"], ["salatalık", "yumurta", "yoğurt", "susam"], ["hızlı", "protein"], 84),
    ("ea-susamli-salatalik", "Susamlı Salatalık Salatası", "Uzak Doğu", "Salata", 10, ["salatalık", "soya sosu", "sarımsak"], ["susam", "sirke", "pul biber"], ["salata", "hafif"], 83),
    ("med-falafel-tava", "Falafel Tava", "Levant", "Ana yemek", 35, ["nohut", "soğan", "sarımsak"], ["maydanoz", "kimyon", "un", "yoğurt"], ["vejetaryen", "bakliyat"], 87),
    ("med-tabbule", "Tabbule Benzeri", "Levant", "Salata", 20, ["bulgur", "maydanoz", "limon"], ["domates", "salatalık", "nane"], ["salata", "ferah"], 86),
    ("med-fattoush", "Fattoush Benzeri", "Levant", "Salata", 15, ["salatalık", "domates", "ekmek"], ["marul", "limon", "sumak", "soğan"], ["salata", "hafif"], 84),
    ("med-mercimek-salatasi", "Mercimek Salatası", "Akdeniz", "Salata", 30, ["yeşil mercimek", "soğan", "limon"], ["maydanoz", "domates", "salatalık", "nar ekşisi"], ["salata", "protein"], 87),
    ("med-tavuklu-lavas", "Tavuklu Pita/Lavaş", "Akdeniz", "Pratik", 25, ["lavaş", "tavuk", "yoğurt"], ["salatalık", "domates", "sarımsak", "limon"], ["protein", "pratik"], 87),
    ("med-greek-salata", "Greek Salata", "Akdeniz", "Salata", 10, ["domates", "salatalık", "peynir"], ["zeytin", "soğan", "kekik", "limon"], ["salata", "hafif"], 85),
    ("med-patlican-yogurtlama", "Patlıcan Yoğurtlama", "Akdeniz / Türk", "Meze", 25, ["patlıcan", "yoğurt", "sarımsak"], ["tahin", "limon", "maydanoz"], ["meze", "vejetaryen"], 88),
    ("mod-scrambled-egg", "Scrambled Egg", "Modern", "Kahvaltı", 10, ["yumurta", "tereyağı"], ["süt", "peynir", "frenk soğanı"], ["kahvaltı", "protein"], 87),
    ("mod-sebzeli-omlet", "Sebzeli Omlet", "Modern", "Kahvaltı", 15, ["yumurta", "sebze"], ["peynir", "mantar", "biber", "domates"], ["protein", "kahvaltı"], 86),
    ("mod-overnight-oats", "Overnight Oats", "Modern", "Kahvaltı", 5, ["yulaf", "yoğurt", "süt"], ["bal", "muz", "ceviz", "tarçın"], ["kahvaltı", "pratik"], 86),
    ("mod-muzlu-yulaf-pankek", "Muzlu Yulaf Pankek", "Modern", "Kahvaltı", 18, ["muz", "yumurta", "yulaf"], ["süt", "tarçın", "bal"], ["kahvaltı", "fit"], 85),
    ("mod-peynirli-ekmek-tavasi", "Peynirli Ekmek Tavası", "Modern", "Pratik", 12, ["ekmek", "yumurta", "peynir"], ["maydanoz", "domates", "kaşar"], ["bayat değerlendirme", "kahvaltı"], 84),
    ("mod-yogurtlu-meyve", "Yoğurtlu Meyve Kasesi", "Modern", "Kahvaltı", 7, ["yoğurt", "meyve"], ["yulaf", "bal", "ceviz", "tarçın"], ["hızlı", "hafif"], 82),
    ("mod-ton-yumurta-salatasi", "Ton Balıklı Yumurta Salatası", "Modern", "Salata", 15, ["yumurta", "ton balığı", "yoğurt"], ["hardal", "salatalık", "mısır", "maydanoz"], ["protein", "salata"], 84),
    ("us-grilled-cheese", "Grilled Cheese", "Amerikan", "Pratik", 10, ["ekmek", "kaşar", "tereyağı"], ["domates", "sucuk", "hardal"], ["hızlı", "az malzemeli"], 84),
    ("tr-sutlac", "Sütlaç", "Türk", "Tatlı", 45, ["pirinç", "süt", "şeker"], ["vanilya", "tarçın"], ["tatlı", "klasik"], 88),
    ("tr-un-helvasi", "Un Helvası", "Türk", "Tatlı", 25, ["un", "tereyağı", "şeker"], ["süt", "ceviz", "tarçın"], ["tatlı", "ekonomik"], 87),
    ("mod-kupa-kek", "Kupa Kek", "Modern", "Tatlı", 8, ["un", "süt", "kakao"], ["yumurta", "şeker", "kabartma tozu", "çikolata"], ["tatlı", "hızlı"], 81),
    ("fr-krep", "Krep", "Fransız", "Kahvaltı", 20, ["yumurta", "süt", "un"], ["şeker", "peynir", "bal", "çikolata"], ["kahvaltı", "çok amaçlı"], 86),
    ("mod-kakaolu-yulaf-toplari", "Kakaolu Yulaf Topları", "Modern", "Tatlı", 15, ["yulaf", "kakao", "bal"], ["fıstık ezmesi", "ceviz", "hindistan cevizi"], ["tatlı", "pişmeyen"], 82),
    ("mod-muzlu-yogurt-tatlisi", "Muzlu Yoğurt Tatlısı", "Modern", "Tatlı", 7, ["muz", "yoğurt", "bal"], ["kakao", "ceviz", "tarçın"], ["tatlı", "hızlı"], 81),
    ("mod-elmali-tava-tatlisi", "Elmalı Tava Tatlısı", "Modern", "Tatlı", 15, ["elma", "tereyağı", "şeker"], ["tarçın", "ceviz", "yulaf"], ["tatlı", "meyveli"], 82),
    ("mod-kori-soslu-tavuk", "Köri Soslu Tavuk", "Modern", "Ana yemek", 30, ["tavuk", "köri", "yoğurt"], ["krema", "sarımsak", "mantar", "pirinç"], ["protein", "pratik"], 86),
    ("mod-tavuklu-mantar-sote", "Tavuklu Mantar Sote", "Modern", "Ana yemek", 25, ["tavuk", "mantar", "soğan"], ["krema", "sarımsak", "kaşar"], ["protein", "hızlı"], 87),
]


def _slug(value: str) -> str:
    value = value.lower()
    value = value.translate(str.maketrans("çğıöşüı", "cgiosui"))
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


def _substitutions_for(ingredients: list[str]) -> dict[str, list[str]]:
    return {item: COMMON_SUBSTITUTIONS[item] for item in ingredients if item in COMMON_SUBSTITUTIONS}


def _steps_for(name: str, category: str, required: list[str], optional: list[str]) -> list[str]:
    main = ", ".join(required[:3])
    optional_text = ", ".join(optional[:3]) if optional else "baharat ve servis dokunuşları"
    if category == "Çorba":
        return [
            f"{main} malzemelerini hazırla; bakliyat varsa yıka ve süz.",
            "Soğan/sarımsak gibi lezzet tabanını yağda kısa süre çevir.",
            "Ana malzemeleri ve sıcak suyu ekleyip yumuşayana kadar pişir.",
            f"{optional_text} ile kıvamı ve aromayı tamamla."
        ]
    if category in {"Makarna", "Noodle"}:
        return [
            "Makarna/noodleı tuzlu suda diri kalacak şekilde haşla.",
            f"Ayrı tavada {main} ile sos veya lezzet tabanı hazırla.",
            "Haşlama suyundan az ekleyip sosu bağla.",
            f"{optional_text} ile bitirip sıcak servis et."
        ]
    if category in {"Salata", "Meze"}:
        return [
            f"{main} malzemelerini doğra, haşla veya ezilecekse hazırla.",
            "Sosu ayrı kapta tuz, yağ ve asit dengesiyle karıştır.",
            "Ana malzemelerle sosu birleştir.",
            f"{optional_text} ekleyip kısa dinlendirerek servis et."
        ]
    if category == "Tatlı":
        return [
            f"{main} malzemelerini ölçülü şekilde hazırla.",
            "Kıvam alana kadar kontrollü ateşte veya uygun kapta pişir/karıştır.",
            f"{optional_text} ile aromayı tamamla.",
            "Ilık ya da soğuk servis et."
        ]
    if category == "Kahvaltı":
        return [
            f"{main} malzemelerini hazırla.",
            "Tavayı orta ateşte ısıt ve ana malzemeyi kurutmadan pişir.",
            f"{optional_text} ile lezzeti güçlendir.",
            "Sıcak servis et."
        ]
    return [
        f"{main} malzemelerini hazırla ve uygun boyutta doğra.",
        "Lezzet tabanını tavada/tencerede kur; soğan, salça veya baharatı kısa kavur.",
        "Ana malzemeleri ekleyip kontrollü ateşte pişir.",
        f"{optional_text} ile son dokunuşu yapıp servis et."
    ]


def _tips_for(category: str, required: list[str]) -> list[str]:
    if "yoğurt" in required:
        return ["Yoğurdu çok sıcak yemeğe doğrudan ekleme; kesilmemesi için ılıtarak veya servis anında kullan."]
    if "tavuk" in required:
        return ["Tavuğu tavaya koyunca hemen karıştırma; mühürlenirse daha sulu kalır."]
    if "makarna" in required or "noodle" in required:
        return ["Haşlama suyundan birkaç kaşık ayırmak sosu bağlamayı kolaylaştırır."]
    if category in {"Salata", "Meze"}:
        return ["Sulu malzemeleri iyi süz; sosu servis zamanına yakın eklemek dokuyu korur."]
    if category == "Çorba":
        return ["Çorba koyulaşırsa soğuk değil sıcak suyla aç; kıvam daha dengeli kalır."]
    if category == "Tatlı":
        return ["Tatlılarda ateşi kontrollü tut; şekerli karışımlar dibi hızlı tutabilir."]
    return ["Ana malzemeyi fazla pişirme; dokuyu korumak lezzeti belirgin artırır."]


def get_extra_recipes(existing_ids: set[str] | None = None) -> list[dict]:
    existing_ids = existing_ids or set()
    recipes: list[dict] = []
    for rid, name, cuisine, category, time_min, required, optional, tags, quality in EXTRA_RECIPE_SPECS:
        if rid in existing_ids:
            continue
        pantry = DEFAULT_PANTRY_BY_CATEGORY.get(category, ["tuz", "karabiber", "zeytinyağı"])
        equipment = EQUIPMENT_BY_CATEGORY.get(category, ["tava", "tencere"])
        recipes.append({
            "id": rid,
            "name": name,
            "cuisine": cuisine,
            "category": category,
            "time_min": time_min,
            "difficulty": "Kolay" if time_min <= 30 else "Orta",
            "servings": 2 if category in {"Kahvaltı", "Meze", "Salata", "Tatlı", "Pratik"} else 4,
            "required_ingredients": required,
            "optional_ingredients": optional,
            "pantry_items": pantry,
            "substitutions": _substitutions_for(required + optional),
            "equipment": equipment,
            "steps": _steps_for(name, category, required, optional),
            "critical_tips": _tips_for(category, required),
            "tags": tags,
            "quality_score": quality,
        })
    return recipes
