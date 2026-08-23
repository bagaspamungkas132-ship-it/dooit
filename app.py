import pandas as pd
import plotly.express as px
import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Dooit | Data Analysis & Visualization",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="auto",
)

WHATSAPP_NUMBER = "6285727645913"

SERVICE_LIST = [
    {
        "title": "Olah Data",
        "label": "Data Processing / Data Analysis",
        "price": "Rp 200.000",
        "icon": "🧹",
        "message": "Halo, saya ingin memesan paket Olah Data seharga Rp 200.000.",
        "bullets": [
            "Membersihkan data dari duplikasi, error, dan format tidak konsisten.",
            "Menyusun tabel, ringkasan, dan hasil analisis yang rapi untuk kebutuhan harian.",
            "Menggunakan Excel, Python, dan Pandas untuk transformasi data yang cepat dan akurat.",
            "Menyediakan file siap pakai untuk laporan, evaluasi, dan keputusan bisnis.",
        ],
    },
    {
        "title": "Visualisasi Data",
        "label": "Data Visualization",
        "price": "Rp 300.000",
        "icon": "📊",
        "message": "Halo, saya ingin memesan paket Visualisasi Data seharga Rp 300.000.",
        "bullets": [
            "Membuat dashboard dan chart interaktif yang mudah dibaca oleh tim maupun atasan.",
            "Menggunakan Looker Studio, Metabase, atau Plotly sesuai kebutuhan dan target audiens.",
            "Menyajikan KPI dan tren data secara jelas untuk presentasi dan monitoring.",
            "Hasil visual siap pakai untuk laporan, rapat, atau kebutuhan publikasi internal.",
        ],
    },
    {
        "title": "Otomasi Excel / Sheets",
        "label": "Excel / Google Sheets Automation",
        "price": "Rp 250.000",
        "icon": "⚙️",
        "message": "Halo, saya ingin memesan paket Otomasi Excel / Sheets seharga Rp 250.000.",
        "bullets": [
            "Membuat formula rumit, pivot table, dan logika otomatis untuk pekerjaan berulang.",
            "Mengurangi waktu kerja manual di spreadsheet dan meminimalkan kesalahan input.",
            "Menyusun workflow otomatis di Google Sheets dan Excel untuk proses yang lebih cepat.",
            "Cocok untuk laporan rutin, dashboard ringan, dan tugas administrasi berulang.",
        ],
    },
    {
        "title": "Query & Ekstraksi Data SQL",
        "label": "SQL Query & Data Extraction",
        "price": "Rp 200.000",
        "icon": "🧠",
        "message": "Halo, saya ingin memesan paket Query & Ekstraksi Data SQL seharga Rp 200.000.",
        "bullets": [
            "Menulis query SQL untuk mengambil, menggabung, dan membersihkan data dari database.",
            "Mempersiapkan extract bersih yang siap dipelajari, dianalisis, atau dipresentasikan.",
            "Mendukung PostgreSQL, BigQuery, dan sumber data lain yang umum digunakan.",
            "Menghasilkan table siap pakai untuk kebutuhan analisis atau pelaporan.",
        ],
    },
    {
        "title": "Laporan Otomatis Terjadwal",
        "label": "Automated Scheduled Reporting",
        "price": "Rp 250.000",
        "icon": "⏰",
        "message": "Halo, saya ingin memesan paket Laporan Otomatis Terjadwal seharga Rp 250.000.",
        "bullets": [
            "Menyusun laporan harian, mingguan, atau bulanan yang berjalan otomatis tanpa input manual.",
            "Menghubungkan data terbaru ke file Excel, email, atau dashboard yang dibutuhkan tim.",
            "Memanfaatkan Google Apps Script atau Python sesuai kebutuhan dan sistem yang ada.",
            "Membantu tim menghemat waktu dan fokus pada keputusan, bukan pekerjaan berulang.",
        ],
    },
]


