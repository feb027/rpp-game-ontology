# Outline Presentasi RPP Game Ontology (Points a‑e)

## Slide A – Cara Unduh & Instalasi Protégé
- Sumber resmi: https://protege.stanford.edu/software/ (Desktop) & GitHub release `protegeproject/protege-distribution`.
- Versi yang dipakai: **Protégé Desktop 5.6.9** (terbaru per Mei 2026).
- Langkah instalasi per OS (Windows, Linux, macOS) – unzip, run `Protege.exe` / `./protege`.
- Tidak perlu instalasi Java terpisah untuk paket platform‑spesifik.
- **Placeholder screenshot**: `screenshots/protege-download.png`, `screenshots/protege-install-win.png`, dll.

## Slide B – Pengenalan Lingkungan Kerja Protégé
- Tab utama: **Active Ontology**, **Entities**, **Classes**, **Object/Data Properties**, **Individuals**, **DL Query**.
- Navigasi global dengan `Ctrl+F`.
- Reasoner (HermiT) untuk inferensi otomatis.
- **Placeholder screenshot**: `screenshots/protege-entities.png`, `screenshots/protege-reasoner.png`.

## Slide C – Deskripsi Persoalan Kasus (Rekomendasi Game)
- Tujuan: merekomendasikan game berdasarkan **mood** pengguna + **preferensi** (genre, platform, mode, durasi, difficulty).
- Kompetensi pertanyaan (CQs) 1‑10 – contoh: *Game apa yang cocok untuk mood santai?*.
- Diagram alur alur kerja: Input mood & preferensi → Reasoning (OWL) → Output rekomendasi + alasan.
- **Placeholder gambar**: diagram alur.

## Slide D – Deskripsi Solusi Ontologi & Reasoning
- **Methontology** sebagai metodologi rekayasa ontologi (Specification → Evaluation → Documentation).
- Kelas utama: `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, `Recommendation`.
- Object/Data Properties: `hasGenre`, `availableOn`, `suitableForMood`, `matchesPreference`, `recommendsGame`, dll.
- Contoh rule berbasis mood (Santai, Kompetitif, Stres) – ditunjukkan dalam tabel.
- Reasoner HermiT menghasilkan **inferred class hierarchy** (e.g., `RelaxingGame`).
- **Placeholder screenshot**: inferred hierarchy.

## Slide E – Penerapan Kasus di Protégé (Demo)
- Membuat individu contoh (Stardew Valley, Minecraft, Valorant, dsb.).
- Mengisi properti sesuai tabel individu.
- Menjalankan **DL Query** untuk mengekstrak rekomendasi (misal: `Game and suitableForMood value Santai`).
- Menampilkan **hasil query** dan **alasan** (property `recommendationReason`).
- Ringkasan langkah demo: buka ontology → pilih DL Query → masukkan query → lihat hasil.
- **Placeholder screenshot**: hasil DL Query.

## Catatan Tambahan untuk Presenter
- Semua teks ditulis dalam Bahasa Indonesia yang formal, cocok untuk presentasi kelas.
- Gunakan visual (ikon, tabel, diagram) pada tiap slide; hindari bullet‑only.
- Sertakan **placeholder** untuk screenshot yang akan di‑capture secara nyata setelah instalasi protégé selesai.
- Jangan menambahkan gambar palsu; user harus mengganti placeholder dengan screenshot asli.
