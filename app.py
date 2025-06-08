
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="Media Intelligence Dashboard", layout="wide")
st.title("📊 Media Intelligence Dashboard")

st.markdown("### 🔐 Masukkan API Key OpenRouter")
api_key = st.text_input("API Key kamu:", type="password")

st.markdown("### 📁 Upload file CSV")
uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

def generate_insight(prompt, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error {response.status_code}: {response.text}"

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    st.subheader("1. Sentiment Breakdown")
    sent_count = df['Sentiment'].value_counts().reset_index()
    sent_count.columns = ['Sentiment', 'Count']
    fig1 = px.pie(sent_count, names='Sentiment', values='Count', title="Distribusi Sentimen")
    st.plotly_chart(fig1, use_container_width=True)
    if api_key:
        prompt1 = f"Buat 3 insight dari distribusi sentimen berikut:\n{sent_count.to_string(index=False)}"
        st.markdown("💡 **AI Insight:**")
        st.write(generate_insight(prompt1, api_key))

    st.subheader("2. Engagement Trend Over Time")
    trend = df.groupby('Date')['Engagements'].sum().reset_index()
    fig2 = px.line(trend, x='Date', y='Engagements', title="Tren Engagement per Tanggal")
    st.plotly_chart(fig2, use_container_width=True)
    if api_key:
        prompt2 = f"Buat insight dari tren engagement berdasarkan tanggal:\n{trend.to_string(index=False)}"
        st.markdown("💡 **AI Insight:**")
        st.write(generate_insight(prompt2, api_key))

    st.subheader("3. Platform Engagements")
    plat = df.groupby('Platform')['Engagements'].sum().reset_index()
    fig3 = px.bar(plat, x='Platform', y='Engagements', title="Engagement per Platform")
    st.plotly_chart(fig3, use_container_width=True)
    if api_key:
        prompt3 = f"Berikan insight dari data engagement tiap platform berikut:\n{plat.to_string(index=False)}"
        st.markdown("💡 **AI Insight:**")
        st.write(generate_insight(prompt3, api_key))

    st.subheader("4. Media Type Mix")
    media = df['Media_Type'].value_counts().reset_index()
    media.columns = ['Media_Type', 'Count']
    fig4 = px.pie(media, names='Media_Type', values='Count', title="Komposisi Jenis Media")
    st.plotly_chart(fig4, use_container_width=True)
    if api_key:
        prompt4 = f"Tolong jelaskan insight dari distribusi jenis media berikut:\n{media.to_string(index=False)}"
        st.markdown("💡 **AI Insight:**")
        st.write(generate_insight(prompt4, api_key))

    st.subheader("5. Top 5 Locations by Engagement")
    loc = df.groupby('Location')['Engagements'].sum().reset_index()
    top5 = loc.sort_values(by='Engagements', ascending=False).head(5)
    fig5 = px.bar(top5, x='Location', y='Engagements', title="Top 5 Lokasi berdasarkan Engagement")
    st.plotly_chart(fig5, use_container_width=True)
    if api_key:
        prompt5 = f"Apa insight dari 5 lokasi dengan engagement tertinggi:\n{top5.to_string(index=False)}"
        st.markdown("💡 **AI Insight:**")
        st.write(generate_insight(prompt5, api_key))
else:
    st.info("Silakan upload file CSV terlebih dahulu.")
