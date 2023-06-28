"""
Conversion.py
~~~~~~~~~~

Conversion module. Provides function to convert data to OHLC format.
"""
import pandas as pd


def convert_to_ohlc(tick_data: pd.DataFrame, period: str) -> pd.DataFrame:
    """
        Converts data to OHLC format

        :param pd.DataFrame tick_data: data in tick-by-tick format
        :param str period: time period to resample data

        :return: pd.DataFrame with data in OHLC format
    """
    LAST_PRICE = "<LAST>"
    VOLUME = "<VOL>"

    ohlc_data = tick_data[LAST_PRICE].resample(period).ohlc()
    ohlc_data[VOLUME] = tick_data[VOLUME].resample(period).sum()

    # filter for not empty fields and return
    return ohlc_data[ohlc_data.open.notna()]
