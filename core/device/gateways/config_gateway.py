"""
ConfigGateway port: interface for persisting device config (e.g. device id).
Concrete implementations are injected at composition root (e.g. in main.py).
"""


class ConfigGateway:
    """Port for reading/writing device configuration. Implementations are injected at composition root."""

    def get_device_id(self):
        """Return the persisted device id, or None if not yet configured. Override in implementations."""
        raise NotImplementedError

    def save_device_id(self, device_id):
        """Persist the device id. Override in implementations."""
        raise NotImplementedError
