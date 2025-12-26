
import pandas as pd
import yfinance as yf


def load_yahoo_finance_data(
    ticker: str,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Load financial time-series data and normalize it into a clean,
    forecasting-ready DataFrame.

    Returns:
        DataFrame indexed by date with columns:
        ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close' (optional)]
    """

    # sanitize inputs
    ticker = ticker.strip().upper()
    start_date = str(start_date).strip()
    end_date = str(end_date).strip()

    # download data
    data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False,   # explicit to avoid future warning
        progress=False,
    )

    if data.empty:
        raise ValueError("No data returned. Check ticker or date range.")


    # FIX: MultiIndex on column
    if isinstance(data.columns, pd.MultiIndex):
        # drop ticker level (AAPL)
        data.columns = data.columns.droplevel(1)

    # remove column index name like "Price"
    data.columns.name = None

    # FIX: MultiIndex on INDEX (Date, Price)
    if isinstance(data.index, pd.MultiIndex):
        if "Price" in data.index.names:
            # unstack price into columns
            data = data.unstack(level="Price")
            data.columns = data.columns.droplevel(0)

    # Final cleanup
    data.index = pd.to_datetime(data.index)
    data.index.name = "date"
    data = data.sort_index()

    return data

