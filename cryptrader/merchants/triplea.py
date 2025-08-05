from .base import MerchantBase

class TripleaMerchant(MerchantBase):
    """Integration for TripleA merchant API."""
    def __init__(self, settings=None):
        super().__init__(settings)
        self.api_url = settings.get('url') if settings else None
        self.api_key = settings.get('api_key') if settings else None

    def create_invoice(self, amount, currency):
        # Implement invoice creation logic for TripleA
        raise NotImplementedError("TripleA invoice creation not implemented.")

    def check_payment(self, invoice_id):
        # Implement payment check logic for TripleA
        raise NotImplementedError("TripleA payment check not implemented.")
