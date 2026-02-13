"""
EventPublisher port: publish an event (side effect). No return.
Implementations can apply to app_state or publish to an event bus.
"""


class EventPublisher:
    """Port: publish an event. Implementations apply to state or publish to an event bus."""

    def publish(self, event):
        raise NotImplementedError


class ApplyToAppStatePublisher(EventPublisher):
    """Publishes by applying the event to app_state. Use until you have an event bus."""

    def __init__(self, state=None):
        if state is None:
            from core.state import app_state
            state = app_state
        self._state = state

    def publish(self, event):
        if event is not None:
            self._state.apply(event)


class SimpleEventPublisher(ApplyToAppStatePublisher):
    """In-memory event publisher for production (applies events to app_state). Same behavior as ApplyToAppStatePublisher."""

    pass
