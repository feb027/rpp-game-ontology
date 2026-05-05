"""Generate the Protégé-compatible OWL ontology from app seed data."""
from __future__ import annotations

from pathlib import Path
import sys

from rdflib import Graph, Literal, Namespace, RDF, RDFS, OWL, XSD
from rdflib.namespace import DC

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.data import DIFFICULTIES, DURATIONS, GAMES, GENRES, MODES, MOODS, PLATFORMS

EX = Namespace("http://example.org/game-recommendation#")
OUT = ROOT / "ontology" / "game_recommendation.owl"


def iri_from_game_id(game_id: str) -> str:
    return "".join(part.capitalize() for part in game_id.split("_"))


def preference_name(prefix: str, value: str) -> str:
    return f"Prefer{prefix}{value.replace('-', '').replace(' ', '')}"


def build_graph() -> Graph:
    graph = Graph()
    graph.bind("", EX)
    graph.bind("owl", OWL)
    graph.bind("rdf", RDF)
    graph.bind("rdfs", RDFS)
    graph.bind("xsd", XSD)
    graph.bind("dc", DC)

    ontology = EX.GameRecommendationOntology
    graph.add((ontology, RDF.type, OWL.Ontology))
    graph.add((ontology, RDFS.label, Literal("Ontologi Rekomendasi Game Berdasarkan Preferensi dan Mood", lang="id")))
    graph.add((ontology, RDFS.comment, Literal("Ontologi tugas besar RPP untuk memodelkan game, mood, preferensi bermain, dan rekomendasi berbasis pengetahuan.", lang="id")))

    classes = {
        "Game": "Entitas game yang dapat direkomendasikan.",
        "Genre": "Kategori gameplay game.",
        "Mood": "Kondisi emosional pengguna saat memilih game.",
        "Platform": "Perangkat tempat game dimainkan.",
        "PlayMode": "Mode bermain game.",
        "Difficulty": "Tingkat kesulitan game.",
        "Duration": "Estimasi durasi sesi bermain.",
        "PlayerPreference": "Preferensi pengguna dalam memilih game.",
        "Recommendation": "Hasil rekomendasi beserta dasar dan alasannya.",
        "RelaxingGame": "Game yang cocok untuk suasana santai atau mengurangi stres.",
        "CompetitiveGame": "Game yang cocok untuk mood kompetitif.",
        "ExplorationGame": "Game yang cocok untuk eksplorasi.",
        "SocialGame": "Game yang cocok untuk bermain sosial.",
    }
    for name, comment in classes.items():
        graph.add((EX[name], RDF.type, OWL.Class))
        graph.add((EX[name], RDFS.label, Literal(name)))
        graph.add((EX[name], RDFS.comment, Literal(comment, lang="id")))
    for subclass in ["RelaxingGame", "CompetitiveGame", "ExplorationGame", "SocialGame"]:
        graph.add((EX[subclass], RDFS.subClassOf, EX.Game))

    object_properties = {
        "hasGenre": ("Game", "Genre", "Game memiliki genre tertentu."),
        "availableOn": ("Game", "Platform", "Game tersedia pada platform tertentu."),
        "hasPlayMode": ("Game", "PlayMode", "Game memiliki mode bermain tertentu."),
        "hasDifficulty": ("Game", "Difficulty", "Game memiliki tingkat kesulitan tertentu."),
        "hasDuration": ("Game", "Duration", "Game cocok untuk durasi sesi tertentu."),
        "suitableForMood": ("Game", "Mood", "Game cocok untuk mood tertentu."),
        "matchesPreference": ("Game", "PlayerPreference", "Game cocok dengan preferensi pengguna tertentu."),
        "recommendsGame": ("Recommendation", "Game", "Rekomendasi menunjuk game tertentu."),
        "basedOnMood": ("Recommendation", "Mood", "Rekomendasi didasarkan pada mood tertentu."),
        "basedOnPreference": ("Recommendation", "PlayerPreference", "Rekomendasi didasarkan pada preferensi tertentu."),
    }
    for name, (domain, range_, comment) in object_properties.items():
        graph.add((EX[name], RDF.type, OWL.ObjectProperty))
        graph.add((EX[name], RDFS.domain, EX[domain]))
        graph.add((EX[name], RDFS.range, EX[range_]))
        graph.add((EX[name], RDFS.label, Literal(name)))
        graph.add((EX[name], RDFS.comment, Literal(comment, lang="id")))

    data_properties = {
        "gameTitle": ("Game", XSD.string, "Judul game."),
        "recommendationReason": ("Recommendation", XSD.string, "Alasan naratif rekomendasi."),
        "priorityScore": ("Recommendation", XSD.integer, "Skor prioritas rekomendasi."),
    }
    for name, (domain, dtype, comment) in data_properties.items():
        graph.add((EX[name], RDF.type, OWL.DatatypeProperty))
        graph.add((EX[name], RDFS.domain, EX[domain]))
        graph.add((EX[name], RDFS.range, dtype))
        graph.add((EX[name], RDFS.label, Literal(name)))
        graph.add((EX[name], RDFS.comment, Literal(comment, lang="id")))

    for collection, cls in [
        (MOODS, "Mood"),
        (GENRES, "Genre"),
        (PLATFORMS, "Platform"),
        (MODES, "PlayMode"),
        (DURATIONS, "Duration"),
        (DIFFICULTIES, "Difficulty"),
    ]:
        for item in collection:
            graph.add((EX[item], RDF.type, OWL.NamedIndividual))
            graph.add((EX[item], RDF.type, EX[cls]))
            graph.add((EX[item], RDFS.label, Literal(item)))

    preference_comments: dict[str, str] = {}
    for genre in GENRES:
        preference_comments[preference_name("", genre)] = f"Preferensi genre {genre}."
    for platform in PLATFORMS:
        preference_comments[preference_name("", platform)] = f"Preferensi platform {platform}."
    for mode in MODES:
        preference_comments[preference_name("", mode)] = f"Preferensi mode {mode}."
    for duration in DURATIONS:
        preference_comments[preference_name("", duration)] = f"Preferensi durasi {duration}."
    for difficulty in DIFFICULTIES:
        preference_comments[preference_name("", difficulty)] = f"Preferensi difficulty {difficulty}."

    for pref, comment in sorted(preference_comments.items()):
        graph.add((EX[pref], RDF.type, OWL.NamedIndividual))
        graph.add((EX[pref], RDF.type, EX.PlayerPreference))
        graph.add((EX[pref], RDFS.label, Literal(pref)))
        graph.add((EX[pref], RDFS.comment, Literal(comment, lang="id")))

    category_by_game = {
        "StardewValley": "RelaxingGame",
        "AnimalCrossing": "RelaxingGame",
        "CandyCrush": "RelaxingGame",
        "TheSims4": "RelaxingGame",
        "Unpacking": "RelaxingGame",
        "Journey": "RelaxingGame",
        "Valorant": "CompetitiveGame",
        "LeagueOfLegends": "CompetitiveGame",
        "CounterStrike2": "CompetitiveGame",
        "ApexLegends": "CompetitiveGame",
        "CivilizationVi": "CompetitiveGame",
        "Minecraft": "ExplorationGame",
        "GenshinImpact": "ExplorationGame",
        "TheWitcher3": "ExplorationGame",
        "Terraria": "ExplorationGame",
        "HollowKnight": "ExplorationGame",
        "Overcooked2": "SocialGame",
        "AmongUs": "SocialGame",
    }

    for game in GAMES:
        node = EX[iri_from_game_id(game["id"])]
        graph.add((node, RDF.type, OWL.NamedIndividual))
        graph.add((node, RDF.type, EX.Game))
        graph.add((node, EX.gameTitle, Literal(game["title"])))
        graph.add((node, RDFS.label, Literal(game["title"])))
        if iri_from_game_id(game["id"]) in category_by_game:
            graph.add((node, RDF.type, EX[category_by_game[iri_from_game_id(game["id"])] ]))

        for genre in game["genres"]:
            graph.add((node, EX.hasGenre, EX[genre]))
            graph.add((node, EX.matchesPreference, EX[preference_name("", genre)]))
        for mood in game["moods"]:
            graph.add((node, EX.suitableForMood, EX[mood]))
        for platform in game["platforms"]:
            graph.add((node, EX.availableOn, EX[platform]))
            graph.add((node, EX.matchesPreference, EX[preference_name("", platform)]))
        for mode in game["modes"]:
            graph.add((node, EX.hasPlayMode, EX[mode]))
            graph.add((node, EX.matchesPreference, EX[preference_name("", mode)]))
        graph.add((node, EX.hasDifficulty, EX[game["difficulty"]]))
        graph.add((node, EX.matchesPreference, EX[preference_name("", game["difficulty"])]))
        for duration in game["durations"]:
            graph.add((node, EX.hasDuration, EX[duration]))
            graph.add((node, EX.matchesPreference, EX[preference_name("", duration)]))

    recommendations = [
        ("Recommendation_Stardew_Stress_PC", "StardewValley", "Stres", ["Casual", "PC", "SinglePlayer", "Mudah", "Sedang"], 15, "Stardew Valley direkomendasikan untuk mood Stres karena cocok dengan genre Casual/Simulation, tersedia di PC, mode SinglePlayer, durasi Sedang, dan difficulty Mudah."),
        ("Recommendation_Valorant_Competitive_PC", "Valorant", "Kompetitif", ["FPS", "PC", "Multiplayer", "Singkat", "Sulit"], 15, "Valorant direkomendasikan untuk mood Kompetitif karena genre FPS, tersedia di PC, mode Multiplayer, durasi Singkat/Sedang, dan difficulty Sulit."),
        ("Recommendation_CounterStrike_Competitive_PC", "CounterStrike2", "Kompetitif", ["FPS", "PC", "Multiplayer", "Singkat", "Sulit"], 15, "Counter-Strike 2 direkomendasikan sebagai opsi kompetitif FPS karena tersedia di PC, mode Multiplayer, sesi Singkat/Sedang, dan difficulty Sulit."),
        ("Recommendation_Apex_Competitive_Social", "ApexLegends", "Kompetitif", ["FPS", "PC", "Multiplayer", "Singkat", "Sulit"], 15, "Apex Legends direkomendasikan untuk kompetitif sekaligus sosial karena FPS BattleRoyale berbasis tim, mode Multiplayer, dan tersedia di PC/Console."),
        ("Recommendation_Unpacking_Stress", "Unpacking", "Stres", ["Casual", "PC", "SinglePlayer", "Mudah", "Singkat"], 14, "Unpacking cocok untuk mood Stres karena gameplay puzzle-casual ringan, single-player, dan sesi singkat."),
        ("Recommendation_Minecraft_Exploration", "Minecraft", "Eksploratif", ["Adventure", "PC", "Multiplayer", "Panjang"], 12, "Minecraft direkomendasikan untuk mood Eksploratif karena mendukung eksplorasi, tersedia di banyak platform, dan dapat dimainkan sendiri maupun bersama."),
    ]
    for rec, game, mood, prefs, score, reason in recommendations:
        graph.add((EX[rec], RDF.type, OWL.NamedIndividual))
        graph.add((EX[rec], RDF.type, EX.Recommendation))
        graph.add((EX[rec], RDFS.label, Literal(rec)))
        graph.add((EX[rec], EX.recommendsGame, EX[game]))
        graph.add((EX[rec], EX.basedOnMood, EX[mood]))
        for pref_value in prefs:
            graph.add((EX[rec], EX.basedOnPreference, EX[preference_name("", pref_value)]))
        graph.add((EX[rec], EX.priorityScore, Literal(score, datatype=XSD.integer)))
        # Keep this as xsd:string, not a language-tagged literal, because
        # recommendationReason has range xsd:string. HermiT treats langString
        # values on an xsd:string property as a datatype clash and can report
        # the ontology as inconsistent.
        graph.add((EX[rec], EX.recommendationReason, Literal(reason, datatype=XSD.string)))

    return graph


if __name__ == "__main__":
    graph = build_graph()
    OUT.write_text(graph.serialize(format="xml"), encoding="utf-8")
    print(f"wrote {OUT} with {len(graph)} triples")
