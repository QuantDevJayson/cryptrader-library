from ..base import MerchantBase
from ..settings import Settings

class CoinPaymentsMerchant(MerchantBase):
    """CoinPayments merchant integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_merchant_url('coinpayments')
        self.api_key = self.settings.get_api_key('coinpayments', kind='merchants')

    def create_invoice(self, amount, currency):
        """Create an invoice on CoinPayments."""
        pass

    def check_payment(self, invoice_id):
        """Check payment status on CoinPayments."""
        pass
