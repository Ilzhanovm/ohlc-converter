"""
Main.py
~~~~~~~

Application launcher for Tick-to-OHLC converter.
"""
from Config import get_configuration
from Io import get_data, save_date
from Visualisation import visualize
from Conversion import convert_to_ohlc

def main():
    """
    Handles application runtime
    """

    config = get_configuration()

    tick_data = get_data(config.input_file)
    if not tick_data:
        print(f"ERROR: can't read from {config.input_file}")
        return

    # for every <TICKER> in input data
    for name, data in tick_data.items():
        ohlc_data = convert_to_ohlc(data, config.period)

        if config.visualize:
            visualize(name, ohlc_data)

        if config.output_file:
            save_date(ohlc_data, name + '_' + config.output_file)


if __name__ == '__main__':
    main()
