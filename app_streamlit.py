import streamlit as st
from data_loader import fetch_stock_data
from analyzer import detect_anomalies
from visualizer import plot_anomalies
import pandas as pd
import os
import yfinance as yf

st.set_page_config(layout="wide")
st.title("📈 Market Behavior Anomaly Detection")

# Input section
symbol = st.text_input("Enter Stock Symbol", "TSLA")
years = st.slider("Select years of historical data", min_value=1, max_value=10, value=5)

if st.button("Run Analysis"):
    with st.spinner("Fetching and analyzing stock data..."):
        # Update fetch with dynamic symbol + years
        st.subheader(f"📈 {info.get('longName')} ({symbol})")
        df = fetch_stock_data(symbol=symbol, years_back=years)
        df = detect_anomalies(df)
#         info = yf.Ticker(symbol).info
#         company_name = info.get('longName') or "Company Name Not Found"

# # Show header
#         st.subheader(f"📈 {company_name} ({symbol.upper()})")

#         st.subheader("📊 Price & Anomaly Chart")
#         plot_anomalies(df)

        st.subheader("📋 Buy/Sell Signals")
        actions = df[df['Action'].notna()][['Date', 'Close', 'Volume', 'Action']]
        if actions.empty:
            st.warning("No Buy/Sell signals detected.")
        else:
            st.dataframe(actions.tail(10))

        # Download CSV
        output_path = os.path.join("data", f"{symbol}_analyzed.csv")
        df.to_csv(output_path, index=False)
        with open(output_path, "rb") as f:
            st.download_button(f"⬇️ Download {symbol}_analyzed.csv", f, file_name=f"{symbol}_analyzed.csv", mime="text/csv")

        st.success("✅ Analysis complete!")
