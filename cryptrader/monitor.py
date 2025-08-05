

import asyncio
import aiohttp
from typing import Callable, Dict, Optional, Awaitable


class AlertMonitor:
    """
    Asynchronous monitor for a set of API URLs, triggers alerts on failures or downtime.
    Uses asyncio and aiohttp for high-performance, parallel monitoring.
    """
    def __init__(
        self,
        urls: Dict[str, str],
        check_interval: int = 60,
        alert_callback: Optional[Callable[[str], Awaitable[None]]] = None,
        ssl_verify: bool = True
    ) -> None:
        self.urls = urls
        self.check_interval = check_interval
        self.alert_callback = alert_callback
        self.ssl_verify = ssl_verify
        self._stop_event = asyncio.Event()

    async def start(self) -> None:
        """Start monitoring asynchronously."""
        self._stop_event.clear()
        await self._monitor()

    def stop(self) -> None:
        """Signal the monitor to stop."""
        self._stop_event.set()

    async def _monitor(self) -> None:
        """Internal async loop to check all URLs and trigger alerts if needed."""
        async with aiohttp.ClientSession() as session:
            while not self._stop_event.is_set():
                tasks = [self._check_url(session, name, url) for name, url in self.urls.items()]
                await asyncio.gather(*tasks)
                try:
                    await asyncio.wait_for(self._stop_event.wait(), timeout=self.check_interval)
                except asyncio.TimeoutError:
                    continue

    async def _check_url(self, session: aiohttp.ClientSession, name: str, url: str) -> None:
        try:
            async with session.get(url, ssl=self.ssl_verify, timeout=10) as resp:
                if resp.status != 200:
                    await self._alert(f"{name} API returned status {resp.status}")
        except Exception as e:
            await self._alert(f"{name} API unreachable: {e}")

    async def _alert(self, message: str) -> None:
        """Trigger an alert with the given message asynchronously."""
        if self.alert_callback:
            await self.alert_callback(message)
        else:
            print(f"[ALERT] {message}")
