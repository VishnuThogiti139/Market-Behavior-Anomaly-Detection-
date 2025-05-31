**Use of This Project (in Simple Words)**
This project helps you spot unusual behavior in stock prices, like a sudden spike in volume or a big price jump.

It can tell you, “Hey, something interesting is happening here — maybe it’s a good time to look into buying or selling.”

It shows this using a chart, marks anomalies, and even suggests Buy or Sell actions based on what’s happening in the market.

You can use it to:

Analyze stock behavior

Get alerts on unusual activity

Make better trading decisions

Visualize trends and signals

Export data for reports or further analysis

 **Full Breakdown** 

The project is a modular pipeline built in Python for detecting unusual market behavior in stock prices. Here's how it works technically:

1. Data Ingestion
Used the yfinance API to pull 5+ years of historical stock data including open, close, high, low, and volume.

The data is loaded and preprocessed using Pandas.

2. Anomaly Detection Logic
Applied a rolling moving average and rolling standard deviation over a 20-day window.

Computed z-score to detect abnormal price volatility.

Computed rolling average volume, then flagged any day where volume exceeded 2x the average as a volume anomaly.

If either condition is met, it's marked as an anomaly.

3. Action Simulation (Buy/Sell)
If an anomaly is detected and the price drops from the previous day, the system marks it as a BUY.

If it rises, it's marked as a SELL.

4. Visualization
A Matplotlib plot shows:

Closing price (blue line)

Volume (gray line)

Anomalies (red X)

Buy actions (green ↑)

Sell actions (orange ↓)

5. Export and Reporting
The entire result, including anomaly flags and simulated actions, is saved to a CSV file: analyzed_data.csv.

The last 10 Buy/Sell actions are printed in the terminal for quick review.

