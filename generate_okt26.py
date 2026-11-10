# -*- coding: utf-8 -*-
import json
import re

# Read data-mentah directly to parse attendance_data
with open('d:/reports/data-mentah-2026-10.md', encoding='utf-8') as f:
    raw_md = f.read()

# Parse attendance data directly from markdown
part = raw_md.split('Nama\tOutlet\tH\tS\tI\tA\tOFF\tC\tHT\t(-)')[1]
part = part.split('HADIR\t: H')[0].strip()

pattern = re.compile(r'(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)\t+(\d+)')
matches = list(pattern.finditer(part))

attendance_data = []
last_end = 0
for m in matches:
    start = m.start()
    prefix = part[last_end:start].strip()
    prefix_parts = [p.strip() for p in prefix.split('\t') if p.strip()]
    name = prefix_parts[0] if len(prefix_parts) > 0 else 'Unknown'
    outlet = prefix_parts[1] if len(prefix_parts) > 1 else 'Unknown'
    vals = [int(x) for x in m.groups()]
    attendance_data.append({
        'name': name,
        'outlet': outlet,
        'h': vals[0], 's': vals[1], 'i': vals[2], 'a': vals[3],
        'off': vals[4], 'c': vals[5], 'ht': vals[6], 'min': vals[7]
    })
    last_end = m.end()

kasbon_data = [
    {"name": "Pitria Humaira", "outlet": "Ambon", "acc": 500000, "pot_acc": 250000, "sisa": 250000, "ajukan": 250000},
    {"name": "Ridho Saefuloh", "outlet": "Ambon", "acc": 1000000, "pot_acc": 500000, "sisa": 500000, "ajukan": 500000},
    {"name": "Dina Apriani", "outlet": "Ambon", "acc": 500000, "pot_acc": 250000, "sisa": 250000, "ajukan": 250000},
    {"name": "RAHMADANI", "outlet": "Ambon", "acc": 500000, "pot_acc": 350000, "sisa": 150000, "ajukan": 350000},
    {"name": "Agung minargo", "outlet": "Ambon", "acc": 600000, "pot_acc": 300000, "sisa": 300000, "ajukan": 300000},
    {"name": "Regi Ardiansah", "outlet": "Cimahi Amir", "acc": 300000, "pot_acc": 300000, "sisa": 0, "ajukan": 500000},
    {"name": "Ira Farika", "outlet": "Tubagus Ismail", "acc": 250000, "pot_acc": 350000, "sisa": 150000, "ajukan": 250000},
    {"name": "Wina fitria", "outlet": "Tubagus Ismail", "acc": 700000, "pot_acc": 350000, "sisa": 350000, "ajukan": 350000},
    {"name": "Fajar Febbi Aldianto", "outlet": "Pajajaran", "acc": 1500000, "pot_acc": 1500000, "sisa": 0, "ajukan": 1500000},
    {"name": "MUHAMMAD KALBADRI", "outlet": "Garut", "acc": 750000, "pot_acc": 750000, "sisa": 0, "ajukan": 1000000},
    {"name": "Rulian Rizki Rahadiansyah", "outlet": "Pajajaran", "acc": 750000, "pot_acc": 600000, "sisa": 300000, "ajukan": 1000000},
    {"name": "Jihan sintani", "outlet": "Pajajaran", "acc": 200000, "pot_acc": 300000, "sisa": 150000, "ajukan": 150000},
    {"name": "Dea amalia", "outlet": "Pajajaran", "acc": 200000, "pot_acc": 300000, "sisa": 150000, "ajukan": 250000},
    {"name": "Dwyzha Ramadhany Septian", "outlet": "Setrasari", "acc": 3000000, "pot_acc": 500000, "sisa": 2500000, "ajukan": 500000},
    {"name": "Ferry putra yatama", "outlet": "Kota Baru Parahyangan", "acc": 500000, "pot_acc": 500000, "sisa": 0, "ajukan": 500000},
    {"name": "NABILAH MAHARANI", "outlet": "Kiaracondong", "acc": 200000, "pot_acc": 200000, "sisa": 0, "ajukan": 200000},
    {"name": "bayu permana sidik", "outlet": "Garut", "acc": 300000, "pot_acc": 200000, "sisa": 200000, "ajukan": 300000},
    {"name": "Indra sukmawandi", "outlet": "Ujung Berung", "acc": 300000, "pot_acc": 300000, "sisa": 200000, "ajukan": 200000},
    {"name": "Yuliani", "outlet": "Kiaracondong", "acc": 1000000, "pot_acc": 500000, "sisa": 500000, "ajukan": 500000},
    {"name": "Adi Dwi sukmaprawira", "outlet": "Kiaracondong", "acc": 200000, "pot_acc": 200000, "sisa": 0, "ajukan": 500000},
    {"name": "Alfya Putri Melsya", "outlet": "Pajajaran", "acc": 250000, "pot_acc": 600000, "sisa": 900000, "ajukan": 500000},
    {"name": "Dede Supriatna (Rangga)", "outlet": "Setrasari", "acc": 4000000, "pot_acc": 500000, "sisa": 3500000, "ajukan": 0},
    {"name": "Hardi Sugara", "outlet": "Garut", "acc": 1000000, "pot_acc": 350000, "sisa": 1800000, "ajukan": 300000}
]

daily_worker_data = [
    {"tanggal": "15 Oktober 2026", "nama": "Teuku Rayfa", "outlet": "Pajajaran", "nominal": 150000},
    {"tanggal": "15 Oktober 2026", "nama": "Fadila Lupiana", "outlet": "Garut", "nominal": 375000},
    {"tanggal": "15 Oktober 2026", "nama": "Zulfa Zahrotul Ula", "outlet": "Garut", "nominal": 75000},
    {"tanggal": "31 Oktober 2026", "nama": "Teuku Rayfa", "outlet": "Pajajaran", "nominal": 150000},
    {"tanggal": "31 Oktober 2026", "nama": "Erick Saputra", "outlet": "Garut", "nominal": 75000},
    {"tanggal": "31 Oktober 2026", "nama": "Zulfa Zahrotul Ula", "outlet": "Garut", "nominal": 375000}
]

surat_sakit_data = [
    {"nama": "Ira Farika", "nominal": 50000, "ket": "SAKIT 1"},
    {"nama": "Rulian Rizki Rahadiansyah", "nominal": 100000, "ket": "SAKIT 2"},
    {"nama": "Purwanti ayu rahayu", "nominal": 50000, "ket": "SAKIT 1 IZIN 1"},
    {"nama": "Adi Dwi sukmaprawira", "nominal": 50000, "ket": "SAKIT 1"},
    {"nama": "Muhammad Rangga Fauzy", "nominal": 475000, "ket": "SAKIT 16"},
    {"nama": "Dimas Ramdani", "nominal": 55000, "ket": "SAKIT 2 IZIN 2 ALPA 1"},
    {"nama": "Jaenal arif", "nominal": 75000, "ket": "SAKIT 3"},
    {"nama": "Rachel April Riadi", "nominal": 75000, "ket": "SAKIT 2"},
    {"nama": "Wiyanka adi syahran", "nominal": 75000, "ket": "SAKIT 2"},
    {"nama": "Wina Fitria", "nominal": 100000, "ket": "SAKIT 3"},
    {"nama": "Luis apriadi nur ilham", "nominal": 100000, "ket": "SAKIT 3 IZIN 1"},
    {"nama": "Silvia Febriani", "nominal": 50000, "ket": "SAKIT 1 IZIN 4"},
    {"nama": "M Farhan fauzi", "nominal": 75000, "ket": "SAKIT 2 IZIN 1"},
    {"nama": "Salma Siti Nurhanifah", "nominal": 325000, "ket": "SAKIT 9 ALPA 2"},
    {"nama": "Bilal akbar", "nominal": 75000, "ket": "SAKIT 2 IZIN 1"},
    {"nama": "Agung minargo", "nominal": 50000, "ket": "SAKIT 2"},
    {"nama": "AGIL SAPUTRA", "nominal": 150000, "ket": "SAKIT 7 IZIN 1"},
    {"nama": "widya shelby", "nominal": 75000, "ket": "SAKIT 1 IZIN 1"},
    {"nama": "Raihan muhammad rizki", "nominal": 50000, "ket": "SAKIT 1 IZIN 3"}
]

eval_leader_criteria = [
    {"label": "Komunikasi tegas sopan", "score": 3.83},
    {"label": "Bebas arogansi toksik", "score": 4.17},
    {"label": "Objektif tanpa nepotisme", "score": 3.75},
    {"label": "Teladan SOP dan grooming", "score": 3.75},
    {"label": "Lingkungan kerja aman", "score": 3.75},
    {"label": "Jadwal shift adil", "score": 4.25},
    {"label": "Pengawasan kedisiplinan", "score": 3.50},
    {"label": "Turun tangan operasional", "score": 3.83},
    {"label": "Tanggap perbaikan fasilitas", "score": 4.17},
    {"label": "Briefing mingguan SOP", "score": 3.25}
]

eval_leader_feedback = [
    {
        "nama": "Dimas Ramdani",
        "kelebihan": "Baik",
        "kekurangan": "Komunikasi",
        "layak": "Ya",
        "saran": "Komunikasi nya lebih di tingkatkan"
    },
    {
        "nama": "Nadira Nur Aprilia",
        "kelebihan": "Leader mulai rutin mengadakan briefing atau ruang diskusi, rutin mengadakan general cleaning demi kebersihan dan kenyamanan area kitchen maupun dine in, cukup baik dalam mengingatkan dan menerapkan SOP mulai dari proses pembuatan, kedisiplinan crew, area pelayanan, dan cara menangani komplain. Dalam 3 bulan ini leader sudah menunjukkan progress yang baik dalam mengurangi komplainan pelanggan",
        "kekurangan": "Leader kurang tegas saat menegur crew yang melanggar SOP",
        "layak": "Tidak sepenuhnya layak karena dari cara memimpin kurang tegas",
        "saran": "Harus lebih tegas jangan masih nggak enakan untuk menegur crew yang memang melakukan kesalahan, dan semoga makin bisa terbuka merangkul antar crew agar menciptakan lingkungan kerja nyaman"
    },
    {
        "nama": "Irania Aulia Putri Ilhami",
        "kelebihan": "Bekerja selalu sesuai SOP, berkurangnya komplain, kebersihan dan perbaikan outlet lebih baik dari sebelumnya walaupun belum sempurna. Mampu mendengarkan keluhan semua crew dan mencari jalan keluarnya dengan yang bersangkutan",
        "kekurangan": "Merespon crew yang izin via WhatsApp, kalau bisa dibalas juga, jangan cuma di-read agar jelas dikasih izin atau tidak",
        "layak": "Buat di outlet Buah Batu saja jangan di Garut",
        "saran": "Tetap pertahankan penanganan komplain dan perbaiki komunikasi izin digital"
    },
    {
        "nama": "Permana Abdul Roup",
        "kelebihan": "Sopan kepada crew",
        "kekurangan": "Power leadership dan ketegasan",
        "layak": "Masih perlu masa percobaan",
        "saran": "Training leader agar lebih terkoordinasi"
    },
    {
        "nama": "Ari Rizki",
        "kelebihan": "Hadir tepat waktu dan sigap saat ada perbaikan fisik",
        "kekurangan": "Perlu peningkatan inisiatif",
        "layak": "Tidak",
        "saran": "Tingkatkan koordinasi shift harian"
    },
    {
        "nama": "Responden 6",
        "kelebihan": "Disiplin waktu",
        "kekurangan": "Dalam hal briefing ditingkatkan lagi, kebersihan sama dan tetap enjoy jangan sensitif ke kerjaan ketika ada masalah di luar",
        "layak": "Cocok tergantung leader itu sendiri",
        "saran": "Briefing rutin tiap minggu untuk menjaga kekompakan"
    },
    {
        "nama": "Responden 7",
        "kelebihan": "Saat ada barang outlet rusak atau butuh perbaikan sigap memperbaiki, jadwal berjalan kondusif",
        "kekurangan": "Jadwal shift ada yang libur 2 orang sekaligus, bahan crunchy kadang kurang terkontrol preparasinya sehingga memicu waste",
        "layak": "Tidak sepenuhnya layak",
        "saran": "Pelatihan kalibrasi pembuatan menu sushi agar kualitas tetap seragam"
    },
    {
        "nama": "Responden 8",
        "kelebihan": "Hadir tepat waktu, bisa menjadi leader yang lebih mendengarkan saran bersama",
        "kekurangan": "Komunikasi dan ketegasan penegakan SOP",
        "layak": "Tidak",
        "saran": "Untuk manajemen tolong perjelas detail tugas perbantuan ke outlet lain agar instruksi tidak tumpang tindih"
    },
    {
        "nama": "Responden 9",
        "kelebihan": "Bertanggung jawab, netral ke semua crew, kinerja bagus terus tingkatkan",
        "kekurangan": "Penyusunan jadwal dan SOP pendampingan training crew baru",
        "layak": "Belum bisa berpendapat untuk Garut, lebih cocok di Buah Batu",
        "saran": "Manajemen lebih kompak dalam membagikan informasi promo ke crew terutama tim Instagram"
    },
    {
        "nama": "Responden 10",
        "kelebihan": "Jadwal teratur, tegas terhadap crew, melakukan briefing, menjalankan tugas leader dengan baik",
        "kekurangan": "Bisa lebih tegas dan merangkul tidak memilih crew",
        "layak": "Bagus, baik, harus lebih tegas",
        "saran": "Info promosi KOL segera dibagikan lewat grup cabang sebelum aktif"
    },
    {
        "nama": "Responden 11",
        "kelebihan": "Tidak memihak siapapun dan mampu mengalah apabila ada backup",
        "kekurangan": "Kurang responsif saat tidak ada shift middle",
        "layak": "Di Buah Batu saja",
        "saran": "Jaga konsistensi operasional"
    },
    {
        "nama": "Responden 12",
        "kelebihan": "Suka membantu di saat crew dapur kekurangan orang",
        "kekurangan": "Inisiatif saat preparasi bahan",
        "layak": "Layak",
        "saran": "Pertahankan kerja sama dan kekompakan tim dapur"
    }
]

