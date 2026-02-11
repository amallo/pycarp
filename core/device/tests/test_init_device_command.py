"""
Test for InitDeviceCommand: runnable on macOS with pytest or unittest.
Uses FakeConfigGateway and FakeDeviceIdGenerator; no ESP32 required.
"""

import unittest

from core.device.commands.init_device import InitDeviceCommand
from core.device.events import DeviceInitialized
from core.device.tests.fake_config_gateway import FakeConfigGateway
from core.device.tests.fake_device_id_generator import FakeDeviceIdGenerator
from core.state import app_state, INITIALIZED


class TestInitDeviceCommand(unittest.TestCase):
    def tearDown(self):
        app_state.reset()

    def test_first_boot_device(self):
        generated_id = "generated-device-id"
        config_gateway = FakeConfigGateway()
        device_id_generator = FakeDeviceIdGenerator(value=generated_id)
        command = InitDeviceCommand(config_gateway, device_id_generator)

        result = command.execute()

        self.assertEqual(config_gateway.saved_device_id, generated_id)
        self.assertIsInstance(result, DeviceInitialized)
        self.assertEqual(result.device_id, generated_id)
        app_state.apply(result)
        self.assertEqual(app_state.device_state, INITIALIZED)

    def test_boot_already_configured_device(self):
        already_configured_id = "already-configured"
        config_gateway = FakeConfigGateway()
        config_gateway.saved_device_id = already_configured_id
        device_id_generator = FakeDeviceIdGenerator()
        command = InitDeviceCommand(config_gateway, device_id_generator)

        result = command.execute()

        self.assertIsInstance(result, DeviceInitialized)
        self.assertEqual(result.device_id, already_configured_id)
        self.assertEqual(config_gateway.saved_device_id, already_configured_id)
        app_state.apply(result)
        self.assertEqual(app_state.device_state, INITIALIZED)


if __name__ == "__main__":
    unittest.main()
