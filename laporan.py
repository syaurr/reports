import os

# Menyiapkan konten HTML
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HR Strategic Report 2026</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1e293b;
            --secondary: #3b82f6;
            --accent: #f59e0b;
            --danger: #ef4444;
            --success: #10b981;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #334155;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }

        header {
            height: 60vh;
            background: linear-gradient(135deg, var(--primary) 0%, #0f172a 100%);
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            letter-spacing: -1px;
        }

        header p {
            font-weight: 300;
            opacity: 0.8;
            max-width: 600px;
        }

        .container {
            max-width: 1000px;
            margin: -50px auto 50px;
            padding: 0 20px;
        }

        section {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #e2e8f0;
        }

        h2 {
            color: var(--primary);
            font-size: 1.8rem;
            margin-bottom: 25px;
            border-left: 5px solid var(--secondary);
            padding-left: 15px;
        }

        h3 {
            margin-top: 25px;
            color: var(--secondary);
            font-size: 1.3rem;
            margin-bottom: 15px;
        }

        p {
            margin-bottom: 15px;
        }

        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
            margin-top: 20px;
        }

        .metric-card {
            background: #f1f5f9;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--primary);
            display: block;
        }

        .metric-label {
            font-size: 0.85rem;
            color: #64748b;
            text-transform: uppercase;
        }

        .chart-container {
            position: relative;
            margin: auto;
            height: 300px;
            width: 100%;
        }

        .alert-box {
            background: #fff1f2;
            border-left: 4px solid var(--danger);
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }

        .success-box {
            background: #f0fdf4;
            border-left: 4px solid var(--success);
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9rem;
        }

        th, td {
            text-align: left;
            padding: 12px;
            border-bottom: 1px solid #e2e8f0;
        }

        th {
            background-color: #f8fafc;
            color: var(--primary);
        }

        .footer {
            background: var(--primary);
            color: white;
            padding: 60px 20px;
            text-align: center;
        }

        .plan-item {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
            text-align: left;
            border-left: 3px solid var(--accent);
        }

        @media (max-width: 768px) {
            .grid { grid-template-columns: 1fr; }
            header h1 { font-size: 1.8rem; }
        }

        .scroll-indicator {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: var(--secondary);
            z-index: 1000;
            width: 0%;
        }
    </style>
</head>
<body>

<div class="scroll-indicator" id="progressBar"></div>

<header>
    <p>LAPORAN STRATEGIS SDM</p>
    <h1>Analisis Efisiensi & Risiko Operasional</h1>
    <p>Periode Februari - April 2026 | PT Altri Sejahtera Indonesia</p>
</header>

