# Final QA — RPP Game Ontology

QA timestamp: 2026-05-05

## Verdict

**TECH_READY_FOR_MANUAL_SLIDE_VIDEO**

Repo sudah siap sebagai basis teknis tugas RPP: ontology OWL/Protégé, artefak Methontology, query/evaluasi, aplikasi demo, dan test otomatis. Belum boleh disebut `READY_FOR_SUBMISSION` sampai video final, YouTube AIS URL, dan ZIP pengumpulan selesai secara manual.

## Assignment Coverage

| Requirement | Status teknis | Evidence | Notes |
|---|---:|---|---|
| a. Cara unduh dan instalasi tools | READY_AS_MATERIAL | `docs/03-research-notes.md`, `docs/06-slide-notes.md`, `slides/outline.md` | Dipakai sebagai bahan slide/video manual. |
| b. Pengenalan lingkungan kerja tools | READY_AS_MATERIAL | `docs/03-research-notes.md`, `docs/06-slide-notes.md` | Menjelaskan Active Ontology, Entities, Classes, Properties, Individuals, Reasoner, DL Query. |
| c. Deskripsi persoalan kasus | PASS | `docs/00-task-brief.md`, `docs/02-scope-and-acceptance.md`, `docs/04-ontology-specification.md` | Studi kasus mood + preferensi game jelas. |
| d. Deskripsi solusi penyelesaian kasus | PASS | `docs/04-ontology-specification.md`, `docs/07-dosen-material-alignment.md`, `docs/08-methontology-artifacts.md`, `ontology/ontology-design.md` | Sudah selaras dengan materi RPP-12/RPP-13 dan Methontology. |
| e. Penerapan kasus menggunakan tools | PASS | `ontology/game_recommendation.owl`, `ontology/queries.md` | OWL parseable, memuat vocabulary utama, 8 game, recommendation individuals, dan query evaluasi. |
| f. Demo aplikasi | PASS | `app/main.py`, `app/recommender.py`, `app/data.py`, `tests/` | App runnable dan test pass. |
| Video tutorial | MANUAL_PENDING | `video/tutorial-script.md`, `video/storyboard.md`, `video/recording-checklist.md` | Script/storyboard ada, final MP4 belum ada. |
| AIS YouTube URL | MANUAL_PENDING | `video/youtube-upload-draft.md` | Upload URL belum tersimpan. |
| ZIP pengumpulan | MANUAL_PENDING | `docs/SUBMISSION_CHECKLIST.md` | ZIP final belum dibuat. |

## Technical Verification

Command:

```bash
source .venv/bin/activate
python -m pytest -q
```

Result:

```text
6 passed in 0.45s
owl_triples=481
pptx_slides=12
streamlit_http_status=200
```

Ontology validation covered by `tests/test_ontology.py`:

- Core classes exist.
- Core object/data properties exist.
- 8 game individuals exist.
- SPARQL smoke queries return expected results.
- Recommendation individual includes reason and score.

## Current Known Manual Blockers

- `video/final-rpp-game-ontology.mp4` belum ada.
- `video/youtube-url.txt` belum ada.
- ZIP final belum dibuat.
- Protégé visual/reasoner check tetap perlu dilakukan manual di laptop saat rekaman.

## Do Not Include in ZIP

- `.git/`
- `.worktrees/`
- `.venv/`
- `node_modules/`
- `.pytest_cache/`
- `__pycache__/`
- `*.pyc`
- `*.zip` hasil build sebelumnya

## Final Technical Decision

Repo teknis sudah siap untuk dipakai membuat slide/video manual. Tahap berikutnya adalah rekam tutorial, upload YouTube AIS, buat ZIP bersih, lalu kirim ke ketua kelas.
