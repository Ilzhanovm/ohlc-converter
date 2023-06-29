"""
Conversion.py
~~~~~~~~~~

Conversion module. Provides function to convert data to OHLC format.
"""
from typing import Dict
import pandas as pd


def convert_to_ohlc(tick_data: pd.DataFrame, period: str, calculate_clusters: bool) -> Dict[str, pd.DataFrame]:
    """
        Converts data to OHLC format

        :param pd.DataFrame tick_data: data in tick-by-tick format
        :param str period: time period to resample data
        :param bool calculate_clusters: calculates cluster data if True

        :return: dictionary, containing data in OHLC format with 'ohlc' key and cluster data with 'cluster' key if calculate_clusters is True
    """
    LAST_PRICE = "<LAST>"
    VOLUME = "<VOL>"

    ohlc_data = {}

    # resample datetime, calculate ohlc for last price and sum for volume
    resampled_data = tick_data.resample(period)
    ohlc = resampled_data.agg({LAST_PRICE: 'ohlc', VOLUME: 'sum'})

    # drops first-level headers and filters for not empty fields
    ohlc_data['ohlc'] = pd.concat([ohlc[LAST_PRICE], ohlc[VOLUME]], axis=1).dropna()

    if calculate_clusters:
        # create structure for cluster data
        cluster_data = pd.DataFrame(
            index=pd.MultiIndex(
                levels=[[],[]],
                codes=[[],[]],
                names=['datetime', LAST_PRICE]
            ),
            columns=[VOLUME]
        )

        # for each time period
        for datetime, last in resampled_data:
            # calculate volume for each price in time period
            volume_data = pd.DataFrame(last.groupby(LAST_PRICE)[VOLUME].sum())

            # add datetime index to volume data
            volume_data = pd.concat({datetime: volume_data}, names=['datetime'])

            # append volume data to cluster data
            cluster_data = pd.concat([cluster_data, volume_data])

        ohlc_data['clusters'] = cluster_data

    return ohlc_data