<div class="container">

    <section>
        <h2>1. Analisis Rekrutmen & Biaya Kekosongan</h2>
        <p>Meskipun minat pelamar sangat tinggi (ToFu), kita menghadapi tantangan besar pada penyaringan kualitas dan kecepatan konversi.</p>
        
        <div class="grid">
            <div class="metric-card">
                <span class="metric-value">1.700+</span>
                <span class="metric-label">Total Pelamar (Feb-Apr)</span>
            </div>
            <div class="metric-card">
                <span class="metric-value">137</span>
                <span class="metric-label">Kandidat Ghosting (Maret-April)</span>
            </div>
        </div>

        <h3>Visualisasi Funnel Rekrutmen</h3>
        <div class="chart-container">
            <canvas id="funnelChart"></canvas>
        </div>

        <div class="alert-box">
            <strong>Red Flag:</strong> Faktor eliminasi terbesar adalah <b>"Pengalaman Tidak Sesuai"</b> (323 orang di Feb-Mar, 244 di April). Ini menandakan iklan kita menarik audiens yang salah (Untargeted Audience).
        </div>

        <h3>Biaya Kekosongan Posisi (Cost of Vacancy)</h3>
        <p>Setiap satu posisi Barista/Crew yang kosong selama 14 hari kerja menimbulkan kerugian sebesar:</p>
        <div class="metric-card" style="background: #fee2e2;">
            <span class="metric-value" style="color: var(--danger);">Rp 1.755.376</span>
            <span class="metric-label">Kerugian per Posisi / 14 Hari</span>
        </div>
        
        <h3>Efisiensi Training per Cabang</h3>
        <table>
            <tr><th>Cabang</th><th>Undangan</th><th>Sukses</th><th>Rasio</th></tr>
            <tr><td>Kiaracondong</td><td>11</td><td>2</td><td>18%</td></tr>
            <tr><td>Tubagus Ismail</td><td>9</td><td>3</td><td>33%</td></tr>
            <tr><td>Cihanjuang</td><td>5</td><td>1</td><td>20%</td></tr>
        </table>

        <div class="alert-box">
            <strong>Risiko Kepatuhan:</strong> Ditemukan celah fatal pada <i>Background Check</i>. Contoh: a.n. Muhammad Rafie menyerahkan SKCK setelah 3 bulan 30 hari bekerja. Ini mengekspos perusahaan pada risiko <b>Negligent Hiring</b>.
        </div>
    </section>

    <section>
        <h2>2. Budaya Kerja & Hubungan Karyawan</h2>
        <p>Data menunjukkan adanya ancaman disintegrasi budaya di beberapa titik outlet yang memerlukan intervensi segera.</p>
        
        <div class="grid">
            <div>
                <h3>Kasus Soreang: Nepotisme</h3>
                <p>Adanya hubungan kakak-beradik dalam satu shift yang mendominasi jadwal dan melangkahi wewenang Leader. Hal ini merusak <i>Psychological Safety</i> tim lainnya.</p>
            </div>
            <div>
                <h3>Ambon & Pajajaran: Keadilan</h3>
                <p>Ketimpangan sanksi aturan berpacaran. <b>Agil</b> dimutasi (rugi finansial), sementara <b>Rahma & Rafi</b> tetap di lokasi tanpa sanksi. Ini memicu <i>Cognitive Dissonance</i> (rasa tidak adil).</p>
            </div>
        </div>

        <div class="alert-box" style="background: #fff7ed; border-color: var(--accent);">
            <strong>Silo Effect:</strong> Miskomunikasi antara Marketing (Instagram) dan Operasional soal Voucher Grab membuat staf lapangan menjadi sasaran kemarahan konsumen (Customer Abuse).
        </div>
    </section>

    <section>
        <h2>3. Keandalan Finansial & Payroll</h2>
        
        <div class="success-box">
            <strong>Pencapaian:</strong> Rasio <b>Zero Error</b> pada penggajian bulan Maret untuk seluruh Daily Worker & Full-Time. Lead-time selesai dalam 1 hari kerja.
        </div>

        <h3>Ledakan Kasbon (Liquidity Risk)</h3>
        <p>Terjadi lonjakan drastis permintaan pinjaman pada bulan April, kemungkinan besar karena kebutuhan hari raya.</p>
        <div class="chart-container">
            <canvas id="kasbonChart"></canvas>
        </div>

        <table>
            <tr><th>Metrik Kasbon</th><th>Maret</th><th>April</th><th>Eskalasi</th></tr>
            <tr><td>Total Pengaju</td><td>16 Orang</td><td>31 Orang</td><td>+93.7%</td></tr>
            <tr><td>Nominal Diajukan</td><td>Rp 9.350.000</td><td>Rp 32.350.000</td><td>+345.9%</td></tr>
            <tr><td>Nominal Disetujui</td><td>Rp 7.300.000</td><td>Rp 12.500.000</td><td>+71.2%</td></tr>
        </table>
    </section>

    <section>
        <h2>4. Infrastruktur IT & Proyek KBP</h2>
        <p>Operasional mulai bergeser ke digital dengan 25 deployment aktif, namun ada kendala di level eksekutif.</p>
        
        <div class="alert-box">
            <strong>Delay Eksekutif:</strong> Laporan Dividen Investor terlambat 6 hari (Deadline 10 April, baru terkirim 16 April).
        </div>

        <h3>Evaluasi Optimasi Kopi Priangan (KBP)</h3>
        <p>Kondisi: <b>"System-Ready but Resource-Starved"</b></p>
        <table>
            <tr><th>Status</th><th>Kondisi Riil</th></tr>
            <tr><td>Administrasi (SOP)</td><td><span style="color: var(--success);">✔ Sudah Jalan & Rutin (Skor 4-5)</span></td></tr>
            <tr><td>Fasilitas Fisik</td><td><span style="color: var(--danger);">✘ Tidak Ada Mesin Kopi, Grinder, Mixer, Roti</span></td></tr>
        </table>
        <p>Kru dipaksa menghafal SOP menu inovasi (Peach Americano, Eskosu Creamy) tanpa alat produksi yang memadai. Akibatnya, skor penerimaan pelanggan jatuh ke angka 1-2.</p>
    </section>

