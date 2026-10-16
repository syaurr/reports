# Dokumentasi Lengkap Repositori Reports

Dokumentasi ini memetakan seluruh berkas, struktur teknis, konteks bisnis, serta temuan inkonsistensi yang ada di repositori reports per Oktober 2026.

## Ringkasan Proyek

Repositori ini berfungsi sebagai repositori laporan operasional Human Resources (HR) dan Executive Personal Assistant (Executive PA) untuk PT Altri / Balista Sushi & Tea. Mayoritas berkas disusun sebagai dashboard berbasis web statis interaktif dan presentasi slide web untuk pelaporan berkala ke tingkat pimpinan (seperti HRVP dan jajaran direksi). Selain laporan internal Balista, repositori ini memuat berkas analisis kelayakan bisnis F&B serta analisis kebutuhan sistem instansi eksternal.

## Arsitektur Teknis

Sebagian besar antarmuka dibangun menggunakan kombinasi HTML5, CSS kustom, Tailwind CSS via CDN, pustaka grafik Chart.js, serta animasi AOS (Animate On Scroll). Tiap modul laporan didesain mandiri (standalone HTML) sehingga dapat dibuka langsung di peramban tanpa memerlukan runtime backend atau bundler Node.js.

Satu skrip otomatisasi berbasis Python disediakan untuk menghasilkan laporan statis terstruktur melalui template string.

## Katalog dan Analisis Berkas

### 1. Dashboard Utama dan Aset Web

#### index.html
Halaman beranda utama yang bertindak sebagai hub navigasi laporan bulanan dan dokumen khusus. Menggunakan tata letak Bento Grid dengan palet warna pastel dan neon. Halaman ini menghubungkan navigasi ke berkas laporan bulanan lokal maupun tautan presentasi eksternal berbasis Canva.

#### style.css
Lembar gaya utama pendukung index.html. Mengatur variabel CSS warna (pink, orange, green, neon-green, red, purple), efek glassmorphism dengan backdrop filter, animasi blob latar belakang, tata letak grid responsif, serta styling gelembung mengapung.

#### script.js
Skrip JavaScript murni untuk index.html. Berfungsi merender 15 elemen gelembung acak pada DOM dengan variasi warna pastel, ukuran, posisi horizontal, serta durasi animasi naik melintasi layar.

### 2. Modul Analisis Khusus

#### bpjs.html
Dashboard analitis terinci berjudul Analisa Kelayakan BPJS Kesehatan 2026 Balista Sushi & Tea. Mengevaluasi data kepesertaan 139 tenaga kerja di 14 outlet Jawa Barat berdasarkan batas probasi 3 bulan merujuk PP Nomor 35 Tahun 2021 dan baseline UMK 2026. Dilengkapi kartu metrik eksekutif, filter outlet, simulasi beban kas terhadap ketentuan upah minimum EDABU, serta tinjauan kepatuhan UU Nomor 24 Tahun 2011 dan PP Nomor 86 Tahun 2013.

#### kopriw.html
Dokumen kajian strategis pasar berjudul Kopriagan goes to Bandoeng. Menganalisis perbandingan model operasional kedai kopi tradisional (tiam) versus penerapan mesin espresso modern di Bandung. Membedah persepsi konsumen kopi susu aren, hambatan operasional saat jam sibuk, pergeseran variasi menu, serta risiko diferensiasi pasar.

#### apa ini.html
Laporan Analisis Kebutuhan Sistem modernisasi ERP dan ekosistem mobile untuk klien Perumda Air Minum Tirta Ampera (PDAM Boyolali) tertanggal 9 Maret 2026. Disusun dalam format cetak A4. Membahas kendala aplikasi desktop lama yang terkunci source code-nya, proses pencatatan meteran manual, penyusunan payroll via Excel, kapasitas SDM, dan rancangan arsitektur Web ERP serta tiga aplikasi Android. Berkas ini merupakan artefak rekayasa perangkat lunak mandiri yang terpisah dari ekosistem operasional Balista.

### 3. Laporan Kinerja Bulanan Executive PA (2026)

#### agt26.html
Presentasi slide interaktif berbasis web untuk EXPA Monthly Report Agustus 2026. Menggunakan transisi layar penuh dengan navigasi keyboard panah kiri kanan dan progress dot. Memuat metrik kontrak baru (6 crew), resignasi (6 crew), perekrutan baru (7 crew), sisa pinjaman kasbon (Rp19.750.000), serta analisis kepatuhan administrasi.

