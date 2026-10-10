from urllib.parse import quote

import pandas as pd
import streamlit as st

# ---- Ubah di sini ----
WHATSAPP = "6285727645913"  # tanpa + dan 0 di depan
EMAIL = ""  # isi untuk menampilkan tombol email, kosongkan untuk menyembunyikan
WA_MESSAGE = "Halo, saya tertarik dengan jasa olah data/dashboard."
BRAND = "Jasa Olah Data"
# ----------------------

st.set_page_config(page_title=f"{BRAND} | Analisis Data & Dashboard", page_icon="📊", layout="centered")

st.markdown(
    """
<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1.5rem; max-width: 860px;}
.brand {color:#0A66C2; font-weight:700; font-size:1.2rem; margin-bottom:12px;}
.hero {background:#0A66C2; color:#fff; border-radius:14px; padding:36px 28px; margin-bottom:8px;}
.hero h1 {color:#fff; font-size:2.3rem; line-height:1.1; margin:0 0 14px; padding:0;}
.hero p {color:#DCEBFA; font-size:1.1rem; margin:0; max-width:36em;}
.price {color:#0A66C2; font-weight:700; text-align:right;}
.small {color:#56687A; font-size:0.85rem;}
.step {color:#0A66C2; font-weight:600; font-size:0.85rem;}
.contact {background:#0A66C2; color:#fff; border-radius:14px; padding:28px; margin-top:8px;}
.contact h2, .contact p {color:#fff; margin:0 0 6px; padding:0;}
</style>
""",
    unsafe_allow_html=True,
)

wa_url = f"https://wa.me/{WHATSAPP}?text={quote(WA_MESSAGE)}"

st.markdown(f'<div class="brand">{BRAND}</div>', unsafe_allow_html=True)

# ---- Hero ----
st.markdown(
    """
<div class="hero">
<h1>Data berantakan jadi keputusan yang jelas.</h1>
<p>Saya analis data berpengalaman. Saya merapikan data, menyusun laporan, dan membangun
dashboard untuk UMKM, startup, dan tim bisnis.</p>
</div>
""",
    unsafe_allow_html=True,
)
st.link_button("Konsultasi lewat WhatsApp", wa_url, type="primary")

# ---- Demo ----
st.subheader("Contoh: data penjualan sebelum dan sesudah dirapikan")
view = st.radio("Tampilan", ["Mentah", "Rapi"], horizontal=True, label_visibility="collapsed")

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
if view == "Mentah":
    css = "background-color:#FFE3B0;color:#6B4200"
    st.table(raw.style.apply(lambda c: [css] * len(c), subset=cols))
else:
    css = "background-color:#DDF3EA;color:#145240"
    st.table(clean.style.apply(lambda c: [css] * len(c), subset=cols))
st.caption("Contoh ilustrasi: duplikat digabung dan format tanggal, nama, serta harga disamakan.")

# ---- Layanan ----
st.subheader("Layanan")
services = [
    ("Data cleaning", "Merapikan data Excel/CSV: duplikat, format tanggal dan angka, serta penulisan yang tidak seragam. Hasilnya siap dianalisis.", "mulai Rp 250 rb", "per file"),
    ("Analisis data & laporan rutin", "Ringkasan KPI, tren, dan temuan untuk pengambilan keputusan. Bisa sekali jadi atau berkala dengan template otomatis.", "mulai Rp 500 rb", "per proyek"),
    ("Dashboard interaktif", "Dashboard di Excel, Power BI, atau Looker Studio dengan KPI utama dan filter. Termasuk panduan singkat dan 2 kali revisi.", "mulai Rp 1,5 jt", "per dashboard"),
    ("Kelas privat Excel & statistik", "Sesi online satu lawan satu, materi disesuaikan dengan level dan kebutuhan kerja Anda.", "mulai Rp 100 rb", "per jam"),
]
for title, desc, price, unit in services:
    with st.container(border=True):
        left, right = st.columns([3, 1])
        left.markdown(f"**{title}**")
        left.write(desc)
        right.markdown(f'<div class="price">{price}<br><span class="small">{unit}</span></div>', unsafe_allow_html=True)
st.caption("Harga final bergantung pada ukuran data dan kompleksitas. Kirim contoh data Anda untuk penawaran yang pasti.")

# ---- Cara kerja ----
st.subheader("Cara kerja")
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

# ---- Tentang ----
st.subheader("Tentang saya")
st.write("Saya analis data dengan pengalaman bertahun-tahun di berbagai industri, dari menyusun laporan rutin dan menganalisis kinerja bisnis sampai membangun dashboard pemantauan.")
st.write("Data klien selalu diperlakukan rahasia. Saya hanya memakai data yang Anda berikan untuk pekerjaan Anda, dan contoh portofolio memakai data sintetis atau publik.")

# ---- Kontak ----
st.markdown(
    '<div class="contact"><h2>Punya data yang perlu dirapikan?</h2>'
    "<p>Kirim contoh datanya. Saya balas dengan perkiraan waktu dan harga.</p></div>",
    unsafe_allow_html=True,
)
c1, c2, _ = st.columns([2, 2, 3])
c1.link_button("Chat WhatsApp", wa_url, type="primary")
if EMAIL:
    c2.link_button("Kirim email", f"mailto:{EMAIL}")

st.caption(f"© 2026 {BRAND}")
