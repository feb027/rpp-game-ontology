const pptxgen = require('pptxgenjs');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Febnawan Fatur Rochman';
pptx.subject = 'Representasi Pengetahuan dan Penalaran';
pptx.title = 'Sistem Rekomendasi Game Berdasarkan Preferensi dan Mood Menggunakan Ontologi';
pptx.company = 'FT UNSIL';
pptx.lang = 'id-ID';
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'id-ID'
};
pptx.defineSlideMaster({
  title: 'CONTENT',
  background: { color: 'F8FAFC' },
  objects: [
    { line: { x: 0.4, y: 6.95, w: 12.5, h: 0, line: { color: 'CBD5E1', width: 1 } } },
    { text: { text: 'RPP • Game Recommendation Ontology', options: { x: 0.45, y: 7.02, w: 6.5, h: 0.25, fontFace: 'Aptos', fontSize: 8, color: '64748B' } } },
    { text: { text: 'Febnawan Fatur Rochman', options: { x: 9.5, y: 7.02, w: 3.0, h: 0.25, fontFace: 'Aptos', fontSize: 8, color: '64748B', align: 'right' } } },
  ],
  slideNumber: { x: 12.55, y: 7.02, color: '64748B' },
});

const C = {
  navy: '1E2761',
  teal: '028090',
  mint: '02C39A',
  ice: 'CADCFC',
  white: 'FFFFFF',
  dark: '0F172A',
  muted: '475569',
  gray: 'E2E8F0',
  pale: 'F8FAFC',
  amber: 'F59E0B',
};

function title(slide, text) {
  slide.addText(text, { x: 0.55, y: 0.35, w: 12.1, h: 0.5, fontSize: 28, bold: true, color: C.dark, margin: 0 });
}
function subtitle(slide, text) {
  slide.addText(text, { x: 0.57, y: 0.9, w: 11.5, h: 0.35, fontSize: 12, color: C.muted, margin: 0 });
}
function card(slide, x, y, w, h, heading, body, color=C.white) {
  slide.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color }, line: { color: C.gray, width: 1 } });
  slide.addText(heading, { x: x+0.2, y: y+0.18, w: w-0.4, h: 0.28, fontSize: 13, bold: true, color: C.navy, margin: 0 });
  slide.addText(body, { x: x+0.2, y: y+0.55, w: w-0.4, h: h-0.65, fontSize: 10.5, color: C.dark, margin: 0.02, breakLine: false, fit: 'shrink' });
}
function bulletList(slide, items, x, y, w, h, size=13) {
  const runs = [];
  for (const item of items) runs.push({ text: item, options: { bullet: { indent: 12 }, hanging: 4, breakLine: true } });
  slide.addText(runs, { x, y, w, h, fontSize: size, color: C.dark, margin: 0.03, fit: 'shrink' });
}
function pill(slide, x, y, text, fill=C.teal) {
  slide.addShape(pptx.ShapeType.roundRect, { x, y, w: 1.55, h: 0.42, rectRadius: 0.12, fill: { color: fill }, line: { color: fill } });
  slide.addText(text, { x, y: y+0.08, w: 1.55, h: 0.22, align: 'center', fontSize: 9, color: C.white, bold: true, margin: 0 });
}

// 1 title
let s = pptx.addSlide();
s.background = { color: C.navy };
s.addShape(pptx.ShapeType.arc, { x: 9.2, y: -0.8, w: 4.2, h: 4.2, line: { color: C.mint, transparency: 20, width: 3 } });
s.addShape(pptx.ShapeType.arc, { x: -1.0, y: 4.7, w: 3.0, h: 3.0, line: { color: C.ice, transparency: 30, width: 2 } });
s.addText('Study Case', { x: 0.8, y: 1.1, w: 3, h: 0.35, color: C.mint, bold: true, fontSize: 16, margin: 0 });
s.addText('Sistem Rekomendasi Game\nBerdasarkan Preferensi dan Mood\nMenggunakan Ontologi', { x: 0.75, y: 1.6, w: 11.3, h: 1.75, color: C.white, bold: true, fontSize: 31, margin: 0, breakLine: false, fit: 'shrink' });
s.addText('Representasi Pengetahuan dan Penalaran', { x: 0.8, y: 4.05, w: 8.0, h: 0.38, color: C.ice, fontSize: 17, margin: 0 });
s.addText('Febnawan Fatur Rochman • NPM 237006029 • Informatika A FT UNSIL', { x: 0.8, y: 5.0, w: 8.8, h: 0.35, color: C.white, fontSize: 12, margin: 0 });
pill(s, 0.8, 5.65, 'Protégé', C.teal); pill(s, 2.55, 5.65, 'OWL/RDF', C.mint); pill(s, 4.30, 5.65, 'Methontology', C.amber);

