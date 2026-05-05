# Scope dan Acceptance Criteria

## Judul
Study Case: Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi

## Tujuan Sistem
Mengembangkan sistem berbasis pengetahuan yang merekomendasikan game berdasarkan kombinasi mood pengguna dan preferensi bermain. Sistem menggunakan ontologi untuk merepresentasikan pengetahuan tentang mood, genre game, platform, mode bermain, tingkat kesulitan, durasi, dan alasan rekomendasi.

## Kerangka Pengembangan: Methontology

Tahapan Methontology yang digunakan dalam tugas ini:

1. **Specification** — menentukan tujuan, ruang lingkup, pengguna, dan pertanyaan kompetensi.
2. **Knowledge Acquisition** — mengumpulkan pengetahuan tentang game, mood, preferensi, dan konsep ontologi.
3. **Conceptualization** — menyusun kelas, relasi, atribut, individu, dan aturan rekomendasi.
4. **Integration** — memastikan konsep dapat dikaitkan dengan OWL/RDF dan Protégé.
5. **Implementation** — membuat ontologi di Protégé serta aplikasi demo.
6. **Evaluation** — menguji apakah rekomendasi sesuai dengan pertanyaan kompetensi.
7. **Documentation** — membuat slide, catatan demo, dan script video tutorial.

## Mapping Rincian Tugas ke Artifact

| Poin | Kebutuhan Tugas | Artifact |
|---|---|---|
| a | Cara unduh dan instalasi tools | slide instalasi Protégé + notes |
| b | Pengenalan lingkungan kerja tools | slide lingkungan Protégé + screenshot checklist |
| c | Deskripsi persoalan kasus | slide studi kasus rekomendasi game |
| d | Deskripsi solusi penyelesaian kasus | slide solusi ontologi + reasoning |
| e | Penerapan kasus menggunakan tools | slide penerapan kelas/properti/individu/rule di Protégé |
| f | Demo aplikasi | aplikasi runnable + ontology file + demo guide |

## Ruang Lingkup Ontologi

### Kelas Utama
- `Game`
- `Genre`
- `Mood`
- `Platform`
- `PlayMode`
- `Difficulty`
- `Duration`
- `PlayerPreference`
- `Recommendation`

### Contoh Mood
- santai
- kompetitif
- stres
- bosan
- ingin eksplorasi
- ingin sosial

### Contoh Preferensi
- genre favorit
- platform yang dimiliki
- durasi bermain
- mode bermain
- toleransi tingkat kesulitan

## Done Criteria

### Ontologi dianggap selesai jika:
- Ada file OWL/RDF yang kompatibel dengan Protégé.
- Kelas, properti, individu, dan relasi utama terdokumentasi.
- Ada contoh reasoning/rekomendasi berbasis mood + preferensi.

### Aplikasi demo dianggap selesai jika:
- Bisa menerima input mood dan preferensi.
- Menghasilkan rekomendasi game beserta alasan.
- Bisa dijalankan dengan command yang jelas.
- Ada seed data dan dokumentasi penggunaan.

### Slide dianggap selesai jika:
- Mencakup poin a sampai e.
- Menggunakan bahasa Indonesia yang jelas untuk presentasi kelas.
- Memiliki struktur tutorial: instalasi → pengenalan tools → kasus → solusi → penerapan.

### Video tutorial dianggap selesai jika:
- Ada script narasi.
- Ada storyboard/susunan scene.
- Ada checklist rekaman layar.
- Mencakup slide dan demo aplikasi.

## Risiko dan Mitigasi

| Risiko | Mitigasi |
|---|---|
| Protégé tidak bisa dijalankan di VPS/headless | Buat ontology file dan screenshot checklist; demo app tetap runnable |
| Ontologi terlalu kompleks | Batasi scope ke mood, genre, platform, mode, durasi, difficulty |
| Rekomendasi terasa subjektif | Jelaskan aturan rekomendasi sebagai knowledge engineering berbasis asumsi domain |
| Slide terlalu padat | Gunakan visual flow dan tabel ringkas |

## Task Graph Terkunci

Urutan kerja:

1. Research Protégé + Methontology.
2. Desain ontology specification.
3. Implementasi ontology + demo app.
4. Review ontology/app.
5. Buat slide.
6. Buat video tutorial script.
7. Final QA dan checklist pengumpulan.
