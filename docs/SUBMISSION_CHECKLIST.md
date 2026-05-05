# Submission Checklist — RPP Game Ontology

Use this as the exact pre-submission checklist for ketua kelas collection and AIS YouTube upload.

## 1. Final verdict gate

Current handoff status: READY_FOR_RECORDING

Agent-side script/storyboard fixes are done. Submit only after these human-side items are true:
- [ ] Final tutorial video has been recorded/exported as `video/final-rpp-game-ontology.mp4`.
- [ ] AIS YouTube upload is complete or the upload-ready video file is handed to the AIS channel operator.
- [ ] YouTube URL is recorded in `video/youtube-url.txt` and in this checklist.

## 2. Package name

Recommended ZIP name:

`RPP_Game_Ontology_Febnawan_Fatur_Rochman_237006029.zip`

If submitting as a group, rename with all required group member names/NPM according to class instruction.

## 3. Files/folders to include for ketua kelas

Include these exact items:

- [ ] `README.md`
- [ ] `docs/00-task-brief.md`
- [ ] `docs/02-scope-and-acceptance.md`
- [ ] `docs/03-research-notes.md`
- [ ] `docs/04-ontology-specification.md`
- [ ] `docs/05-demo-app-guide.md`
- [ ] `docs/06-slide-notes.md`
- [ ] `docs/FINAL_QA.md`
- [ ] `docs/SUBMISSION_CHECKLIST.md`
- [ ] `slides/rpp-game-ontology-presentation.pptx`
- [ ] `slides/outline.md`
- [ ] `ontology/game_recommendation.owl`
- [ ] `ontology/ontology-design.md`
- [ ] `app/__init__.py`
- [ ] `app/data.py`
- [ ] `app/main.py`
- [ ] `app/recommender.py`
- [ ] `requirements.txt`
- [ ] `tests/test_recommender.py`
- [ ] `video/tutorial-script.md`
- [ ] `video/storyboard.md`
- [ ] `video/recording-checklist.md`
- [ ] `video/youtube-upload-draft.md`
- [ ] Final exported video file: `video/final-rpp-game-ontology.mp4` or the final filename required by class.
- [ ] Plain text note containing AIS YouTube URL after upload, e.g. `video/youtube-url.txt`.

## 4. Do NOT include

Exclude generated/runtime/internal folders:

- [ ] `.git/`
- [ ] `.worktrees/`
- [ ] `.venv/`
- [ ] `node_modules/`
- [ ] `.pytest_cache/`
- [ ] `__pycache__/`
- [ ] `*.pyc`
- [ ] OS junk files such as `.DS_Store`

## 5. App run proof before packaging

Run this from repo root before making the ZIP:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
streamlit run app/main.py
```

Expected:
- [ ] Tests show `2 passed`.
- [ ] Browser opens Streamlit app, usually `http://localhost:8501`.
- [ ] User can select mood and preferences in sidebar.
- [ ] App shows recommendation cards with score and reasons.

Demo input to show in video:
- Mood: `Stres`
- Genre: `Casual`
- Platform: `PC`
- Mode: `SinglePlayer`
- Durasi: `Sedang`
- Difficulty: `Mudah`

Expected top result:
- `Stardew Valley` with reasons including mood stress match, Casual genre, PC platform, SinglePlayer mode, and easy difficulty.

## 6. Slide proof before packaging

- [ ] Open `slides/rpp-game-ontology-presentation.pptx` in PowerPoint/LibreOffice.
- [ ] Confirm title slide identity is correct.
- [ ] Confirm points a–e are visible:
  - [ ] a. Cara unduh dan instalasi tools.
  - [ ] b. Pengenalan lingkungan kerja Protégé.
  - [ ] c. Deskripsi persoalan kasus.
  - [ ] d. Deskripsi solusi penyelesaian kasus.
  - [ ] e. Penerapan kasus menggunakan tools.
- [ ] Confirm no fake screenshots are presented as real evidence.
- [ ] If lecturer wants PDF too, export to `slides/rpp-game-ontology-presentation.pdf` and include it.

