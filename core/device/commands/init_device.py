"""
InitDevice: order (data) and handler. Handler publishes DeviceInitialized via EventPublisher.
"""

from core.device.events import DeviceInitialized


class InitDeviceOrder:
    """Order to initialize the device (first boot or already configured). No parameters for now."""
    pass


class InitDeviceCommandHandler:
    """Handles InitDeviceOrder: loads or generates device id, persists, publishes DeviceInitialized."""

    def __init__(self, config_gateway, device_id_generator, event_publisher):
        self._config = config_gateway
        self._device_id_generator = device_id_generator
        self._event_publisher = event_publisher

    def handle(self, order):
        """Execute the init device logic. Publishes event; returns None."""
        if not isinstance(order, InitDeviceOrder):
            return
        existing_id = self._config.get_device_id()
        if existing_id is not None:
            self._event_publisher.publish(DeviceInitialized(device_id=existing_id))
            return
        device_id = self._device_id_generator.generate()
        self._config.save_device_id(device_id)
        self._event_publisher.publish(DeviceInitialized(device_id=device_id))
