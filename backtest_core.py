import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- CONFIGURATION ---
TICKER = "AAPL" # Apple Inc.
START_DATE = "2020-01-01"
END_DATE = datetime.now().strftime('%Y-%m-%d')
INITIAL_CAPITAL = 10000 # Starting with $10,000

def run_backtest(ticker):
    print(f"[*] FETCHING DATA FOR {ticker}...")
    # Download historical data
    df = yf.download(ticker, start=START_DATE, end=END_DATE)
    
    if df.empty:
        print("[!] No data found.")
        return

    # 1. Define Strategy: Golden Cross (SMA50 crosses SMA200)
    # SMA = Simple Moving Average
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['SMA200'] = df['Close'].rolling(window=200).mean()

    # 2. Generate Signals
    # Buy (1) when SMA50 > SMA200 (Bullish)
    # Sell (0) when SMA50 < SMA200 (Bearish)
    df['Signal'] = 0
    df.loc[df['SMA50'] > df['SMA200'], 'Signal'] = 1
    
    # Calculate Daily Returns
    df['Market_Return'] = df['Close'].pct_change()
    
    # Strategy Return: We only get the return if we held the stock (Signal = 1)
    # We shift signal by 1 because we trade based on yesterday's close
    df['Strategy_Return'] = df['Market_Return'] * df['Signal'].shift(1)

    # 3. Calculate Cumulative Profit
    df['Market_Cumulative'] = (1 + df['Market_Return']).cumprod() * INITIAL_CAPITAL
    df['Strategy_Cumulative'] = (1 + df['Strategy_Return']).cumprod() * INITIAL_CAPITAL

    # 4. Results
    final_market = df['Market_Cumulative'].iloc[-1]
    final_strategy = df['Strategy_Cumulative'].iloc[-1]
    
    print("-" * 50)
    print(f"BACKTEST RESULTS: {ticker} ({START_DATE} to {END_DATE})")
    print("-" * 50)
    print(f"Initial Capital:   ${INITIAL_CAPITAL:,.2f}")
    print(f"Buy & Hold Result: ${final_market:,.2f}")
    print(f"Strategy Result:   ${final_strategy:,.2f}")
    print("-" * 50)
    
    if final_strategy > final_market:
        print(f"VERDICT: Strategy OUTPERFORMED Market! 🚀")
    else:
        print(f"VERDICT: Strategy UNDERPERFORMED. Buy & Hold was better. 📉")

    # 5. Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(df['Market_Cumulative'], label='Buy & Hold', color='gray', linestyle='--')
    plt.plot(df['Strategy_Cumulative'], label='Golden Cross Strategy', color='green', linewidth=2)
    plt.title(f'Backtest: {ticker} (Golden Cross Strategy)')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    plt.grid(True)
    
    print("[*] Generating Chart...")
    plt.show()

if __name__ == "__main__":
    user_ticker = input("Enter Stock Ticker (e.g., AAPL, TSLA, NVDA): ").upper()
    if not user_ticker:
        user_ticker = TICKER
    run_backtest(user_ticker)
