"""
Fake ConfigGateway for tests. Records calls for assertions (runnable on macOS, no ESP32).
"""

from core.device.gateways.config_gateway import ConfigGateway


class FakeConfigGateway(ConfigGateway):
    """In-memory config. get_device_id returns _device_id (set to None or a value); save_device_id stores it."""

    def __init__(self, device_id=None):
        self._device_id = device_id

    def get_device_id(self):
        return self._device_id

    def save_device_id(self, device_id):
        self._device_id = device_id
