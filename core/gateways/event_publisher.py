"""
EventPublisher port: publish(event). Implementations run handlers or forward to a bus.
"""


class EventPublisher:
    """Port: publish an event."""

    def publish(self, event):
        raise NotImplementedError
