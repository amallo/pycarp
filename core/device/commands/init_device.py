"""
InitDevice command: initialize the device on first startup.
Uses ConfigGateway to persist device id and mark as initialized.
Returns a DeviceInitialized event on success.
"""

from core.device.events import DeviceInitialized

# Hardcoded for now; will be injected at composition root later.
DEFAULT_DEVICE_ID = "device-initialized-001"


class InitDeviceCommand:
    """Command to run on first boot: persist device id and mark device as initialized."""

    def __init__(self, config_gateway):
        self._config = config_gateway

    def execute(self):
        """Persist default device id and mark device as initialized. Returns DeviceInitialized event."""
        self._config.save_device_id(DEFAULT_DEVICE_ID)
        self._config.mark_initialized()
        return DeviceInitialized(device_id=DEFAULT_DEVICE_ID)
