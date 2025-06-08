
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Media Intelligence Dashboard", layout="wide")
st.title("📊 Media Intelligence Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 1. Sentiment Breakdown
    st.subheader("1. Sentiment Breakdown")
    sent_count = df['Sentiment'].value_counts().reset_index()
    sent_count.columns = ['Sentiment', 'Count']
    fig1 = px.pie(sent_count, names='Sentiment', values='Count')
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Engagement Trend Over Time
    st.subheader("2. Engagement Trend Over Time")
    trend = df.groupby('Date')['Engagements'].sum().reset_index()
    fig2 = px.line(trend, x='Date', y='Engagements')
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Platform Engagement
    st.subheader("3. Platform Engagements")
    plat = df.groupby('Platform')['Engagements'].sum().reset_index()
    fig3 = px.bar(plat, x='Platform', y='Engagements')
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Media Type Mix
    st.subheader("4. Media Type Mix")
    media = df['Media_Type'].value_counts().reset_index()
    media.columns = ['Media_Type', 'Count']
    fig4 = px.pie(media, names='Media_Type', values='Count')
    st.plotly_chart(fig4, use_container_width=True)

    # 5. Top 5 Locations by Engagement
    st.subheader("5. Top 5 Locations by Engagement")
    loc = df.groupby('Location')['Engagements'].sum().reset_index()
    top5 = loc.sort_values(by='Engagements', ascending=False).head(5)
    fig5 = px.bar(top5, x='Location', y='Engagements')
    st.plotly_chart(fig5, use_container_width=True)
