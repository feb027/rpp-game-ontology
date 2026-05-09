# Panduan Demo Natural — RPP Game Ontology

Judul tugas:

> Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi

Gaya bicara: santai, jelas, seperti mahasiswa semester 6 yang sedang demo tugas. Jangan terlalu teknis. Fokus ke: **apa masalahnya, apa solusinya, bagaimana ontology-nya, lalu aplikasi jalan**.

Durasi aman: **7–10 menit**.

---

## 0. Persiapan Sebelum Rekam

Buka dulu semua yang dibutuhkan supaya saat rekaman tidak banyak loading.

### Yang dibuka

1. Slide presentasi.
2. Protégé.
3. File ontology:

   ```text
   ontology/game_recommendation.owl
   ```

4. Aplikasi Streamlit:

   ```text
   https://iot.aquarise.my.id/rpp-game/
   ```

   Kalau mau lokal:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   streamlit run app/main.py
   ```

5. Folder repo untuk menunjukkan file jika perlu:

   ```text
   rpp-game-ontology
   ```

### Jangan lupa

- Zoom browser sekitar 100% atau 110%.
- Protégé jangan terlalu kecil.
- Kalau DL Query muncul `owl:Nothing`, jangan panik. Lihat bagian **Instances**, bukan **Subclasses**.
- Jangan jelaskan semua 18 game satu per satu. Cukup bilang dataset berisi 18 contoh game.

---

## 1. Pembukaan Video

### Tampilan layar

Slide judul atau halaman awal aplikasi.

### Script ngomong

> Assalamualaikum warahmatullahi wabarakatuh.  
> Halo, perkenalkan saya Febnawan Fatur Rochman dari Informatika A.  
> Pada video ini saya akan mendemokan tugas besar mata kuliah Representasi Pengetahuan dan Penalaran, dengan judul Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi.

> Jadi idenya sederhana. Kadang pengguna ingin main game, tapi pilihannya banyak dan belum tentu cocok dengan mood saat itu. Misalnya sedang stres, ingin game yang santai. Atau sedang ingin kompetitif, berarti lebih cocok ke game seperti FPS atau multiplayer.  
> Karena itu, saya membuat ontology untuk memodelkan hubungan antara game, mood, genre, platform, mode bermain, durasi, dan tingkat kesulitan.

---

## 2. Deskripsi Kasus

### Tampilan layar

Slide bagian persoalan kasus / scope.

### Script ngomong

> Studi kasus yang saya ambil adalah rekomendasi game berdasarkan preferensi dan mood.  
> Input yang dipakai ada beberapa, yaitu mood pengguna, genre favorit, platform, mode bermain, durasi bermain, dan tingkat kesulitan.

> Contohnya, kalau pengguna memilih mood stres, genre casual, platform PC, mode single player, durasi sedang, dan difficulty mudah, sistem akan mencoba memberi rekomendasi game yang paling cocok berdasarkan data pengetahuan yang sudah dibuat.

> Jadi di sini sistemnya bukan hanya list game biasa, tapi game-game tersebut dimodelkan dulu sebagai pengetahuan dalam ontology.

---

## 3. Penjelasan Solusi Singkat

### Tampilan layar

Slide solusi / Methontology / struktur ontology.

### Script ngomong

> Untuk pengembangan ontology, saya mengacu ke pendekatan Methontology. Tahapannya dimulai dari menentukan domain dan tujuan, mengumpulkan konsep penting, membuat class dan property, lalu mengimplementasikannya di Protégé.

> Class utama yang saya pakai antara lain `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, `PlayerPreference`, dan `Recommendation`.

> Kemudian relasinya dibuat memakai object property, misalnya `hasGenre`, `suitableForMood`, `availableOn`, `hasPlayMode`, dan `recommendsGame`.

> Untuk data contoh, ontology ini berisi 18 game, seperti Stardew Valley, Minecraft, Valorant, Counter-Strike 2, Apex Legends, Unpacking, Journey, dan beberapa game lain.

---

## 4. Demo Protégé — Buka Ontology

### Tampilan layar

Protégé → file `game_recommendation.owl` sudah terbuka.

### Yang dilakukan

1. Tunjukkan tab **Active Ontology**.
2. Tunjukkan nama/IRI ontology.
3. Pindah ke **Entities → Classes**.

### Script ngomong

> Sekarang saya buka file ontology-nya di Protégé. File yang digunakan adalah `game_recommendation.owl`.

> Di bagian Active Ontology ini terlihat bahwa ontology sudah berhasil dibuka. Selanjutnya kita bisa lihat struktur class-nya di bagian Entities.

---

## 5. Demo Protégé — Class Hierarchy

### Tampilan layar

Entities → Classes.

