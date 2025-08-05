from ..base import MerchantBase
from ..settings import Settings

class PlisioMerchant(MerchantBase):
    """Plisio merchant integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_merchant_url('plisio')
        self.api_key = self.settings.get_api_key('plisio', kind='merchants')

    def create_invoice(self, amount, currency):
        """Create an invoice on Plisio."""
        pass

    def check_payment(self, invoice_id):
        """Check payment status on Plisio."""
        pass
