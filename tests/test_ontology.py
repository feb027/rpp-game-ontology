from pathlib import Path

from rdflib import Graph, Namespace, RDF, OWL, Literal


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_PATH = ROOT / "ontology" / "game_recommendation.owl"
EX = Namespace("http://example.org/game-recommendation#")


def load_graph() -> Graph:
    graph = Graph()
    graph.parse(ONTOLOGY_PATH)
    return graph


def assert_named(graph: Graph, name: str, rdf_type) -> None:
    assert (EX[name], RDF.type, rdf_type) in graph, f"Missing {name} as {rdf_type}"


def test_core_ontology_vocabulary_matches_dosen_methontology_components():
    graph = load_graph()

    for class_name in [
        "Game",
        "Genre",
        "Mood",
        "Platform",
        "PlayMode",
        "Difficulty",
        "Duration",
        "PlayerPreference",
        "Recommendation",
    ]:
        assert_named(graph, class_name, OWL.Class)

    for property_name in [
        "hasGenre",
        "availableOn",
        "hasPlayMode",
        "hasDifficulty",
        "hasDuration",
        "suitableForMood",
        "matchesPreference",
        "recommendsGame",
        "basedOnMood",
        "basedOnPreference",
    ]:
        assert_named(graph, property_name, OWL.ObjectProperty)

    for property_name in ["gameTitle", "recommendationReason", "priorityScore"]:
        assert_named(graph, property_name, OWL.DatatypeProperty)


def test_ontology_contains_all_demo_game_instances():
    graph = load_graph()

    expected_games = {
        "StardewValley": "Stardew Valley",
        "Minecraft": "Minecraft",
        "Valorant": "Valorant",
        "GenshinImpact": "Genshin Impact",
        "CandyCrush": "Candy Crush",
        "Overcooked2": "Overcooked 2",
        "TheWitcher3": "The Witcher 3",
        "AnimalCrossing": "Animal Crossing",
    }

    for individual_name, title in expected_games.items():
        assert_named(graph, individual_name, OWL.NamedIndividual)
        assert (EX[individual_name], RDF.type, EX.Game) in graph
        assert (EX[individual_name], EX.gameTitle, Literal(title)) in graph


def test_sparql_recommendation_queries_have_expected_results():
    graph = load_graph()

    stress_pc_query = """
    PREFIX ex: <http://example.org/game-recommendation#>
    SELECT ?game WHERE {
      ?game a ex:Game ;
            ex:suitableForMood ex:Stres ;
            ex:availableOn ex:PC ;
            ex:hasGenre ex:Casual ;
            ex:hasDifficulty ex:Mudah .
    }
    """
    stress_games = {row.game.split("#")[-1] for row in graph.query(stress_pc_query)}
    assert "StardewValley" in stress_games

    competitive_query = """
    PREFIX ex: <http://example.org/game-recommendation#>
    SELECT ?game WHERE {
      ?game a ex:Game ;
            ex:suitableForMood ex:Kompetitif ;
            ex:availableOn ex:PC ;
            ex:hasPlayMode ex:Multiplayer ;
            ex:hasGenre ex:FPS .
    }
    """
    competitive_games = {row.game.split("#")[-1] for row in graph.query(competitive_query)}
    assert competitive_games == {"Valorant"}


def test_recommendation_individuals_include_reason_and_score():
    graph = load_graph()

    recommendation = EX.Recommendation_Stardew_Stress_PC
    assert (recommendation, RDF.type, EX.Recommendation) in graph
    assert (recommendation, EX.recommendsGame, EX.StardewValley) in graph
    assert (recommendation, EX.basedOnMood, EX.Stres) in graph
    reasons = list(graph.objects(recommendation, EX.recommendationReason))
    scores = list(graph.objects(recommendation, EX.priorityScore))
    assert reasons and "Stres" in str(reasons[0])
    assert scores and int(scores[0]) > 0
