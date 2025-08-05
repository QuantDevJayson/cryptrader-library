
import json
import os
from typing import Any, Optional

class Settings:
    def reload(self) -> None:
        """Reload the settings from the JSON file at runtime."""
        self.data = self._load()

    def list_exchanges(self) -> list[str]:
        """Return a list of all available exchange names."""
        return list(self.data.get('exchanges', {}).keys())

    def list_merchants(self) -> list[str]:
        """Return a list of all available merchant names."""
        return list(self.data.get('merchants', {}).keys())
    """
    Loads API URLs and credentials from a settings file.
    Provides helper methods to retrieve exchange and merchant configuration.
    """
    def __init__(self, path: str = 'settings.json') -> None:
        self.path = path
        self.data = self._load()

    def _load(self) -> dict:
        """Load settings from the JSON file."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Settings file not found: {self.path}")
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in settings file: {e}")

    def get_exchange_url(self, name: str) -> Optional[str]:
        """Get the API URL for a given exchange name."""
        return self.data.get('exchanges', {}).get(name, {}).get('url')

    def get_merchant_url(self, name: str) -> Optional[str]:
        """Get the API URL for a given merchant name."""
        return self.data.get('merchants', {}).get(name, {}).get('url')

    def get_api_key(self, name: str, kind: str = 'exchanges') -> Optional[str]:
        """Get the API key for a given exchange or merchant name."""
        return self.data.get(kind, {}).get(name, {}).get('api_key')