### Yang ditunjukkan

Expand class:

- `Game`
- `Genre`
- `Mood`
- `Platform`
- `PlayMode`
- `Difficulty`
- `Duration`
- `PlayerPreference`
- `Recommendation`

Kalau ada subclass di bawah `Game`, tunjukkan juga:

- `RelaxingGame`
- `CompetitiveGame`
- `ExplorationGame`
- `SocialGame`

### Script ngomong

> Di sini terlihat class utama dari ontology.  
> `Game` digunakan untuk merepresentasikan game yang bisa direkomendasikan.  
> `Mood` untuk kondisi pengguna, seperti santai, stres, kompetitif, bosan, eksploratif, dan sosial.  
> Lalu ada `Genre`, `Platform`, `PlayMode`, `Difficulty`, dan `Duration` untuk menyimpan preferensi permainan.

> Class `Recommendation` digunakan untuk merepresentasikan hasil rekomendasi, jadi bukan hanya game-nya saja, tapi juga alasan dan skor prioritasnya.

> Saya juga membuat subclass seperti `RelaxingGame`, `CompetitiveGame`, `ExplorationGame`, dan `SocialGame` supaya pengelompokan game lebih mudah dijelaskan.

---

## 6. Demo Protégé — Object Property dan Data Property

### Tampilan layar

Entities → Object properties, lalu Data properties.

### Yang ditunjukkan

Object property:

- `hasGenre`
- `suitableForMood`
- `availableOn`
- `hasPlayMode`
- `hasDifficulty`
- `hasDuration`
- `recommendsGame`

Data property:

- `gameTitle`
- `recommendationReason`
- `priorityScore`

### Script ngomong

> Selanjutnya bagian property.  
> Object property dipakai untuk menghubungkan satu individual dengan individual lain. Misalnya game memiliki genre, cocok untuk mood tertentu, tersedia di platform tertentu, dan memiliki mode bermain tertentu.

> Contohnya `suitableForMood` menghubungkan game dengan mood, lalu `hasGenre` menghubungkan game dengan genre.

> Untuk data property, saya menggunakan `gameTitle` untuk judul game, `recommendationReason` untuk alasan rekomendasi, dan `priorityScore` untuk skor prioritas rekomendasi.

---

## 7. Demo Protégé — Individual Game

### Tampilan layar

Entities → Individuals.

### Yang ditunjukkan

Klik individual:

- `StardewValley`
- `Valorant`
- `CounterStrike2`
- `Unpacking`

Tunjukkan bagian property assertions.

### Script ngomong

> Sekarang kita lihat individual atau instance. Individual ini adalah data nyata dari ontology.

> Contohnya `StardewValley`. Di sini terlihat game ini punya genre Simulation dan Casual, cocok untuk mood Santai dan Stres, tersedia di PC, Console, dan Mobile, lalu difficulty-nya mudah.

> Jadi kalau nanti pengguna memilih mood stres dan ingin game casual yang mudah, Stardew Valley bisa muncul sebagai rekomendasi.

> Contoh lain, `Valorant` dan `CounterStrike2` cocok untuk mood kompetitif, genre FPS, platform PC, dan mode multiplayer. Jadi dua game ini masuk akal kalau pengguna ingin game kompetitif.

---

## 8. Demo Protégé — Reasoner HermiT

### Tampilan layar

Menu Reasoner.

### Yang dilakukan

1. Klik:

   ```text
   Reasoner → HermiT
   ```

2. Klik:

   ```text
   Reasoner → Start reasoner
   ```

3. Tunggu selesai.

### Script ngomong

> Setelah struktur ontology dibuat, saya menjalankan reasoner HermiT. Reasoner ini dipakai untuk mengecek apakah ontology konsisten atau tidak.

> Kalau ontology konsisten, berarti class, property, individual, dan tipe datanya tidak saling bertentangan.

> Di demo ini reasoner berhasil dijalankan, sehingga ontology bisa dipakai untuk query.

### Kalau HermiT agak lama

> Kita tunggu sebentar karena reasoner sedang membaca relasi dan axiom yang ada di ontology.

### Kalau ada `owl:Nothing`

> Di DL Query kadang muncul `owl:Nothing` pada bagian Subclasses. Itu tidak masalah, karena yang kita lihat untuk demo rekomendasi adalah bagian Instances atau Individuals.

---

## 9. Demo Protégé — DL Query

### Tampilan layar

Tab DL Query.

Kalau belum ada:

```text
Window → Tabs → DL Query
```

### Query 1 — Stres, Casual, PC, Mudah

Masukkan:

```text
Game and suitableForMood value Stres and hasGenre value Casual and availableOn value PC and hasDifficulty value Mudah
```

