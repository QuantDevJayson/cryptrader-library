from .base import MerchantBase

class PaykassaMerchant(MerchantBase):
    """Integration for Paykassa merchant API."""
    def __init__(self, settings=None):
        super().__init__(settings)
        self.api_url = settings.get('url') if settings else None
        self.api_key = settings.get('api_key') if settings else None

    def create_invoice(self, amount, currency):
        # Implement invoice creation logic for Paykassa
        raise NotImplementedError("Paykassa invoice creation not implemented.")

    def check_payment(self, invoice_id):
        # Implement payment check logic for Paykassa
        raise NotImplementedError("Paykassa payment check not implemented.")
