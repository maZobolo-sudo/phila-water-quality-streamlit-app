import pandas as pd
from io import BytesIO
import streamlit as st
@st.cache_data
def load_data(file_or_buffer):
    if hasattr(file_or_buffer,'name'):
        name = file_or_buffer.name.lower()
        if name.endswith('.csv'): return pd.read_csv(file_or_buffer)
        elif name.endswith('.parquet'): return pd.read_parquet(file_or_buffer)
        else: return pd.read_csv(file_or_buffer)
    else:
        try: return pd.read_csv(BytesIO(file_or_buffer))
        except Exception: return pd.DataFrame()
