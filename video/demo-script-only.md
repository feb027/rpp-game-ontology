# Script Demo Saja — Bagian Febnawan

Konteks: ini untuk presentasi kelompok. Bagian sebelumnya sudah menjelaskan judul, latar belakang, metode, dan slide. Jadi bagian ini **langsung demo**, tanpa perkenalan ulang.

Gaya bicara: santai, sat-set, tidak terlalu formal. Fokus ke menunjukkan bahwa ontology di Protégé jalan dan aplikasi rekomendasi juga jalan.

Durasi target: **4–6 menit**.

---

## 0. Persiapan Sebelum Giliran Demo

Buka dulu sebelum mulai bicara:

1. Protégé dengan file:

   ```text
   ontology/game_recommendation.owl
   ```

2. Tab Protégé yang disiapkan:
   - **Entities → Classes**
   - **Object properties**
   - **Data properties**
   - **Individuals**
   - **DL Query**
   - **OntoGraf** kalau mau ditampilkan

3. Aplikasi Streamlit:

   ```text
   https://iot.aquarise.my.id/rpp-game/
   ```

4. Kalau aplikasi lokal:

   ```powershell
   streamlit run app/main.py
   ```

---

# SCRIPT UTAMA

## 1. Masuk ke Demo Protégé

### Layar
Protégé sudah terbuka di file `game_recommendation.owl`.

### Ngomong

> Oke, sekarang saya langsung masuk ke bagian demonya.  
> Di sini file ontology-nya sudah saya buka di Protégé, namanya `game_recommendation.owl`.

> Jadi di file ini kita sudah punya model pengetahuan untuk rekomendasi game berdasarkan mood dan preferensi pengguna.

---

## 2. Tunjukkan Class

### Layar
`Entities → Classes`

### Klik / tunjukkan
Expand:

- `Game`
- `Mood`
- `Genre`
- `Platform`
- `PlayMode`
- `Difficulty`
- `Duration`
- `Recommendation`

### Ngomong

