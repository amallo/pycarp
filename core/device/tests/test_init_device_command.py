"""
Test for InitDeviceCommand: runnable on macOS with pytest or unittest.
Uses FakeConfigGateway; no ESP32 required.
"""

import unittest

from core.device.commands.init_device import InitDeviceCommand, DEFAULT_DEVICE_ID
from core.device.events import DeviceInitialized
from core.device.tests.fake_config_gateway import FakeConfigGateway
from core.state import app_state, INITIALIZED


class TestInitDeviceCommand(unittest.TestCase):
    def tearDown(self):
        app_state.reset()

    def test_first_boot_device(self):
        configGateway = FakeConfigGateway()
        command = InitDeviceCommand(configGateway)

        result = command.execute()
        

        self.assertEqual(configGateway.saved_device_id, DEFAULT_DEVICE_ID)
        self.assertIsInstance(result, DeviceInitialized)
        self.assertEqual(result.device_id, DEFAULT_DEVICE_ID)
        app_state.apply(result)

        self.assertEqual(app_state.device_state, INITIALIZED)

    def test_boot_already_configured_device(self):
        already_configured_id = "already-configured"
        configGateway = FakeConfigGateway()
        configGateway.saved_device_id = already_configured_id
        command = InitDeviceCommand(configGateway)

        result = command.execute()

        self.assertIsInstance(result, DeviceInitialized)
        self.assertEqual(result.device_id, already_configured_id)
        self.assertEqual(configGateway.saved_device_id, already_configured_id)
        app_state.apply(result)
        self.assertEqual(app_state.device_state, INITIALIZED)


if __name__ == "__main__":
    unittest.main()