// 2 Agenda
s = pptx.addSlide('CONTENT'); title(s, 'Agenda Tugas Besar'); subtitle(s, 'Poin a–f diterjemahkan menjadi slide, ontology, aplikasi, dan video tutorial.');
[['a', 'Unduh & instalasi tools'], ['b', 'Lingkungan kerja Protégé'], ['c', 'Persoalan kasus'], ['d', 'Solusi ontologi'], ['e', 'Penerapan di tools'], ['f', 'Demo aplikasi']].forEach((it, i) => {
  const x = 0.7 + (i%3)*4.1, y = 1.55 + Math.floor(i/3)*2.0;
  card(s, x, y, 3.55, 1.25, `Poin ${it[0]}`, it[1], i%2? 'F1F5F9':'FFFFFF');
});

// 3 install
s = pptx.addSlide('CONTENT'); title(s, 'a. Cara Unduh dan Instalasi Tools'); subtitle(s, 'Tool utama adalah Protégé Desktop untuk membangun ontology OWL.');
card(s, 0.65, 1.45, 3.6, 3.8, '1. Download', 'Buka protege.stanford.edu/software lalu pilih Download for Desktop. Versi desktop mendukung OWL 2 dan reasoner.', 'FFFFFF');
card(s, 4.75, 1.45, 3.6, 3.8, '2. Install', 'Pilih installer sesuai OS. Paket platform-specific lebih mudah karena biasanya sudah menyertakan kebutuhan runtime.', 'FFFFFF');
card(s, 8.85, 1.45, 3.6, 3.8, '3. Jalankan', 'Buka Protégé, buat ontology baru, simpan sebagai .owl, lalu aktifkan reasoner seperti HermiT.', 'FFFFFF');
s.addText('Sumber: Protégé Stanford Software & Protégé 5 Documentation', { x: 0.65, y: 5.8, w: 11.8, h: 0.35, fontSize: 10, color: C.muted, italic: true });

// 4 environment
s = pptx.addSlide('CONTENT'); title(s, 'b. Pengenalan Lingkungan Kerja Protégé'); subtitle(s, 'Entities tab menjadi area utama untuk membangun kelas, properti, dan individu.');
card(s, 0.6, 1.35, 2.8, 1.45, 'Active Ontology', 'Metadata, imports, annotations, dan metrics ontology.');
card(s, 3.65, 1.35, 2.8, 1.45, 'Classes', 'Konsep domain: Game, Mood, Genre, Platform.');
card(s, 6.7, 1.35, 2.8, 1.45, 'Properties', 'Relasi: hasGenre, availableOn, suitableForMood.');
card(s, 9.75, 1.35, 2.8, 1.45, 'Individuals', 'Instance nyata: StardewValley, Valorant, Santai.');
card(s, 2.05, 3.35, 3.9, 1.35, 'Reasoner', 'HermiT/Pellet mengecek konsistensi dan menghasilkan inferred knowledge.');
card(s, 7.25, 3.35, 3.9, 1.35, 'DL Query / Search', 'Menguji ontology melalui query dan pencarian entity.');

// 5 problem
s = pptx.addSlide('CONTENT'); title(s, 'c. Deskripsi Persoalan Kasus'); subtitle(s, 'Pengguna sering bingung memilih game karena mood dan preferensi berubah-ubah.');
bulletList(s, [
  'Pilihan game sangat banyak dan tersebar di berbagai platform.',
  'Rekomendasi umum sering tidak mempertimbangkan mood pengguna.',
  'Preferensi seperti genre, mode, durasi, dan difficulty mempengaruhi kecocokan game.',
  'Diperlukan sistem berbasis pengetahuan yang bisa menjelaskan alasan rekomendasi.'
], 0.8, 1.45, 6.0, 3.7, 14);
card(s, 7.2, 1.55, 4.7, 3.35, 'Contoh situasi', 'User sedang stres, hanya ingin bermain santai, punya PC, menyukai game casual/simulation, dan tidak ingin game yang terlalu sulit.');

// 6 solution
s = pptx.addSlide('CONTENT'); title(s, 'd. Deskripsi Solusi Penyelesaian Kasus'); subtitle(s, 'Solusi: ontology + rule-based reasoning yang transparan.');
card(s, 0.6, 1.35, 3.0, 3.8, 'Representasi', 'Mood, genre, platform, mode, difficulty, duration, dan game dimodelkan sebagai kelas/individu.');
card(s, 4.05, 1.35, 3.0, 3.8, 'Relasi', 'Object properties menghubungkan game dengan genre, mood, platform, dan preferensi.');
card(s, 7.5, 1.35, 3.0, 3.8, 'Reasoning', 'Sistem memberi skor kecocokan dan menampilkan alasan rekomendasi.');
s.addShape(pptx.ShapeType.rightArrow, { x: 3.55, y: 2.85, w: 0.45, h: 0.35, fill: { color: C.teal }, line: { color: C.teal } });
s.addShape(pptx.ShapeType.rightArrow, { x: 7.05, y: 2.85, w: 0.45, h: 0.35, fill: { color: C.teal }, line: { color: C.teal } });

