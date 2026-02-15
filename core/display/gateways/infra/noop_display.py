"""
NoOpDisplay: no-op implementation of Display for headless or tests.
"""

from core.display.gateways.display import Display


class NoOpDisplay(Display):
    """No-op implementation for headless or tests."""

    def show_stage(self, label):
        pass

    def show_ready(self):
        pass

    def show_error(self, msg):
        pass

    def clear(self):
        pass
