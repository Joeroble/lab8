import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin_lab8

class TestBitcoinLab8(TestCase):

    @patch('requests.Response.json')
    def test_get_bitcoin_current_price(self, mock_request_json):
        mock_current_price = 24556
        example_api_response = {"time":{"updated":"Oct 27, 2022 22:51:00 UTC",
        "updatedISO":"2022-10-27T22:51:00+00:00","updateduk":"Oct 27, 2022 at 23:51 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin","bpi":
        {"USD":{"code":"USD","symbol":"&#36;","rate":"20,274.6703","description":"United States Dollar","rate_float":mock_current_price},
        "GBP":{"code":"GBP","symbol":"&pound;","rate":"16,941.3523","description":"British Pound Sterling","rate_float":16941.3523},
        "EUR":{"code":"EUR","symbol":"&euro;","rate":"19,750.4890","description":"Euro","rate_float":19750.489}}}
        mock_request_json = example_api_response
        converted_bitcoin_to_usd = bitcoin_lab8.get_bitcoin_value_in_dollars(123, mock_request_json)
        expected = 3020388
        self.assertEqual(expected, converted_bitcoin_to_usd)


if __name__ == '__main__':
    unittest.main()