import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

title = "Cross Asset Regime Monitor"
st.set_page_config(page_title="Market Dashboard", layout="wide")
st.title(title)

data = pd.read_csv("all_data.csv", index_col=0, parse_dates=True)
data = data.ffill().dropna()
returns = data.pct_change()
cum_returns = (1 + returns).cumprod()

fig = plt.figure(figsize=(10, 5))
plt.plot(cum_returns, label=cum_returns.columns)
plt.legend()
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title(title)

st.dataframe(cum_returns)
st.pyplot(fig)

assets = cum_returns.columns

st.multiselect("Please select your assets", assets)
