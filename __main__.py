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


def test_alpha_vantage():
    from alpha_vantage.timeseries import TimeSeries
    ts = TimeSeries(key='a9415a45ecmsh5c128ed267b8247p14a714jsn54357e5a2229', rapidapi=True, output_format="pandas")
    print(ts.get_intraday(symbol='AAPL'))


def test_iex():
    from iex import reference
    print(reference.symbols())  # Returns a Pandas Dataframe of all stock symbols, names, and more.
    from iex import Stock
    print(Stock("F").price())
    print(Stock("F").chart_table(range="1y"))


def test_pyex():
    import pyEX
    c = pyEX.Client("Tpk_26beda9610f64924923f07dd74fae86b", version="sandbox")
    print(c.symbolsDF().head())
