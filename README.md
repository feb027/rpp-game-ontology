# Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi

Repo teknis untuk Tugas Besar **Representasi Pengetahuan dan Penalaran**.

Studi kasus: sistem berbasis pengetahuan yang merekomendasikan game berdasarkan mood pengguna dan preferensi bermain menggunakan ontologi yang kompatibel dengan **Protégé**.

## Fokus Repo

Repo ini difokuskan pada pengerjaan teknis:

- Ontologi OWL/RDF yang bisa dibuka di Protégé.
- Artefak Methontology sesuai materi dosen.
- Query/evaluasi ontology.
- Aplikasi demo Streamlit.
- Test otomatis untuk app dan ontology.

Slide dan video tutorial dibuat manual memakai artefak repo ini sebagai bahan.

## Mapping Tugas

| Poin tugas | Artefak utama |
|---|---|
| a. Cara unduh dan instalasi tools | `docs/03-research-notes.md`, `docs/06-slide-notes.md` |
| b. Pengenalan lingkungan kerja tools | `docs/03-research-notes.md`, `docs/06-slide-notes.md` |
| c. Deskripsi persoalan kasus | `docs/00-task-brief.md`, `docs/02-scope-and-acceptance.md`, `docs/04-ontology-specification.md` |
| d. Deskripsi solusi penyelesaian kasus | `docs/04-ontology-specification.md`, `docs/08-methontology-artifacts.md`, `ontology/ontology-design.md` |
| e. Penerapan kasus menggunakan tools | `ontology/game_recommendation.owl`, `ontology/queries.md` |
| f. Demo aplikasi | `app/`, `requirements.txt`, `tests/`, `docs/05-demo-app-guide.md` |

## Struktur Folder

```text
app/        aplikasi demo Streamlit dan logic rekomendasi
ontology/   file OWL/RDF, desain, dan query evaluasi
docs/       brief, scope, materi dosen, Methontology artifacts, QA
slides/     bahan/outline slide manual
video/      script/storyboard/checklist video manual
tests/      test app dan ontology
```

## Ontologi

File utama:

```text
ontology/game_recommendation.owl
```

Core class:

- `Game`
- `Genre`
- `Mood`
- `Platform`
- `PlayMode`
- `Difficulty`
- `Duration`
- `PlayerPreference`
- `Recommendation`

Contoh game individual berjumlah 18:

- `StardewValley`
- `Minecraft`
- `Valorant`
- `GenshinImpact`
- `CandyCrush`
- `Overcooked2`
- `TheWitcher3`
- `AnimalCrossing`
- `LeagueOfLegends`
- `CounterStrike2`
- `ApexLegends`
- `Terraria`
- `HollowKnight`
- `CivilizationVi`
- `TheSims4`
- `Unpacking`
- `Journey`
- `AmongUs`

Query evaluasi tersedia di:

```text
ontology/queries.md
```

Ontology OWL dapat diregenerasi dari seed data dengan:

```bash
python scripts/generate_ontology.py
```

Artefak Methontology tersedia di:

```text
docs/08-methontology-artifacts.md
```

Alignment dengan materi dosen tersedia di:

```text
docs/07-dosen-material-alignment.md
```

Panduan pemakaian Protégé, HermiT, DL Query, dan OntoGraf tersedia di:

```text
docs/09-protege-user-guide.md
```

## Cara Menjalankan App

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

Demo input yang direkomendasikan:

- Mood: `Stres`
- Genre: `Casual`
- Platform: `PC`
- Mode: `SinglePlayer`
- Durasi: `Sedang`
- Difficulty: `Mudah`

Expected top result:

- `Stardew Valley`

## Testing

```bash
source .venv/bin/activate
python -m pytest -q
```

Test mencakup:

- behavior rekomendasi app.
- parse dan vocabulary ontology.
- keberadaan 18 game individual di OWL.
- SPARQL smoke query untuk expected result.
- recommendation individual dengan reason dan score.

## Protégé Manual Check

1. Buka Protégé.
2. Open file `ontology/game_recommendation.owl`.
3. Cek tab **Entities**:
   - Classes
   - Object Properties
   - Data Properties
   - Individuals
4. Coba DL Query dari `ontology/queries.md`.
5. Jalankan reasoner jika tersedia untuk consistency check.

## Catatan Pengumpulan

Repo ini belum otomatis menyelesaikan bagian manusia:

- rekam/export video final,
- upload ke YouTube AIS,
- buat ZIP final,
- kirim ke ketua kelas.

Checklist pengumpulan ada di:

```text
docs/SUBMISSION_CHECKLIST.md
```
