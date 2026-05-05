# Panduan Protégé untuk Ontologi Rekomendasi Game

Dokumen ini dibuat untuk pengguna yang belum pernah memakai Protégé. Tujuannya: membuka file OWL, memahami struktur ontologi, menjalankan reasoner HermiT, menjalankan DL Query, dan mengambil screenshot/visualisasi untuk slide atau video tutorial.

## 1. File yang Dipakai

Gunakan file utama berikut:

```text
ontology/game_recommendation.owl
```

File ini sudah berisi:

- 18 individual game.
- Class utama: `Game`, `Genre`, `Mood`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, `Recommendation`.
- Subclass penjelas: `RelaxingGame`, `CompetitiveGame`, `ExplorationGame`, `SocialGame`.
- Object property: `hasGenre`, `availableOn`, `hasPlayMode`, `hasDifficulty`, `hasDuration`, `suitableForMood`, `matchesPreference`, `recommendsGame`, `basedOnMood`, `basedOnPreference`.
- Data property: `gameTitle`, `recommendationReason`, `priorityScore`.

Jika file OWL perlu dibuat ulang dari data aplikasi:

```bash
source .venv/bin/activate
python scripts/generate_ontology.py
```

Di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python scripts/generate_ontology.py
```

## 2. Unduh dan Instal Protégé

1. Buka situs Protégé:
   - <https://protege.stanford.edu/products.php#desktop-protege>
2. Unduh **Protégé Desktop** sesuai OS.
3. Ekstrak file ZIP.
4. Jalankan aplikasi:
   - Windows: klik `run.bat` atau `Protege.exe` jika tersedia.
   - Linux/macOS: jalankan script bawaan dari folder Protégé.
5. Jika diminta Java, gunakan Java yang direkomendasikan oleh paket Protégé. Protégé 5.x biasanya sudah menyertakan runtime atau memberi instruksi Java yang sesuai.

## 3. Membuka Ontologi di Protégé

1. Buka Protégé.
2. Pilih menu **File → Open...**.
3. Arahkan ke repo tugas:

   ```text
   rpp-game-ontology/ontology/game_recommendation.owl
   ```

4. Klik **Open**.
5. Jika muncul dialog format/IRI, pilih default saja.
6. Pastikan tab **Active Ontology** menampilkan IRI:

   ```text
   http://example.org/game-recommendation#GameRecommendationOntology
   ```

## 4. Mengenal Area Kerja Protégé

Tab yang paling penting untuk tugas ini:

| Tab/View | Fungsi | Yang perlu ditunjukkan di video |
|---|---|---|
| **Active Ontology** | Metadata ontology | Nama ontology dan komentar/deskripsi |
| **Entities → Classes** | Struktur class/taksonomi | `Game`, `Genre`, `Mood`, `Recommendation`, subclass game |
| **Entities → Object properties** | Relasi antar individual | `hasGenre`, `suitableForMood`, `recommendsGame` |
| **Entities → Data properties** | Atribut literal | `gameTitle`, `recommendationReason`, `priorityScore` |
| **Entities → Individuals** | Data individual | `StardewValley`, `Valorant`, `CounterStrike2`, dst. |
| **DL Query** | Query berbasis logika OWL | Query rekomendasi game berdasarkan mood/preferensi |
| **OntoGraf** | Visualisasi graf ontology | Class/property/individual dalam bentuk node-edge |

Jika tab **DL Query** atau **OntoGraf** belum muncul, buka:

```text
Window → Tabs → DL Query
Window → Tabs → OntoGraf
```

Jika tidak ada, cek menu:

```text
File → Check for plugins...
```

Lalu cari plugin **DL Query** atau **OntoGraf** jika belum aktif.

## 5. Melihat Class Ontology

1. Buka tab **Entities**.
2. Pilih sub-tab **Classes**.
3. Klik `owl:Thing`.
4. Expand class berikut:
   - `Game`
   - `Genre`
   - `Mood`
   - `Platform`
   - `PlayMode`
   - `Difficulty`
   - `Duration`
   - `PlayerPreference`
   - `Recommendation`
5. Klik class `Game`.
6. Lihat bagian kanan:
   - **Description**: informasi class.
   - **SubClass Of**: relasi subclass.
   - **Instances**: individual game.

Untuk video, rekam bagian ini sambil menjelaskan:

> Class `Game` merepresentasikan game yang akan direkomendasikan. Subclass seperti `RelaxingGame`, `CompetitiveGame`, `ExplorationGame`, dan `SocialGame` dipakai untuk mengelompokkan game berdasarkan karakteristik umum.

## 6. Melihat Individual Game

1. Buka **Entities → Individuals**.
2. Cari dan klik contoh berikut:
   - `StardewValley`
   - `Valorant`
   - `CounterStrike2`
   - `ApexLegends`
   - `Unpacking`
3. Lihat bagian kanan pada **Property assertions**.
4. Contoh yang harus terlihat pada `StardewValley`:
   - `gameTitle` → `Stardew Valley`
   - `hasGenre` → `Simulation`, `Casual`
   - `suitableForMood` → `Santai`, `Stres`
   - `availableOn` → `PC`, `Console`, `Mobile`
   - `hasDifficulty` → `Mudah`
   - `hasDuration` → `Sedang`, `Panjang`

Narasi video:

> Individual merepresentasikan data nyata. Misalnya `StardewValley` adalah individual dari class `Game`, kemudian diberi property genre, mood, platform, mode, tingkat kesulitan, dan durasi bermain.

## 7. Menjalankan Reasoner HermiT

Langkah normal:

1. Buka menu **Reasoner**.
2. Pilih **HermiT**.
3. Klik:

   ```text
   Reasoner → Start reasoner
   ```

4. Tunggu sampai selesai.
5. Jika berhasil, bagian inferred hierarchy akan aktif.

Untuk mengecek konsistensi:

```text
Reasoner → Explain inconsistent ontology
```

atau lihat tanda/error pada bagian bawah Protégé.

### Jika Muncul Error `InconsistentOntologyException`

Error yang kamu alami:

```text
org.semanticweb.owlapi.reasoner.InconsistentOntologyException: Inconsistent ontology
```

Penyebab pada versi sebelumnya kemungkinan besar adalah bentrok datatype:

- property `recommendationReason` diberi range `xsd:string`.
- tetapi nilai reason disimpan sebagai literal bahasa Indonesia `@id` / `rdf:langString`.
- HermiT bisa menganggap `rdf:langString` tidak cocok dengan range `xsd:string`.

Sudah diperbaiki di generator. Sekarang `recommendationReason` dibuat sebagai literal bertipe:

```text
xsd:string
```

bukan literal dengan language tag.

Setelah pull/update repo, lakukan:

```bash
source .venv/bin/activate
python scripts/generate_ontology.py
python -m pytest -q
```

Di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python scripts/generate_ontology.py
python -m pytest -q
```

