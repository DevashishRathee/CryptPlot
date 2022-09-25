# CryptPlot
Automatic Ticker Builder for Cryptocurrencies , Includes a Candlestick graph plotter for Analyzing

Recommended System Requirements:<br />
Python 3.9 <br />
2 GB Memory<br />
Dual Core Processor<br />

Python Modules Requirements:<br />
*CryptPlot uses Pandas,json,Requests for Tick Builder<br />
*CryptPlot uses Plotly for Graph Plotting<br />
All of these can be installed using pip, eg. pip install pandas<br />

Steps to Use:<br />
1.Clone this repo.<br />
2.Run "python ticker.py" and leave it running, this will build and csv in background and will be updating it every minute.<br />
3.Run "plotter.py" to get a chart of Crypto OHLCV.<br />

Version - 0.1<br />
CryptPlot uses Alphavantage API as base. Using this Demo Version you can make 5 calls per minute.<br />
<br />
Future Plans-<br />
1.Add support for multiple cryptocurrencies as it currently only supports BTC.<br />
2.Add dynamic graph support.<br />
3.Remove dependency from Alphavantage API's.<br />
