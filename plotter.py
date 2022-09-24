import datetime
import time as tm
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime , time

if __name__ == '__main__':
    df = pd.read_csv('BTCData.csv')

    fig = make_subplots(rows = 2,
                        cols = 1,
                        shared_xaxes = True,
                        vertical_spacing = 0.1,
                        subplot_titles=('OHLC','Volume'),
                        row_width=[0.3,0.7])

    fig.add_trace(
        go.Candlestick(
            x=df['Time'],
            open=df['OpenPrice'],
            high=df['HighPrice'],
            low=df['LowPrice'],
            close=df['ClosePrice'],
            showlegend=False),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=df['Time'],
            y=df['Volume'],
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.update_layout(
        title='BitCoin Tick : 1 Minute OHLCV',
        yaxis_title='INR',
        xaxis_title='Time',
        width=1280,
        height=680)
    fig.update(layout_xaxis_rangeslider_visible=False)
    fig.show()