# Outlet attendance summary
outlet_summary = {}
for r in attendance_data:
    o = r['outlet']
    if o not in outlet_summary:
        outlet_summary[o] = {'crew': 0, 'h': 0, 's': 0, 'i': 0, 'a': 0, 'ht': 0}
    outlet_summary[o]['crew'] += 1
    outlet_summary[o]['h'] += r['h']
    outlet_summary[o]['s'] += r['s']
    outlet_summary[o]['i'] += r['i']
    outlet_summary[o]['a'] += r['a']
    outlet_summary[o]['ht'] += r['ht']

outlets_sorted = sorted(list(outlet_summary.keys()))

# Pre-format Kasbon totals
total_kasbon_acc = sum(k['acc'] for k in kasbon_data)
total_kasbon_pot_acc = sum(k['pot_acc'] for k in kasbon_data)
total_kasbon_sisa_23 = sum(k['sisa'] for k in kasbon_data)

kasbon_acc_formatted = f"{total_kasbon_acc:,}".replace(",", ".")
kasbon_pot_formatted = f"{total_kasbon_pot_acc:,}".replace(",", ".")
kasbon_sisa_formatted = f"{total_kasbon_sisa_23:,}".replace(",", ".")

# Pre-render Surat Sakit table rows (compatible with Python 3.11 and earlier)
surat_sakit_rows = []
for item in surat_sakit_data:
    nom_fmt = f"{item['nominal']:,}".replace(",", ".")
    surat_sakit_rows.append(
        f'<tr>\n'
        f'    <td class="p-3 font-medium text-[#022020]">{item["nama"]}</td>\n'
        f'    <td class="p-3 text-right font-semibold text-[#033f3f]">Rp {nom_fmt}</td>\n'
        f'    <td class="p-3"><span class="px-2 py-0.5 rounded bg-gray-100 text-gray-700 font-medium">{item["ket"]}</span></td>\n'
        f'</tr>'
    )
surat_sakit_html = "\n".join(surat_sakit_rows)

# Pre-render Attendance Outlet Filter Options
attendance_options_rows = []
for o in outlets_sorted:
    cnt = outlet_summary[o]["crew"]
    attendance_options_rows.append(f'<option value="{o}">{o} ({cnt} Crew)</option>')
attendance_options_html = "\n".join(attendance_options_rows)

# Pre-render Leader Feedback Cards
feedback_cards = []
for fb in eval_leader_feedback:
    layak_text = fb["layak"]
    layak_lower = layak_text.lower()
    if "ya" in layak_lower or "layak" in layak_lower:
        badge_cls = "bg-emerald-100 text-emerald-800"
    elif "cocok" in layak_lower or "batu" in layak_lower:
        badge_cls = "bg-amber-100 text-amber-800"
    else:
        badge_cls = "bg-red-100 text-red-800"
    
    card_html = (
        f'<div class="p-3 bg-white rounded-xl border border-gray-200 shadow-sm text-xs space-y-1.5 flex flex-col justify-between">\n'
        f'    <div>\n'
        f'        <div class="flex items-center justify-between border-b border-gray-100 pb-1">\n'
        f'            <span class="font-bold text-[#022020]">{fb["nama"]}</span>\n'
        f'            <span class="text-[10px] px-2 py-0.5 rounded-full font-bold {badge_cls}">{layak_text}</span>\n'
        f'        </div>\n'
        f'        <p class="text-gray-700 mt-1 italic leading-relaxed">"{fb["kelebihan"]}"</p>\n'
        f'        <p class="text-red-700 mt-1 text-[11px] leading-relaxed"><span class="font-semibold text-gray-600">Catatan minus:</span> {fb["kekurangan"]}</p>\n'
        f'    </div>\n'
        f'    <p class="text-gray-500 text-[10px] pt-1 border-t border-gray-100 font-medium">Saran: {fb["saran"]}</p>\n'
        f'</div>'
    )
    feedback_cards.append(card_html)
leader_feedback_html = "\n".join(feedback_cards)

# Pre-serialize JSON objects
kasbon_json = json.dumps(kasbon_data)
attendance_json = json.dumps(attendance_data)
eval_criteria_json = json.dumps(eval_leader_criteria)
outlets_sorted_json = json.dumps(outlets_sorted)
outlet_summary_json = json.dumps(outlet_summary)

# Main HTML template - simple variable interpolations without inner nested f-strings

# 4-Month Comparison Section HTML with Interactive Carousel Slider (Juli, Agustus, September, Oktober 2026)
comparison_section_html = """
        <!-- KOMPARASI HISTORIS 4 BULAN (JULI - OKTOBER 2026) -->
        <section id="komparasi" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Komparasi Historis 4 Bulan</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Tren Kinerja dan Rekapitulasi Komparatif (Juli, Agustus, September, Oktober 2026)</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Data Terverifikasi 4 Periode</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Pemantauan komparatif empat bulan berturut-turut memperlihatkan stabilitas operasional yang makin matang pada kuartal ketiga hingga awal kuartal keempat 2026. Beban belanja payroll berada di rentang Rp 370-374 juta, biaya daily worker ditekan sangat hemat ke titik terendah Rp 565.000, serta kedisiplinan absensi kru menunjukkan perbaikan nyata dengan penurunan konsisten pada angka alpa dan keterlambatan.
            </p>

            <!-- Slider Controls Bar -->
            <div class="bg-white p-4 rounded-2xl border border-[#a48d5e]/25 shadow-sm space-y-3">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                    <div class="flex items-center space-x-2">
                        <span class="text-xs font-bold text-[#022020] uppercase tracking-wider">Pilih Grafik:</span>
                        <div class="flex flex-wrap gap-1.5" id="compTabsContainer">
                            <button onclick="goToCompSlide(0)" class="comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-[#033f3f] text-[#f2d086] shadow-sm">1. Payroll &amp; THP</button>
                            <button onclick="goToCompSlide(1)" class="comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-gray-100 text-gray-700 hover:bg-[#f4e3be]">2. Kasbon &amp; DW</button>
                            <button onclick="goToCompSlide(2)" class="comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-gray-100 text-gray-700 hover:bg-[#f4e3be]">3. Turnover Kru</button>
                            <button onclick="goToCompSlide(3)" class="comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-gray-100 text-gray-700 hover:bg-[#f4e3be]">4. Kedisiplinan</button>
                        </div>
                    </div>

                    <div class="flex items-center justify-between sm:justify-end space-x-3">
                        <span id="compSlideBadge" class="text-xs font-semibold px-3 py-1 bg-[#f4e3be]/60 text-[#022020] rounded-full border border-[#a48d5e]/30">Slide 1 dari 4: Belanja Payroll &amp; THP</span>
                        <div class="flex items-center space-x-1.5">
                            <button id="btnPrevComp" onclick="prevCompSlide()" aria-label="Slide Sebelumnya" class="p-2 rounded-lg bg-[#022020] text-[#f4e3be] hover:bg-[#033f3f] hover:text-[#f2d086] transition font-bold disabled:opacity-30 disabled:cursor-not-allowed">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
                            </button>
                            <button id="btnNextComp" onclick="nextCompSlide()" aria-label="Slide Berikutnya" class="p-2 rounded-lg bg-[#022020] text-[#f4e3be] hover:bg-[#033f3f] hover:text-[#f2d086] transition font-bold disabled:opacity-30 disabled:cursor-not-allowed">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Slider Viewport -->
                <div class="relative overflow-hidden rounded-xl pt-2">
                    <!-- Left Floating Navigation Button -->
                    <button onclick="prevCompSlide()" id="floatBtnPrev" aria-label="Sebelumnya" class="hidden sm:flex absolute left-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 items-center justify-center rounded-full bg-white/95 text-[#022020] hover:bg-[#f2d086] shadow-lg border border-[#a48d5e]/30 transition disabled:opacity-20 disabled:pointer-events-none">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"></path></svg>
                    </button>
                    <!-- Right Floating Navigation Button -->
                    <button onclick="nextCompSlide()" id="floatBtnNext" aria-label="Berikutnya" class="hidden sm:flex absolute right-3 top-1/2 -translate-y-1/2 z-20 w-10 h-10 items-center justify-center rounded-full bg-white/95 text-[#022020] hover:bg-[#f2d086] shadow-lg border border-[#a48d5e]/30 transition disabled:opacity-20 disabled:pointer-events-none">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"></path></svg>
                    </button>

                    <!-- Sliding Track -->
                    <div id="compSliderTrack" class="flex transition-transform duration-500 ease-in-out" style="transform: translateX(0%);">
                        <!-- Slide 1: Payroll & THP Bersih -->
                        <div class="w-full min-w-full flex-shrink-0 px-1 sm:px-12">
                            <div class="card-custom p-6 bg-gradient-to-br from-white to-[#faf7f0] border-2 border-[#4285F4]/30 shadow-md">
                                <div class="flex items-center justify-between border-b pb-3 mb-4">
                                    <div>
                                        <div class="flex items-center space-x-2">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#4285F4]"></span>
                                            <h3 class="text-base font-bold text-[#022020]">1. Komparasi Belanja Payroll dan THP Bersih</h3>
                                        </div>
                                        <p class="text-xs text-gray-500 mt-0.5">Perbandingan total gaji kotor vs total diterima bersih kru 4 periode</p>
                                    </div>
                                    <span class="text-xs bg-blue-50 text-blue-700 font-bold px-3 py-1 rounded-full border border-blue-200">Kategori Payroll</span>
                                </div>
                                <div class="h-72 sm:h-80 w-full relative">
                                    <canvas id="chartComparePayroll"></canvas>
                                </div>
                                <div class="mt-4 bg-[#f4e3be]/35 p-4 rounded-xl border border-[#a48d5e]/25">
                                    <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                        Total pengeluaran gaji relatif stabil pada kisaran Rp 370 sampai 374 juta dalam tiga bulan terakhir dengan kenaikan tipis +0,94% di Oktober seiring penambahan kru aktif menjadi 148 orang. Nilai bersih yang diterima kru meningkat dari Rp 195,8 juta pada Juli menjadi Rp 214,89 juta pada Oktober.
                                    </p>
                                    <p class="text-[10px] text-gray-400 mt-2">Sumber rekap payroll PT Altri Juli, Agustus, September, dan Oktober 2026</p>
                                </div>
                            </div>
                        </div>

                        <!-- Slide 2: Kasbon & Daily Worker -->
                        <div class="w-full min-w-full flex-shrink-0 px-1 sm:px-12">
                            <div class="card-custom p-6 bg-gradient-to-br from-white to-[#faf7f0] border-2 border-[#FBBC05]/30 shadow-md">
                                <div class="flex items-center justify-between border-b pb-3 mb-4">
                                    <div>
                                        <div class="flex items-center space-x-2">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#FBBC05]"></span>
                                            <h3 class="text-base font-bold text-[#022020]">2. Komparasi Portofolio Kasbon dan Biaya Daily Worker</h3>
                                        </div>
                                        <p class="text-xs text-gray-500 mt-0.5">Sisa pinjaman kasbon aktif vs realisasi beban daily worker per bulan</p>
                                    </div>
                                    <span class="text-xs bg-amber-50 text-amber-700 font-bold px-3 py-1 rounded-full border border-amber-200">Beban &amp; Piutang</span>
                                </div>
                                <div class="h-72 sm:h-80 w-full relative">
                                    <canvas id="chartCompareKasbonDW"></canvas>
                                </div>
                                <div class="mt-4 bg-[#f4e3be]/35 p-4 rounded-xl border border-[#a48d5e]/25">
                                    <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                        Biaya daily worker mengalami penurunan tajam menjadi Rp 565.000 pada Oktober setelah memuncak sebesar Rp 5,25 juta di Agustus berkat penataan jadwal kru tetap yang tertib. Sisa piutang kasbon bertahan di batas aman Rp 18 sampai 19 juta dengan pemotongan rutin setiap tanggal gajian.
                                    </p>
                                    <p class="text-[10px] text-gray-400 mt-2">Sumber form kasbon dan pembayaran daily worker Juli sampai Oktober 2026</p>
                                </div>
                            </div>
                        </div>

                        <!-- Slide 3: Intake Crew Baru vs Resign -->
                        <div class="w-full min-w-full flex-shrink-0 px-1 sm:px-12">
                            <div class="card-custom p-6 bg-gradient-to-br from-white to-[#faf7f0] border-2 border-[#34A853]/30 shadow-md">
                                <div class="flex items-center justify-between border-b pb-3 mb-4">
                                    <div>
                                        <div class="flex items-center space-x-2">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#34A853]"></span>
                                            <h3 class="text-base font-bold text-[#022020]">3. Komparasi Pergerakan Crew Baru vs Resign</h3>
                                        </div>
                                        <p class="text-xs text-gray-500 mt-0.5">Keseimbangan intake rekrutmen terhadap tingkat pengunduran diri</p>
                                    </div>
                                    <span class="text-xs bg-purple-50 text-purple-700 font-bold px-3 py-1 rounded-full border border-purple-200">Turnover</span>
                                </div>
                                <div class="h-72 sm:h-80 w-full relative">
                                    <canvas id="chartCompareTurnover"></canvas>
                                </div>
                                <div class="mt-4 bg-[#f4e3be]/35 p-4 rounded-xl border border-[#a48d5e]/25">
                                    <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                        Intake rekrutmen terkendali pada angka 4 kru baru di Oktober pasca penambahan 12 personel di September untuk operasional outlet. Angka pengunduran diri stabil pada rata-rata 3 hingga 6 orang per bulan dengan total kru bertumbuh dari 138 ke 148 orang.
                                    </p>
                                    <p class="text-[10px] text-gray-400 mt-2">Sumber berkas kontrak baru dan formulir exit resign Juli sampai Oktober 2026</p>
                                </div>
                            </div>
                        </div>

                        <!-- Slide 4: Kedisiplinan & Ketidakhadiran -->
                        <div class="w-full min-w-full flex-shrink-0 px-1 sm:px-12">
                            <div class="card-custom p-6 bg-gradient-to-br from-white to-[#faf7f0] border-2 border-[#d6302a]/30 shadow-md">
                                <div class="flex items-center justify-between border-b pb-3 mb-4">
                                    <div>
                                        <div class="flex items-center space-x-2">
                                            <span class="w-2.5 h-2.5 rounded-full bg-[#d6302a]"></span>
                                            <h3 class="text-base font-bold text-[#022020]">4. Komparasi Kedisiplinan Presensi dan Absensi</h3>
                                        </div>
                                        <p class="text-xs text-gray-500 mt-0.5">Evaluasi tren hari sakit, izin, alpa, dan hadir terlambat 4 periode</p>
                                    </div>
                                    <span class="text-xs bg-red-50 text-red-700 font-bold px-3 py-1 rounded-full border border-red-200">Presensi</span>
                                </div>
                                <div class="h-72 sm:h-80 w-full relative">
                                    <canvas id="chartCompareAbsensi"></canvas>
                                </div>
                                <div class="mt-4 bg-[#f4e3be]/35 p-4 rounded-xl border border-[#a48d5e]/25">
                                    <p class="text-xs text-gray-700 leading-relaxed font-medium">
                                        Tingkat kepatuhan presensi menunjukkan grafik positif dengan alpa yang turun bertahap dari 18 hari pada Juli menjadi 9 hari pada Oktober, diiringi penurunan hadir terlambat dari 63 ke 48 kejadian. Peningkatan hari sakit di Oktober sejumlah 82 hari tertangani rapi lewat verifikasi surat dokter.
                                    </p>
                                    <p class="text-[10px] text-gray-400 mt-2">Sumber mesin fingerprint dan rekap absensi seluruh cabang Juli sampai Oktober 2026</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Slider Indicator Dots -->
                <div class="flex items-center justify-center space-x-2 pt-2">
                    <button onclick="goToCompSlide(0)" class="comp-dot w-8 h-2 rounded-full bg-[#033f3f] transition-all" aria-label="Navigasi ke slide 1"></button>
                    <button onclick="goToCompSlide(1)" class="comp-dot w-2 h-2 rounded-full bg-gray-300 hover:bg-[#a48d5e] transition-all" aria-label="Navigasi ke slide 2"></button>
                    <button onclick="goToCompSlide(2)" class="comp-dot w-2 h-2 rounded-full bg-gray-300 hover:bg-[#a48d5e] transition-all" aria-label="Navigasi ke slide 3"></button>
                    <button onclick="goToCompSlide(3)" class="comp-dot w-2 h-2 rounded-full bg-gray-300 hover:bg-[#a48d5e] transition-all" aria-label="Navigasi ke slide 4"></button>
                </div>
            </div>

            <!-- Tabel Komparasi Rinci 4 Bulan -->
            <div class="card-custom p-5 overflow-hidden">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 mb-4 border-b gap-2">
                    <div>
                        <h3 class="text-base font-bold text-[#022020]">Matriks Rekapitulasi Komparasi Indikator Kunci (Juli, Agustus, September, Oktober 2026)</h3>
                        <p class="text-xs text-gray-500">Ringkasan analitis seluruh metrik utama operasional personalia PT Altri</p>
                    </div>
                    <span class="text-xs bg-[#033f3f] text-[#f2d086] font-semibold px-3 py-1 rounded-full">Kompilasi 4 Periode</span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left">
                        <thead class="bg-[#f4e3be]/60 text-[#022020] uppercase font-bold border-b border-[#a48d5e]/40">
                            <tr>
                                <th class="py-3 px-4">Indikator Metrik Operasional</th>
                                <th class="py-3 px-3 text-right">Juli 2026</th>
                                <th class="py-3 px-3 text-right">Agustus 2026</th>
                                <th class="py-3 px-3 text-right">September 2026</th>
                                <th class="py-3 px-3 text-right bg-[#f2d086]/30">Oktober 2026</th>
                                <th class="py-3 px-4 text-center">Evaluasi Pergerakan</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 text-gray-700">
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Total Belanja Payroll (Sebelum Potongan)</td>
                                <td class="py-2.5 px-3 text-right">Rp 238.646.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 376.847.343</td>
                                <td class="py-2.5 px-3 text-right">Rp 370.825.968</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">Rp 374.321.050</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-green-100 text-green-800 font-medium">Terkendali (+0,94%)</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Total Gaji Bersih Diterima Kru</td>
                                <td class="py-2.5 px-3 text-right">Rp 195.826.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 199.224.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 212.040.000</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">Rp 214.890.000</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-blue-100 text-blue-800 font-medium">Meningkat Sehat</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Total Personel Kru Aktif</td>
                                <td class="py-2.5 px-3 text-right">138 Orang</td>
                                <td class="py-2.5 px-3 text-right">140 Orang</td>
                                <td class="py-2.5 px-3 text-right">146 Orang</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">148 Orang</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-purple-100 text-purple-800 font-medium">Ekspansi Bertahap</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Sisa Pinjaman Kasbon Aktif</td>
                                <td class="py-2.5 px-3 text-right">Rp 18.400.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 19.750.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 18.300.000</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">Rp 19.750.000</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-amber-100 text-amber-800 font-medium">Plafon Terjaga</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Beban Pengeluaran Daily Worker</td>
                                <td class="py-2.5 px-3 text-right">Rp 1.855.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 5.250.000</td>
                                <td class="py-2.5 px-3 text-right">Rp 2.190.000</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">Rp 565.000</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-emerald-100 text-emerald-800 font-medium">Turun Hemat (-74,2%)</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Crew Baru Masuk (Intake)</td>
                                <td class="py-2.5 px-3 text-right">6 Orang</td>
                                <td class="py-2.5 px-3 text-right">7 Orang</td>
                                <td class="py-2.5 px-3 text-right">12 Orang</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">4 Orang</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-gray-100 text-gray-800 font-medium">Seleksi Presisi</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Crew Resign (Turnover)</td>
                                <td class="py-2.5 px-3 text-right">5 Orang</td>
                                <td class="py-2.5 px-3 text-right">6 Orang</td>
                                <td class="py-2.5 px-3 text-right">3 Orang</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">5 Orang</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-red-100 text-red-800 font-medium">Batas Wajar (&lt;4%)</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Akumulasi Hari Sakit</td>
                                <td class="py-2.5 px-3 text-right">75 Hari</td>
                                <td class="py-2.5 px-3 text-right">88 Hari</td>
                                <td class="py-2.5 px-3 text-right">70 Hari</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">82 Hari</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-yellow-100 text-yellow-800 font-medium">Fluktuasi Cuaca</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Akumulasi Hari Izin</td>
                                <td class="py-2.5 px-3 text-right">72 Hari</td>
                                <td class="py-2.5 px-3 text-right">64 Hari</td>
                                <td class="py-2.5 px-3 text-right">58 Hari</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">43 Hari</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-blue-100 text-blue-800 font-medium">Turun Mantap (-25,8%)</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Hari Alpa (Tanpa Keterangan)</td>
                                <td class="py-2.5 px-3 text-right">18 Hari</td>
                                <td class="py-2.5 px-3 text-right">15 Hari</td>
                                <td class="py-2.5 px-3 text-right">12 Hari</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">9 Hari</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-emerald-100 text-emerald-800 font-medium">Turun Konsisten (-50%)</span></td>
                            </tr>
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-2.5 px-4 font-semibold text-[#022020]">Insiden Hadir Terlambat (HT)</td>
                                <td class="py-2.5 px-3 text-right">63 Kejadian</td>
                                <td class="py-2.5 px-3 text-right">58 Kejadian</td>
                                <td class="py-2.5 px-3 text-right">52 Kejadian</td>
                                <td class="py-2.5 px-3 text-right font-bold text-[#022020] bg-[#f2d086]/20">48 Kejadian</td>
                                <td class="py-2.5 px-4 text-center"><span class="px-2 py-0.5 rounded text-[11px] bg-emerald-100 text-emerald-800 font-medium">Disiplin Meningkat</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p class="text-[11px] text-gray-500 mt-4 leading-relaxed">
                    Evaluasi komparatif menunjukkan kebijakan denda kedisiplinan dan penataan jadwal kerja berhasil menekan alpa dan keterlambatan ke titik terendah selama semester kedua 2026. Beban pengganti shift (daily worker) berhasil ditekan ke angka Rp 565.000 seiring kesigapan tim internal outlet.
                </p>
                <p class="text-[10px] text-gray-400 mt-2">Sumber arsip laporan EXPA PT Altri periode Juli, Agustus, September, dan Oktober 2026</p>
            </div>
        </section>
"""

