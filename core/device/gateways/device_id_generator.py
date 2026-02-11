"""
DeviceIdGenerator interface: contract for generating a new device id.
Implementations are injected at composition root (e.g. in main.py).
"""


class DeviceIdGenerator:
    """Interface: generate() returns a new device id (str). No implementation in core."""

    def generate(self):
        """Return a new device id. Override in implementations."""
        raise NotImplementedError
