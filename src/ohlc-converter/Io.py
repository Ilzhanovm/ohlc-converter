"""
Io.py
~~~~~

Input/output module. Provides functions read/write data.
"""
from typing import Dict
import pandas as pd


def save_date(data: pd.DataFrame, file_name: str):
    """
    Saves data to output

    :param pd.DataFrame data: spreadsheet to store
    :param str file_name: name of the output file
    """
    data.to_csv(file_name)


def get_data(file_name: str) -> Dict[str, pd.DataFrame]:
    """
    Retrieves data from input. Converts date and time columns to indexing datetime column.

    :param str file_name: name of the input file

    :return: dictionary with pandas' DataFrames in {<TICKER>: DATA} format
    """
    DATETIME_FORMAT = "%Y%m%d %H%M%S"
    DATE_FIELD = "<DATE>"
    TIME_FIELD = "<TIME>"
    DATE_TIME_FIELD = "<DATE>_<TIME>"

    TICKER_FIELD = "<TICKER>"
    RETURNING_FIELDS = ["<TICKER>", "<LAST>", "<VOL>"]

    # stores DataFrame for each <TICKER>
    data_frames: Dict[str, pd.DataFrame] = {}

    try:
        data = pd.read_csv(
            file_name,
            parse_dates=[[DATE_FIELD, TIME_FIELD]],
            date_format=DATETIME_FORMAT
        )
    except FileNotFoundError:
        return data_frames

    # rename datetime column according to conventions
    data = data.rename(columns={DATE_TIME_FIELD: "datetime"})

    # for every <TICKER> in input data
    for ticker in data[TICKER_FIELD].unique():
        # filter DataFrame to contains only one <TICKER>
        _data = data[data[TICKER_FIELD] == ticker].copy()

        # set datetime to be index and filter for necessary fields
        data_frames[ticker] = _data.set_index("datetime")[RETURNING_FIELDS]

    return data_frames
