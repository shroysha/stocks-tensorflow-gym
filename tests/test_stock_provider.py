import json

from googlefinance import getQuotes
from yahoo_finance import Share


def test_yahoo():
    yahoo = Share('YHOO')
    print(yahoo.get_open())
    print(yahoo.get_price())
    print(yahoo.get_trade_datetime())
    # Refresh data from market

    yahoo.refresh()
    print(yahoo.get_price())
    print(yahoo.get_trade_datetime())
    # Historical data
    print(yahoo.get_historical('2014-04-25', '2014-04-29'))


def test_google():
    print(json.dumps(getQuotes('AAPL'), indent=2))
