import unittest

import liqui_client


class TestPublic(unittest.TestCase):
    def test_getTicker(self):
        connection = liqui_client.BTCEConnection()
        info = liqui_client.APIInfo(connection)
        for pair in info.pair_names:
            liqui_client.getTicker(pair, connection, info)
            liqui_client.getTicker(pair, connection)
            liqui_client.getTicker(pair, info=info)
            liqui_client.getTicker(pair)

    def test_getHistory(self):
        connection = liqui_client.BTCEConnection()
        info = liqui_client.APIInfo(connection)
        for pair in info.pair_names:
            liqui_client.getTradeHistory(pair, connection, info)
            liqui_client.getTradeHistory(pair, connection)
            liqui_client.getTradeHistory(pair, info=info)
            liqui_client.getTradeHistory(pair)

    def test_getDepth(self):
        connection = liqui_client.BTCEConnection()
        info = liqui_client.APIInfo(connection)
        for pair in info.pair_names:
            liqui_client.getDepth(pair, connection, info)
            liqui_client.getDepth(pair, connection)
            liqui_client.getDepth(pair, info=info)
            liqui_client.getDepth(pair)


if __name__ == '__main__':
    unittest.main()