Expected di bagian **Instances**:

- `StardewValley`
- `Unpacking`
- `Journey`

### Script ngomong

> Sekarang saya coba query pertama. Query ini mencari game yang cocok untuk mood stres, genre casual, tersedia di PC, dan difficulty-nya mudah.

> Hasilnya muncul beberapa game seperti Stardew Valley, Unpacking, dan Journey. Artinya ontology berhasil menemukan game yang memenuhi kriteria tersebut.

### Query 2 — Kompetitif, FPS, PC, Multiplayer

Masukkan:

```text
Game and suitableForMood value Kompetitif and availableOn value PC and hasPlayMode value Multiplayer and hasGenre value FPS
```

Expected di bagian **Instances**:

- `Valorant`
- `CounterStrike2`
- `ApexLegends`

### Script ngomong

> Query kedua untuk kondisi yang berbeda. Di sini saya mencari game yang cocok untuk mood kompetitif, tersedia di PC, mode multiplayer, dan genre FPS.

> Hasilnya adalah Valorant, Counter-Strike 2, dan Apex Legends. Ini sesuai dengan data yang sudah dimodelkan di ontology.

### Catatan penting

Kalau hasil layar menampilkan:

```text
owl:Nothing
```

Jangan langsung bilang error. Katakan:

> Yang muncul di bagian Subclasses adalah `owl:Nothing`, itu normal karena ekspresi query ini tidak punya subclass. Untuk hasil rekomendasi, yang dilihat adalah bagian Instances.

---

## 10. Demo Visualisasi Ontology — OntoGraf

### Tampilan layar

Tab OntoGraf.

Kalau belum ada:

```text
Window → Tabs → OntoGraf
```

### Yang ditampilkan

Jangan tampilkan semua node. Pilih sedikit saja:

- `Game`
- `Mood`
- `Genre`
- `StardewValley`
- `Stres`
- `Casual`
- `PC`
- `Recommendation_Stardew_Stress_PC`

### Script ngomong

> Untuk visualisasi, saya menggunakan OntoGraf. Di sini ontology bisa dilihat dalam bentuk graf.

> Node merepresentasikan class atau individual, sedangkan garis atau relasinya menunjukkan property. Misalnya Stardew Valley terhubung dengan mood Stres, genre Casual, dan platform PC.

> Saya tidak menampilkan semua data karena kalau semua 18 game dimunculkan, grafnya akan terlalu padat. Jadi untuk demo saya tampilkan sebagian node yang mewakili alur rekomendasi.

---

## 11. Demo Aplikasi Streamlit

### Tampilan layar

Buka:

```text
https://iot.aquarise.my.id/rpp-game/
```

Atau lokal:

```text
http://localhost:8501
```

### Script pembuka aplikasi

> Setelah ontology dibuat dan diuji di Protégé, saya juga membuat aplikasi demo sederhana menggunakan Streamlit.

> Aplikasi ini digunakan supaya konsep rekomendasi tadi bisa dicoba langsung oleh pengguna dengan input yang lebih mudah.

### Input demo 1 — Stres / Casual

Pilih:

| Input | Nilai |
|---|---|
| Mood saat ini | `Stres` |
| Genre favorit | `Casual` |
| Platform | `PC` |
| Mode bermain | `SinglePlayer` |
| Durasi bermain | `Sedang` |
| Tingkat kesulitan | `Mudah` |

### Script ngomong

> Untuk contoh pertama, saya pilih mood Stres, genre Casual, platform PC, mode SinglePlayer, durasi Sedang, dan difficulty Mudah.

> Setelah input dipilih, aplikasi langsung menghitung rekomendasi tanpa tombol tambahan.

> Di bagian hasil, muncul game dengan skor kecocokan dan alasan rekomendasi. Misalnya Stardew Valley cocok karena mendukung mood stres, genre casual, tersedia di PC, dan tingkat kesulitannya mudah.

### Input demo 2 — Kompetitif / FPS

Pilih:

| Input | Nilai |
|---|---|
| Mood saat ini | `Kompetitif` |
| Genre favorit | `FPS` |
| Platform | `PC` |
| Mode bermain | `Multiplayer` |
| Durasi bermain | `Singkat` atau `Sedang` |
| Tingkat kesulitan | `Sulit` |

### Script ngomong

> Untuk contoh kedua, saya coba kondisi kompetitif. Saya pilih mood Kompetitif, genre FPS, platform PC, mode Multiplayer, dan difficulty Sulit.

> Hasilnya mengarah ke game seperti Valorant, Counter-Strike 2, dan Apex Legends. Ini sama seperti hasil query di Protégé, sehingga data aplikasi dan ontology-nya konsisten.

---

