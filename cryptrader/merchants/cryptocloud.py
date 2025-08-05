from .base import MerchantBase

class CryptocloudMerchant(MerchantBase):
    """Integration for Cryptocloud merchant API."""
    def __init__(self, settings=None):
        super().__init__(settings)
        self.api_url = settings.get('url') if settings else None
        self.api_key = settings.get('api_key') if settings else None

    def create_invoice(self, amount, currency):
        # Implement invoice creation logic for Cryptocloud
        raise NotImplementedError("Cryptocloud invoice creation not implemented.")

    def check_payment(self, invoice_id):
        # Implement payment check logic for Cryptocloud
        raise NotImplementedError("Cryptocloud payment check not implemented.")