Lalu buka ulang file OWL di Protégé:

```text
File → Close
File → Open... → ontology/game_recommendation.owl
Reasoner → HermiT
Reasoner → Start reasoner
```

Jika masih error:

1. Tutup Protégé.
2. Buka lagi file `ontology/game_recommendation.owl` yang terbaru.
3. Pastikan tidak membuka file OWL lama dari folder download/temp.
4. Jalankan **Reasoner → Start reasoner** lagi.
5. Jika masih inconsistent, buka **Reasoner → Explain inconsistent ontology** dan screenshot hasilnya.

## 8. DL Query untuk Demo Rekomendasi

Buka tab:

```text
Window → Tabs → DL Query
```

Aktifkan reasoner HermiT dulu, lalu jalankan query berikut.

### Query 1 — Game untuk mood stres, casual, PC, mudah

```text
Game and suitableForMood value Stres and hasGenre value Casual and availableOn value PC and hasDifficulty value Mudah
```

Expected result:

- `StardewValley`
- `Unpacking`
- `Journey`

### Query 2 — Game kompetitif, PC, multiplayer, FPS

```text
Game and suitableForMood value Kompetitif and availableOn value PC and hasPlayMode value Multiplayer and hasGenre value FPS
```

Expected result:

- `Valorant`
- `CounterStrike2`
- `ApexLegends`