// 7 Methontology
s = pptx.addSlide('CONTENT'); title(s, 'Kerangka Methontology'); subtitle(s, 'Tahapan pengembangan ontology dibuat eksplisit agar sesuai instruksi tugas.');
const steps = ['Specification', 'Knowledge Acquisition', 'Conceptualization', 'Formalization', 'Implementation', 'Evaluation', 'Documentation'];
steps.forEach((step, i) => {
  const x = 0.65 + (i%4)*3.05, y = 1.45 + Math.floor(i/4)*1.85;
  card(s, x, y, 2.55, 1.15, `${i+1}. ${step}`, ['Tujuan & scope', 'Sumber pengetahuan', 'Kelas/relasi', 'Model formal', 'Protégé/OWL', 'Uji hasil', 'Slide/video'][i]);
});

// 8 ontology classes
s = pptx.addSlide('CONTENT'); title(s, 'e. Penerapan Kasus: Struktur Ontologi'); subtitle(s, 'Kelas utama dan relasi yang dibuat pada Protégé.');
card(s, 0.65, 1.35, 4.0, 4.3, 'Kelas utama', 'Game\nGenre\nMood\nPlatform\nPlayMode\nDifficulty\nDuration\nPlayerPreference\nRecommendation');
card(s, 5.0, 1.35, 6.7, 4.3, 'Object properties', 'hasGenre: Game → Genre\navailableOn: Game → Platform\nhasPlayMode: Game → PlayMode\nhasDifficulty: Game → Difficulty\nhasDuration: Game → Duration\nsuitableForMood: Game → Mood\nmatchesPreference: Game → PlayerPreference');

// 9 examples
s = pptx.addSlide('CONTENT'); title(s, 'Contoh Individu dan Aturan Rekomendasi'); subtitle(s, 'Knowledge base berisi contoh game dan alasan kecocokan.');
card(s, 0.6, 1.25, 3.0, 3.9, 'Stardew Valley', 'Genre: Simulation, Casual\nMood: Santai, Stres\nPlatform: PC, Console, Mobile\nDifficulty: Mudah');
card(s, 3.9, 1.25, 3.0, 3.9, 'Valorant', 'Genre: FPS\nMood: Kompetitif, Sosial\nPlatform: PC\nMode: Multiplayer\nDifficulty: Sulit');
card(s, 7.2, 1.25, 4.6, 3.9, 'Contoh rule', 'Jika mood = Stres, prioritaskan game yang mudah, santai, dan single-player.\nJika mood = Kompetitif, prioritaskan multiplayer dan difficulty sedang/sulit.');

// 10 demo app
s = pptx.addSlide('CONTENT'); title(s, 'f. Demo Aplikasi'); subtitle(s, 'Aplikasi Streamlit menerima input dan menghasilkan rekomendasi beserta alasan.');
card(s, 0.65, 1.35, 3.5, 3.9, 'Input', 'Mood\nGenre favorit\nPlatform\nMode bermain\nDurasi\nDifficulty');
card(s, 4.85, 1.35, 3.5, 3.9, 'Reasoning', 'Sistem memberi skor pada game yang cocok dengan mood dan preferensi.');
card(s, 9.05, 1.35, 3.0, 3.9, 'Output', 'Daftar game\nSkor kecocokan\nAlasan rekomendasi');
s.addText('Command: streamlit run app/main.py', { x: 0.75, y: 5.65, w: 6.0, h: 0.35, fontFace: 'Consolas', fontSize: 12, color: C.navy });

// 11 demo scenario
s = pptx.addSlide('CONTENT'); title(s, 'Skenario Demo'); subtitle(s, 'Contoh input dan output yang akan ditunjukkan pada video tutorial.');
card(s, 0.75, 1.35, 5.1, 3.6, 'Input user', 'Mood: Stres\nGenre: Casual\nPlatform: PC\nMode: SinglePlayer\nDurasi: Sedang\nDifficulty: Mudah');
card(s, 6.4, 1.35, 5.1, 3.6, 'Output rekomendasi', 'Stardew Valley\nAlasan: cocok untuk mood stres, genre casual, tersedia di PC, mendukung single-player, dan difficulty mudah.');

// 12 closing
s = pptx.addSlide(); s.background = { color: C.navy };
s.addText('Kesimpulan', { x: 0.8, y: 0.9, w: 8.0, h: 0.6, color: C.white, bold: true, fontSize: 34, margin: 0 });
bulletList(s, [
  'Ontologi membuat pengetahuan rekomendasi game lebih terstruktur.',
  'Protégé digunakan untuk memodelkan kelas, properti, dan individu.',
  'Methontology memberi tahapan sistematis dari specification sampai documentation.',
  'Demo aplikasi menunjukkan rekomendasi yang dapat dijelaskan.'
], 0.95, 2.0, 9.6, 2.8, 15);
s.addText('Terima kasih', { x: 0.95, y: 5.6, w: 4.0, h: 0.4, color: C.mint, fontSize: 20, bold: true, margin: 0 });

pptx.writeFile({ fileName: 'slides/rpp-game-ontology-presentation.pptx' });
