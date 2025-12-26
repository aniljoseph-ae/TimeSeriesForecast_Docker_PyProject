import pandas as pd
import yfinance as yf


def make_ml(data, index, targets):
    return data.loc[:, [index, *targets]].reset_index(drop = True)
