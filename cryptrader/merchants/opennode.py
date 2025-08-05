from ..base import MerchantBase
from ..settings import Settings

class OpenNodeMerchant(MerchantBase):
    """OpenNode merchant integration stub."""
    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self.url = self.settings.get_merchant_url('opennode')
        self.api_key = self.settings.get_api_key('opennode', kind='merchants')

    def create_invoice(self, amount, currency):
        """Create an invoice on OpenNode."""
        pass

    def check_payment(self, invoice_id):
        """Check payment status on OpenNode."""
        pass
