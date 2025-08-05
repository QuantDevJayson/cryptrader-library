from ..base import ExchangeBase
from ..settings import Settings

class ProbitExchange(ExchangeBase):
    """Probit exchange integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_exchange_url('probit')
        self.api_key = self.settings.get_api_key('probit')

    def buy(self, symbol, amount):
        pass
    def sell(self, symbol, amount):
        pass
    def get_balance(self):
        pass
