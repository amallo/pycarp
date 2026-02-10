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

    def test_execute_persists_device_id_and_marks_initialized(self):
        fake = FakeConfigGateway()
        command = InitDeviceCommand(fake)

        result = command.execute()

        self.assertEqual(fake.saved_device_id, DEFAULT_DEVICE_ID)
        self.assertTrue(fake.mark_initialized_called)
        self.assertIsInstance(result, DeviceInitialized)
        self.assertEqual(result.device_id, DEFAULT_DEVICE_ID)

    def test_execute_updates_shared_state_when_event_applied(self):
        fake = FakeConfigGateway()
        command = InitDeviceCommand(fake)

        result = command.execute()
        app_state.apply(result)

        self.assertEqual(app_state.device_state, INITIALIZED)


if __name__ == "__main__":
    unittest.main()
