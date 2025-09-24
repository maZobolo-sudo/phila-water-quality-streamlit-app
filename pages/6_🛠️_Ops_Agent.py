import streamlit as st, pandas as pd, os
from pathlib import Path
from src.agent import log_alert

st.title("🛠️ Ops & Agent")
WORKSPACE = st.secrets.get("workspace_key","default")
logpath = f"tenants/{WORKSPACE}/reports/agent_log.csv"

message = st.text_area("Message", "Alert: High non-compliance risk at Plant X. Please investigate and retest.")
severity = st.selectbox("Severity", ["info","warning","critical"])
if st.button("Log Alert"):
    path = log_alert(message, severity, logpath); st.success(f"Logged to {path}")
st.subheader("Alert Log")
if os.path.exists(logpath): st.dataframe(pd.read_csv(logpath).tail(50))
else: st.info("No alerts logged yet.")
