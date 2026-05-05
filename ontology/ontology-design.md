# Ontology Design Summary

## Namespace
`http://example.org/game-recommendation#`

## Core Classes

```text
Thing
├── Game
├── Genre
├── Mood
├── Platform
├── PlayMode
├── Difficulty
├── Duration
├── PlayerPreference
└── Recommendation
```

## Core Object Properties

```text
Game --hasGenre--> Genre
Game --availableOn--> Platform
Game --hasPlayMode--> PlayMode
Game --hasDifficulty--> Difficulty
Game --hasDuration--> Duration
Game --suitableForMood--> Mood
Game --matchesPreference--> PlayerPreference
Recommendation --recommendsGame--> Game
Recommendation --basedOnMood--> Mood
Recommendation --basedOnPreference--> PlayerPreference
```

## Reasoning Model

A game is recommended if it satisfies a combination of:

1. mood match,
2. platform match,
3. genre/preference match,
4. play mode match,
5. duration/difficulty fit.

For the student demo, scoring can be implemented in Python while the ontology stores the structured knowledge. Protégé is still used to model and inspect the ontology.
