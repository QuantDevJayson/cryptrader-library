from cryptrader.settings import Settings
import pytest
import os

def test_settings_loads():
    s = Settings('settings.json')
    assert s.get_exchange_url('binance') == 'https://api.binance.com'
    assert s.get_merchant_url('bitpay') == 'https://bitpay.com/api'
    assert s.get_api_key('kraken') == 'YOUR_KRAKEN_KEY'
    assert s.get_api_key('coingate', kind='merchants') == 'YOUR_COINGATE_KEY'

def test_settings_file_not_found():
    with pytest.raises(FileNotFoundError):
        Settings('nonexistent.json')