> Di bagian class ini, konsep utamanya ada `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, dan `Recommendation`.

> Jadi `Game` itu objek yang akan direkomendasikan.  
> `Mood` untuk kondisi pengguna, misalnya stres, santai, kompetitif, bosan, eksploratif, dan sosial.  
> Lalu class lain seperti genre, platform, mode bermain, durasi, dan difficulty dipakai sebagai kriteria rekomendasi.

> Di sini juga ada class turunan seperti `RelaxingGame`, `CompetitiveGame`, `ExplorationGame`, dan `SocialGame`, supaya game bisa dikelompokkan lebih mudah.

---

## 3. Tunjukkan Object Property

### Layar
`Entities → Object properties`

### Klik / tunjukkan
Tunjukkan beberapa property:

- `hasGenre`
- `suitableForMood`
- `availableOn`
- `hasPlayMode`
- `hasDifficulty`
- `hasDuration`
- `recommendsGame`

### Ngomong

> Selanjutnya ini bagian relasinya.  
> Misalnya `hasGenre` untuk menghubungkan game dengan genre, `suitableForMood` untuk menghubungkan game dengan mood yang cocok, dan `availableOn` untuk platform.

> Jadi misalnya satu game bisa punya genre Casual, cocok untuk mood Stres, dan tersedia di PC. Relasi seperti ini yang nanti dipakai untuk proses rekomendasi.

---

## 4. Tunjukkan Data Property

### Layar
`Entities → Data properties`

### Klik / tunjukkan

- `gameTitle`
- `recommendationReason`
- `priorityScore`

### Ngomong

> Kalau data property ini dipakai untuk nilai biasa.  
> Contohnya `gameTitle` untuk judul game, `recommendationReason` untuk alasan rekomendasi, dan `priorityScore` untuk skor prioritasnya.

---

## 5. Tunjukkan Individual Game

### Layar
`Entities → Individuals`

### Klik `StardewValley`

### Ngomong

> Sekarang kita lihat contoh individual.  
> Ini `StardewValley`, dia termasuk individual dari class `Game`.

> Di sini kelihatan property-nya. Stardew Valley punya genre Casual dan Simulation, cocok untuk mood Santai dan Stres, tersedia di PC, Console, dan Mobile, lalu difficulty-nya Mudah.

> Jadi kalau pengguna sedang stres dan ingin game yang santai atau casual, Stardew Valley bisa direkomendasikan.

### Klik `Valorant` atau `CounterStrike2`

### Ngomong

> Contoh lainnya, ini `Valorant` atau `CounterStrike2`.  
> Game ini cocok untuk mood Kompetitif, genre FPS, platform PC, dan mode Multiplayer.

> Jadi nanti kalau input pengguna arahnya kompetitif dan FPS, game seperti ini yang akan muncul.

---

## 6. Jalankan HermiT Reasoner

### Layar
Menu `Reasoner`

### Klik

```text
Reasoner → HermiT
Reasoner → Start reasoner
```

### Ngomong

> Setelah datanya dibuat, saya jalankan reasoner HermiT.  
> Fungsinya untuk mengecek apakah ontology ini konsisten atau tidak.

> Kalau tidak ada error inconsistent, berarti relasi class, property, dan individual-nya aman untuk dipakai query.

Kalau reasoner butuh waktu:

> Kita tunggu sebentar, karena HermiT sedang membaca struktur ontology-nya.

---

## 7. Demo DL Query 1 — Stres Casual

### Layar
Tab `DL Query`

### Query
Paste query ini:

```text
Game and suitableForMood value Stres and hasGenre value Casual and availableOn value PC and hasDifficulty value Mudah
```

### Expected di bagian Instances

- `StardewValley`
- `Unpacking`
- `Journey`

### Ngomong

> Sekarang saya coba query pertama.  
> Query ini artinya mencari game yang cocok untuk mood Stres, genre Casual, tersedia di PC, dan difficulty-nya Mudah.

> Hasilnya muncul di bagian Instances, seperti Stardew Valley, Unpacking, dan Journey.

> Jadi dari sini kelihatan kalau ontology bisa mencari game berdasarkan kombinasi kriteria.

### Kalau muncul `owl:Nothing`

> Kalau di bagian Subclasses muncul `owl:Nothing`, itu tidak masalah. Yang kita lihat untuk hasil rekomendasi adalah bagian Instances.

---

## 8. Demo DL Query 2 — Kompetitif FPS

### Query
Paste query ini:

```text
Game and suitableForMood value Kompetitif and availableOn value PC and hasPlayMode value Multiplayer and hasGenre value FPS
```

### Expected di bagian Instances

- `Valorant`
- `CounterStrike2`
- `ApexLegends`

### Ngomong

> Query kedua saya coba untuk kondisi kompetitif.  
> Di sini kriterianya mood Kompetitif, platform PC, mode Multiplayer, dan genre FPS.

> Hasilnya muncul Valorant, CounterStrike2, dan ApexLegends.

> Ini sesuai dengan data yang tadi kita lihat di individual game.

---

## 9. Tunjukkan OntoGraf Singkat

### Layar
Tab `OntoGraf`

Kalau tidak sempat, boleh skip. Kalau ditampilkan, jangan semua node.

### Tampilkan node contoh

- `StardewValley`
- `Stres`
- `Casual`
- `PC`
- `Recommendation_Stardew_Stress_PC`

### Ngomong

> Untuk visualisasinya, di Protégé juga bisa pakai OntoGraf.  
> Di sini bentuknya graf, jadi node-nya mewakili class atau individual, lalu garisnya mewakili relasi.

> Saya tampilkan sebagian saja supaya tidak terlalu penuh. Dari sini bisa terlihat hubungan antara game, mood, genre, platform, dan rekomendasi.

---

## 10. Pindah ke Aplikasi Streamlit

### Layar
Buka:

```text
https://iot.aquarise.my.id/rpp-game/
```

### Ngomong

> Setelah ontology-nya bisa dipakai di Protégé, sekarang saya tunjukkan aplikasi demo sederhananya.

> Aplikasi ini dibuat supaya pengguna bisa mencoba rekomendasi lewat input yang lebih mudah, tanpa harus menulis query di Protégé.

---

## 11. Demo Aplikasi — Input Stres Casual

### Pilih input

| Field | Nilai |
|---|---|
| Mood saat ini | `Stres` |
| Genre favorit | `Casual` |
| Platform | `PC` |
| Mode bermain | `SinglePlayer` |
| Durasi bermain | `Sedang` |
| Tingkat kesulitan | `Mudah` |

### Ngomong

> Untuk contoh pertama, saya pilih mood Stres.  
> Genre-nya Casual, platform PC, mode SinglePlayer, durasi Sedang, dan tingkat kesulitan Mudah.

> Aplikasinya langsung menampilkan rekomendasi. Di sini ada nama game, skor kecocokan, dan alasan kenapa game itu direkomendasikan.

> Jadi misalnya Stardew Valley cocok karena dia casual, cocok untuk mood stres, tersedia di PC, dan difficulty-nya mudah.

---

## 12. Demo Aplikasi — Input Kompetitif FPS

### Pilih input

| Field | Nilai |
|---|---|
| Mood saat ini | `Kompetitif` |
| Genre favorit | `FPS` |
| Platform | `PC` |
| Mode bermain | `Multiplayer` |
| Durasi bermain | `Singkat` atau `Sedang` |
| Tingkat kesulitan | `Sulit` |

### Ngomong

> Sekarang saya coba contoh kedua, yaitu pengguna yang ingin game kompetitif.  
> Saya pilih mood Kompetitif, genre FPS, platform PC, mode Multiplayer, dan difficulty Sulit.

> Hasilnya mengarah ke game kompetitif seperti Valorant, Counter-Strike 2, dan Apex Legends.

> Ini nyambung dengan query yang tadi kita jalankan di Protégé, jadi data aplikasi dan ontology-nya konsisten.

---

## 13. Closing Bagian Demo

### Layar
Tetap di aplikasi atau kembali ke slide berikutnya.

### Ngomong

> Jadi dari demo ini, bagian Protégé dipakai untuk membangun dan menguji ontology-nya, sedangkan aplikasi Streamlit dipakai sebagai tampilan demo untuk pengguna.

> Dengan begitu, rekomendasi game bisa dijelaskan dari sisi representasi pengetahuan, bukan hanya dari pencocokan data biasa.

> Oke, itu saja untuk bagian demo dari saya.

---

# Versi Lebih Sat-Set Kalau Harus Cepat

Pakai kalau waktu tinggal 2–3 menit.

## Protégé

> Saya langsung ke demo ontology-nya. Di Protégé ini sudah terbuka file `game_recommendation.owl`.

> Class utamanya ada `Game`, `Mood`, `Genre`, `Platform`, `PlayMode`, `Difficulty`, `Duration`, dan `Recommendation`.

> Relasinya ada `hasGenre`, `suitableForMood`, `availableOn`, `hasPlayMode`, dan `recommendsGame`.

> Contoh individualnya, `StardewValley` punya genre Casual dan Simulation, cocok untuk mood Stres dan Santai, serta tersedia di PC. Sedangkan `Valorant` dan `CounterStrike2` cocok untuk mood Kompetitif, genre FPS, dan mode Multiplayer.

## Query

> Saya coba query untuk mood Stres, genre Casual, PC, dan difficulty Mudah. Hasilnya muncul Stardew Valley, Unpacking, dan Journey.

> Lalu query kompetitif FPS multiplayer di PC menghasilkan Valorant, CounterStrike2, dan ApexLegends.

## Aplikasi

> Sekarang di aplikasi, pengguna tinggal memilih mood dan preferensi. Contohnya mood Stres, genre Casual, platform PC, mode SinglePlayer, durasi Sedang, dan difficulty Mudah.

> Sistem langsung menampilkan rekomendasi beserta skor dan alasannya.

> Kalau dipilih Kompetitif, FPS, PC, Multiplayer, dan Sulit, hasilnya mengarah ke game seperti Valorant, Counter-Strike 2, dan Apex Legends.

## Tutup

> Jadi Protégé dipakai untuk model ontology-nya, dan aplikasi ini dipakai untuk mendemokan hasil rekomendasinya.

---

# Checklist Cepat Sebelum Presentasi

- [ ] Protégé sudah buka file OWL.
- [ ] HermiT sudah bisa jalan.
- [ ] DL Query 1 sudah disiapkan.
- [ ] DL Query 2 sudah disiapkan.
- [ ] Aplikasi sudah terbuka di browser.
- [ ] Input demo stres/casual sudah tahu urutannya.
- [ ] Input demo kompetitif/FPS sudah tahu urutannya.
- [ ] Jangan bahas instalasi terlalu lama.
- [ ] Jangan bahas kode terlalu lama.
- [ ] Jangan perkenalan ulang, langsung demo.
