from cryptrader.analytics import ExchangeAnalytics
from cryptrader.settings import Settings

settings = Settings('settings.json')
analytics = ExchangeAnalytics(settings)

def test_check_liquidity():
    result = analytics.check_liquidity('binance', 'BTC')
    assert 'liquidity' in result
    assert 'risk' in result

def test_check_compliance():
    result = analytics.check_compliance('binance')
    assert 'compliance' in result

def test_get_breach_insights():
    result = analytics.get_breach_insights('binance')
    assert 'breach' in result
    assert 'sentiment' in result

def test_get_arbitrage_opportunities():
    result = analytics.get_arbitrage_opportunities('BTC')
    assert isinstance(result, list)

def test_get_liquidity_updates():
    result = analytics.get_liquidity_updates()
    assert isinstance(result, list)

def test_get_fee_trends():
    result = analytics.get_fee_trends()
    assert isinstance(result, list)

def test_get_crash_alerts():
    result = analytics.get_crash_alerts()
    assert isinstance(result, list)
