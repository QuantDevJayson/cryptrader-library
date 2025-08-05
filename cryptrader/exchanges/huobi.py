from ..base import ExchangeBase
from ..settings import Settings

class HuobiExchange(ExchangeBase):
    """Huobi exchange integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_exchange_url('huobi')
        self.api_key = self.settings.get_api_key('huobi')

    def buy(self, symbol, amount):
        pass
    def sell(self, symbol, amount):
        pass
    def get_balance(self):
        pass
