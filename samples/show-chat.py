#!/usr/bin/env python
import liqui_client

btce_domain = "api.liqui.io"

with liqui_client.BTCEConnection(btce_domain) as connection:
    info = liqui_client.APIInfo(connection)

    mainPage = info.scrapeMainPage()
    for message in mainPage.messages:
        msgId, user, time, text = message
        print("%s %s: %s" % (time, user, text))

    print()

    print("dev online: %s" % ('yes' if mainPage.devOnline else 'no'))
    print("support online: %s" % ('yes' if mainPage.supportOnline else 'no'))
    print("admin online: %s" % ('yes' if mainPage.adminOnline else 'no'))
