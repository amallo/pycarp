"""
FakeConfigGateway: in-memory test double for ConfigGateway.
Records calls for assertions in tests (runnable on macOS, no ESP32).
"""

from core.device.gateways.config_gateway import ConfigGateway


class FakeConfigGateway(ConfigGateway):
    """Test double that records save_device_id calls."""

    def __init__(self):
        self.saved_device_id = None

    def get_device_id(self):
        return self.saved_device_id

    def save_device_id(self, device_id):
        self.saved_device_id = device_id
