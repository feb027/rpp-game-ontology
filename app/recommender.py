"""Rule-based reasoning layer for game recommendations.

The ontology stores structured knowledge. This module demonstrates the reasoning
logic used by the application: match mood + preferences and produce explainable
recommendations.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from app.data import GAMES


@dataclass(frozen=True)
class Recommendation:
    title: str
    score: int
    reasons: list[str]


def _contains(values: Iterable[str], selected: str | None) -> bool:
    return bool(selected) and selected != "Bebas" and selected in values


def recommend_games(
    mood: str,
    genre: str = "Bebas",
    platform: str = "Bebas",
    mode: str = "Bebas",
    duration: str = "Bebas",
    difficulty: str = "Bebas",
    limit: int = 5,
) -> list[Recommendation]:
    """Return ranked game recommendations with explainable reasons."""
    recommendations: list[Recommendation] = []

    for game in GAMES:
        score = 0
        reasons: list[str] = []

        if _contains(game["moods"], mood):
            score += 4
            reasons.append(f"cocok untuk mood {mood}")

        if _contains(game["genres"], genre):
            score += 3
            reasons.append(f"sesuai genre {genre}")

        if _contains(game["platforms"], platform):
            score += 2
            reasons.append(f"tersedia di platform {platform}")

        if _contains(game["modes"], mode):
            score += 2
            reasons.append(f"mendukung mode {mode}")

        if _contains(game["durations"], duration):
            score += 1
            reasons.append(f"cocok untuk durasi {duration}")

        if difficulty != "Bebas" and game["difficulty"] == difficulty:
            score += 1
            reasons.append(f"tingkat kesulitan {difficulty}")

        # Mood-specific heuristic rules from the ontology specification.
        if mood == "Stres" and game["difficulty"] == "Mudah":
            score += 2
            reasons.append("mudah dimainkan saat pengguna ingin menurunkan stres")
        if mood == "Kompetitif" and "Multiplayer" in game["modes"]:
            score += 2
            reasons.append("mode multiplayer mendukung suasana kompetitif")
        if mood == "Sosial" and any(m in game["modes"] for m in ["Coop", "Multiplayer"]):
            score += 2
            reasons.append("mendukung interaksi sosial/co-op")
        if mood == "Bosan" and "Singkat" in game["durations"]:
            score += 1
            reasons.append("bisa dimainkan cepat saat bosan")

        if score > 0:
            recommendations.append(Recommendation(game["title"], score, reasons))

    return sorted(recommendations, key=lambda item: item.score, reverse=True)[:limit]
