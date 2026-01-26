import numpy as np
import pandas as pd


def validate_returns_df(df: pd.DataFrame, tickers: list):
    """
    Validate returns DataFrame before portfolio optimization.
    Fails fast if data is malformed.
    """
    assert not df.empty, "Returns DataFrame is empty"
    assert all(t in df.columns for t in tickers), "Missing required tickers"
    assert not df.isna().any().any(), "NaN values detected in returns data"


def annualize_return(daily_return: float, trading_days: int = 252) -> float:
    """
    Convert average daily return to annualized return.
    """
    return daily_return * trading_days


def annualize_covariance(cov_matrix: pd.DataFrame, trading_days: int = 252):
    """
    Annualize covariance matrix.
    """
    return cov_matrix * trading_days
