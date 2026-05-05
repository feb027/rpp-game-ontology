# Plan Finalisasi — RPP Game Ontology

Tanggal audit: 2026-05-05 13:54:25
Repo: `/home/aqua/rpp-game-ontology`
Judul tugas: **Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi**

## 1. Tujuan

Menuntaskan tugas besar Representasi Pengetahuan dan Penalaran dari kondisi repo sekarang sampai siap dikumpulkan: slide, ontology Protégé, aplikasi demo, video tutorial, YouTube AIS, dan paket ZIP bersih.

## 2. Status saat audit

### Sudah ada / lulus cek teknis

- Slide presentasi: `slides/rpp-game-ontology-presentation.pptx`
  - PPTX terbaca sebagai ZIP valid.
  - Jumlah slide: 12.
- Outline/catatan slide:
  - `slides/outline.md`
  - `docs/06-slide-notes.md`
- Ontologi:
  - `ontology/game_recommendation.owl`
  - parse RDF/OWL berhasil.
  - jumlah triple: 95.
- Dokumentasi ontologi/demo:
  - `ontology/ontology-design.md`
  - `docs/04-ontology-specification.md`
  - `docs/05-demo-app-guide.md`
- Aplikasi demo Streamlit:
  - `app/main.py`
  - `app/recommender.py`
  - `app/data.py`
  - `requirements.txt`
- Test aplikasi:
  - `python -m pytest -q` → `2 passed in 0.03s`.
- Smoke test Streamlit:
  - `streamlit run app/main.py --server.headless true --server.port 8510 --server.address 127.0.0.1`
  - HTTP check ke `http://127.0.0.1:8510` → status `200`.
- Script/storyboard video sudah menyesuaikan UI aktual:
  - tidak lagi menginstruksikan tombol rekomendasi.
  - opsi UI memakai `Multiplayer`, `Singkat/Sedang/Panjang`, `Mudah/Sedang/Sulit`.

### Belum / blocker sebelum dikumpulkan

1. **Final video belum ada**
   - Missing: `video/final-rpp-game-ontology.mp4`.
   - Ini blocker utama karena tugas meminta semuanya dikemas menjadi video tutorial.

2. **URL YouTube AIS belum ada**
   - Missing: `video/youtube-url.txt`.
   - Setelah upload ke channel AIS, URL harus disimpan dan dimasukkan ke pesan pengumpulan.

3. **ZIP final belum dibuat**
   - Belum ada file `*.zip` di root repo.
   - ZIP harus berisi file tugas saja, bukan folder runtime/dev.

4. **Visual QA manual belum final**
   - PPTX perlu dibuka di PowerPoint/LibreOffice untuk cek tampilan, identitas, dan layout.
   - OWL perlu dibuka di Protégé untuk cek class/property/individual dan reasoner.
   - Video harus memakai rekaman/screenshot asli, bukan placeholder/fake screenshot.

5. **Repo cleanup belum rapi untuk commit/paket**
   - Git status menunjukkan untracked:
     - `.worktrees/`
     - `node_modules/`
     - `package.json`
     - `package-lock.json`
     - `slides/`
     - `docs/06-slide-notes.md`
     - `docs/FINAL_QA.md`
   - `.gitignore` belum mengecualikan `node_modules/` dan `.worktrees/`.
   - `node_modules/`, `.worktrees/`, `.venv/`, `.pytest_cache/`, dan `__pycache__/` tidak boleh masuk ZIP.

6. **`docs/FINAL_QA.md` sudah sebagian outdated**
   - File itu masih menulis blocker mismatch script UI.
   - Audit terbaru menunjukkan script/storyboard sudah diperbaiki.
   - Perlu rerun/update final QA setelah video dan packaging selesai.

## 3. Rencana kerja dari awal sampai submit

### Phase 0 — Kunci scope, tanpa Kanban dulu

Output: pemahaman sederhana.

- Pakai scope yang sudah ada: rekomendasi game berbasis mood + preferensi dengan ontologi.
- Jangan tambah fitur besar.
- Jangan ubah studi kasus.
- Fokus pada deliverable dosen:
  - a–e = slide.
  - f = aplikasi.
  - semua = video tutorial.

### Phase 1 — Rapikan repo dev

Output: repo tidak membingungkan dan aman dipaketkan.

Langkah:
1. Update `.gitignore` untuk menambahkan:
   - `node_modules/`
   - `.worktrees/`
   - `video/final-rpp-game-ontology.mp4` bila file video besar tidak mau di-commit.
   - `*.zip`
2. Pastikan `package.json`, `package-lock.json`, `slides/generate_presentation.js`, dan slide artifacts yang memang diperlukan tetap masuk repo.
3. Jangan hapus `.venv`/`node_modules` dulu kalau masih dipakai lokal, tapi pastikan tidak masuk ZIP/commit.

### Phase 2 — Final QA teknis sebelum rekaman

Output: bukti aplikasi/ontologi/slide siap direkam.

Langkah:
1. Jalankan test:
   - `source .venv/bin/activate`
   - `python -m pytest -q`
2. Jalankan app:
   - `streamlit run app/main.py`
3. Cek demo input wajib:
   - Mood: `Stres`
   - Genre: `Casual`
   - Platform: `PC`
   - Mode: `SinglePlayer`
   - Durasi: `Sedang`
   - Difficulty: `Mudah`
