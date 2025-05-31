import pandas as pd
from config import VOLUME_SPIKE_THRESHOLD, VOLATILITY_WINDOW

def detect_anomalies(df):
    df = df.copy().reset_index(drop=True)

    ma_close = df['Close'].rolling(window=VOLATILITY_WINDOW).mean()
    volatility = df['Close'].rolling(window=VOLATILITY_WINDOW).std()
    volume_avg = df['Volume'].rolling(window=VOLATILITY_WINDOW).mean().bfill()

    df['MA_Close'] = ma_close
    df['Volatility'] = volatility
    df['Volume_Anomaly'] = df['Volume'] > VOLUME_SPIKE_THRESHOLD * volume_avg

    z_score = (df['Close'] - ma_close) / volatility
    df['Z_Score'] = z_score
    df['Volatility_Anomaly'] = z_score.abs() > 2
    df['Anomaly'] = df['Volume_Anomaly'] | df['Volatility_Anomaly']

    df['Action'] = None
    for i in range(1, len(df)):
        try:
            if df.at[i, 'Anomaly']:
                price_diff = df.at[i, 'Close'] - df.at[i - 1, 'Close']
                if price_diff < 0:
                    df.at[i, 'Action'] = 'BUY'
                elif price_diff > 0:
                    df.at[i, 'Action'] = 'SELL'
                else:
                    df.at[i, 'Action'] = 'HOLD'

        except:
            continue

    return df
