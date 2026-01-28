# ============================================================================
# market_data_tool.py
# Market data fetching utility using yfinance
# Provides functions to retrieve real-time and historical market data
# ============================================================================

# Import yfinance library for accessing financial market data
# yfinance allows easy retrieval of stock prices, historical data, and other market information
import yfinance as yf

def fetch_market_data(ticker: str, period: str = "6mo"):
    """
    Fetch historical market data for a given stock or index from Yahoo Finance.
    
    This function:
    1. Accepts a stock ticker symbol and time period
    2. Connects to Yahoo Finance API via yfinance
    3. Retrieves historical price data for the specified period
    4. Returns the data as a pandas DataFrame
    5. Handles exceptions and provides error messages
    
    Args:
        ticker (str): Stock symbol or index code
                     Examples:
                     - 'AAPL' for Apple Inc.
                     - 'GOOGL' for Google
                     - '^NSEI' for Nifty 50 Index
                     - 'BTC-USD' for Bitcoin
        
        period (str): Time duration for historical data (default: '6mo')
                     Valid options:
                     - '1d': 1 day
                     - '5d': 5 days
                     - '1mo': 1 month
                     - '3mo': 3 months
                     - '6mo': 6 months (default)
                     - '1y': 1 year
                     - '2y': 2 years
                     - '5y': 5 years
                     - '10y': 10 years
                     - 'max': All available data
    
    Returns:
        pandas.DataFrame: Historical price data with the following columns:
                         - Open: Opening price for the day
                         - High: Highest price during the day
                         - Low: Lowest price during the day
                         - Close: Closing price for the day
                         - Volume: Number of shares traded
                         - Dividends: Dividend information (if applicable)
                         Index: Date (DatetimeIndex)
    
    Raises:
        RuntimeError: If the market data fetch fails
                     Includes the original error message for debugging
    
    Example:
        >>> data = fetch_market_data('AAPL', '1y')
        >>> print(data.head())  # Print first 5 rows
        >>> print(data.tail())  # Print last 5 rows
    """
    
    # Wrap the data fetching logic in try-except for error handling
    try:
        # Step 1: Create a Ticker object for the given stock symbol
        # The Ticker class manages all interactions with that specific stock
        stock = yf.Ticker(ticker)
        
        # Step 2: Retrieve historical price data for the specified period
        # The history() method fetches data from Yahoo Finance servers
        # It returns a DataFrame indexed by date with OHLCV data (Open, High, Low, Close, Volume)
        data = stock.history(period=period)
        
        # Step 3: Return the retrieved data
        # The caller can now use this data for analysis, calculations, charting, etc.
        return data
        
    # Exception handling: Catch any errors that occur during data fetching
    except Exception as error:
        # Step 4: Raise a RuntimeError with a descriptive message
        # This helps users understand what went wrong
        # Common reasons for errors:
        # - Invalid ticker symbol (ticker doesn't exist)
        # - Network connectivity issues
        # - Yahoo Finance service temporarily unavailable
        # - Invalid period parameter
        raise RuntimeError(f"Market data fetch failed: {error}")
