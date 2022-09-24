import json

import requests
import time
import pandas as pd

def fetch_crypto_data_AV(avkey):
    print('Inside fetch_crypto_data_AV , AVKey is ' + avkey)
    crypto_symbols = ['BTC']
    PushedTicker = []
    time_pricex = []
    open_pricex = []
    high_pricex = []
    low_pricex = []
    close_pricex = []
    volumex = []
    while(True):
        time_price = []
        open_price = []
        high_price = []
        low_price = []
        close_price = []
        volume = []
        for symbol in crypto_symbols:
            URL = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+symbol+'&market=INR&interval=1min&apikey='+avkey
            r = requests.get(url = URL)
            dataset = json.loads(r.text)
            if dataset.get('Time Series Crypto (1min)') == None:
                time.sleep(60)
                continue
            mkt_dataset = dataset['Time Series Crypto (1min)']
            for key,value in mkt_dataset.items():
                mkt_dataset_index = value
                time_price.append(key)
                for key2,val2 in mkt_dataset_index.items():
                    if key2 == '1. open':
                        open_price.append(val2)
                    if key2 == '2. high':
                        high_price.append(val2)
                    if key2 == '3. low':
                        low_price.append(val2)
                    if key2 == '4. close':
                        close_price.append(val2)
                    if key2 == '5. volume':
                        volume.append(val2)

            datasize = len(time_price)

            for i in range(datasize):
                if time_price[i] in PushedTicker:
                    continue
                print(time_price[i], ":", open_price[i], ",", close_price[i], ",", high_price[i], ",", low_price[i],",", volume[i], "\n")
                time_pricex.append(time_price[i])
                open_pricex.append(open_price[i])
                high_pricex.append(high_price[i])
                low_pricex.append(low_price[i])
                close_pricex.append(close_price[i])
                volumex.append(volume[i])
                PushedTicker.append(time_price[i])

            mktdict = {'Time' : time_pricex,'OpenPrice' : open_pricex ,'ClosePrice':close_pricex,'HighPrice':high_pricex,'LowPrice' : low_pricex , 'Volume' : volumex}
            df = pd.DataFrame(mktdict)
            df.to_csv("BTCData.csv",index=False)

        time.sleep(60)

if __name__ == '__main__':
    print('Welcome To CryptUp ! \n')
    avkey = 'float'
    fetch_crypto_data_AV(avkey)

