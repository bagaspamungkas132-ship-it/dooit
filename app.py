from urllib.parse import quote

import numpy as np
import pandas as pd
import streamlit as st

# ---- Ubah di sini ----
WHATSAPP = "6285727645913"  # tanpa + dan 0 di depan
EMAIL = ""  # isi untuk menampilkan tombol email
BRAND = "Jasa Olah Data"
BASE = {"Data cleaning": 250_000, "Analisis data & laporan": 500_000, "Dashboard interaktif": 1_500_000}
SIZE = {"Kecil (di bawah 1.000 baris)": 1.0, "Sedang (hingga 50.000 baris)": 1.6, "Besar (di atas 50.000 baris)": 2.5}
RUSH = {"Normal": 1.0, "Cepat (prioritas)": 1.3}
# ----------------------

st.set_page_config(page_title=f"{BRAND} | Analisis Data & Dashboard", page_icon="📊", layout="centered")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
html, body, [class*="css"], .stMarkdown, button {font-family:'Inter',system-ui,sans-serif;}
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding-top:1.5rem; max-width:880px;}
h2 {font-weight:700; letter-spacing:-.01em; margin-top:1.6rem;}
.brand {color:#0A66C2; font-weight:700; font-size:1.2rem; margin-bottom:12px;}
.hero {background:linear-gradient(135deg,#0A66C2 0%,#004182 100%); color:#fff; border-radius:16px; padding:44px 32px; margin-bottom:10px;}
.hero h1 {color:#fff; font-size:2.5rem; line-height:1.1; letter-spacing:-.02em; margin:0 0 14px; padding:0;}
.hero p {color:#DCEBFA; font-size:1.1rem; margin:0; max-width:36em;}
.sub {color:#56687A; margin:-6px 0 14px;}
.price {color:#0A66C2; font-weight:700; text-align:right;}
.small {color:#56687A; font-size:.85rem; font-weight:400;}
.step {color:#0A66C2; font-weight:600; font-size:.85rem;}
.trust {font-weight:600; color:#191919;}
.contact {background:linear-gradient(135deg,#0A66C2 0%,#004182 100%); color:#fff; border-radius:16px; padding:28px; margin-top:12px;}
.contact h2, .contact p {color:#fff; margin:0 0 6px; padding:0;}
div[data-testid="stVerticalBlockBorderWrapper"] {border-radius:12px; transition:box-shadow .2s, transform .2s;}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {box-shadow:0 6px 18px rgba(10,102,194,.15);}
button[role="tab"] {font-weight:600;}
</style>
""",
    unsafe_allow_html=True,
)


def rp(x):
    return "Rp " + f"{int(round(x, -3)):,}".replace(",", ".")


def wa(msg):
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"


@st.cache_data
def sales():
    rng = np.random.default_rng(7)
    price = {"Kopi Susu": 18000, "Teh Tarik": 15000, "Roti Bakar": 22000, "Nasi Goreng": 28000}
    rows = []
    for i, d in enumerate(pd.date_range("2026-06-01", periods=120)):
        for p, pr in price.items():
            q = int(rng.integers(8, 30) + i * 0.08 + (6 if d.dayofweek >= 5 else 0))
            rows.append((d, p, q, q * pr))
    return pd.DataFrame(rows, columns=["Tanggal", "Produk", "Qty", "Omzet"])


st.markdown(f'<div class="brand">{BRAND}</div>', unsafe_allow_html=True)
st.markdown(
    """<div class="hero"><h1>Data berantakan jadi keputusan yang jelas.</h1>
<p>Saya analis data berpengalaman. Saya merapikan data, menyusun laporan, dan membangun
dashboard untuk UMKM, startup, dan tim bisnis.</p></div>""",
    unsafe_allow_html=True,
)
st.link_button("Konsultasi lewat WhatsApp", wa("Halo, saya tertarik dengan jasa olah data/dashboard."), type="primary")

t1, t2, t3 = st.columns(3)
for col, text, desc in [
    (t1, "Revisi hingga 2 kali", "Hasil disesuaikan dengan kebutuhan Anda"),
    (t2, "File bisa diedit sendiri", "Bukan sekadar gambar atau PDF"),
    (t3, "Data dijaga rahasia", "Hanya dipakai untuk pekerjaan Anda"),
]:
    with col.container(border=True):
        st.markdown(f'<div class="trust">{text}</div>', unsafe_allow_html=True)
        st.caption(desc)

# ---- Coba langsung ----
st.markdown("## Coba langsung")
st.markdown('<div class="sub">Tiga contoh singkat agar Anda bisa melihat hasil kerja saya.</div>', unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Sebelum & sesudah", "Dashboard contoh", "Estimasi harga"])

with tab1:
    raw = pd.DataFrame(
        {
            "Tanggal": ["3/10/26", "03-Okt-2026", "2026-10-04", "4 Oktober"],
            "Produk": ["kopi susu ", "Kopi Susu", "teh tarik", "TEH TARIK"],
            "Qty": [2, 2, 1, 1],
            "Harga (Rp)": ["Rp18.000", "18000", "15,000", "15000"],
        }
    )
    clean = pd.DataFrame(
        {
            "Tanggal": ["2026-10-03", "2026-10-04"],
            "Produk": ["Kopi Susu", "Teh Tarik"],
            "Qty": [2, 1],
            "Harga (Rp)": ["18.000", "15.000"],
        }
    )
    cols = ["Tanggal", "Produk", "Harga (Rp)"]
    if st.toggle("Rapikan data ini", value=False):
        css = "background-color:#DDF3EA;color:#145240"
        st.table(clean.style.apply(lambda c: [css] * len(c), subset=cols))
        st.success("4 baris berantakan menjadi 2 baris rapi.")
        st.markdown("- Format tanggal disamakan\n- Huruf besar/kecil dan spasi berlebih dirapikan\n- Format harga diseragamkan\n- Duplikat digabung")
    else:
        css = "background-color:#FFE3B0;color:#6B4200"
        st.table(raw.style.apply(lambda c: [css] * len(c), subset=cols))
        st.caption("Sel kuning menandai masalah: format campur aduk dan duplikat. Aktifkan tombol di atas untuk melihat hasilnya.")

with tab2:
    df = sales()
    a, b = st.columns([2, 3])
    prods = a.multiselect("Produk", sorted(df["Produk"].unique()), default=sorted(df["Produk"].unique()))
    lo, hi = df["Tanggal"].min().date(), df["Tanggal"].max().date()
    start, end = b.slider("Periode", lo, hi, (lo, hi), format="DD MMM")
    f = df[df["Produk"].isin(prods) & df["Tanggal"].dt.date.between(start, end)]
    if f.empty:
        st.info("Pilih minimal satu produk.")
    else:
        daily = f.groupby("Tanggal")["Omzet"].sum()
        by_prod = f.groupby("Produk")["Omzet"].sum()
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Total omzet", rp(f["Omzet"].sum()))
        k2.metric("Terjual", f"{int(f['Qty'].sum()):,}".replace(",", "."))
        k3.metric("Rata-rata harian", rp(daily.mean()))
        k4.metric("Terlaris", by_prod.idxmax())
        st.markdown("**Omzet harian**")
        st.line_chart(daily, color="#0A66C2")
        st.markdown("**Omzet per produk**")
        st.bar_chart(by_prod, color="#0A66C2")
    st.caption("Data sintetis hanya untuk contoh. Dashboard asli dibuat dari data Anda.")

with tab3:
    c1, c2, c3 = st.columns(3)
    svc = c1.selectbox("Layanan", list(BASE))
    size = c2.selectbox("Ukuran data", list(SIZE))
    rush = c3.selectbox("Kecepatan", list(RUSH))
    est = BASE[svc] * SIZE[size] * RUSH[rush]
    st.metric("Perkiraan biaya", f"{rp(est)} - {rp(est * 1.3)}")
    st.caption("Perkiraan awal. Harga final saya konfirmasi setelah melihat contoh data Anda.")
    msg = f"Halo, saya ingin konsultasi: {svc}, data {size}, kecepatan {rush}. Perkiraan {rp(est)} - {rp(est * 1.3)}."
    st.link_button("Kirim detail ini lewat WhatsApp", wa(msg), type="primary")

# ---- Layanan ----
st.markdown("## Layanan")
services = [
    ("Data cleaning", "Merapikan data Excel/CSV: duplikat, format tanggal dan angka, serta penulisan yang tidak seragam. Hasilnya siap dianalisis.", "mulai Rp 250 rb", "per file"),
    ("Analisis data & laporan rutin", "Ringkasan KPI, tren, dan temuan untuk pengambilan keputusan. Bisa sekali jadi atau berkala dengan template otomatis.", "mulai Rp 500 rb", "per proyek"),
    ("Dashboard interaktif", "Dashboard di Excel, Power BI, atau Looker Studio dengan KPI utama dan filter. Termasuk panduan singkat dan 2 kali revisi.", "mulai Rp 1,5 jt", "per dashboard"),
    ("Kelas privat Excel & statistik", "Sesi online satu lawan satu, materi disesuaikan dengan level dan kebutuhan kerja Anda.", "mulai Rp 100 rb", "per jam"),
    ("Pembahasan soal matematika & statistik", "Soal latihan atau tugas dikerjakan langkah demi langkah dengan penjelasan di setiap langkah, supaya Anda paham caranya, bukan hanya mendapat jawaban.", "mulai Rp 50 rb", "per soal"),
]
for title, desc, price, unit in services:
    with st.container(border=True):
        left, right = st.columns([3, 1])
        left.markdown(f"**{title}**")
        left.write(desc)
        right.markdown(f'<div class="price">{price}<br><span class="small">{unit}</span></div>', unsafe_allow_html=True)

with st.expander("Lihat contoh pembahasan soal matematika"):
    st.markdown("**Soal:** Tentukan turunan dari")
    st.latex(r"f(x) = x^2 \sin x")
    st.markdown("**Langkah 1.** Fungsi ini adalah hasil kali dua fungsi, jadi pakai aturan hasil kali:")
    st.latex(r"(uv)' = u'v + uv'")
    st.markdown("**Langkah 2.** Misalkan u = x² dan v = sin x, maka:")
    st.latex(r"u' = 2x, \quad v' = \cos x")
    st.markdown("**Langkah 3.** Masukkan ke aturan hasil kali:")
    st.latex(r"f'(x) = 2x \sin x + x^2 \cos x")
    st.caption("Setiap jawaban disertai alasan di balik tiap langkah, bukan hanya hasil akhirnya.")

# ---- Cara kerja ----
st.markdown("## Cara kerja")
steps = [
    ("Ceritakan kebutuhan", "Kirim data contoh dan tujuan Anda lewat WhatsApp."),
    ("Terima penawaran", "Ruang lingkup, harga, dan waktu disepakati di awal."),
    ("Pengerjaan & revisi", "Anda menerima hasil awal, lalu revisi sesuai kesepakatan."),
    ("Serah terima", "File editable dan panduan singkat memakainya."),
]
for col, (i, (title, desc)) in zip(st.columns(4), enumerate(steps, 1)):
    with col.container(border=True):
        st.markdown(f'<div class="step">Langkah {i}</div>', unsafe_allow_html=True)
        st.markdown(f"**{title}**")
        st.caption(desc)

# ---- FAQ ----
st.markdown("## Pertanyaan yang sering diajukan")
faqs = [
    ("Berapa lama pengerjaannya?", "Tergantung ukuran dan kompleksitas data. Data kecil biasanya selesai dalam beberapa hari. Waktu pasti saya sampaikan di penawaran."),
    ("Apakah data saya aman?", "Data hanya dipakai untuk pekerjaan Anda dan tidak dibagikan ke pihak lain. Anda juga boleh mengirim data yang sudah disamarkan."),
    ("Saya tidak punya data yang rapi. Apakah tetap bisa?", "Bisa. Data berantakan justru kasus yang paling sering saya tangani. Kirim contohnya dan saya beri gambaran apa yang bisa dilakukan."),
    ("Bagaimana pembayarannya?", "Pembayaran dibicarakan di penawaran, umumnya sebagian di awal dan sisanya setelah serah terima."),
    ("Apakah menerima soal ujian atau skripsi?", "Saya membantu membahas dan menjelaskan soal latihan, tugas, dan konsep agar Anda paham. Saya tidak menerima joki ujian atau pengerjaan skripsi untuk diserahkan sebagai karya sendiri."),
]
for q, ans in faqs:
    with st.expander(q):
        st.write(ans)

# ---- Tentang ----
st.markdown("## Tentang saya")
st.write("Saya analis data dengan pengalaman bertahun-tahun di berbagai industri, dari menyusun laporan rutin dan menganalisis kinerja bisnis sampai membangun dashboard pemantauan.")

# ---- Kontak ----
st.markdown(
    '<div class="contact"><h2>Punya data yang perlu dirapikan?</h2>'
    "<p>Kirim contoh datanya. Saya balas dengan perkiraan waktu dan harga.</p></div>",
    unsafe_allow_html=True,
)
c1, c2, _ = st.columns([2, 2, 3])
c1.link_button("Chat WhatsApp", wa("Halo, saya tertarik dengan jasa olah data/dashboard."), type="primary")
if EMAIL:
    c2.link_button("Kirim email", f"mailto:{EMAIL}")
st.caption(f"© 2026 {BRAND}")
