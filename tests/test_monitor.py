from cryptrader.monitor import AlertMonitor
import time

def test_alert_monitor_triggers(monkeypatch):
    triggered = []
    def fake_get(url, timeout):
        class Resp:
            status_code = 500
        return Resp()
    monkeypatch.setattr('requests.get', fake_get)
    def alert_cb(msg):
        triggered.append(msg)
    monitor = AlertMonitor({'test':'http://fakeurl'}, check_interval=1, alert_callback=alert_cb)
    monitor.start()
    time.sleep(2)
    monitor.stop()
    assert any('API returned status' in m for m in triggered)
