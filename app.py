import streamlit as st
import yfinance as yf
import pandas as pd

# Set the page config
st.set_page_config(page_title="OMXC25 Index Closing Prices", layout="wide")

# Title for the app
st.title("Potentielle gevinter og tab ved invesering OMXC25 over en længere tidshorisont")

st.subheader("OMXC25 Index Closing Prices Since 2000")

# Fetch the OMXC25 data
omxc25 = yf.Ticker("^OMXC25")  # This might need adjustment if the ticker symbol is not recognized

# Get historical data
hist_data = omxc25.history(period="max")

# Filter data from 2000 onwards
hist_data_since_2000 = hist_data.loc['2000-01-01':]

# Display the closing prices
st.line_chart(hist_data_since_2000['Close'])

# Resample the data to get the first entry of each month and round to 2 decimal places
monthly_data = hist_data_since_2000.resample('MS').first().round(2)

# Create a DataFrame with just the 'Close' prices
monthly_closing_prices = monthly_data[['Close']].round(2)

# Rename the column for clarity
monthly_closing_prices.rename(columns={'Close': 'Closing Price on First Day of Month'}, inplace=True)

# Display the table in the Streamlit app using st.table for a static table
st.write(monthly_closing_prices)

st.subheader("Ændring i procent fra første dag i første måned til første dat i seneste måned i datasættet")
# Display percentage change in price from the first month of the data set to the latest month
percentage_change = ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[0]) / monthly_closing_prices.iloc[0]) * 100
st.write(f"Percentage change in price from the first month to the latest month: {percentage_change.values[0]:.2f}%") 

# Display the percentage change for the last 4 years
st.subheader("Procentvis ændring for de sidste 4 år")
percentage_change_4_years = ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-48]) / monthly_closing_prices.iloc[-48]) * 100
st.write(f"Percentage change in price from the first month to the latest month: {percentage_change_4_years.values[0]:.2f}%")

