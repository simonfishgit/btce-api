#!/usr/bin/env python
import liqui_client

btce_domain = "api.liqui.io"

attrs = ('high', 'low', 'avg', 'vol', 'vol_cur', 'last',
         'buy', 'sell', 'updated')

print("Tickers:")
connection = liqui_client.BTCEConnection(btce_domain)

info = liqui_client.APIInfo(connection)
for pair in info.pair_names:
    ticker = liqui_client.getTicker(pair, connection)
    print(pair)
    for a in attrs:
        print("\t%s %s" % (a, getattr(ticker, a)))
