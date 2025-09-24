import streamlit as st, pandas as pd, os
st.title("🏁 Overview")
st.metric("Build", "v1.0")
st.write("Data dictionary")
st.table(pd.DataFrame({
    "column": ["ph","Hardness","Solids","Chloramines","Sulfate","Conductivity","Organic_carbon","Trihalomethanes","Turbidity","non_compliant"],
    "description": ["Acidity/Basicity","Water hardness (mg/L)","Dissolved solids (ppm)","Chloramine level (ppm)","Sulfate (mg/L)","Conductivity (µS/cm)","Organic carbon (mg/L)","Trihalomethanes (µg/L)","Turbidity (NTU)","Target: 1=non-compliant, 0=compliant"]
}))
