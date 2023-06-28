# OHLC-converter

Converts tick-by-tick stock market data to OHLC format. Supports visualization with mplfinance.

## Dependencies

Requires pandas for core operations. Matplotlib and mplfinance are required for visualization.

## Input data format
- Headers: <TICKER>, <DATE>, <TIME>, <LAST>, <VOL>
- Date format: YYYYMMDD
- Time format: HHMMSS

### Example data:
```
<TICKER>,<DATE>,<TIME>,<LAST>,<VOL>
STOCKNAME,20230610,100000,160.500000000,20
STOCKNAME,20230610,100001,160.550000000,10
STOCKNAME,20230610,100002,160.510000000,10
```

## Output data format
- Headers: datetime, open, high, low, close, <VOL>
- output file name TICKER_<output>, where <output> is specified in args

## Usage

```
ohlc-converter [-h] [-v] [-p PERIOD] INPUT [-o OUTPUT] 
```
### positional arguments:

- INPUT - name of the data containing file

### optional arguments:

- -h - show help message
- -v - show matplotlib's ohlc chart
- -p PERIOD - set period for ohlc data, defaults to '3h'
- -o OUTPUT - name of output file, doesn't store result if ignored

### example 
```
ohlc-converter -v -p 1d input.csv -o output.csv
```
Reads data from input.csv, calculates ohlc data for a period of one day, shows data visualization and saves results in output.csv.