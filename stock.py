import yfinance as yf
import pandas as pd

def get_avg_yearly_performance(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="max")
        
        if hist.empty:
            print("No historical data found for this ticker.")
            return
        
        hist['Year'] = hist.index.year
        
        # Exclude the current year
        current_year = pd.to_datetime("today").year
        hist = hist[hist.index.year < current_year]
        
        yearly_returns = hist['Close'].resample('YE').last().pct_change()
        avg_yearly_performance = yearly_returns.mean() * 100
        
        print(f"Average Yearly Performance of {ticker_symbol} (excluding the current year): {avg_yearly_performance:.2f}%")
        print(f"Total Years: {len(yearly_returns)}") 
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ticker = input("Enter a valid stock Ticker: ").strip().upper()
    get_avg_yearly_performance(ticker)

