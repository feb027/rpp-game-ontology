# Catatan Pembicara — Presentasi Ontologi Rekomendasi Game

## Slide A – Cara Unduh & Instalasi Protégé
- **Pembukaan**: "Selamat siang, hari ini kita akan mempresentasikan sistem rekomendasi game berbasis ontologi."
- **Poin 1**: Tools utama adalah Protégé Desktop versi 5.6.9, gratis dan open source dari Stanford.
- **Poin 2**: Unduh dari https://protege.stanford.edu/software/ atau GitHub release terbaru.
- **Poin 3**: Untuk Windows, unzip `Protege-5.6.9-win.zip`, jalankan `Protege.exe`. Untuk Linux, ekstrak tar.gz dan jalankan `./protege`. macOS: drag ke Applications.
- **Poin 4**: Paket sudah menyertakan JRE 64‑bit, jadi tidak perlu instal Java terpisah.
- **Poin 5**: Setelah terbuka, tampilkan "Active Ontology" tab sebagai konfirmasi instalasi.
- **Catatan**: Tunjukkan screenshot halaman download dan folder hasil ekstrak (jangan pakai gambar palsu).

## Slide B – Pengenalan Lingkungan Kerja Protégé
- **Poin 1**: Protégé adalah lingkungan pengembangan ontologi OWL 2 yang populer.
- **Poin 2**: Tab **Active Ontology** menampilkan metadata ontology aktif (IRI, annotation, metrics).
- **Poin 3**: Tab **Entities** adalah pusat navigasi: klik kiri untuk class/property/individual, detail muncul di panel kanan.
- **Poin 4**: Tab **Classes** untuk membangun hierarki konsep, **Object Properties** untuk relasi antar‑individu, **Data Properties** untuk nilai data.
- **Poin 5**: Tab **Individuals** untuk membuat instance nyata (misal: StardewValley sebagai Game).
- **Poin 6**: **Reasoner** (HermiT) digunakan untuk klasifikasi otomatis; hasil reasoning ditandai sebagai *inferred* (berbeda dari *asserted*).
- **Poin 7**: **DL Query** memungkinkan pencarian ekspresif dengan Manchester OWL Syntax setelah ontology diklasifikasi.
- **Catatan**: Tunjukkan screenshot tab‑tab penting dan menu Reasoner → HermiT.

## Slide C – Deskripsi Persoalan Kasus (Rekomendasi Game)
- **Poin 1**: Kasus: User memiliki mood (santai, kompetitif, stres, bosan, eksplorasi, sosial) dan preferensi (genre, platform, mode, durasi, difficulty).
- **Poin 2**: Sistem harus mengeluarkan rekomendasi game beserta alasan berdasarkan mood & preferensi tersebut.
- **Poin 3**: Competency Questions (CQs) yang harus dijawab ontology: 10 pertanyaan (contoh: *Game apa yang cocok untuk mood santai?*).
- **Poin 4**: Ontologi digunakan karena dapat merepresentasikan pengetahuan domain secara terstruktur dan mendukung reasoning.
- **Poin 5**: Diagram alur: Input → Ontology Reasoning → Output rekomendasi + alasan.
- **Catatan**: Tunjukkan tabel CQs dan diagram alur (bisa dibuat dengan draw.io atau PowerPoint shapes).

## Slide D – Deskripsi Solusi Ontologi & Reasoning
- **Poin 1**: Menggunakan metodologi **Methontology** (Fernández et al., 1997) dengan tahapan: Specification, Knowledge Acquisition, Conceptualization, Integration, Implementation, Evaluation, Documentation.
- **Poin 2**: Kelas utama (`Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, `Recommendation`) disusun dalam hierarki `Thing`.
- **Poin 3**: Object properties menghubungkan antar‑individu (misal: `hasGenre`, `suitableForMood`, `recommendsGame`).
- **Poin 4**: Data properties menyimpan nilai data (misal: `gameTitle`, `recommendationReason`, `priorityScore`).
- **Poin 5**: Rule sederhana: Jika game memiliki genre Casual dan cocok untuk mood Santai, maka dapat diklasifikasikan sebagai `RelaxingGame` (inferred).
- **Poin 6**: Reasoner HermiT akan menghitung konsekuensi logis dari axioms tersebut dan menampilkan *Inferred Class Hierarchy*.
- **Poin 7**: Evaluasi dilakukan dengan DL Query untuk memastikan CQs terjawab.
- **Catatan**: Tunjukkan tabel kelas/properti dan hasil inferred hierarchy setelah reasoning.

## Slide E – Penerapan Kasus di Protégé (Demo)
- **Poin 1**: Buat individu `StardewValley` bertipe `Game`, isi `hasGenre` = `Simulation`, `suitableForMood` = `Santai`, `availableOn` = `PC`, dll.
- **Poin 2**: Lakukan hal yang sama untuk individu lain (Minecraft, Valorant, Genshin Impact, dsb.) sesuai tabel seed data.
- **Poin 3**: Jalankan **Reasoner → HermiT** → **Start reasoner**. Perhatikan inferred class hierarchy muncul.
- **Poin 4**: Buka tab **DL Query**, ketik: `Game and suitableForMood value Santai and availableOn value PC` → tekan Enter. Hasilnya akan muncul daftar game yang memenuhi kriteria.
- **Poin 5**: Untuk mendapatkan alasan, periksa individu `Recommendation` yang terhubung dengan `recommendsGame` dan baca `recommendationReason`.
- **Poin 6**: Demo menunjukkan bahwa sistem dapat menjawab CQs secara otomatis via reasoning.
- **Catatan**: Lakukan live demo jika memungkinkan; jika tidak, tunjukkan screenshot hasil DL Query.

## Tips Tambahan untuk Presentasi
- Gunakan bahasa Indonesia yang jelas, hindari *jargon* berlebihan.
- Sisipkan ikon pada judul slide untuk mempercantik visual (misal: ikon download untuk slide instalasi).
- Untuk screenshot, pastikan resolusi jelas dan tidak ada informasi sensitif (path lokal, nama user, dsb.).
- Jika ada waktu, tunjukkan sebentar cara mengubah tampilan Protégé (resize view, float, split) untuk fleksibilitas.
