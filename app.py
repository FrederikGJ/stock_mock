import streamlit as st
import yfinance as yf
import pandas as pd

# Set the page config
st.set_page_config(page_title="OMXC25 Index Closing Prices", layout="wide")

# Title for the app
st.title("Potentielle gevinter og tab ved inveseringer i forskellige index over en længere tidshorisont")

st.subheader("OMXC25 Index Closing Prices Since 2016")

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

# Calculate the percentage change
percentage_change = ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[0]) / monthly_closing_prices.iloc[0]) * 100
percentage_change_value = percentage_change.values[0]
# Display the algebraic formula
st.latex(r"\text{Percentage Change} = \left( \frac{\text{Latest Closing Price} - \text{First Closing Price}}{\text{First Closing Price}} \right) \times 100")
# Display the numeric calculation
st.latex(f"\\text{{Percentage Change}} = \\left( \\frac{{{monthly_closing_prices.iloc[-1].values[0]:.2f} - {monthly_closing_prices.iloc[0].values[0]:.2f}}}{{{monthly_closing_prices.iloc[0].values[0]:.2f}}} \\right) \\times 100 = {percentage_change_value:.2f}\\%")
# Display the result with st.latex
st.latex(f"\\text{{Percentage change in price from the first month to the latest month: }} {percentage_change_value:.2f}\\%")

# Subheader for overall percentage change
st.subheader("Ændring i procent for forskellige tidsperioder")

# Calculate the percentage changes
percentage_changes = {
    "Period": ["Since First Month", "Last 4 Years", "Last 2 Years", "Last Year", "Last 6 Months"],
    "Percentage Change": [
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[0]) / monthly_closing_prices.iloc[0] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-48]) / monthly_closing_prices.iloc[-48] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-24]) / monthly_closing_prices.iloc[-24] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-12]) / monthly_closing_prices.iloc[-12] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-6]) / monthly_closing_prices.iloc[-6] * 100).values[0],
    ]
}

# Create a DataFrame
percentage_change_df = pd.DataFrame(percentage_changes)

# Format the 'Percentage Change' column to round to two decimal places
percentage_change_df['Percentage Change'] = percentage_change_df['Percentage Change'].map('{:.2f}%'.format)

# Display the table in the Streamlit app using st.write
st.write(percentage_change_df)

#### s&p 500

st.subheader("S&P 500 Index Closing Prices Since 2000")

# Fetch the S&P 500 data
sp500 = yf.Ticker("^GSPC")  # Correct ticker symbol for S&P 500

# Get historical data
hist_data = sp500.history(period="max")

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

st.subheader("Ændring i procent fra første dag i første måned til første dag i seneste måned i datasættet")

# Calculate the percentage change
percentage_change = ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[0]) / monthly_closing_prices.iloc[0]) * 100
percentage_change_value = percentage_change.values[0]
# Display the algebraic formula
st.latex(r"\text{Percentage Change} = \left( \frac{\text{Latest Closing Price} - \text{First Closing Price}}{\text{First Closing Price}} \right) \times 100")
# Display the numeric calculation
st.latex(f"\\text{{Percentage Change}} = \\left( \\frac{{{monthly_closing_prices.iloc[-1].values[0]:.2f} - {monthly_closing_prices.iloc[0].values[0]:.2f}}}{{{monthly_closing_prices.iloc[0].values[0]:.2f}}} \\right) \\times 100 = {percentage_change_value:.2f}\\%")
# Display the result with st.latex
st.latex(f"\\text{{Percentage change in price from the first month to the latest month: }} {percentage_change_value:.2f}\\%")

# Subheader for overall percentage change
st.subheader("Ændring i procent for forskellige tidsperioder")

# Calculate the percentage changes
percentage_changes = {
    "Period": ["Since First Month", "Last 4 Years", "Last 2 Years", "Last Year", "Last 6 Months"],
    "Percentage Change": [
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[0]) / monthly_closing_prices.iloc[0] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-48]) / monthly_closing_prices.iloc[-48] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-24]) / monthly_closing_prices.iloc[-24] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-12]) / monthly_closing_prices.iloc[-12] * 100).values[0],
        ((monthly_closing_prices.iloc[-1] - monthly_closing_prices.iloc[-6]) / monthly_closing_prices.iloc[-6] * 100).values[0],
    ]
}

# Create a DataFrame
percentage_change_df = pd.DataFrame(percentage_changes)

# Format the 'Percentage Change' column to round to two decimal places
percentage_change_df['Percentage Change'] = percentage_change_df['Percentage Change'].map('{:.2f}%'.format)

# Display the table in the Streamlit app using st.write
st.write(percentage_change_df)