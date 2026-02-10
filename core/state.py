"""
Shared application state at core root. Updated only via apply(event).
Readable by all modules (device, and future modules).
"""

# Device state constants (MicroPython-friendly, no enum dependency)
NOT_INITIALIZED = "NOT_INITIALIZED"
INITIALIZED = "INITIALIZED"


class AppState:
    """Shared state; only apply(event) mutates it."""

    def __init__(self):
        self.device_state = NOT_INITIALIZED

    def apply(self, event):
        """Update state from an event. No-op for unknown event types."""
        from core.device.events import DeviceInitialized

        if isinstance(event, DeviceInitialized):
            self.device_state = INITIALIZED

    def reset(self):
        """Reset state (for tests)."""
        self.device_state = NOT_INITIALIZED


# Shared instance for all modules
app_state = AppState()
