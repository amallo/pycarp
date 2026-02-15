"""
SimpleCommandBus: in-memory implementation of CommandBus. Register handlers, dispatch runs handler.handle(order).
"""

from core.gateways.command_bus import CommandBus


class SimpleCommandBus(CommandBus):
    """In-memory: routes by order type. Handler is responsible for publishing events."""

    def __init__(self):
        self._handlers = {}

    def register(self, order_type, handler):
        """Register a handler for an order type. Handler must have handle(order)."""
        self._handlers[order_type] = handler

    def dispatch(self, order):
        """Find handler for type(order), call handler.handle(order). Returns None."""
        handler = self._handlers.get(type(order))
        if handler is None:
            return
        handler.handle(order)
