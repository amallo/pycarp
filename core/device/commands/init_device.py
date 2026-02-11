"""
InitDevice command: initialize the device on first startup.
Uses ConfigGateway and DeviceIdGenerator; returns a DeviceInitialized event.
"""

from core.device.events import DeviceInitialized


class InitDeviceCommand:
    """Command to run on first boot or when already configured: persist or reuse device id, return DeviceInitialized."""

    def __init__(self, config_gateway, device_id_generator):
        self._config = config_gateway
        self._device_id_generator = device_id_generator

    def execute(self):
        """Return a DeviceInitialized event (same state INITIALIZED for first boot or already configured)."""
        existing_id = self._config.get_device_id()
        if existing_id is not None:
            return DeviceInitialized(device_id=existing_id)
        device_id = self._device_id_generator.generate()
        self._config.save_device_id(device_id)
        return DeviceInitialized(device_id=device_id)