If PPTX needs regeneration:

```bash
npm install
node slides/generate_presentation.js
```

## 7. Ontology proof before packaging

- [ ] Open `ontology/game_recommendation.owl` in Protégé.
- [ ] Confirm core classes exist: `Game`, `Genre`, `Mood`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, `Recommendation`.
- [ ] Confirm object properties exist for game relations, especially `hasGenre`, `availableOn`, `hasPlayMode`, `hasDifficulty`, `hasDuration`, `suitableForMood`.
- [ ] Confirm example individuals exist, especially `StardewValley`, `Valorant`, mood individuals, genre individuals, and platform individuals.
- [ ] Run/mention reasoner consistency check if available in Protégé.

## 8. Video recording checklist

Before recording:
- [ ] Open `video/tutorial-script.md` and `video/storyboard.md`.
- [ ] Follow the detailed handoff in `video/recording-checklist.md`.
- [ ] Confirm app demo uses auto-rendered recommendations; do not say there is a recommendation button.
- [ ] Use actual app labels/options: `Multiplayer`, `Singkat/Sedang/Panjang`, `Mudah/Sedang/Sulit`.
- [ ] Prepare screen resolution 1920x1080 or clear 16:9.
- [ ] Prepare microphone/audio narration.
- [ ] Prepare slides and app window.
- [ ] Prepare Protégé with `ontology/game_recommendation.owl` opened.

Record these scenes:
- [ ] Opening/title and identity.
- [ ] Protégé download/install explanation.
- [ ] Protégé environment: Active Ontology, Entities/Classes, Properties, Individuals, Reasoner, DL Query.
- [ ] Case explanation: mood + game preferences.
- [ ] Ontology solution: classes, properties, individuals, Methontology mapping.
- [ ] Protégé application demo: show ontology and query/reasoning concept.
- [ ] Streamlit app run command.
- [ ] Streamlit app input/output demo.
- [ ] Closing summary.

Export settings:
- [ ] Format: MP4/H.264.
- [ ] Resolution: 1080p if possible.
- [ ] Audio: clear Indonesian narration.
- [ ] Filename: `video/final-rpp-game-ontology.mp4`.

## 9. AIS YouTube upload checklist

Use `video/youtube-upload-draft.md` as source.

Upload fields:
- [ ] Title: `Tutorial Sistem Rekomendasi Game Berbasis Ontologi dengan Protégé & Streamlit`
- [ ] Description: include assignment context, tools, and short explanation from upload draft.
- [ ] Timestamps: use draft timestamps and adjust after final edit.
- [ ] Tags: `Ontologi`, `Protégé`, `Streamlit`, `RekomendasiGame`, `Python`, `Mahasiswa`.
- [ ] Thumbnail: optional but recommended; use clean visual of Protégé/app, not misleading game art.
- [ ] Visibility: follow AIS/class instruction. If unspecified, ask before choosing Public/Unlisted.
- [ ] Upload account/channel: AIS YouTube channel.

After upload:
- [ ] Play uploaded video once from YouTube to confirm audio/video works.
- [ ] Copy final YouTube URL.
- [ ] Save URL to `video/youtube-url.txt`.
- [ ] Send URL with package to ketua kelas.

## 10. Final message to ketua kelas

Template:

```text
Assalamu'alaikum, berikut pengumpulan Tugas Besar RPP:

Judul: Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi
Nama/NPM: Febnawan Fatur Rochman / 237006029
Isi paket: slide presentasi, ontology OWL, aplikasi demo Streamlit, dokumentasi, dan video tutorial.
Link YouTube AIS: [ISI LINK YOUTUBE]

Catatan run app:
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. streamlit run app/main.py

Terima kasih.
```

## 11. Final pre-submit tick boxes

- [ ] QA blockers fixed.
- [ ] Final video file exists.
- [ ] YouTube URL exists.
- [ ] ZIP contains required files only.
- [ ] App command tested after ZIP extraction if possible.
- [ ] Package sent to ketua kelas.
- [ ] YouTube link shared as required.
