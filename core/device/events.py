"""
Device domain events. Commands return these; core state is updated via apply(event).
"""


class DeviceInitialized:
    """Emitted when the device has been initialized on first boot."""

    def __init__(self, device_id):
        self.device_id = device_id
