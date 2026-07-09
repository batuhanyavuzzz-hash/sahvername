from __future__ import annotations

from pathlib import Path

import streamlit as st

from engine.matcher import all_ingredients, load_recipes, match_recipes


BASE_DIR = Path(__file__).resolve().parent
RECIPES_PATH = BASE_DIR / "data" / "recipes_seed.json"


st.set_page_config(
    page_title="Şahvername",
    page_icon="🍲",
    layout="wide",
)


@st.cache_data
def get_recipes() -> list[dict]:
    return load_recipes(RECIPES_PATH)


recipes = get_recipes()

st.title("🍲 Şahvername")
st.caption("Evde ne varsa, Şahvername sana ondan bir sofra kurar.")

with st.sidebar:
    st.header("Malzemeler")
    ingredients = all_ingredients(recipes)
    selected = st.multiselect(
        "Elindeki malzemeleri seç",
        options=ingredients,
        placeholder="Örn: tavuk, yoğurt, sarımsak...",
    )

    st.divider()
    st.header("Filtreler")
    cuisines = ["Tümü"] + sorted({r["cuisine"] for r in recipes})
    categories = ["Tümü"] + sorted({r["category"] for r in recipes})

    cuisine = st.selectbox("Mutfak", cuisines)
    category = st.selectbox("Kategori", categories)
    time_choice = st.selectbox("Maksimum süre", ["Fark etmez", "15 dk", "30 dk", "45 dk", "60 dk"])
    missing_choice = st.selectbox("Eksik zorunlu malzeme toleransı", [0, 1, 2, 3, "Fark etmez"], index=3)
    include_pantry = st.checkbox("Tuz, su, yağ gibi temel malzemeleri var say", value=True)
    min_score = st.slider("Minimum uyum skoru", min_value=0, max_value=100, value=25, step=5)

time_map = {"15 dk": 15, "30 dk": 30, "45 dk": 45, "60 dk": 60}
max_time = time_map.get(time_choice)
max_missing = None if missing_choice == "Fark etmez" else int(missing_choice)

if not selected:
    st.info("Soldan elindeki birkaç malzemeyi seç. İlk sonuçlar uyum yüzdesine göre sıralanacak.")
    st.subheader("Şahvername V0.2 veri havuzu")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tarif", len(recipes))
    col2.metric("Mutfak", len({r['cuisine'] for r in recipes}))
    col3.metric("Malzeme", len(all_ingredients(recipes)))
    col4.metric("Ortalama kalite", f"{round(sum(r.get('quality_score', 0) for r in recipes) / len(recipes))}/100")
    st.stop()

results = match_recipes(
    recipes,
    selected,
    cuisine=cuisine,
    category=category,
    max_time=max_time,
    max_missing_required=max_missing,
    include_default_pantry=include_pantry,
    min_score=min_score,
)

fallback_mode = False
if not results:
    fallback_mode = True
    st.warning(
        "Bu filtrelerle tam sonuç çıkmadı. Filtreleri gevşetip en yakın tarifleri gösteriyorum."
    )
    results = match_recipes(
        recipes,
        selected,
        cuisine="Tümü",
        category="Tümü",
        max_time=None,
        max_missing_required=None,
        include_default_pantry=include_pantry,
        min_score=0,
    )[:12]

if fallback_mode:
    st.subheader(f"En yakın {len(results)} tarif")
else:
    st.subheader(f"{len(results)} tarif bulundu")

if not results:
    st.error("Hiç yakın eşleşme bulunamadı. Tarif havuzuna bu malzeme ailesinden yeni tarif eklemek gerekir.")
    st.stop()

for result in results:
    recipe = result.recipe
    score = result.score
    missing = result.missing_required

    with st.container(border=True):
        left, right = st.columns([3, 1])
        with left:
            st.markdown(f"### {recipe['name']}")
            st.write(f"**Mutfak:** {recipe['cuisine']}  ·  **Kategori:** {recipe['category']}  ·  **Süre:** {recipe['time_min']} dk  ·  **Zorluk:** {recipe['difficulty']}")
            if missing:
                st.warning("Eksik zorunlu malzeme: " + ", ".join(missing))
            else:
                st.success("Eksik zorunlu malzeme yok. Bu tarif tam yapılabilir görünüyor.")
        with right:
            st.metric("Uyum", f"%{score}")
            st.caption(f"Kalite puanı: {recipe.get('quality_score', '-')}/100")

        tab1, tab2, tab3, tab4 = st.tabs(["Malzeme uyumu", "Tarif", "Alternatifler", "Püf noktası"])

        with tab1:
            c1, c2 = st.columns(2)
            c1.markdown("**Elindeki zorunlu malzemeler**")
            c1.write(", ".join(result.matched_required) if result.matched_required else "—")
            c1.markdown("**Elindeki opsiyonel malzemeler**")
            c1.write(", ".join(result.matched_optional) if result.matched_optional else "—")
            c2.markdown("**Eksik zorunlu malzemeler**")
            c2.write(", ".join(result.missing_required) if result.missing_required else "—")
            c2.markdown("**Eksik opsiyonel malzemeler**")
            c2.write(", ".join(result.missing_optional) if result.missing_optional else "—")

        with tab2:
            for i, step in enumerate(recipe.get("steps", []), start=1):
                st.write(f"{i}. {step}")

        with tab3:
            substitutions = recipe.get("substitutions", {})
            if substitutions:
                for item, alts in substitutions.items():
                    st.write(f"**{item}:** " + ", ".join(alts))
            else:
                st.write("Alternatif malzeme bilgisi yok.")

        with tab4:
            for tip in recipe.get("critical_tips", []):
                st.write("• " + tip)
            tags = recipe.get("tags", [])
            if tags:
                st.caption("Etiketler: " + ", ".join(tags))
