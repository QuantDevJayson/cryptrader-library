from ..base import MerchantBase

class BitPayMerchant(MerchantBase):
    def create_invoice(self, amount, currency):
        # Implement BitPay invoice creation logic
        pass

    def check_payment(self, invoice_id):
        # Implement BitPay payment check logic
        pass
