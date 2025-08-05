import pytest
from cryptrader.base import ExchangeBase, MerchantBase

class DummyExchange(ExchangeBase):
    pass

class DummyMerchant(MerchantBase):
    pass

def test_exchange_base_methods():
    ex = DummyExchange()
    with pytest.raises(NotImplementedError):
        ex.buy('BTC', 1)
    with pytest.raises(NotImplementedError):
        ex.sell('BTC', 1)
    with pytest.raises(NotImplementedError):
        ex.get_balance()

def test_merchant_base_methods():
    m = DummyMerchant()
    with pytest.raises(NotImplementedError):
        m.create_invoice(1, 'BTC')
    with pytest.raises(NotImplementedError):
        m.check_payment('inv123')
