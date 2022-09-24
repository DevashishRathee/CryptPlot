# CryptUp
Automatic Ticker Builder for Cryptocurrencies , Includes a Candlestick graph plotter for Analyzing

Recommended System Requirements:
Python 3.9 
2 GB Memory
Dual Core Processor

Python Modules Requirements:
*CryptUp uses Pandas,json,Requests for Tick Builder
*CryptUp uses Plotly for Graph Plotting
All of these can be installed using pip, eg. pip install pandas

Steps to Use:
1.Clone this repo.
2.Run "python ticker.py" and leave it running, this will build and csv in background and will be updating it every minute.
3.Run "plotter.py" to get a chart of Crypto OHLCV.

Version - 0.1
CryptUp uses Alphavantage API as base. Using this Demo Version you can make 5 calls per minute.

Future Plans-
1.Add support for multiple cryptocurrencies as it currently only supports BTC.
2.Add dynamic graph support.
3.Remove dependency from Alphavantage API's.