</div>

<footer class="footer">
    <div class="container" style="margin-top: 0; background: transparent; box-shadow: none; border: none;">
        <h2 style="color: white; border: none; text-align: center;">Master Action Plan 2026</h2>
        
        <div class="plan-item">
            <strong>1. Anti-Nepotism Policy:</strong> Larangan keras keluarga inti (kakak-adik/pasangan) berada dalam satu outlet/shift. Mutasi permanen segera untuk kasus Soreang.
        </div>
        <div class="plan-item">
            <strong>2. Zero-Tolerance SKCK:</strong> SKCK menjadi syarat mutlak H-1 masuk kerja. Tidak ada toleransi keterlambatan untuk akses area operasional.
        </div>
        <div class="plan-item">
            <strong>3. Blind Justice (Equity):</strong> Eksekusi proses indisipliner untuk pasangan di outlet Ambon guna memulihkan kewibawaan HR.
        </div>
        <div class="plan-item">
            <strong>4. Project Reset (KBP):</strong> Bekukan KPI Penjualan KBP hingga seluruh perangkat keras standar Pajajaran terpasang utuh.
        </div>
        <div class="plan-item">
            <strong>5. Smart Filtering:</strong> Ubah copywriting iklan dengan pertanyaan "knock-out" pengalaman minimal untuk mengurangi beban administrasi.
        </div>

        <p style="font-size: 0.8rem; opacity: 0.6; margin-top: 40px;">
            Referensi: UMK Bandung 2026, Dr. John Sullivan (Cost of Vacancy), Adams' Equity Theory, Internal Data Maret-April.
        </p>
    </div>
</footer>

<script>
    // Progress Bar
    window.onscroll = function() {
        let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        let scrolled = (winScroll / height) * 100;
        document.getElementById("progressBar").style.width = scrolled + "%";
    };

    // Funnel Chart
    const funnelCtx = document.getElementById('funnelChart').getContext('2d');
    new Chart(funnelCtx, {
        type: 'bar',
        data: {
            labels: ['Total Pelamar', 'Screening Tahap 1', 'Kandidat Layak (Pool)'],
            datasets: [{
                label: 'Feb-Mar',
                data: [962, 474, 388],
                backgroundColor: '#1e293b'
            }, {
                label: 'April',
                data: [738, 380, 314],
                backgroundColor: '#3b82f6'
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });

    // Kasbon Chart
    const kasbonCtx = document.getElementById('kasbonChart').getContext('2d');
    new Chart(kasbonCtx, {
        type: 'line',
        data: {
            labels: ['Maret', 'April'],
            datasets: [{
                label: 'Nominal Diajukan (Juta Rp)',
                data: [9.35, 32.35],
                borderColor: '#ef4444',
                tension: 0.1,
                fill: false
            }, {
                label: 'Nominal Disetujui (Juta Rp)',
                data: [7.3, 12.5],
                borderColor: '#10b981',
                tension: 0.1,
                fill: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true }
            },
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
</script>

</body>
</html>
"""

# Menulis konten ke file .html
file_path = "HR_Strategic_Report_2026.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File berhasil dibuat: {file_path}")