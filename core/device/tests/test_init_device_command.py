"""
Tests for InitDeviceCommandHandler. BDD style (Given/When/Then). No ESP32 required.
"""

import unittest

from core.gateways.infra import FakeEventPublisher
from core.device.gateways.infra import FakeConfigGateway, FakeDeviceIdGenerator
from core.device.commands import InitDeviceOrder
from core.device.tests.helpers import (
    TestDependencies,
    build_init_device_command_bus,
    assert_one_device_initialized,
)


class InitDeviceCommandHandlerTest(unittest.TestCase):
    def test_given_existing_device_id_when_init_device_then_publishes_with_that_id(self):
        # Given: dependencies with existing device id
        deps = TestDependencies(
            config_gateway=FakeConfigGateway(device_id="existing-id"),
            device_id_generator=FakeDeviceIdGenerator("ignored"),
            event_publisher=FakeEventPublisher(),
        )
        command_bus = build_init_device_command_bus(deps)
        # When
        command_bus.dispatch(InitDeviceOrder())
        # Then
        assert_one_device_initialized(self, deps.event_publisher, "existing-id")

    def test_given_no_device_id_when_init_device_then_generates_saves_and_publishes(self):
        # Given: no device id; generator returns "new-generated-id"
        deps = TestDependencies(
            config_gateway=FakeConfigGateway(device_id=None),
            device_id_generator=FakeDeviceIdGenerator(generated_device_id="new-generated-id"),
            event_publisher=FakeEventPublisher(),
        )
        command_bus = build_init_device_command_bus(deps)
        # When
        command_bus.dispatch(InitDeviceOrder())
        # Then
        self.assertEqual(deps.config_gateway.get_device_id(), "new-generated-id")
        assert_one_device_initialized(self, deps.event_publisher, "new-generated-id")


if __name__ == "__main__":
    unittest.main()
