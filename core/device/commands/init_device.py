"""
InitDevice: order (data) and handler. Handler publishes DeviceInitialized via EventPublisher.
"""

from core.device.events import DeviceInitialized


class InitDeviceOrder:
    """Order to initialize the device (first boot or already configured). No parameters for now."""
    pass


class InitDeviceCommandHandler:
    """Handles InitDeviceOrder: loads or generates device id, persists, publishes DeviceInitialized."""

    def __init__(self, dependencies):
        self._dependencies = dependencies

    def handle(self, order):
        """Execute the init device logic. Publishes event; returns None."""
        if not isinstance(order, InitDeviceOrder):
            return
        existing_id = self._dependencies.config_gateway.get_device_id()
        if existing_id is not None:
            self._dependencies.event_publisher.publish(DeviceInitialized(device_id=existing_id))
            return
        device_id = self._dependencies.device_id_generator.generate()
        self._dependencies.config_gateway.save_device_id(device_id)
        self._dependencies.event_publisher.publish(DeviceInitialized(device_id=device_id))
