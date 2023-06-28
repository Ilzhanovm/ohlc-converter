"""
Config.py
~~~~~~~~~

Configuration module. Provides function to get the configuration.
"""
import argparse


def get_configuration() -> argparse.Namespace:
    """
    Retrieves configuration from the command line arguments

    :return: configuration namespace
    """

    parser = argparse.ArgumentParser(description="Convert tick-by-tick data to ohlc format")
    parser.add_argument('-v', '--visualize', action='store_true',   help="Show matplotlib's ohlc chart")
    parser.add_argument('-p', '--period', default='3h',             help="Period for ohlc data, defaults to '3h'")
    parser.add_argument('input_file', type=str,                     help="Input file")
    parser.add_argument('-o', '--output_file',                      help="Output file")

    return parser.parse_args()
