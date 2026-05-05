# AGENTS.md — RPP Game Ontology Assignment

## Project Role

This repository contains coursework deliverables for Representasi Pengetahuan dan Penalaran:
"Study Case: Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi".

## Deliverables

- Slides for technical points a–e.
- Ontology files created/compatible with Protégé.
- Demo application for point f.
- Video tutorial script/storyboard and final packaging notes.

## Rules

- Do not invent lecturer requirements beyond the provided brief.
- Keep Indonesian academic/coursework tone.
- Use clear, beginner-friendly explanations for Protégé installation and environment.
- For ontology work, document Methontology stages explicitly.
- For demo app, keep it runnable on a normal laptop/VPS with simple commands.
- Every coding task must report changed files, tests/run commands, and commit hash or no-commit reason.
- Do not edit unrelated files.

## Suggested Commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
streamlit run app/main.py
```

If requirements/tests are not available yet, create them as part of the implementation task.
