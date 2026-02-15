"""
ESP32 implementation of DeviceIdGenerator. Generates unique id as "carpe-" + hex from machine.unique_id().
Use at composition root (main.py) on device; not imported in tests.
"""

import binascii
import machine

from core.device.gateways.device_id_generator import DeviceIdGenerator

PREFIX = "carpe-"
DEFAULT_HEX_BYTES = 4  # 4 bytes -> 8 hex chars


class ESP32DeviceIdGenerator(DeviceIdGenerator):
    """Generates device id as carpe-<hex> from machine.unique_id() (e.g. MAC). hex_bytes controls length (default 4 -> 8 hex chars)."""

    def __init__(self, hex_bytes=DEFAULT_HEX_BYTES):
        self._hex_bytes = min(hex_bytes, 6)  # cap at 6 (MAC length)

    def generate(self):
        uid = machine.unique_id()
        hex_part = binascii.hexlify(uid[: self._hex_bytes]).decode("utf-8")
        return PREFIX + hex_part
