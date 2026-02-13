"""
Tests for InitDeviceCommandHandler. Uses FakeConfigGateway, FakeDeviceIdGenerator, FakeEventPublisher; no ESP32 required.
"""

import unittest

from core.gateways.infra import FakeEventPublisher
from core.device.gateways.infra import FakeConfigGateway, FakeDeviceIdGenerator
from core.device.commands import InitDeviceOrder, InitDeviceCommandHandler
from core.device.events import DeviceInitialized


class InitDeviceCommandHandlerTest(unittest.TestCase):
    def test_handle_when_device_id_exists_publishes_device_initialized_with_existing_id(self):
        existing_id = "existing-id"
        config_gateway = FakeConfigGateway(device_id=existing_id)
        device_id_generator = FakeDeviceIdGenerator("ignored")
        event_publisher = FakeEventPublisher()
        handler = InitDeviceCommandHandler(config_gateway, device_id_generator, event_publisher)
        handler.handle(InitDeviceOrder())
        self.assertEqual(len(event_publisher.published_events), 1)
        self.assertIsInstance(event_publisher.published_events[0], DeviceInitialized)
        self.assertEqual(event_publisher.published_events[0].device_id, existing_id)

    def test_handle_when_no_device_id_generates_saves_and_publishes_device_initialized(self):
        device_id = "new-generated-id"
        config_gateway = FakeConfigGateway(device_id=None)
        device_id_generator = FakeDeviceIdGenerator(generated_device_id=device_id)
        event_publisher = FakeEventPublisher()
        handler = InitDeviceCommandHandler(config_gateway, device_id_generator, event_publisher)
        handler.handle(InitDeviceOrder())
        self.assertEqual(config_gateway.get_device_id(), device_id)
        self.assertEqual(len(event_publisher.published_events), 1)
        self.assertIsInstance(event_publisher.published_events[0], DeviceInitialized)
        self.assertEqual(event_publisher.published_events[0].device_id, device_id_generator.generated_device_id)


if __name__ == "__main__":
    unittest.main()