4. Pastikan top result: `Stardew Valley`.
5. Buka PPTX dan cek poin a–e terlihat jelas.
6. Buka OWL di Protégé dan cek:
   - class utama ada.
   - object property utama ada.
   - individual contoh ada.
   - reasoner/DL Query bisa dijelaskan minimal secara konseptual.

### Phase 3 — Rekam video tutorial

Output: `video/final-rpp-game-ontology.mp4`.

Urutan scene yang direkomendasikan:
1. Opening judul + identitas/kelompok.
2. Slide a: cara unduh & instal Protégé.
3. Slide b: pengenalan lingkungan Protégé.
4. Slide c: deskripsi persoalan kasus.
5. Slide d: solusi ontologi + Methontology.
6. Slide e: penerapan kasus di Protégé.
7. Demo Protégé:
   - buka `ontology/game_recommendation.owl`.
   - tunjukkan classes/properties/individuals.
   - jelaskan reasoning/DL Query.
8. Demo aplikasi:
   - `streamlit run app/main.py`.
   - input demo `Stres + Casual + PC + SinglePlayer + Sedang + Mudah`.
   - jelaskan hasil `Stardew Valley`, skor, dan alasan.
9. Closing: sistem memenuhi tugas besar RPP dan bisa dikembangkan dengan data game lebih banyak.

Catatan penting:
- Jangan menyebut tombol rekomendasi karena aplikasi auto-render.
- Jangan pakai screenshot palsu sebagai bukti.
- Audio harus jelas, 16:9, ideal 1080p.

### Phase 4 — Upload YouTube AIS

Output: `video/youtube-url.txt`.

Langkah:
1. Pakai `video/youtube-upload-draft.md` untuk title/description/timestamps.
2. Upload ke channel YouTube AIS sesuai instruksi kelas.
3. Setelah upload, tonton sekali dari YouTube untuk cek audio/video.
4. Simpan URL final ke:
   - `video/youtube-url.txt`
5. Masukkan URL ke checklist/pesan pengumpulan.

### Phase 5 — Update final QA dan checklist

Output: checklist benar-benar final.

Langkah:
1. Update `docs/FINAL_QA.md` dari `REQUEST_CHANGES` menjadi status final hanya jika:
   - final MP4 ada.
   - URL YouTube ada.
   - test/app/ontology/slide sudah dicek ulang.
2. Tick item di `docs/SUBMISSION_CHECKLIST.md` yang sudah valid.
3. Pastikan tidak ada klaim palsu: kalau Protégé reasoner tidak sempat dijalankan, tulis sebagai demo konseptual atau rekaman pembukaan OWL saja.

### Phase 6 — Buat ZIP final

Output: `RPP_Game_Ontology_Febnawan_Fatur_Rochman_237006029.zip`.

Isi minimal ZIP:
- `README.md`
- `docs/00-task-brief.md`
- `docs/02-scope-and-acceptance.md`
- `docs/03-research-notes.md`
- `docs/04-ontology-specification.md`
- `docs/05-demo-app-guide.md`
- `docs/06-slide-notes.md`
- `docs/FINAL_QA.md`
- `docs/SUBMISSION_CHECKLIST.md`
- `slides/rpp-game-ontology-presentation.pptx`
- `slides/outline.md`
- `ontology/game_recommendation.owl`
- `ontology/ontology-design.md`
- `app/`
- `requirements.txt`
- `tests/test_recommender.py`
- `video/tutorial-script.md`
- `video/storyboard.md`
- `video/recording-checklist.md`
- `video/youtube-upload-draft.md`
- `video/final-rpp-game-ontology.mp4`
- `video/youtube-url.txt`

Exclude:
- `.git/`
- `.worktrees/`
- `.venv/`
- `node_modules/`
- `.pytest_cache/`
- `__pycache__/`
- `*.pyc`
- OS junk.

### Phase 7 — Final extraction test

Output: bukti ZIP bisa dijalankan.

Langkah:
1. Extract ZIP ke folder sementara.
2. Jalankan:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
   - `python -m pytest -q`
   - `streamlit run app/main.py`
3. Cek PPTX bisa dibuka.
4. Cek MP4 bisa diputar.
5. Cek `video/youtube-url.txt` berisi URL valid.

### Phase 8 — Kirim ke ketua kelas

Output: paket terkirim.

Pesan template:

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

## 4. Prioritas kerja berikutnya

Urutan paling aman:

1. Rapikan `.gitignore` supaya `node_modules/` dan `.worktrees/` tidak mengganggu.
2. Buka PPTX + OWL secara manual untuk QA visual/Protégé.
3. Rekam video final.
4. Upload ke YouTube AIS dan simpan URL.
5. Update `FINAL_QA` + checklist.
6. Buat ZIP.
7. Test ZIP hasil ekstrak.
8. Kirim.

## 5. Risiko

- Video menjadi blocker terbesar karena tidak bisa diselesaikan penuh dari repo tanpa rekaman layar/manual upload.
- Jika Protégé tidak bisa jalan di laptop, tetap bisa jelaskan OWL + struktur ontology, tapi sebaiknya minimal tampilkan OWL terbuka di Protégé agar sesuai instruksi tugas.
- Jika ZIP dibuat dari seluruh repo tanpa filter, file akan terlalu besar dan berisi folder yang tidak perlu (`node_modules`, `.venv`, `.worktrees`).