#### juli26.html
Laporan Kinerja Executive PA periode Juli 2026 yang ditujukan kepada HRVP. Memiliki styling modern dengan Poppins dan JetBrains Mono, integrasi Chart.js serta plugin ChartDataLabels. Menyajikan evaluasi mendalam performa personalia, efisiensi rekrutmen, dan pemantauan arus operasional.

#### juni26.html
Laporan Kinerja EPA periode Juni 2026 dengan palet warna krem, merah, dan emas. Dilengkapi bilah navigasi lengket (sticky) yang membagi tinjauan menjadi delapan bab operasional yaitu Ringkasan, Dokumen, Rekrutmen, Payroll, Proyek, Investor, Sistem, dan Absensi.

#### mei26.html
Laporan Executive Report Mei Balista yang mengusung tema estetika Y2K dengan neo-brutalist border tegas, bayangan jatuh kaku, aksen stiker animasi mengambang, serta integrasi pustaka AOS dan Chart.js.

#### apr26.html
Laporan April Report EXPA yang mengadaptasi palet warna Google (biru, merah, kuning, hijau). Memuat visualisasi mendalam terkait corong sourcing kandidat, onboarding karyawan baru, kepatuhan dokumen SP dan paklaring, penyelesaian kendala crew lapangan, komparasi gaji, hingga penilaian kinerja berkala.

#### mar26.html
Dashboard bertab eksekutif untuk laporan periode Maret hingga April 2026. Memuat visualisasi funnel rekrutmen, kalkulator biaya kekosongan posisi (Cost of Vacancy), evaluasi ketegangan budaya kerja berbasis Adams Equity Theory dan nepotisme, lonjakan pengajuan pinjaman kasbon, serta radar kesiapan operasional gerai baru Kota Baru Parahyangan (KBP).

#### jan26.html
Laporan HR Update Februari 2026 dengan pendekatan visual Neo-Brutalisme ceria berlatar titik-titik (dotted pattern) dan tipografi Poppins tebal.

### 4. Laporan Historis dan Arsip (2025)

#### nov.html
Laporan operasional bertema visual pink dan ungu bertajuk November Executive PA Time. Berfokus pada akurasi data personalia (pencapaian 97%), arsip digital SOP di Google Drive dan Canva (100%), persiapan pembukaan gerai Pajajaran per 28 Desember, penertiban dokumen paklaring, serta administrasi slip gaji.

#### sept.html
Laporan bertajuk september s nya apa dengan konsep visual retro piksel 8-bit dan scrapbook gelap memanfaatkan font VT323 dan Press Start 2P.

#### agt.html
Laporan Kinerja HR-PA periode Juli hingga Agustus 2025. Bertindak sebagai baseline perbandingan kinerja operasional satu tahun sebelum periode 2026.

### 5. Skrip dan Utilitas Otomatisasi

#### laporan.py
Skrip Python yang menyusun dokumen HTML mandiri berjudul HR_Strategic_Report_2026.html. Memuat template visual lengkap dengan kartu metrik dan integrasi Chart.js untuk membandingkan nominal pengajuan versus persetujuan kasbon antara bulan Maret dan April.

### 6. Berkas Konfigurasi dan Panduan Agen

#### GEMINI.md dan AGENTS.md
Berkas aturan tata kelola agen AI pada lingkungan Antigravity. Mengatur batasan gaya bahasa, ketentuan verifikasi klaim, alur vibe coding bertahap, serta memori preferensi pengguna.

#### .gitattributes
Pengaturan Git untuk normalisasi akhir baris otomatis (LF conversion) pada berkas teks.

#### .vscode/
Direktori konfigurasi editor Visual Studio Code tingkat workspace.

## Temuan dan Evaluasi Kritis

Pemeriksaan mendalam terhadap repositori menemukan beberapa catatan inkonsistensi berikut ini.

Tautan berkas pada index.html baris 33 mengarah ke BPJS.html dengan huruf kapital, sedangkan berkas aktual bernama bpjs.html dengan huruf kecil. Pada sistem berkas Windows ini tetap terbaca, namun akan menghasilkan galat 404 jika diunggah ke server hosting Linux.

Kartu Jan-Feb 2026 pada index.html baris 63 diarahkan ke nov.html, sementara berkas laporan awal tahun yang tersedia adalah jan26.html. Hal ini menyebabkan duplikasi karena kartu Okt-Nov juga mengarah ke nov.html.

Berkas apa ini.html merupakan dokumen spesifikasi teknis untuk PDAM Boyolali, berbeda sektor bisnis dengan seluruh berkas lain yang berpusat pada operasional F&B PT Altri dan Balista Sushi & Tea.

Skrip laporan.py belum dieksekusi ulang di repositori sehingga berkas hasil kompilasinya (HR_Strategic_Report_2026.html) belum berwujud di dalam direktori.