def build_whatsapp_link(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #F8FAFC;
                --surface: #FFFFFF;
                --navy: #0F172A;
                --accent: #2563EB;
                --success: #25D366;
                --muted: #475569;
                --line: #E2E8F0;
            }

            html, body, .stApp {
                background: linear-gradient(180deg, #F8FAFC 0%, #EEF6FF 100%);
                color: var(--navy);
            }

            .block-container {
                max-width: 1200px;
                padding-top: 1rem;
                padding-bottom: 2rem;
            }

            section[data-testid="stSidebar"] {
                background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
                border-right: 1px solid rgba(148, 163, 184, 0.25);
            }

            section[data-testid="stSidebar"] .stRadio,
            section[data-testid="stSidebar"] label,
            section[data-testid="stSidebar"] p,
            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2,
            section[data-testid="stSidebar"] h3,
            section[data-testid="stSidebar"] span {
                color: #F8FAFC;
            }

            section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {
                color: #F8FAFC;
                background: rgba(15, 23, 42, 0.35);
                border-radius: 999px;
            }

            [data-testid="stVerticalBlockBorderWrapper"] {
                background: var(--surface);
                border: 1px solid var(--line) !important;
                border-radius: 22px;
                box-shadow: 0 14px 32px rgba(15, 23, 42, 0.07);
                padding: 1.1rem;
                margin-bottom: 1rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            [data-testid="stVerticalBlockBorderWrapper"]:hover {
                transform: translateY(-2px);
                box-shadow: 0 18px 34px rgba(15, 23, 42, 0.1);
            }

            .section-heading {
                margin-bottom: 0.25rem;
                font-size: 2.2rem;
                font-weight: 800;
                line-height: 1.2;
                color: var(--navy);
            }

            .section-copy {
                margin-bottom: 1rem;
                color: var(--muted);
                line-height: 1.7;
            }

            .eyebrow {
                display: inline-block;
                background: rgba(37, 99, 235, 0.08);
                color: var(--accent);
                border-radius: 999px;
                font-size: 0.77rem;
                font-weight: 800;
                letter-spacing: 0.02em;
                padding: 0.38rem 0.72rem;
                margin-bottom: 0.8rem;
            }

            .hero-title {
                font-size: 2.6rem;
                line-height: 1.08;
                font-weight: 800;
                color: var(--navy);
                margin: 0.25rem 0 0.9rem;
            }

            .hero-copy {
                font-size: 1.07rem;
                color: var(--muted);
                line-height: 1.75;
                margin-bottom: 1rem;
            }

            .stat-pill {
                display: inline-flex;
                align-items: center;
                padding: 0.38rem 0.8rem;
                margin: 0.2rem 0.45rem 0.2rem 0;
                border-radius: 999px;
                background: #EEF6FF;
                color: var(--accent);
                font-size: 0.8rem;
                font-weight: 700;
            }

            .service-icon {
                font-size: 1.2rem;
                margin-right: 0.3rem;
            }

            .service-name {
                margin-top: 0.2rem;
                margin-bottom: 0.6rem;
                font-size: 1.35rem;
                font-weight: 800;
                color: var(--navy);
            }

            .service-price {
                color: var(--accent);
                font-size: 1.7rem;
                font-weight: 800;
                margin: 0.35rem 0 0.9rem;
            }

            .service-list {
                margin: 0 0 1rem;
                padding-left: 1.1rem;
                color: var(--muted);
                line-height: 1.6;
            }

            .service-list li {
                margin-bottom: 0.34rem;
            }

            .metric-box {
                padding: 0.8rem 0.9rem;
                border-radius: 16px;
                background: #F8FAFC;
                border: 1px solid var(--line);
                color: var(--navy);
                margin: 0.4rem 0;
                font-weight: 600;
            }

            .mini-title {
                font-size: 1.05rem;
                font-weight: 700;
                margin: 0.2rem 0 0.6rem;
            }

            .quote {
                color: var(--muted);
                font-style: italic;
                line-height: 1.7;
                margin: 0.5rem 0;
            }

            div[data-testid="stLinkButton"] a,
            div[data-testid="stButton"] button,
            div[data-testid="stFormSubmitButton"] button {
                width: 100%;
                border: none;
                border-radius: 999px;
                background: linear-gradient(135deg, #25D366 0%, #1CB75B 100%);
                color: #ffffff;
                font-weight: 800;
                padding: 0.82rem 1rem;
                box-shadow: 0 12px 24px rgba(37, 211, 102, 0.25);
                text-decoration: none;
            }

            div[data-testid="stLinkButton"] a:hover,
            div[data-testid="stButton"] button:hover,
            div[data-testid="stFormSubmitButton"] button:hover {
                filter: brightness(0.98);
                box-shadow: 0 12px 26px rgba(37, 211, 102, 0.32);
            }

            .footer-card {
                margin-top: 2rem;
                padding: 1.1rem 1.2rem;
                border-radius: 18px;
                background: #0F172A;
                color: #E2E8F0;
                text-align: center;
                line-height: 1.7;
            }

            @media (max-width: 768px) {
                .block-container {
                    padding-left: 0.6rem;
                    padding-right: 0.6rem;
                }

                .hero-title {
                    font-size: 2rem;
                }

                .section-heading {
                    font-size: 1.7rem;
                }

                .section-copy {
                    font-size: 0.96rem;
                }

                [data-testid="stVerticalBlockBorderWrapper"] {
                    padding: 0.9rem;
                    border-radius: 18px;
                }

                div[data-testid="stHorizontalBlock"] {
                    display: block !important;
                }

                div[data-testid="stHorizontalBlock"] > div {
                    width: 100% !important;
                    max-width: 100% !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_home() -> None:
    st.markdown("<div class='eyebrow'>📈 DATA ANALYSIS • DATA VISUALIZATION • RAPID DELIVERY</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Bantu bisnis Anda mengambil keputusan lebih cepat lewat data yang rapi dan jelas.</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='hero-copy'>Saya membantu UMKM, tim operasional, dan bisnis yang ingin lebih cepat mengambil keputusan dengan data yang bersih, terstruktur, dan mudah dipahami. Layanan yang saya tawarkan mencakup analisis data, visualisasi, spreadsheet automation, SQL extraction, serta laporan otomatis yang hemat waktu.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class='stat-pill'>Excel • Google Sheets</div><div class='stat-pill'>Python • SQL</div><div class='stat-pill'>Looker Studio • Metabase</div>",
        unsafe_allow_html=True,
    )

    st.link_button(
        "📲 Konsultasi via WhatsApp",
        build_whatsapp_link("Halo, saya ingin konsultasi paket data analysis dan visualisasi."),
        use_container_width=True,
    )

    with st.container(border=True):
        st.markdown("<div class='mini-title'>Manfaat yang bisa Anda dapatkan</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>✅ Data dibersihkan dan disusun rapi agar mudah dianalisis</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>📊 Visual dashboard dan chart yang mudah dipahami tim dan atasan</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-box'>🔒 Proses cepat, aman, dan siap dipakai untuk kebutuhan rutin</div>", unsafe_allow_html=True)


def render_services() -> None:
    st.markdown("<div class='section-heading'>Layanan yang tersedia</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Pilih paket yang paling sesuai dengan kebutuhan Anda. Setiap layanan dapat disesuaikan dengan tingkat kompleksitas, format file, dan deadline kerja.</div>",
        unsafe_allow_html=True,
    )

    for index in range(0, len(SERVICE_LIST), 2):
        cols = st.columns(2, gap="large")
        for offset, column in enumerate(cols):
            service = SERVICE_LIST[index + offset] if index + offset < len(SERVICE_LIST) else None
            if service is None:
                continue
            with column:
                with st.container(border=True):
                    st.markdown(
                        f"<div class='eyebrow'><span class='service-icon'>{service['icon']}</span>{service['title']}</div>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"<div class='service-name'>{service['label']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='service-price'>{service['price']}</div>", unsafe_allow_html=True)
                    st.markdown(
                        "<ul class='service-list'>" + "".join(f"<li>{item}</li>" for item in service["bullets"]) + "</ul>",
                        unsafe_allow_html=True,
                    )
                    st.link_button(
                        "🛒 Order via WhatsApp",
                        build_whatsapp_link(service["message"]),
                        use_container_width=True,
                    )


def render_portfolio() -> None:
    st.markdown("<div class='section-heading'>Portfolio & Contoh Hasil</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Berikut contoh visual dan hasil yang sering saya buat untuk kebutuhan operasional dan analisis bisnis.</div>",
        unsafe_allow_html=True,
    )

    sample_df = pd.DataFrame(
        {
            "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
            "Penjualan": [120, 140, 132, 160, 175, 190],
            "Target": [110, 130, 135, 150, 165, 180],
        }
    )

    chart = px.line(
        sample_df,
        x="Bulan",
        y=["Penjualan", "Target"],
        markers=True,
        color_discrete_sequence=["#2563EB", "#22C55E"],
    )
    chart.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="#F8FAFC",
        margin=dict(l=18, r=18, t=18, b=18),
        legend_title_text="",
        height=320,
    )

    left_col, right_col = st.columns([1.2, 0.9], gap="large")
    with left_col:
        with st.container(border=True):
            st.markdown("<div class='eyebrow'>📈 Sample Dashboard</div>", unsafe_allow_html=True)
            st.plotly_chart(chart, use_container_width=True)
    with right_col:
        with st.container(border=True):
            st.markdown("<div class='eyebrow'>🧼 Before & After</div>", unsafe_allow_html=True)
            st.markdown("<div class='mini-title'>Sebelum</div>", unsafe_allow_html=True)
            st.code("Nama, Kota, Penjualan\nAdit, Jakarta, 100000\nAdit, Jakarta, 100000\nBudi, Bandung, 150000")
            st.markdown("<div class='mini-title'>Sesudah</div>", unsafe_allow_html=True)
            st.code("Nama,Kota,Penjualan\nAdit,Jakarta,100000\nBudi,Bandung,150000")


def render_how_it_works() -> None:
    st.markdown("<div class='section-heading'>Bagaimana prosesnya?</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Proses yang sederhana, transparan, dan cepat agar Anda tidak perlu menghabiskan waktu untuk tugas data yang berulang.</div>",
        unsafe_allow_html=True,
    )

    steps = [
        ("1. Konsultasi", "Ceritakan kebutuhan, target, dan jenis file yang ingin diolah."),
        ("2. Kirim Data", "Upload file Excel, CSV, atau data mentah yang ingin dibersihkan."),
        ("3. Proses", "Saya lakukan cleaning, transformasi, analisis, dan visualisasi sesuai kebutuhan."),
        ("4. Delivery", "Hasil dikirim dalam format yang siap dipakai dan bisa direvisi jika perlu."),
    ]

    step_cols = st.columns(4, gap="small")
    for index, (title, description) in enumerate(steps):
        with step_cols[index]:
            with st.container(border=True):
                st.markdown(f"<div class='eyebrow'>{title}</div>", unsafe_allow_html=True)
                st.write(description)


def render_testimonials() -> None:
    st.markdown("<div class='section-heading'>Testimoni Sampel</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Berikut contoh testimoni placeholder yang dapat Anda ganti dengan pengalaman klien nyata di kemudian hari.</div>",
        unsafe_allow_html=True,
    )

    testimonials = [
        ("Rina", "Founder UMKM", "Proses cepat, hasil rapi, dan sangat membantu untuk laporan bulanan kami.", "★★★★★"),
        ("Dwiki", "Tim Operasional", "Dashboard yang dibuat jelas, mudah dibaca, dan sangat membantu presentasi ke atasan.", "★★★★★"),
        ("Sari", "Admin Finance", "Data jadi lebih teratur dan saya tidak perlu mengerjakan ulang pekerjaan manual setiap minggu.", "★★★★☆"),
    ]

    cols = st.columns(3, gap="large")
    for index, (name, role, quote, rating) in enumerate(testimonials):
        with cols[index]:
            with st.container(border=True):
                st.markdown(f"<div class='mini-title'>{name}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='color: #64748B; margin-bottom: 0.5rem;'>{role}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='quote'>“{quote}”</div>", unsafe_allow_html=True)
                st.write(rating)


def render_faq() -> None:
    st.markdown("<div class='section-heading'>FAQ</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Jawaban singkat untuk pertanyaan yang sering muncul sebelum memulai kerja sama.</div>",
        unsafe_allow_html=True,
    )

    faq_items = [
        ("Berapa lama turnaround-nya?", "Biasanya saya bisa menyelesaikan pekerjaan dalam 1–3 hari, tergantung kompleksitas data dan kebutuhan revisi."),
        ("Apakah data aman?", "Ya. Saya menjaga kerahasiaan data dan hanya menggunakan file yang Anda kirimkan untuk kebutuhan pekerjaan yang disepakati."),
        ("Apakah ada revisi?", "Tentu. Satu kali revisi ringan biasanya sudah termasuk dalam paket, dan revisi tambahan bisa dibahas lebih lanjut."),
        ("Format file apa yang diterima?", "Saya menerima Excel, CSV, TXT, export SQL, atau data mentah yang bisa dikonversi ke format yang sesuai."),
        ("Bagaimana pembayaran?", "Pembayaran bisa dilakukan melalui transfer bank atau metode yang disepakati sebelum pekerjaan dimulai."),
    ]

    for title, content in faq_items:
        with st.expander(title):
            st.write(content)


def render_contact() -> None:
    st.markdown("<div class='section-heading'>Order Now</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='section-copy'>Siap mulai? Kirim kebutuhan Anda, dan saya akan bantu menyiapkan pesan WhatsApp yang sesuai dengan paket yang Anda butuhkan.</div>",
        unsafe_allow_html=True,
    )

    with st.form("contact_form"):
        name = st.text_input("Nama")
        need = st.text_input("Kebutuhan Anda")
        message = st.text_area("Pesan singkat")
        submitted = st.form_submit_button("Buat pesan WhatsApp")

    if submitted:
        full_message = (
            f"Halo, saya {name or 'mau order'}. "
            f"Kebutuhan saya: {need or 'lihat paket layanan'}. "
            f"Pesan singkat: {message or 'mohon bantu saya'}"
        )
        st.success("Pesan siap dikirim.")
        st.link_button("📲 Kirim lewat WhatsApp", build_whatsapp_link(full_message), use_container_width=True)

    with st.container(border=True):
        st.markdown("<div class='mini-title'>Atau langsung hubungi</div>", unsafe_allow_html=True)
        st.markdown("<p>📱 WhatsApp: +62 857 2764 5913</p>", unsafe_allow_html=True)
        st.markdown("<p>✉️ Kirim detail kebutuhan, deadline, dan format file yang ingin diproses.</p>", unsafe_allow_html=True)


def render_footer() -> None:
    st.markdown(
        """
        <div class='footer-card'>
            <strong>Dooit</strong> — layanan olah data, analisis, visualisasi, dan laporan otomatis untuk kebutuhan bisnis yang bergerak cepat.<br>
            WhatsApp: +62 857 2764 5913<br>
            Harga dan paket dapat disesuaikan dengan kompleksitas pekerjaan.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> str:
    with st.sidebar:
        st.title("Dooit")
        st.caption("Data Analysis & Visualization")
        page = st.radio(
            "Navigasi",
            [
                "Home",
                "Services",
                "Portfolio / Sample Work",
                "How It Works",
                "Testimonials",
                "FAQ",
                "Contact / Order Now",
            ],
            index=0,
        )
    return page


def main() -> None:
    inject_css()
    page = render_sidebar()

    if page == "Home":
        render_home()
    elif page == "Services":
        render_services()
    elif page == "Portfolio / Sample Work":
        render_portfolio()
    elif page == "How It Works":
        render_how_it_works()
    elif page == "Testimonials":
        render_testimonials()
    elif page == "FAQ":
        render_faq()
    else:
        render_contact()

    render_footer()


if __name__ == "__main__":
    main()
