# Alignment Materi Dosen — RPP-12/RPP-13 ke Repo Teknis

Dokumen ini memetakan materi dosen ke artefak teknis repo `rpp-game-ontology`. Slide dan video dibuat manual; repo ini difokuskan sebagai bukti teknis: ontologi OWL/Protégé, artefak Methontology, query/evaluasi, aplikasi demo, dan test.

## Sumber Materi

- `docs/RPP-12 Pengembangan Ontologi-I.ppt.pdf`
- `docs/RPP-13 Pengembangan Ontologi-II.pptx.pdf`

## Ringkasan RPP-12: Pengembangan Ontologi I

| Materi dosen | Makna | Implementasi di repo |
|---|---|---|
| Representasi knowledge | Pengetahuan perlu direpresentasikan agar bisa disimpan, dipertukarkan, dan dipakai ulang | `ontology/game_recommendation.owl` merepresentasikan pengetahuan game, mood, preferensi, dan rekomendasi |
| Ontologi sebagai skema konseptual vocabulary dan relationship | Domain dimodelkan dengan istilah/konsep dan relasi | `docs/08-methontology-artifacts.md` berisi glossary, taxonomy, concept dictionary, dan binary relation |
| 7 komponen pengetahuan ontologi | concepts, relations, instances, constants, attributes, formal axioms, rules | Semua komponen dipetakan dalam `docs/08-methontology-artifacts.md` |
| Karakteristik ontologi | formality, explicitness, being shared, conceptuality, domain specificity | OWL memakai bahasa formal, konsep/relasi eksplisit, scope domain dibatasi pada rekomendasi game |
| Bahasa ontologi | RDF, RDFS, OWL, SPARQL | File OWL memakai RDF/XML; query contoh tersedia di `ontology/queries.md` |
| Protégé sebagai ontology editor | Tools untuk membuat/memeriksa ontologi | `ontology/game_recommendation.owl` dapat dibuka di Protégé |

## Ringkasan RPP-13: Pengembangan Ontologi II

| Materi dosen | Makna | Implementasi di repo |
|---|---|---|
| Methontology | Metodologi terstruktur untuk membangun ontologi | Alur kerja dan output ada di `docs/08-methontology-artifacts.md` |
| Intermediate representations | IR menjembatani pemikiran domain ke bahasa ontology formal | Dibuat sebagai tabel glossary, taxonomy, concept dictionary, relation, attribute, axiom, rule, dan instance |
| Glossary of terms | Mengumpulkan semua istilah domain | Bagian 3 di `docs/08-methontology-artifacts.md` |
| Concept taxonomies | Hierarki konsep | Bagian 4 di `docs/08-methontology-artifacts.md`; juga class hierarchy di OWL |
| Concept dictionary | Definisi konsep, relasi, instance, atribut | Bagian 5 di `docs/08-methontology-artifacts.md` |
| Ad hoc binary relation | Relasi antar konsep beserta domain/range/kardinalitas | Bagian 6 di `docs/08-methontology-artifacts.md`; object property di OWL |
| Instance/class attribute | Atribut instance/class | Bagian 7–8 di `docs/08-methontology-artifacts.md`; data property di OWL |
| Formal axioms dan rules | Batasan/aturan untuk penalaran | Bagian 9–10 di `docs/08-methontology-artifacts.md`; contoh rule dipakai app |
| Instances | Individual nyata pada domain | OWL memuat 8 game, vocabulary mood/genre/platform/mode/duration/difficulty, preference, dan recommendation |
| Implementasi Protégé | Ontologi disusun pada environment yang mendukung bahasa formal | `ontology/game_recommendation.owl` kompatibel dengan Protégé dan RDF/OWL |
| Evaluasi | Verifikasi/validasi ontology, software environment, dokumentasi | `tests/test_ontology.py`, `tests/test_recommender.py`, dan `ontology/queries.md` |

## Posisi Repo terhadap Tugas

| Kebutuhan tugas | Artefak repo | Status teknis |
|---|---|---|
| a. Cara unduh dan instalasi tools | `docs/03-research-notes.md`, `docs/06-slide-notes.md`, `slides/outline.md` | Bahan manual slide/video tersedia |
| b. Pengenalan lingkungan kerja tools | `docs/03-research-notes.md`, `docs/06-slide-notes.md` | Bahan manual tersedia |
| c. Deskripsi persoalan kasus | `docs/00-task-brief.md`, `docs/02-scope-and-acceptance.md`, `docs/04-ontology-specification.md` | Selesai |
| d. Deskripsi solusi penyelesaian kasus | `docs/04-ontology-specification.md`, `docs/08-methontology-artifacts.md`, `ontology/ontology-design.md` | Selesai teknis |
| e. Penerapan kasus menggunakan tools | `ontology/game_recommendation.owl`, `ontology/queries.md` | Selesai teknis; perlu buka manual di Protégé untuk rekaman |
| f. Demo aplikasi | `app/`, `requirements.txt`, `tests/`, `docs/05-demo-app-guide.md` | Selesai teknis |

## Catatan Penting untuk Slide/Video Manual

- Jangan menjadikan repo sebagai generator utama slide/video.
- Pakai repo sebagai sumber bukti teknis: OWL, app, query, test, dan tabel Methontology.
- Saat merekam, buka `ontology/game_recommendation.owl` langsung di Protégé.
- Jalankan app dengan `streamlit run app/main.py` dan tunjukkan input demo.
- Jika menyebut evaluasi, sebutkan dua tingkat:
  1. Evaluasi ontologi: parse OWL, query, dan consistency check di Protégé.
  2. Evaluasi aplikasi: unit test dan smoke demo rekomendasi.