### Query 3 — Game eksploratif di PC

```text
Game and suitableForMood value Eksploratif and availableOn value PC
```

Expected result:

- `Minecraft`
- `GenshinImpact`
- `TheWitcher3`
- `Terraria`
- `HollowKnight`
- `CivilizationVi`
- `Journey`

### Query 4 — Recommendation untuk Stardew Valley

```text
Recommendation and recommendsGame value StardewValley
```

Expected result:

- `Recommendation_Stardew_Stress_PC`

Catatan penting: jika hasil yang muncul hanya `owl:Nothing`, biasanya kamu sedang melihat bagian **Subclasses**. Itu normal karena ekspresi query tidak punya subclass. Untuk tugas rekomendasi game, hasil yang dicari adalah bagian **Instances / Individuals**. Di panel hasil DL Query, aktifkan/lihat checkbox atau section **Instances** dan abaikan `owl:Nothing` pada bagian Subclasses.

Jika bagian Instances tetap kosong, cek tiga hal:

1. Reasoner sudah aktif.
2. Nama individual persis sama, misalnya `Stres`, bukan `Stress`.
3. Query memakai Manchester Syntax, bukan SPARQL.
4. Pastikan ontology sudah konsisten. Jika HermiT masih inconsistent, tutup Protégé lalu buka ulang file OWL terbaru dari `ontology/game_recommendation.owl`.

## 9. SPARQL Query Alternatif

SPARQL bisa dijalankan dari Python/rdflib atau tool RDF lain. Query lengkap ada di:

```text
ontology/queries.md
```

Untuk demo cepat via terminal:

```bash
source .venv/bin/activate
python - <<'PY'
from rdflib import Graph

g = Graph()
g.parse('ontology/game_recommendation.owl')

q = '''
PREFIX ex: <http://example.org/game-recommendation#>
SELECT ?game ?title WHERE {
  ?game a ex:Game ;
        ex:gameTitle ?title ;
        ex:suitableForMood ex:Kompetitif ;
        ex:availableOn ex:PC ;
        ex:hasPlayMode ex:Multiplayer ;
        ex:hasGenre ex:FPS .
}
'''

for row in g.query(q):
    print(row.game, row.title)
PY
```

Expected:

```text
http://example.org/game-recommendation#Valorant Valorant
http://example.org/game-recommendation#CounterStrike2 Counter-Strike 2
http://example.org/game-recommendation#ApexLegends Apex Legends
```

## 10. Visualisasi Ontology dengan OntoGraf

OntoGraf cocok untuk screenshot slide/video karena menampilkan node dan relasi.

Langkah:

1. Buka:

   ```text
   Window → Tabs → OntoGraf
   ```

2. Pada OntoGraf, klik tombol tambah/entity selection.
3. Tambahkan node berikut agar graf tidak terlalu ramai:
   - `Game`
   - `Mood`
   - `Genre`
   - `Platform`
   - `Recommendation`
   - `StardewValley`
   - `Valorant`
   - `CounterStrike2`
   - `ApexLegends`
   - `Unpacking`
   - `Stres`
   - `Kompetitif`
   - `Casual`
   - `FPS`
   - `PC`
4. Klik kanan node tertentu lalu pilih opsi untuk menampilkan connected entities / properties jika tersedia.
5. Rapikan posisi node dengan drag manual.
6. Screenshot area graf.

Rekomendasi visual untuk slide:

