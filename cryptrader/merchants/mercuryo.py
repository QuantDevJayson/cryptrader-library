from ..base import MerchantBase
from ..settings import Settings

class MercuryoMerchant(MerchantBase):
    """Mercuryo merchant integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_merchant_url('mercuryo')
        self.api_key = self.settings.get_api_key('mercuryo', kind='merchants')

    def create_invoice(self, amount, currency):
        pass
    def check_payment(self, invoice_id):
        pass
