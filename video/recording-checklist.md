# Recording Checklist — Final Tutorial Video

Target output lokal:

`video/final-rpp-game-ontology.mp4`

Target upload:

AIS YouTube channel, lalu simpan URL final ke `video/youtube-url.txt`.

## Status handoff

Agent tidak bisa merekam layar lokal, mengisi audio narasi manusia, atau mengunggah ke AIS YouTube dari environment ini. File video final dan URL YouTube harus dibuat oleh human uploader.

Placeholder yang harus diganti manusia:
- `[ISI NAMA PRESENTER / KELOMPOK]`
- `[ISI LINK YOUTUBE AIS SETELAH UPLOAD]`
- Jika nama file final berbeda, catat nama file final di checklist pengumpulan.

## Pre-recording

- [ ] Buka repo: `/home/aqua/rpp-game-ontology`.
- [ ] Baca `video/tutorial-script.md` sebagai naskah narasi.
- [ ] Baca `video/storyboard.md` sebagai urutan visual.
- [ ] Siapkan resolusi rekaman 16:9, disarankan 1920×1080.
- [ ] Pastikan microphone aktif dan suara jelas.
- [ ] Siapkan slide presentasi `slides/rpp-game-ontology-presentation.pptx`.
- [ ] Siapkan Protégé dan buka `ontology/game_recommendation.owl`.
- [ ] Siapkan terminal di root repo.
- [ ] Jalankan test cepat jika sempat:

```bash
cd /home/aqua/rpp-game-ontology
source .venv/bin/activate 2>/dev/null || true
python -m pytest -q
```

## Run app untuk scene demo

Jika `.venv` belum ada:

```bash
cd /home/aqua/rpp-game-ontology
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

Jika `.venv` sudah ada:

```bash
cd /home/aqua/rpp-game-ontology
source .venv/bin/activate
streamlit run app/main.py
```

Buka browser ke `http://localhost:8501`.

## Scene wajib direkam

1. Opening dan identitas: `[ISI NAMA PRESENTER / KELOMPOK]`.
2. Cara unduh/instal Protégé.
3. Lingkungan Protégé: Active Ontology, Entities/Classes, Object Properties, Data Properties, Individuals.
4. Deskripsi kasus: rekomendasi game berdasarkan mood dan preferensi.
5. Solusi ontologi: kelas, properti, individu, Methontology.
6. Reasoner HermiT dan DL Query konseptual.
7. Terminal menjalankan `streamlit run app/main.py`.
8. Streamlit app dengan sidebar **Input Preferensi**.
9. Demo input aktual:
   - Mood saat ini: `Stres`
   - Genre favorit: `Casual`
   - Platform: `PC`
   - Mode bermain: `SinglePlayer`
   - Durasi bermain: `Sedang`
   - Tingkat kesulitan: `Mudah`
   - Catatan opsi UI: mode mencakup `Multiplayer`; durasi mencakup `Singkat`, `Sedang`, `Panjang`; tingkat kesulitan mencakup `Mudah`, `Sedang`, `Sulit`.
10. Bagian **Hasil Rekomendasi** muncul otomatis; jangan klik/menyebut tombol rekomendasi karena memang tidak ada.
11. Sorot rekomendasi, skor kecocokan, dan alasan rekomendasi.
12. Closing summary.

## Export settings

- [ ] Format: MP4.
- [ ] Codec: H.264 jika tersedia.
- [ ] Resolusi: 1080p jika memungkinkan.
- [ ] Audio: AAC atau default editor, pastikan terdengar jelas.
- [ ] Nama file: `video/final-rpp-game-ontology.mp4`.
- [ ] Putar file sekali sebelum upload untuk cek suara, layar, dan tidak ada bagian kosong.

## AIS YouTube upload

Gunakan `video/youtube-upload-draft.md` untuk title, description, timestamps, tags, dan thumbnail note.

- [ ] Login ke akun/channel AIS YouTube sesuai instruksi kelas.
- [ ] Upload `video/final-rpp-game-ontology.mp4`.
- [ ] Isi judul dari draft upload.
- [ ] Isi description dari draft upload.
- [ ] Atur visibility sesuai instruksi kelas/AIS. Jika tidak ada instruksi, tanya ketua kelas sebelum memilih Public/Unlisted.
- [ ] Setelah upload selesai, buka video dari YouTube dan cek playback.
- [ ] Salin URL final.
- [ ] Buat/isi file `video/youtube-url.txt` dengan format:

```text
AIS YouTube URL: [ISI LINK YOUTUBE AIS SETELAH UPLOAD]
Uploaded by: [ISI NAMA UPLOADER]
Upload date: [ISI TANGGAL UPLOAD]
Final video file: video/final-rpp-game-ontology.mp4
```

## Final package handoff ke ketua kelas

- [ ] `video/final-rpp-game-ontology.mp4` ada di folder video atau sudah diserahkan terpisah jika ukuran file terlalu besar.
- [ ] `video/youtube-url.txt` sudah berisi link asli, bukan placeholder.
- [ ] `docs/SUBMISSION_CHECKLIST.md` dicentang sesuai kondisi final.
- [ ] ZIP tidak memasukkan `.venv/`, `node_modules/`, `.pytest_cache/`, `__pycache__/`, atau `.git/`.
- [ ] Pesan pengumpulan memakai template di `docs/SUBMISSION_CHECKLIST.md`.
