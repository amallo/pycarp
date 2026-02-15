"""
SimpleEventPublisher: in-memory implementation of EventPublisher. Subscribe handlers, publish(event) runs them.
"""

from core.gateways.event_publisher import EventPublisher


class SimpleEventPublisher(EventPublisher):
    """In-memory: runs registered event handlers only. Register e.g. event_applier.apply to update state."""

    def __init__(self):
        self._handlers = {}  # event_type -> list of callables

    def subscribe(self, event_type, handler):
        """Register handler(event) for this event type."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def publish(self, event):
        if event is None:
            return
        event_type = type(event)
        for h in self._handlers.get(event_type, []):
            h(event)
