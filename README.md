# Şahvername V0.2

**Şahvername**, kullanıcının elindeki malzemelere göre gerçekten yapılabilir yemek tariflerini uyum yüzdesiyle sıralayan bir tarif öneri programıdır.

Ana fikir:

> Evde ne varsa, Şahvername sana ondan bir sofra kurar.

## Özellikler

- Malzeme seçimine göre tarif önerme
- Uyum yüzdesi hesaplama
- Eksik zorunlu malzeme gösterimi
- Opsiyonel malzeme eşleşmesi
- Mutfak, kategori, süre ve eksik malzeme toleransı filtreleri
- Tarif adımları, alternatif malzeme ve püf noktası sekmeleri
- 31 elle düzenlenmiş çekirdek tarif + genişletilmiş başlangıç kataloğu
- Filtreler çok dar kalırsa otomatik “en yakın tarifler” fallback’i

## Kurulum

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Proje yapısı

```text
sahvername/
├─ app.py
├─ data/
│  └─ recipes_seed.json
├─ engine/
│  ├─ extra_recipes.py
│  ├─ matcher.py
│  ├─ normalizer.py
│  └─ scoring.py
├─ tests/
│  └─ test_engine.py
├─ requirements.txt
└─ README.md
```

## Tarif havuzu mantığı

Şahvername iki katmanlı çalışır:

1. `data/recipes_seed.json`: elle düzenlenmiş çekirdek tarifler.
2. `engine/extra_recipes.py`: MVP'nin çok daha fazla malzeme kombinasyonunda sonuç verebilmesi için genişletilmiş başlangıç kataloğu.

Bu yapı ileride SQLite veya gerçek tarif yönetim paneline geçene kadar hızlı geliştirme sağlar.

## Tarif kabul standardı

Şahvername'e eklenecek tariflerde şu alanlar mümkün olduğunca dolu olmalıdır:

- `required_ingredients`: tarif için gerçekten şart malzemeler
- `optional_ingredients`: lezzet artıran ama şart olmayan malzemeler
- `substitutions`: alternatif malzeme önerileri
- `steps`: uygulanabilir, kısa ve net tarif adımları
- `critical_tips`: sonucu iyileştiren püf noktaları
- `quality_score`: 0-100 arası kalite/kürasyon puanı

## Sonraki geliştirme fikirleri

- SQLite veri tabanı
- Tarif ekleme/düzenleme ekranı
- Alışveriş listesi üretme
- Dolap modu ve son kullanma tarihi takibi
- Besin değeri ve protein/kalori modu
- Kullanıcı beğenilerine göre kişiselleştirme
- API/dataset destekli geniş tarif havuzu
