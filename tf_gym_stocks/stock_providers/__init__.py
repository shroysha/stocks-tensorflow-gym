class StockProvider:

    def get_pd_dataframe(self):
        raise NotImplementedError("Must implement")


class GoogleStockProvider(StockProvider):

    def get_pd_dataframe(self):
        pass


class YahooStockProvider(StockProvider):

    def get_pd_dataframe(self):
        pass
