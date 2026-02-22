# Quantitative Strategy Backtester 📈

An algorithmic trading simulation engine that tests technical analysis strategies against historical market data.

## 🧠 The Strategy: "The Golden Cross"
This engine tests the classic **Golden Cross** strategy:
* **Buy Signal:** When the short-term average (50-Day SMA) crosses *above* the long-term average (200-Day SMA).
* **Sell Signal:** When the short-term average crosses *below* the long-term average ("Death Cross").

## 🛠️ Technology Stack
* **Data Source:** Yahoo Finance API (`yfinance`)
* **Data Processing:** Pandas (Time-series analysis, vectorization)
* **Visualization:** Matplotlib (Performance charting)

## 🚀 Features
* **Historical Simulation:** Retests strategies on data from 2020 to present.
* **Performance Comparison:** Benchmarks the strategy against a standard "Buy & Hold" approach.
* **Visual Analytics:** Generates a growth curve chart comparing Strategy Equity vs. Market Equity.

## ⚡ Usage
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the engine:
    ```bash
    python backtest_core.py
    ```
3.  Enter a ticker (e.g., `BTC-USD` or `NVDA`) to see the report.
