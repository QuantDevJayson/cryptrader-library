from ..base import MerchantBase
from ..settings import Settings
import requests

class CoinGateMerchant(MerchantBase):
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_merchant_url('coingate')
        self.api_key = self.settings.get_api_key('coingate', kind='merchants')

    def create_invoice(self, amount, currency):
        # Implement CoinGate invoice creation logic
        pass

    def check_payment(self, invoice_id):
        # Implement CoinGate payment check logic
        pass
