#!/usr/bin/env python
import btceapi

btce_domain = "api.liqui.io"

with btceapi.BTCEConnection(btce_domain) as connection:
    info = btceapi.APIInfo(connection)

    print("Server time: %s" % info.server_time)

    print("Active currencies:")
    for curr in info.currencies:
        print("    %s" % curr)

    print("Active trading pairs:")
    for name in info.pair_names:
        data = info.pairs[name]
        print("    %s" % name)
        print("         decimal places: %s" % data.decimal_places)
        print("              min price: %s" % data.min_price)
        print("              max price: %s" % data.max_price)
        print("             min amount: %s" % data.min_amount)
        print("                 hidden: %s" % data.hidden)
        print("                    fee: %s" % data.fee)
