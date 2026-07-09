"""Curated starter recipe catalog for Şahvername.

Important product rule: no fake volume. A recipe is allowed here only if its
steps are specific enough to cook from. Draft/template recipes are intentionally
not returned.
"""
from __future__ import annotations


CURATED_EXTRA_RECIPES: list[dict] = [
    {
        "id": "tr-mantar-sote",
        "name": "Sarımsaklı Mantar Sote",
        "cuisine": "Türk / Modern",
        "category": "Pratik",
        "time_min": 18,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["mantar", "sarımsak", "tereyağı"],
        "optional_ingredients": ["soğan", "maydanoz", "limon", "kaşar", "kekik"],
        "pantry_items": ["tuz", "karabiber", "zeytinyağı"],
        "substitutions": {"tereyağı": ["zeytinyağı", "sıvı yağ"], "maydanoz": ["dereotu", "taze soğan"]},
        "equipment": ["geniş tava"],
        "steps": [
            "Mantarları ıslatmadan temizle; gerekirse nemli bezle sil. İnce değil, iri dilimle.",
            "Geniş tavayı iyice ısıt. Mantarları tavaya tek kat yay ve ilk 2-3 dakika karıştırma.",
            "Mantar suyunu salıp tekrar çekmeye başlayınca tereyağı ve az zeytinyağı ekle.",
            "Ezilmiş sarımsağı son 1 dakikada ekle; yanmasına izin verme.",
            "Tuzunu en son ver. Karabiber, limon ve maydanozla servis et."
        ],
        "critical_tips": [
            "Mantar kalabalık tavada haşlanır; geniş tava ve yüksek ateş lezzeti belirler.",
            "Tuzu başta atma; mantarın su salmasını hızlandırır."
        ],
        "tags": ["mantar", "hızlı", "az malzemeli", "vejetaryen"],
        "quality_score": 93
    },
    {
        "id": "it-kremali-mantarli-makarna-curated",
        "name": "Kremalı Mantarlı Makarna",
        "cuisine": "İtalyan esintili",
        "category": "Makarna",
        "time_min": 25,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["mantar", "makarna", "krema"],
        "optional_ingredients": ["sarımsak", "kaşar", "tavuk", "maydanoz", "karabiber"],
        "pantry_items": ["su", "tuz", "zeytinyağı"],
        "substitutions": {"krema": ["süt + un + tereyağı", "labne + makarna suyu"], "kaşar": ["parmesan", "eski kaşar"]},
        "equipment": ["tencere", "geniş tava"],
        "steps": [
            "Makarnayı bol tuzlu suda diri kalacak şekilde haşla; yarım bardak haşlama suyu ayır.",
            "Mantarları geniş tavada yüksek ateşte suyunu çektirerek sotele.",
            "Sarımsak kullanacaksan mantar renk aldıktan sonra ekle ve 30-40 saniye çevir.",
            "Kremayı ekle; kaynatıp keskinleştirme, sadece hafifçe ısıt.",
            "Makarnayı tavaya al. Gerekirse ayırdığın makarna suyuyla sosu incelt.",
            "Karabiber ve peynirle bitir."
        ],
        "critical_tips": [
            "Makarna suyundaki nişasta sosu bağlar; kremayı artırmak yerine önce makarna suyu kullan.",
            "Mantar iyi kavrulmadan krema eklenirse yemek sulu ve zayıf olur."
        ],
        "tags": ["mantar", "makarna", "doyurucu"],
        "quality_score": 92
    },
    {
        "id": "tr-mantarli-yumurta-curated",
        "name": "Mantarlı Yumurta",
        "cuisine": "Türk / Modern",
        "category": "Kahvaltı",
        "time_min": 15,
        "difficulty": "Kolay",
        "servings": 1,
        "required_ingredients": ["mantar", "yumurta", "tereyağı"],
        "optional_ingredients": ["kaşar", "maydanoz", "soğan", "pul biber"],
        "pantry_items": ["tuz", "karabiber"],
        "substitutions": {"tereyağı": ["zeytinyağı"], "kaşar": ["beyaz peynir", "eski kaşar"]},
        "equipment": ["tava"],
        "steps": [
            "Mantarları iri doğra ve sıcak tavada suyunu salıp çekene kadar pişir.",
            "Tereyağını ekleyip mantarı 1 dakika lezzetlendir.",
            "Yumurtaları ayrı kapta hafifçe çırp; çok köpürtme.",
            "Yumurtayı tavaya dök, altı kısık-orta ateşte yavaşça pişir.",
            "Kaşar kullanacaksan son 30 saniyede serpip kapağı kapat."
        ],
        "critical_tips": ["Yumurtayı mantar suyunu çekmeden eklersen sonuç sulu olur."],
        "tags": ["mantar", "yumurta", "kahvaltı", "protein"],
        "quality_score": 90
    },
    {
        "id": "tr-kasarli-mantar-firin",
        "name": "Kaşarlı Fırın Mantar",
        "cuisine": "Türk",
        "category": "Ara sıcak",
        "time_min": 25,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["mantar", "kaşar", "tereyağı"],
        "optional_ingredients": ["sarımsak", "kekik", "pul biber", "maydanoz"],
        "pantry_items": ["tuz", "karabiber"],
        "substitutions": {"kaşar": ["mozarella", "eski kaşar"], "tereyağı": ["zeytinyağı"]},
        "equipment": ["fırın kabı"],
        "steps": [
            "Mantarların saplarını çıkar, şapkalarını fırın kabına diz.",
            "Her mantarın içine çok az tereyağı, tuz ve karabiber koy.",
            "190°C fırında mantarlar suyunu salıp çekmeye başlayana kadar 10-12 dakika pişir.",
            "Üzerine kaşar ekle ve peynir kızarana kadar 5-7 dakika daha pişir.",
            "Maydanoz veya kekikle sıcak servis et."
        ],
        "critical_tips": ["Peyniri baştan koyma; mantar suyunda eriyip lastik gibi olabilir."],
        "tags": ["mantar", "fırın", "ara sıcak"],
        "quality_score": 89
    },
    {
        "id": "tr-mantarli-tavuk-sote-curated",
        "name": "Mantarlı Tavuk Sote",
        "cuisine": "Türk / Modern",
        "category": "Ana yemek",
        "time_min": 30,
        "difficulty": "Kolay",
        "servings": 3,
        "required_ingredients": ["tavuk", "mantar", "soğan"],
        "optional_ingredients": ["sarımsak", "krema", "biber", "kaşar", "kekik"],
        "pantry_items": ["tuz", "karabiber", "zeytinyağı"],
        "substitutions": {"krema": ["süt + un + tereyağı", "yoğurt + az sıcak su"], "tavuk": ["hindi"]},
        "equipment": ["geniş tava"],
        "steps": [
            "Tavuğu küçük küpler halinde doğra, tavayı iyice ısıt ve tavukları tek kat yay.",
            "Tavuk renk alınca kenara al. Aynı tavada mantarları yüksek ateşte suyunu çektir.",
            "Soğanı ekleyip yumuşat, sarımsak kullanıyorsan sonradan ekle.",
            "Tavuğu geri al, tuz-karabiber-kekik ile karıştır.",
            "Kremalı yapmak istersen ocağı kıs, kremayı ekle ve sadece 2-3 dakika bağla."
        ],
        "critical_tips": ["Tavuk ve mantarı aynı anda kalabalık tavaya atma; ikisi de haşlanır."],
        "tags": ["mantar", "tavuk", "protein"],
        "quality_score": 91
    },
    {
        "id": "it-mushroom-toast",
        "name": "Mantarlı Peynirli Tost / Ekmek Üstü",
        "cuisine": "Modern",
        "category": "Pratik",
        "time_min": 15,
        "difficulty": "Kolay",
        "servings": 1,
        "required_ingredients": ["mantar", "ekmek", "kaşar"],
        "optional_ingredients": ["sarımsak", "tereyağı", "maydanoz", "hardal"],
        "pantry_items": ["tuz", "karabiber"],
        "substitutions": {"ekmek": ["lavaş", "tost ekmeği"], "kaşar": ["peynir", "mozarella"]},
        "equipment": ["tava", "tost makinesi"],
        "steps": [
            "Mantarları ince dilimle ve tavada suyunu çektirerek sotele.",
            "Sarımsak ve az tereyağı ekleyip 30 saniye çevir.",
            "Ekmeğin üzerine mantarı yay, kaşarı ekle.",
            "Tost makinesinde veya kapaklı tavada peynir eriyene kadar pişir.",
            "Karabiber ve maydanozla servis et."
        ],
        "critical_tips": ["Mantar harcını sulu bırakma; ekmek yumuşar ve tost çöker."],
        "tags": ["mantar", "tost", "hızlı"],
        "quality_score": 86
    },
    {
        "id": "tr-patatesli-yumurta-curated",
        "name": "Patatesli Yumurta",
        "cuisine": "Türk",
        "category": "Kahvaltı",
        "time_min": 25,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["patates", "yumurta", "soğan"],
        "optional_ingredients": ["biber", "kaşar", "pul biber", "maydanoz"],
        "pantry_items": ["tuz", "karabiber", "zeytinyağı"],
        "substitutions": {"soğan": ["taze soğan"], "kaşar": ["peynir"]},
        "equipment": ["tava"],
        "steps": [
            "Patatesleri küçük küp doğra; küçük doğramak pişmeyi hızlandırır.",
            "Tavada yağ ile patatesleri orta ateşte kızartmadan yumuşat.",
            "Soğanı ekle ve patatesle birlikte hafif renk alana kadar çevir.",
            "Yumurtayı kır; ister karıştır, ister göz göz bırak.",
            "Tuz, karabiber ve pul biberle servis et."
        ],
        "critical_tips": ["Patatesi çok büyük doğrama; dışı kızarıp içi çiğ kalır."],
        "tags": ["kahvaltı", "ekonomik", "yumurta"],
        "quality_score": 89
    },
    {
        "id": "tr-soganli-yumurta-curated",
        "name": "Soğanlı Yumurta",
        "cuisine": "Türk",
        "category": "Kahvaltı",
        "time_min": 18,
        "difficulty": "Kolay",
        "servings": 1,
        "required_ingredients": ["yumurta", "soğan", "tereyağı"],
        "optional_ingredients": ["domates", "biber", "kaşar", "pul biber"],
        "pantry_items": ["tuz", "karabiber"],
        "substitutions": {"tereyağı": ["zeytinyağı"], "soğan": ["taze soğan"]},
        "equipment": ["tava"],
        "steps": [
            "Soğanı yarım ay doğra ve yağda orta-kısık ateşte yumuşat.",
            "Soğan hafif tatlanıp renk alınca tuzunu ekle.",
            "Yumurtayı kır ve kısık ateşte pişir.",
            "Pul biber ve karabiberle sıcak servis et."
        ],
        "critical_tips": ["Soğanı hızlı yakma; yavaş pişerse tatlılaşır ve yumurtayı taşır."],
        "tags": ["kahvaltı", "az malzemeli"],
        "quality_score": 86
    },
    {
        "id": "tr-domatesli-bulgur-pilavi-curated",
        "name": "Domatesli Bulgur Pilavı",
        "cuisine": "Türk",
        "category": "Pilav",
        "time_min": 30,
        "difficulty": "Kolay",
        "servings": 3,
        "required_ingredients": ["bulgur", "domates", "soğan"],
        "optional_ingredients": ["salça", "biber", "tereyağı", "sarımsak"],
        "pantry_items": ["su", "tuz", "karabiber", "zeytinyağı"],
        "substitutions": {"domates": ["konserve domates", "salça + su"], "bulgur": ["pirinç"]},
        "equipment": ["tencere"],
        "steps": [
            "Soğanı yağda yumuşat, biber kullanıyorsan ekleyip çevir.",
            "Domatesi ve salçayı ekleyip çiğ kokusu gidene kadar pişir.",
            "Bulguru ekle, 1-2 dakika kavur.",
            "Sıcak suyu ekle; kapağı kapalı kısık ateşte suyunu çekene kadar pişir.",
            "Altını kapatıp 10 dakika dinlendir."
        ],
        "critical_tips": ["Bulgur pilavı dinlenmeden servis edilirse tane tane değil ıslak kalır."],
        "tags": ["pilav", "ekonomik", "doyurucu"],
        "quality_score": 90
    },
    {
        "id": "tr-sarimsakli-yogurtlu-makarna-curated",
        "name": "Sarımsaklı Yoğurtlu Makarna",
        "cuisine": "Türk",
        "category": "Makarna",
        "time_min": 18,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["makarna", "yoğurt", "sarımsak"],
        "optional_ingredients": ["tereyağı", "nane", "pul biber", "ceviz"],
        "pantry_items": ["su", "tuz"],
        "substitutions": {"yoğurt": ["süzme yoğurt + az su", "labne"]},
        "equipment": ["tencere", "kase"],
        "steps": [
            "Makarnayı tuzlu suda haşla; çok yumuşatmadan süz.",
            "Yoğurdu ezilmiş sarımsak ve az tuzla pürüzsüz karıştır.",
            "Makarna çok sıcakken yoğurdu dökme; 1-2 dakika ılımasını bekle.",
            "Yoğurtla karıştır, istersen tereyağında nane-pul biber yakıp üzerine gezdir.",
            "Hemen servis et; beklerse yoğurt makarnayı çeker."
        ],
        "critical_tips": ["Yoğurdun kesilmemesi için makarnayı hafif ılıtmak şart."],
        "tags": ["makarna", "yoğurt", "hızlı"],
        "quality_score": 89
    },
    {
        "id": "it-aglio-olio-curated",
        "name": "Sarımsaklı Zeytinyağlı Spagetti",
        "cuisine": "İtalyan",
        "category": "Makarna",
        "time_min": 18,
        "difficulty": "Kolay",
        "servings": 2,
        "required_ingredients": ["spagetti", "sarımsak", "zeytinyağı"],
        "optional_ingredients": ["pul biber", "maydanoz", "parmesan", "limon"],
        "pantry_items": ["su", "tuz"],
        "substitutions": {"spagetti": ["makarna"], "parmesan": ["eski kaşar", "kaşar"]},
        "equipment": ["tencere", "tava"],
        "steps": [
            "Spagettiyi bol tuzlu suda al dente haşla; yarım bardak suyunu ayır.",
            "Sarımsağı ince dilimle, zeytinyağında kısık-orta ateşte yakmadan çevir.",
            "Pul biber kullanıyorsan sarımsak kokusu çıkınca ekle.",
            "Makarnayı tavaya al; ayırdığın sudan ekleyerek parlak bir sos oluştur.",
            "Maydanoz ve peynirle bitir."
        ],
        "critical_tips": ["Sarımsak yanarsa bütün yemek acılaşır; amaç kızartmak değil yağa kokusunu geçirmek."],
        "tags": ["makarna", "az malzemeli", "hızlı"],
        "quality_score": 92
    },
    {
        "id": "tr-tavuklu-pilav-curated",
        "name": "Tavuklu Pilav",
        "cuisine": "Türk",
        "category": "Pilav",
        "time_min": 45,
        "difficulty": "Orta",
        "servings": 4,
        "required_ingredients": ["tavuk", "pirinç", "tereyağı"],
        "optional_ingredients": ["şehriye", "limon", "karabiber", "tavuk suyu"],
        "pantry_items": ["su", "tuz"],
        "substitutions": {"pirinç": ["bulgur"], "tereyağı": ["zeytinyağı"]},
        "equipment": ["tencere"],
        "steps": [
            "Tavuğu tuzlu suda haşla; suyunu pilavda kullanmak için ayır.",
            "Pirinci yıka, nişastası gidene kadar süz ve mümkünse 10 dakika beklet.",
            "Tereyağında şehriye kullanıyorsan hafif renk aldır; ardından pirinci ekle ve kavur.",
            "Sıcak tavuk suyunu ekle, kapağı kapatıp kısık ateşte pişir.",
            "Pilavı 10 dakika dinlendir, didiklenmiş tavukla servis et."
        ],
        "critical_tips": ["Pilavın tane tane olması için piştikten sonra karıştırmadan dinlendir."],
        "tags": ["tavuk", "pilav", "protein"],
        "quality_score": 91
    }
]


def get_extra_recipes(existing_ids: set[str] | None = None) -> list[dict]:
    existing_ids = existing_ids or set()
    return [recipe for recipe in CURATED_EXTRA_RECIPES if recipe.get("id") not in existing_ids]
