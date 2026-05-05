from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

# Streamlit may execute this file with app/ as sys.path[0], especially on Windows.
# Add the repository root so package imports like `app.data` work consistently.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.data import DIFFICULTIES, DURATIONS, GENRES, MODES, MOODS, PLATFORMS
from app.recommender import recommend_games

st.set_page_config(page_title="Game Ontology Recommender", page_icon="🎮", layout="centered")

st.title("🎮 Sistem Rekomendasi Game Berbasis Ontologi")
st.caption("Study Case: rekomendasi game berdasarkan preferensi dan mood menggunakan ontologi")

st.markdown(
    """
Aplikasi ini mendemonstrasikan sistem berbasis pengetahuan. Ontologi memodelkan
relasi antara **Game**, **Mood**, **Genre**, **Platform**, **PlayMode**, **Difficulty**,
dan **Duration**. Reasoning sederhana dilakukan dengan mencocokkan input pengguna
terhadap knowledge base.
"""
)

with st.sidebar:
    st.header("Input Preferensi")
    mood = st.selectbox("Mood saat ini", MOODS)
    genre = st.selectbox("Genre favorit", ["Bebas"] + GENRES)
    platform = st.selectbox("Platform", ["Bebas"] + PLATFORMS)
    mode = st.selectbox("Mode bermain", ["Bebas"] + MODES)
    duration = st.selectbox("Durasi bermain", ["Bebas"] + DURATIONS)
    difficulty = st.selectbox("Tingkat kesulitan", ["Bebas"] + DIFFICULTIES)

recommendations = recommend_games(mood, genre, platform, mode, duration, difficulty)

st.subheader("Hasil Rekomendasi")

if not recommendations:
    st.warning("Belum ada rekomendasi yang cocok. Coba longgarkan preferensi.")
else:
    for idx, rec in enumerate(recommendations, start=1):
        with st.container(border=True):
            st.markdown(f"### {idx}. {rec.title}")
            st.metric("Skor kecocokan", rec.score)
            st.markdown("**Alasan rekomendasi:**")
            for reason in rec.reasons:
                st.write(f"- {reason}")

st.divider()
st.markdown(
    """
**Catatan demo:** file ontology berada di `ontology/game_recommendation.owl` dan
bisa dibuka melalui Protégé. Aplikasi ini memakai data yang konsisten dengan
kelas, properti, dan individu yang dijelaskan pada ontology specification.
"""
)
