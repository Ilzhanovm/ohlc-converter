# OHLC-converter

Converts tick-by-tick stock market data to OHLC format. Supports visualization with mplfinance.

## Dependencies

Requires pandas for core operations. Matplotlib and mplfinance are required for visualization.

## Input data format
- Headers: &lt;TICKER&gt;, &lt;DATE&gt;, &lt;TIME&gt;, &lt;LAST&gt;, &lt;VOL&gt;
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

### OHLC data

- Headers: datetime, open, high, low, close, &lt;VOL&gt;
- output file name is  TICKER&#95;&lt;output&gt;, where &lt;output&gt; is specified in args

### Cluster data
- Headers: datetime, &lt;LAST&gt;, &lt;VOL&gt;
- output file is  TICKER_CLUSTER&#95;&lt;output&gt;, where &lt;output&gt; is specified in args

## Usage

```
ohlc-converter [-h] [-v] [-c] [-p PERIOD] INPUT [-o OUTPUT] 
```
### positional arguments:

- INPUT - name of the data containing file

### optional arguments:

- -h - show help message
- -v - show matplotlib's ohlc chart
- -c - calculate clusters for each candle
- -p PERIOD - set period for ohlc data, defaults to '3h'
- -o OUTPUT - name of output file, doesn't store result if ignored

### example 
```
ohlc-converter -v -c -p 1d input.csv -o output.csv
```
Reads data from input.csv, calculates ohlc data for a period of one day, shows data visualization and saves results in TICKER&#95;output.csv. Also calculates clusters for each candle and saves results in TICKER&#95;CLUSTER&#95;output.csv