"""
FakeDeviceIdGenerator: test double for DeviceIdGenerator.
Returns a fixed value for deterministic tests.
"""

from core.device.gateways.device_id_generator import DeviceIdGenerator


class FakeDeviceIdGenerator(DeviceIdGenerator):
    """Test double that returns a configurable fixed device id."""

    def __init__(self, value="generated-device-id"):
        self.value = value

    def generate(self):
        return self.value
