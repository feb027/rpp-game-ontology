# Ontology Specification: Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood

## 1. Tujuan Ontologi

Ontologi ini merepresentasikan pengetahuan tentang hubungan antara mood pengguna, preferensi bermain, karakteristik game, dan rekomendasi game. Ontologi digunakan untuk membantu aplikasi demo menjelaskan mengapa suatu game direkomendasikan untuk kondisi pengguna tertentu.

## 2. Scope Ontologi

### In Scope
- Mood pengguna.
- Genre game.
- Platform game.
- Mode bermain.
- Durasi bermain.
- Tingkat kesulitan.
- Preferensi pengguna.
- Relasi kecocokan antara game dan mood/preferensi.
- Alasan rekomendasi.

### Out of Scope
- Prediksi rating berbasis machine learning.
- Data game real-time dari API eksternal.
- Personalisasi historis jangka panjang.
- Sistem login pengguna.

## 3. Competency Questions

1. Game apa yang cocok untuk pengguna dengan mood santai?
2. Game apa yang cocok untuk pengguna yang sedang stres dan ingin bermain santai?
3. Game apa yang cocok untuk pengguna dengan mood kompetitif?
4. Game apa yang tersedia di platform PC?
5. Game apa yang memiliki mode multiplayer atau co-op?
6. Game apa yang cocok untuk durasi bermain singkat?
7. Game apa yang cocok untuk pengguna yang menyukai genre RPG?
8. Game apa yang cocok untuk pengguna yang ingin eksplorasi?
9. Game apa yang cocok untuk pengguna yang ingin bermain sosial?
10. Mengapa game tertentu direkomendasikan untuk mood dan preferensi tertentu?

## 4. Kelas Utama

| Class | Deskripsi | Contoh Individu |
|---|---|---|
| `Game` | Entitas game yang dapat direkomendasikan | `StardewValley`, `Valorant`, `Minecraft` |
| `Genre` | Kategori gameplay game | `RPG`, `FPS`, `Simulation`, `Puzzle`, `Adventure` |
| `Mood` | Kondisi emosional pengguna saat memilih game | `Santai`, `Kompetitif`, `Stres`, `Bosan`, `Eksploratif`, `Sosial` |
| `Platform` | Perangkat tempat game dimainkan | `PC`, `Mobile`, `Console` |
| `PlayMode` | Mode bermain game | `SinglePlayer`, `Multiplayer`, `Coop` |
| `Difficulty` | Tingkat kesulitan game | `Mudah`, `Sedang`, `Sulit` |
| `Duration` | Estimasi durasi sesi bermain | `Singkat`, `Sedang`, `Panjang` |
| `PlayerPreference` | Preferensi pengguna | `PreferRPG`, `PreferMultiplayer`, `PreferShortSession` |
| `Recommendation` | Hasil rekomendasi dan alasan | `Recommendation_Stardew_Relax` |

## 5. Object Properties

| Property | Domain | Range | Makna |
|---|---|---|---|
| `hasGenre` | `Game` | `Genre` | Game memiliki genre tertentu |
| `availableOn` | `Game` | `Platform` | Game tersedia pada platform tertentu |
| `hasPlayMode` | `Game` | `PlayMode` | Game memiliki mode bermain tertentu |
| `hasDifficulty` | `Game` | `Difficulty` | Game memiliki tingkat kesulitan tertentu |
| `hasDuration` | `Game` | `Duration` | Game cocok untuk durasi sesi tertentu |
| `suitableForMood` | `Game` | `Mood` | Game cocok untuk mood tertentu |
| `matchesPreference` | `Game` | `PlayerPreference` | Game cocok dengan preferensi tertentu |
| `recommendsGame` | `Recommendation` | `Game` | Rekomendasi menunjuk ke game tertentu |
| `basedOnMood` | `Recommendation` | `Mood` | Rekomendasi didasarkan pada mood tertentu |
| `basedOnPreference` | `Recommendation` | `PlayerPreference` | Rekomendasi didasarkan pada preferensi tertentu |

## 6. Data Properties

| Property | Domain | Tipe | Makna |
|---|---|---|---|
| `gameTitle` | `Game` | `xsd:string` | Judul game |
| `recommendationReason` | `Recommendation` | `xsd:string` | Alasan naratif rekomendasi |
| `priorityScore` | `Recommendation` | `xsd:integer` | Skor prioritas sederhana |

## 7. Contoh Individu Game

