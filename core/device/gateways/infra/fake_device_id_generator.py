"""
Fake DeviceIdGenerator for tests. Use generated_device_id to set the value returned by generate().
"""

from core.device.gateways.device_id_generator import DeviceIdGenerator


class FakeDeviceIdGenerator(DeviceIdGenerator):
    """Returns the value set in generated_device_id when generate() is called."""

    def __init__(self, generated_device_id="fake-device-id"):
        self.generated_device_id = generated_device_id

    def generate(self):
        return self.generated_device_id
