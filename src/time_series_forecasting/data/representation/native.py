import pandas as pd
import yfinance as yf


def make_native(data, index, targets):
    return data.loc[:, [index, *targets]]