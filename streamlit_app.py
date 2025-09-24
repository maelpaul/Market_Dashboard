import pandas as pd
import streamlit as st

title = "Cross Asset Regime Monitor"
st.set_page_config(page_title="Market Dashboard", layout="wide")
st.title(title)

data = pd.read_csv("all_data.csv", index_col=0, parse_dates=True)
