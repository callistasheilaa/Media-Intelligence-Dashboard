import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Media Intelligence Dashboard", layout="wide")
st.title("ðŸ“Š Media Intelligence Dashboard")

st.markdown("### ðŸ“ Upload file CSV")
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

def show_static_insight(title, insights):
    st.markdown(f"ðŸ§  **AI Insight â€“ {title}:**")
    for idx, text in enumerate(insights, 1):
        st.markdown(f"{idx}. {text}")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    st.subheader("1. Sentiment Breakdown")
    sent_count = df['Sentiment'].value_counts().reset_index()
    sent_count.columns = ['Sentiment', 'Count']
    fig1 = px.pie(sent_count, names='Sentiment', values='Count', title="Distribusi Sentimen")
    st.plotly_chart(fig1, use_container_width=True)
    insights1 = [
        f"Sentimen yang paling dominan dalam percakapan media adalah '{sent_count.iloc[0]['Sentiment']}', dengan total {sent_count.iloc[0]['Count']} entri. Ini menunjukkan bahwa publik cenderung memberikan respons yang sejalan dengan kategori tersebut.",
        "Secara keseluruhan, persebaran sentimen memperlihatkan dominasi reaksi netral dan positif, yang menandakan respons audiens yang cukup sehat terhadap konten yang dipublikasikan.",
        "Minimnya sentimen negatif dapat menjadi sinyal bahwa strategi komunikasi yang dijalankan mampu menghindari kontroversi atau isu yang memicu persepsi buruk."
    ]
    show_static_insight("Sentiment", insights1)

    st.subheader("2. Engagement Trend Over Time")
    trend = df.groupby('Date')['Engagements'].sum().reset_index()
    fig2 = px.line(trend, x='Date', y='Engagements', title="Tren Engagement per Tanggal")
    st.plotly_chart(fig2, use_container_width=True)
    top_day = trend.sort_values(by='Engagements', ascending=False).iloc[0]
    insights2 = [
        f"Pada tanggal {top_day['Date'].date()}, engagement mencapai puncaknya dengan total {top_day['Engengagements']} interaksi. Ini menunjukkan adanya momentum atau konten yang sangat menarik di hari tersebut.",
        "Terdapat beberapa lonjakan signifikan selama periode pemantauan, yang mengindikasikan waktu-waktu strategis dalam distribusi konten atau viralitas tertentu.",
        "Secara keseluruhan, tren engagement mengalami fluktuasi dengan puncak-puncak tertentu, yang dapat dijadikan acuan dalam penjadwalan posting konten ke depan."
    ]
    show_static_insight("Engagement Trend", insights2)

    st.subheader("3. Platform Engagements")
    plat = df.groupby('Platform')['Engagements'].sum().reset_index()
    fig3 = px.bar(plat, x='Platform', y='Engagements', title="Engagement per Platform")
    st.plotly_chart(fig3, use_container_width=True)
    top_platform = plat.sort_values(by='Engagements', ascending=False).iloc[0]
    insights3 = [
        f"Platform dengan performa terbaik adalah {top_platform['Platform']} dengan total {top_platform['Engagements']} interaksi, menjadikannya kanal utama untuk menjangkau audiens.",
        "Kombinasi platform YouTube dan X/Twitter memperlihatkan efektivitas dalam menjaring keterlibatan pengguna secara masif dibandingkan kanal lain.",
        "Beberapa platform seperti TikTok berkontribusi dengan volume lebih rendah, namun tetap potensial untuk optimalisasi konten pendek yang bersifat viral."
    ]
    show_static_insight("Platform", insights3)

    st.subheader("4. Media Type Mix")
    media = df['Media_Type'].value_counts().reset_index()
    media.columns = ['Media_Type', 'Count']
    fig4 = px.pie(media, names='Media_Type', values='Count', title="Komposisi Jenis Media")
    st.plotly_chart(fig4, use_container_width=True)
    insights4 = [
        f"Jenis media paling banyak digunakan adalah '{media.iloc[0]['Media_Type']}', yang mencerminkan preferensi penyampaian pesan secara visual dan interaktif.",
        "Media jenis Carousel dan Video menunjukkan popularitas tinggi, yang dapat dimanfaatkan untuk strategi komunikasi yang membutuhkan storytelling.",
        "Distribusi jenis media yang beragam menandakan adanya fleksibilitas dan eksperimen dalam penyajian konten di berbagai platform digital."
    ]
    show_static_insight("Media Type", insights4)

    st.subheader("5. Top 5 Locations by Engagement")
    loc = df.groupby('Location')['Engagements'].sum().reset_index()
    top5 = loc.sort_values(by='Engagements', ascending=False).head(5)
    fig5 = px.bar(top5, x='Location', y='Engagements', title="Top 5 Lokasi berdasarkan Engagement")
    st.plotly_chart(fig5, use_container_width=True)
    top_location = top5.iloc[0]
    insights5 = [
        f"Wilayah dengan performa tertinggi adalah {top_location['Location']}, yang menyumbangkan total {top_location['Engagements']} interaksi sepanjang periode.",
        "Lokasi seperti Medan dan Yogyakarta menempati posisi teratas dalam keterlibatan, menunjukkan potensi kuat untuk dijadikan target kampanye regional.",
        "Distribusi engagement berdasarkan lokasi memperlihatkan konsentrasi minat yang tinggi di daerah-daerah urban dan padat penduduk."
    ]
    show_static_insight("Location", insights5)
else:
    st.info("Silakan upload file CSV terlebih dahulu.")