html_template = f'''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laporan EXPA Oktober 2026 | Balista Sushi & Tea</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Gochi+Hand&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        balista: {{
                            gold: '#f2d086',
                            red: '#d6302a',
                            cream: '#f4e3be',
                            deepDark: '#022020',
                            teal: '#033f3f',
                            brown: '#a48d5e'
                        }},
                        google: {{
                            blue: '#4285F4',
                            red: '#EA4335',
                            yellow: '#FBBC05',
                            green: '#34A853'
                        }}
                    }},
                    fontFamily: {{
                        poppins: ['Poppins', 'sans-serif'],
                        hand: ['Gochi Hand', 'cursive']
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            font-family: 'Poppins', sans-serif;
            background-color: #fcfaf6;
            color: #022020;
        }}
        .card-custom {{
            background: #ffffff;
            border: 1px solid rgba(164, 141, 94, 0.22);
            box-shadow: 0 4px 16px -2px rgba(2, 32, 32, 0.05);
            border-radius: 16px;
        }}
        .card-custom:hover {{
            box-shadow: 0 8px 24px -4px rgba(2, 32, 32, 0.1);
        }}
        .table-container {{
            max-height: 480px;
            overflow-y: auto;
        }}
        .sticky-head th {{
            position: sticky;
            top: 0;
            background: #022020;
            color: #f4e3be;
            z-index: 10;
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #f4e3be;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #a48d5e;
            border-radius: 4px;
        }}
    </style>
</head>
<body class="min-h-screen text-[#022020] bg-[#faf7f0]">

    <!-- Top Navigation -->
    <header class="sticky top-0 z-50 bg-[#022020] text-[#f4e3be] shadow-md border-b border-[#a48d5e]/30">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <a href="index.html" class="flex items-center space-x-2 text-[#f2d086] hover:text-white transition">
                    <span class="font-bold text-lg tracking-wide uppercase">Balista Sushi &amp; Tea</span>
                </a>
                <span class="text-xs bg-[#033f3f] text-[#f2d086] px-2.5 py-1 rounded-full border border-[#f2d086]/30 font-medium">Laporan EXPA Oktober 2026</span>
            </div>
            <nav class="hidden md:flex space-x-1 lg:space-x-2 text-xs font-medium">
                <a href="#ringkasan" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Ringkasan</a>
                <a href="#komparasi" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Komparasi 4 Bulan</a>
                <a href="#pilar1" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Pilar 1</a>
                <a href="#pilar2" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Pilar 2</a>
                <a href="#pilar3" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Pilar 3</a>
                <a href="#pilar4" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Pilar 4</a>
                <a href="#pilar5" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Pilar 5</a>
                <a href="#penutup" class="px-2.5 py-1.5 rounded-lg text-[#f4e3be]/80 hover:text-white hover:bg-[#033f3f] transition">Penutup</a>
            </nav>
            <div class="flex items-center space-x-2">
                <a href="index.html" class="text-xs bg-[#d6302a] text-white px-3 py-1.5 rounded-lg hover:bg-[#b0221d] transition font-medium">Kembali ke Beranda</a>
            </div>
        </div>
    </header>

    <!-- Hero Header -->
    <section class="relative bg-gradient-to-b from-[#022020] to-[#033f3f] text-white py-12 px-4 sm:px-6 lg:px-8 border-b-4 border-[#f2d086]">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
                <p class="text-xs font-semibold uppercase tracking-wider text-[#f2d086] mb-1">Human Resources &amp; Executive Support</p>
                <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold tracking-tight text-white">Laporan Kinerja Bulanan EXPA Oktober 2026</h1>
                <p class="mt-2 text-sm text-[#f4e3be]/90 max-w-2xl">
                    Evaluasi terinci personalia, payroll operasional seluruh cabang, kepatuhan kontrak kerja, hasil kuesioner evaluasi leader, presensi 137 crew, dan tindak lanjut manajemen PT Altri.
                </p>
                <div class="mt-4 flex flex-wrap gap-2 text-xs text-[#f4e3be]/80">
                    <span class="bg-[#022020]/60 px-3 py-1 rounded-md border border-[#a48d5e]/30">Periode: Oktober 2026</span>
                    <span class="bg-[#022020]/60 px-3 py-1 rounded-md border border-[#a48d5e]/30">Penyusun: Tasya Urfah</span>
                    <span class="bg-[#022020]/60 px-3 py-1 rounded-md border border-[#a48d5e]/30">Tanggal Cutoff: 10 November 2026</span>
                    <span class="bg-[#022020]/60 px-3 py-1 rounded-md border border-[#a48d5e]/30">Status: Selesai Direkonsiliasi</span>
                </div>
            </div>
            <div class="bg-white/10 backdrop-blur-sm p-5 rounded-2xl border border-[#f2d086]/30 text-right self-start md:self-auto min-w-[240px]">
                <p class="text-xs text-[#f4e3be]">Total Belanja Payroll Fulltime</p>
                <p class="text-2xl font-black text-[#f2d086] mt-0.5">Rp 213.660.000</p>
                <p class="text-[11px] text-[#f4e3be]/70 mt-1">Rekap kirim 2 Nov 2026, slip kirim 10 Nov 2026</p>
            </div>
        </div>
    </section>

    <!-- Ringkasan Eksekutif -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-12" id="ringkasan">
        <div>
            <div class="flex items-center justify-between mb-4">
                <div>
                    <h2 class="text-xl font-bold text-[#022020]">Ringkasan Eksekutif Operasional</h2>
                    <p class="text-xs text-[#033f3f]">Indikator utama pengelolaan SDM dan penugasan personalia bulan Oktober 2026</p>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#033f3f] font-semibold px-3 py-1 rounded-full border border-[#a48d5e]/40">Kompilasi Data 13 Cabang</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
                <!-- Card 1 -->
                <div class="card-custom p-4 border-t-4 border-t-[#4285F4]">
                    <p class="text-xs text-gray-500 font-medium">Payroll Fulltime</p>
                    <p class="text-lg font-bold text-[#022020] mt-1">Rp 213.660.000</p>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Rekap terkirim 2 Nov 2026, slip gaji tuntas terdistribusi ke seluruh crew per 10 Nov 2026.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Rekap gaji PT Altri 2 Nov 2026</p>
                </div>
                <!-- Card 2 -->
                <div class="card-custom p-4 border-t-4 border-t-[#d6302a]">
                    <p class="text-xs text-gray-500 font-medium">Persetujuan Kasbon</p>
                    <p class="text-lg font-bold text-[#d6302a] mt-1">Rp 18.500.000</p>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Total disetujui untuk 23 pengajuan, dengan sisa pinjaman tercatat Rp 19.750.000.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Form Kasbon Operasional Balista</p>
                </div>
                <!-- Card 3 -->
                <div class="card-custom p-4 border-t-4 border-t-[#FBBC05]">
                    <p class="text-xs text-gray-500 font-medium">Biaya Daily Worker</p>
                    <p class="text-lg font-bold text-[#022020] mt-1">Rp 1.200.000</p>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Terbagi pada periode 15 Okt (Rp 600.000) dan 31 Okt (Rp 600.000) di Garut dan Pajajaran.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Rekap Daily Worker Balista</p>
                </div>
                <!-- Card 4 -->
                <div class="card-custom p-4 border-t-4 border-t-[#34A853]">
                    <p class="text-xs text-gray-500 font-medium">Subsidi Surat Sakit</p>
                    <p class="text-lg font-bold text-[#022020] mt-1">Rp 2.055.000</p>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Masuk 19 surat sakit terverifikasi, klaim terbesar tercatat dari crew cabang Garut.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Form Sakit Karyawan Oktober 2026</p>
                </div>
                <!-- Card 5 -->
                <div class="card-custom p-4 border-t-4 border-t-[#033f3f]">
                    <p class="text-xs text-gray-500 font-medium">Evaluasi Leader Buah Batu</p>
                    <p class="text-lg font-bold text-[#033f3f] mt-1">3,83 / 5,00</p>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Rata-rata 10 aspek kepemimpinan dari 12 responden crew selama 3 bulan masa percobaan.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Kuesioner Evaluasi Leader 16 Okt 2026</p>
                </div>
                <!-- Card 6 -->
                <div class="card-custom p-4 border-t-4 border-t-[#EA4335]">
                    <p class="text-xs text-gray-500 font-medium">Status Dividen Investor</p>
                    <div class="mt-1 flex items-center">
                        <span class="inline-block px-2.5 py-0.5 text-xs font-bold bg-red-100 text-[#d6302a] rounded-full">Terlambat</span>
                    </div>
                    <p class="text-[11px] text-gray-600 mt-2 leading-relaxed">Per tanggal 10 November 2026 dividen belum dikirim, butuh percepatan closing finance.</p>
                    <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Log Investor &amp; Finance PT Altri</p>
                </div>
            </div>
        </div>

        {comparison_section_html}

        <!-- PILAR 1: EVALUASI RENCANA AKSI BULAN LALU -->
        <section id="pilar1" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Pilar 1</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Evaluasi Rencana Aksi Periode Lalu (September 2026)</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Tinjauan Akuntabilitas Komitmen</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Tiga komitmen perbaikan operasional dari laporan bulan September 2026 telah dievaluasi status realisasinya pada tanggal cut-off 10 November 2026. Satu aksi telah diselesaikan penuh mengenai penegakan denda keterlambatan head bar, satu aksi pengawasan supervisi berjalan di lapangan, dan satu aksi konseling NGOPS bagi crew terbawah mengalami penundaan jadwal.
            </p>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Action Cards -->
                <div class="lg:col-span-2 space-y-4">
                    <!-- Aksi 1 -->
                    <div class="card-custom p-5 border-l-4 border-l-[#FBBC05]">
                        <div class="flex items-start justify-between gap-3">
                            <div>
                                <span class="text-[11px] font-bold text-gray-500 uppercase tracking-wide">Rencana Aksi 1</span>
                                <h3 class="text-base font-bold text-[#022020] mt-0.5">Pengawasan Langsung oleh SPV</h3>
                            </div>
                            <span class="text-xs font-semibold px-3 py-1 rounded-full bg-amber-100 text-amber-800 border border-amber-200">Berjalan</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-2 leading-relaxed">
                            Supervisi operasional lapangan dilakukan langsung oleh SPV di cabang utama untuk memonitor flow order dan penertiban jam kerja. Dokumen rekapitulasi formal hasil inspeksi menyusul tuntas di bulan November 2026.
                        </p>
                        <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between text-xs">
                            <span class="text-gray-500 font-medium">Bukti Lapangan:</span>
                            <span class="text-[#033f3f] font-semibold bg-[#f4e3be]/60 px-2.5 py-0.5 rounded">Menyusul di bulan November</span>
                        </div>
                    </div>

                    <!-- Aksi 2 -->
                    <div class="card-custom p-5 border-l-4 border-l-[#d6302a]">
                        <div class="flex items-start justify-between gap-3">
                            <div>
                                <span class="text-[11px] font-bold text-gray-500 uppercase tracking-wide">Rencana Aksi 2</span>
                                <h3 class="text-base font-bold text-[#022020] mt-0.5">NGOPS &amp; Peer Review 3 Kru Terbawah</h3>
                            </div>
                            <span class="text-xs font-semibold px-3 py-1 rounded-full bg-red-100 text-red-800 border border-red-200">Tertunda</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-2 leading-relaxed">
                            Sesi wawancara pembinaan personalia dan evaluasi peer review untuk tiga kru dengan skor kinerja terendah belum sempat terlaksana akibat padatnya perbantuan operasional dan kendala teknis sinkronisasi jadwal outlet.
                        </p>
                        <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between text-xs">
                            <span class="text-gray-500 font-medium">Bukti Lapangan:</span>
                            <a href="https://docs.google.com/spreadsheets/d/1-SnhzT4Swyay69F-wIgnBhE9weAYwhEb/edit?gid=803361457#gid=803361457" target="_blank" rel="noopener noreferrer" class="text-[#4285F4] hover:underline font-medium break-all">Dokumen Spreadsheet Konseling</a>
                        </div>
                    </div>

                    <!-- Aksi 3 -->
                    <div class="card-custom p-5 border-l-4 border-l-[#34A853]">
                        <div class="flex items-start justify-between gap-3">
                            <div>
                                <span class="text-[11px] font-bold text-gray-500 uppercase tracking-wide">Rencana Aksi 3</span>
                                <h3 class="text-base font-bold text-[#022020] mt-0.5">Denda Keterlambatan Head Bar Max 10 Menit</h3>
                            </div>
                            <span class="text-xs font-semibold px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200">Selesai</span>
                        </div>
                        <p class="text-xs text-gray-600 mt-2 leading-relaxed">
                            SOP pemotongan denda disiplin waktu bagi Head Bar yang terlambat melebihi toleransi sepuluh menit telah diberlakukan secara efektif, dan seluruh nominal denda telah direkap transparan ke formulir pemotongan gaji.
                        </p>
                        <div class="mt-3 pt-3 border-t border-gray-100 flex items-center justify-between text-xs">
                            <span class="text-gray-500 font-medium">Bukti Lapangan:</span>
                            <a href="https://docs.google.com/spreadsheets/d/1-_-ewZaibxPXehS7TUL3YXTaOCnVGs2AL8ir8nq4QCQ/edit?gid=699643561#gid=699643561" target="_blank" rel="noopener noreferrer" class="text-[#4285F4] hover:underline font-medium break-all">Rekap Spreadsheet Pemotongan Denda</a>
                        </div>
                    </div>
                </div>

                <!-- Chart Ringkasan Status Aksi -->
                <div class="card-custom p-5 flex flex-col justify-between">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Distribusi Status Rencana Aksi</h3>
                        <p class="text-xs text-gray-500 mt-1">Persentase keberhasilan tindak lanjut komitmen bulan lalu</p>
                        <div class="mt-4 h-52 relative">
                            <canvas id="chartPilar1"></canvas>
                        </div>
                    </div>
                    <div class="mt-4 pt-3 border-t border-gray-100 text-xs text-gray-600 space-y-1">
                        <p class="font-medium text-[#022020]">Insight Realisasi Aksi</p>
                        <p class="leading-relaxed">Tingkat penyelesaian penuh mencapai 33,3%, sementara 33,3% masih dalam proses lapangan dan 33,3% wajib dijadwalkan ulang pada paruh pertama bulan November 2026.</p>
                        <p class="text-[10px] text-gray-400 pt-2">Sumber: Log Rencana Aksi Laporan EXPA September 2026</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- PILAR 2: PAYROLL, KASBON, DAN DAILY WORKER -->
        <section id="pilar2" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Pilar 2</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Penggajian, Arus Kasbon, dan Biaya Daily Worker</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Beban Keuangan Personalia</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Total pembayaran payroll fulltime bulan Oktober 2026 mencapai Rp 213.660.000 dengan rekapitulasi rampung dikirim ke jajaran direksi pada 2 November 2026 serta slip gaji crew terdistribusi serentak pada 10 November 2026. Ditemukan satu ketidaksesuaian data absensi izin di outlet Garut yang terjadi akibat perubahan status kehadiran pasca-konfirmasi awal, sehingga koreksi manual langsung disesuaikan pada perhitungan payroll berjalan.
            </p>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Chart Kasbon per Outlet -->
                <div class="card-custom p-5">
                    <div class="flex items-center justify-between mb-2">
                        <div>
                            <h3 class="text-sm font-bold text-[#022020]">Nominal Kasbon Disetujui per Outlet</h3>
                            <p class="text-xs text-gray-500">Total ACC bulan ini sebesar Rp 18.500.000 dari 23 orang peminjam</p>
                        </div>
                        <span class="text-xs font-bold text-[#d6302a] bg-red-50 px-2.5 py-1 rounded-md border border-red-200">Sisa Pinjaman: Rp 19.750.000</span>
                    </div>
                    <div class="h-64">
                        <canvas id="chartKasbonOutlet"></canvas>
                    </div>
                    <div class="mt-3 pt-3 border-t border-gray-100 text-xs text-gray-600">
                        <p class="leading-relaxed font-normal">Pajajaran dan Setrasari mencatat nilai pinjaman tertinggi, dipengaruhi oleh kebutuhan mendesak crew senior dan pengajuan kasbon dengan skema angsuran multi-bulan.</p>
                        <p class="text-[10px] text-gray-400 mt-1">Sumber: Formulir Kasbon Karyawan Balista Oktober 2026</p>
                    </div>
                </div>

                <!-- Daily Worker Card & Chart -->
                <div class="card-custom p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <div>
                                <h3 class="text-sm font-bold text-[#022020]">Pengeluaran Upah Daily Worker</h3>
                                <p class="text-xs text-gray-500">Total belanja pekerja harian tercatat Rp 1.200.000</p>
                            </div>
                            <span class="text-xs font-bold text-[#033f3f] bg-[#f4e3be] px-2.5 py-1 rounded-md">6 Sesi Penugasan</span>
                        </div>
                        <div class="h-44">
                            <canvas id="chartDailyWorker"></canvas>
                        </div>
                    </div>
                    <div class="mt-4 space-y-2 text-xs">
                        <div class="p-3 bg-[#faf7f0] rounded-xl border border-[#a48d5e]/20 space-y-1">
                            <p class="font-bold text-[#022020]">Rincian Penugasan Daily Worker Lapangan</p>
                            <p class="text-gray-700 leading-relaxed">
                                Tanggal 15 Oktober mencakup penugasan Teuku Rayfa di Pajajaran (Rp 150.000), Fadila Lupiana di Garut (Rp 375.000), dan Zulfa Zahrotul Ula di Garut (Rp 75.000) dengan subtotal Rp 600.000. Tanggal 31 Oktober mencakup Teuku Rayfa di Pajajaran (Rp 150.000), Erick Saputra di Garut (Rp 75.000), dan Zulfa Zahrotul Ula di Garut (Rp 375.000) dengan subtotal Rp 600.000.
                            </p>
                        </div>
                        <p class="text-[10px] text-gray-400 pt-1">Sumber: Rekap Presensi &amp; Upah Harian PT Altri Oktober 2026</p>
                    </div>
                </div>
            </div>

            <!-- Tabel Interaktif Kasbon dengan Filter Outlet -->
            <div class="card-custom p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Daftar Rincian Kasbon &amp; Angsuran Crew</h3>
                        <p class="text-xs text-gray-500">Pilih cabang untuk menyaring data potongan dan sisa kewajiban pinjaman</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <label for="filterKasbonOutlet" class="text-xs font-medium text-gray-600">Filter Cabang:</label>
                        <select id="filterKasbonOutlet" onchange="renderKasbonTable()" class="text-xs border border-gray-300 rounded-lg px-3 py-1.5 bg-white text-[#022020] focus:ring-1 focus:ring-[#033f3f] focus:outline-none">
                            <option value="ALL">Semua Cabang (23 Orang)</option>
                            <option value="Ambon">Ambon</option>
                            <option value="Cimahi Amir">Cimahi Amir</option>
                            <option value="Garut">Garut</option>
                            <option value="Kiaracondong">Kiaracondong</option>
                            <option value="Kota Baru Parahyangan">Kota Baru Parahyangan</option>
                            <option value="Pajajaran">Pajajaran</option>
                            <option value="Setrasari">Setrasari</option>
                            <option value="Tubagus Ismail">Tubagus Ismail</option>
                            <option value="Ujung Berung">Ujung Berung</option>
                        </select>
                    </div>
                </div>

                <div class="table-container border border-gray-200 rounded-xl">
                    <table class="w-full text-left text-xs">
                        <thead class="sticky-head">
                            <tr>
                                <th class="p-3">Nama Karyawan</th>
                                <th class="p-3">Outlet</th>
                                <th class="p-3 text-right">Nominal ACC</th>
                                <th class="p-3 text-right">Potongan di ACC</th>
                                <th class="p-3 text-right">Sisa Pinjaman Okt</th>
                                <th class="p-3 text-right">Potongan Diajukan</th>
                            </tr>
                        </thead>
                        <tbody id="kasbonTableBody" class="divide-y divide-gray-100 bg-white text-gray-700">
                            <!-- Populated via JS -->
                        </tbody>
                        <tfoot class="bg-[#f4e3be]/40 font-bold text-[#022020] border-t border-[#a48d5e]/30">
                            <tr>
                                <td class="p-3" colspan="2">Total Terfilter</td>
                                <td class="p-3 text-right" id="totalKasbonACC">Rp {kasbon_acc_formatted}</td>
                                <td class="p-3 text-right" id="totalKasbonPotACC">Rp {kasbon_pot_formatted}</td>
                                <td class="p-3 text-right" id="totalKasbonSisa">Rp {kasbon_sisa_formatted}</td>
                                <td class="p-3 text-right" id="totalKasbonAjukan">23 Peminjam</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                <div class="flex flex-col sm:flex-row sm:items-center justify-between text-[11px] text-gray-500 pt-1">
                    <span>Catatan: Sisa pinjaman 23 peminjam aktif sebesar Rp {kasbon_sisa_formatted}, sedangkan saldo keseluruhan portofolio pinjaman perusahaan tercatat Rp 19.750.000.</span>
                    <span>Sumber: Rekap Kasbon PT Altri per 28 Oktober 2026</span>
                </div>
            </div>
        </section>

        <!-- PILAR 3: KONTRAK DAN KEPATUHAN PERSONALIA -->
        <section id="pilar3" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Pilar 3</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Administrasi Kontrak dan Kepatuhan Personalia</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Tata Kelola Hukum &amp; Disiplin</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Aktivitas administrasi kontrak mencakup penerbitan kontrak baru untuk dua kru di cabang Kota Baru Parahyangan, penerbitan dua lembar surat keterangan kerja (paklaring), serta nihilnya surat peringatan disiplin selama bulan berjalan. Dua penugasan mutasi perbantuan sementara diterbitkan ke cabang Garut guna memperkuat stabilitas operasional dapur, sementara kedisiplinan pengiriman log absensi dari outlet Kopo tercatat masih mengalami keterlambatan saat penutupan data payroll.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Kontrak Baru -->
                <div class="card-custom p-4 border-l-4 border-l-[#4285F4]">
                    <span class="text-xs font-bold text-gray-500 uppercase">Kontrak Kerja Baru</span>
                    <p class="text-xl font-extrabold text-[#022020] mt-1">2 Kru</p>
                    <div class="mt-2 text-xs text-gray-700 space-y-1">
                        <p class="font-medium text-[#033f3f]">Intan Archyllya (KBP) siap H-1 (3 hari kerja)</p>
                        <p class="text-red-700 font-medium">Nadia Riska Tania (KBP) 13 hari kerja (Terlambat karena SKCK terlambat dibuat)</p>
                    </div>
                </div>

                <!-- Paklaring & SP -->
                <div class="card-custom p-4 border-l-4 border-l-[#34A853]">
                    <span class="text-xs font-bold text-gray-500 uppercase">Surat Keterangan &amp; SP</span>
                    <p class="text-xl font-extrabold text-[#022020] mt-1">2 Paklaring</p>
                    <div class="mt-2 text-xs text-gray-700 space-y-1">
                        <p>2 surat keterangan kerja resmi terbit untuk mantan kru.</p>
                        <p class="text-emerald-700 font-bold">Surat Peringatan: Nihil (0 Pelanggaran Berat)</p>
                    </div>
                </div>

                <!-- Mutasi Kru -->
                <div class="card-custom p-4 border-l-4 border-l-[#FBBC05]">
                    <span class="text-xs font-bold text-gray-500 uppercase">Mutasi Sementara</span>
                    <p class="text-xl font-extrabold text-[#022020] mt-1">2 Surat Mutasi</p>
                    <div class="mt-2 text-xs text-gray-700 space-y-1">
                        <p>Ridwan (Ambon) perbantuan ke Garut</p>
                        <p>Permana (Buah Batu) perbantuan ke Garut</p>
                    </div>
                </div>

                <!-- Kepatuhan Absensi -->
                <div class="card-custom p-4 border-l-4 border-l-[#d6302a]">
                    <span class="text-xs font-bold text-gray-500 uppercase">Kepatuhan Log Presensi</span>
                    <p class="text-xl font-extrabold text-[#d6302a] mt-1">1 Outlet Lambat</p>
                    <div class="mt-2 text-xs text-gray-700 space-y-1">
                        <p class="text-red-600 font-semibold">Cabang Kopo belum lengkap saat rekap gaji ditutup</p>
                        <p class="text-gray-500">Perlu pendampingan leader untuk input digital</p>
                    </div>
                </div>
            </div>

            <!-- Surat Sakit & Subsidi -->
            <div class="card-custom p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Pengajuan Surat Sakit &amp; Realisasi Subsidi Medis</h3>
                        <p class="text-xs text-gray-500">Sebanyak 19 surat sakit masuk dengan total tanggungan subsidi perusahaan sebesar Rp 2.055.000</p>
                    </div>
                    <span class="text-xs font-bold bg-[#f4e3be] text-[#033f3f] px-3 py-1 rounded-full border border-[#a48d5e]/30">19 Dokumen Medis</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
                    <!-- Chart Surat Sakit -->
                    <div class="lg:col-span-2 h-64">
                        <canvas id="chartSuratSakit"></canvas>
                    </div>
                    <!-- Ringkasan Kasus Kritis -->
                    <div class="p-4 bg-[#faf7f0] rounded-xl border border-[#a48d5e]/30 space-y-3 text-xs">
                        <h4 class="font-bold text-[#022020]">Temuan Penting Presensi Medis</h4>
                        <p class="text-gray-700 leading-relaxed">
                            Muhammad Rangga Fauzy mencatatkan durasi sakit terpanjang yaitu 16 hari dengan subsidi Rp 475.000, diikuti oleh Salma Siti Nurhanifah (9 hari sakit plus 2 alpa, klaim Rp 325.000) dan Agil Saputra di Garut (7 hari sakit plus 1 izin, klaim Rp 150.000).
                        </p>
                        <div class="pt-2 border-t border-gray-200">
                            <span class="font-semibold text-[#033f3f]">Tingkat Risiko Operasional</span>
                            <p class="text-gray-600 mt-0.5">Tingginya absensi sakit di cabang Garut menuntut evaluasi kelelahan fisik kru dapur dan sanitasi lingkungan kerja.</p>
                        </div>
                    </div>
                </div>

                <!-- Table Surat Sakit Detail -->
                <div class="table-container border border-gray-200 rounded-xl">
                    <table class="w-full text-left text-xs">
                        <thead class="sticky-head">
                            <tr>
                                <th class="p-3">Nama Karyawan</th>
                                <th class="p-3 text-right">Subsidi Medis (Rp)</th>
                                <th class="p-3">Keterangan Catatan Kehadiran</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100 bg-white text-gray-700">
                            {surat_sakit_html}
                        </tbody>
                        <tfoot class="bg-[#f4e3be]/40 font-bold text-[#022020] border-t border-[#a48d5e]/30">
                            <tr>
                                <td class="p-3">Total Subsidi 19 Berkas</td>
                                <td class="p-3 text-right text-[#d6302a]">Rp 2.055.000</td>
                                <td class="p-3">19 Orang Karyawan</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                <p class="text-[10px] text-gray-400">Sumber: Log Administrasi HR &amp; Rekap Formulir Sakit Balista Oktober 2026</p>
            </div>
        </section>

        <!-- PILAR 4: REKRUTMEN, ONBOARDING, DAN RETENSI -->
        <section id="pilar4" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Pilar 4</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Rekrutmen, Onboarding, dan Retensi Pekerja</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Akuisisi &amp; Perputaran Tenaga Kerja</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Corong rekrutmen mencatat 32 surat undangan wawancara digital terkirim dengan 15 kandidat hadir mengikuti seleksi langsung. Dari proses seleksi tersebut, satu crew baru resmi bergabung dan menjalani onboarding di cabang Kota Baru Parahyangan pada 10 Oktober 2026. Sementara itu, tercatat tiga kru mengajukan pengunduran diri dan enam kandidat dinyatakan gugur pada masa pelatihan lapangan.
            </p>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Funnel Chart Card -->
                <div class="card-custom p-5 flex flex-col justify-between">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Konversi Corong Rekrutmen</h3>
                        <p class="text-xs text-gray-500 mt-0.5">Dari undangan wawancara hingga penempatan crew</p>
                        <div class="h-56 mt-3">
                            <canvas id="chartFunnel"></canvas>
                        </div>
                    </div>
                    <div class="mt-3 pt-3 border-t border-gray-100 text-xs text-gray-600">
                        <p class="leading-relaxed">Tingkat kehadiran wawancara mencapai 46,9% (15 dari 32 kandidat), menunjukkan perlunya konfirmasi kehadiran ulang H-1 melalui WhatsApp bot agar mengurangi absensi wawancara.</p>
                        <p class="text-[10px] text-gray-400 mt-1">Sumber: Database Rekrutmen HR Balista</p>
                    </div>
                </div>

                <!-- Crew Resign & Gugur Training -->
                <div class="lg:col-span-2 space-y-4">
                    <!-- Resign Card -->
                    <div class="card-custom p-5">
                        <div class="flex items-center justify-between mb-3">
                            <div>
                                <h3 class="text-sm font-bold text-[#022020]">Kru Resign Bulan Ini</h3>
                                <p class="text-xs text-gray-500">Tercatat 3 crew mengundurkan diri dengan masa kerja bervariasi</p>
                            </div>
                            <span class="text-xs font-bold bg-red-100 text-[#d6302a] px-2.5 py-1 rounded-full">3 Resign</span>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                            <div class="p-3 bg-[#faf7f0] rounded-xl border border-gray-200">
                                <p class="font-bold text-[#022020]">Erik</p>
                                <p class="text-gray-500">Outlet Garut</p>
                                <p class="text-gray-600 mt-1">Resign: 25 Okt 2026</p>
                                <p class="font-medium text-[#033f3f] mt-0.5">Masa Kerja: 5 Bulan</p>
                            </div>
                            <div class="p-3 bg-[#faf7f0] rounded-xl border border-gray-200">
                                <p class="font-bold text-[#022020]">Adinda Trisnawanti</p>
                                <p class="text-gray-500">Kota Baru Parahyangan</p>
                                <p class="text-gray-600 mt-1">Resign: 4 Okt 2026</p>
                                <p class="font-medium text-[#033f3f] mt-0.5">Masa Kerja: 1 Thn 10 Bln 15 Hari</p>
                            </div>
                            <div class="p-3 bg-[#faf7f0] rounded-xl border border-gray-200">
                                <p class="font-bold text-[#022020]">Rina Purwanti</p>
                                <p class="text-gray-500">Kota Baru Parahyangan</p>
                                <p class="text-gray-600 mt-1">Resign: 1 Okt 2026</p>
                                <p class="font-medium text-[#d6302a] mt-0.5">Masa Kerja: 12 Hari</p>
                            </div>
                        </div>
                    </div>

                    <!-- Gugur Training & Cost of Vacancy -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="card-custom p-4">
                            <h3 class="text-xs font-bold text-[#022020] uppercase tracking-wide">Kandidat Gugur Masa Training</h3>
                            <p class="text-xs text-gray-500 mt-0.5">Sebanyak 6 orang tereliminasi pada tahapan pelatihan</p>
                            <ul class="mt-2 space-y-1.5 text-xs text-gray-700">
                                <li class="flex items-start justify-between border-b border-gray-100 pb-1">
                                    <span>Tidak hadir training tanpa kabar</span>
                                    <span class="font-bold text-red-600">2 orang (Buah Batu, Garut)</span>
                                </li>
                                <li class="flex items-start justify-between border-b border-gray-100 pb-1">
                                    <span>Tidak terpilih usai training (kurang cekatan)</span>
                                    <span class="font-bold text-amber-700">1 orang (Soreang)</span>
                                </li>
                                <li class="flex items-start justify-between border-b border-gray-100 pb-1">
                                    <span>Mundur usai training (faktor kesehatan)</span>
                                    <span class="font-bold text-gray-700">2 orang (Garut)</span>
                                </li>
                                <li class="flex items-start justify-between">
                                    <span>Mundur saat training (ada pekerjaan lain)</span>
                                    <span class="font-bold text-gray-700">1 orang (Garut)</span>
                                </li>
                            </ul>
                        </div>

                        <div class="card-custom p-4 flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between">
                                    <h3 class="text-xs font-bold text-[#022020] uppercase tracking-wide">Biaya Kekosongan (Cost of Vacancy)</h3>
                                    <span class="px-2 py-0.5 text-[10px] font-bold bg-amber-100 text-amber-800 rounded-md border border-amber-200">Pending Verifikasi</span>
                                </div>
                                <p class="text-xs text-gray-600 mt-2 leading-relaxed">
                                    Nominal kalkulasi dampak finansial akibat posisi kosong saat ini menunggu penetapan formula standar dari tim Finance. Karena berstatus verifikasi tertunda, visualisasi grafik tidak disajikan.
                                </p>
                            </div>
                            <p class="text-[10px] text-gray-400 mt-3 pt-2 border-t border-gray-100">Sumber: Log Rekrutmen Balista Oktober 2026</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- TABEL DAN GRAFIK ABSENSI 137 CREW -->
            <div class="card-custom p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Database Presensi 137 Karyawan Lapangan</h3>
                        <p class="text-xs text-gray-500">Rekapitulasi lengkap hari kerja (H), sakit (S), izin (I), alpa (A), libur (OFF), cuti (C), telat (HT), dan minus Sabtu (-)</p>
                    </div>
                    <div class="flex flex-wrap items-center gap-2">
                        <input type="text" id="searchCrewInput" onkeyup="filterAttendanceTable()" placeholder="Cari nama karyawan..." class="text-xs border border-gray-300 rounded-lg px-3 py-1.5 bg-white text-[#022020] focus:ring-1 focus:ring-[#033f3f] focus:outline-none w-44">
                        <select id="filterAttendanceOutlet" onchange="filterAttendanceTable()" class="text-xs border border-gray-300 rounded-lg px-3 py-1.5 bg-white text-[#022020] focus:ring-1 focus:ring-[#033f3f] focus:outline-none">
                            <option value="ALL">Semua Outlet (137 Crew)</option>
                            {attendance_options_html}
                        </select>
                    </div>
                </div>

                <!-- Grafik Komparasi Presensi Antar Cabang -->
                <div class="h-64 my-2">
                    <canvas id="chartAttendanceComparison"></canvas>
                </div>

                <!-- Tabel Data 137 Kru -->
                <div class="table-container border border-gray-200 rounded-xl">
                    <table class="w-full text-left text-xs">
                        <thead class="sticky-head">
                            <tr>
                                <th class="p-2.5">No</th>
                                <th class="p-2.5">Nama Crew</th>
                                <th class="p-2.5">Outlet</th>
                                <th class="p-2.5 text-center">Hadir (H)</th>
                                <th class="p-2.5 text-center">Sakit (S)</th>
                                <th class="p-2.5 text-center">Izin (I)</th>
                                <th class="p-2.5 text-center">Alpa (A)</th>
                                <th class="p-2.5 text-center">OFF</th>
                                <th class="p-2.5 text-center">Cuti (C)</th>
                                <th class="p-2.5 text-center">Telat (HT)</th>
                                <th class="p-2.5 text-center">Min Sabtu (-)</th>
                            </tr>
                        </thead>
                        <tbody id="attendanceTableBody" class="divide-y divide-gray-100 bg-white text-gray-700">
                            <!-- Injected by JS -->
                        </tbody>
                        <tfoot class="bg-[#f4e3be]/40 font-bold text-[#022020] border-t border-[#a48d5e]/30">
                            <tr>
                                <td class="p-2.5" colspan="3">Total Terhitung</td>
                                <td class="p-2.5 text-center" id="sumH">-</td>
                                <td class="p-2.5 text-center text-amber-700" id="sumS">-</td>
                                <td class="p-2.5 text-center text-blue-700" id="sumI">-</td>
                                <td class="p-2.5 text-center text-red-700" id="sumA">-</td>
                                <td class="p-2.5 text-center text-gray-500" id="sumOFF">-</td>
                                <td class="p-2.5 text-center text-gray-500" id="sumC">-</td>
                                <td class="p-2.5 text-center text-orange-700" id="sumHT">-</td>
                                <td class="p-2.5 text-center text-gray-400" id="sumMin">-</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                <div class="flex items-center justify-between text-[11px] text-gray-500 pt-1">
                    <span>Legenda: H = Hadir Normal, S = Sakit, I = Izin Resmi, A = Alpa Tanpa Keterangan, HT = Hadir Terlambat, (-) = Tidak Hadir Sabtu</span>
                    <span>Sumber: Database Rekap Absensi PT Altri 2026-10</span>
                </div>
            </div>
        </section>

        <!-- PILAR 5: MASUKAN CREW, PENILAIAN, SUPPORT EKSEKUTIF -->
        <section id="pilar5" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Pilar 5</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Masukan Karyawan, Penilaian, dan Dukungan Eksekutif</h2>
                </div>
                <span class="text-xs bg-[#f4e3be] text-[#022020] px-3 py-1 rounded-full font-medium">Suara Kru &amp; Pengambilan Keputusan</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Pilar kelima merangkum laporan hasil evaluasi kinerja Leader Outlet Buah Batu (Ridho Setiawan) setelah menjalani masa evaluasi tiga bulan, kompilasi masukan kru untuk kantor pusat, notulen pertemuan leader ke-6 mengenai komplain dan program pemasaran, serta status pengiriman dividen bulanan bagi para pemegang saham.
            </p>

            <!-- Evaluasi Leader Buah Batu: Ridho Setiawan -->
            <div class="card-custom p-6 space-y-6 bg-gradient-to-br from-white to-[#faf7f0]">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-gray-200 pb-4">
                    <div>
                        <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wide">Evaluasi Masa Percobaan 3 Bulan</span>
                        <h3 class="text-lg font-black text-[#022020]">Ridho Setiawan (Leader Outlet Buah Batu)</h3>
                        <p class="text-xs text-gray-600 mt-0.5">Periode Evaluasi: 11 Juli 2026 – 10 Oktober 2026 | Responden: 12 Kru Buah Batu</p>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="text-right">
                            <p class="text-[11px] text-gray-500 font-medium">Skor Keseluruhan</p>
                            <p class="text-2xl font-black text-[#033f3f]">3,83 <span class="text-xs font-normal text-gray-500">/ 5,00</span></p>
                        </div>
                        <span class="px-3 py-1.5 rounded-xl bg-emerald-100 text-emerald-800 text-xs font-bold border border-emerald-300">Dinyatakan Lolos</span>
                    </div>
                </div>

                <!-- Radar / Bar Chart Evaluasi & Temuan Kualitatif -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-center">
                    <div>
                        <h4 class="text-xs font-bold text-[#022020] uppercase tracking-wide mb-2">Penilaian 10 Aspek Kepemimpinan</h4>
                        <div class="h-72">
                            <canvas id="chartLeaderEval"></canvas>
                        </div>
                    </div>

                    <div class="space-y-4 text-xs">
                        <div class="p-3.5 bg-emerald-50/70 border border-emerald-200 rounded-xl space-y-1">
                            <p class="font-bold text-emerald-900">Kekuatan &amp; Keberhasilan Operasional</p>
                            <p class="text-emerald-800 leading-relaxed">
                                Penurunan komplain tamu terbukti nyata selama tiga bulan. Leader sigap turun ke section kitchen saat kekurangan kru, mengedepankan sikap sopan tanpa senioritas intimidatif, dan memiliki skor tertinggi pada manajemen jadwal kerja adil (4,25).
                            </p>
                        </div>

                        <div class="p-3.5 bg-amber-50/70 border border-amber-200 rounded-xl space-y-1">
                            <p class="font-bold text-amber-900">Celah &amp; Area Perbaikan Lapangan</p>
                            <p class="text-amber-800 leading-relaxed">
                                Terdapat defisit ketegasan saat menegur kru yang melanggar SOP, kebiasaan hanya membaca tanpa membalas perizinan di WhatsApp, pengawasan preparasi bahan crunchy yang kurang teliti sehingga memicu waste, dan skor terendah pada rutinitas briefing mingguan (3,25).
                            </p>
                        </div>

                        <div class="p-3.5 bg-blue-50/70 border border-blue-200 rounded-xl space-y-1">
                            <p class="font-bold text-blue-900">Rekomendasi Kontrak &amp; Penempatan Cabang</p>
                            <p class="text-blue-800 leading-relaxed">
                                Disarankan dikonfirmasi permanen sebagai Leader Outlet tetap di Buah Batu (bukan dipindahkan ke Garut sesuai aspirasi kru), dengan kewajiban mengikuti program Pelatihan Kepemimpinan Lanjutan dari pusat untuk memperkuat ketegasan komunikasi asertif.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Filterable Testimoni Kru Buah Batu: ALL 12 RESPONDENTS -->
                <div class="pt-4 border-t border-gray-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <h4 class="text-xs font-bold text-[#022020] uppercase tracking-wide">Kutipan Asli Seluruh Responden Kru Buah Batu (12 Responden)</h4>
                        <span class="text-[11px] text-gray-500 font-medium">100% Data Masukan Ditampilkan</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                        {leader_feedback_html}
                    </div>
                </div>
            </div>

            <!-- Masukan untuk Manajemen Pusat & Notulen Leader Meeting -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Masukan untuk Manajemen Pusat -->
                <div class="card-custom p-5 space-y-3 flex flex-col justify-between">
                    <div>
                        <h3 class="text-sm font-bold text-[#022020]">Aspirasi Kru untuk Manajemen Pusat</h3>
                        <p class="text-xs text-gray-500">Poin penting koordinasi kantor pusat dan operasional lapangan</p>
                        
                        <div class="mt-4 space-y-3 text-xs">
                            <div class="p-3 bg-[#faf7f0] rounded-xl border-l-4 border-l-[#FBBC05]">
                                <p class="font-bold text-[#022020]">Sinkronisasi Kampanye Promo KOL</p>
                                <p class="text-gray-700 mt-1 leading-relaxed">
                                    Sering timbul kesalahpahaman antara kru kasir dan tamu karena promo Instagram belum disosialisasikan syarat dan ketentuannya ke cabang. Manajemen diwajibkan menyebarkan SOP promo H-2 sebelum publikasi media sosial berjalan.
                                </p>
                            </div>

                            <div class="p-3 bg-[#faf7f0] rounded-xl border-l-4 border-l-[#d6302a]">
                                <p class="font-bold text-[#022020]">Standardisasi Modul Kru Perbantuan</p>
                                <p class="text-gray-700 mt-1 leading-relaxed">
                                    Kru yang diperbantukan sementara ke cabang lain mengeluhkan ketidakjelasan alur tugas serta perlakuan yang kurang elok dari supervisor cabang penerima. Manajemen perlu menerbitkan panduan perbantuan resmi agar instruksi tetap adil dan fokus pada beban kerja yang ditugaskan.
                                </p>
                            </div>
                        </div>
                    </div>
                    <p class="text-[10px] text-gray-400 pt-2 border-t border-gray-100">Sumber: Rekap Kuesioner Evaluasi Balista Buah Batu</p>
                </div>

                <!-- Notulen Leader Meeting Ke-6 -->
                <div class="card-custom p-5 space-y-3 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between">
                            <h3 class="text-sm font-bold text-[#022020]">Notulen Leader Meeting Ke-6</h3>
                            <span class="text-xs bg-[#f4e3be] text-[#033f3f] px-2.5 py-0.5 rounded font-bold">3 Nov 2026</span>
                        </div>
                        <p class="text-xs text-gray-500">Pertemuan di Balista Pajajaran dihadiri direksi dan kasir seluruh cabang</p>

                        <div class="mt-3 space-y-2 text-xs text-gray-700">
                            <div class="p-2.5 bg-red-50 rounded-lg border border-red-200">
                                <p class="font-bold text-[#d6302a]">Tiga Komplain Kritis yang Dievaluasi</p>
                                <ul class="mt-1 space-y-0.5 text-[11px] text-gray-700">
                                    <li>• Setrasari: Salmon memiliki bintik merah, tidak segar, dan berbau</li>
                                    <li>• Buah Batu: Temuan helai rambut pada menu Beef Set</li>
                                    <li>• Tubagus Ismail: Waktu tunggu melampaui batas (1 jam) dan produk datang dalam kondisi gosong</li>
                                </ul>
                            </div>

                            <div class="p-2.5 bg-[#faf7f0] rounded-lg border border-gray-200">
                                <p class="font-bold text-[#022020]">Program Edukasi &amp; Administrasi HR</p>
                                <p class="text-[11px] leading-relaxed mt-0.5">
                                    Kuis dan games simulasi penanganan komplain digelar dengan pemenang Dea (Pajajaran), Cameila (Buah Batu), Pitria (Ambon), Tiara (Kopo), Jamilia (Cihanjuang), Nela (Tubagus), Karlina (Setrasari), Maharani (Amir), Yuli (Kiaracondong), dan Hana (KBP).
                                </p>
                                <p class="text-[11px] text-gray-600 mt-1">
                                    Sosialisasi HR mencakup pencatatan denda dan alpa pada spreadsheet presensi, perbaikan formula lembar kehadiran, serta pemberlakuan resmi formulir invoice baru dari Finance.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="pt-2 border-t border-gray-100 flex items-center justify-between text-xs">
                        <span class="text-gray-500">Dividen Pemegang Saham:</span>
                        <span class="text-[#d6302a] font-bold bg-red-100 px-2 py-0.5 rounded">Tertunda (per 10 Nov belum dikirim)</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- PENUTUP: AKAR MASALAH, SOLUSI, TENGGAT, PENANGGUNG JAWAB -->
        <section id="penutup" class="space-y-6 pt-6">
            <div class="border-b-2 border-[#f2d086] pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                <div>
                    <span class="text-xs font-bold text-[#d6302a] uppercase tracking-wider">Bagian Penutup</span>
                    <h2 class="text-xl font-extrabold text-[#022020]">Matriks Akar Masalah, Solusi Konkret, dan Tindak Lanjut</h2>
                </div>
                <span class="text-xs bg-[#033f3f] text-[#f4e3be] px-3 py-1 rounded-full font-medium">Rencana Aksi Bulan November 2026</span>
            </div>

            <p class="text-sm text-gray-700 leading-relaxed">
                Berdasarkan seluruh temuan evaluasi pada lima pilar personalia, dirumuskan lima aksi perbaikan konkret dengan target tenggat waktu dan penanggung jawab yang terukur di lapangan agar kendala administratif dan operasional tidak berulang pada periode berikutnya.
            </p>

            <div class="card-custom overflow-hidden border border-gray-200">
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-[#022020] text-[#f4e3be]">
                            <tr>
                                <th class="p-3.5 w-1/5">Isu Operasional</th>
                                <th class="p-3.5 w-1/4">Akar Masalah</th>
                                <th class="p-3.5 w-1/3">Solusi Konkret</th>
                                <th class="p-3.5">Tenggat Waktu</th>
                                <th class="p-3.5">Penanggung Jawab</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-200 bg-white text-gray-800">
                            <tr class="hover:bg-[#faf7f0]">
                                <td class="p-3.5 font-bold text-[#d6302a]">Keterlambatan Dividen Investor</td>
                                <td class="p-3.5 text-gray-600">Rekonsiliasi arus kas dan laporan laba rugi bulanan di bagian finance membutuhkan waktu validasi lebih panjang.</td>
                                <td class="p-3.5 text-gray-700">Memprioritaskan closing pembukuan sebelum tanggal 12 dan mengotomatiskan rekonsiliasi transfer investor.</td>
                                <td class="p-3.5 font-semibold text-[#033f3f]">14 November 2026</td>
                                <td class="p-3.5 font-medium">Tasya Urfah &amp; Finance</td>
                            </tr>
                            <tr class="hover:bg-[#faf7f0]">
                                <td class="p-3.5 font-bold text-[#022020]">Miskomunikasi Promo KOL</td>
                                <td class="p-3.5 text-gray-600">Publikasi kampanye media sosial diluncurkan tanpa koordinasi checklist ke kasir dan leader cabang.</td>
                                <td class="p-3.5 text-gray-700">Pemberlakuan SOP broadcast promosi wajib ke seluruh grup leader cabang minimal H-2 sebelum konten tayang.</td>
                                <td class="p-3.5 font-semibold text-[#033f3f]">18 November 2026</td>
                                <td class="p-3.5 font-medium">SPV Marketing &amp; HR Support</td>
                            </tr>
                            <tr class="hover:bg-[#faf7f0]">
                                <td class="p-3.5 font-bold text-[#022020]">Defisit Ketegasan Leader Buah Batu</td>
                                <td class="p-3.5 text-gray-600">Rasa sungkan menegur sesama kru dan belum terbiasa menerapkan gaya komunikasi asertif dalam pengawasan SOP.</td>
                                <td class="p-3.5 text-gray-700">Pemberian modul Leadership Training komunikasi asertif dari HR serta pendampingan langsung oleh SPV area.</td>
                                <td class="p-3.5 font-semibold text-[#033f3f]">25 November 2026</td>
                                <td class="p-3.5 font-medium">HR Training &amp; SPV Area</td>
                            </tr>
                            <tr class="hover:bg-[#faf7f0]">
                                <td class="p-3.5 font-bold text-[#022020]">Keterlambatan Log Absensi Kopo</td>
                                <td class="p-3.5 text-gray-600">Disiplin pencatatan formulir digital presensi harian masih belum terlaksana konsisten di tingkat leader cabang.</td>
                                <td class="p-3.5 text-gray-700">Audit harian secara daring via grup WhatsApp dan peringatan otomatis jika rekap belum diperbarui pada H-3 payroll.</td>
                                <td class="p-3.5 font-semibold text-[#033f3f]">20 November 2026</td>
                                <td class="p-3.5 font-medium">Leader Kopo &amp; HR Personalia</td>
                            </tr>
                            <tr class="hover:bg-[#faf7f0]">
                                <td class="p-3.5 font-bold text-[#022020]">Standardisasi Kru Perbantuan</td>
                                <td class="p-3.5 text-gray-600">Belum adanya lembar instruksi resmi yang merinci batasan peran dan hak operasional tenaga kerja mutasi sementara.</td>
                                <td class="p-3.5 text-gray-700">Penerbitan surat tugas rotasi terpadu lengkap dengan checklist section kerja yang wajib diketahui supervisor penerima.</td>
                                <td class="p-3.5 font-semibold text-[#033f3f]">22 November 2026</td>
                                <td class="p-3.5 font-medium">HR Personalia &amp; Area Manager</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="bg-[#022020] text-[#f4e3be] py-10 mt-16 border-t-4 border-[#f2d086]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6 text-xs">
            <div>
                <p class="font-bold text-base text-[#f2d086] tracking-wide">PT ALTRI / BALISTA SUSHI &amp; TEA</p>
                <p class="text-gray-400 mt-1">Laporan Operasional Human Resources dan Executive Support Periode Oktober 2026</p>
                <p class="text-gray-500 mt-0.5">Disusun sesuai ketentuan baku PANDUAN LAPORAN EXPA dan AGENTS.md</p>
            </div>
            <div class="flex items-center space-x-4">
                <a href="index.html" class="text-[#f4e3be] hover:text-[#f2d086] transition font-medium">Daftar Laporan</a>
                <span class="text-gray-600">|</span>
                <a href="#ringkasan" class="text-[#f2d086] hover:underline font-bold">Kembali ke Atas</a>
            </div>
        </div>
    </footer>

    <!-- JavaScript Data and Interactive Logic -->
    <script>
        // Data Embeds
        const kasbonList = {kasbon_json};
        const attendanceList = {attendance_json};
        const evalCriteria = {eval_criteria_json};
        const outletNames = {outlets_sorted_json};
        const outletSummaryData = {outlet_summary_json};

        // Slider State & Navigation Logic
        let currentCompSlide = 0;
        const totalCompSlides = 4;
        const compSlideTitles = [
            'Slide 1 dari 4: Belanja Payroll & THP',
            'Slide 2 dari 4: Kasbon & Daily Worker',
            'Slide 3 dari 4: Pergerakan Crew & Turnover',
            'Slide 4 dari 4: Kedisiplinan Absensi'
        ];
        let compChartInstances = [];

        function updateCompSlider() {{
            const track = document.getElementById('compSliderTrack');
            if (track) {{
                track.style.transform = 'translateX(-' + (currentCompSlide * 100) + '%)';
            }}
            const badge = document.getElementById('compSlideBadge');
            if (badge) {{
                badge.textContent = compSlideTitles[currentCompSlide] || ('Slide ' + (currentCompSlide + 1) + ' dari ' + totalCompSlides);
            }}
            const btnPrev = document.getElementById('btnPrevComp');
            const btnNext = document.getElementById('btnNextComp');
            const floatBtnPrev = document.getElementById('floatBtnPrev');
            const floatBtnNext = document.getElementById('floatBtnNext');

            if (btnPrev) btnPrev.disabled = (currentCompSlide === 0);
            if (btnNext) btnNext.disabled = (currentCompSlide === totalCompSlides - 1);
            if (floatBtnPrev) floatBtnPrev.disabled = (currentCompSlide === 0);
            if (floatBtnNext) floatBtnNext.disabled = (currentCompSlide === totalCompSlides - 1);

            // Update tab styles
            const tabs = document.querySelectorAll('.comp-tab-btn');
            tabs.forEach((tab, idx) => {{
                if (idx === currentCompSlide) {{
                    tab.className = 'comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-[#033f3f] text-[#f2d086] shadow-sm';
                }} else {{
                    tab.className = 'comp-tab-btn text-xs px-3 py-1.5 rounded-lg font-semibold transition bg-gray-100 text-gray-700 hover:bg-[#f4e3be]';
                }}
            }});

            // Update dot indicators
            const dots = document.querySelectorAll('.comp-dot');
            dots.forEach((dot, idx) => {{
                if (idx === currentCompSlide) {{
                    dot.className = 'comp-dot w-8 h-2 rounded-full bg-[#033f3f] transition-all';
                }} else {{
                    dot.className = 'comp-dot w-2 h-2 rounded-full bg-gray-300 hover:bg-[#a48d5e] transition-all';
                }}
            }});

            // Trigger resize on current active chart
            if (compChartInstances[currentCompSlide]) {{
                setTimeout(() => {{
                    try {{ compChartInstances[currentCompSlide].resize(); }} catch(e) {{}}
                }}, 250);
            }}
        }}

        function prevCompSlide() {{
            if (currentCompSlide > 0) {{
                currentCompSlide--;
                updateCompSlider();
            }}
        }}

        function nextCompSlide() {{
            if (currentCompSlide < totalCompSlides - 1) {{
                currentCompSlide++;
                updateCompSlider();
            }}
        }}

        function goToCompSlide(idx) {{
            if (idx >= 0 && idx < totalCompSlides) {{
                currentCompSlide = idx;
                updateCompSlider();
            }}
        }}

        // Initialize DOM & Charts
        document.addEventListener('DOMContentLoaded', () => {{
            if (typeof AOS !== 'undefined') {{
                AOS.init({{ duration: 600, once: true }});
            }}
            initCharts();
            renderKasbonTable();
            filterAttendanceTable();
            updateCompSlider();
        }});

        function initCharts() {{
            // Helper for safe chart creation
            function createSafeChart(id, config) {{
                const el = document.getElementById(id);
                if (!el) {{
                    console.warn('Canvas not found:', id);
                    return null;
                }}
                try {{
                    return new Chart(el.getContext('2d'), config);
                }} catch (err) {{
                    console.error('Error rendering chart ' + id + ':', err);
                    return null;
                }}
            }}

            // --- 4-MONTH COMPARISON CHARTS (JULI - OKTOBER 2026) ---
            // 1. Chart Compare Payroll & THP
            const chartComp1 = createSafeChart('chartComparePayroll', {{
                type: 'bar',
                data: {{
                    labels: ['Juli 2026', 'Agustus 2026', 'September 2026', 'Oktober 2026'],
                    datasets: [
                        {{
                            label: 'Total Gaji Kotor (Rp)',
                            data: [238646000, 376847343, 370825968, 374321050],
                            backgroundColor: '#a48d5e',
                            borderRadius: 6,
                            order: 2
                        }},
                        {{
                            label: 'Gaji Bersih Diterima (Rp)',
                            data: [195826000, 199224000, 212040000, 214890000],
                            backgroundColor: '#033f3f',
                            borderRadius: 6,
                            order: 3
                        }},
                        {{
                            label: 'Total Personel Kru',
                            data: [138, 140, 146, 148],
                            type: 'line',
                            borderColor: '#d6302a',
                            backgroundColor: '#d6302a',
                            borderWidth: 2,
                            tension: 0.3,
                            yAxisID: 'yCrew',
                            order: 1
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'bottom', labels: {{ boxWidth: 12, font: {{ size: 10, family: 'Poppins' }} }} }},
                        tooltip: {{
                            callbacks: {{
                                label: function(c) {{
                                    if (c.dataset.yAxisID === 'yCrew') {{
                                        return c.dataset.label + ': ' + c.raw + ' orang';
                                    }}
                                    return c.dataset.label + ': Rp ' + c.raw.toLocaleString('id-ID');
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: false,
                            min: 150000000,
                            ticks: {{
                                font: {{ size: 9, family: 'Poppins' }},
                                callback: function(v) {{ return 'Rp ' + (v / 1000000) + ' jt'; }}
                            }}
                        }},
                        yCrew: {{
                            position: 'right',
                            beginAtZero: false,
                            min: 120,
                            max: 160,
                            grid: {{ drawOnChartArea: false }},
                            ticks: {{
                                font: {{ size: 9, family: 'Poppins' }},
                                callback: function(v) {{ return v + ' org'; }}
                            }}
                        }},
                        x: {{ ticks: {{ font: {{ size: 10, family: 'Poppins' }} }} }}
                    }}
                }}
            }});

            // 2. Chart Compare Kasbon & DW
            const chartComp2 = createSafeChart('chartCompareKasbonDW', {{
                type: 'bar',
                data: {{
                    labels: ['Juli 2026', 'Agustus 2026', 'September 2026', 'Oktober 2026'],
                    datasets: [
                        {{
                            label: 'Sisa Pinjaman Kasbon (Rp)',
                            data: [18400000, 19750000, 18300000, 19750000],
                            backgroundColor: '#022020',
                            borderRadius: 6
                        }},
                        {{
                            label: 'Beban Daily Worker (Rp)',
                            data: [1855000, 5250000, 2190000, 565000],
                            backgroundColor: '#FBBC05',
                            borderRadius: 6
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'bottom', labels: {{ boxWidth: 12, font: {{ size: 10, family: 'Poppins' }} }} }},
                        tooltip: {{
                            callbacks: {{
                                label: function(c) {{ return c.dataset.label + ': Rp ' + c.raw.toLocaleString('id-ID'); }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            ticks: {{
                                font: {{ size: 9, family: 'Poppins' }},
                                callback: function(v) {{ return 'Rp ' + (v / 1000000) + ' jt'; }}
                            }}
                        }},
                        x: {{ ticks: {{ font: {{ size: 10, family: 'Poppins' }} }} }}
                    }}
                }}
            }});

            // 3. Chart Compare Turnover
            const chartComp3 = createSafeChart('chartCompareTurnover', {{
                type: 'bar',
                data: {{
                    labels: ['Juli 2026', 'Agustus 2026', 'September 2026', 'Oktober 2026'],
                    datasets: [
                        {{
                            label: 'Kru Baru Masuk',
                            data: [6, 7, 12, 4],
                            backgroundColor: '#34A853',
                            borderRadius: 6
                        }},
                        {{
                            label: 'Kru Resign',
                            data: [5, 6, 3, 5],
                            backgroundColor: '#d6302a',
                            borderRadius: 6
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'bottom', labels: {{ boxWidth: 12, font: {{ size: 10, family: 'Poppins' }} }} }},
                        tooltip: {{
                            callbacks: {{
                                label: function(c) {{ return c.dataset.label + ': ' + c.raw + ' orang'; }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 15,
                            ticks: {{
                                stepSize: 3,
                                font: {{ size: 9, family: 'Poppins' }}
                            }}
                        }},
                        x: {{ ticks: {{ font: {{ size: 10, family: 'Poppins' }} }} }}
                    }}
                }}
            }});

            // 4. Chart Compare Absensi
            const chartComp4 = createSafeChart('chartCompareAbsensi', {{
                type: 'line',
                data: {{
                    labels: ['Juli 2026', 'Agustus 2026', 'September 2026', 'Oktober 2026'],
                    datasets: [
                        {{
                            label: 'Hari Sakit',
                            data: [75, 88, 70, 82],
                            borderColor: '#f2d086',
                            backgroundColor: '#f2d086',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 4
                        }},
                        {{
                            label: 'Hari Izin',
                            data: [72, 64, 58, 43],
                            borderColor: '#4285F4',
                            backgroundColor: '#4285F4',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 4
                        }},
                        {{
                            label: 'Hari Alpa',
                            data: [18, 15, 12, 9],
                            borderColor: '#d6302a',
                            backgroundColor: '#d6302a',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 4
                        }},
                        {{
                            label: 'Hadir Telat (HT)',
                            data: [63, 58, 52, 48],
                            borderColor: '#033f3f',
                            backgroundColor: '#033f3f',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 4
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ position: 'bottom', labels: {{ boxWidth: 12, font: {{ size: 10, family: 'Poppins' }} }} }},
                        tooltip: {{
                            callbacks: {{
                                label: function(c) {{ return c.dataset.label + ': ' + c.raw + ' kejadian/hari'; }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 100,
                            ticks: {{
                                font: {{ size: 9, family: 'Poppins' }}
                            }}
                        }},
                        x: {{ ticks: {{ font: {{ size: 10, family: 'Poppins' }} }} }}
                    }}
                }}
            }});

            compChartInstances = [chartComp1, chartComp2, chartComp3, chartComp4];

            // 5. Chart Pilar 1 (Rencana Aksi Status)
            createSafeChart('chartPilar1', {{
                type: 'doughnut',
                data: {{
                    labels: ['Selesai (Denda Head Bar)', 'Berjalan (Pengawasan SPV)', 'Tertunda (NGOPS & Peer Review)'],
                    datasets: [{{
                        data: [1, 1, 1],
                        backgroundColor: ['#34A853', '#FBBC05', '#d6302a'],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom',
                            labels: {{ boxWidth: 12, font: {{ size: 10, family: 'Poppins' }} }}
                        }}
                    }}
                }}
            }});

            // 6. Chart Kasbon per Outlet (Pilar 2)
            const kasbonOutletMap = {{}};
            kasbonList.forEach(k => {{
                kasbonOutletMap[k.outlet] = (kasbonOutletMap[k.outlet] || 0) + k.acc;
            }});
            const kasbonOutlets = Object.keys(kasbonOutletMap);
            const kasbonValues = kasbonOutlets.map(o => kasbonOutletMap[o]);

            createSafeChart('chartKasbonOutlet', {{
                type: 'bar',
                data: {{
                    labels: kasbonOutlets,
                    datasets: [{{
                        label: 'Nominal ACC Kasbon (Rp)',
                        data: kasbonValues,
                        backgroundColor: '#033f3f',
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        x: {{
                            ticks: {{ font: {{ size: 10, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }},
                        y: {{
                            ticks: {{
                                font: {{ size: 10, family: 'Poppins' }},
                                callback: function(v) {{ return 'Rp ' + (v / 1000000) + ' jt'; }}
                            }},
                            grid: {{ color: '#f0ede6' }}
                        }}
                    }}
                }}
            }});

            // 7. Chart Daily Worker (Pilar 2)
            createSafeChart('chartDailyWorker', {{
                type: 'bar',
                data: {{
                    labels: ['Garut (4 shift)', 'Pajajaran (2 shift)'],
                    datasets: [{{
                        label: 'Realisasi Biaya (Rp)',
                        data: [380000, 185000],
                        backgroundColor: ['#f2d086', '#033f3f'],
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        x: {{
                            ticks: {{ font: {{ size: 10, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }},
                        y: {{
                            beginAtZero: true,
                            ticks: {{
                                font: {{ size: 10, family: 'Poppins' }},
                                callback: function(v) {{ return 'Rp ' + (v / 1000) + ' rb'; }}
                            }},
                            grid: {{ color: '#f0ede6' }}
                        }}
                    }}
                }}
            }});

            // 8. Chart Subsidi Surat Sakit (Pilar 3)
            createSafeChart('chartSuratSakit', {{
                type: 'bar',
                data: {{
                    labels: ['Garut', 'Kopo', 'Amir', 'TKI', 'Dipatiukur', 'Cibiru'],
                    datasets: [{{
                        label: 'Subsidi Surat Sakit (Rp)',
                        data: [450000, 375000, 310000, 280000, 220000, 420000],
                        backgroundColor: '#a48d5e',
                        borderRadius: 6
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        x: {{
                            ticks: {{ font: {{ size: 10, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }},
                        y: {{
                            beginAtZero: true,
                            ticks: {{
                                font: {{ size: 10, family: 'Poppins' }},
                                callback: function(v) {{ return 'Rp ' + (v / 1000) + ' rb'; }}
                            }},
                            grid: {{ color: '#f0ede6' }}
                        }}
                    }}
                }}
            }});

            // 9. Chart Funnel Rekrutmen (Pilar 4)
            createSafeChart('chartFunnel', {{
                type: 'bar',
                data: {{
                    labels: ['Undangan Interview', 'Hadir Interview', 'Lolos Onboarding'],
                    datasets: [{{
                        label: 'Jumlah Kandidat',
                        data: [32, 15, 1],
                        backgroundColor: ['#4285F4', '#FBBC05', '#34A853'],
                        borderRadius: 8
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y',
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        x: {{
                            beginAtZero: true,
                            ticks: {{ font: {{ size: 10, family: 'Poppins' }} }},
                            grid: {{ color: '#f0ede6' }}
                        }},
                        y: {{
                            ticks: {{ font: {{ size: 10, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }}
                    }}
                }}
            }});

            // 10. Chart Presensi Antar Cabang (Pilar 3)
            const hadirData = outletNames.map(o => outletSummaryData[o].h);
            const sakitData = outletNames.map(o => outletSummaryData[o].s);
            const izinData = outletNames.map(o => outletSummaryData[o].i);
            const alpaData = outletNames.map(o => outletSummaryData[o].a);

            createSafeChart('chartAttendanceComparison', {{
                type: 'bar',
                data: {{
                    labels: outletNames,
                    datasets: [
                        {{ label: 'Hadir Normal', data: hadirData, backgroundColor: '#033f3f', stack: 'presensi' }},
                        {{ label: 'Sakit', data: sakitData, backgroundColor: '#FBBC05', stack: 'presensi' }},
                        {{ label: 'Izin', data: izinData, backgroundColor: '#4285F4', stack: 'presensi' }},
                        {{ label: 'Alpa', data: alpaData, backgroundColor: '#d6302a', stack: 'presensi' }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom',
                            labels: {{ boxWidth: 10, font: {{ size: 9, family: 'Poppins' }} }}
                        }}
                    }},
                    scales: {{
                        x: {{
                            stacked: true,
                            ticks: {{ font: {{ size: 9, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }},
                        y: {{
                            stacked: true,
                            ticks: {{ font: {{ size: 9, family: 'Poppins' }} }},
                            grid: {{ color: '#f0ede6' }}
                        }}
                    }}
                }}
            }});

            // 11. Chart Evaluasi Leader Buah Batu (Pilar 5)
            createSafeChart('chartLeaderEval', {{
                type: 'bar',
                data: {{
                    labels: evalCriteria.map(c => c.label),
                    datasets: [{{
                        label: 'Skor Evaluasi (Skala 5.0)',
                        data: evalCriteria.map(c => c.score),
                        backgroundColor: evalCriteria.map(c => c.score >= 4.0 ? '#34A853' : (c.score < 3.5 ? '#d6302a' : '#FBBC05')),
                        borderRadius: 4
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: 'y',
                    plugins: {{
                        legend: {{ display: false }}
                    }},
                    scales: {{
                        x: {{
                            min: 0,
                            max: 5,
                            ticks: {{ font: {{ size: 9, family: 'Poppins' }} }},
                            grid: {{ color: '#f0ede6' }}
                        }},
                        y: {{
                            ticks: {{ font: {{ size: 9, family: 'Poppins' }} }},
                            grid: {{ display: false }}
                        }}
                    }}
                }}
            }});
        }}
        
        
        // Render Kasbon Table with Filter
        function renderKasbonTable() {{
            const selectedOutlet = document.getElementById('filterKasbonOutlet').value;
            const tbody = document.getElementById('kasbonTableBody');
            tbody.innerHTML = '';

            let filtered = kasbonList;
            if (selectedOutlet !== 'ALL') {{
                filtered = kasbonList.filter(k => k.outlet === selectedOutlet);
            }}

            let sumACC = 0;
            let sumPotACC = 0;
            let sumSisa = 0;

            filtered.forEach(k => {{
                sumACC += k.acc;
                sumPotACC += k.pot_acc;
                sumSisa += k.sisa;

                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-50';
                tr.innerHTML = `
                    <td class="p-3 font-medium text-[#022020]">${{k.name}}</td>
                    <td class="p-3"><span class="px-2 py-0.5 rounded bg-gray-100 text-gray-700">${{k.outlet}}</span></td>
                    <td class="p-3 text-right font-semibold text-[#033f3f]">Rp ${{k.acc.toLocaleString('id-ID')}}</td>
                    <td class="p-3 text-right">Rp ${{k.pot_acc.toLocaleString('id-ID')}}</td>
                    <td class="p-3 text-right text-gray-700 font-medium">Rp ${{k.sisa.toLocaleString('id-ID')}}</td>
                    <td class="p-3 text-right text-gray-500">${{k.ajukan > 0 ? 'Rp ' + k.ajukan.toLocaleString('id-ID') : '-'}}</td>
                `;
                tbody.appendChild(tr);
            }});

            document.getElementById('totalKasbonACC').textContent = 'Rp ' + sumACC.toLocaleString('id-ID');
            document.getElementById('totalKasbonPotACC').textContent = 'Rp ' + sumPotACC.toLocaleString('id-ID');
            document.getElementById('totalKasbonSisa').textContent = 'Rp ' + sumSisa.toLocaleString('id-ID');
            document.getElementById('totalKasbonAjukan').textContent = filtered.length + ' Peminjam';
        }}

        // Filter Attendance Table
        function filterAttendanceTable() {{
            const selectedOutlet = document.getElementById('filterAttendanceOutlet').value;
            const searchKeyword = document.getElementById('searchCrewInput').value.toLowerCase().trim();
            const tbody = document.getElementById('attendanceTableBody');
            tbody.innerHTML = '';

            let filtered = attendanceList;
            if (selectedOutlet !== 'ALL') {{
                filtered = filtered.filter(r => r.outlet === selectedOutlet);
            }}
            if (searchKeyword) {{
                filtered = filtered.filter(r => r.name.toLowerCase().includes(searchKeyword));
            }}

            let totH = 0, totS = 0, totI = 0, totA = 0, totOFF = 0, totC = 0, totHT = 0, totMin = 0;

            filtered.forEach((r, idx) => {{
                totH += r.h;
                totS += r.s;
                totI += r.i;
                totA += r.a;
                totOFF += r.off;
                totC += r.c;
                totHT += r.ht;
                totMin += r.min;

                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-50';
                tr.innerHTML = `
                    <td class="p-2.5 text-gray-400 font-mono text-[11px]">${{idx + 1}}</td>
                    <td class="p-2.5 font-medium text-[#022020]">${{r.name}}</td>
                    <td class="p-2.5 text-gray-600">${{r.outlet}}</td>
                    <td class="p-2.5 text-center font-bold text-[#033f3f]">${{r.h}}</td>
                    <td class="p-2.5 text-center ${{r.s > 0 ? 'font-bold text-amber-700 bg-amber-50 rounded' : 'text-gray-400'}}">${{r.s}}</td>
                    <td class="p-2.5 text-center ${{r.i > 0 ? 'font-bold text-blue-700 bg-blue-50 rounded' : 'text-gray-400'}}">${{r.i}}</td>
                    <td class="p-2.5 text-center ${{r.a > 0 ? 'font-bold text-red-700 bg-red-100 rounded' : 'text-gray-400'}}">${{r.a}}</td>
                    <td class="p-2.5 text-center text-gray-500">${{r.off}}</td>
                    <td class="p-2.5 text-center text-gray-500">${{r.c}}</td>
                    <td class="p-2.5 text-center ${{r.ht > 0 ? 'font-bold text-orange-700 bg-orange-50 rounded' : 'text-gray-400'}}">${{r.ht}}</td>
                    <td class="p-2.5 text-center text-gray-400">${{r.min}}</td>
                `;
                tbody.appendChild(tr);
            }});

            document.getElementById('sumH').textContent = totH;
            document.getElementById('sumS').textContent = totS;
            document.getElementById('sumI').textContent = totI;
            document.getElementById('sumA').textContent = totA;
            document.getElementById('sumOFF').textContent = totOFF;
            document.getElementById('sumC').textContent = totC;
            document.getElementById('sumHT').textContent = totHT;
            document.getElementById('sumMin').textContent = totMin;
        }}
    </script>
</body>
</html>
'''

# Write okt26.html
with open('d:/reports/okt26.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("okt26.html written successfully!")
