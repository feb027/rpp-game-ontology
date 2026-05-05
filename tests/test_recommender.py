from collections import Counter

from app.data import GAMES
from app.recommender import recommend_games


def test_demo_dataset_is_large_enough_for_coursework():
    assert len(GAMES) >= 18

    mood_counts = Counter(mood for game in GAMES for mood in game["moods"])
    assert mood_counts["Kompetitif"] >= 3
    assert mood_counts["Stres"] >= 3
    assert all(mood_counts[mood] >= 3 for mood in ["Santai", "Bosan", "Eksploratif", "Sosial"])


def test_recommendation_for_stress_returns_relaxing_game():
    results = recommend_games(
        mood="Stres",
        genre="Casual",
        platform="PC",
        mode="SinglePlayer",
        duration="Sedang",
        difficulty="Mudah",
    )
    assert results
    assert any(item.title == "Stardew Valley" for item in results)
    assert results[0].score > 0


def test_competitive_pc_multiplayer_recommends_competitive_options():
    results = recommend_games(
        mood="Kompetitif",
        genre="FPS",
        platform="PC",
        mode="Multiplayer",
        duration="Singkat",
        difficulty="Sulit",
        limit=5,
    )
    titles = [item.title for item in results]
    assert results
    assert titles[0] == "Valorant"
    assert {"Counter-Strike 2", "Apex Legends"}.issubset(set(titles))
