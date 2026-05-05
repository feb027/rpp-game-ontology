# Plan Implementasi Teknis — RPP Game Ontology

Tanggal: 2026-05-05
Repo: `/home/aqua/rpp-game-ontology`

## Goal

Mereorientasi repo agar fokus pada pengerjaan teknis tugas RPP: ontologi Protégé/OWL, artefak Methontology sesuai materi dosen, query/evaluasi, aplikasi demo, dan test. Slide/video tetap disiapkan manual memakai output repo sebagai bahan.

## Scope

### In scope
- Tambah dokumen alignment materi dosen RPP-12/RPP-13.
- Tambah artefak Methontology lengkap berbasis intermediate representation.
- Perluas ontology OWL agar konsisten dengan seed data 8 game.
- Tambah contoh recommendation individual, data property alasan/skor, dan query/evaluasi.
- Tambah test ontology.
- Update README dan `.gitignore`.
- Commit dan push.

### Out of scope
- Membuat video final.
- Upload YouTube AIS.
- Mendesain ulang slide manual.
- Mengubah studi kasus.

## Langkah

1. TDD: buat `tests/test_ontology.py` dengan target ontology baru, jalankan dan pastikan gagal terhadap OWL lama.
2. Update `ontology/game_recommendation.owl`:
   - 8 game individual.
   - core object/data properties lengkap.
   - recommendation example individuals.
   - label/comment agar jelas di Protégé.
3. Buat `docs/07-dosen-material-alignment.md`.
4. Buat `docs/08-methontology-artifacts.md`.
5. Buat `ontology/queries.md`.
6. Update README agar repo difokuskan pada teknis, bukan generator slide/video.
7. Update `.gitignore` untuk runtime/build artifacts.
8. Jalankan validasi:
   - `python -m pytest -q`
   - parse OWL dengan rdflib.
   - query smoke check.
9. Commit dan push branch aktif.

## Validation

- Semua test pass.
- OWL parseable.
- OWL memuat classes/properties/individuals sesuai dokumen.
- DL Query/SPARQL examples punya expected results.
- Git status bersih untuk file yang sengaja dikerjakan.

## Risiko

- File PDF materi dosen bisa sensitif jika repo public; push sebaiknya ke private repo atau PDF tidak dipublish jika repo public.
- Protégé visual QA tetap perlu dilakukan manual di laptop.
- Video/YouTube tetap blocker submission, tapi bukan blocker teknis repo.
