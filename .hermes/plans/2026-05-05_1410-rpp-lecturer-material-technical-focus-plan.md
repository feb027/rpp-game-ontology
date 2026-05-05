# Plan Reorientasi Teknis — RPP Game Ontology vs Materi Dosen

Tanggal: 2026-05-05
Repo: `/home/aqua/rpp-game-ontology`
Materi dosen yang diaudit:

- `docs/RPP-12 Pengembangan Ontologi-I.ppt.pdf`
- `docs/RPP-13 Pengembangan Ontologi-II.pptx.pdf`

## 1. Kesimpulan audit

Repo **sudah sesuai secara arah besar**, tetapi **belum ideal kalau mengacu detail materi dosen**.

Yang sudah sesuai:

- Menggunakan studi kasus sistem berbasis pengetahuan.
- Menggunakan ontologi dengan format OWL yang kompatibel dengan Protégé.
- Memakai Protégé sebagai tools utama secara dokumentasi.
- Sudah memakai konsep class, property, individual, OWL/RDF, dan reasoning.
- Sudah memetakan proses ke Methontology.
- Sudah ada aplikasi demo yang menunjukkan reasoning/rekomendasi berbasis aturan.

Yang masih kurang jika dibandingkan materi dosen:

- Materi RPP-13 menekankan intermediate representations Methontology, tetapi repo belum punya artefak teknis lengkap seperti:
  - glossary of terms,
  - concept taxonomy,
  - concept dictionary,
  - ad hoc binary relation table,
  - instance attribute table,
  - class attribute table,
  - formal axioms,
  - rules,
  - instances table.
- File OWL masih minimal:
  - 9 classes,
  - 6 object properties,
  - 1 data property,
  - 25 named individuals,
  - hanya 2 game individual (`StardewValley`, `Valorant`).
- Specification menulis 8 game, tetapi OWL belum memuat semua 8 game.
- OWL belum memuat property/individual `Recommendation` secara nyata, padahal dokumen menulis class `Recommendation` dan reasoning dengan alasan rekomendasi.
- Evaluasi teknis baru berupa parse OWL + unit test app; belum ada dokumentasi competency question/SPARQL/DL Query sebagai bukti evaluasi ontologi.

## 2. Prinsip baru sesuai arahan user

Slide dan video dibuat manual di luar fokus utama repo.

Repo harus fokus pada pengerjaan teknis:

1. Ontologi yang kuat dan bisa dibuka di Protégé.
2. Artefak Methontology yang sesuai materi dosen.
3. Aplikasi demo yang runnable.
4. Test dan bukti teknis.
5. Dokumentasi teknis singkat untuk membantu slide/video manual.

Repo tidak perlu menjadi generator slide/video utama. Slide/video cukup sebagai handoff/checklist, bukan prioritas coding.

## 3. Mapping materi dosen ke kebutuhan repo

### RPP-12 Pengembangan Ontologi-I

Materi penting:

- Representasi knowledge.
- Ontologi sebagai skema konseptual vocabulary dan relationship.
- 7 komponen pengetahuan ontologi:
  - concepts,
  - relations,
  - instances,
  - constants,
  - attributes,
  - formal axioms,
  - rules.
- Karakteristik ontologi:
  - formality,
  - explicitness,
  - being shared,
  - conceptuality,
  - domain specificity.
- Bahasa ontologi:
  - RDF,
  - RDFS,
  - OWL,
  - SPARQL.
- Tools:
  - Protégé sebagai ontology editor.

Repo sudah mencakup sebagian besar, tetapi perlu dibuat lebih eksplisit dalam dokumen teknis.

### RPP-13 Pengembangan Ontologi-II

Materi penting:

- Methontology sebagai metodologi terstruktur.
- Methontology memakai intermediate representations.
- Tahapan/artefak konseptualisasi:
  - glossary of terms,
  - concept taxonomies,
  - ad hoc binary diagram/relation,
  - concept dictionary,
  - instance attribute,
  - class attribute,
  - formal axioms,
  - rules,
  - instances.
- Implementasi memakai Protégé.
- Evaluasi ontologi:
  - reasoning Protégé,
  - OOPS!/OntoQA/OQuaRE/SPARQL sebagai opsi,
  - verifikasi dan validasi.

