
from typing import Any, Dict

class CryptoIntegrationError(Exception):
    """Base exception for all crypto integration errors."""
    pass

class ExchangeBase:
    """
    Abstract base class for all exchange integrations.
    Methods should be implemented by subclasses for specific exchanges.
    """
    def buy(self, symbol: str, amount: float) -> Dict[str, Any]:
        """Place a buy order for a given symbol and amount."""
        raise NotImplementedError("Buy method must be implemented by the exchange subclass.")

    def sell(self, symbol: str, amount: float) -> Dict[str, Any]:
        """Place a sell order for a given symbol and amount."""
        raise NotImplementedError("Sell method must be implemented by the exchange subclass.")

    def get_balance(self) -> Dict[str, Any]:
        """Retrieve account balances from the exchange."""
        raise NotImplementedError("get_balance method must be implemented by the exchange subclass.")

class MerchantBase:
    """
    Abstract base class for all merchant integrations.
    Methods should be implemented by subclasses for specific merchants.
    """
    def create_invoice(self, amount: float, currency: str) -> Dict[str, Any]:
        """Create an invoice for a given amount and currency."""
        raise NotImplementedError("create_invoice method must be implemented by the merchant subclass.")

    def check_payment(self, invoice_id: str) -> Dict[str, Any]:
        """Check the payment status of a given invoice."""
        raise NotImplementedError("check_payment method must be implemented by the merchant subclass.")
