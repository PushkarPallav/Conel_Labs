import sys
import os
import streamlit as st
import pandas as pd

# -----------------------------
# Fix import path for src folder
# -----------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ingest import preprocess
from detect import detect_anomalies

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="CloudDocs Dashboard", layout="wide")

st.title(" CloudDocs Anomaly Detection Dashboard")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader("📂 Upload your JSONL file", type=["jsonl"])

if uploaded_file is not None:

    
    # Load Data
    df = pd.read_json(uploaded_file, lines=True)

    # -----------------------------
    # Preprocess
    # -----------------------------
    df = preprocess(df)

    # -----------------------------
    # Detect Anomalies
    # -----------------------------
    anomalies = detect_anomalies(df)

    # -----------------------------
    # Metrics Section
    # -----------------------------
    st.subheader("📊 Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Anomalies", len(anomalies))
    col2.metric("Critical", len(anomalies[anomalies['severity'] == 'critical']))
    col3.metric("Warnings", len(anomalies[anomalies['severity'] == 'warning'])

    )

    # -----------------------------
    # Filters
    # -----------------------------
    st.subheader("🔍 Filters")

    col1, col2 = st.columns(2)

    severity = col1.selectbox(
        "Select Severity",
        ["all", "critical", "warning", "info"]
    )

    user_search = col2.text_input("Search by User ID")

    filtered = anomalies.copy()

    if severity != "all":
        filtered = filtered[filtered['severity'] == severity]

    if user_search:
        filtered = filtered[filtered['user_id'].astype(str).str.contains(user_search)]

    # -----------------------------
    # Results Table
    # -----------------------------
    st.subheader("📋 Anomaly Results")
    st.dataframe(filtered, use_container_width=True)

    # -----------------------------
    # Severity Chart
    # -----------------------------
    st.subheader("📈 Severity Distribution")
    st.bar_chart(anomalies['severity'].value_counts())

else:
    st.info("Upload a JSONL file to start analysis")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built for CloudDocs Security Analysis ")