- Jangan tampilkan semua 18 game sekaligus karena graf akan padat.
- Buat 2 screenshot:
  1. Screenshot class hierarchy: `Game`, `Mood`, `Genre`, `Recommendation`.
  2. Screenshot contoh rekomendasi: `StardewValley`, `Stres`, `Casual`, `PC`, `Recommendation_Stardew_Stress_PC`.

Narasi video:

> Visualisasi ini menunjukkan bagaimana ontologi menghubungkan game dengan mood, genre, platform, dan rekomendasi. Node merepresentasikan class atau individual, sedangkan edge merepresentasikan property seperti `suitableForMood`, `hasGenre`, dan `availableOn`.

## 11. Screenshot yang Wajib Diambil untuk Slide/Video

Ambil screenshot berikut:

| No | Screenshot | Lokasi di Protégé | Fungsi di presentasi/video |
|---:|---|---|---|
| 1 | Active Ontology | Active Ontology | Bukti file OWL terbuka |
| 2 | Class hierarchy | Entities → Classes | Menjelaskan class dan taxonomy |
| 3 | Object properties | Entities → Object properties | Menjelaskan relasi pengetahuan |
| 4 | Individual `StardewValley` | Entities → Individuals | Contoh data game santai/stres |
| 5 | Individual `Valorant`/`CounterStrike2` | Entities → Individuals | Contoh data kompetitif |
| 6 | DL Query stress/casual | DL Query | Bukti query rekomendasi jalan |
| 7 | DL Query competitive FPS | DL Query | Bukti query multi-kriteria jalan |
| 8 | OntoGraf visual | OntoGraf | Visualisasi relasi ontology |
| 9 | Streamlit app demo | Browser/app | Bukti perangkat lunak demo berjalan |

## 12. Alur Video Tutorial yang Disarankan

1. Pembukaan judul:
   - Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi.
2. Jelaskan masalah:
   - Pengguna bingung memilih game sesuai mood/preferensi.
3. Jelaskan solusi:
   - Ontologi memodelkan game, mood, genre, platform, mode, difficulty, duration, dan recommendation.
4. Buka Protégé dan file OWL.
5. Tunjukkan class hierarchy.
6. Tunjukkan object property dan data property.
7. Tunjukkan individual game.
8. Jalankan HermiT reasoner.
9. Jalankan DL Query.
10. Tunjukkan OntoGraf.
11. Jalankan aplikasi demo Streamlit.
12. Penutup:
   - Ontologi dapat dipakai sebagai basis pengetahuan untuk rekomendasi game.

## 13. Troubleshooting Cepat

| Masalah | Penyebab umum | Solusi |
|---|---|---|
| OWL tidak bisa dibuka | File path salah atau file belum tergenerate | Jalankan `python scripts/generate_ontology.py` |
| DL Query kosong | Reasoner belum aktif atau nama individual salah | Start HermiT, cek ejaan individual |
| HermiT inconsistent | Bentrok datatype/axiom | Pakai OWL terbaru, regenerate file, buka ulang Protégé |
| OntoGraf terlalu ramai | Terlalu banyak node ditampilkan | Tampilkan subset node saja |
| Individual tidak muncul di class | Reasoner belum refresh atau view belum reload | Klik ulang class, restart reasoner, reopen file |
| Query `Stress` gagal | Individual yang benar adalah `Stres` | Pakai nama Indonesia sesuai ontology |

## 14. Kalimat Penjelasan Singkat untuk Presentasi

> Ontologi ini dibangun menggunakan Protégé dengan pendekatan Methontology. Domain yang dimodelkan adalah rekomendasi game berdasarkan mood dan preferensi pemain. Class utama meliputi Game, Mood, Genre, Platform, PlayMode, Difficulty, Duration, PlayerPreference, dan Recommendation. Individual game diberi property seperti suitableForMood, hasGenre, availableOn, hasPlayMode, hasDifficulty, dan hasDuration. Reasoner HermiT digunakan untuk mengecek konsistensi ontology dan DL Query digunakan untuk membuktikan bahwa sistem dapat menemukan game yang sesuai dengan kriteria pengguna.
