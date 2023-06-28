"""
Visualisation.py
~~~~~~~~~~~~~~~~

Visualisation module. Provides function to draw an OHLC graph.
"""
import pandas as pd
import mplfinance as mpl

def visualize(name: str, data: pd.DataFrame):
    """
        Shows OHLC graph for given data

        :param pd.DataFrame data: OHLC data
    """
    mpl.plot(
        data,
        type="candle",
        title = f"{name}",
        style="charles"
    )
