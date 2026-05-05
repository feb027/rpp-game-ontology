"""Seed knowledge base for the game recommendation demo."""

GAMES = [
    {
        "id": "stardew_valley",
        "title": "Stardew Valley",
        "genres": ["Simulation", "Casual"],
        "moods": ["Santai", "Stres"],
        "platforms": ["PC", "Console", "Mobile"],
        "modes": ["SinglePlayer", "Coop"],
        "difficulty": "Mudah",
        "durations": ["Sedang", "Panjang"],
    },
    {
        "id": "minecraft",
        "title": "Minecraft",
        "genres": ["Adventure", "Sandbox"],
        "moods": ["Eksploratif", "Sosial", "Bosan"],
        "platforms": ["PC", "Console", "Mobile"],
        "modes": ["SinglePlayer", "Multiplayer", "Coop"],
        "difficulty": "Sedang",
        "durations": ["Sedang", "Panjang"],
    },
    {
        "id": "valorant",
        "title": "Valorant",
        "genres": ["FPS"],
        "moods": ["Kompetitif", "Sosial"],
        "platforms": ["PC"],
        "modes": ["Multiplayer"],
        "difficulty": "Sulit",
        "durations": ["Singkat", "Sedang"],
    },
    {
        "id": "genshin_impact",
        "title": "Genshin Impact",
        "genres": ["RPG", "Adventure"],
        "moods": ["Eksploratif", "Santai"],
        "platforms": ["PC", "Mobile", "Console"],
        "modes": ["SinglePlayer", "Coop"],
        "difficulty": "Sedang",
        "durations": ["Sedang", "Panjang"],
    },
    {
        "id": "candy_crush",
        "title": "Candy Crush",
        "genres": ["Puzzle", "Casual"],
        "moods": ["Bosan", "Santai"],
        "platforms": ["Mobile"],
        "modes": ["SinglePlayer"],
        "difficulty": "Mudah",
        "durations": ["Singkat"],
    },
    {
        "id": "overcooked_2",
        "title": "Overcooked 2",
        "genres": ["Simulation", "Party"],
        "moods": ["Sosial", "Bosan"],
        "platforms": ["PC", "Console"],
        "modes": ["Coop", "Multiplayer"],
        "difficulty": "Sedang",
        "durations": ["Singkat", "Sedang"],
    },
    {
        "id": "the_witcher_3",
        "title": "The Witcher 3",
        "genres": ["RPG", "Adventure"],
        "moods": ["Eksploratif"],
        "platforms": ["PC", "Console"],
        "modes": ["SinglePlayer"],
        "difficulty": "Sedang",
        "durations": ["Panjang"],
    },
    {
        "id": "animal_crossing",
        "title": "Animal Crossing",
        "genres": ["Simulation", "Casual"],
        "moods": ["Santai", "Stres"],
        "platforms": ["Console"],
        "modes": ["SinglePlayer", "Multiplayer"],
        "difficulty": "Mudah",
        "durations": ["Sedang"],
    },
]

MOODS = ["Santai", "Kompetitif", "Stres", "Bosan", "Eksploratif", "Sosial"]
GENRES = sorted({genre for game in GAMES for genre in game["genres"]})
PLATFORMS = sorted({platform for game in GAMES for platform in game["platforms"]})
MODES = sorted({mode for game in GAMES for mode in game["modes"]})
DURATIONS = ["Singkat", "Sedang", "Panjang"]
DIFFICULTIES = ["Mudah", "Sedang", "Sulit"]
