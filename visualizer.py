import matplotlib.pyplot as plt
import streamlit as st

def plot_anomalies(df):
    fig, ax1 = plt.subplots(figsize=(14, 6))

    ax1.set_title("Stock Price with Anomalies")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close Price")
    ax1.plot(df['Date'], df['Close'], label='Close', color='blue')

    # Anomalies
    ax1.scatter(df[df['Anomaly']]['Date'], df[df['Anomaly']]['Close'], color='red', marker='x', label='Anomaly')

    # Buy/Sell
    ax1.scatter(df[df['Action'] == 'BUY']['Date'], df[df['Action'] == 'BUY']['Close'], marker='^', color='green', label='BUY')
    ax1.scatter(df[df['Action'] == 'SELL']['Date'], df[df['Action'] == 'SELL']['Close'], marker='v', color='orange', label='SELL')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Volume", color='gray')
    ax2.plot(df['Date'], df['Volume'], color='gray', alpha=0.3)

    fig.tight_layout()
    fig.legend(loc='upper left')
    ax1.grid(True)

    # ✅ Show chart in Streamlit
    st.pyplot(fig)
