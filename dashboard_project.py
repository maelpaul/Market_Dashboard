#yolo# Dashboard with equity (SPY), forex (USD), commodities (gold, crude oil, wheat), bonds (inflation-linked bonds)
# Data about growth, inflation, volatility, and yield
# Data goes back as far as possible, with widget slider to choose time frame

##################################################
# source ~/myenv/bin/activate

#import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Getting the data for SPY (daily)
# Closing prices only
data = yf.download("SPY", period="max")['Close']
data.to_csv("spy_data.csv")

# print(data)
# print(data.index)

# print("\n\n\n\n")

spy = (pd.read_csv("spy_data.csv", index_col=0, parse_dates=True)['SPY'].pct_change() + 1).cumprod()

# print(data)
# print(data.index)

# Check for missing values
# missing_values = data.isna().sum() # number is zero, no missing values -> if there are missing values ffill = forward fill = replace blanks by the last value, do not interpolate !

# print(missing_values)

# Plot the data
# data['SPY'].plot()
spy.plot(label = "SPY")
plt.ylabel("SPY Closing Price")
plt.title("SPY Closing Prices Over Time")
plt.yscale('log')

# Forex using USD index
usd = (yf.download("DX-Y.NYB", start=spy.index.min())['Close'].pct_change() + 1).cumprod()
usd['DX-Y.NYB'].plot(label='USD Index')
plt.legend()
plt.show()
