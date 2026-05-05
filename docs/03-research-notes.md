# Research Notes: Protégé, Methontology, dan Ontology-Based Game Recommendation

Tanggal akses: 2026-05-05

## 1. Protégé: Unduh dan Instalasi

### Sumber resmi
- Protégé Stanford — Software: https://protege.stanford.edu/software/
- Protégé 5 Documentation: https://protegeproject.github.io/protege/
- Install Protege5 Wiki: https://protegewiki.stanford.edu/wiki/Install_Protege5

### Poin penting
- Protégé tersedia sebagai **Protégé Desktop** dan **WebProtégé**.
- Keduanya gratis, open-source, dan mendukung **OWL 2 Web Ontology Language**.
- Protégé Desktop mendukung OWL 2, visualisasi struktur ontologi, refactoring ontology, serta koneksi ke reasoner seperti **HermiT** dan **Pellet**.
- Situs resmi mencantumkan **Protégé Desktop v5.6.9** sebagai versi desktop yang dapat diunduh.
- Platform independent version membutuhkan Java, sedangkan paket platform-specific biasanya lebih mudah untuk pengguna Windows/Mac/Linux.

### Slide-ready bullets
- Buka https://protege.stanford.edu/software/
- Pilih **Download for Desktop**.
- Pilih installer sesuai sistem operasi.
- Jalankan Protégé Desktop.
- Buat ontology baru atau buka file `.owl`.

## 2. Pengenalan Lingkungan Kerja Protégé

### Sumber resmi
- Getting Started: http://protegeproject.github.io/protege/getting-started/
- User Docs: https://protegewiki.stanford.edu/wiki/ProtegeDesktopUserDocs

### Komponen utama workspace
- **Active Ontology tab**: melihat metadata ontology, imports, annotations, dan metrics.
- **Entities tab**: area utama untuk mengelola classes, properties, dan individuals.
- **Classes**: konsep/domain utama, misalnya `Game`, `Mood`, `Genre`.
- **Object Properties**: relasi antar-individual, misalnya `hasGenre`, `recommendedForMood`.
- **Data Properties**: atribut literal, misalnya `hasTitle`, `hasRating`, `hasDurationMinutes`.
- **Individuals**: instance nyata, misalnya `StardewValley`, `RelaxedMood`, `RPGGenre`.
- **Reasoner menu**: menjalankan reasoner untuk inferensi.

### Reasoning di Protégé
- Dokumentasi Getting Started menjelaskan bahwa Protégé menyertakan reasoner **HermiT**.
- Reasoner dapat dijalankan melalui menu **Reasoner > HermiT**, lalu start reasoning dengan `Ctrl+R` atau `Cmd+R`.
- Hasil inferensi dapat muncul sebagai inferred hierarchy atau informasi dengan highlight tertentu.
- Reasoner lain seperti **Pellet** dan **FaCT++** dapat dipasang melalui plugin.

### Screenshot target untuk slide/video
- Halaman download Protégé.
- Tampilan awal Protégé Desktop.
- Active Ontology tab.
- Entities tab.
- Class hierarchy.
- Object Properties dan Data Properties.
- Individuals tab.
- Reasoner menu.

## 3. Methontology

### Sumber utama
- Fernández, M., Gómez-Pérez, A., & Juristo, N. (1997). *METHONTOLOGY: From Ontological Art Towards Ontological Engineering*. AAAI Technical Report SS-97-06. https://oa.upm.es/5484/1/METHONTOLOGY_.pdf

### Inti Methontology
Methontology adalah metodologi rekayasa ontologi yang bertujuan membuat pengembangan ontologi lebih sistematis, bukan sekadar ad-hoc. Paper aslinya menekankan aktivitas, urutan, teknik, life cycle berbasis evolving prototypes, dan dokumentasi pada setiap tahap.

### Aktivitas pengembangan ontologi
Berdasarkan paper Methontology, aktivitas penting mencakup:

1. **Planning** — merencanakan tugas, sumber daya, dan jadwal.
2. **Specification** — menentukan tujuan, pengguna, penggunaan, dan scope ontology.
3. **Knowledge Acquisition** — memperoleh pengetahuan dari sumber, pakar, dokumen, atau ontology lain.
4. **Conceptualization** — menyusun model konseptual berupa konsep, relasi, dan vocabulary domain.
5. **Formalization** — mengubah model konseptual menjadi model formal/semi-formal.
6. **Integration** — mempertimbangkan reuse/integrasi ontology lain.
7. **Implementation** — mengodekan ontology dalam bahasa formal seperti OWL.
8. **Evaluation** — memeriksa kualitas, konsistensi, dan kemampuan ontology menjawab kebutuhan.
9. **Documentation** — mendokumentasikan proses dan hasil pada seluruh tahap.
10. **Maintenance** — menjaga dan mengembangkan ontology setelah dibuat.

