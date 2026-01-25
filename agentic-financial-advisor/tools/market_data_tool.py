"""
market_data_tool.py
Fetches real-time market data using yfinance.
"""

import yfinance as yf

def fetch_market_data(ticker: str, period: str = "6mo"):
    """
    Fetch historical market data for a given stock/index.

    Input:
        ticker (str): Stock symbol (e.g., 'AAPL', '^NSEI')
        period (str): Time duration (default '6mo')

    Output:
        pandas.DataFrame: Historical price data
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        return data
    except Exception as error:
        raise RuntimeError(f"Market data fetch failed: {error}")
