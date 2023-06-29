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

    # resample datetime, calculate ohlc for last price and sum for volume
    ohlc_data = tick_data.resample(period).agg({LAST_PRICE: 'ohlc', VOLUME: 'sum'})

    # drops first-level headers and filters for not empty fields
    ohlc_data = pd.concat([ohlc_data[LAST_PRICE], ohlc_data[VOLUME]], axis=1).dropna()

    return ohlc_data
