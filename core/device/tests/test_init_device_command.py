"""
Test for InitDeviceCommand: runnable on macOS with pytest or unittest.
Uses FakeConfigGateway; no ESP32 required.
"""

import unittest

from core.device.commands.init_device import InitDeviceCommand, DEFAULT_DEVICE_ID
from core.device.tests.fake_config_gateway import FakeConfigGateway


class TestInitDeviceCommand(unittest.TestCase):
    def test_execute_persists_device_id_and_marks_initialized(self):
        fake = FakeConfigGateway()
        command = InitDeviceCommand(fake)

        command.execute()

        self.assertEqual(fake.saved_device_id, DEFAULT_DEVICE_ID)
        self.assertTrue(fake.mark_initialized_called)


if __name__ == "__main__":
    unittest.main()