### Penerapan pada studi kasus game
- Specification: sistem merekomendasikan game berdasarkan mood dan preferensi.
- Knowledge acquisition: kumpulkan data genre, mood, platform, mode, difficulty, dan contoh game.
- Conceptualization: definisikan kelas `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`.
- Formalization: definisikan property seperti `hasGenre`, `availableOn`, `suitableForMood`, `hasDifficulty`.
- Implementation: buat ontology di Protégé dan simpan sebagai OWL/RDF.
- Evaluation: uji competency questions dan hasil rekomendasi.
- Documentation: slide, demo guide, dan script video.

## 4. Ontology-Based Recommendation dan Game Recommendation

### Sumber dan inspirasi
- Artikel terkait ontology untuk rekomendasi game berbasis profil pemain/BrainHex muncul dalam hasil pencarian dengan tema ontologi, recommendation system, player profile, dan OWL.
- VideOWL: https://github.com/Stefano-Angelo-Rizzo/VideOWL — contoh video-game OWL ontology yang dapat dibuka di Protégé dan memakai reasoner HermiT untuk inferensi genre.
- Literatur sistem rekomendasi berbasis semantic web menunjukkan bahwa ontology dapat menghubungkan konteks pengguna, preferensi, mood/situasi, dan item rekomendasi.

### Konsep yang bisa dipakai
- Ontology cocok untuk merepresentasikan pengetahuan yang terstruktur dan relasional.
- Rekomendasi dapat dijelaskan secara transparan: “direkomendasikan karena mood santai cocok dengan genre simulation/casual dan difficulty mudah”.
- Aturan rekomendasi dapat dibuat dengan kombinasi relasi OWL, query SPARQL, atau aturan aplikasi.

### Contoh competency questions
1. Game apa yang cocok untuk pengguna dengan mood santai?
2. Game apa yang cocok untuk mood kompetitif dan mode multiplayer?
3. Game apa yang tersedia di platform PC dan memiliki difficulty sedang?
4. Game apa yang cocok untuk durasi bermain singkat?
5. Genre apa yang paling sesuai untuk mood stres?
6. Game apa yang cocok untuk pengguna yang ingin eksplorasi?
7. Game apa yang direkomendasikan untuk pengguna yang ingin bermain sosial/co-op?
8. Mengapa suatu game direkomendasikan untuk mood tertentu?

## 5. Slide-Ready Structure

### Slide a — Cara unduh dan instalasi tools
- Jelaskan Protégé Desktop, link download resmi, pilihan platform, dan langkah install.

### Slide b — Pengenalan lingkungan kerja tools
- Jelaskan Active Ontology, Entities, Classes, Object Properties, Data Properties, Individuals, Reasoner.

### Slide c — Deskripsi persoalan kasus
- Banyak pilihan game membuat pengguna sulit memilih game yang sesuai mood dan preferensi.

### Slide d — Deskripsi solusi penyelesaian kasus
- Gunakan ontology untuk memodelkan mood, genre, platform, mode bermain, difficulty, duration, dan relasi rekomendasi.

### Slide e — Penerapan kasus menggunakan tools
- Tunjukkan kelas/properti/individu di Protégé, lalu contoh reasoning/rekomendasi.

## 6. Daftar Referensi

1. Protégé Stanford. “Software - Protégé.” https://protege.stanford.edu/software/ — diakses 2026-05-05.
2. Protégé Project. “Protégé 5 Documentation.” https://protegeproject.github.io/protege/ — diakses 2026-05-05.
3. Protégé Project. “Getting Started.” http://protegeproject.github.io/protege/getting-started/ — diakses 2026-05-05.
4. Protégé Wiki. “Install Protege5.” https://protegewiki.stanford.edu/wiki/Install_Protege5 — diakses 2026-05-05.
5. Protégé Wiki. “Protege Desktop User Documentation.” https://protegewiki.stanford.edu/wiki/ProtegeDesktopUserDocs — diakses 2026-05-05.
6. Fernández, M., Gómez-Pérez, A., & Juristo, N. (1997). *METHONTOLOGY: From Ontological Art Towards Ontological Engineering*. https://oa.upm.es/5484/1/METHONTOLOGY_.pdf — diakses 2026-05-05.
7. Stefano-Angelo-Rizzo. “VideOWL.” GitHub. https://github.com/Stefano-Angelo-Rizzo/VideOWL — diakses 2026-05-05.