## 12. Penjelasan Hubungan Protégé dan Aplikasi

### Tampilan layar

Bisa tetap di aplikasi, atau pindah sebentar ke repo/file `ontology/game_recommendation.owl`.

### Script ngomong

> Jadi hubungan antara Protégé dan aplikasi ini adalah: Protégé digunakan untuk membangun dan memeriksa model pengetahuannya, sedangkan aplikasi Streamlit digunakan sebagai demo interaktif untuk pengguna.

> Data game, mood, genre, platform, dan preferensi dibuat konsisten dengan file ontology. Jadi aplikasi bukan berdiri sendiri tanpa konsep, tapi mengikuti struktur pengetahuan yang sudah dimodelkan.

> Untuk tugas ini, fokusnya adalah menunjukkan bahwa kasus rekomendasi game bisa direpresentasikan sebagai ontology, lalu digunakan untuk proses pencarian rekomendasi berdasarkan kriteria tertentu.

---

## 13. Penutup

### Tampilan layar

Slide penutup atau aplikasi.

### Script ngomong

> Dari demo ini bisa disimpulkan bahwa ontology dapat digunakan untuk merepresentasikan pengetahuan dalam domain rekomendasi game.

> Dengan Protégé, kita bisa membuat class, property, individual, menjalankan reasoner, dan mencoba query. Kemudian dengan aplikasi Streamlit, pengguna bisa mencoba rekomendasi secara langsung melalui input yang lebih sederhana.

> Sekian demo dari saya. Terima kasih sudah menyimak. Wassalamualaikum warahmatullahi wabarakatuh.

---

## 14. Versi Super Singkat Kalau Waktu Mepet

Pakai ini kalau dosen/rekaman minta cepat.

### Pembukaan

> Halo, saya Febnawan. Di video ini saya mendemokan sistem rekomendasi game berdasarkan preferensi dan mood menggunakan ontology.

### Kasus

> Masalahnya, pengguna sering bingung memilih game yang cocok dengan kondisi mereka. Jadi saya membuat ontology yang menghubungkan game dengan mood, genre, platform, mode bermain, durasi, dan difficulty.

### Protégé

> Di Protégé, ontology ini memiliki class seperti Game, Mood, Genre, Platform, PlayMode, Difficulty, Duration, PlayerPreference, dan Recommendation.  
> Untuk relasinya ada property seperti hasGenre, suitableForMood, availableOn, hasPlayMode, dan recommendsGame.

### Individual

> Contohnya Stardew Valley cocok untuk mood Stres dan Santai, punya genre Casual dan Simulation, serta tersedia di PC. Untuk game kompetitif ada Valorant, Counter-Strike 2, dan Apex Legends.

### Query

> Saya jalankan query untuk mood Stres, genre Casual, platform PC, dan difficulty Mudah. Hasilnya muncul Stardew Valley, Unpacking, dan Journey.  
> Lalu query kompetitif FPS multiplayer di PC menghasilkan Valorant, Counter-Strike 2, dan Apex Legends.

### Aplikasi

> Setelah itu saya buka aplikasi Streamlit. Pengguna tinggal memilih mood dan preferensi, lalu sistem menampilkan rekomendasi beserta skor dan alasan.

### Penutup

> Jadi ontology di sini digunakan sebagai representasi pengetahuan, sedangkan aplikasi digunakan sebagai demo agar rekomendasi bisa dicoba langsung.

---

## 15. Checklist Saat Rekaman

- [ ] Slide judul terlihat.
- [ ] Protégé membuka `game_recommendation.owl`.
- [ ] Class hierarchy terlihat.
- [ ] Object properties terlihat.
- [ ] Individual `StardewValley` terlihat.
- [ ] HermiT reasoner dijalankan.
- [ ] DL Query 1 menghasilkan rekomendasi stress/casual.
- [ ] DL Query 2 menghasilkan rekomendasi kompetitif/FPS.
- [ ] OntoGraf ditunjukkan singkat.
- [ ] Aplikasi Streamlit dibuka.
- [ ] Input demo 1 dicoba.
- [ ] Input demo 2 dicoba.
- [ ] Penutup singkat.

---

## 16. Bagian yang Tidak Perlu Dibahas Panjang

Jangan terlalu lama menjelaskan ini:

- Detail kode Python.
- Semua isi file OWL.
- Semua 18 game satu per satu.
- Semua tahap Methontology secara teori panjang.
- Error teknis seperti virtual environment, package install, atau Caddy deployment.

Cukup sebut kalau perlu:

> Bagian teknis seperti kode dan deployment sudah disiapkan, tapi fokus demo ini adalah penggunaan ontology di Protégé dan hasil rekomendasi aplikasinya.
