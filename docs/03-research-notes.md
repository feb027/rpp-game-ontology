# Research Notes — Protégé, Methontology, dan Ontologi Rekomendasi Game

Tanggal akses semua sumber: 2026-05-05.

## 1. Ringkasan untuk Slide

### Slide A — Cara Unduh dan Instalasi Protégé

Poin utama:
- Gunakan Protégé Desktop sebagai tools utama untuk membuat ontologi OWL/RDF.
- Sumber resmi unduhan: halaman Software Protégé Stanford dan GitHub release resmi `protegeproject/protege-distribution`.
- Versi yang tercatat pada sumber resmi saat riset: Protégé Desktop 5.6.9.
- Protégé tersedia gratis, open source, mendukung OWL 2, dan ada juga WebProtégé untuk kerja kolaboratif berbasis browser.
- Paket Windows, macOS, dan Linux sudah menyertakan 64-bit Java Runtime Environment (JRE), sehingga Java tidak perlu diinstal terpisah untuk paket platform-spesifik. Untuk platform-independent package, Java tetap relevan.

Langkah instalasi ringkas:
1. Buka halaman resmi Protégé: https://protege.stanford.edu/software/
2. Pilih download Protégé Desktop sesuai OS.
3. Alternatif: buka GitHub release terbaru: https://github.com/protegeproject/protege-distribution/releases/latest
4. Windows: unduh `Protege-5.6.9-win.zip`, extract, jalankan `Protege.exe` atau `run.bat`.
5. Linux: unduh `Protege-5.6.9-linux.tar.gz`, extract dengan `tar zxvf Protege-5.6.9-linux.tar.gz`, masuk folder hasil extract, jalankan `./protege`.
6. macOS: unduh `Protege-5.6.9-mac.zip`, extract, drag aplikasi Protégé ke Applications, lalu jalankan.
7. Buat shortcut jika perlu agar mudah dibuka saat demo.

Catatan slide:
- Tekankan sumber resmi dan versi tools.
- Jangan tampilkan screenshot palsu; ambil screenshot langsung dari perangkat saat sudah menginstal.

Target screenshot yang perlu dibuat nanti:
- Halaman download Protégé resmi.
- File hasil download sesuai OS.
- Folder hasil extract/install.
- Tampilan awal Protégé Desktop setelah dibuka.

### Slide B — Pengenalan Lingkungan Kerja Protégé

Poin utama:
- Protégé adalah OWL ontology development environment.
- Tab penting: Active Ontology, Entities, Classes, Object Properties, Data Properties, Individuals, DL Query.
- Active Ontology menampilkan ringkasan ontology aktif, annotation, imports, dan metrics.
- Entities tab adalah pusat navigasi untuk classes, properties, dan individuals.
- Workspace Protégé terdiri dari tab dan view. View dapat di-resize, dipindah, di-float, di-split, dan ditumpuk.
- Pemilihan entity bersifat global: jika class/property/individual dipilih di panel kiri, detailnya tampil di panel kanan.
- Search global bisa diakses dengan tombol Search atau `Ctrl+F`/`Cmd+F`.
- Reasoner seperti HermiT digunakan untuk klasifikasi dan inferensi.

Target screenshot yang perlu dibuat nanti:
- Active Ontology tab.
- Entities tab.
- Class hierarchy: `Game`, `Mood`, `Genre`, `Platform`, `Recommendation`.
- Object Properties tab: contoh `hasMood`, `hasGenre`, `recommendedForMood`.
- Individuals tab: contoh `StardewValley`, `Santai`, `PC`.
- Reasoner menu dengan HermiT.
- Inferred Class Hierarchy setelah reasoning.
- DL Query tab.

### Slide C/D/E — Konsep Ontologi untuk Kasus Rekomendasi Game

