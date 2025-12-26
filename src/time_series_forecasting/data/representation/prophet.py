import pandas as pd
import yfinance as yf


def make_prophet(df, index, target):
    out = df.loc[:, [index, target]]
    out.columns = ["ds", "y"]
    return out
