import streamlit as st
import yfinance as yf
import pandas as pd

# Set the page config
st.set_page_config(page_title="OMXC25 Index Closing Prices", layout="wide")

# Title for the app
st.title("OMXC25 Index Closing Prices Since 2000")

# Fetch the OMXC25 data
omxc25 = yf.Ticker("^OMXC25")  # This might need adjustment if the ticker symbol is not recognized

# Get historical data
hist_data = omxc25.history(period="max")

# Filter data from 2000 onwards
hist_data_since_2000 = hist_data.loc['2000-01-01':]

# Display the closing prices
st.line_chart(hist_data_since_2000['Close'])