Poin utama:
- OWL 2 merepresentasikan pengetahuan memakai classes, properties, individuals, dan data values.
- Class = kategori/konsep, misalnya `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `Recommendation`.
- Individual = objek/instance nyata dalam domain, misalnya `StardewValley`, `Minecraft`, `Santai`, `Kompetitif`, `PC`, `Mobile`.
- Object property = relasi antar-individual, misalnya `hasGenre`, `availableOn`, `suitableForMood`, `hasPlayMode`.
- Data property = relasi individual ke nilai data, misalnya `hasEstimatedDurationMinutes`, `hasReleaseYear`, `hasRecommendationScore`.
- Annotation property = metadata untuk label/deskripsi, misalnya `rdfs:label` dan `rdfs:comment`.
- Reasoner = alat inferensi yang menghitung konsekuensi logis dari axioms, misalnya mengklasifikasikan game sebagai `RelaxingGame` jika punya genre casual/simulation dan cocok untuk mood santai.
- Dalam Protégé, informasi hasil inferensi ditandai sebagai inferred information, biasanya berbeda dari asserted information.
- DL Query dipakai untuk menguji ekspresi rekomendasi, misalnya mencari game yang cocok untuk mood santai, tersedia di PC, dan durasi singkat.

Contoh model untuk slide:
- Class hierarchy:
  - `Thing`
    - `Game`
      - `RelaxingGame`
      - `CompetitiveGame`
      - `ExplorationGame`
    - `Mood`
      - `RelaxedMood`
      - `CompetitiveMood`
      - `BoredMood`
    - `Genre`
    - `Platform`
    - `PlayMode`
    - `Difficulty`
    - `Duration`
    - `Recommendation`
- Object properties:
  - `hasGenre`: `Game -> Genre`
  - `availableOn`: `Game -> Platform`
  - `hasPlayMode`: `Game -> PlayMode`
  - `hasDifficulty`: `Game -> Difficulty`
  - `suitableForMood`: `Game -> Mood`
  - `recommendedGame`: `Recommendation -> Game`
- Data properties:
  - `hasReasonText`: `Recommendation -> xsd:string`
  - `hasScore`: `Recommendation -> xsd:decimal`
- Individuals:
  - `StardewValley rdf:type Game`
  - `Simulation rdf:type Genre`
  - `Santai rdf:type Mood`
  - `PC rdf:type Platform`

Contoh DL Query untuk demo:
```text
Game and suitableForMood value Santai and availableOn value PC
```

Contoh rule/axiom konseptual:
```text
Game and hasGenre value Casual and suitableForMood value Santai -> RelaxingGame
```

Catatan: aturan di atas harus diterjemahkan ke bentuk OWL class expression/SWRL/rule sesuai pendekatan implementasi berikutnya.

## 2. Methontology untuk Coursework

Methontology adalah metodologi terstruktur untuk membangun ontologi dari awal. Sumber utama Fernández, Gómez-Pérez, dan Juristo (AAAI Spring Symposium 1997) menjelaskan bahwa Methontology bertujuan memberi urutan aktivitas, teknik, dan deliverable dalam ontology engineering, bukan sekadar membuat daftar istilah.

Tahapan yang cocok dipakai dalam tugas ini:

| Tahap | Makna | Output untuk proyek rekomendasi game |
|---|---|---|
| Specification | Menentukan tujuan, scope, pengguna, kebutuhan, dan competency questions | Dokumen tujuan: sistem merekomendasikan game berdasarkan mood + preferensi |
| Knowledge Acquisition | Mengumpulkan pengetahuan domain dari sumber, contoh game, genre, mood, dan preferensi pengguna | Daftar konsep game, mood, genre, platform, durasi, difficulty, mode |
| Conceptualization | Menyusun model konseptual: class, relasi, atribut, instance, rule/axiom | Diagram/tabel class hierarchy, object properties, data properties, individuals |
| Integration | Meninjau reuse konsep/ontology/vocabulary yang sudah ada | Gunakan OWL/RDF, pertimbangkan label `rdfs:label`, dan inspirasi Video Game Ontology |
| Implementation | Mengimplementasikan model ke tools ontology | File OWL/RDF dibuat di Protégé |
| Evaluation | Mengecek ontology dengan competency questions, reasoner, dan query | Uji DL Query/reasoner: apakah rekomendasi muncul sesuai mood + preferensi |
| Documentation | Mendokumentasikan ontology, asumsi domain, cara instalasi, demo, dan hasil evaluasi | Slide, research notes, tutorial video script, README demo |

Slide-ready bullets:
- Methontology membuat pengembangan ontologi lebih sistematis.
- Prosesnya iteratif/evolving prototype: jika ada konsep salah atau kurang, model boleh direvisi.
- Untuk tugas ini, Methontology dipakai sebagai alur kerja dari analisis kebutuhan sampai implementasi di Protégé dan evaluasi reasoner.
- Evaluation tidak hanya mengecek file bisa dibuka, tetapi mengecek apakah ontology menjawab competency questions.

Contoh competency questions:
- Game apa yang cocok untuk mood santai dan durasi bermain singkat?
- Game apa yang cocok untuk pemain kompetitif di platform PC?
- Game apa yang cocok untuk pemain yang ingin eksplorasi dan memilih single-player?
- Mengapa game tertentu direkomendasikan kepada user?

## 3. Inspirasi Ontologi dan Rekomendasi Game

### A. Ontologi untuk rekomendasi game digital berbasis profil pemain

Artikel `Uma ontologia para recomendação de jogos digitais / An ontology for recommending digital games` membangun ontologi untuk merekomendasikan game digital berdasarkan profil dan kemampuan pemain, memakai model BrainHex dan metodologi Noy. Untuk proyek ini, inspirasi yang berguna adalah pendekatan relasi antara profil pemain, fitur game, dan output rekomendasi.

Adaptasi ke tugas:
- Profil pemain dapat disederhanakan menjadi mood + preferensi.
- Fitur game dapat berupa genre, platform, mode, durasi, dan difficulty.
- Rekomendasi diberi alasan agar output bisa dijelaskan di slide/demo.

### B. Video Game Ontology (VGO) untuk interoperabilitas dan pemodelan game

Paper `An ontology for videogame interoperability` memperkenalkan Video Game Ontology sebagai model untuk interoperabilitas game dan analisis gameplay. Walaupun fokusnya bukan mood recommendation, VGO relevan sebagai inspirasi struktur domain game: game, gameplay/session, data game, dan representasi knowledge graph.

Adaptasi ke tugas:
- Gunakan class `Game` sebagai pusat domain.
- Hubungkan game dengan metadata/faktor rekomendasi.
- Evaluasi ontology dengan pertanyaan kompetensi agar tidak hanya berupa daftar game.

### C. Ludo ontology untuk serious games dan rekomendasi resource

Paper `Ludo: An Ontology to Create Linked Data Driven Serious Games` menunjukkan ontology yang memodelkan serious games, profil pemain, konteks, dan rekomendasi resource pembelajaran. Inspirasi utamanya adalah pemanfaatan profil/konteks pemain untuk membuat rekomendasi lebih personal.

Adaptasi ke tugas:
- Mood = konteks pengguna saat bermain.
- Preferensi platform/genre/mode = bagian dari profil pengguna.
- Output rekomendasi harus bisa memberi alasan berbasis relasi ontology.

## 4. Source Notes dan Referensi Langsung

| No | Sumber | Tanggal sumber | Tanggal akses | Ringkasan kegunaan |
|---|---|---:|---:|---|
| 1 | Protégé Software — Stanford: https://protege.stanford.edu/software/ | halaman berjalan/current | 2026-05-05 | Sumber resmi untuk download Protégé, membedakan WebProtégé dan Protégé Desktop, menyatakan dukungan OWL 2/RDF dan reasoner seperti HermiT/Pellet. |
| 2 | Protégé GitHub Release Latest: https://github.com/protegeproject/protege-distribution/releases/latest | release 5.6.9, 2026-03-07 menurut halaman GitHub | 2026-05-05 | Sumber release resmi untuk versi terbaru, catatan Java >= 11 sampai Java 25 untuk platform-independent version, dan arsip unduhan. |
| 3 | Protégé Linux Installation: https://protegeproject.github.io/protege/installation/linux/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Langkah install Linux: unduh tar.gz, extract, jalankan `./protege`; paket Linux menyertakan 64-bit JRE. |
| 4 | Protégé Windows Installation: https://protegeproject.github.io/protege/installation/windows/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Langkah install Windows: unduh zip, extract, jalankan `Protege.exe` atau `run.bat`; paket Windows menyertakan 64-bit JRE. |
| 5 | Protégé Mac OS X Installation: https://protegeproject.github.io/protege/installation/osx/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Langkah install macOS: unduh zip, drag app ke Applications, izinkan via Privacy & Security jika macOS memblokir. |
| 6 | Protégé Getting Started: https://protegeproject.github.io/protege/getting-started/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Pengenalan workspace: Active Ontology, Entities tab, classes/properties/individuals, navigation, search, HermiT reasoner, inferred hierarchy, DL Query. |
| 7 | Protégé Class Description View: https://protegeproject.github.io/protege/views/class-description/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Detail editor class: EquivalentTo, SubClassOf, Instances, DisjointWith, inferred information, Manchester OWL Syntax. |
| 8 | Protégé Object Property Description View: https://protegeproject.github.io/protege/views/object-property-description/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Detail object property: equivalent, subproperty, inverse, domain, range, disjoint, property chain. Penting untuk menjelaskan relasi ontology. |
| 9 | Protégé Individual Description View: https://protegeproject.github.io/protege/views/individual-description/ | dokumentasi Protégé 5.6.9 | 2026-05-05 | Detail individual: Types/ClassAssertions, SameIndividual, DifferentIndividuals, dan inferred named types. |
| 10 | Protégé DL Query Tab: https://protegewiki.stanford.edu/wiki/DLQueryTab | halaman wiki Protégé | 2026-05-05 | DL Query hanya berjalan pada ontology yang sudah diklasifikasi oleh reasoner; mendukung query Manchester OWL Syntax. |
| 11 | W3C OWL 2 Primer: https://www.w3.org/TR/owl2-primer/ | W3C Recommendation, 2012-12-11 | 2026-05-05 | Definisi OWL 2, classes, properties, individuals, data values, open-world assumption, dan reasoners. Cocok untuk teori slide. |
| 12 | AAAI — Methontology: https://aaai.org/papers/0005-ss97-06-005-methontology-from-ontological-art-towards-ontological-engineering/ | AAAI Spring Symposium 1997 | 2026-05-05 | Sumber akademik utama Methontology; menjelaskan metodologi terstruktur untuk membangun ontologi dari awal. |
| 13 | PDF UPM — Methontology: https://oa.upm.es/5484/1/METHONTOLOGY_.pdf | 1997 | 2026-05-05 | PDF langsung paper Methontology, berisi fase specification, knowledge acquisition, conceptualization, integration, implementation, evaluation, documentation. |
| 14 | Andrade et al. — An ontology for recommending digital games: https://ojs.brazilianjournals.com.br/ojs/index.php/BJHR/article/download/62513/44987/152178 | 2023, accepted 2023-08-25 | 2026-05-05 | Contoh langsung ontology untuk rekomendasi game digital berdasarkan profil/kemampuan pemain; relevan untuk inspirasi domain. |
| 15 | Parkkila et al. — An ontology for videogame interoperability: https://link.springer.com/article/10.1007/s11042-016-3552-6 | published 2016-05-17; volume 2017 | 2026-05-05 | Contoh Video Game Ontology untuk interoperabilitas dan conceptualization/evaluation domain game. |
| 16 | Ludo ontology paper: https://inria.hal.science/hal-01188202v1/document | 2015 | 2026-05-05 | Contoh ontology serious games yang memakai profil/konteks pemain dan Linked Data untuk rekomendasi resource. |

## 5. Materi Siap Pakai untuk Narasi Slide

### Narasi instalasi

"Tools yang digunakan adalah Protégé Desktop. Protégé dipilih karena gratis, open source, mendukung OWL 2/RDF, dan memiliki integrasi reasoner seperti HermiT. Instalasi dilakukan dari sumber resmi Protégé Stanford atau GitHub release resmi. Setelah file sesuai OS diunduh, pengguna cukup mengekstrak paket dan menjalankan aplikasi."

### Narasi lingkungan Protégé

"Lingkungan kerja Protégé terdiri dari beberapa tab. Active Ontology menampilkan informasi ontology aktif. Entities tab menjadi pusat untuk melihat class, property, dan individual. Class hierarchy digunakan untuk menyusun konsep, Object/Data Properties untuk membuat relasi, Individuals untuk membuat instance, dan Reasoner/DL Query untuk menguji inferensi ontology."

### Narasi konsep OWL

"Dalam OWL, class merepresentasikan kategori seperti Game atau Mood. Individual merepresentasikan contoh nyata seperti StardewValley atau Santai. Property menghubungkan individual, misalnya game memiliki genre atau cocok untuk mood tertentu. Reasoner kemudian membaca axioms tersebut untuk menghasilkan informasi baru, misalnya mengelompokkan game sebagai RelaxingGame."

### Narasi Methontology

"Pengembangan ontology mengikuti Methontology. Pertama, specification menentukan tujuan dan competency questions. Kedua, knowledge acquisition mengumpulkan konsep domain. Ketiga, conceptualization menyusun class, property, individual, dan rule. Keempat, integration mempertimbangkan reuse konsep atau standar. Kelima, implementation membuat ontology di Protégé. Keenam, evaluation menguji hasil dengan reasoner dan query. Terakhir, documentation menyimpan semua keputusan desain dan hasil pengujian."

## 6. Checklist untuk Task Berikutnya

- [ ] Buat ontology specification berdasarkan class/property/individual di catatan ini.
- [ ] Tentukan competency questions final.
- [ ] Implementasikan file OWL/RDF di Protégé atau generator OWL yang kompatibel dengan Protégé.
- [ ] Siapkan data contoh game minimal 8–12 individual.
- [ ] Jalankan reasoner dan dokumentasikan query hasil rekomendasi.
- [ ] Ambil screenshot asli dari Protégé setelah ontology dibuat, bukan gambar generik.