Repo saat ini belum cukup eksplisit pada bagian intermediate representations dan evaluasi ontology.

## 4. Revised technical backlog

### T1 — Tambah dokumen alignment materi dosen

Buat:

- `docs/07-dosen-material-alignment.md`

Isi:

- Ringkasan poin RPP-12 dan RPP-13 yang dipakai.
- Mapping materi dosen → artefak repo.
- Catatan bahwa slide/video dibuat manual, repo fokus teknis.

### T2 — Buat artefak Methontology teknis

Buat:

- `docs/08-methontology-artifacts.md`

Isi wajib:

1. Specification.
2. Knowledge acquisition summary.
3. Glossary of terms.
4. Concept taxonomy.
5. Concept dictionary.
6. Ad hoc binary relation table.
7. Instance attribute table.
8. Class attribute table.
9. Formal axioms.
10. Rules.
11. Instances table.
12. Evaluation plan.

Format tabel agar mudah dipindah ke slide/manual video.

### T3 — Perkuat OWL agar konsisten dengan specification

Update `ontology/game_recommendation.owl` agar memuat minimal:

- Semua 8 game dari specification/app:
  - `StardewValley`
  - `Minecraft`
  - `Valorant`
  - `GenshinImpact`
  - `CandyCrush`
  - `Overcooked2`
  - `TheWitcher3`
  - `AnimalCrossing`
- Object properties lengkap:
  - `hasGenre`
  - `availableOn`
  - `hasPlayMode`
  - `hasDifficulty`
  - `hasDuration`
  - `suitableForMood`
  - `matchesPreference`
  - `recommendsGame`
  - `basedOnMood`
  - `basedOnPreference`
- Data properties:
  - `gameTitle`
  - `recommendationReason`
  - `priorityScore`
- Recommendation individuals untuk contoh minimal:
  - `Recommendation_Stardew_Stress_PC`
  - `Recommendation_Valorant_Competitive_PC`

### T4 — Tambah query/evaluation teknis

Buat:

- `ontology/queries.md`

Isi:

- DL Query yang bisa dicoba di Protégé.
- SPARQL query untuk RDF/OWL parse lokal jika feasible.
- Expected results.

Contoh:

```text
Game and suitableForMood value Stres and availableOn value PC
```

Expected: `StardewValley`.

### T5 — Tambah test ontology lebih kuat

Update/extend test:

- `tests/test_ontology.py`

Validasi:

- OWL parseable.
- Core classes ada.
- Core object/data properties ada.
- 8 game individuals ada.
- Query RDF sederhana menghasilkan expected entities.
- App seed data dan OWL tidak drift terlalu jauh.

### T6 — Reposisi slide/video assets

Karena slide/video akan dibuat manual:

- Pertahankan `video/tutorial-script.md`, `video/storyboard.md`, dan `slides/outline.md` sebagai bahan bantu.
- Jangan prioritaskan generator PPTX kecuali user minta.
- README harus menekankan technical deliverables:
  - OWL Protégé,
  - Methontology artifacts,
  - Streamlit app,
  - tests,
  - manual slide/video handoff.

### T7 — Update final QA

Setelah T1–T6:

- Update `docs/FINAL_QA.md`.
- Status teknis bisa `TECH_READY_FOR_MANUAL_SLIDE_VIDEO`.
- Jangan tulis `READY_FOR_SUBMISSION` sampai video final + YouTube URL benar-benar ada.

## 5. Definition of done teknis

Repo dianggap teknis siap jika:

- `python -m pytest -q` pass.
- OWL parseable.
- OWL memuat class/property/individual utama sesuai docs.
- 8 game muncul di OWL dan app.
- Methontology artifacts lengkap dan selaras dengan RPP-13.
- Ada DL Query/SPARQL expected result.
- App demo bisa jalan via `streamlit run app/main.py`.
- README menjelaskan repo sebagai teknis, bukan pusat pembuatan slide/video.

## 6. Jawaban atas pertanyaan user

- Sudah sesuai secara konsep umum.
- Belum sepenuhnya sesuai detail materi dosen karena IR Methontology dan evaluasi ontologi belum lengkap.
- Arah yang benar sekarang adalah memperkuat aspek teknis repo, bukan menghabiskan waktu membuat slide/video otomatis.
