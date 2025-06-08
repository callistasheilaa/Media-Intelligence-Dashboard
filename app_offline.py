
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Media Intelligence Dashboard", layout="wide")
st.title("📊 Media Intelligence Dashboard")

st.markdown("### 📁 Upload file CSV")
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

def show_static_insight(title, insights):
    st.markdown(f"💡 **{title} Insight:**")
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
        f"Sentimen terbanyak adalah '{sent_count.iloc[0]['Sentiment']}' dengan jumlah {sent_count.iloc[0]['Count']}.",
        "Perbandingan antara sentimen positif dan negatif cukup mencolok.",
        "Distribusi sentimen menunjukkan kecenderungan persepsi publik."
    ]
    show_static_insight("Sentiment", insights1)

    st.subheader("2. Engagement Trend Over Time")
    trend = df.groupby('Date')['Engagements'].sum().reset_index()
    fig2 = px.line(trend, x='Date', y='Engagements', title="Tren Engagement per Tanggal")
    st.plotly_chart(fig2, use_container_width=True)
    top_day = trend.sort_values(by='Engagements', ascending=False).iloc[0]
    insights2 = [
        f"Tanggal dengan engagement tertinggi adalah {top_day['Date'].date()} sebanyak {top_day['Engagements']}.",
        "Terjadi lonjakan engagement pada beberapa titik waktu.",
        "Tren umum menunjukkan fluktuasi aktivitas media."
    ]
    show_static_insight("Engagement Trend", insights2)

    st.subheader("3. Platform Engagements")
    plat = df.groupby('Platform')['Engagements'].sum().reset_index()
    fig3 = px.bar(plat, x='Platform', y='Engagements', title="Engagement per Platform")
    st.plotly_chart(fig3, use_container_width=True)
    top_platform = plat.sort_values(by='Engagements', ascending=False).iloc[0]
    insights3 = [
        f"Platform dengan engagement tertinggi adalah {top_platform['Platform']} dengan {top_platform['Engagements']}.",
        "Beberapa platform memiliki kontribusi engagement yang rendah.",
        "Distribusi platform menunjukkan fokus utama kanal komunikasi."
    ]
    show_static_insight("Platform", insights3)

    st.subheader("4. Media Type Mix")
    media = df['Media_Type'].value_counts().reset_index()
    media.columns = ['Media_Type', 'Count']
    fig4 = px.pie(media, names='Media_Type', values='Count', title="Komposisi Jenis Media")
    st.plotly_chart(fig4, use_container_width=True)
    insights4 = [
        f"Jenis media terbanyak adalah '{media.iloc[0]['Media_Type']}' sebanyak {media.iloc[0]['Count']}.",
        "Media type menunjukkan kecenderungan saluran distribusi konten.",
        "Distribusi jenis media cukup merata antar kategori."
    ]
    show_static_insight("Media Type", insights4)

    st.subheader("5. Top 5 Locations by Engagement")
    loc = df.groupby('Location')['Engagements'].sum().reset_index()
    top5 = loc.sort_values(by='Engagements', ascending=False).head(5)
    fig5 = px.bar(top5, x='Location', y='Engagements', title="Top 5 Lokasi berdasarkan Engagement")
    st.plotly_chart(fig5, use_container_width=True)
    top_location = top5.iloc[0]
    insights5 = [
        f"Lokasi dengan engagement tertinggi adalah {top_location['Location']} dengan {top_location['Engagements']}.",
        "Top 5 lokasi menyumbang mayoritas engagement.",
        "Distribusi lokasi dapat menjadi acuan untuk targeting konten."
    ]
    show_static_insight("Location", insights5)
else:
    st.info("Silakan upload file CSV terlebih dahulu.")
