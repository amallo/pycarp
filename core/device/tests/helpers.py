"""
Shared test helpers for device module. Dependencies are passed in; helpers wire and return bus or assert.
"""

from core.gateways.infra import FakeCommandBus
from core.device.dependencies import Dependencies
from core.device.commands import InitDeviceOrder, InitDeviceCommandHandler
from core.device.events import DeviceInitialized


class TestDependencies(Dependencies):
    """Test double: holds fakes; exposes config_gateway, device_id_generator, event_publisher."""

    def __init__(self, config_gateway, device_id_generator, event_publisher):
        self._config_gateway = config_gateway
        self._device_id_generator = device_id_generator
        self._event_publisher = event_publisher

    @property
    def config_gateway(self):
        return self._config_gateway

    @property
    def device_id_generator(self):
        return self._device_id_generator

    @property
    def event_publisher(self):
        return self._event_publisher


def build_init_device_command_bus(dependencies):
    """Given dependencies, return a command_bus with InitDeviceOrder -> handler registered."""
    handler = InitDeviceCommandHandler(dependencies)
    command_bus = FakeCommandBus()
    command_bus.register(InitDeviceOrder, handler)
    return command_bus


def assert_one_device_initialized(test_case, event_publisher, expected_device_id):
    """Then: exactly one DeviceInitialized event with the given device_id."""
    test_case.assertEqual(len(event_publisher.published_events), 1)
    test_case.assertIsInstance(event_publisher.published_events[0], DeviceInitialized)
    test_case.assertEqual(event_publisher.published_events[0].device_id, expected_device_id)
