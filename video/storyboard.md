# Storyboard Video Tutorial

| Scene | Durasi (detik) | Visual / Screen | Narasi / Aksi |
|---:|---:|---|---|
| 1 | 10 | Opening slide: "Sistem Rekomendasi Game Berbasis Ontologi" + identitas presenter | Sapa penonton dan sebutkan konteks tugas Representasi Pengetahuan dan Penalaran. |
| 2 | 25 | Browser membuka halaman download Protégé | Jelaskan cara unduh Protégé sesuai OS. |
| 3 | 25 | File Protégé diekstrak dan aplikasi dibuka | Tunjukkan bahwa Protégé berhasil berjalan. |
| 4 | 25 | Protégé tab **Active Ontology** | Jelaskan IRI, annotation, dan metrics ontology. |
| 5 | 35 | Protégé tab **Entities / Classes** | Tunjukkan class `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, `Recommendation`. |
| 6 | 35 | Protégé tab **Object Properties** dan **Data Properties** | Jelaskan relasi `hasGenre`, `suitableForMood`, `availableOn`, `hasPlayMode`, `hasDifficulty`, `hasDuration`, serta data seperti `recommendationReason`. |
| 7 | 35 | Protégé tab **Individuals**, pilih contoh `StardewValley` / `Valorant` | Tunjukkan contoh individu dan properti yang melekat. |
| 8 | 30 | Menu **Reasoner → HermiT → Start reasoner** | Jelaskan bahwa reasoner digunakan untuk mengecek konsistensi dan inferensi. |
| 9 | 40 | Tab **DL Query** dengan query contoh `Game and suitableForMood value Santai and availableOn value PC` | Tunjukkan konsep pencarian game berdasarkan mood dan platform. |
| 10 | 45 | Terminal: setup venv, install requirements, run `streamlit run app/main.py` | Jalankan aplikasi demo Streamlit. |
| 11 | 20 | Browser membuka Streamlit: judul **🎮 Sistem Rekomendasi Game Berbasis Ontologi** | Perkenalkan aplikasi dan tujuan rekomendasi. |
| 12 | 60 | Sidebar **Input Preferensi** | Pilih input aktual: Mood `Stres`, Genre `Casual`, Platform `PC`, Mode `SinglePlayer`, Durasi `Sedang`, Tingkat kesulitan `Mudah`. |
| 13 | 35 | Bagian **Hasil Rekomendasi** otomatis berubah setelah input dipilih | Tekankan bahwa aplikasi auto-render; tidak ada tombol rekomendasi. |
| 14 | 45 | Kartu rekomendasi menampilkan judul game, **Skor kecocokan**, dan **Alasan rekomendasi** | Sorot contoh `Stardew Valley` dan jelaskan alasan kecocokan. |
| 15 | 20 | Closing slide berisi ringkasan dan ajakan eksplorasi ontology | Tutup video dan ucapkan terima kasih. |

## Detail UI Streamlit yang wajib akurat

- Sidebar header: **Input Preferensi**.
- Label input:
  - **Mood saat ini**
  - **Genre favorit**
  - **Platform**
  - **Mode bermain**
  - **Durasi bermain**
  - **Tingkat kesulitan**
- Opsi penting yang harus disebut sesuai aplikasi:
  - Mode: `Multiplayer` (kapitalisasi sesuai aplikasi).
  - Durasi: `Singkat`, `Sedang`, `Panjang`.
  - Tingkat kesulitan: `Mudah`, `Sedang`, `Sulit`.
- Output muncul otomatis setelah sidebar diubah; jangan menyebut klik tombol rekomendasi.

## Checklist aset rekaman

- [ ] Screen capture 16:9, disarankan 1920×1080.
- [ ] Audio narasi Bahasa Indonesia jernih.
- [ ] Webcam intro/outro opsional; boleh tanpa webcam jika screen recording jelas.
- [ ] Slide pembuka dan penutup siap.
- [ ] Protégé sudah bisa membuka `ontology/game_recommendation.owl`.
- [ ] Terminal sudah berada di root repo `/home/aqua/rpp-game-ontology`.
- [ ] Aplikasi Streamlit bisa dijalankan dengan `streamlit run app/main.py`.
- [ ] Browser siap di `http://localhost:8501`.
- [ ] Scene aplikasi menunjukkan rekomendasi otomatis tanpa tombol `Recommend`.
- [ ] Rekaman akhir diekspor ke `video/final-rpp-game-ontology.mp4`.
- [ ] Setelah upload, link AIS YouTube dicatat ke `video/youtube-url.txt`.
