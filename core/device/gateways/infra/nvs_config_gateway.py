"""
NVS implementation of ConfigGateway for ESP32 (MicroPython). Persists device_id in esp32.NVS.
Use at composition root (main.py) on device; not imported in tests.
"""

import esp32

from core.device.gateways.config_gateway import ConfigGateway

# NVS key and max device_id length (blob size for get_blob buffer)
DEVICE_ID_KEY = "device_id"
DEVICE_ID_MAX_LEN = 64


class NVSConfigGateway(ConfigGateway):
    """Persists device_id in ESP32 NVS (non-volatile storage). Namespace and key are configurable."""

    def __init__(self, namespace="pycarpe", key=DEVICE_ID_KEY):
        self._nvs = esp32.NVS(namespace)
        self._key = key

    def get_device_id(self):
        """Return the persisted device id, or None if not yet configured or on read error."""
        try:
            buf = bytearray(DEVICE_ID_MAX_LEN)
            length = self._nvs.get_blob(self._key, buf)
            return buf[:length].decode("utf-8")
        except OSError:
            return None

    def save_device_id(self, device_id):
        """Persist the device id to NVS and commit to flash."""
        self._nvs.set_blob(self._key, device_id.encode("utf-8"))
        self._nvs.commit()
