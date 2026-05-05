# Artefak Methontology — Ontologi Rekomendasi Game

Dokumen ini menjadi intermediate representation teknis sebelum/selain implementasi formal di OWL. Struktur mengikuti materi RPP-13: glossary of terms, concept taxonomies, concept dictionary, ad hoc binary relation, attributes, formal axioms, rules, dan instances.

## 1. Specification

| Elemen | Isi |
|---|---|
| Nama ontologi | Ontologi Rekomendasi Game Berdasarkan Preferensi dan Mood |
| Tujuan | Merepresentasikan pengetahuan untuk merekomendasikan game berdasarkan mood dan preferensi bermain |
| Pengguna akhir | Mahasiswa/presenter/demo user yang ingin memilih game sesuai kondisi mood |
| Scope | Mood, genre, platform, mode bermain, tingkat kesulitan, durasi, preferensi, game, rekomendasi |
| Out of scope | Machine learning, login user, API game real-time, histori personal jangka panjang |
| Bahasa formal | OWL/RDF, kompatibel dengan Protégé |
| Evaluasi utama | Competency questions, DL Query/SPARQL, parse OWL, unit test app |

## 2. Knowledge Acquisition Summary

Pengetahuan domain dikumpulkan dari:

- Materi RPP-12/RPP-13 tentang ontologi, OWL/RDF, Protégé, dan Methontology.
- Contoh game umum yang mudah dipahami saat demo kelas.
- Asumsi knowledge engineering: mood tertentu dipetakan ke karakteristik game tertentu.
- Preferensi user yang umum dipakai dalam rekomendasi game: genre, platform, mode, durasi, dan difficulty.

## 3. Glossary of Terms

| Term | Sinonim/label | Tipe | Deskripsi |
|---|---|---|---|
| Game | Permainan digital | Concept | Entitas game yang dapat direkomendasikan |
| Genre | Kategori gameplay | Concept | Jenis permainan seperti RPG, FPS, Casual |
| Mood | Kondisi emosional | Concept | Kondisi pengguna saat memilih game |
| Platform | Perangkat bermain | Concept | Media menjalankan game: PC, Mobile, Console |
| PlayMode | Mode bermain | Concept | SinglePlayer, Multiplayer, Coop |
| Difficulty | Tingkat kesulitan | Concept | Mudah, Sedang, Sulit |
| Duration | Durasi sesi | Concept | Singkat, Sedang, Panjang |
| PlayerPreference | Preferensi pemain | Concept | Pilihan/kecenderungan user terhadap game |
| Recommendation | Rekomendasi | Concept | Hasil rekomendasi yang menunjuk game tertentu |
| hasGenre | memiliki genre | Relation | Relasi Game ke Genre |
| availableOn | tersedia pada | Relation | Relasi Game ke Platform |
| suitableForMood | cocok untuk mood | Relation | Relasi Game ke Mood |
| recommendsGame | merekomendasikan game | Relation | Relasi Recommendation ke Game |
| gameTitle | judul game | Attribute | Nilai teks judul game |
| recommendationReason | alasan rekomendasi | Attribute | Narasi alasan rekomendasi |
| priorityScore | skor prioritas | Attribute | Skor sederhana untuk ranking rekomendasi |

## 4. Concept Taxonomy

```text
Thing
├── Game
│   ├── RelaxingGame
│   ├── CompetitiveGame
│   ├── ExplorationGame
│   └── SocialGame
├── Genre
├── Mood
├── Platform
├── PlayMode
├── Difficulty
├── Duration
├── PlayerPreference
└── Recommendation
```

Relasi taksonomi utama: `RelaxingGame`, `CompetitiveGame`, `ExplorationGame`, dan `SocialGame` adalah subclass dari `Game` untuk memudahkan penjelasan reasoning di Protégé.

## 5. Concept Dictionary

