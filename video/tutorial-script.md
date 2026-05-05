# Skrip Narasi Video Tutorial

## Pendahuluan
- **Salam pembuka**: "Selamat siang, teman‑teman! Hari ini kita akan belajar membuat sistem rekomendasi game berbasis ontologi menggunakan Protégé dan aplikasi demo sederhana."
- **Perkenalan diri**: "Saya [Nama], mahasiswa Informatika FT UNSIL, mempersembahkan projek untuk mata kuliah Representasi Pengetahuan dan Penalaran."
- **Tujuan video**: menjelaskan instalasi alat, pengenalan lingkungan Protégé, penerapan ontologi, dan demo aplikasi rekomendasi game.

## Bagian 1 – Instalasi Protégé (Slide A)
1. Buka https://protege.stanford.edu/software/ atau halaman GitHub release Protégé.
2. Unduh versi sesuai OS (Windows: `.zip`, Linux: `.tar.gz`, macOS: `.dmg`).
3. Ekstrak, lalu jalankan `Protege.exe` (Windows) atau `./protege` (Linux).
4. Tampilkan tab **Active Ontology** sebagai bukti Protégé berhasil dibuka.

## Bagian 2 – Mengenal Lingkungan Protégé (Slide B)
- Tab **Active Ontology**: metadata, IRI, annotation, dan metrics ontology.
- Tab **Entities / Classes**: hierarki konsep seperti `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, dan `Recommendation`.
- Tab **Object Properties**: relasi antarindividu, misalnya `hasGenre`, `suitableForMood`, `availableOn`, `hasPlayMode`, `hasDifficulty`, dan `hasDuration`.
- Tab **Data Properties**: atribut data seperti `gameTitle`, `recommendationReason`, dan `priorityScore`.
- Tab **Individuals**: contoh instance nyata seperti `StardewValley` dan `Valorant`.
- **Reasoner HermiT**: digunakan untuk mengecek konsistensi dan inferensi ontology.
- **DL Query**: digunakan untuk mencoba query berbasis Manchester OWL Syntax.

## Bagian 3 – Deskripsi Kasus & Solusi (Slide C & D)
- Kasus: pengguna ingin rekomendasi game berdasarkan mood dan preferensi bermain.
- Preferensi yang dipakai: mood, genre, platform, mode bermain, durasi bermain, dan tingkat kesulitan.
- Ontologi dibangun dengan tahapan Methontology: specification, knowledge acquisition, conceptualization, integration, implementation, evaluation, dan documentation.
- Kelas utama: `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, dan `Recommendation`.
- Contoh rule konseptual: game dengan genre casual, durasi singkat/sedang, dan tingkat kesulitan mudah dapat direkomendasikan untuk pengguna yang ingin bermain santai atau mengurangi stres.
- Reasoner membantu memastikan relasi antar kelas, properti, dan individu tetap konsisten.

## Bagian 4 – Demo Protégé (Slide E)
1. Buka file `ontology/game_recommendation.owl` di Protégé.
2. Tampilkan hierarki class dan jelaskan hubungan konsep game, mood, genre, platform, mode, durasi, dan difficulty.
3. Buka contoh individu `StardewValley` atau `Valorant`.
4. Tunjukkan relasi seperti `hasGenre`, `suitableForMood`, `availableOn`, `hasPlayMode`, `hasDifficulty`, dan `hasDuration`.
5. Jalankan **Reasoner → HermiT → Start reasoner** untuk menunjukkan proses reasoning.
6. Jika DL Query tersedia, contohkan query seperti `Game and suitableForMood value Santai and availableOn value PC`.
7. Jelaskan bahwa hasil reasoning ini menjadi dasar konsep yang kemudian didemokan dalam aplikasi Streamlit.

## Bagian 5 – Demo Aplikasi Streamlit

### Persiapan run aplikasi
```bash
cd /home/aqua/rpp-game-ontology
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/main.py
```

### UI yang harus ditunjukkan
- Judul halaman: **🎮 Sistem Rekomendasi Game Berbasis Ontologi**.
- Sidebar: **Input Preferensi**.
- Label input aktual di aplikasi:
  - **Mood saat ini**: `Santai`, `Kompetitif`, `Stres`, `Bosan`, `Eksploratif`, `Sosial`.
  - **Genre favorit**: `Bebas` atau genre seperti `Casual`, `Simulation`, `RPG`, `FPS`, dan lainnya.
  - **Platform**: `Bebas`, `Console`, `Mobile`, `PC`.
  - **Mode bermain**: `Bebas`, `Coop`, `Multiplayer`, `SinglePlayer`.
  - **Durasi bermain**: `Bebas`, `Singkat`, `Sedang`, `Panjang`.
  - **Tingkat kesulitan**: `Bebas`, `Mudah`, `Sedang`, `Sulit`.

### Alur demo sesuai aplikasi saat ini
1. Buka aplikasi di browser, biasanya `http://localhost:8501`.
2. Pilih contoh input berikut di sidebar:
   - **Mood saat ini**: `Stres`
   - **Genre favorit**: `Casual`
   - **Platform**: `PC`
   - **Mode bermain**: `SinglePlayer`
   - **Durasi bermain**: `Sedang`
   - **Tingkat kesulitan**: `Mudah`
3. Tidak ada tombol rekomendasi. Setelah pilihan diubah, aplikasi otomatis menghitung dan menampilkan rekomendasi.
4. Tunjukkan bagian **Hasil Rekomendasi**.
5. Sorot kartu rekomendasi, **Skor kecocokan**, dan daftar **Alasan rekomendasi**.
6. Jelaskan contoh hasil: `Stardew Valley` cocok karena mendukung mood `Stres`, genre `Casual`, platform `PC`, mode `SinglePlayer`, durasi `Sedang`, dan tingkat kesulitan `Mudah`.
7. Tutup dengan catatan bahwa aplikasi memakai data yang konsisten dengan `ontology/game_recommendation.owl` dan reasoning rule-based agar mudah dijelaskan dalam demo kuliah.

## Bagian 6 – Penutup
- Ringkas langkah: instalasi Protégé, pengenalan environment Protégé, model ontologi, reasoning, dan demo aplikasi.
- Ajak penonton mengeksplorasi ontology: menambah game, mengubah preferensi, atau memperluas aturan rekomendasi.
- Ucapkan terima kasih.

---
*Catatan produksi: narasi memakai Bahasa Indonesia, gaya mahasiswa yang menjelaskan projek kuliah secara jelas dan tidak terlalu formal.*
