"""
ConfigGateway port: interface for persisting device config (e.g. device id, initialized flag).
Concrete implementations are injected at composition root (e.g. in main.py).
"""


class ConfigGateway:
    """Port for reading/writing device configuration. Implementations are injected at composition root."""

    def save_device_id(self, device_id):
        """Persist the device id. Override in implementations."""
        raise NotImplementedError

    def mark_initialized(self):
        """Mark the device as initialized (first boot done). Override in implementations."""
        raise NotImplementedError