| Concept | Parent | Relations | Attributes | Example instances |
|---|---|---|---|---|
| Game | Thing | hasGenre, availableOn, hasPlayMode, hasDifficulty, hasDuration, suitableForMood, matchesPreference | gameTitle | StardewValley, Minecraft, Valorant |
| Genre | Thing | inverse dari hasGenre | - | Casual, RPG, FPS, Simulation |
| Mood | Thing | inverse dari suitableForMood | - | Santai, Stres, Kompetitif |
| Platform | Thing | inverse dari availableOn | - | PC, Mobile, Console |
| PlayMode | Thing | inverse dari hasPlayMode | - | SinglePlayer, Multiplayer, Coop |
| Difficulty | Thing | inverse dari hasDifficulty | - | Mudah, Sedang, Sulit |
| Duration | Thing | inverse dari hasDuration | - | Singkat, Sedang, Panjang |
| PlayerPreference | Thing | inverse dari matchesPreference/basedOnPreference | - | PreferCasual, PreferPC, PreferSinglePlayer |
| Recommendation | Thing | recommendsGame, basedOnMood, basedOnPreference | recommendationReason, priorityScore | Recommendation_Stardew_Stress_PC |

## 6. Ad Hoc Binary Relation Table

| Relation | Source concept | Target concept | Cardinality source→target | Inverse meaning | Deskripsi |
|---|---|---|---:|---|---|
| hasGenre | Game | Genre | 1..n | genreOfGame | Game dapat memiliki satu atau lebih genre |
| availableOn | Game | Platform | 1..n | platformForGame | Game tersedia pada satu atau lebih platform |
| hasPlayMode | Game | PlayMode | 1..n | playModeOfGame | Game mendukung satu atau lebih mode bermain |
| hasDifficulty | Game | Difficulty | 1 | difficultyOfGame | Game memiliki tingkat kesulitan utama |
| hasDuration | Game | Duration | 1..n | durationOfGame | Game cocok untuk satu atau lebih durasi sesi |
| suitableForMood | Game | Mood | 1..n | moodSuitableForGame | Game cocok untuk mood tertentu |
| matchesPreference | Game | PlayerPreference | 0..n | preferenceMatchedByGame | Game memenuhi preferensi user |
| recommendsGame | Recommendation | Game | 1 | gameRecommendedBy | Rekomendasi menunjuk game tertentu |
| basedOnMood | Recommendation | Mood | 1 | moodBasisForRecommendation | Rekomendasi didasarkan pada mood tertentu |
| basedOnPreference | Recommendation | PlayerPreference | 1..n | preferenceBasisForRecommendation | Rekomendasi didasarkan pada preferensi tertentu |

## 7. Instance Attribute Table

| Instance attribute | Concept | Value type | Range/default | Cardinality | Deskripsi |
|---|---|---|---|---:|---|
| gameTitle | Game | xsd:string | judul game | 1 | Judul game untuk tampilan user |
| recommendationReason | Recommendation | xsd:string | teks alasan | 1 | Narasi mengapa game direkomendasikan |
| priorityScore | Recommendation | xsd:integer | 0–100 | 1 | Skor prioritas sederhana |

## 8. Class Attribute Table

| Class attribute | Concept | Value type | Unit | Cardinality | Keterangan |
|---|---|---|---|---:|---|
| defaultRecommendationWeight | Recommendation | integer | poin | 0..1 | Konsep bobot default; diimplementasikan pada aplikasi sebagai scoring rule |
| preferredSessionLength | Duration | category | - | 0..1 | Konsep durasi umum: Singkat/Sedang/Panjang |
| challengeLevel | Difficulty | category | - | 1 | Konsep kesulitan: Mudah/Sedang/Sulit |

Catatan: class attribute ini lebih bersifat konseptual untuk dokumentasi Methontology. Implementasi praktis memakai individual dan data property agar mudah dibuka di Protégé.

## 9. Formal Axioms

| Axiom | Natural language | Formal/OWL-style expression | Referenced concepts/relations |
|---|---|---|---|
| A1 | Setiap rekomendasi harus menunjuk minimal satu game | `Recommendation SubClassOf recommendsGame some Game` | Recommendation, recommendsGame, Game |
| A2 | Setiap game harus memiliki minimal satu genre | `Game SubClassOf hasGenre some Genre` | Game, hasGenre, Genre |
| A3 | Setiap game harus tersedia minimal pada satu platform | `Game SubClassOf availableOn some Platform` | Game, availableOn, Platform |
| A4 | Game relaksasi adalah game yang cocok untuk Santai/Stres dan difficulty mudah/sedang | `RelaxingGame SubClassOf Game and suitableForMood some Mood` | RelaxingGame, suitableForMood, Mood |
| A5 | Game kompetitif adalah game yang cocok untuk mood Kompetitif dan mode Multiplayer | `CompetitiveGame SubClassOf Game and hasPlayMode value Multiplayer` | CompetitiveGame, hasPlayMode, Multiplayer |

