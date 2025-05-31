import yfinance as yf
from datetime import datetime, timedelta

def fetch_stock_data(symbol="AAPL", years_back=5):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=years_back * 365)
    df = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    df.reset_index(inplace=True)
    return df
