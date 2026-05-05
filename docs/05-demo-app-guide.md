# Demo App Guide

## Cara Menjalankan

```bash
cd /home/aqua/rpp-game-ontology
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

## Cara Testing

```bash
python -m pytest -q
```

## Alur Demo

1. Buka aplikasi Streamlit.
2. Pilih mood pengguna, misalnya `Stres`.
3. Pilih preferensi genre/platform/mode/durasi/difficulty.
4. Sistem menampilkan daftar rekomendasi game.
5. Setiap rekomendasi memiliki alasan, misalnya cocok untuk mood tertentu, tersedia di platform tertentu, atau mendukung mode bermain tertentu.

## Hubungan dengan Ontologi

- File `ontology/game_recommendation.owl` menyimpan kelas, properti, dan individu yang kompatibel dengan Protégé.
- Aplikasi memakai seed knowledge yang konsisten dengan ontology specification.
- Reasoning pada aplikasi dibuat rule-based agar mudah didemokan dan dijelaskan dalam video tutorial.
