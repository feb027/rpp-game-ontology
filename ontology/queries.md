# Ontology Query dan Evaluation Notes

File ini berisi query yang dapat dipakai untuk mengevaluasi ontology `game_recommendation.owl` di Protégé atau secara programatik dengan RDF/SPARQL.

## 1. DL Query untuk Protégé

Buka `ontology/game_recommendation.owl` di Protégé, aktifkan reasoner jika tersedia, lalu gunakan tab **DL Query**.

### CQ1 — Game apa yang cocok untuk mood stres, genre casual, platform PC, dan difficulty mudah?

```text
Game and suitableForMood value Stres and hasGenre value Casual and availableOn value PC and hasDifficulty value Mudah
```

Expected result:

- `StardewValley`

### CQ2 — Game apa yang cocok untuk mood kompetitif di PC dan mode multiplayer?

```text
Game and suitableForMood value Kompetitif and availableOn value PC and hasPlayMode value Multiplayer
```

Expected result:

- `Valorant`

### CQ3 — Game apa yang cocok untuk eksplorasi dan tersedia di PC?

```text
Game and suitableForMood value Eksploratif and availableOn value PC
```

Expected result:

- `Minecraft`
- `GenshinImpact`
- `TheWitcher3`

### CQ4 — Game apa yang cocok untuk sosial dan memiliki mode co-op/multiplayer?

```text
Game and suitableForMood value Sosial and (hasPlayMode value Coop or hasPlayMode value Multiplayer)
```

Expected result:

- `Minecraft`
- `Valorant`
- `Overcooked2`

### CQ5 — Rekomendasi apa yang menunjuk Stardew Valley?

```text
Recommendation and recommendsGame value StardewValley
```

Expected result:

- `Recommendation_Stardew_Stress_PC`

## 2. SPARQL Query

SPARQL dapat dijalankan melalui script Python/rdflib atau tools RDF yang mendukung SPARQL.

### SQ1 — Stress/Casual/PC/Easy

```sparql
PREFIX ex: <http://example.org/game-recommendation#>
SELECT ?game ?title WHERE {
  ?game a ex:Game ;
        ex:gameTitle ?title ;
        ex:suitableForMood ex:Stres ;
        ex:availableOn ex:PC ;
        ex:hasGenre ex:Casual ;
        ex:hasDifficulty ex:Mudah .
}
```

Expected:

| game | title |
|---|---|
| `ex:StardewValley` | `Stardew Valley` |

### SQ2 — Competitive Multiplayer PC

```sparql
PREFIX ex: <http://example.org/game-recommendation#>
SELECT ?game ?title WHERE {
  ?game a ex:Game ;
        ex:gameTitle ?title ;
        ex:suitableForMood ex:Kompetitif ;
        ex:availableOn ex:PC ;
        ex:hasPlayMode ex:Multiplayer ;
        ex:hasGenre ex:FPS .
}
```

Expected:

| game | title |
|---|---|
| `ex:Valorant` | `Valorant` |

### SQ3 — Recommendation Reason

```sparql
PREFIX ex: <http://example.org/game-recommendation#>
SELECT ?recommendation ?game ?reason ?score WHERE {
  ?recommendation a ex:Recommendation ;
                  ex:recommendsGame ?game ;
                  ex:basedOnMood ex:Stres ;
                  ex:recommendationReason ?reason ;
                  ex:priorityScore ?score .
}
```

Expected:

| recommendation | game | score |
|---|---|---:|
| `ex:Recommendation_Stardew_Stress_PC` | `ex:StardewValley` | 15 |

## 3. Python Smoke Check

```bash
python - <<'PY'
from rdflib import Graph

g = Graph()
g.parse('ontology/game_recommendation.owl')
print(len(g), 'triples')

q = '''
PREFIX ex: <http://example.org/game-recommendation#>
SELECT ?game ?title WHERE {
  ?game a ex:Game ;
        ex:gameTitle ?title ;
        ex:suitableForMood ex:Stres ;
        ex:availableOn ex:PC ;
        ex:hasGenre ex:Casual ;
        ex:hasDifficulty ex:Mudah .
}
'''
for row in g.query(q):
    print(row.game, row.title)
PY
```

Expected output includes:

```text
http://example.org/game-recommendation#StardewValley Stardew Valley
```

## 4. Evaluation Decision

Ontology dianggap valid untuk tugas ini jika:

- File OWL dapat dibuka di Protégé.
- Core class, property, dan individual muncul di tab Entities.
- DL Query/SPARQL menjawab competency questions.
- App demo menghasilkan rekomendasi yang konsisten dengan relasi ontology.
- Test suite lokal pass.
