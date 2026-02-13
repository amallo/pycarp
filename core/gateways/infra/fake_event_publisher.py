"""
FakeEventPublisher: test double for EventPublisher (infra of core module).
Records published events and applies them to app_state for state assertions.
"""

from core.gateways.event_publisher import EventPublisher
from core.state import app_state


class FakeEventPublisher(EventPublisher):
    """Records published events; applies to app_state so tests can assert on state."""

    def __init__(self):
        self.published_events = []

    def publish(self, event):
        if event is not None:
            self.published_events.append(event)
            app_state.apply(event)