## 10. Rules

| Rule | Deskripsi | Ekspresi konseptual | Output |
|---|---|---|---|
| R1 Mood Stres | Jika user stres, prioritaskan game mudah, santai, casual/simulation | `Mood=Stres ∧ Genre∈{Casual,Simulation} ∧ Difficulty=Mudah` | skor rekomendasi naik |
| R2 Mood Kompetitif | Jika user kompetitif, prioritaskan multiplayer, FPS/strategy, difficulty sedang/sulit | `Mood=Kompetitif ∧ Mode=Multiplayer ∧ Genre∈{FPS,Strategy}` | rekomendasi kompetitif |
| R3 Ingin Eksplorasi | Jika user ingin eksplorasi, prioritaskan Adventure/RPG/Sandbox dan sesi sedang/panjang | `Mood=Eksploratif ∧ Genre∈{Adventure,RPG,Sandbox}` | rekomendasi eksplorasi |
| R4 Ingin Sosial | Jika user ingin sosial, prioritaskan Coop/Multiplayer | `Mood=Sosial ∧ Mode∈{Coop,Multiplayer}` | rekomendasi sosial |
| R5 Durasi Singkat | Jika user punya waktu singkat, prioritaskan game dengan `Duration=Singkat` | `Duration=Singkat` | skor durasi naik |

Implementasi rule ada di `app/recommender.py`, sedangkan OWL menyimpan struktur pengetahuan yang menjadi basis penjelasan.

## 11. Instances Table

| Instance | Class | Key attributes/relations |
|---|---|---|
| StardewValley | Game, RelaxingGame | Casual, Simulation, Stres, Santai, PC/Console/Mobile, SinglePlayer/Coop, Mudah, Sedang/Panjang |
| Minecraft | Game, ExplorationGame | Adventure, Sandbox, Eksploratif/Sosial/Bosan, PC/Console/Mobile, SinglePlayer/Multiplayer/Coop |
| Valorant | Game, CompetitiveGame | FPS, Kompetitif/Sosial, PC, Multiplayer, Sulit, Singkat/Sedang |
| GenshinImpact | Game, ExplorationGame | RPG, Adventure, Eksploratif/Santai, PC/Mobile/Console, SinglePlayer/Coop |
| CandyCrush | Game, RelaxingGame | Puzzle, Casual, Bosan/Santai, Mobile, SinglePlayer, Mudah, Singkat |
| Overcooked2 | Game, SocialGame | Simulation, Party, Sosial/Bosan, PC/Console, Coop/Multiplayer |
| TheWitcher3 | Game, ExplorationGame | RPG, Adventure, Eksploratif, PC/Console, SinglePlayer, Panjang |
| AnimalCrossing | Game, RelaxingGame | Simulation, Casual, Santai/Stres, Console, SinglePlayer/Multiplayer, Mudah |
| Recommendation_Stardew_Stress_PC | Recommendation | recommendsGame StardewValley, basedOnMood Stres, priorityScore 15 |
| Recommendation_Valorant_Competitive_PC | Recommendation | recommendsGame Valorant, basedOnMood Kompetitif, priorityScore 14 |
| Recommendation_Minecraft_Exploration | Recommendation | recommendsGame Minecraft, basedOnMood Eksploratif, priorityScore 12 |

## 12. Evaluation Plan

| Evaluation target | Method | Artifact | Expected result |
|---|---|---|---|
| Syntax OWL | Parse dengan rdflib | `ontology/game_recommendation.owl` | Tidak error |
| Vocabulary completeness | Unit test | `tests/test_ontology.py` | Core class/property/individual ada |
| Competency questions | DL Query/SPARQL | `ontology/queries.md` | Query menghasilkan game sesuai expected result |
| App behavior | Unit test recommender | `tests/test_recommender.py` | Input stres menghasilkan Stardew Valley; kompetitif menghasilkan Valorant |
| Demo run | Streamlit smoke test | `app/main.py` | App terbuka dan menampilkan rekomendasi |
| Manual Protégé validation | Buka OWL di Protégé + reasoner | `ontology/game_recommendation.owl` | Ontologi terbaca dan struktur terlihat di tab Entities |
