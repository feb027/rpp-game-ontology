from app.recommender import recommend_games


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


def test_competitive_pc_multiplayer_recommends_valorant():
    results = recommend_games(
        mood="Kompetitif",
        genre="FPS",
        platform="PC",
        mode="Multiplayer",
        duration="Singkat",
        difficulty="Sulit",
    )
    assert results
    assert results[0].title == "Valorant"
