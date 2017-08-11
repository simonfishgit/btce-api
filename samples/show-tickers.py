#!/usr/bin/env python
import btceapi

btce_domain = "api.liqui.io"

attrs = ('high', 'low', 'avg', 'vol', 'vol_cur', 'last',
         'buy', 'sell', 'updated')

print("Tickers:")
connection = btceapi.BTCEConnection(btce_domain)

info = btceapi.APIInfo(connection)
for pair in info.pair_names:
    ticker = btceapi.getTicker(pair, connection)
    print(pair)
    for a in attrs:
        print("\t%s %s" % (a, getattr(ticker, a)))
