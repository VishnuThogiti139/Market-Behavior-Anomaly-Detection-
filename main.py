from data_loader import fetch_stock_data
from analyzer import detect_anomalies
from visualizer import plot_anomalies
import os

def main():
    print("📥 Fetching stock data...")
    df = fetch_stock_data()

    print("🔎 Running anomaly detection...")
    df = detect_anomalies(df)

    # 🔍 Print a few detected anomaly rows (debug view)
    print("\n🧪 Sample Anomaly Rows:")
    print(df[df['Anomaly']].tail(5))

    print("📈 Generating chart...")
    plot_anomalies(df)

    # Save to /data/analyzed_data.csv
    output_path = os.path.join("data", "analyzed_data.csv")
    df.to_csv(output_path, index=False)
    print(f"\n✅ Saved to: {os.path.abspath(output_path)}")

    # Print action signals (BUY/SELL)
    actions = df[df['Action'].notna()][['Date', 'Close', 'Volume', 'Action']]
    if actions.empty:
        print("❗ No Buy/Sell actions detected. Try another stock symbol or a longer time range.")
    else:
        print("\n📋 Last 10 Buy/Sell Actions:")
        print(actions.tail(10))

if __name__ == "__main__":
    main()
