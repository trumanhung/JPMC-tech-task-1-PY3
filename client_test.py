import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        price_verification = {"ABC": ("ABC", 120.48, 121.2, 120.84),
                              "DEF": ("DEF", 117.87, 121.68, 119.775)
                              }

        for quote in quotes:
            result = getDataPoint(quote)
            self.assertEqual(result, price_verification[result[0]])

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            self.assertRaises(ValueError, getDataPoint, quote)

    def test_getRatio_calculateRatio(self):
        ratio_verification = float(1.008891671884784)
        price_a = 120.84
        price_b = 119.775

        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, ratio_verification)

    def test_getRatio_calculateRatioZeroDenominator(self):
        price_a = 120.84
        price_b = 0

        self.assertRaises(ZeroDivisionError, getRatio, price_a, price_b)


if __name__ == '__main__':
    unittest.main()
