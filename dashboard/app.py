import streamlit as st
import pandas as pd

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="CloudDocs Dashboard", layout="wide")

st.title("🚨 CloudDocs Anomaly Detection Dashboard")

# -----------------------
# Load Data
# -----------------------
try:
    df = pd.read_csv("output/suspicious_activity.csv")
except:
    st.error("❌ CSV file not found. Please run main.py first.")
    st.stop()

# -----------------------
# Metrics Section
# -----------------------
st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Anomalies", len(df))
col2.metric("Critical", len(df[df['severity'] == 'critical']))
col3.metric("Warnings", len(df[df['severity'] == 'warning']))

# -----------------------
# Filter Section
# -----------------------
st.subheader("🔍 Filters")

col1, col2 = st.columns(2)

severity_filter = col1.selectbox(
    "Select Severity",
    ["all", "critical", "warning", "info"]
)

user_filter = col2.text_input("Search by User ID")

filtered_df = df.copy()

if severity_filter != "all":
    filtered_df = filtered_df[filtered_df['severity'] == severity_filter]

if user_filter:
    filtered_df = filtered_df[filtered_df['user_id'].str.contains(user_filter)]

# -----------------------
# Data Table
# -----------------------
st.subheader("📋 Anomaly Details")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

# -----------------------
# Severity Distribution
# -----------------------
st.subheader("📈 Severity Distribution")

severity_counts = df['severity'].value_counts()
st.bar_chart(severity_counts)

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Built for CloudDocs Security Analysis 🚀")