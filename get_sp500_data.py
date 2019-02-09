import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import os
import pickle

with open ('sp500_tickers.pickle', 'rb') as f:
    tickers = pickle.load(f)

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2018, 12, 31)
count = 0
for ticker in tickers:
    count += 1
    print(count)
    if not os.path.exists('data/{}.csv'.format(ticker)):
        df = web.DataReader(ticker, 'yahoo', start, end)
        df.to_csv('data/{}.csv'.format(ticker))
        print('File {}.csv created'.format(ticker))
    else:
        print('File {}.csv already exists'.format(ticker))
