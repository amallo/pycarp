"""
Command bus port: dispatch(order) routes to the registered handler.
"""


class CommandBus:
    """Port: dispatch(order) routes to the registered handler. No return value."""

    def dispatch(self, order):
        raise NotImplementedError
