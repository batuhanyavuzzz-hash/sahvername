# Şahvername V0.1

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
- Başlangıç için elle düzenlenmiş kaliteli seed tarif havuzu

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
│  ├─ matcher.py
│  ├─ normalizer.py
│  └─ scoring.py
├─ requirements.txt
└─ README.md
```

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