| Game | Genre | Mood Cocok | Platform | Mode | Difficulty | Duration |
|---|---|---|---|---|---|---|
| Stardew Valley | Simulation, Casual | Santai, Stres | PC, Console, Mobile | SinglePlayer, Coop | Mudah | Sedang, Panjang |
| Minecraft | Adventure, Sandbox | Eksploratif, Sosial, Bosan | PC, Console, Mobile | SinglePlayer, Multiplayer, Coop | Sedang | Sedang, Panjang |
| Valorant | FPS | Kompetitif, Sosial | PC | Multiplayer | Sulit | Singkat, Sedang |
| Genshin Impact | RPG, Adventure | Eksploratif, Santai | PC, Mobile, Console | SinglePlayer, Coop | Sedang | Sedang, Panjang |
| Candy Crush | Puzzle, Casual | Bosan, Santai | Mobile | SinglePlayer | Mudah | Singkat |
| Overcooked 2 | Simulation, Party | Sosial, Bosan | PC, Console | Coop, Multiplayer | Sedang | Singkat, Sedang |
| The Witcher 3 | RPG, Adventure | Eksploratif | PC, Console | SinglePlayer | Sedang | Panjang |
| Animal Crossing | Simulation, Casual | Santai, Stres | Console | SinglePlayer, Multiplayer | Mudah | Sedang |

## 8. Strategi Reasoning

Untuk tugas ini, reasoning dibuat sederhana dan dapat dijelaskan:

1. **Ontology reasoning di Protégé**
   - Struktur kelas, properti, dan individu dibuat di Protégé.
   - Reasoner seperti HermiT digunakan untuk mengecek konsistensi ontology.
   - Relasi seperti `suitableForMood` dan `matchesPreference` menjadi dasar inferensi/rekomendasi.

2. **Rule-based reasoning di aplikasi demo**
   - Aplikasi membaca data ontology/seed knowledge.
   - Input pengguna dipetakan ke mood dan preferensi.
   - Game diberi skor jika memenuhi mood, genre, platform, mode, difficulty, dan duration.
   - Output menampilkan game dengan skor tertinggi dan alasan rekomendasi.

## 9. Contoh Aturan Rekomendasi

### Rule 1 — Mood Santai
Jika pengguna memilih mood `Santai`, maka sistem memprioritaskan game dengan genre `Casual`, `Simulation`, atau difficulty `Mudah`.

### Rule 2 — Mood Kompetitif
Jika pengguna memilih mood `Kompetitif`, maka sistem memprioritaskan game dengan mode `Multiplayer`, difficulty `Sedang/Sulit`, dan genre `FPS` atau `Strategy`.

### Rule 3 — Mood Stres
Jika pengguna memilih mood `Stres`, maka sistem memprioritaskan game dengan difficulty `Mudah`, mode `SinglePlayer`, dan genre `Casual` atau `Simulation`.

### Rule 4 — Ingin Sosial
Jika pengguna ingin bermain sosial, maka sistem memprioritaskan game dengan mode `Coop` atau `Multiplayer`.

### Rule 5 — Durasi Singkat
Jika pengguna hanya punya waktu singkat, maka sistem memprioritaskan game dengan `Duration = Singkat`.

## 10. Contoh Output Rekomendasi

### Input 1
- Mood: Stres
- Platform: PC
- Preferensi: Casual, single-player, mudah

### Output
- Stardew Valley — karena cocok untuk mood santai/stres, genre simulation/casual, difficulty mudah, dan tersedia di PC.
- Animal Crossing — karena cocok untuk mood santai/stres, difficulty mudah, dan gameplay ringan.

### Input 2
- Mood: Kompetitif
- Platform: PC
- Preferensi: multiplayer, sesi singkat

### Output
- Valorant — karena cocok untuk mood kompetitif, genre FPS, mode multiplayer, tersedia di PC, dan cocok untuk sesi singkat/sedang.

## 11. Mapping ke Methontology

| Tahap Methontology | Penerapan pada Studi Kasus |
|---|---|
| Specification | Menentukan tujuan sistem rekomendasi game berbasis mood/preferensi |
| Knowledge Acquisition | Mengumpulkan konsep game, mood, genre, platform, dan preferensi |
| Conceptualization | Menyusun class, property, individual, dan competency questions |
| Formalization | Merancang relasi formal menggunakan OWL concepts |
| Integration | Menghubungkan ontology dengan aplikasi demo Python |
| Implementation | Membuat file ontology dan demo app |
| Evaluation | Mengecek konsistensi ontology dan hasil rekomendasi |
| Documentation | Membuat slide, demo guide, dan script video |

## 12. Artifact Implementation Target

- `ontology/game_recommendation.owl` — file ontology untuk Protégé.
- `app/main.py` — aplikasi demo.
- `app/recommender.py` — logika rekomendasi.
- `app/data.py` — seed data game dan knowledge base.
- `requirements.txt` — dependency aplikasi.
- `docs/05-demo-app-guide.md` — panduan demo.
