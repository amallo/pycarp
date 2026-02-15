"""
FakeCommandBus: test double for CommandBus. Routes orders to registered handlers; records dispatched orders.
"""

from core.gateways.command_bus import CommandBus


class FakeCommandBus(CommandBus):
    """Register handlers; dispatch(order) routes to handler and appends order to dispatched_orders."""

    def __init__(self):
        self._handlers = {}
        self.dispatched_orders = []

    def register(self, order_type, handler):
        """Register a handler for an order type. Handler must have handle(order)."""
        self._handlers[order_type] = handler

    def dispatch(self, order):
        handler = self._handlers.get(type(order))
        if handler is None:
            return
        self.dispatched_orders.append(order)
        handler.handle(order)
